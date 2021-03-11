#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2016-2021
# Álvaro García-Recuero, algarecu@gmail.com
#
# This file is part of the PPANF framework

import random
import networkx as nx
from hashlib import sha1


def generate_preferential_attachment ( size ):
	k = 2
	if size > k:
		G = nx.Graph ()
		G.add_nodes_from (range (k))
		G.add_edge (0, 1)
		node_array = [G.nodes ()[0], G.nodes ()[1]]
		for i in range (k + 1, size):
			x = random.choice (node_array)
			G.add_node (i)
			G.add_node (x)
			G.add_edge (i, x)
			node_array.append (i)
			node_array.append (x)
		return G
	return None


def generate_lattice_graph ( n ):
	if n < 1:
		return None
	G = nx.Graph ()
	if n == 1:
		G.add_node (1)
		return G
	for i in range (0, n):
		for j in range (1, n):
			node = i * n + j
			G.add_edge (node, node + 1)
	for i in range (0, n - 1):
		for j in range (1, n + 1):
			node = i * n + j
			G.add_edge (node, node + n)
	return G


def parse(filename):
	G = nx.Graph ()
	nodes = set ()
	split_string = " "  # Google and Enron use tabs, Twitter and Facebook use spaces
	datadir = "./data/"

	with open (datadir + filename) as graph_file:
		for line in graph_file:
			try:
				n1, n2 = line.split(split_string)
			except ValueError:  # Some datasets use spaces, some tabs.
				n1, n2 = line.split("\t")

			if filename == 'mastodon_combined.txt':
				node1 = int (sha1(n1.encode ("utf-8")).hexdigest(), 16)
				node2 = int (sha1(n2.encode ("utf-8")).hexdigest(), 16)
			else:
				node1 = int(n1)
				node2 = int(n2)

			if node1 not in nodes:
				nodes.add (node1)
				G.add_node (node1)

			if node2 not in nodes:
				nodes.add (node2)
				G.add_node (node2)

			G.add_edge(node1, node2)

	return G