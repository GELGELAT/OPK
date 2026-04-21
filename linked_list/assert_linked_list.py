import linked_list

from linked_list import from_list, remove, append, remove_first


def test_sorting_algorithms():
    # from_list и to_list
    assert linked_list.to_list(linked_list.from_list([0, 1, 2, 3])) == [0, 1, 2, 3], "from_list 1"
    assert linked_list.to_list(linked_list.from_list([0])) == [0], "from_list 2"
    assert linked_list.to_list(linked_list.from_list([])) is None, "from_list 3"
    assert linked_list.to_list(linked_list.from_list(None)) is None, "from_list 4"

    # length
    assert linked_list.length(linked_list.from_list([0, 1, 2, 3])) == 4, "length 1"
    assert linked_list.length(linked_list.from_list([0])) == 1, "length 2"
    assert linked_list.length(linked_list.from_list([])) == 0, "length 3"
    assert linked_list.length(linked_list.from_list(None)) == 0, "length 4"
    assert linked_list.length(None) == 0, "length 5"

    # prepend
    assert linked_list.to_list(linked_list.prepend(linked_list.from_list([0, 1, 2, 3]), 69)) == [69, 0, 1, 2,
                                                                                                 3], "prepend 1"
    assert linked_list.to_list(linked_list.prepend(linked_list.from_list([]), 69)) == [69], "prepend 2"
    assert linked_list.to_list(linked_list.prepend(linked_list.from_list(None), 69)) == [69], "prepend 3"
    assert linked_list.to_list(linked_list.prepend(linked_list.from_list([0, 1, 2, 3]), None)) == [0, 1, 2,
                                                                                                   3], "prepend 3"
    assert linked_list.to_list(linked_list.prepend(None, 69)) == [69], "prepend 4"

    # get
    assert linked_list.get(from_list([1, 2]), 0) == 1, "get 1"
    assert linked_list.get(from_list([1, 2]), 1) == 2, "get 2"
    assert linked_list.get(from_list([1, 2]), 2) == -1, "get 3"
    assert linked_list.get(from_list([1, 2]), None) == -1, "get 4"
    assert linked_list.get(None, 69) == -1, "get 5"

    # remove
    assert linked_list.to_list(remove(from_list([1, 2, 3, 4, 5]), 0)[1]) == [2, 3, 4, 5], "remove 1"
    assert linked_list.to_list(remove(from_list([1, 2, 3, 4, 5]), 1)[1]) == [1, 3, 4, 5], "remove 2"
    assert linked_list.remove(linked_list.from_list([1, 2]), None) == -1, "remove 3"
    assert linked_list.remove(None, 69) == -1, "remove 4"
    assert linked_list.to_list(remove(from_list([1]), 0)[1]) is None, "remove 5"

    # append
    assert linked_list.to_list(append(from_list([1]), 69)) == [1, 69], "append 1"
    assert linked_list.to_list(append(from_list([1]), None)) == [1], "append 2"
    assert linked_list.to_list(append(from_list([]), 69)) == [69], "append 3"
    assert linked_list.to_list(append(None, 69)) == [69], "append 4"
    assert linked_list.to_list(append(None, None)) is None, "append 5"

    # get_last
    assert linked_list.get_last(from_list([1, 2, 3, 4, 5])) == 5, "get_last 1"
    assert linked_list.get_last(from_list(None)) is None, "get_last 2"

    # find
    assert linked_list.find(from_list([0, 1, 2, 3, 4, 5]), 5) == 5, "find 1"
    assert linked_list.find(from_list([0, 1, 2, 3, 4, 5]), 0) == 0, "find 2"
    assert linked_list.find(from_list([0, 1, 2, 3, 4, 5]), None) == -1, "find 3"
    assert linked_list.find(from_list([0, 1, 2, 3, 4, 5]), 69) == -1, "find 4"
    assert linked_list.find(None, 69) == -1, "find 5"

    # remove_first
    assert linked_list.to_list(remove_first(from_list([1, 2, 3, 4, 5]), 2)) == [1, 3, 4, 5], "remove_first 1"
    assert linked_list.to_list(remove_first(from_list([1, 2, 3, 4, 5, 1]), 1)) == [2, 3, 4, 5, 1], "remove_first 2"
    assert linked_list.to_list(remove_first(from_list([1, 2, 3, 4, 5]), 69)) == [1, 2, 3, 4, 5], "remove_first 3"
    assert linked_list.to_list(remove_first(from_list([1, 2, 3, 4, 5]), None)) == [1, 2, 3, 4, 5], "remove_first 4"
    assert linked_list.to_list(remove_first(None, 69)) is None, "remove_first 5"
    assert linked_list.to_list(remove_first(None, None)) is None, "remove_first 6"

    # remove_all
    assert linked_list.to_list(linked_list.remove_all(from_list([3, 1, 3, 2, 3, 4, 5, 3]), 3)) == [1, 2, 4,
                                                                                                   5], "remove_all 1"
    assert linked_list.to_list(linked_list.remove_all(from_list([3, 1, 3, 2, 3, 4, 5, 3]), 1)) == [3, 3, 2, 3, 4, 5,
                                                                                                   3], "remove_all 2"
    assert linked_list.to_list(linked_list.remove_all(from_list([3, 1, 3, 2, 3, 4, 5, 3]), 69)) == [3, 1, 3, 2, 3, 4, 5,
                                                                                                    3], "remove_all 3"
    assert linked_list.to_list(linked_list.remove_all(from_list([3, 1, 3, 2, 3, 4, 5, 3]), None)) == [3, 1, 3, 2, 3, 4,
                                                                                                      5,
                                                                                                      3], "remove_all 4"
    assert linked_list.to_list(linked_list.remove_all(None, 69)) is None, "remove_all 5"
    assert linked_list.to_list(linked_list.remove_all(None, None)) is None, "remove_all 6"

    # copy
    assert linked_list.to_list(linked_list.copy(from_list([3, 1, 3, 2, 3, 4, 5, 3]))) == [3, 1, 3, 2, 3, 4, 5,3], "copy 1"
    assert linked_list.to_list(linked_list.copy(None)) is None, "copy 2"

    #concat
    assert linked_list.to_list(linked_list.concat(from_list([3, 1, 3, 2, 3, 4, 5, 3]),from_list([69669696969]))) == [3, 1, 3, 2, 3, 4, 5, 3, 69669696969], "concat 1"
    assert linked_list.to_list(linked_list.concat(None,from_list([69669696969]))) == [69669696969], "concat 2"
    assert linked_list.to_list(linked_list.concat(from_list([3, 1, 3, 2, 3, 4, 5, 3]),None)) == [3, 1, 3, 2, 3, 4, 5, 3], "concat 3"
    assert linked_list.to_list(linked_list.concat(None,None)) is None, "concat 4"

    #find_custom
    assert linked_list.find_custom(from_list([3, -1, -3, 2,11, -3, 4, 5, 3]), lambda x: x > 10) == (11, 4), "find_custom 1"
    assert linked_list.find_custom(from_list([3, -1, -3, 2,11, -3, 4, 5, 3]), lambda x: x == 69) == -1, "find_custom 2"
    assert linked_list.find_custom(None, lambda x: x == 69) == -1, "find_custom 3"
test_sorting_algorithms()

#foreach
linked_list.foreach(from_list([3, -1]), lambda x: print(x))
linked_list.foreach(from_list([3, -1]), lambda x: print(x*2))
