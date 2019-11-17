from pyspark.sql import SparkSession, Row
import os

def main():
    # Build the SparkSession
    spark = SparkSession.builder \
        .master("local") \
        .appName( os.getenv('APP_NAME', "Spark Map Reduce") ) \
        .config("spark.executor.memory", os.getenv('SPARK_MEM', "1gb") ) \
        .getOrCreate()
    
    sc = spark.sparkContext

    #Carregar arquivo CSV
    rdd = sc.textFile('data/nomes-censos-ibge.csv')

    #Dividir colunas com split
    rdd = rdd.map(lambda line: line.split(","))

    #Criar DataFrame
    df = rdd.map(lambda line: Row(Name=line[0],  ate2000=line[8], ate2010=line[9])).toDF()

    #Filtrar por crescimento acima de 10000 mil a cada 10 anos
    dfFiltred = df.filter( (df.ate2010 - df.ate2000) > 10000 )

    #Exibir 20 primeiras linhas
    dfFiltred.show()


if __name__ == '__main__':
    main()
    pass