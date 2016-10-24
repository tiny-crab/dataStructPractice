from linkedList import *

ll = LinkedList()
node1 = Node(1234)
node2 = Node("hello")
node3 = Node("world")

ll.add(node1)
ll.add(node2)
ll.add(node3)

ll.print_list()

ll.delete("hello")

ll.print_list()

cl = CircularList()

cl.add(node1)
cl.add(node2)
cl.add(node3)

cl.print_list()


