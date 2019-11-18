from pyspark.sql import SparkSession, Row
from pyspark.sql.types import *
from pyspark.sql.functions import grouping, col, desc, asc
from operator import add
import os

def main():
    # Build the SparkSession
    spark = SparkSession.builder \
        .master("local") \
        .appName( os.getenv('APP_NAME', "Spark Hadoop") ) \
        .config("spark.executor.memory", os.getenv('SPARK_MEM', "1gb") ) \
        .getOrCreate()
    
    sc = spark.sparkContext

    #Carregar arquivo CSV
    rdd = sc.textFile('data/nomes-censos-ibge.csv')

    #Dividir colunas com split
    rdd = rdd.map(lambda line: line.split(","))

    #Criar DataFrame
    df = rdd.map(lambda line: Row(Name=line[0],  Year2000=line[8], Year2010=line[9], Diff=defaultZero(line[9]) - defaultZero(line[8]) ) ).toDF()
    df = convertColumn(df, ["Year2000", "Year2010", "Diff"], FloatType())
    
    #Filtrar por crescimento acima de 10000 mil a cada 10 anos
    df.createOrReplaceTempView("names")
    df2 = spark.sql("SELECT Name, Year2000, Year2010, Diff, (Diff/Year2000*100) as Increase from names where (Year2010 - Year2000) > 10000 order by (Diff/Year2000*100) DESC")
    
    #Top 10 nomes que mais se tornaram comuns entre 2000 e 2010
    df2.show(n=10)


def convertColumn(df, columns, Type):
    for name in columns :
        df = df.withColumn(name, df[name].cast(Type))
    return df

def defaultZero(value):
    try:
        return int(float(0 if value is None else value))
    except:
        return 0

if __name__ == '__main__':
    main()
    pass