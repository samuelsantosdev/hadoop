# Sample PySpark
In this simple test, we read a CSV file with most used Names in Brazil,
and show a result with top names in 10 years

### Download Spark Hadoop

```
$ cd <project_path>/spark
$ wget https://www-us.apache.org/dist/spark/spark-3.0.0-preview/spark-3.0.0-preview-bin-hadoop2.7.tgz 
$ tar xvf spark-3.0.0-preview-bin-hadoop2.7.tgz
```

### Set the path of Spark in .env
SPARK_PATH=<path_to_projetct>/spark/spark-3.0.0-preview-bin-hadoop2.7/
SPARK_MEM=1gb
APP_NAME=Spark Hadoop Teste

### Run the test
```
$ python main.py
+--------+--------+--------+-------+------------------+                         
|    Name|Year2000|Year2010|   Diff|          Increase|
+--------+--------+--------+-------+------------------+
|RIQUELME|   202.0| 14037.0|13835.0| 6849.009900990099|
| KAILANE|   382.0| 22802.0|22420.0| 5869.109947643979|
|    CAUA|  2069.0| 83253.0|81184.0| 3923.827936201063|
|    KAUA|  1419.0| 56563.0|55144.0|3886.1169837914026|
|   CAUAN|  1285.0| 44513.0|43228.0| 3364.046692607004|
|   KAUAN|  2221.0| 66962.0|64741.0| 2914.948221521837|
|    RIAN|  2790.0| 72137.0|69347.0|2485.5555555555557|
|    RYAN|  1303.0| 32674.0|31371.0|2407.5978511128164|
|    ENZO|  2088.0| 44056.0|41968.0| 2009.961685823755|
|  CAMILI|   679.0| 13968.0|13289.0|1957.1428571428573|
+--------+--------+--------+-------+------------------+
```

# Sample MrJob
