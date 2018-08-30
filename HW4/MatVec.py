import re
import sys
from pyspark import SparkConf, SparkContext

def pair(l):
    return [(l[i],i) for i in range(1,len(l))]

def vec_pair(l):
    return [(i+1,l[i]) for i in range(len(l))]

def compute_element(l):
    for i in range(len(l[1])):
        yield l[1][i][1], (l[0],l[1][i][0])
def compute_vector(l):
    for i in range(len(l)):
        yield i+1, l[i][1]

def matvec(matrix_file, vector_file):
    conf = SparkConf()
    sc = SparkContext(conf=conf)
    matrixs = sc.textFile(matrix_file)
    vectors = sc.textFile(vector_file)
    matrix = matrixs.map(lambda l: list(map(float, re.split(':|,', l))))
    vector = vectors.map(lambda l: list(map(float, re.split(':|,', l))))

    matrix = matrix.map(lambda l: (l[0]+1,pair(l)))
    vector = vector.map(lambda l: vec_pair(l))
    #4th step
    
    element = matrix.flatMap(compute_element)
    #5th step
    vec_element=vector.flatMap(compute_vector)
    element=element.join(vec_element)
    
    #6th step
    #(2, ((1.0, 3.0), 4.0))
    #(2, ((2.0, 5.0), 4.0))
    #(2, ((3.0, 7.0), 4.0))
    element=element.map(lambda l:(l[1][0][0],l[1][0][1]*l[1][1]))
    answer=element.reduceByKey(lambda a,b:a+b)
    answer=answer.map(lambda l: l[1])

    answer.saveAsTextFile("exercise3")
    sc.stop()
    return answer

if __name__=="__main__":
    answer=matvec(sys.argv[1],sys.argv[2])
