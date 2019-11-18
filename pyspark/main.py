import findspark, os, settings

# Carregar Spark com Hadoop
findspark.init( settings.SPARK_PATH )

import runmr
runmr.main()