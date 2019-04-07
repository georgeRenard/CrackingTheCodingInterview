import sys



STACK_1 = 1
STACK_2 = 2
STACK_3 = 3



class Multistack:
    

    # Simulation of a standard array that is initialized
    def __init__(self, size):
        self.arr = [0] * size
        self.capacity = size
        self.stack_1_head = 0
        self.stack_2_head = 1
        self.stack_3_head = 2
        self.count = 0
        self.stack_1_count = 0


    def push(self, item, stack_number):

        if self.count > self.capacity:
            self.resize()

        if stack_number is None or type(stack_number) != int:
            stack_number = STACK_1

        if stack_number == STACK_1:
            # Add to stack 1
            self.arr[self.stack_1_head] = item
            self.stack_1_head += 3 
            self.stack_1_count += 1
        elif stack_number == STACK_2:
            self.arr[self.stack_2_head] = item
            self.stack_2_head += 3
            # Add to stack 2
        elif stack_number == STACK_3:
            self.arr[self.stack_3_head] = item
            self.stack_3_head += 3
            # Add to stack 3
        else:
            raise Exception("There is no stack number {0}".format(stack_number)) 

        self.count += 1
        


    def pop(self, stack_number):


        if self.count == 0:
            raise Exception("The multistack is empty!")

        if self.count < self.capacity // 3:
            self.shrink()

        if stack_number is None or type(stack_number) != int:
            stack_number = STACK_1

        if stack_number == STACK_1:
            # Remove from stack 1
            if self.stack_1_head < 0:
                self.stack_1_head = 0
                raise Exception("You cannot remove from stack number 1 since its emtpy") 
            self.stack_1_head -= 3
            self.arr[self.stack_1_head] = 0
        elif stack_number == STACK_2:
            # Remove from stack 2
            if self.stack_2_head < 0:
                self.stack_2_head = 1
                raise Exception("You cannot remove from stack number 2 since its empty")
            self.stack_2_head -= 3
            self.arr[self.stack_2_head] = 0
        elif stack_number == STACK_3:
            # Remove from stack 3
            if self.stack_3_head < 0:
                self.stack_3_head = 2
                raise Exception("You cannot remove from stack number 3 since its empty")
            self.stack_3_head -= 3
            self.arr[self.stack_3_head] = 0
        else:
            raise Exception("There is no stack number {0}".format(stack_number))

        self.count -= 1


    def resize(self):
        self.capacity *= 2
        new_arr = [0] * self.capacity
        for i in range(len(self.arr)):
            new_arr[i] = arr[i]
                
        self.arr = new_arr

    
    def shrink(self):
        self.capacity /= 2
        new_arr = [0] * self.capacity
        for i in range(len(self.arr)):
            new_arr[i] = arr[i]

        self.arr = new_arr

    def __iter__(self):
        return self.MultistackIterator(self.arr, self.stack_1_head, self.stack_1_count) 


    class MultistackIterator():

        def __init__(self, multistack, stack_head, count):
            self.arr = multistack
            self.ind = stack_head - 3
            self.count = count
            self.iter = 0

        def __next__(self):

            if self.iter < self.count:
                element = self.arr[self.ind]
                self.ind -= 3
                self.iter += 1
                return element
            else:
                raise StopIteration()
        



if __name__ == '__main__':
    args = sys.argv[1:]
    stacks = Multistack(12)
    stacks.push(5, STACK_1)
    stacks.push(6, STACK_1)
    stacks.push(5, STACK_1)
    stacks.push(1, STACK_2)
    stacks.push(2, STACK_2)
    stacks.push(3, STACK_3)
    stacks.push(7, STACK_3)
    print(stacks.arr)
    stacks.pop(STACK_2)
    print(stacks.arr)
