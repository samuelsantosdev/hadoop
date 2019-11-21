from libraries.kafka_handler import KafkaHandler
from libraries.file_stream import FileStream
import logging
import settings as settings
from helpers.logs import *

def main():
    
    try:
        fileIO      = FileStream( filename="{}{}".format(settings.PATH_DATA, settings.WORDS.replace(',','-')) )
        kafka       = KafkaHandler( settings.KAFKA_TOPIC, settings.KAFKA_KEY, settings.KAFKA_HOST )
        for line in fileIO.streamFile():
            #do_log("READ", bytes(line.read()).decode("utf-8") )
            kafka.publishMessage( line )
    except Exception as e:
        logging.warning(str(e))

if __name__ == '__main__':
    main()