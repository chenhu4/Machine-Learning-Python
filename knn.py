# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:53:00 2020

@author: 76754
"""
import math
k=3
import numpy as np
data=[[ 3.88951125,  2.14164428,  3.79599499,  3.54037238,  0.49345561],
       [ 2.87323353,  3.84530452,  1.29070084,  0.13235598,  2.35567639],
       [ 0.63684627,  2.12126517,  0.49796594,  1.59431037,  0.79019315],
       [ 0.96113571,  2.77874645, -0.32525298,  2.854477  ,  1.16563593],
       [ 2.76001288, -0.43670643,  3.58027062,  4.37925925,  3.40281813],
       [ 3.46165174, -0.37814231,  2.62153281,  4.48472353,  2.6965205 ],
       [ 1.60657671,  4.34638861, -0.18015312, -0.16024361,  1.27418687],
       [-0.35007517,  0.25067709,  0.84768086,  3.05895676,  0.77691708],
       [ 2.04955466,  4.21203697,  0.77569219,  2.13577824,  0.82163468],
       [ 1.28578269, -0.29457374,  1.66790371,  4.50966477,  0.54175918]]
#label=[1,0,1,0,1,1,1,1,0,0]
label=[-0.86846097, -0.48399104, -1.36562909, -0.15892619,  0.8553947 ,
        -0.94374444,  0.60519648, -0.00509691, -0.46844946, -1.06941832]
target=[0.85889086, 0.52814978, 0.59720879, 0.34708483, 0.83180433]

##################sklearn###############
from sklearn.neighbors import KNeighborsRegressor

neigh = KNeighborsRegressor(n_neighbors=3)
neigh.fit(data, label)

print(neigh.predict([target]))

#################Scratch################
def distance(data1,data2):
'''
input: two data samples
output: distance between two samples

data1:sample1 
data2:sample2

idea: Calculate distance between two samples by using formula sqrt(sum((s1.-s2.)^2))
'''
    dist=0.0
    for i in range(len(data1)):
        dist+=(data1[i]-data2[i])**2
    return math.sqrt(dist)
'''
def knn(k,data,target):


    new=[]
    for i in data:
        dist=distance(i,target)
        new.append((dist,i))
    new.sort(key=lambda a: a[0])
    output_index=[]
    for j in range(len(new[:k])):
        output_index.append(data.index(new[:k][j][1]))
    return output_index
'''
def find_k_neighbours(k,data_in,target):
'''
       
input: Total number of nearest neighbours,training data, testing data
output: The #k index of the nearest neighbours

idea: 
1.using for loop to calculate distances between all the traing data and the testing data.
2.sorting the tuple(distance,index) by distance. 
3.select the smallest k tuples and output the index.
'''
    tmp=[]
    for index,item in enumerate(data_in):
        dist=distance(item,target)
        tmp.append((dist,index))
        tmp.sort(key=lambda x:x[0])
    output_index=[]
    for i in range(k):    
        output_index.append(tmp[:k][i][1])
    return output_index


def prediction(output_index,target,label,k,classification):
    if classification==1:# knn classification
        result=([label[i] for i in output_index])
        final=max(result,key=result.count)
        return final
    else:#knn regression
        result=([label[i] for i in output_index])
        final=sum(result)/k
        return final
  

out=knn(k,data,target)
prediction(out,target,label,k,classification=0)




# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:43:10 2020

@author: 76754
"""


########################kd tree################################
def calculate_distance(data1,data2):
    dist=0.0
    for item in range(len(data1)):
        dist+=(data1[item]-data2[item])**2
    return math.sqrt(dist)

def closet_point(data,target):
    best=None
    point=None
    for i,item in enumerate(data):
        dist=calculate_distance(item,target)
        if best==None or dist<best:
            best=dist
            point=i
    return point
closet_point(data,target)


def build_kdtree(data,depth=0,k=5):
    n=len(data)
    if n<=0:
        return None
    axis=depth%k
    tmp=sorted(data,key=lambda a:a[axis])
    return {'root': tmp[n//2],
            'left': build_kdtree(tmp[:n//2],depth=depth+1,k=5),
            'right': build_kdtree(tmp[n//2+1:],depth=depth+1,k=5)
            }
tree=(build_kdtree(data,depth=0,k=5))
import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(build_kdtree(data))



def select_close_distance(target,data1,data2):
    if data1 is None:
        return data2
    if data2 is None:
        return data1
    dist1=calculate_distance(data1,target)
    dist2=calculate_distance(data2,target)
    if dist1<dist2:
        return data1
    else:
        return data2
    
def kdtree_closet(tree,target,depth=0):
    if tree is None:
        return None
    next_branch=None
    opposite_branch=None
    axis=depth%k
    
    if tree['root'][axis]<target[axis]:
        next_branch=tree['right']
        opposite_branch=tree['left']
    else:
        next_branch=tree['left']
        opposite_branch=tree['right']
    best=select_close_distance(target,kdtree_closet(next_branch,target,depth=depth+1),tree['root'])
    if calculate_distance(best,target)>math.sqrt((tree['root'][axis]-target[axis])**2):
        best=select_close_distance(target,kdtree_closet(opposite_branch,target,depth=depth+1),best)

kdtree_closet(tree,target,depth=0)

def kdtree_closet(tree,target,depth=0):
    if tree is None:
        return None
    next_branch=None
    opposite_branch=None
    axis=depth%k
    
    if tree['root'][axis]<target[axis]:
        next_branch=tree['right']
        opposite_branch=tree['left']
    else:
        next_branch=tree['left']
        opposite_branch=tree['right']

    best=select_close_distance(target,kdtree_closet(next_branch,target,depth=depth+1),tree['root'])
    if calculate_distance(best,target)>math.sqrt((tree['root'][axis]-target[axis])**2):
        best=select_close_distance(target,kdtree_closet(opposite_branch,target,depth=depth+1),best)

    return best

kdtree_closet(tree,target,depth=0)




def run(tree,node=0,action=None):
    a.append(node)
    print(a)    
    print(tree['root'],'Layer is ',node,action)
    if tree['left']:
        action='left'
        run(tree['left'],node=node+1,action=action)
    if tree['right']:
        action='right'
        run(tree['right'],node=node+1,action=action)
a=[]

run(tree,node=0,action=None)
