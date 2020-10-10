class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    # define getters and setters
    def setData(self, data):
        self.Data = data

    def setNext(self, next):
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next


class LinkedList(object):
    def __init__(self):
        self.head = None

    def search(self, data):

        if self.head == None:
            print('LL is empty')

        else:
            index = 0
            temp = self.head
            while(temp):
                if (temp.data == data):
                    print('Key {} found at index {}'.format(data, i))
                    return
                temp = temp.next
                index += 1

            print('Key {} not found'.format(data))

    def insertInBeg(self, data):

        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def insertAtEnd(self, data):

        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = newNode

    def insertAtIndex(self, data, index):
        # Case 1: index < 0
        # Case 2: index == 0
        # Case 3: index > length of list
        # Case 4: 0 < index <= length

        if index < 0:                   # Case 1
            return
        elif index == 0:                # Case 2
            insertInBeg(data)
            return
        else:
            temp = self.head
            i = 0
            while(temp.next and i < index - 1):
                temp = temp.next
                i += 1

            if temp.next == None:       # Case 3
                temp.next = Node(data)
            else:                       # Case 4
                newNode = Node(data)
                newNode.next = temp.next
                temp.next = newNode

    def deleteFromBeg(self):
        if self.head == None:
            print('LL is empty')
            return
        else:
            temp = self.head
            self.head = self.head.next
            del temp

    def deleteFromEnd(self):
        if self.head == None:   # no node
            print('LL is empty')
        else:
            temp = self.head
            prev = None
            while(temp.next):
                prev = temp     # save prev node so as to set second last node's next
                temp = temp.next

            if prev == None:    # single node
                temp = self.head
                del temp
                self.head = None

            else:               # multiple nodes
                del temp
                prev.next = None

    def deleteFromIndex(self, index):
        # Case 1: index < 0 or list is empty
        # Case 2: index == 0
        # Case 3: index > length of list
        # Case 4: 0 < index <= length of list

        if index < 0 or self.head == None:          # Case 1
            return
        elif index == 0:                            # Case 2
            deleteFromBeg()
        else:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
                if temp == None:
                    break

            if temp == None or temp.next == None:    # Case 3
                return

            toDelete = temp.next                     # Case 4
            next_to_next = toDelete.next
            temp.next = next_to_next
            del toDelete

    def deleteData(self, key):
        if self.head == None:
            print('LL is empty')
            return

        temp = self.head
        if (temp.next == None):     # single node
            if(temp.data == key):
                self.head == None
                del temp
            else:
                print('Key not present in LL')
        else:                       # multiple nodes
            if (temp.data == key):  # head node holds key
                self.head = temp.next
                del temp
                return

            # store prev, temp
            while(temp):
                if temp.data == key:
                    break
                prev = temp
                temp = temp.next

            if temp == None:
                print('Key not present in LL')
                return

            prev.next = temp.next
            del temp

    def printLinkedList(self):
        temp = self.head
        print()
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next


if __name__ == '__main__':
    List = LinkedList()
    List.head = Node(4)
    node2 = Node(5)
    List.head.setNext(node2)
    node3 = Node(6)
    node2.setNext(node3)
    node3.setNext(Node(9))
    List.insertAtEnd(2)
    List.printLinkedList()
    List.insertAtIndex(3, 7)
    List.printLinkedList()
    List.insertAtIndex(6, 11)
    List.printLinkedList()
    List.insertAtIndex(9, 10)
    List.printLinkedList()
    List.deleteData(4)
    List.printLinkedList()
    List.deleteFromBeg()
    List.printLinkedList()
    List.deleteFromIndex(3)
    List.printLinkedList()
