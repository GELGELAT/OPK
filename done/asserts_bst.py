import binary_search_tree
import creating_massives

arr = creating_massives.make_random_mass(1000)

def test_sorting_algorithms():

    # create
    assert  binary_search_tree._preorder_traversal_to_list(binary_search_tree.create_tree(None))== [], "create 1"

    # clear
    assert  binary_search_tree._preorder_traversal_to_list(binary_search_tree.clear(binary_search_tree.create_tree(None)))== [], "clear 1"
    assert  binary_search_tree._preorder_traversal_to_list(binary_search_tree.clear(binary_search_tree._from_list([1,2,3,4],binary_search_tree._default_compare)))== [], "clear 2"
    assert  binary_search_tree._preorder_traversal_to_list(binary_search_tree.clear(binary_search_tree._from_list([],binary_search_tree._default_compare)))== [], "clear 3"
    assert  binary_search_tree._preorder_traversal_to_list(binary_search_tree.clear(None)) is None, "clear 4"

    # size
    assert  binary_search_tree.size(binary_search_tree._from_list([1,2,3,4],binary_search_tree._default_compare))== 4, "clear 1"
    assert  binary_search_tree.size(binary_search_tree._from_list([],binary_search_tree._default_compare))== 0, "clear 2"
    assert  binary_search_tree.size(binary_search_tree._from_list(None,binary_search_tree._default_compare)) is None, "clear 3"
    assert  binary_search_tree.size(None) is None, "clear 4"


    # find
    assert binary_search_tree.find(binary_search_tree._from_list([1,2,69], binary_search_tree._default_compare), 69) == 69, "find 1"
    assert binary_search_tree.find(binary_search_tree._from_list([], binary_search_tree._default_compare), 69) is None, "find 2"
    assert binary_search_tree.find(None, 69) is None, "find 3"

    # insert
    assert binary_search_tree._preorder_traversal_to_list(binary_search_tree.insert(binary_search_tree._from_list([3,2,69],binary_search_tree._default_compare),1)) == [3,2,1,69], "insert 1"
    assert binary_search_tree._preorder_traversal_to_list(binary_search_tree.insert(binary_search_tree._from_list([],binary_search_tree._default_compare),69)) == [69], "insert 2"
    assert binary_search_tree._preorder_traversal_to_list(binary_search_tree.insert(binary_search_tree._from_list([],binary_search_tree._default_compare),None)) is None, "insert 3"
    assert binary_search_tree._preorder_traversal_to_list(binary_search_tree.insert(None,69)) is None, "insert 4"
    assert binary_search_tree._preorder_traversal_to_list(binary_search_tree.insert(binary_search_tree._from_list([3,2,69],binary_search_tree._default_compare),69)) == [3,2,69], "insert одинаковый"


    #delete
    left = [50, 25, 12, 37, 6, 31, 43]
    right = [50, 75, 62, 87, 56, 68, 81]
    list = [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 68, 81, 93]

    assert binary_search_tree._preorder_traversal_to_list(binary_search_tree.delete(binary_search_tree._from_list(left,binary_search_tree._default_compare),25))  == [50, 31, 12, 6, 37, 43], "delete 1 2 соседа"
    assert binary_search_tree._preorder_traversal_to_list(binary_search_tree.delete(binary_search_tree._from_list(left,binary_search_tree._default_compare),12))  == [50, 25, 6, 37, 31, 43], "delete 2 1 сосед"
    assert binary_search_tree._preorder_traversal_to_list(binary_search_tree.delete(binary_search_tree._from_list(left,binary_search_tree._default_compare),18))  == [50, 25, 12, 6, 37, 31, 43], "delete 3 нет соседа"

    assert binary_search_tree._preorder_traversal_to_list(binary_search_tree.delete(binary_search_tree._from_list(list,binary_search_tree._default_compare),50))  == [56, 25, 12, 6, 18, 37, 31, 43, 75, 62, 68, 87, 81, 93], "delete 4"

    assert binary_search_tree._preorder_traversal_to_list(binary_search_tree.delete(binary_search_tree._from_list(right,binary_search_tree._default_compare),75))  == [50, 81, 62, 56, 68, 87], "delete 1"
    assert binary_search_tree._preorder_traversal_to_list(binary_search_tree.delete(binary_search_tree._from_list(right,binary_search_tree._default_compare),87))  == [50, 75, 62, 56, 68, 81], "delete 2"
    assert binary_search_tree._preorder_traversal_to_list(binary_search_tree.delete(binary_search_tree._from_list(right,binary_search_tree._default_compare),81))  == [50, 75, 62, 56, 68, 87], "delete 3"

    assert binary_search_tree._preorder_traversal_to_list(binary_search_tree.delete(binary_search_tree._from_list([1],binary_search_tree._default_compare),1))  == [], "delete 4"
    assert binary_search_tree._preorder_traversal_to_list(binary_search_tree.delete(binary_search_tree._from_list([2,3],binary_search_tree._default_compare),1))  == [2,3], "delete 4"

    assert binary_search_tree._preorder_traversal_to_list(binary_search_tree.delete(binary_search_tree._from_list([2,3],binary_search_tree._default_compare),None))  == [2,3], "delete 4"
    assert binary_search_tree._preorder_traversal_to_list(binary_search_tree.delete(binary_search_tree._from_list(None,binary_search_tree._default_compare),1))  is None, "delete 4"
    assert binary_search_tree._preorder_traversal_to_list(binary_search_tree.delete(binary_search_tree._from_list([],binary_search_tree._default_compare),1)) == [], "delete 4"




test_sorting_algorithms()

binary_search_tree._preorder_traversal_to_list(binary_search_tree.foreach(binary_search_tree._from_list([50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 68, 81, 93],binary_search_tree._default_compare), lambda x: print(x+6969)))
print(binary_search_tree._preorder_traversal_to_list(binary_search_tree._from_list(arr, binary_search_tree._default_compare)))
