"""
The module contains a directed acyclic graph and its creation logic.
It can be used to represent a dictionary
"""
import os
import sys
from string import ascii_uppercase
from typing import TypeVar

from src.backend.datastructures.graphnode import GraphNode


class DAWG:
    """
    Directed acyclic word graph
    """
    def __init__(self):
        self.trie = GraphNode()

    def create(self, dictionary_name: str) -> None:
        """
        Creates the dawg from scratch
        :param dictionary_name: Name of the dictionary
        """
        # Check existence and generate path
        dictionaries_directory = os.path.join(os.getcwd(), 'data', 'dictionaries')
        if dictionary_name not in os.listdir(dictionaries_directory):
            sys.exit("Couldn't find specified dictionary.")
        dictionary_path = os.path.join(dictionaries_directory, dictionary_name)

        # Read file line by line
        with open(dictionary_path, 'r', encoding='utf-8') as file:
            count = 0
            while True:
                count += 1
                line = file.readline()

                if line:
                    self._process_new_line(line)
                else:
                    break

            # Number trie
            self.trie.number_graph()

            # Minimize trie to dawg
            self._minimize_trie()

    def _process_new_line(self, line: str) -> None:
        """
        Processes a single line that is read from the dictionary file.
        """
        line = line.strip()
        self.trie.add_word(line)

    def _minimize_trie(self):
        """
        Minimizes the trie into a directed acyclic graph using Nerode
        """

        # Create list of all nodes
        node_list = self.trie.node_list()

        # Create list of unique pairs and initialize with false
        pairs: list[[GraphNode, GraphNode, bool]] = DAWG._list_to_pairs(node_list)

        # Mark all pairs as not combinable if they differ in their acceptance
        for pair in pairs:
            pair[2] = not GraphNode.compare_end_states(pair[0], pair[1])

        # Mark all pairs that are not combinable
        pairs = DAWG._mark_pairs_by_transitions(pairs)

        # Make groups
        groups = DAWG._group_pairs(node_list, pairs)

        # Create dawg from groups
        self.dawg = DAWG._create_dawg_from_groups(groups, self.trie)

    def load(self) -> None:
        """
        Loads the DAWG from a file
        """

    # Static members for minimization ------------------------------------------------------
    T = TypeVar('T')  # Defines generic type T

    @staticmethod
    def _create_dawg_from_groups(groups: list[[list[GraphNode], GraphNode]], old_start: GraphNode) -> GraphNode:
        """
        Takes the groups of trie-nodes and combines them in a new dawg.
        :param groups: The trie-node groups
        :param old_start: Reference to the old starting node of the trie.
        :return: Reference to the new starting node of the DAWG
        """
        new_dawg: GraphNode = GraphNode()
        for group in groups:
            group_nodes: list[GraphNode] = group[0]
            group_trie: GraphNode = group[1]

            # Set end state
            if group_nodes[0].is_end:
                group_trie.is_end = True

            # Add transitions
            for node in group_nodes:
                for letter, transition_trie in zip(node.transition_keys(), node.transition_values()):
                    destination_group_trie = DAWG._find_group(groups, transition_trie)[1]
                    group_trie.add_transition(letter, destination_group_trie)

            if old_start in group_nodes:
                new_dawg = group_trie

        new_dawg.number_graph()
        return new_dawg

    @staticmethod
    def _group_pairs(node_list: list[GraphNode],
                     pairs: list[[GraphNode, GraphNode, bool]]) -> list[[list[GraphNode], GraphNode]]:
        """
        Takes a list of pairs and groups them together by the ability to be combined.
        :param node_list: List of all nodes
        :param pairs: List of all pairs
        :return: List of groups
        """
        groups: list[[list[GraphNode], GraphNode]] = []

        for node in node_list:
            # Check if node is already in one of the groups
            in_group = False
            for group_list in groups:
                if node in group_list[0]:
                    in_group = True

            if in_group:
                continue

            # Get all nodes with which the node is combinable
            combinable_with = []
            for pair in DAWG._filter_pairs(pairs, combinable=True):
                if pair[0] == node:
                    combinable_with.append(pair[1])
                elif pair[1] == node:
                    combinable_with.append(pair[0])

            group = [[node], GraphNode()]
            if len(combinable_with) > 0:
                group[0] += combinable_with
            groups.append(group)
        return groups

    @staticmethod
    def _mark_pairs_by_transitions(pairs: list[[GraphNode, GraphNode, bool]]) -> list[list[GraphNode, GraphNode, bool]]:
        """
        Takes all pairs and marks some as not combinable, if a not combinable pair can be reached.
        :param pairs: List of pairs
        :return: Updated list of pairs
        """
        marking_count = 1
        while marking_count > 0:
            marking_count = 0

            # Loop through all pairs, that are still combinable
            for check_pair in DAWG._filter_pairs(pairs, combinable=True):
                a: GraphNode = check_pair[0]  # First node of the pair
                b: GraphNode = check_pair[1]  # Second node of the pair

                # For each pair, check each letter
                for letter in ascii_uppercase:

                    # Both have a transition with the same letter
                    if letter in a.transition_keys() and letter in b.transition_keys():
                        destination_pair = DAWG._find_pair(pairs, [a.go(letter), b.go(letter)])
                        if destination_pair[2]:
                            check_pair[2] = True
                            marking_count += 1
                            break

                    # One of the nodes has the letter and the other would transition into an and state
                    if (letter in a.transition_keys() and letter not in b.transition_keys()
                            or letter not in a.transition_keys() and letter in b.transition_keys()):
                        check_pair[2] = True
                        marking_count += 1
                        break
        return pairs

    @staticmethod
    def _list_to_pairs(li: list[T]) -> list[[T, T, bool]]:
        """
        Takes a list and combines its elements in unique pairs.
        """
        pairs = []
        for i, a in enumerate(li[:-1]):
            for b in li[i + 1:]:
                pairs.append([a, b, False])
        return pairs

    @staticmethod
    def _print_pair(pair: [GraphNode, GraphNode, bool]):
        """
        Prints a pair to the console
        """
        print(f"{str(pair[0])} - {str(pair[1])} => {str(pair[2])}")

    @staticmethod
    def _print_pairs(pairs: list[[GraphNode, GraphNode, bool]]):
        """
        Prints all pairs to the console
        """
        for pair in pairs:
            DAWG._print_pair(pair)

    @staticmethod
    def _filter_pairs(pairs: list[[GraphNode, GraphNode, bool]], combinable: bool):
        """
        Filters the list of pairs and returns only (not) combinable pairs
        """
        return list(filter(lambda p: p[2] != combinable, pairs))

    @staticmethod
    def _find_pair(pairs: list[[GraphNode, GraphNode, bool]],
                   pair_to_find: list[GraphNode]) -> [GraphNode, GraphNode, bool]:
        """
        Finds a pair in a list of pairs
        """
        for pair in pairs:
            # Kleine Zahl steht links
            if (pair_to_find[0] == pair[0] and pair_to_find[1] == pair[1]
                    or pair_to_find[1] == pair[0] and pair_to_find[0] == pair[1]):
                return pair
        return []

    @staticmethod
    def _find_group(groups: list[list[GraphNode], GraphNode], trie: GraphNode) -> [list[GraphNode], GraphNode]:
        """
        Takes a trie and finds the group, the trie belongs to.
        :param groups: List of groups
        :param trie: Trie to find
        :return: Group of the trie
        """
        for group in groups:
            if trie in group[0]:
                return group
        return []
