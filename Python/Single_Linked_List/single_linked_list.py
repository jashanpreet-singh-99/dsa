class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

# insert

class SLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


    def contains(self, value) -> bool:
        s_node = self.head
        
        while s_node is not None and s_node.value != value:
            s_node = s_node.next

        if s_node is None:
            return False
        return True
    
    def delete(self, value, multi=False) -> bool:
        if self.head is None:
            return False
        
        # if self.head.value == value:
        #     if self.head is self.tail:
        #         self.head = None
        #         self.tail = None
        #     else:
        #         self.head = self.head.next
            
        #     return True
        
        s_node = self.head

        if s_node == value:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            return True

        while s_node.next is not None and s_node.next.value != value:
            s_node = s_node.next

        if s_node.next is not None:
            if s_node.next == self.tail:
                self.tail = s_node
            s_node 
            return True

        return False


def main():
    l_list = SLinkedList()

    l_list.insert(10)
    l_list.insert(20)
    l_list.insert(30)
    l_list.insert(40)
    l_list.insert(50)

    print('Check value: 30', l_list.contains(30))
    print('Check value: 70', l_list.contains(70))

if __name__ == '__main__':
    main()