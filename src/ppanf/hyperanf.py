#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2016-2021
# Álvaro García-Recuero, algarecu@gmail.com
#
# This file is part of the PPANF framework

from ppanf.hyperloglog import HyperLogLog
from joblib import Parallel, delayed, parallel_backend
import multiprocessing
import time


class HyperANF:
	def __init__ ( self, G, b, p):
		"""
		Defines the HyperANF algorithm

		param G: the input graph
		param b: balls radius or depth
		param p: hll precision

		returns: len(consecutive run of zeroes + 1)
		"""
		# Init precision
		self.p = p

		# Init max radius
		self.b = b

		# Init hll counters, where index = t
		self.balls = dict()

		# Init one hll counter per node
		self.c = dict()

		# Se parallelism level
		num_cores = multiprocessing.cpu_count()

		# for v in G: # not very efficient for large graphs
		#     self.balls[v] = []
		with parallel_backend('threading'):
			Parallel()(delayed(self.myfunctionA)(v) for v in G)

		# for v in G:
		# 	self.c[v] = HyperLogLog(p)
		with parallel_backend('threading'):
			Parallel()(delayed(self.myfunctionH)(self.p, v) for v in G)

		# For all vertices in G, |B(v,0)|
		# for v in G:
		# 	self.c[v].add(v)
		# 	self.balls[v].append(self.c[v])
		with parallel_backend('threading'):
			Parallel()(delayed(self.myfunctionB)(v) for v in G)

		# Run HyperANF until counters stabilize
		changed = True
		self.t = 0
		while changed and self.t <= self.b:
			changed = False
			pairs = dict()
			for v in G:
				a = self.c[v].copy()
				for w in G.neighbors(v):
					a.union(self.c[w])
				pairs[v] = a
				# Store <v, a> pair
				self.balls[v].append(a)
			# Check if counters are unchanged and update c
			for v in G:
				changed = changed or not pairs[v].equals(self.c[v])
				self.c[v] = pairs[v]
			print("t=" + str(self.t))
			self.t += 1

	def myfunctionA (self, v):
		self.balls[v] = []
		return

	def myfunctionH (self, p, v):
		self.c[v] = HyperLogLog(p)
		return

	def myfunctionB (self, v):
		self.c[v].add(v)
		self.balls[v].append(self.c[v])
		return

	def hyper_run_ball_sizes ( self, v, t ):
		return int(self.balls[v][t].size())

	def get_max_t (self):
		return self.t

	def nr_of_nodes_with_distance_from ( self, v, t ):
		if t == 0:
			return 1
		elif t >= self.get_max_t():
			return 0
		else:
			return int(self.balls[v][t].size() - self.balls[v][t - 1].size())
