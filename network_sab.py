# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 14:46:44 2021

@author: Ji
"""

import networkx as nx
import numpy as np
import  pandas  as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

node1, node2, weight = np.loadtxt('Ecoil_network_0.7.txt',dtype=str,delimiter=',',unpack=True)
a = np.loadtxt('out.txt',dtype=str,delimiter='	')
G = nx.Graph()
drug = ['AMK','GEN','TOB','TET','CLA','ERY','CHL','CIP','LEV','NAL','TRI','OXA','CEF','NIT','KAN','PNG','ROX','SUL']

def snode(j):
    s = set()
    for i in range(1,len(a)):
        if float(a[i][j]) >=0.0065:
            s.add(a[i][0])
    return s

def get_separation_within_set(nodes_from, lengths=None):
    values = []
    # Distance to closest node within the set (A or B)
    for source_id in nodes_from:
        inner_values = []
        for target_id in nodes_from:
            if source_id == target_id:
                continue
            d = nx.shortest_path_length(G, source_id, target_id)
            inner_values.append(d)
        values.append(np.min(inner_values))
    return values


def get_separation_between_sets(nodes_from, nodes_to):
    values = []
    for source_id in nodes_from:
        source_to_values = []
        for target_id in nodes_to:
            d = nx.shortest_path_length(G, source_id, target_id)
            source_to_values.append(d)
        values.append(np.min(source_to_values))
    for target_id in nodes_to:
        target_to_values = []
        for source_id in nodes_from:
            d = nx.shortest_path_length(G, target_id, source_id)
            target_to_values.append(d)
        values.append(np.min(source_to_values))

    return values
    

def get_separation(nodes_from, nodes_to):
    dAA = np.mean(get_separation_within_set(nodes_from))
    dBB = np.mean(get_separation_within_set(nodes_to))
    dAB = np.mean(get_separation_between_sets(nodes_from, nodes_to))
    d = dAB - (dAA + dBB) / 2.0
    return d


for i in range(len(node1)):
    G.add_edge(node1[i], node2[i])

for i in range(1,18):
    sa = snode(i)
    for j in range(i+1,19):
        sb= snode(j)
        #print(drug[i-1],drug[j-1],len(sa),len(sb))
        #venn2([set(sa), set(sb)],set_labels = (drug[i-1], drug[j-1]))
        #plt.show()
        print(drug[i-1],drug[j-1],len(sa & sb)/len(sa|sb),get_separation(sa,sb))
        #get_separation_between_sets(sa,sb)
