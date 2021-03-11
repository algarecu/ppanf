#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2016-2021
# Álvaro García-Recuero, algarecu@gmail.com
#
# This file is part of the PPANF framework

import ppanf.graph_generators as gg
from ppanf.util import small_world_coefficient, small_world_coefficient_raw


print("Parsing Enron graph")
enron = gg.parse("email-Enron.txt")
print("Done parsing Enron, calculating coefficient for Enron")
small_world_coefficient(enron, "enron")
small_world_coefficient_raw(enron, "enron_bfs")

print ("Parsing Twitter graph")
twitter = gg.parse ("twitter_combined.txt")
print ("Done parsing Twitter, calculating coefficient for Twitter")
small_world_coefficient (twitter, "twitter")
small_world_coefficient_raw (twitter, "twitter_bfs")

print ("Parsing Facebook graph")
facebook = gg.parse ("facebook_combined.txt")
print ("Graph contains " + str (len (facebook)) + " nodes.")
print ("Done parsing Facebook, calculating coefficient for Facebook")
small_world_coefficient (facebook, "facebook")
small_world_coefficient_raw (facebook, "facebook_bfs")

print ("Parsing Mastodon graph")
mastodon = gg.parse ("mastodon_combined.txt")
print ("Done parsing Mastodon, calculating coefficient for Mastodon")
small_world_coefficient(mastodon, "mastodon")
small_world_coefficient_raw(mastodon, "mastodon_bfs")