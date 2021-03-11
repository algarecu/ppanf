#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2016-2021
# Álvaro García-Recuero, algarecu@gmail.com
#
# This file is part of the PPANF framework

import random
import networkx as nx
import fnmatch
import os

def parse(filename):
    G = nx.Graph()
    datadir = "./data/"
    for dir_, _, files in os.walk(datadir):
        for fileName in files:
            relFile = os.path.join(datadir, fileName)
            if fnmatch.fnmatch(fileName, 'facebook_combined.txt') or fnmatch.fnmatch(fileName, 'twitter_combined.txt') or fnmatch.fnmatch(filename, 'mastodon_combined.xt'):
                split_string = " "
            else:
                split_string = "\t"
    graph_file = open(datadir + filename, 'rb') # @TODO nodetype=int, delimiter=split_string
    G = nx.read_edgelist(graph_file)
    graph_file.close()
    return G
