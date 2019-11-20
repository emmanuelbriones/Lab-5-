class DLL(object):
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value

    def __str__(self):
        return "(%s, %s)" % (self.key, self.value)


class LRU(object):
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity has to be > 0")
        self.hash_map = {}
        self.head = None
        self.end = None
        self.capacity = capacity
        self.current_size = 0

    def get(self, key):
        if key not in self.hash_map:
            return -1
        node = self.hash_map[key]
        if self.head == node:
            return node.value
        self.remove(node)
        self.set_head(node)
        return node.value

    def put(self, key, value):
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value
            if self.head != node:
                self.remove(node)
                self.set_head(node)
        else:
            new_node = DLL(key, value)
            if self.current_size == self.capacity:
                del self.hash_map[self.end.key]
                self.remove(self.end)
            self.set_head(new_node)
            self.hash_map[key] = new_node

    def max_capacity(self):
        return self.capacity

    def size(self):
        return self.current_size

    def print(self):
        n = self.head
        print("head =",self.head)
        print("end =",self.end)
        while n:
            print(n)
            n = n.prev
        
    def remove(self, node):
        if not self.head:
            return
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if not node.next and not node.prev:
            self.head = None
            self.end = None
        if self.end == node:
            self.end = node.next
            self.end.prev = None
        self.current_size -= 1
        return node

    def set_head(self, node):
        if not self.head:
            self.head = node
            self.end = node
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node
        self.current_size += 1


def main():
    lru = LRU(capacity=5)
    lru.put(1, 6)
    lru.put(2, 9)
    lru.put(3, 9)
    lru.put(4, 69)
    lru.put(5, 32)
    print(lru.size())
    print(lru.get(4))
    print(lru.get(2))
    lru.put(6, 69)
    print(lru.get(2))
    print(lru.get(1))
    print(lru.max_capacity())
    lru.print()


if __name__ == '__main__':
    main()