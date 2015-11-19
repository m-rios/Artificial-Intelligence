import math


def parse_links(path, nodes):
    city_map = {}
    f = open(path, 'r')

    # get rid of the first line
    f.readline()

    for line in f.readlines():
        node = line.split(';')
        _f = node[0]
        t = node[1].rstrip()
        if _f in city_map:
            city_map[_f].append((t, nodes[t][0], nodes[t][1]))
        else:
            city_map[_f] = [(t, nodes[t][0], nodes[t][1])]
    f.close()
    return city_map


def parse_nodes(path):
    nodes = {}
    f = open(path, 'r')

    # get rid of the first line
    f.readline()

    for line in f.readlines():
        node = line.split(';')
        nodes[node[0]] = [int(node[1]), int(node[2].rstrip())]

    f.close()

    return nodes
