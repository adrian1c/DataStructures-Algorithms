# ADRIAN CHING LIANSHENG 18063865
# NG WEI JINN 18064154
# ROGER JIA SIEN BOON 18046847

import heapq
import matplotlib.pyplot as plt
import networkx as nx

#----------------------------------------------------------
#--------------------DIJKSTRA ALGORITHM--------------------
#----------------------------------------------------------

# Calculates the shortest distance to reach 
# all nodes from a starting node
def dijkstra(graph, starting_node, ending_node = None):
    
    # Set distance for all nodes to infinity, 
    # except for the starting node
    distances = {node: float('infinity') for node in graph}
    distances[starting_node] = 0
    
    # Set path for all nodes to include starting node
    path = {node: [starting_node] for node in graph}

    # Make a priority queue and loop
    # until all paths are explored
    pq = [(0, starting_node)]

    while len(pq) > 0:
        
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():

            temp_distance = current_distance + weight['weight']
            temp_path = path[current_node] + [neighbor]
            
            # Get the shortest path if it exists
            if temp_distance < distances[neighbor]:
                path[neighbor] = temp_path
                distances[neighbor] = temp_distance
                heapq.heappush(pq, (temp_distance, neighbor))        
        
    # Remove the starting node from the result
    # because the starting node will always be 0
    del distances[starting_node]
    del path[starting_node]

    # Return the shortest distance to reach all nodes from starting node
    if ending_node is None:
        return distances, path
    else:
        return distances[ending_node], path[ending_node]


#--------------------------------------------------------
#-----------------VISUALIZATION OF GRAPH-----------------
#--------------------------------------------------------


#Shows the created graph
def show_graph(graph: list, weighted = True, directed = False):
    
    global isWeighted

    if directed is False:
        G = nx.Graph()
    else:
        G = nx.DiGraph()
    
    if weighted is True:
        isWeighted = True
        for i in graph:
            G.add_edge(i[0], i[1], weight=i[2])
    else:
        isWeighted = False
        for i in graph:
            G.add_edge(i[0], i[1], weight=1)

    # Configuration of layout
    plt.figure(1, figsize=[8,8])
    plt.title('Graph')
    
    # Position and arrangement of nodes
    pos = nx.shell_layout(G, scale=1)  
    
    # Draw nodes of graph
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='#2f56a1')
    
    # Draw edges of graph
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edges(G, pos, width=2, edge_color='#183161', arrowsize=30)
    if isWeighted:
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, label_pos=0.6, font_size=20)
    
    # Draw labels of nodes of graph
    nx.draw_networkx_labels(G, pos, font_size=15, font_family='sans-serif', font_color='w')

    plt.figtext(0.12, 0.89, f'Weighted: {isWeighted}', horizontalalignment='left', fontsize=12)
    
    return G


def show_graph_all(G, starting_node):
    
    # Configuration of layout
    plt.figure(2, figsize=[8,8])
    plt.title(f'Distances from starting node {starting_node}')

    # Get result of the algorithm
    distances, path = dijkstra(G, starting_node, ending_node = None)
    
    # Separate the starting node from the rest of the nodes
    nodesList = list(G.nodes)
    nNormal = [i for i in nodesList if i != starting_node]
    nStarting = [i for i in nodesList if i == starting_node]
    
    # Position and arrangement of nodes
    pos = nx.shell_layout(G, scale=1)
            
    # Draw nodes of graph
    nx.draw_networkx_nodes(G, pos, nodelist=nNormal, node_size=500, node_color='#2f56a1')
    nx.draw_networkx_nodes(G, pos, nodelist=nStarting, node_size=500, node_color='#ed345f')

    # Draw edges of graph
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edges(G, pos, width=2, edge_color='#183161', arrowsize=30)
    if isWeighted:
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, label_pos=0.6, font_size=20)
    
    # Draw labels of nodes of graph
    nx.draw_networkx_labels(G, pos, font_size=15, font_family='sans-serif', font_color='w')
    
    # Display the results of the algorithm
    dist = ''
    for key, value in distances.items():
        dist += f'From {starting_node} to {key}: {value},      {path[key][0]}'
        for i in path[key][1:]:
            dist += f' \u2192 {i}'
        dist += '\n'
    plt.figtext(0.5, -0.01, dist, horizontalalignment='center', fontsize=10)
    plt.figtext(0.12, 0.89, f'Weighted: {isWeighted}', horizontalalignment='left', fontsize=12)
    
    return


#Shows the shortest pathway using dijkstra's algorithm from start node to goal node
def show_graph_start_goal(G, starting_node, ending_node):
    
    # Configuration of layout
    plt.figure(3, figsize=[8,8])
    plt.title(f'Shortest path from {starting_node} to {ending_node}')
    
    # Get result of the algorithm
    distance, path = dijkstra(G, starting_node, ending_node)
    
    # Position and arrangement of nodes
    pos = nx.shell_layout(G, scale=1)

    # Separate the goal nodes from the normal nodes
    nNormal = [i for i in list(G.nodes) if i not in path]
    nGoal = [i for i in list(G.nodes) if i in path]
    
    # Draw nodes of graph
    nx.draw_networkx_nodes(G, pos, nodelist=nNormal, node_size=500, node_color='#2f56a1')
    nx.draw_networkx_nodes(G, pos, nodelist=nGoal, node_size=500, node_color='#ed345f')
    labels = nx.get_edge_attributes(G, 'weight')
    
    #Convert from
    #['X', 'Y', 'Z'] To [('X','Y'),('Y','Z')]
    pathList = [(path[i], path[i+1]) for i in range(len(path)) if i < (len(path)-1) ]

    # Separate the goal edges from the normal edges
    eNormal = [i for i in list(G.edges) if i not in pathList and i[::-1] not in pathList]
    eGoal = [i for i in list(G.edges) if i in pathList or i[::-1] in pathList]
    
    # Draw edges of graph
    nx.draw_networkx_edges(G, pos, edgelist=eNormal, width=2, edge_color='#183161', arrowsize=30)
    nx.draw_networkx_edges(G, pos, edgelist=eGoal, width=3, edge_color='#b31e41', arrowsize=30)
    if isWeighted:
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, label_pos=0.6, font_size=20)
    
    # Draw labels of nodes of graph
    nx.draw_networkx_labels(G, pos, font_size=15, font_family='sans-serif', font_color='w')

    # Display the results of the algorithm
    pathway = f'{path[0]}'
    for i in path[1:]:
            pathway += f' \u2192 {i}'
    pathway += f'\nTotal Distance: {distance}'
    
    plt.figtext(0.5, 0.05, pathway, horizontalalignment='center', fontsize=12)  
    plt.figtext(0.12, 0.89, f'Weighted: {isWeighted}', horizontalalignment='left', fontsize=12)
    
    return
        


#-----------------------------------------------------
#---------------------MAIN CLASS----------------------
#-----------------------------------------------------

if __name__ == '__main__':
    
    plt.close('all')

    # Graph with DOUBLE weight 
    # edges = [
    #     ['A', 'B', 5.23],
    #     ['B', 'C', 1.4182],
    #     ['C', 'D', 3.7],
    #     ['D', 'E', 7.218],
    #     ['A', 'D', 3.3],
    #     ['C', 'E', 1.506],
    # ]

    # Graph with INT nodes and DOUBLE weight 
    # edges = [
    #     [1, 2, 5.23],
    #     [2, 3, 1.4182],
    #     [3, 4, 3.7],
    #     [4, 5, 7.218],
    #     [1, 4, 3.3],
    #     [3, 5, 1.506],
    # ]

    # Specify the edges from one node to another 
    # along with its weight
    edges = [
        ['A', 'B', 5],
        ['A', 'C', 2],
        ['B', 'D', 3],
        ['B', 'E', 1],
        ['C', 'D', 3],
        ['C', 'E', 3],
        ['D', 'F', 4],
        ['E', 'F', 2],
    ]
    
    # Create a graph from the edges list. 
    # Parameter settings:
    #    Set weighted=False for unweighted graph
    #    Set directed=True for directed graph
    G = show_graph(edges, weighted = False, directed = True)

    # Add nodes/edges 
    #
    # G.add_edge('node1', 'node2', weight=1)
    # G.add_edge('node2', 'node3', weight=2)
    # ...
    # G.add_edge('F', 'G', weight=5)
    # G.remove_node('E')
    
    # Shortest distance of all nodes from starting node
    show_graph_all(G, 'A')
    
    # Shortest path from starting node to ending node
    show_graph_start_goal(G, 'A', 'F')
    

    plt.show()
    