# implement a FIFO queue using only 2 stacks
# the queue should support all functions of a normal queue:
    # push -> add item to end of queue
    # peek -> return the item at front of queue
    # pop -> remove and return item from front of queue
    # empty -> returns True is queue is empty, false if item(s) are in it

class MyQueue:

    def __init__(self):
        self.q = []
        self.pop_q = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        while self.q:
            self.pop_q.append(self.q.pop())
        popped = self.pop_q.pop()
        while self.pop_q:
            self.q.append(self.pop_q.pop())
        return popped

    def peek(self) -> int:
        while self.q:
            self.pop_q.append(self.q.pop())
        popped = self.pop_q[-1]
        while self.pop_q:
            self.q.append(self.pop_q.pop())
        return popped

    def empty(self) -> bool:
        if len(self.q) > 0:
            return False
        else:
            return True

my_q = MyQueue()
my_q.push(1)
print(my_q.q) # [1]
my_q.push(2)
print(my_q.q) # [1,2]
print(my_q.peek()) # 1
print(my_q.pop()) # 1
print(my_q.q) # [2]
print(my_q.empty())
