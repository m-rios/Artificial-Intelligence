#!/usr/bin/python
from parser import *


# recursive implementation of the iterative depth-first algorithm
def iterative_depth_first_recursive(map, frontier, visited, depth):
    pass


if __name__ == '__main__':
    link_path = "links.csv"
    node_path = 'nodes.csv'

    nodes = parse_nodes(node_path)
    city_map = parse_links(link_path, nodes)

    print nodes
