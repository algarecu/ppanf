#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2016-2021
# Álvaro García-Recuero, algarecu@gmail.com
#
# This file is part of the PPANF framework

class Bfs:
    def __init__(self, G, depth):
        self.depth = depth
        # Index = Distance from v
        self.balls = dict()
        for v in G.nodes():
            self.balls[v] = list()
        # Bfs for all vertices
        for v in G.nodes():
            self.bfs(G,v)

    def bfs(self, G, seed):
        """
        Breadth first Search graph traversal to update balls
        """
        # Init BFS params
        seen = set()
        q_followers_friends = [seed]
        # Add depth to a dictionary as {node_id: index}, where index = distance
        self.balls[seed].append({seed})
        # Keep a record of which nodes to visit at depth + 1
        boundary = set()
        depth = 1
        while len(q_followers_friends) != 0 and depth <= self.depth:
            v = q_followers_friends.pop(0)
            # Check which ones not seen
            for n in G.neighbors(v):
                if n not in seen:
                    seen.add(n)
                    boundary.add(n)
            # Extend depth of boundary to next hop:
            # A/ q_followers_friends is empty -> stop.
            # B/ Update the ball with new boundary nodes
            if len(q_followers_friends) == 0:
                q_followers_friends.extend(boundary)
                if len(q_followers_friends) != 0:
                    # next ball is: previous ball + boundary
                    self.balls[seed].append(set(self.balls[seed][depth - 1]))
                    self.balls[seed][depth] |= boundary # bitwise OR operator
                    depth += 1
                boundary = set()

    def get_ball(self, v, t):
        return self.balls[v][t]

    def get_balls(self, v):
        return self.balls[v]

    def get_ball_size(self, v, t):
        return len(self.balls[v][t])

    def number_of_nodes_at_distance_from(self, v, t):
        balls = self.balls[v]
        if t == 0:
            return 1
        elif t >= len(balls):
            return 0
        else:
            return len(balls[t]) - len(balls[t - 1])
