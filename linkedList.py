
class Node:

    def __init__(self, data):
        self.pointer = None
        self.data = data


class LinkedList:

    def __init__(self):
        self.first_node = None
        self.last_node = None
        self.node_count = 0

    # data should be an instance of a Node
    def add(self, data):
        added_node = data
        if self.node_count == 0:
            self.first_node = added_node
            self.last_node = added_node
        else:
            self.last_node.pointer = added_node
            self.last_node = added_node
        self.node_count += 1

    def delete(self, data):
        current_node = self.first_node
        prev_node = self.first_node
        while current_node is not None:
            if current_node.data == data:
                if current_node == self.first_node:
                    self.first_node = self.first_node.pointer
                else:
                    prev_node.pointer = current_node.pointer
                    # do I need to do some sort of node cleanup here?
                    break
            current_node = current_node.pointer

    def print_list(self):
        node_iterator = self.first_node
        while node_iterator != self.last_node:
            print node_iterator.data
            node_iterator = node_iterator.pointer
        print node_iterator.data


class CircularList(LinkedList):

    def add(self, data):
        added_node = data
        if self.node_count == 0:
            self.first_node = added_node
            self.last_node = added_node
        else:
            self.last_node.pointer = added_node
            self.last_node = added_node
            self.last_node.pointer = self.first_node
        self.node_count += 1