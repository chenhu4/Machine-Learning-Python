# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 22:16:43 2020

@author: 76754
"""

import matplotlib.pyplot as plt
x=np.arange(1,11)
y=np.array([5.56,5.70,5.91,6.40,6.80,7.05,8.90,8.70,9.00,9.05])
T=np.array([0]*len(x),dtype='float64')
for i in range(100):
    r,L,f=Boosting_tree(x,y)
    y=r
    T+=f
    if L<0.05:
        break
    
def find_threshild(x):
    if len(x)==0:
        return 
    thresh=[i+0.5 for i in x]
    return thresh
def Boosting_tree(x,y):
    rss_all=[]   
    thresh=find_threshild(x)
    for i in thresh:
        left=np.mean(y[x<i])
        right=np.mean(y[x>=i])
        rss=sum((y[x<i]-left)**2)+sum((y[x>=i]-right)**2)
        rss_all.append(rss)
    min_index=rss_all.index(min(rss_all))
    seg=thresh[min_index]
    left1=np.mean(y[x<seg])
    right1=np.mean(y[x>=seg])  
    f=[]
    for j in x:
        if j<seg:
            f.append(left1)
        else:
            f.append(right1)
    f=np.array(f)
    r=y-f
    L=sum((f-y)**2)
    return r,L,f

        
plt.plot(x,y)
plt.plot(x,T)        