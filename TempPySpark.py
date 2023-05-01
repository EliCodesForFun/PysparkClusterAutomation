import findspark
findspark.init('C:\BigDataLocalSetup\spark')

from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.sql import SparkSession



conf = SparkConf()
conf.setMaster('spark://10.5.0.2:7077')
conf.setAppName('spark-basic')
sc = SparkContext(conf=conf)


spark = SparkSession.builder \
                    .master('spark://10.5.0.2:7077') \
                    .appName('Vlad is cool') \
                    .getOrCreate()




def mod(x):
    import numpy as np
    return (x, np.mod(x, 2))

#rdd = sc.parallelize(range(1000)).map(mod).take(10)
# rdd = sc.parallelize(range(100 + 1))
# rdd.sum()

data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

rdd_multiplied = rdd.map(lambda x: x * 2)

print(rdd_multiplied.collect())

print(rdd)

argp


import pandas as pd
print (pd.__version__)

url = 'https://en.wikipedia.org/wiki/List_of_Nobel_laureates'
df_table = pd.read_html(url, header=0, index_col=0, attrs={"class": "wikitable sortable jquery-tablesorter"}, parse_dates=True, flavor='bs4', extract)[0]