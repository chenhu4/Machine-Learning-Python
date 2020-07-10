# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 14:11:47 2020

@author: 76754
"""
import numpy as np
import math
# trainging set
x=np.arange(10)
y=np.array([1,1,1,-1,-1,-1,1,1,1,-1])

#intialize weight vector
w=np.array([0.1]*len(y))

main(x,y,w)
def main(x,y,w):
    f_all=[]
    w_all=[]
    a_ll=[]
    b=[]
    iter=0
    f1=np.array([0]*len(y),dtype='float64')
    while  iter<=100:
        a,f,w,find_min=train(x,y,w)
        f_all.append(f)
        w_all.append(w)
        a_ll.append(a)
        b.append(find_min)
        f1+=f
        signf=[]
        for i in f1:
            if i>0:
                signf.append(1)
            else:
                signf.append(-1)
        
        error_rate=error(signf,y)
        iter+=1
        if error_rate==0:
            break
    return iter,a_ll,f1
# find threshold
def find_threshild(x):
    if len(x)==0:
        return 
    thresh=[i+0.5 for i in x]
    return thresh

# calculate error rate 
def cal_error1(threshold,x,y):
    res=[]
    for i in range(len(y)):
        if x[i]<threshold:
            res.append(1)
        else:
            res.append(-1)
    return res
def cal_error2(threshold,x,y):
    res=[]
    for i in range(len(y)):
        if x[i]>threshold:
            res.append(1)
        else:
            res.append(-1)
    return res
#    
def train(x,y,w):
    thresh=find_threshild(x)
    count1=[]
    count2=[]
    res_all1=[]
    res_all2=[]
    for threshold in thresh:   
        res=cal_error1(threshold,x,y)
        res_all1.append(res)
        count1.append(sum(w[res!=y]))
    
        res=cal_error2(threshold,x,y)
        res_all2.append(res)
        count2.append(sum(w[res!=y]))
        
    if min(count1)<min(count2):
        find_min=count1.index(min(count1))
        #threshold_min=thresh[find_min]
        w_index=[i for i in range(len(res_all1[find_min])) if res_all1[find_min][i]!=y[i]]
        G=res_all1[find_min]
    else:
        find_min=count2.index(min(count2))
        #threshold_min=thresh[find_min]
        w_index=[i for i in range(len(res_all2[find_min])) if res_all2[find_min][i]!=y[i]]
        G=res_all2[find_min]
    e=sum(w[w_index])
    a=round(0.5*math.log((1-e)/e),6)
    z=0
    for i in range(len(G)):
        w[i]=round(w[i]*math.exp(-a*y[i]*G[i]),6)
        z+=w[i] 
    w=w/z
    

    f=a*np.array(G)

    return a,f,w,find_min


def error(signf,y):
    count=sum(signf!=y)
    return count/len(y)




