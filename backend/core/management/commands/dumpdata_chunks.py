from django.core.exceptions import ImproperlyConfigured
from django.core.management.base import BaseCommand, CommandError
from django.core import serializers
from django.db import router, DEFAULT_DB_ALIAS
from collections import OrderedDict
from django.apps import apps

from optparse import make_option

class Command(BaseCommand):
    help = ("Output the contents of the database as a fixture of the given "
            "format (using each model's default manager unless --all is "
            "specified).")
    args = '[appname appname.ModelName ...]'

    def handle(self, *app_labels, **options):

        output_folder = './dumpdata'
        print ("Output folder:", output_folder)
        print ("NOTE: See --output-folder option")
        max_records_per_chunk = 100000
        format = 'json'
        indent = None
        using = DEFAULT_DB_ALIAS
        excludes = []
        use_natural_keys = False
        use_base_manager = False

        excluded_apps = set()
        excluded_models = set()

        if len(app_labels) == 0:
            app_list = OrderedDict((app, None) for app in apps.all_models if app not in excluded_apps)
        # Check that the serialization format exists; this is a shortcut to
        # avoid collating all the objects and _then_ failing.
        if format not in serializers.get_public_serializer_formats():
            raise CommandError("Unknown serialization format: %s" % format)

        try:
            serializers.get_serializer(format)
        except KeyError:
            raise CommandError("Unknown serialization format: %s" % format)

        # Now collate the objects to be serialized.
        objects = []
        model_count = 1000
        chunk_count = 1000
        for model in sort_dependencies(app_list.items()):
            model_count += 1 
            if model in excluded_models:
                continue
            if not model._meta.proxy and router.allow_syncdb(using, model):
                if use_base_manager:
                    objects.extend(model._base_manager.using(using).all())
                else:
                    items_total = model._default_manager.using(using).count()
                    chunks_total = (items_total / max_records_per_chunk) +1
                    for chunk_num in range(0, chunks_total):
                        output_objects = model._default_manager.using(using).all().order_by('id')[chunk_num*max_records_per_chunk:(chunk_num+1)*max_records_per_chunk]
                        if output_objects:
                            chunk_count += 1 
                            dump_file_name = output_folder + "/%d_%d.json" % (model_count, chunk_count)
                            print (f"Dumping file: {dump_file_name} [{chunks_total}]")
                            output = serializers.serialize(format, output_objects, indent=indent,
                                        use_natural_keys=use_natural_keys)
                            with open(dump_file_name, "w") as dumpfile:
                                dumpfile.write(output)
        return ''

def sort_dependencies(app_list):
    """Sort a list of app,modellist pairs into a single list of models.
    The single list of models is sorted so that any model with a natural key
    is serialized before a normal model, and any model with a natural key
    dependency has it's dependencies serialized first.
    """
    # Process the list of models, and get the list of dependencies
    model_dependencies = []
    models = set()
    for app, model_list in app_list:
        if model_list is None:
            model_list = apps.all_models

        for model in model_list:
            models.add(model)
            # Add any explicitly defined dependencies
            if hasattr(model, 'natural_key'):
                deps = getattr(model.natural_key, 'dependencies', [])
                if deps:
                    deps = [apps.get_model(*d.split('.')) for d in deps]
            else:
                deps = []

            # Now add a dependency for any FK or M2M relation with
            # a model that defines a natural key
            for field in model._meta.fields:
                if hasattr(field.rel, 'to'):
                    rel_model = field.rel.to
                    if hasattr(rel_model, 'natural_key'):
                        deps.append(rel_model)
            for field in model._meta.many_to_many:
                rel_model = field.rel.to
                if hasattr(rel_model, 'natural_key'):
                    deps.append(rel_model)
            model_dependencies.append((model, deps))

    model_dependencies.reverse()
    # Now sort the models to ensure that dependencies are met. This
    # is done by repeatedly iterating over the input list of models.
    # If all the dependencies of a given model are in the final list,
    # that model is promoted to the end of the final list. This process
    # continues until the input list is empty, or we do a full iteration
    # over the input models without promoting a model to the final list.
    # If we do a full iteration without a promotion, that means there are
    # circular dependencies in the list.
    model_list = []
    while model_dependencies:
        skipped = []
        changed = False
        while model_dependencies:
            model, deps = model_dependencies.pop()

            # If all of the models in the dependency list are either already
            # on the final model list, or not on the original serialization list,
            # then we've found another model with all it's dependencies satisfied.
            found = True
            for candidate in ((d not in models or d in model_list) for d in deps):
                if not candidate:
                    found = False
            if found:
                model_list.append(model)
                changed = True
            else:
                skipped.append((model, deps))
        if not changed:
            raise CommandError("Can't resolve dependencies for %s in serialized app list." %
                ', '.join('%s.%s' % (model._meta.app_label, model._meta.object_name)
                for model, deps in sorted(skipped, key=lambda obj: obj[0].__name__))
            )
        model_dependencies = skipped

    return model_list