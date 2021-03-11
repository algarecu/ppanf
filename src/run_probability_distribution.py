#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2016-2021
# Álvaro García-Recuero, algarecu@gmail.com
#
# This file is part of the PPANF framework

from ppanf.graph_generators import parse
from ppanf.util import path_length_probability_distribution

import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

G = parse("mastodon_combined.txt")
distribution = path_length_probability_distribution(G)

fig1, ax1 = plt.subplots()
ax1.plot([1, 10, 100], [1, 2, 3])
ax1.set_xscale('log')
ax1.set_xticks([1, 10, 100])
ax1.get_xaxis().set_major_formatter(ScalarFormatter())

plt.loglog(distribution)
plt.show()
plt.savefig('mastodon_combined.png', bbox_inches='tight')

########################
G = parse("twitter_combined.txt")
distribution = path_length_probability_distribution(G)

fig1, ax1 = plt.subplots ()
ax1.plot([1, 10, 100], [1, 2, 3])
ax1.set_xscale('log')
ax1.set_xticks([1, 10, 100])
ax1.get_xaxis().set_major_formatter(ScalarFormatter())

plt.loglog(distribution)
plt.show()
plt.savefig('twitter_combined.png', bbox_inches='tight')

########################
G = parse("facebook_combined.txt")
distribution = path_length_probability_distribution(G)

fig1, ax1 = plt.subplots ()
ax1.plot ([1, 10, 100], [1, 2, 3])
ax1.set_xscale ('log')
ax1.set_xticks ([1, 10, 100])
ax1.get_xaxis ().set_major_formatter(ScalarFormatter())

plt.loglog(distribution)
plt.show()
plt.savefig('facebook_combined.png', bbox_inches='tight')