class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
            print()

    def search(self, data):
        if self.head is None:
            print("LinkedList is empty")
        else:
            current = self.head
            while current:
                if current.data == data:
                    print("Data {} found in LinkedList".format(data))
                    return
                current = current.next
            print("Data {} not found in LinkedList".format(data))

    def remove(self, data):
        if self.head is None:
            print("LinkedList is empty")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            print("Data {} not found in LinkedList".format(data))
        else:
            prev.next = current.next
            print("Data {} removed from LinkedList".format(data))

    def update(self, old_data, new_data):
        if self.head is None:
            print("LinkedList is empty")
        else:
            current = self.head
            while current:
                if current.data == old_data:
                    current.data = new_data
                    print("Data {} updated to {} in LinkedList".format(old_data, new_data))
                    return
                current = current.next
            print("Data {} not found in LinkedList".format(old_data))

def main():
    linked_list = LinkedList()

    while 1:
            print("""
1: display linked list
2: insert an item
3: remove an item
4: change an item
5: search an item
6: exit
""")
            n = input()
            if n == '1':
                linked_list.display()
            elif n == '2':
                newItem = input("new item: ")
                linked_list.insert(newItem)
            elif n == '3':
                delItem = input("item you want to remove: ")
                linked_list.remove(delItem)
            elif n == '4':
                old = input("item you want to change: ")
                new = input("new item: ")
                linked_list.update(old, new)
            elif n == '5':
                item = input("item you want to search: ")
                linked_list.search(item)
            elif n == '6':
                return

main()
