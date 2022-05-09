
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self,data):
        # node = Node(data,None)
        if self.head is None:
            self.head = Node(data,None)
            return
        iterator = self.head
        while iterator.next:
            iterator= iterator.next
        iterator.next =Node(data,None)

    def get_length(self):
        count = 0
        iterator = self.head
        while iterator:
            iterator = iterator.next
            count += 1
        return count

    def insert_at_index(self,index,data):

        if index < 0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)

        if index == self.get_length():
            self.insert_at_end(data)

        iterator = self.head
        count = 0
        while iterator:
            if count == index-1:
                iterator.next = Node(data, iterator.next)
                break
            iterator = iterator.next
            count += 1

    def insert_from_list(self,data):
        for x in data:
            self.insert_at_beginning(x)
        return

    def remove_from_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        count = 0
        iterator = self.head
        while iterator:
            if count == index-1:
                iterator.next = iterator.next.next
                break
            iterator = iterator.next
            count += 1

    def replace_at_index(self, index, data):
        if index < 0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = Node(data,self.head.next)

        if index == self.get_length()-1:
            iterator = self.head
            count = 0
            while iterator:
                if count == self.get_length()-2:
                    iterator.next = Node(data,None)
                    break
                iterator = iterator.next
                count += 1

        iterator = self.head
        count = 0
        while iterator:
            if count == index-1:
                iterator.next = Node(data, iterator.next.next)
                break
            iterator = iterator.next
            count += 1

    def insert_after_value(self,data_after,data_to_insert):
         iterator = self.head

         while iterator.next:
             if iterator.data == data_after:
                iterator.next = Node(data_to_insert, iterator.next)
                break
             iterator = iterator.next

    def remove_by_value(self,data_to_remove):
        if self.head is None:
            print("Linked list is empty, value not found")
            return
        if self.head.data == data_to_remove:
            self.head = self.head.next

        iterator = self.head
        while iterator.next:
            if iterator.next.data == data_to_remove:
                iterator.next = iterator.next.next
                break
            iterator = iterator.next


    def print(self):
        if self.head is None:
            print("The LinkedList is empty")
        iterator = self.head
        list_values = ''
        while iterator:
            list_values += f'{str(iterator.data)} --->'
            iterator = iterator.next
        print(list_values)

if __name__ == '__main__':
    ll = LinkedList()

    ll.insert_from_list(["apples","bananas","carrots","grapes"])
    ll.print()

    # ll.remove_from_index(1)
    # ll.print()

    ll.insert_at_end('Avocados')
    ll.print()

    print(f'The length of the linkedlist is {ll.get_length()}')

    ll.insert_at_index(1, "mangoes")
    print(f'The length of the linkedlist is {ll.get_length()}')
    ll.print()

    ll.replace_at_index(4, "pears")
    print(f'The length of the linkedlist is {ll.get_length()}')
    ll.print()

    ll.insert_after_value("grapes","Vanilla")
    print(f'The length of the linkedlist is {ll.get_length()}')
    ll.print()

    ll.remove_by_value("grapes")
    print(f'The length of the linkedlist is {ll.get_length()}')
    ll.print()