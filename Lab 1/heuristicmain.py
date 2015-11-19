from parser import *
from collections import namedtuple

Node = namedtuple("Node","parent, name, x, y, start_dist, goal_dist")

def get_distance(pos1,pos2):
    vec = [pos1[0]-pos2[0],pos1[1] - pos2[1]]
    return math.sqrt(vec[0]**2 + vec[1]**2)


def select_best(frontier):
    local_frontier = []
    # convert frontier to list
    for key, value in frontier.iteritems():
        local_frontier.append(value)
    min = local_frontier.pop(0)
    while len(local_frontier) > 0:
        candidate = local_frontier.pop(0)
        if min.start_dist + min.goal_dist > candidate.start_dist + candidate.goal_dist:
            min = candidate
    return min


def get_scored_child(parent, current, goal_position):
    # nodes is the node dictionary {node_name}: pos1, pos2
    # goal_position: list of the two positions of goal
    distance_to_parent = get_distance([parent.x,parent.y], [current[1], current[2]])
    goal_dist = get_distance([current[1], current[2]], goal_position)
    return Node(parent.name, current[0], current[1], current[2], parent.start_dist + distance_to_parent, goal_dist)


def get_children(parent,city_map,visited, goal_position):
    # parent is Node
    children = city_map[parent.name]
    filtered_children = []
    for child in children:
        scored_child = get_scored_child(parent, child, nodes, nodes[goal])
        if scored_child.name in visited:
            old = visited[scored_child.name]
            if old.start_dist + old.goal_dist > scored_child.start_dist + scored_child.goal_dist:
                del visited[old.name]
                filtered_children.append(scored_child)
            # elif
        # elif
    return filtered_children


def a_star_search(city_map, start, nodes, goal):
    # start is a Node
    # goal is string
    frontier = {}
    frontier[start.name] = start
    visited = {} #name is key, Node is body
    path = {}
    count = 0
    while frontier:
        current = select_best(frontier)
        print current.name
        if current.name == goal:
            path[current.name] = current
            count += 1
            print count
            return path
        del frontier[current.name]
        visited[current.name] = current
    #     succesors
        children = city_map[current.name]
        path[current.name] = current
        count += 1
        for child in children:
            scored_child = get_scored_child(current, child, nodes[goal])
            if scored_child.name in visited:
                old = visited[scored_child.name]
                if old.start_dist + old.goal_dist > scored_child.start_dist + scored_child.goal_dist:
                    del visited[old.name]
                    frontier[scored_child.name] = scored_child
            else:
                frontier[scored_child.name] = scored_child
    return None


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

    origin = 'Norra Bro'
    goal = 'Hagaby'
    position = nodes[origin]
    start = Node(None,origin, position[0], position[1], 0, get_distance(position, nodes[goal]))

    path = a_star_search(city_map, start, nodes, goal)
    cool_path = get_path(goal,path)
    print cool_path

