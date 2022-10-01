"""

Documentation Doc: https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings

"""

from enum import Enum, unique
import logging
import operator

logging.basicConfig(filename='heapLog.log',
                    level=logging.WARNING,
                    format='%(asctime)s | %(name)s | %(filename)s:%(lineno)s | %(funcName)20s() | %(levelname)s | %('
                           'message)s')

@unique
class HeapType(Enum):
    """Enumeration for possible heap types"""
    MAX = {'MAX':operator.gt}
    MIN = {'MIN':operator.lt}


class EmptyHeap(Exception): pass

class Heap:
    """
    Implementation of the well known Heap data structure

    Attributes
    ----------

    Methods
    -------

    insert(node)
        Inserts a new node into the heap

    find_max()
        Finds the maximum item in the max-heap
    find_min()
        Finds the minimum item in the min-heap
    """

    def __init__(self, heap_type=HeapType.MAX, data=[]):
        """
        Parameters
        ----------

        :param heap_type: HeapType
            Either a min or max heap, by default a max heap.
        :param data: [int]
            An array of integers used to initialize the heap
        """

        self.heap_type = heap_type
        self.data = data

        # Heapify if more than node is passed for the heap
        if len(data) > 1:
            self.build_heap()

    def insert(self, node, heapify=False) -> bool:
        """ Insert a new node into the heap

        Parameters
        ----------

        :param heapify:
        :param node: int
        :return: bool
            returns true if the node was added to the max-heap, false otherwise
        """

        logging.debug(f'Adding {node} to the {self.heap_type}-heap with existing data {self.data}')
        self.data.append(node)

        if heapify:
            self.__heapify()

    def set_heap_type(self, heap_type):
        """Make the heap a min or max heap

        :param heap_type: HeapType
             A min or max heap
        :return:
            Nothing
        """

        if heap_type != self.heap_type:
            self.heap_type = heap_type
            self.build_heap()
        else:
            logging.info(f'Heap is already a {self.heap_type} heap')

    def __heapify(self, root_index):
        """Ensure the heap maintains the properties of a max or min heap

        :param root_index: int
            index of node in the heap
        :return:
        """
        heap_node_count = len(self.data)
        if root_index > heap_node_count:
            logging.error(f'Attempting to access the {root_index}th element in {self.data} which is out if root_index range.')
            raise IndexError()

        curr_largest_node_index = root_index
        left_node_index = 2 * root_index + 1
        right_node_index = 2 * root_index + 2

        if self.heap_type == HeapType.MIN:
            logging.debug('Making a min heap')
        else:
            logging.debug('Making a max heap.')

        if left_node_index < heap_node_count and self.heap_type.value[self.heap_type.name](self.data[left_node_index], self.data[curr_largest_node_index]):
            curr_largest_node_index = left_node_index

        if right_node_index < heap_node_count and self.heap_type.value[self.heap_type.name](self.data[right_node_index], self.data[curr_largest_node_index]):
            curr_largest_node_index = right_node_index

        if curr_largest_node_index != root_index:
            # The current largest node becomes the tree's root node
            self.data[root_index], self.data[curr_largest_node_index] = self.data[curr_largest_node_index], self.data[root_index]

            # Heapify the tree until the root index if the largest node in the tree
            self.__heapify(curr_largest_node_index)

        if self.heap_type == HeapType.MIN:
            logging.debug('Converting the heap to a min-heap')
            # https://www.geeksforgeeks.org/convert-min-heap-to-max-heap/

    def build_heap(self):
        """Creates a heap of self.heap_type"""
        if self.heap_type.MAX:
            logging.debug('Making a max heap')
        else:
            logging.debug('Making a min heap')

        last_non_leaf_node_index = len(self.data) // 2 - 1

        for current_leaf_node_index in range(last_non_leaf_node_index, -1, -1):
            self.__heapify(current_leaf_node_index)

    def __peek(self) -> int:
        """Returns the first element in self.data without removing it.

        :return: int
            The first element in self.data
        """
        return self.data[0]

    def find_max(self) -> int:
        """Find a maximum item of a max-heap

        :return: int
            The maximum item in the max-heap
        """

        if not self.data:
            logging.warning('Attempting to find maximum item for an empty heap.')
            raise EmptyHeap()
        else:
            logging.debug('Finding maximum item…')

        logging.debug(f'Found max_item of value {self.__peek()}')

    def find_min(self) -> int:
        """Find a minimum item of a min-heap

        :return: int
            The minimum item in the min-heap
        """

        if not self.data:
            logging.warning('Attempting to find minimum item for an empty heap.')
            raise EmptyHeap()
        else:
            logging.debug('Finding minimum item…')

        logging.debug(f'Found min_item of value {self.__peek()}')

    def extract_min(self):
        pass

    def extract_max(self):
        pass

    def delete_max(self):
        pass

    def replace(self):
        pass
