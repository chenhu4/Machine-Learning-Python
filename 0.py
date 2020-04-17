# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:53:00 2020

@author: 76754
"""



from sklearn.neighbors import KNeighborsRegressor
data = [[1,2], [2,3], [-1,0]]
target= [1, 3, 2]
neigh = KNeighborsRegressor(n_neighbors=2)
neigh.fit(data, target)

print(neigh.predict([[0,0]]))

import math
data=[[1,2],[2,3],[-1,0]]
label=[1,3,2]
target=[[0,0]]
k=2
def distance(data1,data2):
    a=data1[0]
    b=data1[1]
    c=data2[0]
    d=data2[1]
    return math.sqrt((a-c)**2+(b-d)**2)


def knn(k,data,target):
    tmp={}
    output=[]
    label1=[]
    for i in range(len(target)):
        for index,value in enumerate(data):
            tmp[distance(target[i],value)]=index
        near=sorted(tmp.keys())
        for j in range(k):
            label0=tmp[near[j]]
            label1.append(label[label0])
        output.append(sum(label1)/k)
        return output    

knn(k,data,target)