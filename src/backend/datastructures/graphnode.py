"""
The module contains the GraphNode from wich a letter tree or a dawg can be build
"""

from __future__ import annotations


class GraphNode:
    """
    Single node of a graph.
    """
    def __init__(self, num=0):
        self.subgraphs: dict[str, GraphNode] = {}
        self.is_end = False
        self.number = num

    def add_word(self, word: str) -> None:
        """
        Adds a word to the graph, using new nodes
        :param word: Word to be added
        """
        if len(word) == 0:
            self.is_end = True
        if len(word) >= 1:
            if word[0] not in self.subgraphs:
                self.subgraphs[word[0]] = GraphNode()
            self.subgraphs[word[0]].add_word(word[1:])

    def add_transition(self, letter: str, node: GraphNode) -> None:
        """
        Add a transition the node
        :param letter: Letter of the transition
        :param node: Connected node
        """
        self.subgraphs[letter] = node

    def node_list(self) -> list[GraphNode]:
        """
        Creates a list of all connected Nodes
        :return: List of the nodes
        """
        node_list: list[GraphNode] = [self]
        if len(self.subgraphs) > 0:
            for subgraph in self.subgraphs.values():
                node_list += subgraph.node_list()
        return node_list

    def number_graph(self) -> None:
        """
        Takes the whole graph and assigns a unique number to each node.
        """
        for i, node in enumerate(self.node_list()):
            node.set_number(i)

    def set_number(self, number):
        """
        Sets the number of the node
        """
        self.number = number

    def go(self, letter: str) -> GraphNode:
        """
        Uses a transition to go to the next node.
        :param letter: Letter of the transition.
        :return: Reached node.
        """
        return self.subgraphs[letter]

    def transition_keys(self) -> list[str]:
        """
        Returns a list of all keys from all transitions
        """
        return list(self.subgraphs.keys())

    def transition_values(self) -> list[GraphNode]:
        """
        Returns a list of all values reachable from all transitions
        """
        return list(self.subgraphs.values())

    def __str__(self):
        return f"[{self.number}]"

    # Static members ------------------------------------------------------
    @staticmethod
    def compare_end_states(a: GraphNode, b: GraphNode) -> bool:
        """
        Compares if the both nodes are end states
        """
        return (a.is_end and b.is_end) or (not a.is_end and not b.is_end)
