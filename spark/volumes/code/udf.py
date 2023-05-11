from pyspark.sql import functions as f
from pyspark.sql import types as t
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('simple_app').getOrCreate()
df = spark.read.format('csv').option('inferSchema', 'true').option('header', 'true').load('/opt/data/clients.csv')

schema = t.StructType(
    [
        t.StructField('id',t.IntegerType(),True),
        t.StructField('income_log',t.FloatType(),True),
        t.StructField('expenses_log',t.FloatType(),True),

    ]
)

def normalize(pdf):
    import pandas as pd
    import numpy as np

    df=pdf[['id','income','expenses']]

    df.loc[:,'income_log']=np.log1p(df.loc[:,'income'])
    df.loc[:,'expenses_log']=np.log1p(df.loc[:,'expenses'])

    return df [['id','income_log','expenses_log']]

df_normalized = df \
.groupBy(f.col('id')) \
.applyInPandas(normalize,schema=schema)

df_normalized.show()