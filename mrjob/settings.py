import os

APP_NAME=os.getenv('APP_NAME', "Spark Hadoop")
SPARK_MEM=os.getenv('SPARK_MEM', "1gb")
SPARK_PATH=os.getenv( "SPARK_PATH" , "{}{}".format(os.getcwd(), '/../spark/spark-3.0.0-preview-bin-hadoop2.7/') )