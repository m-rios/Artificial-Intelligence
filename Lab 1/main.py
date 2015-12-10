#!/usr/bin/python
from parser import *
from collections import namedtuple

Node = namedtuple("Node","parent, name, distance, depth")

def get_children(parent,city_map,visited):
    children = city_map[parent.name]
    filtered_children = []
    for child in children:
        if child[0] not in visited:
            filtered_children.append(Node(parent.name,child[0],child[1],parent.depth+1))
    return filtered_children

def iterative_deepening_search(cityMap, start, goal):
    path = None
    max_depth = 0
    start = Node(None,start,0,0)
    while path is None:
        path = depth_limited_search(cityMap,start,[],[],{},max_depth, goal)
        max_depth += 1
    return get_path(goal,path)

def depth_limited_search(cityMap, current, visited, frontier, path, max_depth, goal):
    if current.name == goal:
        path[current.name] = current
        return path
    elif not frontier and current.depth >= max_depth:
        return None
    if current.depth < max_depth:
#         add children
        children = get_children(current,cityMap,visited)
        frontier = children + frontier
    visited.append(current.name)
    next_node = frontier.pop(0)
    path[current.name] = current
    return depth_limited_search(cityMap, next_node, visited, frontier, path, max_depth, goal)


def get_path(goal, path):
    current = path[goal]
    real_path = []
    while current.parent is not None:
        real_path = [current.name] + real_path
        current = path[current.parent]
    return [current.name] + real_path

if __name__ == '__main__':
    link_path = "links.csv"
    node_path = 'nodes.csv'

    nodes = parse_nodes(node_path)
    city_map = parse_links(link_path, nodes)
    path = iterative_deepening_search(city_map,'Brickebacken','Hagaby')
    print path
