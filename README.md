# pphanf
Code for ppanf

## Usage
- python src/run_hanf.py --graph filename --depth bfsdepth --precision hll_pbits

## Usage Example
- pipenv check
- pipenv sync
- pipenv run python src/run_hanf.py --graph facebook_combined.txt --depth 4 --precision 4

You should get something like this,
```
HyperANF in Python (translated by @algarecu)
  
  optional arguments:
    -h, --help            show this help message and exit
    --graph GRAPH         Enter filename of graph
    --depth DEPTH         Max depth crawl
    --precision PRECISION
                          HyperLogLog precision
  Graph contains 4039 nodes.
  Starting HyperANF...
  t=0
  t=1
  t=2
  t=3
  t=4
  The HyperANF balls:  [1, 338, 773, 1158]
  HyperANF has reached depth of 5
  2021-03-11 22:05:49.715699 2021-03-11 22:05:36.070302 HyperANF0:00:13.645397
  Starting BFS...
  2021-03-11 22:07:31.687025 2021-03-11 22:05:49.715943 Bfs0:01:41.971082
  The BFS balls:  [1, 347, 1171, 1742]
  BFS has reached depth of 5
  The max depth in the graph is:5
  Absolute Error for each t in depth_range:
   [0, 9, 398, 584]
  Percentage Error for each t in depth_range:
   [0.0, 2.5936599423631126, 33.98804440649018, 33.524684270952925]
```

For the final network metrics (approximated and actual/raw ) run this command, which will take a while to finish while it seemingly produces no output, roughly as indicated in our results.
- pipenv run python src/run_small_world.py

[Experimental] In case of willing to see the distributions of each graph run this time consuming command, as it will take a while to finish while it seemingly produces no output.
- pipenv run python src/run_probability_distribution.py

## Datasets
- All datasets are provided here when possible according to the size limit of github. Else, ask for a link to it and will provide it.
