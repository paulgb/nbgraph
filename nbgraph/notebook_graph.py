
from nbgraph import renderer

class NotebookGraph(object):
    def __init__(self):
        self.edges = list()
        self.nodes = list()
        self.next_edge_id = 0

    def _get_next_edge_id(self):
        this_edge_id = self.next_edge_id
        self.next_edge_id += 1
        return this_edge_id

    def add_edge(self, source, target):
        self.edges.append({
            'id': self._get_next_edge_id(),
            'source': str(source),
            'target': str(target)
        })

    def add_node(self, id, label=None):
        id = str(id)
        if label is None:
            label = str(id)
        self.nodes.append({
            'id': id,
            'label': label
        })

    def as_dict(self):
        return {'nodes': self.nodes, 'edges': self.edges}

    def _repr_html_(self):
        return renderer.generate_html(self)