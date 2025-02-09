# Crie duas listas encadeadas: uma contendo um ciclo e a outra sem ciclo. Certifique-se de que cada lista tenha um método
# detect_cycle que identifique se ela tem um ciclo. Chame detect_cycle em cada lista.

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

    def create_cycle(self):
        """ Cria um ciclo fazendo com que o último elemento da lista aponte de volta para a cabeça """
        if not self.head:
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = self.head

    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while True:
            try:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True
            except:
                return False

    def show_elements(self):
        if self.detect_cycle() == False:
            node = self.head
            while node is not None:
                print(node.data)
                node = node.next
        else:
            node = self.head
            while node.next is not None: 
                print(node.data)
                node = node.next
                if node == self.head:
                    break

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def main():
    ll = LinkedList()
    llc = LinkedList()

    for i in range(1, 11):
        ll.append(i)
        llc.append(i)

    llc.create_cycle()

    print(ll.detect_cycle())
    print(llc.detect_cycle())

if __name__ == '__main__':
    main()

