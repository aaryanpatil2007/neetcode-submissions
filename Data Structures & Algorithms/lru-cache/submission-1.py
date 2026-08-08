class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if not key in self.cache.keys():
            return -1
        else:
            save = self.cache[key]
            self.delete(save)
            self.insert(save)
            return save.val
        
        # if not key in cache return none
        # remove key from linked list
        # add key to right side of list
        # return value


    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            save = self.cache[key]
            self.delete(save)
            save.val = value
            self.insert(save)
        else:
            if len(self.cache) == self.capacity:
                lru = self.left.next
                self.delete(lru)
                del self.cache[lru.key]
                new = Node(key, value)
                self.insert(new)
                self.cache[key] = new
            else:
                new = Node(key, value)
                self.insert(new)
                self.cache[key] = new

        # if key already in map: remove from ll, add key to right side, update value
        # if not key in map:
            # if greater than capacity, remove lru 
            # else add to right side of the list
            
                
    def insert(self, node: Node):
        # add to right side of list 
        save = self.right.prev
        self.right.prev = node
        save.next = node
        node.prev = save
        node.next = self.right
        

    def delete(self, node: Node):
        # reorder nodes
        save1 = node.prev
        save2 = node.next
        save1.next = save2
        save2.prev = save1




