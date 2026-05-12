class Node:
    pass


class Tree:
    pass


def _default_compare(current, key):
    if key.data < current.data:
        return -1
    elif key.data > current.data:
        return 1
    else:
        return 0


def _from_list(list, compare_func):
    if list is None:
        return None
    if not list:
        return create_tree(compare_func)
    tree = create_tree(compare_func)
    tree.root = _create_node(list[0])
    for i in range(len(list[1:])):
        current_node = tree.root
        comparable = _create_node(list[i + 1])
        while True:
            current_comparable = tree.compare(current_node, comparable)
            if current_comparable == -1:
                if current_node.left is None:
                    current_node.left = comparable
                    break
                else:
                    current_node = current_node.left
            elif current_comparable == 1:
                if current_node.right is None:
                    current_node.right = comparable
                    break
                else:
                    current_node = current_node.right
            else:
                break
    return tree


def _preorder_traversal_to_list(tree):
    if _is_tree_none(tree):
        return None
    if tree.root is None:
        return []
    node = tree.root
    stack = [node]
    result = []
    while stack:
        current = stack.pop()
        result.append(current.data)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return result


def _is_tree_none(tree):
    if tree is None:
        return True
    else:
        return False


def _create_node(data):
    node = Node()
    node.data = data
    node.left, node.right = None, None
    return node


def create_tree(compare_func=_default_compare):
    tree = Tree()
    tree.root = None
    tree.compare = compare_func
    return tree


def clear(tree):
    if _is_tree_none(tree):
        return None
    tree.root = None
    return tree


def size(tree):
    if _is_tree_none(tree):
        return None
    return len(_preorder_traversal_to_list(tree))


def find(tree, data):
    if _is_tree_none(tree) or tree.root is None:
        return None
    current = tree.root
    comparable = _create_node(data)
    while True:
        current_comparable = tree.compare(current, comparable)
        if current_comparable == 0:
            return current.data
        if current_comparable == -1:
            if current.left:
                current = current.left
            else:
                break
        else:
            if current.right:
                current = current.right
            else:
                break
    return None


def insert(tree, data):
    if _is_tree_none(tree) or data is None:
        return None
    if tree.root is None:
        tree.root = _create_node(data)
        return tree
    current = tree.root
    comparable = _create_node(data)
    while True:
        current_comparable = tree.compare(current, comparable)
        if current_comparable == -1:
            if current.left is None:
                current.left = comparable
                break
            else:
                current = current.left
        elif current_comparable == 1:
            if current.right is None:
                current.right = comparable
                break
            else:
                current = current.right
        else:
            current.data = data
    return tree


def _find_min_data_node(node):
    parent = None
    current = node
    while current.left:
        parent = current
        current = current.left
    return parent, current


def delete(tree, data):
    if tree is None or tree.root is None or data is None:
        return tree

    parent = None
    current = tree.root
    comparable = _create_node(data)

    while current:
        current_comparable = tree.compare(current, comparable)
        if current_comparable == 0:
            break
        parent = current
        if current_comparable == -1:
            current = current.left
        else:
            current = current.right
    else:
        return tree

    if current.left is None and current.right is None:
        if parent is None:
            tree.root = None
        elif parent.left is current:
            parent.left = None
        else:
            parent.right = None

    elif current.left is None:
        if parent is None:
            tree.root = current.right
        elif parent.left is current:
            parent.left = current.right
        else:
            parent.right = current.right

    elif current.right is None:
        if parent is None:
            tree.root = current.left
        elif parent.left is current:
            parent.left = current.left
        else:
            parent.right = current.left

    else:
        min_parent, min_node = _find_min_data_node(current.right)
        current.data = min_node.data

        if min_parent is None:
            current.right = None
        else:
            min_parent.left = None

    return tree



def foreach(tree, func):
    if _is_tree_none(tree):
        return None
    result = []
    stack = []
    current = tree.root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        current.data = func(current.data)
        result.append(current.data)
        current = current.right
    return tree

_preorder_traversal_to_list(foreach(_from_list([50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 68, 81, 93],_default_compare), lambda x: print(x)))
