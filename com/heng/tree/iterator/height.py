from com.heng.tree.node import BinaryNode, getBinaryTree

root = getBinaryTree()


# recursive
def get_height_r(r):
    if r is None:
        return 0
    return max(get_height_r(r.left), get_height_r(r.right)) + 1


# layer
def get_hight_l(r):
    list = [r]
    height = 0
    while len(list) > 0:
        height += 1
        list2 = []
        for n in list:
            if n.left is not None:
                list2.append(n.left)
            if n.right is not None:
                list2.append(n.right)
        list = list2
    return height


print(get_height_r(root))
print(get_hight_l(root))
