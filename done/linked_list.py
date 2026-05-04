class Node:
    pass


class LinkedList:
    pass


def _is_not_none_node(node):
    if node is None or node.data is None:
        return None
    return node


def _is_not_none_data(data):
    if data is None:
        return None
    return data


def create_node(data):
    node = Node()
    node.data = data
    node.next = None
    return node


def create_linked_list(data):
    head = create_node(data)
    return head


def length(head):
    if _is_not_none_node(head):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length
    return 0


def prepend(head, data):
    if _is_not_none_data(data):
        new_node = create_node(data)
        new_node.next = head
        return new_node
    return head


def append(head, data):
    if _is_not_none_data(data):
        if head:
            new_node = create_node(data)
            current = head
            current_index = 0
            for _ in range(length(head) - 1):
                current = current.next
                current_index += 1
            current.next = new_node
            return head
        return create_linked_list(data)
    return head


def get(head, index):
    if _is_not_none_node(head) and index is not None and index < length(head) and index >= 0:
        index_current = 0
        current = head
        while current:
            if index == index_current:
                return current.data
            index_current += 1
            current = current.next
        return head.data
    return -1


def get_last(head):
    if _is_not_none_node(head):
        current = head
        for _ in range(length(head) - 1):
            current = current.next
        return current.data
    return None


def remove(head, index):
    if _is_not_none_node(head) and index is not None and index < length(head) and index >= 0:
        index_current = 0
        current = head
        main = current.next
        while current:
            if index_current == index - 1:
                main = current
                deleted = current.next
                for _ in range(2):
                    current = current.next
                    main.next = current
                return deleted.data, head
            index_current += 1
            current = current.next
        return head.data, main
    return -1


def find(head, data):
    current = head
    current_index = 0
    for _ in range(length(head)):
        if current.data == data:
            return current_index
        current = current.next
        current_index += 1
    return -1


def _find_all(head, data):
    current = head
    current_index = 0
    indexes = []
    for _ in range(length(head)):
        if current.data == data:
            indexes.append(current_index)
        current = current.next
        current_index += 1
    return indexes


def remove_first(head, data):
    if _is_not_none_node(head):
        index = find(head, data)
        if index != -1:
            return remove(head, index)[1]
        return head
    return None


def remove_all(head, data):
    if _is_not_none_node(head):
        main = head
        indexes = _find_all(head, data)
        for i in range(len(indexes)):
            main = remove_first(main, data)
        return main
    return None


def copy(head):
    if _is_not_none_node(head):
        main = head
        copied = create_linked_list(get(head, 0))
        current = copied
        for i in range(length(head) - 1):
            current.next = create_node(get(main, i + 1))
            current = current.next
        return copied
    return None


def concat(head1, head2):
    copied1 = copy(head1)
    copied2 = copy(head2)
    if copied1 is not None:
        current = copied1
        for _ in range(length(copied1) - 1):
            current = current.next
        current.next = copied2
        return copied1
    return copied2


def foreach(head, func):
    if _is_not_none_node(head):
        current = head
        for _ in range(length(head)):
            current.data = func(current.data)
            current = current.next
        return head
    return None


def find_custom(head, predicate):
    if _is_not_none_node(head):
        current = head
        current_index = 0
        for _ in range(length(head)):
            if predicate(current.data):
                return current.data, current_index
            current_index += 1
            current = current.next
        return -1

    return -1


def from_list(list):
    if list:
        head = create_linked_list(list[0])
        current = head
        for i in range(len(list) - 1):
            current.next = create_node(list[i + 1])
            current = current.next
        return head
    return None


def to_list(head):
    if head != -1 and _is_not_none_node(head):
        nodes = []
        current = head
        while current:
            nodes.append(current.data)
            current = current.next
        return nodes
    return None



