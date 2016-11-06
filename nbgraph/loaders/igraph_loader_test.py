import unittest

import igraph
from nbgraph.loaders import igraph_loader


class TestNetworkxLoader(unittest.TestCase):

    def test_loader(self):
        graph = igraph.Graph.Atlas(66)
        nb_graph = igraph_loader.load_graph(graph)
        expected = {'edges':
                    [{'target': '2', 'id': 0, 'source': '0'},
                     {'target': '3', 'id': 1, 'source': '1'},
                     {'target': '2', 'id': 2, 'source': '1'},
                     {'target': '5', 'id': 3, 'source': '3'}],
                    'nodes':
                    [{'id': '0', 'label': '0'},
                     {'id': '1', 'label': '1'},
                     {'id': '2', 'label': '2'},
                     {'id': '3', 'label': '3'},
                     {'id': '4', 'label': '4'},
                     {'id': '5', 'label': '5'}]}
        self.assertEqual(nb_graph.as_dict(), expected)

if __name__ == '__main__':
    unittest.main()
