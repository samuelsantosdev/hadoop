import re, os, sys, argparse as ap
from operator import add
from mrjob.job import MRJob

WORD_RE = re.compile(r"[\w']+")

class MRSparkWordcountAWS(MRJob):

    def spark(self, input_path, output_path):
        # Spark may not be available where script is launched
        from pyspark import SparkContext

        sc = SparkContext(appName='mrjob Spark wordcount script')

        lines = sc.textFile(input_path)

        counts = (
            lines.flatMap(self.get_words)
            .map(lambda word: (word, 1))
            .reduceByKey(add))

        counts.saveAsTextFile(output_path)

        sc.stop()

    def get_words(self, line):
        return [w.lower() for w in WORD_RE.findall(line)]

class MRSparkWordcount(MRJob):
    
    def spark(self, input_path, output_path):
        # Spark may not be available where script is launched
        from pyspark.sql import SparkSession
        from pyspark import SparkContext
        import pyspark.sql.functions as f
        import settings

        spark = SparkSession.builder \
            .master("local") \
            .appName( settings.APP_NAME ) \
            .config("spark.executor.memory", settings.SPARK_MEM ) \
            .getOrCreate()

        sc = spark.sparkContext

        lines = sc.textFile(input_path)

        counts = ( lines.flatMap(self.get_words)
            .map(lambda word: (word, 1))
            .reduceByKey(add) )

        counts.saveAsTextFile(output_path)

        sc.stop()

    def get_words(self, line):
        return [w.lower() for w in WORD_RE.findall(line)]

if __name__ == '__main__':
    if len(sys.argv) >= 4 :
        if str(sys.argv[3]) == 'emr':
            MRSparkWordcountAWS.run()
    else:
        MRSparkWordcount.run()