import os
from array import array
from string import ascii_uppercase

from backend.datastructures.trie import Trie


class DAWG:
    def __init__(self):
        self.trie = Trie()

    def create(self, dictionary_name):
        # Check existence and generate path
        dictionaries_directory = os.path.join(os.getcwd(), 'data', 'dictionaries')
        if dictionary_name not in os.listdir(dictionaries_directory):
            exit("Couldn't find specified dictionary.")
        dictionary_path = os.path.join(dictionaries_directory, dictionary_name)

        # Read file line by line
        file = open(dictionary_path, 'r')
        count = 0
        while True:
            count += 1
            line = file.readline()

            if line:
                self._process_new_line(line)
            else:
                break

        # Number trie
        self.trie.number_trie()

        # Minimze trie to dawg
        self._minimze_trie()

    def _process_new_line(self, line):
        line = line.strip()
        self.trie.add_word(line)

    def _minimze_trie(self):
        node_list = self.trie.node_list()

        # Create list of unique pairs and initialize with false
        pairs: list[array[Trie, Trie, bool]] = []
        for i, node_a in enumerate(node_list[:-1]):
            for node_b in node_list[i+1:]:
                pairs.append([node_a, node_b, False])

        # Mark all pairs as not combinable if they differ in their acceptance
        for i, pair in enumerate(pairs):
            if (pair[0].is_end and not pair[1].is_end) or (pair[1].is_end and not pair[0].is_end):
                pair[2] = True

        # Mark all pairs that are not combinable
        marking_count = 1
        while marking_count > 0:
            marking_count = 0
            filtered_pairs: list[array[Trie, Trie, bool]] = list(filter(lambda p: not p[2], pairs))

            for check_pair in filtered_pairs:
                for letter in ascii_uppercase:

                    if letter in check_pair[0].subtrie_keys() and letter in check_pair[1].subtrie_keys():
                        if (check_pair[0].go(letter).is_end and not check_pair[1].go(letter).is_end) or (check_pair[1].go(letter).is_end and not check_pair[0].go(letter).is_end):
                            check_pair[2] = True
                            marking_count += 1
                            break
                    elif letter in check_pair[0].subtrie_keys() and letter not in check_pair[1].subtrie_keys():
                        if check_pair[0].go(letter).is_end:
                            check_pair[2] = True
                            marking_count += 1
                            break
                    elif letter not in check_pair[0].subtrie_keys() and letter in check_pair[1].subtrie_keys():
                        if check_pair[1].go(letter).is_end:
                            check_pair[2] = True
                            marking_count += 1
                            break


        for i, pair in enumerate(list(filter(lambda p: not p[2], pairs))):
            print(f"{str(pair[0])} - {str(pair[1])} => {str(pair[2])}")

        # Make groups
        groups: list[list[Trie], Trie] = []
        combinable = list(filter(lambda p: not p[2], pairs))

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
            for pair in combinable:
                if pair[0] == node:
                    combinable_with.append(pair[1])
                elif pair[1] == node:
                    combinable_with.append(pair[0])

            group = [[node], Trie()]
            if len(combinable_with) > 0:
                group[0] += combinable_with
            groups.append(group)

        print(len(groups))

        self.dawg = Trie



    def load(self):
        print('Load DAWG ...')
