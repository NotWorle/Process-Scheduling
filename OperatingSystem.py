from collections import deque
import heapq

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


"""Process Control Block be created when execute context switch, it contains address of information each process"""
class ProcessControlBlock:
    def __init__(self, pc:ProgramCounter, pr, memory, accounting, io):
        self.state = "new"
        self.pc = pc                      # Program counter
        self.pr = pr                      # Processor registers
        self.memory = memory              # chứa địa chỉ text, stack, data, heap
        self.accounting = accounting      # CPU time, priority,...
        self.io = io                      # I/O devices

    def change_state(self, state):
        if state in ["new", "running", "waiting", 'ready', 'terminated']:
            self.state = state

"""
Multiple parts
-   The program code, also called text section
-   Current activity including program counter, processor registers
-   Stack containing temporary data Function parameters, return addresses, local variables
-   Data section containing global variables
-   Heap containing memory dynamically allocated during run time
Process contains just contain 
"""
wait = deque()
ready = deque()
class Process:
    def __init__(self, text_section, stack: deque, data, heap, pcb: ProcessControlBlock):
        self.text_section = text_section
        self.stack = stack
        self.data = data
        self.heap = heap
        self.pcb = pcb   # Mỗi tiến trình có 1 PCB đi kèm

    def add_program(self,program):
        pass

    @staticmethod
    def load_process(pcb:ProcessControlBlock):
        ready.append(pcb)

if __name__ == "__main__":
    # PC1 = ProgramCounter(["A=3","b=2",'print()','a = fun(c)'])
    # print(PC1.get_address())
    # PC1.jump(2)
    # print(PC1.get_address())
