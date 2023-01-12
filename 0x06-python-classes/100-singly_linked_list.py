#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:

    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (value is not None) and (not isinstance(value, Node)):
            raise TypeError("next node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self) -> None:
        self.__head = None  # head node

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """

        new = Node(value)
        # for an empty list
        if self.__head is None:
            new.next_node = None
            self.__head = new   # head node is now new node
        # for a non-empty list with value less than data
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            # for a non-empty node with value greater than data
            temp = self.__head  # create temp value
            while (temp.next_node is not None and
                   temp.next_node.data < value):
                # keep searching until value < data
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""

        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ("\n".join(values))
