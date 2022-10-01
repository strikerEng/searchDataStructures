import Heap
import logging
import unittest

logging.basicConfig(filename='heapLog.log',
                    level=logging.INFO,
                    format='%(asctime)s | %(name)s | %(filename)s:%(lineno)s | %(funcName)20s() | %(levelname)s | %('
                           'message)s')

class MyTestCase(unittest.TestCase):
    def test_findMaxAndMinOfEmptyHeapRaisesAnError(self):
        empty_min_heap = Heap.Heap(heap_type=Heap.HeapType.MIN, data=[])
        with self.assertRaises(Heap.EmptyHeap):
            empty_min_heap.find_min()

        empty_max_heap = Heap.Heap(heap_type=Heap.HeapType.MAX, data=[])
        with self.assertRaises(Heap.EmptyHeap):
            empty_max_heap.find_min()

    def test_insert_node_into_heap(self):
        max_heap = Heap.Heap(heap_type=Heap.HeapType.MAX, data=[])
        self.assertTrue(len(max_heap.data) == 0, 'The heap is not empty but it is supposed to be.')
        max_heap.insert(1,heapify=False)
        self.assertTrue(max_heap.data == [1], 'The heap is supposed to be equivalent to [1] but it does not.')
        self.assertFalse(max_heap.data == [5], 'The heap is not supposed to be equivalent to [5] but it does.')

    def test_building_a_max_heap(self):
        max_heap = Heap.Heap(
            heap_type=Heap.HeapType.MAX,
            data=[1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
        )

        correct_max_heap_order =  [17, 15, 13, 9, 6, 5, 10, 4, 8, 3, 1]
        logging.info(f'The heap type inequality is {max_heap.heap_type.value[max_heap.heap_type.name]}')
        self.assertEqual(max_heap.data, correct_max_heap_order, 'The array was not properly heapified.')

    def test_building_a_min_heap(self):
        min_heap = Heap.Heap(
            heap_type=Heap.HeapType.MIN,
            data= [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
        )

        correct_min_heap_order = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
        logging.info(f'The heap type inequality is {min_heap.heap_type.value}')
        self.assertEqual(min_heap.data, correct_min_heap_order, 'The array was not properly heapified.')

        min_heap.set_heap_type(Heap.HeapType.MIN)
        self.assertEqual(min_heap.data, correct_min_heap_order, 'The array was not properly heapified.')

        min_heap.set_heap_type(Heap.HeapType.MAX)
        correct_max_heap_order = [20, 18, 10, 12, 9, 9, 3, 5, 6, 8]
        self.assertEqual(min_heap.data, correct_max_heap_order, 'The array was not properly heapified.')

if __name__ == '__main__':
    unittest.main()
