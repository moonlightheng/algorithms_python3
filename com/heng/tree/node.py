


class BinaryNode:
    left = None
    right = None
    value = 0

    def __init__(self, value):
        self.value = value


def getBinaryTree():
    root = BinaryNode(20)
    # left
    nodel = BinaryNode(8)

    nodell = BinaryNode(5)
    nodelll = BinaryNode(3)
    nodellr = BinaryNode(6)

    nodell.left = nodelll
    nodell.right = nodellr

    nodel.left = nodell

    nodelr = BinaryNode(11)
    nodelrl = BinaryNode(9)
    nodelrr = BinaryNode(12)

    nodelr.left = nodelrl
    nodelr.right = nodelrr

    nodel.right = nodelr

    # right
    noder = BinaryNode(40)

    noderl = BinaryNode(30)
    noderll = BinaryNode(25)
    noderlr = BinaryNode(32)

    noderl.left = noderll
    noderl.right = noderlr

    noder.left = noderl

    noderr = BinaryNode(50)
    noderrl = BinaryNode(45)
    noderrr = BinaryNode(55)

    noderr.left = noderrl
    noderr.right = noderrr

    noder.right = noderr

    root.left = nodel
    root.right = noder
    return root



