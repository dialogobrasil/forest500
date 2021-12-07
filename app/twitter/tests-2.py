from twitter.crawler.timeline import *
from twitter.models import *

tl = TwitterTimeline()

user_id = User.objects.all()[1].id
print(user_id)
tl.getTimeline(user_id)