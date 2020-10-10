'''Data Structure: Array, maintains a list of homogenous elements'''
class Array(object):

    def __init__(self, capacity, arrayType=int):
        self.capacity = capacity
        self.arrayItems = [arrayType(0)] * capacity
        self.arrayType = arrayType
        self.length = 0

    def __str__(self):
        return ' '.join([str(i) for i in self.arrayItems])

    def __len__(self):
        return self.length

    def __setitem__(self, index, data):
        self.arrayItems[index] = data

    def __getitem__(self, index):
        return self.arrayItems[index]

    # linear search
    def search(self, keyToSearch):
        for i in range(self.length):
            if (self.arrayItems[i] == keyToSearch):
                print('Key {} found at index {}'.format(keyToSearch, i))
                return

        print('Key not found in the array')

    def insert(self, keyToInsert, position=0):
        # if position too large, simply append at end
        if (position >= self.length):
            self.arrayItems[self.length] = keyToInsert
            self.length += 1

        # insert at given position
        else:
            # first displace forward by one position
            for i in range(self.length - 1, position - 1, -1):
                self.arrayItems[i + 1] = self.arrayItems[i]

            # then insert at the given position
            self.arrayItems[position] = keyToInsert
            self.length += 1

        # double the capacity if capacity full
        if (self.length == self.capacity):
            self.capacity *= 2

            newarray = [arrayType(0)] * self.capacity
            for i in range(self.length):
                newarray[i] = self.arrayItems[i]
            self.arrayItems = newarray

    def remove(self, keyToDelete):

        index = -1
        # first find the index of the element
        for i in range(self.length):
            if self.arrayItems[i] == keyToDelete:
                index = i
                break

        if index == -1:
            print('Key {} not found'.format(keyToDelete))

        else:
            # then just displace the next elements by -1
            for i in range(i, self.length):
                self.arrayItems[i] = self.arrayItems[i + 1]
            self.length -= 1


if __name__ == '__main__':
    a = Array(10, str)
    a.remove('Krishna')
    a.insert('Krishna')
    a.insert('Madhav')
    a.insert('Kapil', 50)
    a.insert('Rishikesh', 1)
    a.search('Madhav')
    a.remove('Rishikesh')
    print(a)
    print(a.length)
