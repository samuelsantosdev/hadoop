from libraries.kafka_handler import KafkaHandler
from libraries.spark_handler import SparkHandler
import settings as settings
from helpers.logs import *

def main():
    
    spark_path  = settings.SPARK_HOME
    path_output = "{}{}.{}".format(settings.PATH_DATA, settings.WORDS.replace(',','-'), 'out')

    #try:

    kafka       = KafkaHandler( settings.KAFKA_TOPIC, settings.KAFKA_KEY, settings.KAFKA_HOST )    
    spark       = SparkHandler( [settings.KAFKA_HOST], [settings.KAFKA_TOPIC], spark_path, path_output )
    spark.countWords()
        
    #except Exception as e:
    #    do_log("EXCEPTION", str(e))

if __name__ == '__main__':
    main()