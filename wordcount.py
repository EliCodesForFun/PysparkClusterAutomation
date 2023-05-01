import sys

from pyspark import SparkContext, SparkConf

if __name__ == "__main__":

    # create Spark context with Spark configuration

    #conf = SparkConf().setAppName("Word Count - Python").set("spark.hadoop.yarn.resourcemanager.address", "192.168.0.104:8032")
    
    conf = SparkConf().setAppName("Word Count - Python").setMaster("spark://10.5.0.2:7077")
    sc = SparkContext(conf=conf)

    # read in text file and split each document into words
#    words = sc.textFile("somewords.txt").flatMap(lambda line: line.split(" "))

    # count the occurrence of each word
#    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)

#    wordCounts.saveAsTextFile("output/")
    print("I got here" * 100)

    def mod(x):
        import numpy as np
        return (x, np.mod(x, 2))

    rdd = sc.parallelize(range(1000)).map(mod).take(10)
    print(rdd)
