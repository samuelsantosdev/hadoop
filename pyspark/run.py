import findspark, os
import settings

# Carregar Spark com Hadoop
findspark.init( settings.SPARK_PATH )

import main
main.main()