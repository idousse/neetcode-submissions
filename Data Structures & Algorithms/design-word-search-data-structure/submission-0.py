class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.endOfWord = True
        

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return node.endOfWord

            if word[i] == ".":
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True
                return False

            else:
                if word[i] not in node.children:
                    return False
                
                node = node.children[word[i]]

                return dfs(node, i+1)
                
        

        return dfs(self.root, 0)







        
