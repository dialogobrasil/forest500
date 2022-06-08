import tweepy
import datetime
from twitter.models import *
from institution.models import *
from elasticsearch import Elasticsearch
from topic.models import Topic
from twitter.documents import StatusDocument

class TwitterAPI:
    def __init__(self,token,secret):
        # self.keys = [['2m2IZIw55y8XMTRLep2gx6van','kcF8ZCrA6yK4zZFVkGYSkEd7W5sopi5GFjJoQLg1n75WA22Vlc'],
        #             ['3nVuSoBZnx6U4vzUxf5w','Bcs59EFbbsdF6Sl9Ng71smgStWEGwXXKSjYvPVt7qys'],
        #             ['IQKbtAYlXLripLGPWd0HUA','GgDYlkSvaPxGxC4X8liwpUoqKwwr3lCADbz8A7ADU'],
        #             ['CjulERsDeqhhjSme66ECg','IQWdVyqFxghAtURHGeGiWAsmCAGmdW3WmbEx6Hck'],
        #             ['3rJOl1ODzm9yZy63FACdg','5jPoQ5kQvMJFDYRNE8bQ4rHuds4xJqhvgNJM4awaE8'],
        #             ['3nVuSoBZnx6U4vzUxf5w','Bcs59EFbbsdF6Sl9Ng71smgStWEGwXXKSjYvPVt7qys'],
        #             ['d0CTc4Zg9pufCnMkteDc7w','z4FMZhP87U5QEwycggDe5JN6TDDh7xEyhnAcEpdWk'],
        #             ['CVbiuNGV6MeQCsku7SUZnejVb','AXzQ9ZSxu1JPWbQNXHj4Zn1uI32fMDviLDYyKM6RihwPjGz6i9'],
        #             ['53aMoQiFaQfoUtxyJIkGdw','Twnh3SnDdtQZkJwJ3p8Tu5rPbL5Gt1I0dEMBBtQ6w'],
        #             ['7Uifmz2gkHF8RcOcMtItTJRoF', 'YmcL95Yy15zvwAfGVaCrbGaUkcWo6wv0OT9RXCOxWfoHwuY1RT'],
        #             ]
        self.api = None
        self.data = {}

        try:
            auth = tweepy.AppAuthHandler(token, secret) 
            authenticated = tweepy.API(auth, wait_on_rate_limit=True)
            self.api = authenticated
        except:
            print(f'Failure on credentials, does not work any more')
        
    def parse_date(tweet):
        tweet['created_at'] = datetime.datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
        tweet['user']['created_at'] = datetime.datetime.strptime(tweet['user']['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
        if ('retweeted_status' in tweet):
            tweet['retweeted_status']['created_at'] = datetime.datetime.strptime(tweet['retweeted_status']['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
            tweet['retweeted_status']['user']['created_at'] = datetime.datetime.strptime(tweet['retweeted_status']['user']['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
        return tweet

    def getTweets(self, userids,inicialid):
    
        for row in userids:
            id = row[0]
            self.data[id] = []
            print(id)
            try:
                for x in tweepy.Cursor(self.api.user_timeline, user_id=id,since_id=inicialid,tweet_mode="extended",count=200).items():
                    self.data[id].append(x._json)
            except:
                print('except')
                continue

def parse_date(tweet):
    tweet['created_at'] = datetime.datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
    tweet['user']['created_at'] = datetime.datetime.strptime(tweet['user']['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
    return tweet

def tweetParse(tweet):
    tweet = parse_date(tweet)

    if('retweeted_status' in tweet):
        retweeted_status = tweetParse(tweet.get('retweeted_status',False))
    else:
        retweeted_status = None

    if('quoted_status' in tweet):
        quoted_status = tweetParse(tweet.get('quoted_status',False))
    else:
        quoted_status = None

    user = User(
        id = tweet['user']['id_str'],
        name = tweet['user']['name'],
        screen_name = tweet['user']['screen_name'],
        location = tweet['user']['location'],
        description = tweet['user']['description'],
        protected = tweet['user']['protected'],
        followers_count = tweet['user']['followers_count'],
        fast_followers_count = tweet['user'].get('fast_followers_count',None),
        normal_followers_count = tweet['user'].get('normal_followers_count',None),
        friends_count = tweet['user']['friends_count'],
        listed_count = tweet['user']['listed_count'],
        created_at = tweet['user']['created_at'],
        favourites_count = tweet['user']['favourites_count'],
        geo_enabled = tweet['user']['geo_enabled'],
        verified = tweet['user']['verified'],
        statuses_count = tweet['user']['statuses_count'],
        media_count = tweet['user'].get('media_count',None),
        lang = tweet['user']['lang'],
        contributors_enabled = tweet['user']['contributors_enabled'],
        is_translator = tweet['user']['is_translator'],
        is_translation_enabled = tweet['user']['is_translation_enabled'],
        profile_background_color = tweet['user']['profile_background_color'],
        profile_background_image_url = tweet['user']['profile_background_image_url'],
        profile_background_image_url_https = tweet['user']['profile_background_image_url_https'],
        profile_background_tile = tweet['user']['profile_background_tile'],
        profile_image_url = tweet['user']['profile_image_url'],
        profile_image_url_https = tweet['user']['profile_image_url_https'],
        profile_banner_url = tweet['user'].get('profile_banner_url',None),
        profile_link_color = tweet['user']['profile_link_color'],
        profile_sidebar_border_color = tweet['user']['profile_sidebar_border_color'],
        profile_sidebar_fill_color = tweet['user']['profile_sidebar_fill_color'],
        profile_text_color = tweet['user']['profile_text_color'],
        profile_use_background_image = tweet['user']['profile_use_background_image'],
        has_custom_timelines = tweet['user'].get('has_custom_timelines',None),
        advertiser_account_type = tweet['user'].get('advertiser_account_type',None),
        analytics_type = tweet['user'].get('analytics_type',None),
        translator_type = tweet['user'].get('translator_type',None),
    )
    user.save()

    for url_json in tweet['user']['entities'].get('url',{'urls':[]})['urls']:
        url = Url(
            url = url_json['url'],
            expanded_url = url_json.get('expanded_url',None),
            display_url = url_json.get('display_url', None),
        )
        url.save()
        user.urls.add(url)

        
    for description_url_json in tweet['user']['entities']['description']['urls']:
        url = Url(
            url = description_url_json['url'],
            expanded_url = description_url_json['expanded_url'],
            display_url = description_url_json['display_url'],
        )
        url.save()
        user.descriptionUrl.add(url)

    status = Status(
        created_at = tweet['created_at'],
        id = tweet['id_str'],
        content = tweet['full_text'],
        display_text_range_start = tweet['display_text_range'][0],
        display_text_range_end = tweet['display_text_range'][1],
        user_id = user.id,
        source = tweet['source'],
        in_reply_to_status_id = tweet['in_reply_to_status_id'],
        in_reply_to_user_id = tweet['in_reply_to_user_id'],
        in_reply_to_screen_name = tweet['in_reply_to_screen_name'],
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
    status.save()

    if 'extended_entities' in tweet:
        for entity_json in tweet['extended_entities']['media']:
            if(entity_json['type'] == "photo"):
                url = Url(
                    url = entity_json['url'],
                    display_url = entity_json['display_url'],
                    expanded_url = entity_json['expanded_url'],
                )
                url.save()

                photo = Photo(
                    id = entity_json['id_str'],
                    media_url = entity_json['media_url'],
                    media_url_https = entity_json['media_url_https'],
                    media_key = entity_json.get('media_key',None),
                    url_id = url.url,
                )
                photo.save()
                status.photos.add(photo)

            elif(entity_json['type'] == "video"):
                url = Url(
                    url = entity_json['url'],
                    display_url = entity_json['display_url'],
                    expanded_url = entity_json['expanded_url'],
                )
                url.save()
                for variants_json in entity_json['video_info']['variants']:
                    if( variants_json["content_type"] == "application/x-mpegURL" ):
                        video_url = variants_json["url"]
                    
                video = Video(
                    id = entity_json['id_str'],
                    media_url = entity_json['media_url'],
                    media_url_https = entity_json['media_url_https'],
                    media_key = entity_json.get('media_key',None),
                    url_id = url.url,
                    aspect_ratio_x = entity_json['video_info']['aspect_ratio'][0],
                    aspect_ratio_y = entity_json['video_info']['aspect_ratio'][1],
                    duration_millis = entity_json['video_info']['duration_millis'],
                    video_url = video_url,
                )
                video.save()
                status.videos.add(video)

            elif(entity_json['type'] == "animated_gif"):
                url = Url(
                    url = entity_json['url'],
                    display_url = entity_json['display_url'],
                    expanded_url = entity_json['expanded_url'],
                )
                url.save()
                gif = Gif(
                    id = entity_json['id_str'],
                    media_url = entity_json['media_url'],
                    media_url_https = entity_json['media_url_https'],
                    media_key = entity_json.get('media_key',None),
                    url_id = url.url,
                    aspect_ratio_x = entity_json['video_info']['aspect_ratio'][0],
                    aspect_ratio_y = entity_json['video_info']['aspect_ratio'][1],
                    gif_url = entity_json['video_info']['variants'][0]["url"],
                )
                gif.save()
                status.gifs.add(gif)


    for hashtag_json in tweet['entities']['hashtags']:
        hashtag = Hashtag(
            text = hashtag_json['text']
        )
        hashtag.save()
        status.hashtags.add(hashtag)

    for user_mention_json in tweet['entities']['user_mentions']:
        user_mention = UserMention(
            screen_name = user_mention_json['screen_name'],
            name = user_mention_json['name'],
            id = user_mention_json['id_str'],
        )
        user_mention.save()
        status.user_mentions.add(user_mention)

    for url_json in tweet['entities']['urls']:
        url = Url(
            url = url_json['url'],
            expanded_url = url_json['expanded_url'],
            display_url = url_json['display_url'],
        )
        url.save()
        status.urls.add(url)

    return Status


def updateTweets():
    lastTweet = Status.objects.latest('created_at')
    lastID = lastTweet.id
    lastDate = lastTweet.created_at 
    users_ids = Handle.objects.exclude(user__isnull=True).values_list('user__id')
    key = APIKey.objects.last()
    api = TwitterAPI(key.acess_token,key.acess_token_secret)
    api.getTweets(userids=users_ids,inicialid=lastID)
    for user in api.data:
        print(user)
        for tweet in api.data[user]:
            tweetParse(tweet)
    
    es = Elasticsearch(['http://elasticsearch:9200/'])
    for topic in Topic.objects.all():
        print(topic)
        topics_bulk = []
        topics_bulk_es = {}

        s = StatusDocument.search().filter('range', created_at={'gte':lastDate, 'lte': datetime.datetime.now()}).query('query_string',default_field='content',query=topic.query).scan()

        for hit in s:
            topics_bulk.append(Topic.status.through(topic_id=topic.name, status_id=hit.id))
            if (hit.id not in topics_bulk_es) :
                topics_bulk_es[hit.id] = []
            topics_bulk_es[hit.id].append(topic.name)
            Status.objects.get(pk=hit.id).topic_set.add(topic)

updateTweets()