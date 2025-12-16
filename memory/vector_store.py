class VectorStore:
    def __init__(self):
        self.memory = []

    def add(self, text):
        self.memory.append(text)
