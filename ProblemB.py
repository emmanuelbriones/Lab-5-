import matplotlib.pyplot as plt
import math


class MaxHeap(object):
    # Constructor
    def __init__(self):
        self.tree = []

    def is_empty(self):
        return len(self.tree) == 0

    def parent(self, i):
        if i == 0:
            return ""
        return self.tree[(i - 1) // 2]

    def left_child(self, i):
        c = 2 * i + 1
        if c >= len(self.tree):
            return ""
        return self.tree[c]

    def right_child(self, i):
        c = 2 * i + 2
        if c >= len(self.tree):
            return ""
        return self.tree[c]

    def insert(self, item):
        self.tree.append(item)
        self._percolate_up(len(self.tree) - 1)

    def _percolate_up(self, i):
        if i == 0:
            return

        parent_index = (i - 1) // 2

        if self.tree[parent_index] < self.tree[i]:
            self.tree[i], self.tree[parent_index] = self.tree[parent_index], self.tree[i]
            self._percolate_up(parent_index)

    def extract_max(self):
        if len(self.tree) < 1:
            return None
        if len(self.tree) == 1:
            return self.tree.pop()

        root = self.tree[0]
        self.tree[0] = self.tree.pop()

        self._percolate_down(0)

        return root

    def _percolate_down(self, i):

        if self.tree[i] >= max(self.left_child(i), self.right_child(i)):
            return

        max_child_index = 2 * i + 1 if self.left_child(i) > self.right_child(i) else 2 * i + 2

        self.tree[i], self.tree[max_child_index] = self.tree[max_child_index], self.tree[i]
        self._percolate_down(max_child_index)


    def draw(self):
        if not self.is_empty():
            fig, ax = plt.subplots()
            self.draw_(0, 0, 0, 100, 50, ax)
            ax.axis('off')
            ax.set_aspect(1.0)

            plt.show()

    def draw_(self, i, x, y, dx, dy, ax):
        if self.left_child(i) > -math.inf:
            ax.plot([x, x - dx], [y, y - dy], linewidth=1, color='k')
            self.draw_(2 * i + 1, x - dx, y - dy, dx / 2, dy, ax)
        if self.right_child(i) > -math.inf:
            ax.plot([x, x + dx], [y, y - dy], linewidth=1, color='k')
            self.draw_(2 * i + 2, x + dx, y - dy, dx / 2, dy, ax)
        ax.text(x, y, str(self.tree[i]), size=20,
                ha="center", va="center",
                bbox=dict(facecolor='w', boxstyle="circle"))

    def k_frequent(self, k):
        # raise an error if k is out of bounds
        if k >= len(self.tree) or k<=0:
            raise ValueError("Not in Bounds")
            return -1
        # create dictionary to keep count of the words
        hashmap = {}
        # traverse through the heap
        while self.tree:
            key = self.extract_max()
            # add every element of the heap and the number of times seen
            if key in hashmap:
                hashmap[key] += 1
            else: hashmap[key] = 1
        # get the word with the biggest value k times
        for i in range(k):
            key2, value = self.find_biggest(hashmap)
            print(key2, value)

    def find_biggest(self, hashmap):
        max = 0
        key2 = ""
        # iterate through the dictionary and compare values
        for key in hashmap:
            if hashmap[key] > max: 
                max = hashmap[key]
                key2 = key
        # set the current biggest value to 0 to not repeat the value 
        hashmap[key2] = 0
        return key2, max

def heap_sort(a_lst):
    h = MaxHeap()
    for a in a_lst:
        h.insert(a)
    i = len(a_lst) - 1
    while not h.is_empty():
        a_lst[i] = h.extract_max()
        i -= 1



if __name__ == "__main__":
    plt.close("all")
    h = MaxHeap()
    a_list = ["and", "need", "before", "and", "cat", "dog", "and", "need", "help", "dog", "hello", "hi", "hello"]
    for a in a_list:
        h.insert(a)
    print(h.tree)

    #h.draw()
    '''
    while not h.is_empty():
        a = h.extract_max()
        print(h.tree)
    '''
    #heap_sort(a_list)
    #print(a_list)
    print("The most frequent words:")
    h.k_frequent(5)
    