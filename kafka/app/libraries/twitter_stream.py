import sys
from typing import List

from tweepy import OAuthHandler
from tweepy import API
from tweepy import Stream
from tweepy.streaming import StreamListener

import logging

class Listener(StreamListener):
    def __init__(self, output_file=sys.stdout):
        super(Listener,self).__init__()
        self.output_file = output_file

    def on_status(self, status):
        print(status.text, file=self.output_file)

    def on_error(self, status_code):
        print(status_code)
        return False

class TwitterStream():
    
    __file_output=None
    __api=None

    def __init__(self, consumer_key: str, consumer_secret: str, access_token_key: str, access_token_secret: str):
        auth        = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token_key, access_token_secret)

        self.__api  = API(auth, wait_on_rate_limit=True,
                wait_on_rate_limit_notify=True)

    def streamWord(self, file_output: str, words: List[str]):

        logging.warn("Wrods={}".format(",".join(words)))
        self.__file_output = file_output
        output = open(self.__file_output, 'w')

        listener = Listener(output_file=output)
        stream = Stream(auth=self.__api.auth, listener=listener)

        try:
            stream.filter(track=words)
        except KeyboardInterrupt:
            logging.warning("Stopped.")
        finally:
            logging.warning('Done.')
            stream.disconnect()
            output.close()