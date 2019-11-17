import os

SPARK_PATH=os.getenv( "SPARK_PATH" , "{}{}".format(os.getcwd(), '/spark/spark-3.0.0-preview-bin-hadoop2.7/') )