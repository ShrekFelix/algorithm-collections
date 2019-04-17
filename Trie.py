from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children=defaultdict(TrieNode)
        self.isWord=False

class Trie:    
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node=self.root
        for letter in word:
            node=node.children[letter]
        node.isWord=True
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node=self.root
        for letter in word:
            if letter in node.children:
                node=node.children[letter]
            else:
                return False
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node=self.root
        for letter in prefix:
            if letter in node.children:
                node=node.children[letter]
            else:
                return False
        return True

# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)