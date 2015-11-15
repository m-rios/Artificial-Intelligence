import math


def parse_links(path, nodes):
    city_map = {}
    f = open(path, 'r')

    # get rid of the first line
    f.readline()

    for line in f.readlines():
        node = line.split(';')
        f = node[0]
        t = node[1].rstrip()
        distance = get_distance(nodes[t],nodes[f])
        if f in city_map:
            city_map[f].append((t, distance))
        else:
            city_map[f] = [(t, distance)]
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


def get_distance(pos1,pos2):
    vec = [pos1[0]-pos2[0],pos1[1] - pos2[1]]
    return math.sqrt(vec[0]**2 + vec[1]**2)
