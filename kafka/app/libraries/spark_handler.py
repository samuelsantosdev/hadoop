import re, os, sys, argparse as ap
from operator import add
from typing import List
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import pyspark.sql.functions as f
import findspark
from helpers.logs import *

class SparkHandler():
    
    __output_path = None
    __brokers = None
    __topics = None

    def __init__(self, brokers: List[str], topics: List[str], spark_path: str, output_path: str=''):
        
        # Carregar Spark com Hadoop
        do_log("PATH", spark_path)
        findspark.init( spark_path )

        self.__brokers      = brokers
        self.__output_path  = output_path
        self.__topics       = topics

    def countWords(self):

        
        #os.environ['PYSPARK_SUBMIT_ARGS'] = '--jars spark-streaming_2.11-2.4.4.jar'
        os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.4.4 pyspark-shell'
                                                                        
        sc = SparkContext(appName="Sparkstreaming")
        spark = SparkSession.builder.appName("Spark-Kafka-Integration").master("local").config("spark.executor.memory", "1gb" ).getOrCreate()
        ssc = StreamingContext(sc,1)
        
        kvs = KafkaUtils.createDirectStream(ssc, self.__topics,{"metadata.broker.list": self.__brokers[0]})
        lines = kvs.map(lambda x: x[1])
        counts = lines.flatMap(lambda line: line.split(" ")) \
            .filter(lambda word: len(word) > 3 and word != 'love' ) \
            .map(lambda word: (word, 1)) \
            .reduceByKey(lambda a, b: a+b) \
            .transform(lambda a: a.sortBy(lambda x:x[1], ascending=False) )
        counts.pprint()

        ssc.start()
        ssc.awaitTermination()
        

    def get_words(self, line):
        return [w.lower() for w in re.compile(r"[\w']+").findall(line) ]