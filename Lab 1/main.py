#!/usr/bin/python
from parser import *
from collections import namedtuple

LEVEL_UP = -1
Node = namedtuple("Node","parent, name, distance")

def compute_children(parent, _map):
    '''
    Extracts node's children from _map, and converts them to implicit tree node
    :param parent: the name (key) of the node to exploit
    :param _map: the dictionary node -> children
    :return: a list of tree nodes
    '''
    (name, distance) = _map[parent]
    children = []
    for child in children:
        children.append(Node(parent, name, distance))
    return children


def depth_limited_search(_from, _to, _map, frontier, limit, depth=1,
                         visited={}):
    '''
    Performs a depth-first bounded search

    :param _from: key of an initial node
    :param _to: key of a destination node
    :param _map: dictionary containing the problem search space
    :param frontier: list of nodes pending of being visited
    :param visited: list of nodes already visited
    :param depth: level of the search tree where the algorithm currently is
    :param limit: depth of the tree at which to stop the search
    :return: a list of ordered nodes, representing the path from _from to _to
    '''
    # if no solution found and no nodes left, the solution is not at this depth
    if frontier is None:
        return None
    # if there are nodes left in frontier, and we're within limit depth,
    # keep exploiting tree
    elif depth <= limit:
        # end of level, must climb up
        if _from is LEVEL_UP:
            visited[_from.name] = None
            _from = frontier.pop()
            depth_limited_search(_from, _to, _map, frontier, limit, --depth, visited)
        # Compute children and insert them to top of frontier
        else:
            visited[_from.name] = None
            children = compute_children(_from.name, _map)
            frontier = children + frontier
            _from = frontier.pop()
            depth_limited_search(_from ,_to, _map, frontier, limit, depth, visited)
    else:
        # Limit reached, jump to next node in the frontier
        visited[_from.name] = None
        # pop first LEVEL_UP, and get next node in frontier
        frontier.pop()
        _from = frontier.pop()
        depth_limited_search(_from, _to, _map, frontier, limit, --depth, visited)

    return path


if __name__ == '__main__':
    link_path = "links.csv"
    node_path = 'nodes.csv'

    nodes = parse_nodes(node_path)
    city_map = parse_links(link_path, nodes)
    print nodes
    iterative_depth_first_recursive()
