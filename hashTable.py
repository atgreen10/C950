# HashTable class using chaining.
class Hash_Table(object):
    # 2 dimensional array

    def __init__(self, initialCapacity=39):
        self.capacity = initialCapacity
        self.size = 0
        self.bucket = [None] * self.capacity



    def hash(self, key):
        hashVal = key
        return hashVal

    def add(self, key, value):
        self.size += 1
        index = self.hash(key)
        if self.bucket[index] is not None:
            # checks is the add is an update to already existing key value pair
            for kvpair in self.bucket[index]:
                # if key is found then update its value to the new value
                if kvpair[0] == key:
                    kvpair[1] = value
                    break
            else:
                # no key was found and can be added to end of the list
                self.bucket[index].append([key, value])
        else:
            # initiates a list to append the key-value pair to.
            self.bucket[index] = []
            self.bucket[index].append([key, value])

    def get(self, key):
        index = self.hash(key)
        if self.bucket[index] is None:
            raise KeyError()
        else:
            for kvpair in \
                    self.bucket[index]:
                if kvpair[0] == key:
                    return kvpair[1]

    def delete(self, key):
        index = self.hash(key)
        for match in self.bucket[index]:
            if match[0] == key:
                self.bucket[index].remove([match[0], match[1]])
