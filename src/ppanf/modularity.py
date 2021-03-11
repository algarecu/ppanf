#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2016-2021
# Álvaro García-Recuero, algarecu@gmail.com
#
# This file is part of the PPANF framework

import community as community_louvain
import matplotlib.cm as cm
import matplotlib.pyplot as plt

from parsing_graph import parse

# load the karate club graph
graph_filename = "mastodon_combined.txt"
G = parse(graph_filename)

# compute the best partition
partition = community_louvain.best_partition (G)

# draw the graph
pos = nx.spring_layout (G)

# color the nodes according to their partition
cmap = cm.get_cmap ('viridis', max (partition.values ()) + 1)
nx.draw_networkx_nodes (G, pos, partition.keys (), node_size=40,
						cmap=cmap, node_color=list (partition.values ()))
nx.draw_networkx_edges (G, pos, alpha=0.5)
plt.show ()