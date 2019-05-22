class LinkedNode:
    next = None
    value = 0

    def __init__(self, value):
        self.value = value


def get_linked_list():

    head = LinkedNode(1)
    node2 = LinkedNode(2)
    node3 = LinkedNode(3)
    node4 = LinkedNode(4)
    node5 = LinkedNode(5)
    node6 = LinkedNode(6)
    node7 = LinkedNode(7)
    node8 = LinkedNode(8)
    node9 = LinkedNode(9)
    node10 = LinkedNode(10)

    node9.next = node10
    node8.next = node9
    node7.next = node8
    node6.next = node7
    node5.next = node6
    node4.next = node5
    node3.next = node4
    node2.next = node3
    head.next = node2

    return head
