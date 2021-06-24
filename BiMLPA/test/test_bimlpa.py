import unittest
from BiMLPA import *
from codecs import open
from os import path


class BiMLPATestCase(unittest.TestCase):

    def test_bimlpa_SqrtDeg(self):
        here = path.abspath(path.dirname(__file__))
        G = generate_network(path.join(here, 'southernwomen.net'))
        bimlpa = BiMLPA_SqrtDeg(G, 0.3, 7)
        bimlpa.start()
        relabeling(G)
        top, bottom = output_community(G)
        self.assertIsInstance(top, list)
        self.assertIsInstance(bottom, list)

    def test_bimlpa(self):
        here = path.abspath(path.dirname(__file__))
        G = generate_network_with_name(path.join(here, 'southernwomen.net'))
        bimlpa = BiMLPA(G, 0.3, 7)
        bimlpa.start()
        relabeling(G)
        top, bottom = output_community(G)
        self.assertIsInstance(top, list)
        self.assertIsInstance(bottom, list)

    def test_bimlpa_BiMLPA_EdgeProb(self):
        here = path.abspath(path.dirname(__file__))
        G = generate_network(path.join(here, 'southernwomen.net'))
        bimlpa = BiMLPA_EdgeProb(G, 0.3, 7)
        bimlpa.start()
        relabeling(G)
        top, bottom = output_community(G)
        self.assertIsInstance(top, list)
        self.assertIsInstance(bottom, list)


if __name__ == '__main__':
    unittest.main()
