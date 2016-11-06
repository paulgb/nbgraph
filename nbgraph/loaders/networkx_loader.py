
from nbgraph.notebook_graph import NotebookGraph

def load_graph(networkx_graph):
    graph = NotebookGraph()
    for node in networkx_graph.nodes():
        graph.add_node(str(node), str(node))
    for source, target in networkx_graph.edges():
        graph.add_edge(str(source), str(target))
    return graph