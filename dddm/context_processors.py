from django.core.cache import cache
import twitter


def latest_tweets(request):
    tweets = cache.get('tweets')
    
    if tweets:
        return {"tweets":tweets}
    
    api = twitter.Api()
    results = api.GetSearch(term="#dddscot")
    cache.set('tweets', results, 60)
    
    return {"tweets":results}