#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2016-2021
# Álvaro García-Recuero, algarecu@gmail.com
#
# This file is part of the PPANF framework

from datetime import datetime

from ppanf.parsing_graph import parse
from ppanf.hyperanf import HyperANF
from ppanf.bfs import Bfs

import argparse

# Add arguments
parser = argparse.ArgumentParser(description='HyperANF in Python (translated by @algarecu)', prog='run_hanf.py', usage='%(prog)s [options]')
parser.add_argument('--graph', default='facebook_combined.txt',  help='Enter filename of graph')
parser.add_argument('--depth', default=4, type=int, required=True, help='Max depth crawl')
parser.add_argument('--precision', default=4, type=int, required=False, help='HyperLogLog precision')

parser.print_help()

# Argument parsing
try:
    args = parser.parse_args()
except Exception as e:
    raise e

depth = int(args.depth)
precision = int(args.precision)
graph_filename = args.graph
G = parse(graph_filename)
print ("Graph contains " + str(len(G)) + " nodes.")

if G:
    # Get the nodes
    v = G.nodes()[0]

    print ( "Starting HyperANF..." )
    hanf_start = datetime.now()
    hyper_run = HyperANF(G, depth, precision)
    hanf_stop = datetime.now()
    print ("The HyperANF balls: ", [hyper_run.nr_of_nodes_with_distance_from(v, t) for t in range(depth)])
    print ("HyperANF has reached depth of " + str(hyper_run.get_max_t()))
    print (str(hanf_stop), str(hanf_start), "HyperANF: " + str(hanf_stop - hanf_start) )

    # Absolute errors
    hyper_run_ball_sizes = [hyper_run.nr_of_nodes_with_distance_from(v, i) for i in range(depth)]

    print("Starting BFS...")
    bfs_start = datetime.now()
    bfs_run = Bfs(G,depth)
    bfs_balls = bfs_run.get_balls(v)
    bfs_stop = datetime.now()
    print(str (bfs_stop), str (bfs_start), "Bfs: " + str(bfs_stop - bfs_start) )
    print ("The BFS balls: ", [bfs_run.number_of_nodes_at_distance_from(v, t) for t in range(depth)] )
    print ("BFS has reached depth of " + str(len(bfs_balls)) )
    # Absolute errors
    bfs_run_ball_sizes = [bfs_run.number_of_nodes_at_distance_from(v, i) for i in range(depth)]

# Get the depth
max_depth_range = max(hyper_run.get_max_t(),len(bfs_balls))
print ("The max depth in the graph is:" + str(max_depth_range))

difference = [abs(hyper_run_ball_sizes[i] - bfs_run_ball_sizes[i]) for i in range(depth)]
error_percentages = [100 * (difference[i] / float(bfs_run_ball_sizes[i])) for i in range(depth)]

print ( "Absolute Error for each t in depth_range:\n %s" % difference)
print ( "Percentage Error for each t in depth_range:\n %s" % error_percentages)
