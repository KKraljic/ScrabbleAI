
class Trie:
    def __init__(self):
        self.subtries: dict[str, Trie] = {}
        self.is_end = False
        self.number = 0

    def add_word(self, word):
        if len(word) == 0:
            self.is_end = True
        if len(word) >= 1:
            if word[0] not in self.subtries.keys():
                self.subtries[word[0]] = Trie()
            self.subtries[word[0]].add_word(word[1:])

    def node_list(self):
        node_list: list[Trie] = [self]
        if len(self.subtries) > 0:
            for subtrie in self.subtries.values():
                node_list += subtrie.node_list()


        return node_list

    def number_trie(self):
        for i, node in enumerate(self.node_list()):
            node.set_number(i)

    def set_number(self, number):
        self.number = number

    def go(self, letter):
        return self.subtries[letter]

    def subtrie_keys(self):
        return self.subtries.keys()

    def __str__(self):
        return f"[{self.number}]"
