class trieNode:
    def __init__(self):
        self.characters = {}
        self.isEndOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = trieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for c in word:
            if c not in current.characters:
                current.characters[c] = trieNode()
            current = current.characters[c]
        current.isEndOfWord = True

    def search(self, word: str) -> bool:
        current = self.root

        for c in word:
            if c not in current.characters:
                return False
            current = current.characters[c]
        return current.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for c in prefix:
            if c not in current.characters:
                return False
            current = current.characters[c]
        return True
