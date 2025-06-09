from collections import deque

"""
Multiple parts
-   The program code, also called text section
-   Current activity including program counter, processor registers
-   Stack containing temporary data Function parameters, return addresses, local variables
-   Data section containing global variables
-   Heap containing memory dynamically allocated during run time
"""
class Process: #tiến trình
    def __init__(self,text_section, stack:deque, data, heap):
        self.text_section = text_section
        self.stack = stack
        self.data = data
        self.heap = heap
        self.state = "new"

    def program_count(self):
        pass

    def process_register(self):
        pass

    def change(self, state):
        state_space = ["new", "running", "waiting", 'ready', 'terminated']

        if state in state_space:
            self.state = state

class ProgramCounter:
    def __init__(self, initial_address:list):
        self.address = initial_address
        self.index = 0

    def __str__(self):
        return f'Program Counter: {self.index}: {self.address[self.index]}'

    def get_address(self):
        return self.address[self.index]

    def get_index(self):
        return self.index

    def jump(self, index):
        if index < 0 or len(self.address) <= index :
            print("Program counter index out of range")
        self.index = index




class ProcessControlBlock:
    def __init__(self, process:Process,):
        pass
if __name__ == "__main__":
    PC1 = ProgramCounter(["A=3","b=2",'print()','a = fun(c)'])
    print(PC1.get_address())
    PC1.jump(2)
    print(PC1.get_address())
