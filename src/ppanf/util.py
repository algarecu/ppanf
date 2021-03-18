#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2016-2021
# Álvaro García-Recuero, algarecu@gmail.com
#
# This file is part of the PPANF framework

from ppanf.hyperanf import HyperANF
from ppanf.graph_generators import generate_lattice_graph

import math
import networkx as nx
from datetime import datetime


def small_world_coefficient(G, name):
	"""
	Calculate a coefficient between -1 and 1 indicating how strong the small world phenomenon occurs.
	A coefficient close to 0 indicates a strong influence of small world
	Positive values indicate a graph with more random characteristics.
	Negative values indicate regularity/lattice-like graphs
	"""
	# Generate random graph with equivalent amount of nodes and edges
	R = nx.gnm_random_graph (len (G.nodes ()), len (G.edges ()))

	# Generate lattice graph with same amount of vertices
	L = generate_lattice_graph (int (math.sqrt (len (G.nodes ()))))

	# Check how average path length of random graph R compares to G
	l = average_path_length (R) / average_path_length (G)
	print ("Average Length Path of R/G is: " + str (l))

	# Check how average clustering coefficient of graph compares to that of a lattice graph
	# c = nx.average_clustering (G) / float((nx.average_clustering (L)))
	if nx.average_clustering (L) == 0:
		c = nx.average_clustering(G)
		print("Avg. Clustering coeff. for G/L is the coeff. of G which is " + str(c))
		# c = average_clustering_coefficient (G)
	else:
		c = nx.average_clustering (G) / float(nx.average_clustering (L))
		print ("Avg. Clustering coeff. for G/L is " + str (c))
		# c = average_clustering_coefficient (G) / float(average_clustering_coefficient (L))

	print("Clustering Coefficient of G/L: " + str(c))

	# Calculate coefficient
	smc = (l - c)
	print ("Small World Coefficient l - c: " + str(smc) + " of " + str(name))
	return


def small_world_coefficient_raw(G, name):
	"""
	Calculate a coefficient between -1 and 1 indicating how strong the small world phenomenon occurs.
	A coefficient close to 0 indicates a strong influence of small world
	Positive values indicate a graph with more random characteristics.
	Negative values indicate regularity/lattice-like graphs
	"""
	# Generate random graph with equivalent amount of nodes and edges
	R = nx.gnm_random_graph (len (G.nodes ()), len (G.edges ()))

	# Generate lattice graph with same amount of vertices
	L = generate_lattice_graph (int (math.sqrt (len (G.nodes ()))))

	# Check how average path length of random graph R compares to G
	l = average_path_length_raw (R) / average_path_length_raw (G)
	print ("Average Length Path of R/G is: " + str (l))

	# Check how average clustering coefficient of graph compares to that of a lattice graph
	if nx.average_clustering(L) == 0:
		c = nx.average_clustering (G)
		print("Avg. Clustering RAW coeff. for G/L is the coeff. of G which is " + str(c))
		# c = average_clustering_coefficient (G)
	else:
		c = nx.average_clustering (G) / float (nx.average_clustering(L))
		print ("Avg. Clustering RAW coeff. for G/L is " + str (c))
		# c = average_clustering_coefficient (G) / average_clustering_coefficient (L)
	print ("Clustering Coefficient of G/L: " + str (c))

	# Calculate coefficient
	print ("Small World Coefficient l - c: " + str (l - c) + " of " + str (name))
	return


def path_length_probability_distribution(G):
	"""
	For all path lengths t (corresponding to index + 1) give the probability that
	between a random pair of nodes <x,y>: d(x,y) = t
	"""
	hb = HyperANF (G, 1, 4)
	nr_of_paths_of_length_per_node = dict ()

	for v in G.nodes ():
		nr_of_paths_of_length_per_node[v] = [
			hb.nr_of_nodes_with_distance_from (v, t) for t in
			range (hb.get_max_t ())]

	# For all nodes, sum the number of paths of length t
	nr_of_paths_of_length = [
		sum ([nr_of_paths_of_length_per_node[v][t] for v in G.nodes ()]) for t
		in range (hb.get_max_t ())]

	# Count number of paths. Don't count paths of length 0
	nr_of_paths_total = sum (nr_of_paths_of_length[1:])
	return [(nr_of_paths_of_length[i] / float (nr_of_paths_total)) * 100 for i
			in range (len (nr_of_paths_of_length))]


def average_degree(G):
	return sum([G.degree (v) for v in G.nodes()]) / float(len(G.nodes()))


def average_clustering_coefficient(G):
	average_clustering_coefficient = sum(nx.clustering(G, G.nodes())) / float(len(G.nodes()))
	return average_clustering_coefficient


def average_path_length ( G ):
	"""
	Estimate the average path length using HyperANF
	"""
	hanf_start = datetime.now ()
	# Run HyperANF to be able to estimate paths
	hb = HyperANF(G, 4, 4)
	nr_of_paths_of_length_per_node = dict ()

	for v in G.nodes ():
		nr_of_paths_of_length_per_node[v] = [
			hb.nr_of_nodes_with_distance_from (v, t) for t in
			range (hb.get_max_t ())]

	# For all nodes, sum the number of paths of length t
	nr_of_paths_of_length = [
		sum ([nr_of_paths_of_length_per_node[v][t] for v in G.nodes ()]) for t in range (hb.get_max_t ())]

	# Count number of paths. Don't count paths of length 0
	nr_of_paths_total = sum (nr_of_paths_of_length[1:])

	# The sum
	the_sum = sum ([t * nr_of_paths_of_length[t] for t in range (1, hb.get_max_t ())]) / float (nr_of_paths_total)

	hanf_stop = datetime.now ()
	print (hanf_stop, hanf_start, hanf_stop - hanf_start)
	return the_sum


def average_path_length_raw(G):
	"""

	:param G:
	:return: sum of path lengths
	"""
	raw_start = datetime.now ()
	the_sum = nx.average_shortest_path_length(G)
	raw_stop = datetime.now ()
	print (raw_stop, raw_start, raw_stop - raw_start)
	return the_sum