"""Unit tests for the binary search tree module."""

import pytest

from trees import tree_exceptions

from trees.binary_trees import binary_search_tree
from trees.binary_trees import traversal


def test_simple_case(basic_tree):
    """Test the basic methods of a binary search tree."""
    tree = binary_search_tree.BinarySearchTree()

    assert tree.empty

    # 23, 4, 30, 11, 7, 34, 20, 24, 22, 15, 1
    for key, data in basic_tree:
        tree.insert(key=key, data=data)

    assert tree.empty is False
    assert tree.get_leftmost(node=tree.root).key == 1
    assert tree.get_leftmost(node=tree.root).data == "1"
    assert tree.search(key=24).data == "24"
    assert tree.get_height(node=tree.root) == 4

    tree.delete(key=15)
    tree.delete(key=22)
    tree.delete(key=7)
    tree.delete(key=20)

    with pytest.raises(tree_exceptions.KeyNotFoundError):
        tree.search(key=15)


def test_deletion(basic_tree):
    """Test the deletion of a binary search tree."""
    tree = binary_search_tree.BinarySearchTree()

    # 23, 4, 30, 11, 7, 34, 20, 24, 22, 15, 1
    for key, data in basic_tree:
        tree.insert(key=key, data=data)

    # No child
    tree.delete(15)
    assert [item for item in traversal.levelorder_traverse(tree)] == [
        (23, "23"),
        (4, "4"),
        (30, "30"),
        (1, "1"),
        (11, "11"),
        (24, "24"),
        (34, "34"),
        (7, "7"),
        (20, "20"),
        (22, "22"),
    ]

    # One right child
    tree.delete(20)
    assert [item for item in traversal.levelorder_traverse(tree)] == [
        (23, "23"),
        (4, "4"),
        (30, "30"),
        (1, "1"),
        (11, "11"),
        (24, "24"),
        (34, "34"),
        (7, "7"),
        (22, "22"),
    ]

    # One left child
    tree.insert(key=17, data="17")
    tree.delete(22)
    assert [item for item in traversal.levelorder_traverse(tree)] == [
        (23, "23"),
        (4, "4"),
        (30, "30"),
        (1, "1"),
        (11, "11"),
        (24, "24"),
        (34, "34"),
        (7, "7"),
        (17, "17"),
    ]

    # Two children
    tree.delete(11)
    assert [item for item in traversal.levelorder_traverse(tree)] == [
        (23, "23"),
        (4, "4"),
        (30, "30"),
        (1, "1"),
        (17, "17"),
        (24, "24"),
        (34, "34"),
        (7, "7"),
    ]
