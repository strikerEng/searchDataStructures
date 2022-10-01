import unittest
from SearchDataStructures.main import *
import logging


# The logger is set to the warning level by default, change to info
logging.basicConfig(level=logging.INFO)


class MyTestCase(unittest.TestCase):
    def test_node_has_initial_state(self):
        initialNode = Node(State.INITIAL)
        self.assertEqual(initialNode.state, State.INITIAL, "The node created is not in the initial state.")
        logging.info("The node was correctly initialized with the initial state.")

if __name__ == '__main__':
    unittest.main()
