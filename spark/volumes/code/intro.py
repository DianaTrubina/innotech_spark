from pyspark.sql import functions as f
from pyspark.sql import types as t
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('simple_app').getOrCreate()
# df = spark.read.format('csv').option('inferSchema', 'true').option('header', 'true').load('/opt/data/clients.csv')

# df_agg = df \
#      .groupBy(f.col('gender')) \
#     .agg(f.count(f.col('id')).cast(t.IntegerType()).alias('id_cnt'))

# df_agg.show()