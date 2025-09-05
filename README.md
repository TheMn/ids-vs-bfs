# Graph Search Algorithm Comparison

This repository contains a Python script, `Compare.py`, that implements and compares the performance of three graph search algorithms:
- Breadth-First Search (BFS)
- Depth-Limited Search (DLS)
- Iterative Deepening Search (IDS)

The script generates a random graph, runs the search algorithms to find a target node, and then plots the number of nodes visited by each algorithm using `matplotlib`.

## Purpose

The main purpose of this script is to provide a visual comparison of the performance of BFS, DLS, and IDS in a sample graph. It serves as a practical demonstration of how these algorithms explore a graph to find a goal.

## Setup

To run this script, you need to have Python 3 installed, along with the `numpy` and `matplotlib` libraries.

You can install the required libraries using pip:

```bash
pip install numpy matplotlib
```

## Usage

To run the script, simply execute it from your terminal:

```bash
python Compare.py
```

When you run the script, it will:
1.  Generate a random graph with a random number of nodes and edges.
2.  Print the total number of nodes and the list of nodes.
3.  Run a series of tests, each with a new random target node.
4.  For each test, it will print the number of nodes visited by BFS, IDS, and DLS.
5.  Finally, it will display a plot comparing the number of nodes visited by each algorithm across the tests.

The plot will show 'bfs', 'ids', and 'dls' performance, helping you visualize their efficiency for the given graph and targets.
