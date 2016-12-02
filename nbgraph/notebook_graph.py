
from nbgraph import renderer


class NotebookGraph(object):
    '''Class representing a simple graph as a list of nodes and edges, as well
    as methods for rendering itself in a notebook environment.

    The typical user will want to use one of the loaders in nbgraph.loaders to
    construct this graph rather than calling add_edge and add_node directly.
    '''

    def __init__(self):
        self.edges = list()
        self.nodes = list()
        self.next_edge_id = 0

    def add_edge(self, source, target):
        '''Adds an edge to the graph. add_node must also be called on the
        source and target nodes (the order doesn't matter).

        PARAMS:
            source          The source node of the edge as a string identifier.
            target          The target node of the edge as a string identifier.
        '''
        self.edges.append({
            'id': self._get_next_edge_id(),
            'source': str(source),
            'target': str(target)
        })

    def add_node(self, identifier, label=None):
        '''Adds a node to the graph.

        PARAMS:
            identifier      A string uniquely identifying the node.
            label           An optional string label for the node.
        '''
        identifier = str(identifier)
        if label is None:
            label = str(identifier)
        self.nodes.append({
            'id': identifier,
            'label': label
        })

    def as_dict(self):
        '''Converts the graph to a dictionary representation, mirroring the
        JavaScript object representation of a graph used by sigma.js.
        '''
        return {'nodes': self.nodes, 'edges': self.edges}

    def show(self, include_scripts=False, config=None):
        '''Displays the graph in the jupyter/IPython notebook that this code is
        called from.

        PARAMS:
            include_scripts     If True, includes all necessary JavaScript code
                                required to display the graph. If
                                renderer.prepare_notebook has been called in
                                this notebook, this is not required.
            config              Rendering configuration parameters.
        '''
        return renderer.display_notebook(self, include_scripts, config)

    def _get_next_edge_id(self):
        this_edge_id = self.next_edge_id
        self.next_edge_id += 1
        return this_edge_id

    def _repr_html_(self):
        return renderer.generate_html(self)
