from libraries.twitter_stream import TwitterStream
import settings as settings

def main():
    
    twitter     = TwitterStream( settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET, settings.TWITTER_ACCESS_TOKEN_KEY, settings.TWITTER_ACCESS_TOKEN_SECRET )

    twitter.streamWord( "{}{}".format(settings.PATH_DATA, settings.WORDS.replace(',','-')), settings.WORDS.split(',') )

if __name__ == '__main__':
    main()