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
    def __init__(self, initial_address):
        self.address = [initial_address]
        self.index = 0

    def __str__(self):
        return f'Program Counter: {self.index}: {self.address[index]}'

    def get_address(self):
        return self.address[self.index]

    def get_index(self):
        return self.index

    def jump(self, index=None):
        if index is None:
            self.index = self.index + 1
        else:
            self.index = index




class ProcessControlBlock:
    def __init__(self, process:Process,):
        pass
if __name__ == "__main__":
    PC1 = ProgramCounter(["0x99","0x100"])
    print(PC1.get_address())
