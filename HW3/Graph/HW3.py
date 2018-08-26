import numpy as np
from ast import literal_eval as make_tuple
import heapq as hq
def read_graph(filename):

    file = open(filename)
    lines = file.readlines()
    lines = [x.strip() for x in lines]
    num_nodes=len(lines)/2
    graph=dict()
    for i in range(num_nodes):
        graph[float(lines[i*2])]=[]
        edge=[]
        temp=""
        if len(lines[i*2+1])>0:
            temp+=lines[i*2+1][0]
        for j in range(1,len(lines[i*2+1])):
            
            if not(lines[i*2+1][j]=="," and lines[i*2+1][j-1]== ")"):
                temp+=lines[i*2+1][j]
            else:
                temp=make_tuple(temp)
                temp1=(float(temp[0]),float(temp[1]))
                edge.append(temp1)
                temp=""
        if temp != "":
            temp=make_tuple(temp)
            temp1=(float(temp[0]),float(temp[1]))
            edge.append(temp1)
        graph[int(lines[i*2])]=edge
    return graph  
        
def find_shortest_path(name_txt_file, source, destination):
    graph = read_graph(name_txt_file)
    S=[]
    F=[]
    Path=dict()
    d=dict()
    hq.heappush(F,(0.,source))
    Path[source]=[source]
    d[source]=0.
    while len(F)!=0:
        f=hq.heappop(F)
        S.append(f)
        for node in graph[f[1]]:
            S_node=[]
            F_node=[]
            for i in range(len(S)):
                S_node.append(S[i][1])
            for i in range(len(F)):
                F_node.append(F[i][1])
            if node[0] not in S_node and node[0] not in F_node:
                d[node[0]]=d[f[1]]+node[1]
                hq.heappush(F,(d[node[0]],node[0]))
                Path[node[0]]=Path[f[1]][:]
                Path[node[0]].append(node[0])
            elif d[f[1]]+node[1]<d[node[0]]:
                d[node[0]]=d[f[1]]+node[1]
                for i in range(len(F)):
                    if F[i][1]==node[0]:
                        F[i]=(d[node[0]],node[0])
                        Path[node[0]]=Path[f[1]][:]
                        Path[node[0]].append(node[0])
                temp=[]
                for i in range(len(F)):
                    ff=hq.heappop(F)
                    hq.heappush(temp,ff)
                F=temp
    if destination in d.keys():
        return d[destination], Path[destination]
    else:
        return float("inf"), [] 

def F(graph, num_step, source, destination):
    if num_step==0:
        if destination==source:
            return 0, [source]
        else:
            return float("inf"), []
    child=[]
    path=[]
    for node in graph[source]:
        temp = F(graph, num_step-1, node[0], destination)
        child.append(temp[0] + node[1])
        path.append(temp[1])
    if len(child)==0:
        if source==destination:
            return 0, [source]
        else:
            return float("inf"), []
    temp_min=np.min(child)
    min_path=path[np.argmin(child)][:]
    previous=F(graph, num_step-1, source, destination)
    minimum = np.min([temp_min,previous[0]])
    if temp_min<previous[0]:
        min_path.insert(0,source)
    else:
        min_path=previous[1][:]
    return minimum, min_path

def find_negative_cicles(name_txt_file):
    graph = read_graph(name_txt_file)
    N=len(graph)
    for source,source_child in graph.items():
        for destination, destination_child in graph.items():
            temp_N=F(graph, N, source, destination)
            temp_n=F(graph, N-1, source, destination)
            path=[]
            if temp_N[0]<temp_n[0]:
                path=temp_N[1][:]
                start=0
                end=0
                for end in range(1,len(path)):
                    for start in range(0,end):
                        if path[end]==path[start]:
                            return path[start:end+1]
    return []











                  
#print(find_negative_cicles("../test.txt"))
 
