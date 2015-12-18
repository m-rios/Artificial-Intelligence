import random
import copy

def parse_wine(path):
    f = open(path, 'r')
    data_set = []
    size = 178

    for line in f.readlines():
        row = line.split(',')
        # row[len(row)-1] = row[len(row)-1].rstrip()
        num_row = []
        for i in range(len(row)):
            num_row.append(float(row[i]))
        data_set.append(num_row)
    f.close()
    return data_set


def rand_init_cluster(data_set, n_clusters):
    c = {}
    for i in range(n_clusters):
        c[i] = []

    for line in data_set:
        c[random.randrange(0,n_clusters)].append(line)

    return c


def mean(cluster):
    mean = []
    for x in range(len(cluster[0])):
        mean.append(0)

    for i in range(1, len(cluster)):
        for j in range(len(cluster[i])):
            mean[j] = mean[j] + cluster[i][j]
    mean.pop(0)
    result = [r/len(cluster) for r in mean]

    return result


def distance(wine, cluster):
    result = 0
    for i in range(len(cluster)):
        result += abs(wine[i+1] - cluster[i])
    return result


def k_means_clustering(data_set, n_clusters):

    c_new = rand_init_cluster(data_set, n_clusters)
    #new dict
    c = {}
    # for i in range(n_clusters):
    #     c[i] = []

    while not c == c_new:

        c = dict(c_new)
        # clear c_new
        for key in c_new.keys():
            c_new[key] = []

        #get mean / cluster
        means = []
        for i in range(n_clusters):
            means.append(mean(c[i]))

        #Compute distance map
        distance_array = []
        for i in range(n_clusters):
            distance_row = []
            for j in range(len(data_set)):
                distance_row.append(distance(data_set[j], means[i]))
            distance_array.append(distance_row)

        #Re-arrange
        for i in range(len(data_set)):
            column = []
            for j in range(n_clusters):
                column.append(distance_array[j][i])
            _min = min(column)
            index = column.index(_min)
            c_new[index].append(data_set[i])

    return c

if __name__ == '__main__':
    data = parse_wine("wine.data")

    c = k_means_clustering(data,3)

    print c[0]
    print c[1]
    print c[2]
