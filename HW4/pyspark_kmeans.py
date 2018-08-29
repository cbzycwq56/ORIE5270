import re
import sys
from pyspark import SparkConf, SparkContext
from numpy.linalg import norm
import numpy as np
def pair(l,centroid):
    index=0
    c_list=centroid
    min_dist=norm(l-list(c_list[0]))
    for i in range(1,len(c_list)):
        temp=norm(l-list(c_list[i]))
        if temp<min_dist:
            index=i
            min_dist=temp
    return (index,(l,1))

def fun(dFile, cFile):
    conf = SparkConf()
    sc = SparkContext(conf=conf)
    
    
    data = sc.textFile(dFile).map(lambda line: np.array([float(x) for x in line.split(' ')])).cache()
   # Load the initial centroids
    centroid = sc.textFile(cFile).map(lambda line: np.array([float(x) for x in line.split(' ')])).collect()
        
    loop =data.map(lambda l: pair(l,centroid))
    
    for i in range(100):
        print(i)
        loop=loop.reduceByKey(lambda a,b:(a[0]+b[0],a[1]+b[1])).sortByKey(ascending=True)
        centroid=loop.map(lambda l: l[1][0]/l[1][1])
        centroid=centroid.collect()
        loop=data.map(lambda l: pair(l,centroid))
    
    f=open("answer.txt","w+")
    for i in range(len(centroid)):
        str1 = ' '.join(str(e) for e in centroid[i])
        str1+="\n"
        f.write(str1)
    f.close()
    #centroid.saveAsTextFile("answer")
    
if __name__ == "__main__":
    fun(sys.argv[1],sys.argv[2])

