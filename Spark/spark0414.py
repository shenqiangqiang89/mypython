# -*- coding: utf-8 -*-

from pyspark import SparkConf, SparkContext

#创建sparkconf，设置spark的相关参数
#conf = SparkConf().setMaster("local[2]").setAppName("spark0401")
conf = SparkConf()

#创建SparkContext
sc = SparkContext(conf=conf)

#业务逻辑
data = [1, 2, 3, 4, 5, 6]

distData = sc.parallelize(data)
distData = distData.map(lambda x: x + 1)
print(distData.collect())

#关闭sc，养成好习惯
sc.stop()