# Crie uma lista encadeada contendo os números de 1 a 100. Em seguida, exiba cada nó da lista.

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def show_elements(self):
        if not self.head:
            print("Empty")
            return

        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def main():
    ll = LinkedList()
    for i in range(1, 101):
        ll.append(i)
    ll.show_elements()

if __name__ == '__main__':
    main()
