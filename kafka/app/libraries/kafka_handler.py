from kafka import KafkaProducer
import logging
from helpers.logs import *
from kafka import KafkaConsumer

class KafkaHandler():

    producer=None

    __topic_name=None
    __key=None
    __kafka_host=None

    def __init__(self, topic_name: str, key:str, kafka_host: str):

        self.__topic_name   = topic_name
        self.__key          = key
        self.__kafka_host   = kafka_host

        try:
            
            self.producer = KafkaProducer(bootstrap_servers=[ self.__kafka_host ], api_version=(0, 10))

        except Exception as ex:
            do_log("EXCEPTION", 'Exception while connecting Kafka {}'.format(str(ex)))
        

    def publishMessage(self, value: str):
        
        try:

            value       = bytes(value, encoding='utf-8')
            if value == '' and value == None :
                return

            key_bytes   = bytes(self.__key, encoding='utf-8')
            self.producer.send(self.__topic_name, key=key_bytes, value=value)
            self.producer.flush()

            do_log("PUBLISH", 'Message published successfully.')
            
        except Exception as ex:
            do_log("EXCEPTION", 'Exception while published Kafka {}'.format(str(ex)))

    def getMessage(self):
        for msg in KafkaConsumer(self.__topic_name):
            yield msg
        