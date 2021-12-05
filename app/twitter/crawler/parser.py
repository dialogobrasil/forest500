from twitter.models import *
import datetime

def parse_date(tweet):
    tweet['created_at'] = datetime.datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
    tweet['user']['created_at'] = datetime.datetime.strptime(tweet['user']['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
    return tweet

def parse_user(user):
    user = User(
        id = user['id'],
        name = user['name'],
        screen_name = user['screen_name'],
        location = user['location'],
        description = user['description'],
        protected = user['protected'],
        followers_count = user['followers_count'],
        fast_followers_count = user.get('fast_followers_count',None),
        normal_followers_count = user.get('normal_followers_count',None),
        friends_count = user['friends_count'],
        listed_count = user['listed_count'],
        created_at = user['created_at'],
        favourites_count = user['favourites_count'],
        geo_enabled = user['geo_enabled'],
        verified = user['verified'],
        statuses_count = user['statuses_count'],
        media_count = user.get('media_count',None),
        lang = user['lang'],
        contributors_enabled = user['contributors_enabled'],
        is_translator = user['is_translator'],
        is_translation_enabled = user['is_translation_enabled'],
        profile_background_color = user['profile_background_color'],
        profile_background_image_url = user['profile_background_image_url'],
        profile_background_image_url_https = user['profile_background_image_url_https'],
        profile_background_tile = user['profile_background_tile'],
        profile_image_url = user['profile_image_url'],
        profile_image_url_https = user['profile_image_url_https'],
        profile_banner_url = user.get('profile_banner_url',None),
        profile_link_color = user['profile_link_color'],
        profile_sidebar_border_color = user['profile_sidebar_border_color'],
        profile_sidebar_fill_color = user['profile_sidebar_fill_color'],
        profile_text_color = user['profile_text_color'],
        profile_use_background_image = user['profile_use_background_image'],
        has_custom_timelines = user.get('has_custom_timelines',None),
        advertiser_account_type = user.get('advertiser_account_type',None),
        analytics_type = user.get('analytics_type',None),
        translator_type = user.get('translator_type',None),
    )
    return user

def parse_retweet(tweet):
    if('retweeted_status' in tweet):
        return tweetParse(tweet.get('retweeted_status',False))
    return None

def parse_quote(tweet):
    if('quoted_status' in tweet):
        return tweetParse(tweet.get('quoted_status',False))
    return None

def tweetParse(tweet):
    tweet = parse_date(tweet)
    retweeted_status = parse_retweet(tweet)
    quoted_status = parse_quote(tweet)

    user = User(tweet['user'])
    users_bulk[user.id] = user

    

    for url_json in user['entities'].get('url',{'urls':[]})['urls']:
        url = Url(
            #id = url_json['url'],
            url = url_json['url'],
            expanded_url = url_json.get('expanded_url',None),
            display_url = url_json.get('display_url', None),
        )
        url_bulk[url.url] = url
        url_bulk_through[(url.url,user.id)] = User.urls.through(user_id=user.id,url_id=url.url)

        
    for description_url_json in tweet['user']['entities']['description']['urls']:
        url = Url(
            url = description_url_json['url'],
            expanded_url = description_url_json['expanded_url'],
            display_url = description_url_json['display_url'],
        )
        url_bulk[url.url] = url
        urlDescription_bulk_through[(url.url,user.id)] = User.descriptionUrl.through(user_id=user.id,url_id=url.url)

    status = Status(
        created_at = tweet['created_at'],
        id = tweet['id'],
        content = tweet['full_text'],
        display_text_range_start = tweet['display_text_range'][0],
        display_text_range_end = tweet['display_text_range'][1],
        user_id = user.id,
        source = tweet['source'],
        in_reply_to_status_id = tweet['in_reply_to_status_id'],
        in_reply_to_user_id = tweet['in_reply_to_user_id'],
        in_reply_to_screen_name = tweet['in_reply_to_screen_name'],
        #place = models.ForeignKey(Place,on_delete=models.PROTECT)
        is_quote_status = tweet['is_quote_status'],
        retweet_count = tweet['retweet_count'],
        favorite_count = tweet['favorite_count'],
        conversation_id = tweet.get('conversation_id',None),
        possibly_sensitive = tweet.get('possibly_sensitive',False),
        possibly_sensitive_editable = tweet.get('possibly_sensitive_editable',False),
        lang = tweet['lang'],
        retweet_status_id = None, #if retweeted_status == None else retweeted_status.id,
        quoted_status_id = None #if quoted_status == None else quoted_status.id,
    )
    status_bulk[status.id] = status

    if 'extended_entities' in tweet:
        for entity_json in tweet['extended_entities']['media']:
            if(entity_json['type'] == "photo"):
                url = Url(
                    url = entity_json['url'],
                    display_url = entity_json['display_url'],
                    expanded_url = entity_json['expanded_url'],
                )
                url_bulk[url.url] = url
                photo = Photo(
                    id = entity_json['id'],
                    media_url = entity_json['media_url'],
                    media_url_https = entity_json['media_url_https'],
                    media_key = entity_json.get('media_key',None),
                    url_id = url.url,
                )
                photos_bulk[photo.id] = photo
                photoStatus_bulk[(photo.id,status.id)] = Status.photos.through(photo_id=photo.id,status_id=status.id)

            elif(entity_json['type'] == "video"):
                url = Url(
                    url = entity_json['url'],
                    display_url = entity_json['display_url'],
                    expanded_url = entity_json['expanded_url'],
                )
                url_bulk[url.url] = url
                for variants_json in entity_json['video_info']['variants']:
                    if( variants_json["content_type"] == "application/x-mpegURL" ):
                        video_url = variants_json["url"]
                    
                video = Video(
                    id = entity_json['id'],
                    media_url = entity_json['media_url'],
                    media_url_https = entity_json['media_url_https'],
                    media_key = entity_json.get('media_key',None),
                    url_id = url.url,
                    aspect_ratio_x = entity_json['video_info']['aspect_ratio'][0],
                    aspect_ratio_y = entity_json['video_info']['aspect_ratio'][1],
                    duration_millis = entity_json['video_info']['duration_millis'],
                    video_url = video_url,
                )
                videos_bulk[video.id] = video
                videosStatus_bulk[(video.id,status.id)] = Status.videos.through(video_id=video.id,status_id=status.id)
            elif(entity_json['type'] == "animated_gif"):
                url = Url(
                    url = entity_json['url'],
                    display_url = entity_json['display_url'],
                    expanded_url = entity_json['expanded_url'],
                )
                url_bulk[url.url] = url
                gif = Gif(
                    id = entity_json['id'],
                    media_url = entity_json['media_url'],
                    media_url_https = entity_json['media_url_https'],
                    media_key = entity_json.get('media_key',None),
                    url_id = url.url,
                    aspect_ratio_x = entity_json['video_info']['aspect_ratio'][0],
                    aspect_ratio_y = entity_json['video_info']['aspect_ratio'][1],
                    gif_url = entity_json['video_info']['variants'][0]["url"],
                )
                gifs_bulk[gif.id] = gif
                gifsStatus_bulk[(gif.id,status.id)] = Status.gifs.through(gif_id=gif.id,status_id=status.id)


    for hashtag_json in tweet['entities']['hashtags']:
        hashtag = Hashtag(
            text = hashtag_json['text']
        )
        hashtag_bulk[hashtag.text] = hashtag
        hashtag_bulk_through[(hashtag.text,status.id)] = Status.hashtags.through(status_id=status.id,hashtag_id=hashtag.text)

    for user_mention_json in tweet['entities']['user_mentions']:
        user_mention = UserMention(
            screen_name = user_mention_json['screen_name'],
            name = user_mention_json['name'],
            id = user_mention_json['id'],
        )
        userMention_bulk[user_mention.id] = user_mention 
        userMention_bulk_through[(user_mention.id,status.id)] = Status.user_mentions.through(status_id=status.id,usermention_id=user_mention.id)

    for url_json in tweet['entities']['urls']:
        url = Url(
            url = url_json['url'],
            expanded_url = url_json['expanded_url'],
            display_url = url_json['display_url'],
        )
        url_bulk[url.url] = url
        urlStatus_bulk_through[(url.url,status.id)] = Status.urls.through(status_id=status.id,url_id=url.url)

    return Status



