#-*- coding:utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import math




def get_CCycle(node_num, p, display=False):
    G = nx.random_graphs.erdos_renyi_graph(node_num, p)
    colors = [0 for i in range(node_num)]
    start_point = -1
    max_degree = 0
    for n in G.node:
        if G.degree(n) > max_degree:
            start_point = n
            max_degree = G.degree(n)

    if start_point == -1:
        return G, []
    colors[start_point] = 1
    adj_points = list(G[start_point].keys())
    for p in adj_points:
        for q in G[p]:
            if q in adj_points:
                colors[p] = colors[q] = 1
                if display:
                    pos = nx.shell_layout(G)
                    nx.draw(G, pos, with_labels=True, node_color=colors)
                    plt.show()
                return G, [start_point, p, q]
    return G, []


def checkIE(G, CC):
    degrees = []
    for p in CC:
        degrees.append(G.degree(p))
    cri = degrees[0]
    for d in degrees:
        if cri != d:
            return False
    return True

def test(epoch, num_node, p=0.5):
    t_count = 0
    for i in range(epoch):
        G, CC = get_CCycle(num_node, p)
        if len(CC) == 0:
            continue
        t_count += checkIE(G, CC)
    print(t_count, epoch)
    return t_count

def find_top(node_num):
    G = nx.random_graphs.erdos_renyi_graph(node_num, 0.5)
    degrees = {}
    for p in G.node:
        if G.degree(p) in degrees:
            degrees[G.degree(p)].append(p)
        else:
            degrees[G.degree(p)] = [p]
    print(degrees)

def normal_CCycle(node_num, p, display=False):
    G = nx.random_graphs.erdos_renyi_graph(node_num, p)
    colors = [0 for i in range(node_num)]
    start_point = -1
    max_degree = 0
    for n in G.node:
        if G.degree(n) > max_degree:
            start_point = n
            max_degree = G.degree(n)

    if start_point == -1:
        return G, []

    cycle = find_cycle(G, start_point)
    for p in cycle:
        colors[p] = 1

    if display:
        pos = nx.shell_layout(G)
        nx.draw(G, pos, with_labels=True, node_color=colors)
        plt.show()


def find_cycle(G, start):
    stack = list(G[start].keys())
    cycle = [start]
    flag = True
    fs = [True for i in G.node]
    while True:
        next_point = stack.pop()
        fs[next_point] = False
        cycle.append(next_point)
        for p in G[next_point]:
            if fs[p]:
                stack.append(p)
                fs[p] = False
            else:
                if p == start:
                    return cycle
                
def local_search(node_num, p, display=False):
    if node_num >= 20 or p >= 0.3:
        get_CCycle(node_num, p, display)
    else:
        normal_CCycle(20, 0.3, True)

if __name__ == '__main__':
    label = []
    line = []
    for p in range(1, 10, 2):
        x_index = []
        y_index = []
        for i in range(10, 40):
            x_index.append(i)
            y_index.append(test(10000, i, p / 10))
        plt.plot(x_index, y_index)
        label.append('p={}'.format(p/10))
    plt.legend(label)
    plt.show()

