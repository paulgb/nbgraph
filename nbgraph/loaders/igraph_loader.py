from nbgraph.notebook_graph import NotebookGraph

def load_graph(igraph_graph):
    graph = NotebookGraph()
    for node in igraph_graph.vs():
        graph.add_node(node.index)
    for edge in igraph_graph.es():
        graph.add_edge(edge.source, edge.target)
    return graph
