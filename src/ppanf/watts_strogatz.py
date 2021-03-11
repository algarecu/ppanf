#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2016-2021
# Álvaro García-Recuero, algarecu@gmail.com
#
# This file is part of the PPANF framework

import networkx as nx
import math
from util import small_world_coefficient
import matplotlib.pyplot as plt
import numpy as np

n = 100
k = 4

coeffs = []
ps = []

for i in range (40):
	p = math.pow (10, -i / 10)
	G = nx.watts_strogatz_graph (n, k, p)
	coeffs.append (small_world_coefficient (G))
	ps.append (p)

print (coeffs)
plt.ylabel ("Small world coefficient")
plt.xlabel ("i")
plt.plot (np.arange (0, 4, 4 / len (coeffs)), coeffs)
plt.plot(coeffs)
plt.show ()