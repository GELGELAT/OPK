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
            break
    return tree


def _find_min_data_node(node):
    current = node
    if current.right.left is None:
        current_data = current.right.data
        current.right = None
        return current_data
    current = node.right
    while True:
        if current.left.left is None:
            current_data = current.left.data
            current.left = None
            return current_data
        else:
            current = current.left


def delete(tree, data):
    if _is_tree_none(tree) or data is None or tree.root is None:
        return tree
    if tree.root.data == data:
        if tree.root.left is None and tree.root.right is None:
            tree.root = None
        elif tree.root.left is not None and tree.root.right is None:
            tree.root = tree.root.left
        elif tree.root.left is None and tree.root.right is not None:
            tree.root = tree.root.right
        else:
            replacemant = _create_node(_find_min_data_node(tree.root))
            tree.root.data = replacemant.data
        return tree
    current = tree.root
    comparable = _create_node(data)

    while True:
        if current.left is not None and current.left.data == comparable.data:
            if current.left.left is None and current.left.right is None:
                current.left = None
            elif current.left.left is not None and current.left.right is None:
                current.left = current.left.left
            elif current.left.left is None and current.left.right is not None:
                current.left = current.left.left
            else:
                replacemant = _create_node(_find_min_data_node(current.left))
                current.left.data = replacemant.data
            return tree
        if current.right is not None and current.right.data == comparable.data:
            if current.right.left is None and current.right.right is None:
                current.right = None
            elif current.right.left is not None and current.right.right is None:
                current.right = current.right.left
            elif current.right.left is None and current.right.right is not None:
                current.right = current.right.right
            else:
                replacemant = _create_node(_find_min_data_node(current.right))
                current.right.data = replacemant.data
            return tree
        current_comparable = tree.compare(current, comparable)
        if current_comparable == -1:
            if current.left is None:
                break
            else:
                current = current.left
        else:
            if current.right is None:
                break
            else:
                current = current.right
    return tree


def foreach(tree, func):
    if _is_tree_none(tree):
        return None
    if tree.root is None:
        return []

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


