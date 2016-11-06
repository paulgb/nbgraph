import unittest

import networkx
from nbgraph.loaders import networkx_loader


class TestNetworkxLoader(unittest.TestCase):

    def test_loader(self):
        graph = networkx.hypercube_graph(3)
        nb_graph = networkx_loader.load_graph(graph)
        expected = {'edges':
                    [{'id': 0, 'target': '(0, 1, 0)', 'source': '(0, 1, 1)'},
                     {'id': 1, 'target': '(0, 0, 1)', 'source': '(0, 1, 1)'},
                     {'id': 2, 'target': '(1, 1, 1)', 'source': '(0, 1, 1)'},
                     {'id': 3, 'target': '(1, 0, 0)', 'source': '(0, 0, 0)'},
                     {'id': 4, 'target': '(0, 1, 0)', 'source': '(0, 0, 0)'},
                     {'id': 5, 'target': '(0, 0, 1)', 'source': '(0, 0, 0)'},
                     {'id': 6, 'target': '(1, 0, 0)', 'source': '(1, 1, 0)'},
                     {'id': 7, 'target': '(0, 1, 0)', 'source': '(1, 1, 0)'},
                     {'id': 8, 'target': '(1, 1, 1)', 'source': '(1, 1, 0)'},
                     {'id': 9, 'target': '(1, 0, 1)', 'source': '(1, 0, 0)'},
                     {'id': 10, 'target': '(1, 0, 1)', 'source': '(0, 0, 1)'},
                     {'id': 11, 'target': '(1, 0, 1)', 'source': '(1, 1, 1)'}],
                    'nodes': [
                        {'id': '(0, 1, 1)', 'label': '(0, 1, 1)'},
                        {'id': '(1, 0, 0)', 'label': '(1, 0, 0)'},
                        {'id': '(0, 0, 1)', 'label': '(0, 0, 1)'},
                        {'id': '(1, 0, 1)', 'label': '(1, 0, 1)'},
                        {'id': '(0, 0, 0)', 'label': '(0, 0, 0)'},
                        {'id': '(1, 1, 1)', 'label': '(1, 1, 1)'},
                        {'id': '(1, 1, 0)', 'label': '(1, 1, 0)'},
                        {'id': '(0, 1, 0)', 'label': '(0, 1, 0)'}]}
        self.assertEqual(nb_graph.as_dict(), expected)

if __name__ == '__main__':
    unittest.main()