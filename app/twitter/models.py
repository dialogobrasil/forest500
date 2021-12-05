from django.db import models

class API(models.Model):
    acess_token = models.CharField(max_length=100)
    acess_token_secret = models.CharField(max_length=100)
    working = models.BooleanField(null=True)

class Hashtag(models.Model):
    text = models.CharField(primary_key=True,max_length=280)

class UserMention(models.Model):
    screen_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    id = models.BigIntegerField(primary_key=True)

    def __str__(self):
        return self.screen_name

class Url(models.Model):
    url = models.URLField(primary_key=True,max_length=2048)
    expanded_url = models.URLField(blank=True,null=True,max_length=2048)
    display_url = models.URLField(blank=True,null=True,max_length=2048)

    def __str__(self):
        return self.url

class PinnedTweet(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey('User',on_delete=models.CASCADE)

class AdvertiserAccountServiceLevel(models.Model):
    advertiser_account_service_levels = models.CharField(max_length=50)
    user = models.ForeignKey('USer',on_delete=models.CASCADE)
    

class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    screen_name = models.CharField(max_length=50)
    location = models.CharField(max_length=1000)
    description = models.CharField(max_length=2048)
    urls = models.ManyToManyField(Url,related_name='urls')
    descriptionUrl = models.ManyToManyField(Url,related_name='description_url')
    protected = models.BooleanField()
    followers_count = models.BigIntegerField()
    fast_followers_count = models.BigIntegerField(blank=True,null=True)
    normal_followers_count = models.BigIntegerField(blank=True,null=True)
    friends_count = models.BigIntegerField()
    listed_count = models.BigIntegerField()
    created_at = models.DateTimeField()
    favourites_count = models.BigIntegerField()
    geo_enabled = models.BooleanField()
    verified = models.BooleanField()
    statuses_count = models.BigIntegerField()
    media_count = models.BigIntegerField(blank=True,null=True)
    lang = models.CharField(null=True,max_length=10)
    contributors_enabled = models.BooleanField()
    is_translator = models.BooleanField()
    is_translation_enabled = models.BooleanField()
    profile_background_color = models.CharField(max_length=20)
    profile_background_image_url = models.URLField(null=True,max_length=2048)
    profile_background_image_url_https = models.URLField(null=True,max_length=2048)
    profile_background_tile = models.BooleanField()
    profile_image_url = models.URLField(null=True,max_length=2048)
    profile_image_url_https = models.URLField(null=True,max_length=2048)
    profile_banner_url = models.URLField(null=True,max_length=2048)
    profile_link_color = models.CharField(max_length=20)
    profile_sidebar_border_color = models.CharField(max_length=20)
    profile_sidebar_fill_color = models.CharField(max_length=20)
    profile_text_color = models.CharField(max_length=20)
    profile_use_background_image = models.BooleanField()
    has_custom_timelines = models.BooleanField(blank=True,null=True)
    advertiser_account_type = models.CharField(blank=True,null=True,max_length=50)
    analytics_type = models.CharField(blank=True,null=True,max_length=200)
    translator_type = models.CharField(blank=True,null=True,max_length=200)
    
    def __str__(self):
        return self.screen_name

class Place(models.Model):
    bounding_box = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    country_code = models.CharField(max_length=10)
    full_name = models.CharField(max_length=1000)
    id = models.CharField(primary_key=True,max_length=1000)
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=2048)

    def __str__(self):
        return self.full_name
    
class Photo(models.Model):
    id = models.CharField(primary_key=True,max_length=1000)
    media_url = models.URLField(max_length=2048)
    media_url_https = models.URLField(max_length=2048)
    url = models.ForeignKey(Url,on_delete=models.CASCADE)
    media_key = models.CharField(blank=True,null=True,max_length=1000)

    def __str__(self):
        return self.media_url

class Video(models.Model):
    id = models.CharField(primary_key=True,max_length=1000)
    media_url = models.URLField(max_length=2048)
    media_url_https = models.URLField(max_length=2048)
    url = models.ForeignKey(Url,on_delete=models.CASCADE)
    media_key = models.CharField(blank=True,null=True,max_length=1000)
    aspect_ratio_x = models.IntegerField()
    aspect_ratio_y = models.IntegerField()
    duration_millis = models.BigIntegerField()
    video_url = models.URLField(max_length=2048)

    def __str__(self):
        return self.media_url

class Gif(models.Model):
    id = models.CharField(primary_key=True,max_length=1000)
    media_url = models.URLField(max_length=2048)
    media_url_https = models.URLField(max_length=2048)
    url = models.ForeignKey(Url,on_delete=models.CASCADE)
    display_url = models.URLField(max_length=2048)
    expanded_url = models.URLField(max_length=2048)
    media_key = models.CharField(blank=True,null=True,max_length=1000)
    aspect_ratio_x = models.IntegerField()
    aspect_ratio_y = models.IntegerField()
    gif_url = models.URLField(max_length=2048)

    def __str__(self):
        return self.media_url

class Status(models.Model):
    created_at = models.DateTimeField()
    id = models.BigIntegerField(primary_key=True)
    content = models.CharField(max_length=2048)
    display_text_range_start = models.IntegerField()
    display_text_range_end = models.IntegerField()
    hashtags = models.ManyToManyField(Hashtag)
    user_mentions = models.ManyToManyField(UserMention)
    urls = models.ManyToManyField(Url)
    source = models.CharField(max_length=300)
    in_reply_to_status_id = models.BigIntegerField(null=True)
    in_reply_to_user_id = models.BigIntegerField(null=True)
    in_reply_to_screen_name = models.CharField(null=True,max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    place = models.ForeignKey(Place,on_delete=models.CASCADE,null=True, blank=True)
    is_quote_status = models.BooleanField()
    retweet_count = models.BigIntegerField()
    favorite_count = models.BigIntegerField()
    conversation_id = models.BigIntegerField(blank=True,null=True)
    possibly_sensitive = models.BooleanField(null=True,blank=True)
    possibly_sensitive_editable = models.BooleanField(null=True,blank=True)
    lang = models.CharField(max_length=10)
    retweet_status = models.ForeignKey('self',on_delete=models.CASCADE,related_name='retweet',blank=True,null=True)
    quoted_status = models.ForeignKey('self',on_delete=models.CASCADE,related_name='quoted',blank=True,null=True)
    photos = models.ManyToManyField(Photo,related_name='photos')
    videos = models.ManyToManyField(Video,related_name='videos')
    gifs = models.ManyToManyField(Gif,related_name='gifs')

    def __str__(self):
        return self.content
    
