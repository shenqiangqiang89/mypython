windows下配置pyspark的方法
1. 拷贝hadoop-2.6.0目录到某一个目录下
   D:\Program Files\hadoop-2.6.0\bin

   配置环境变量：
     HADOOP_HOME=D:\Program Files\hadoop-2.6.0
     path =  D:\Program Files\hadoop-2.6.0\bin

2. 配置pycharm
    拷贝 spark-2.3.0-bin-2.6.0-cdh5.7.0 到一个目录下
  （1） 选择edit configurations， New一个configuration，
       配置 environment variables，
     SPARK_HOME = E:\centos_sys\spark-2.3.0-bin-2.6.0-cdh5.7.0
     PYTHONPATH = E:\centos_sys\spark-2.3.0-bin-2.6.0-cdh5.7.0\python

3. 设置 ---》project structure
    +add content root
    选择 E:\centos_sys\spark-2.3.0-bin-2.6.0-cdh5.7.0\python\lib\py4j-0.10.6-src.zip
        E:\centos_sys\spark-2.3.0-bin-2.6.0-cdh5.7.0\python\lib\pyspark.zip

配置完毕！