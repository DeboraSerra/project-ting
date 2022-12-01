class Queue:
    def __init__(self):
        self.line = []

    def __len__(self):
        return len(self.line)

    def enqueue(self, value):
        self.line.append(value)

    def dequeue(self):
        first_item = self.line[0]
        self.line.pop(0)
        return first_item

    def search(self, index):
        if index < 0 or index >= len(self.line):
            raise IndexError()
        return self.line[index]
