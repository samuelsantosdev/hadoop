import twitter, os

class TwitterHandler():

    __api=None

    def __init__(self, consumer_key: str, consumer_secret: str, access_token_key: str, access_token_secret: str):

        self.__api = twitter.Api(consumer_key,
                            consumer_secret,
                            access_token_key,
                            access_token_secret)

    def getFriends(self):
        return self.__api.GetFriends()

    def getAllTweets(self):
        for u in self.getFriends() :
            
            try:
                
                statuses = self.__api.GetUserTimeline(screen_name=u.screen_name)
                posts = [ post.text.strip() for post in statuses ]
                    
                yield { 'username' : u.screen_name, 'posts' : posts }

            except Exception as e:
                print("{} not found".format(u.screen_name))