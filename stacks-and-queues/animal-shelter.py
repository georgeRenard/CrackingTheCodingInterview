import sys


def problem():
    """
        Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
        out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
        or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
        that type). They cannot select which specific animal they would like. Create the data structures to
        maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
        and dequeueCat. You may use the built-in Linked list data structure. 
    """
    pass 


class Cat:

    def __init__(self, name):
        self.name = name



    def __repr__(self):
        return "Cat(Name=\"{0}\")".format(self.name)


class Dog:

    def __init__(self, name):
        self.name = name


    def __repr__(self):
        return "Dog(Name=\"{0}\")".format(self.name)


# This data structure is more of a bidirectional acyclic graph than a linked list
class AnimalShelter:


    def __init__(self):
        self.cat_head = None
        self.dog_head = None
        self.cat_tail = None
        self.dog_tail = None
        self.head = None
        self.tail = None
        self.count = 0


    def enqueue(self, item):
        
        new_node = self.Node(item)

        if isinstance(item, Dog):

            if self.dog_head is None and self.dog_tail is None:
                self.dog_head = new_node 
                self.dog_tail = self.dog_head
            else:
                self.dog_tail.next_of_kind = new_node
                new_node.prev_of_kind = self.dog_tail
                self.dog_tail = new_node 

        elif isinstance(item, Cat):

            if self.cat_head is None and self.cat_tail is None:
                self.cat_head = new_node
                self.cat_tail = self.cat_head
            else:
                self.cat_tail.next_of_kind = new_node
                new_node.prev_of_kind = self.dog_tail
                self.cat_tail = new_node

        else:
            raise Exception("The animal must be either a cat or a dog")

           
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = self.head
            return

        self.tail.next_node = new_node
        new_node.prev_node = self.tail
        self.tail = new_node
        self.count += 1
              
            
         
    def dequeueAny(self):


        if self.count == 0:
            raise Exception("You cannot remove an animal from an emtpy shelter")
 
        element = self.head.item
        nxt = self.head.next_node
        nxt.prev_node = None
        self.head = nxt

        if isinstance(element, Dog):
            nxt_dog = self.dog_head.next_of_kind

            if nxt_dog is not None:
                nxt_dog.prev_of_kind = None

            self.dog_head = nxt_dog
        elif isinstance(element, Cat):
            nxt_cat = self.cat_head.next_of_kind

            if nxt_cat is not None:
                nxt_cat.prev_of_kind = None

            self.cat_head = nxt_cat
            
        self.count -= 1

        return element



    
    def dequeueCat(self):

        element = self.cat_head.item
        nxt_cat = self.cat_head.next_of_kind

        if nxt_cat is not None:
            nxt_cat.prev_of_kind = None

        prev = self.cat_head.prev_node
        nxt = self.cat_head.next_node
            
        if prev is not None:
            prev.next_node = nxt

        if nxt is not None:
            nxt.prev_node = prev

        if self.head == self.cat_head:
            self.head == nxt

        self.cat_head = nxt_cat

        self.count -= 1

        return element


    def dequeueDog(self):

        element = self.dog_head.item
        nxt_dog = self.dog_head.next_of_kind

        if nxt_dog is not None:
            nxt_dog.prev_of_kind = None

        prev = self.dog_head.prev_node
        nxt = self.dog_head.next_node
            
        if prev is not None:
            prev.next_node = nxt

        if nxt is not None:
            nxt.prev_node = prev

        if self.head == self.dog_head:
            self.head = nxt

        self.dog_head = nxt_dog

        self.count -= 1

        return element


    class Node:

        def __init__(self, item, next_node = None, prev_node = None):
            self.item = item
            self.next_node = next_node
            self.prev_node = prev_node
            self.next_of_kind = None
            self.prev_of_kind = None


        def __repr__(self):
            return "Node Object - Value: {0}".format(self.item)




if __name__ == '__main__':
    args = sys.argv[1:]
    shelter = AnimalShelter()

    shelter.enqueue(Dog("Dog1"))
    shelter.enqueue(Dog("Dog2"))
    shelter.enqueue(Dog("Dog3"))
    shelter.enqueue(Cat("Cat1"))
    shelter.enqueue(Dog("Dog4"))
    shelter.enqueue(Cat("Cat2"))
    shelter.enqueue(Cat("Cat3"))
    shelter.enqueue(Dog("Dog5"))
    shelter.enqueue(Cat("Cat4"))

    print(shelter.dequeueCat())
    print(shelter.dequeueAny())
    print(shelter.dequeueDog())
    print(shelter.dequeueCat())
    print(shelter.dequeueAny())
    print(shelter.dequeueAny())
    print(shelter.dequeueAny())
