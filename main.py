class HashMap:
    def __init__(self, capacity: int = 16, load_factor: float = 0.67) -> None:
        self.capacity = capacity
        self.load_factor = load_factor
        self.threshold = int(self.capacity * self.load_factor)
        self.length = 0
        self.hash_table = [None] * self.capacity

    def put(self, key, value):
        hash_key = hash(key)
        index = hash_key % self.capacity
        while self.hash_table[index] is not None and self.hash_table[index][0] != key:
            index = (index + 1) % self.capacity
        if self.hash_table[index] is not None and self.hash_table[index][0] == key:
            self.hash_table[index] = (key, value)
        else:
            self.hash_table[index] = (key, value)
            self.length += 1
            if self.length >= self.threshold:
                self.resize()

    def get(self, key):
        index = hash(key) % self.capacity
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                return self.hash_table[index][1]
            index = (index + 1) % self.capacity
        raise KeyError(key)

    def __len__(self):
        return self.length

    def resize(self):
        self.capacity *= 2
        old_table = self.hash_table
        self.hash_table = [None] * self.capacity
        self.threshold = int(self.capacity * self.load_factor)
        self.length = 0
        for item in old_table:
            if item is not None:
                self.put(item[0], item[1])

    def contains_key(self, key):
        index = hash(key) % self.capacity
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                return True
            index = (index + 1) % self.capacity
        return False

    def keys(self):
        return [item[0] for item in self.hash_table if item is not None]

    def values(self):
        return [item[1] for item in self.hash_table if item is not None]

    def items(self):
        return [(item[0], item[1]) for item in self.hash_table if item is not None]

    def remove(self, key):
        index = hash(key) % self.capacity
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                self.hash_table[index] = None
                self.length -= 1
                return
            index = (index + 1) % self.capacity
        raise KeyError(key)

    def __iter__(self):
        for item in self.hash_table:
            if item is not None:
                yield item[0], item[1]
