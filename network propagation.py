# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 13:59:58 2021

@author: Ji
"""


import networkx as nx
import numpy as np
import  pandas  as pd
np.set_printoptions(suppress=True)

def read_excel(x):
    df = pd.read_excel(x)
    df_li = df.values.tolist()
    return(df_li)

node1, node2, weight = np.loadtxt('Ecoil_network_0.7.txt',dtype=str,delimiter=',',unpack=True)
G = nx.Graph()

for i in range(len(node1)):
    G.add_edge(node1[i], node2[i])

def ff(b):
    f = b
    for i in range(40):
        f = 0.7*np.dot(A1,f)+0.3*b
    return f

A = nx.to_numpy_array(G)
D = A.sum(axis=0)

A1 = A
for i in range(len(A)):
    for j in range(len(A)):
        if D[i]*D[j] !=0:
            A1[i][j] = A1[i][j]/(D[i]*D[j])**0.5
        else:
            A1[i][j] = A1[i][j]
            
b = np.loadtxt('New Text Document.txt')

f = ff(b)

#for j in range(20):
#    f= ff(f)
#    print(np.mean(np.sort(f,axis=0)[-10:],axis=0))
#    f = f + b


data = pd.DataFrame(f)
writer = pd.ExcelWriter('A-test-0.7.xlsx')       # 写入Excel文件
data.to_excel(writer, 'page_1', float_format='%.5f')        # ‘page_1’是写入excel的sheet名
writer.save()
writer.close()