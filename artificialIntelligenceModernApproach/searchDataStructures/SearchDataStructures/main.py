from enum import Enum, unique


# Create an Error class


# The state of a node
# Make sure each enumeration has a unique value
@unique
class State(Enum):
    INITIAL = 'Initial'
    GOAL = 'Goal'
    DIRTY = 'Dirty'
    CLEAR = 'Clean'

# Represents a problem
class Problem:

    def __init__(self, goal):
        self.goal = goal
        self.state = State.INITIAL

    # Update the state of the problem
    def updatestate(self, state):
        self.state = state if isinstance(state, State) else print(f'Incorrect state type passed. {state}')

    # Check if the problem has reached its goal state
    @property
    def isgoal(self):
        return self.state == self.goal

# Data structure to keep track of the search tree
class Node:

    def __init__(self, state, data=None, parent=None, next=None):
        # The state to which the node corresponds
        self.state = state if isinstance(state, State) else print(f'Incorrect state type passed. {state}')
        self.parent = parent if isinstance(parent, Node) else print(f'Incorrect parent type passed. {parent}')
        self.next = next if isinstance(next, Node) else print(f'Incorrect parent type passed. {next}')

        # The total cost of the path from the initial state to this node
        # In mathematical formulas, we use g(node) as a synonym for PATH-COST
        self.path_cost = self.get_path_cost

        # The action that was applied to the parent's state to generate this node
        self.action = self.get_action
        self.data = data

    # Action applied to the parent node to generate node Y
    @property
    def get_action(self):
        return None

    # Total cost of the path from the initial state to this node
    @property
    def get_path_cost(self):
        return None

# Doubly Linked List to link all root nodes in the Fibonacci Heap
class DoublyLinkedList:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
        self.list = []

    # Traverse the doubly linked list from the head
    # Pass a function to do something with the node data
    def forward_traversal(self):
        node = self.head
        while node is not None:
            # Do something with node data
            node = node.next

    # Traverse the double linked list from the tail
    def backward_traversal(self):
        node = self.tail
        while node is not None:
            # Do something with node data
            node = node.parent

    # Insert a node after a node
    def insert_after(self, node, new_node):
        new_node.parent = node

        # Adding a new tail to the list
        if node.next == None:
            new_node.next = None
            self.tail = new_node
        # Adding a node in between a current link
        else:
            new_node.next = node.next
            # Make node.next original parent the new_node that will be inserted before it
            node.next.parent = new_node
        node.next = new_node

    # Insert a node before a node
    def insert_before(self, node, new_node):
        new_node.next = node

        # Adding a node before the head
        if node.parent == None:
            self.head = new_node
            new_node.parent = None
        # Adding a node in between a current link
        else:
            new_node.parent = node.parent
            node.parent.next = new_node

        node.parent = new_node

    # Insert a node at the beginning of the doubly linked list
    def insert_beginning(self, new_node):
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.parent = None
            new_node.next = None
        else:
            self.insert_before(self.head, new_node)

    # Insert a node at the end of the doubly linked list
    def insert_end(self, new_node):
        if not self.tail:
            self.insert_beginning(new_node)
        else:
            self.insert_after(self.tail, new_node)

    # Remove a node from the linked list
    def remove(self, node):
        # Removing beginning of linked list
        if not node.parent:
            self.head = node.next
        else:
            node.parent.next = node.next

        # Removing end of linked list
        if not node.next:
            self.tail = node.parent
        else:
            node.next.parent = node.parent

# Priority Queue
class PriorityQueue:
    def __init__(self):
        self.content = []
        self.evaluationFunction = None

    def pop(self):
        pass

    def top(self):
        pass

    def add(self, node):
        node_to_add = node if isinstance(node, Node) else print(f'Incorrect parent type passed. {node}')

    def insert_with_priority(self, node, priority):
        node_to_add = node if isinstance(node, Node) else print(f'Incorrect parent type passed. {node}')

    @property
    def isempty(self):
        return None

if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
