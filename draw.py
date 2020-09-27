# -*- coding: utf-8 -*-

import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import random
from copy import deepcopy


class City:
    graph = g = nx.Graph()
    node_positions = []
    edges = []  # only used in generate_city()
    nodes = []  # only used in generate_city()


def load_city():
    edgelist = pd.read_csv('data/edge.csv')
    nodelist = pd.read_csv('data/nodes.csv')
    

    g = nx.Graph()

    for i, element in edgelist.iterrows():
        g.add_edge(element[0], element[1], weight=element[2])

    for i, element in nodelist.iterrows():
        g.nodes[element['id']].update(element[1:].to_dict())

    

    city = City()
    city.graph = g
   
    
    city.node_positions = {node[0]: (node[1]['x'], node[1]['y']) for node in city.graph.nodes(data=True)}

    return city

def visualize_city(city):

    fig = plt.figure(dpi=200, figsize=[20, 20])
    ax = fig.add_subplot(111)
    draw_city_on_axes(city, ax)
    plt.axis('square')
    




def draw_city_on_axes(city,ax):
    number_id = 0
   
    node_positions = {node[0]: (node[1]['x'], node[1]['y']) for node in city.graph.nodes(data=True)}
    label_positions = {node[0]: (node[1]['x'] - 15, node[1]['y'] + 10) for node in city.graph.nodes(data=True)}
    node_labels = {}
    for node in city.graph.nodes(data=True):
        node_labels.update({node[0]: node[0]})
    nx.draw_networkx_nodes(city.graph, pos=city.node_positions, node_size=2, node_color='black', alpha=0.2, ax=ax)
    nx.draw_networkx_labels(city.graph, pos=label_positions, labels=node_labels, font_size=2, font_color='black', horizontalalignment='center', verticalalignment='center', ax=ax)
    nx.draw_networkx_edges(city.graph, pos=city.node_positions, edge_color='blue', alpha=0.2, ax=ax)
    bbox = {'ec':[1,1,1,0], 'fc':[1,1,1,0]}
    # hack to label edges over line (rather than breaking up line)
    edge_labels = nx.get_edge_attributes(city.graph,'weight')
    nx.draw_networkx_edge_labels(city.graph, pos=city.node_positions, edge_labels=edge_labels, font_size=2)


def draw_current_node_on_axes(nodeID):
	position = load_city().node_positions[nodeID]
	# dic_position = {}
	# dic_position[nodeID] = position
	# print(dic_position)
	# nx.draw_networkx_nodes(city.graph, pos=dic_position, node_size=5, node_color='red', alpha=0.2, ax=ax)

