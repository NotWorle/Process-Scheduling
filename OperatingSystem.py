import copy
import csv
import queue
import threading
import math
import operator
from collections import deque

stack = [] # Area of address stack
heap = []  # Area of address heap
process_register = [] # Area of address process register
text_section = [] # Area of address text section
in_out_put = [] # Area of address I/O devices

"""Program contains many components:
-Code: translate by assembly
-Data: global variables, const 
-Resource: pictures, file
-Metadata: version 
"""
class Program:
    def __init__(self, data:str):
        self.data = data


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

class Assembly:
    def __init__(self, program:Program):
        size_stack = len(stack)
        temp_stack = {}
        var, num = '', ''
        code = program.data
        ki_tu = 0

        while ki_tu < len(code):
            if code[ki_tu] == '=':
                ki_tu += 1
                while ki_tu < len(code) and code[ki_tu] != ';' :
                    num += code[ki_tu]
                    ki_tu += 1
                temp_stack[var] = int(num)
                var, num = '', ''
            else:
                var += code[ki_tu]
            ki_tu += 1
        stack.append([temp_stack])

        self.data = size_stack




"""Process Control Block be created when execute context switch, it contains address of information each process"""
class ProcessControlBlock:
    def __init__(self, pc, pr, memory, accounting, io):
        self.state = "new"
        self.pc = pc                      # Program counter
        self.pr = pr                      # Processor registers
        self.memory = memory              # chứa địa chỉ text, stack, data, heap
        self.accounting = accounting      # CPU time, priority,...
        self.io = io                      # I/O devices

    def change_state(self, state):
        if state in ["new", "running", "waiting", 'ready', 'terminated']:
            self.state = state

    def __str__(self):
        return f'\n-state: {self.state}\n-pc: {self.pc}\n-pr: {self.pr}\n-memory:{self.memory}\n-accounting: {self.accounting}\n-io: {self.io}'
"""
Multiple parts
-   The program code, also called text section
-   Current activity including program counter, processor registers
-   Stack containing temporary data Function parameters, return addresses, local variables
-   Data section containing global variables
-   Heap containing memory dynamically allocated during run time
Process contains just contain are of address
"""
class Process:
    def __init__(self, pcb:ProcessControlBlock,name:str, arrive:int, burst:int, prior:int):
        self.text_section = None
        self.stack = None
        self.data = None
        self.heap = None
        self.pcb = pcb   # Mỗi tiến trình có 1 PCB đi kèm
        self.name = name
        self.burst = burst
        self.arrive = arrive
        self.prior = prior

    def __str__(self):
        return (f'Process:\ntext_section: {self.text_section} \n'
                f'stack: {self.stack} \n'
                f'data: {self.data}\n'
                f'heap: {self.heap} \n'
                f'pcb: {self.pcb}\n'
                f'name: {self.name}\n'
                f'time: {self.burst}\n'
                f'arrive: {self.arrive}\n'
                 f'prior: {self.prior}\n')

    def __lt__(self, other):
        return self.burst < other.burst

    @staticmethod
    def save_process(pcb:ProcessControlBlock):
        ready_process.append((0,pcb))


class Dispatcher:
    def __init__(self, process:Process):
        self.process = []
        self.process.append(process)

    def add(self, process:Process):
        self.process.append(process)

    def __str__(self):
        s = ''
        for process in self.process:
            s += f'{process} \n\n'
        return s

ready_process = queue.PriorityQueue()
class CPUScheduler:
    def __init__(self):
        self.process = None


    def first_come_served(self):
        for i in Example:
            ready_process.put((i.arrive, i))

        time = 0
        while not ready_process.empty():
            process = ready_process.get()[1]
            self.process = process
            while process.arrive > time:
                print(time)
                time += 1
            print(f'{time} : {process.name}')
            time += process.burst
            self.process = None
        print(f'{time}')

    def shortest_job_first(self):
        for i in Example:
            ready_process.put((i.burst, i))

        time = 0
        while not ready_process.empty():
            process = ready_process.get()[1]
            self.process = process
            while process.arrive > time:
                print(time)
                time += 1
            print(f'{time} : {process.name}')
            time += process.burst
            self.process = None
        print(f'{time}')

    def round_robin(self):
        pass

    def priority_scheduling(self):
        pass

    def prio_round_robin(self):
        pass

    def rate_monotonic(self):
        pass

    def earliest_deadline(self):
        pass


def search_arrive(array:list, arrive):
    for i in array:
        if i.arrive == arrive:
            return i
    return False

def input_processes(namefile:str):
    array = []
    with open(namefile, 'r', encoding='utf-8') as p:
        reader = csv.reader(p)
        for row in reader:
            row = row[0].split()
            array.append(create_process(row))
    return array

def create_process(infor:list):
    pcb = ProcessControlBlock(1, 1, 1, 1, 1)

    try:
        priority = int(infor[3])
    except IndexError:
        priority = 0
    process = Process(pcb, infor[0], int(infor[1]), int(infor[2]), priority)

    return process



class Memory:
    def __init__(self, page:int, word:int, frame:int):
        self.page = page
        self.word = word
        self.frame = frame

    def logic_address(self):
        return math.log(self.page,2) + math.log(self.word,2)

    def physic_address(self):
        return math.log(self.frame,2) + math.log(self.word,2)

    @staticmethod
    def move_x_head(arr:list, x:float):
        if x in arr:
            arr.index(x)
            arr.remove(x)
            arr.insert(0, x)
        else:
            arr.pop()
            arr.insert(0, x)

    def page_fault(self, page:list, mode:str):
        time = [-1 for i in range(self.frame)]
        page_frame = [-1 for i in range(self.frame)]
        count = 0
        size = len(page)
        if mode == 'LRU': # Least Recently Used
            for i in range(size):
                if page[i] not in time:
                    index = page_frame.index(-1) if -1 in page_frame else page_frame.index(time[self.frame - 1])
                    page_frame[index] = page[i]
                    count += 1
                    self.move_x_head(time, page[i])
                else:
                    self.move_x_head(time, page[i])
                print(f'{page[i]}:  {page_frame} -- {time}')
        elif mode == 'FIFO':
            time = deque(maxlen=self.frame)
            for i in range(size):
                if page[i] not in page_frame:
                    index = page_frame.index(-1) if -1 in page_frame else page_frame.index(time.popleft())
                    page_frame[index] = page[i]
                    count += 1
                    time.append(page[i])
                print(f'{page[i]}:  {page_frame} -- {time}')
        elif mode == 'optimal':
            for i in range(size):
                if page[i] not in page_frame:
                    if -1 in page_frame:
                        index = page_frame.index(-1)
                    else:
                        best = float('-inf')
                        index = 0
                        for pag in page_frame:
                            try:
                                val = reverse_index(page, pag,end=i)
                                if val > best:
                                    best = val
                                    index = page_frame.index(pag)
                            except ValueError:
                                index = page_frame.index(pag)
                                break
                    page_frame[index] = page[i]
                    count += 1
                print(f'{page[i]}:  {page_frame}')
        return count







class MemoryAllocation:
    def __init__(self,memory:list, process:list):
        self.memory = memory
        self.process = process

    def compare_searching(self, x:float, compare:str):
        ops = {
            '>':operator.gt,
            '>=':operator.ge,
            '<':operator.lt,
            '<=':operator.le,
        }
        if compare not in ops:
            raise ValueError("Invalid comparison operator.")
        for index in range(len(self.memory)):
            if ops[compare](self.memory[index], self.process[x]):
                return index

    def operation_searching(self,x:int, operation:str, maximum:str):
        ops = {
            '-': operator.sub,
            '+': operator.add,
            '*': operator.mul,
            '/': operator.truediv,
            'max': operator.gt, # >
            'min': operator.lt, # <
        }
        if operation not in ops:
            raise ValueError("Invalid operation operator.")

        maximum_val = float('inf')
        maximum_index = -1

        for index, val in enumerate(self.memory):
            result = ops[operation](val,self.process[x])
            if result >= 0 and ops[maximum](result, maximum_val):
                maximum_val = result
                maximum_index = index
        return maximum_index

    '''
    f là first - fit
    b là best - fit
    w là worst - fit
    '''
    def allocate_memory(self, mode:str):
        if mode == 'f': # first-fit
            x = 0
            while True:
                if x >= len(self.process):
                    break
                index = self.compare_searching(x, '>=')
                if index is not None:
                    self.memory[index] -= self.process[x]
                    self.process[x] = 0
                x+=1
        elif mode == 'b': # best-fit
            x = 0
            while True:
                if x == len(self.process):
                    break
                index = self.operation_searching(x, '-','min')
                self.memory[index] -= self.process[x]
                self.process[x] = 0
                x += 1
        elif mode == 'w': # worst-fit
            x = 0
            while True:
                if x == len(self.process):
                    break
                index = self.memory.index(max(self.memory))
                if self.memory[index] >= self.process[x]:
                    self.memory[index] -= self.process[x]
                    self.process[x] = 0
                x += 1
        print(self.memory)
        print(self.process)

def reverse_index(arr:list, val:float, begin:int=None, end:int=0):
    begin = len(arr)-1 if begin is None else begin
    for i in range(begin, end, -1):
        if arr[i] == val:
            return i
    raise ValueError(f'{val} not in {arr}')


memory1 = Memory(4,1024,4)
print(memory1.logic_address())
print(memory1.physic_address())
print('----------------------------------------')
print(memory1.page_fault([1,2,4,6,8,4,3,6,4,4,3,2,5,6,7,3,2,5,6,7,1,2,3,4,5], "optimal"))

# memory2 = Memory(3,1024,3)
# print(memory2.page_fault([7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1], 'FIFO'))

# allocation = MemoryAllocation([480,450,250,300], [255,435,215,452])
# allocation.allocate_memory('w')
#
# allocation2 = MemoryAllocation([300,600,350,200,750,125], [115,500,358,200,375,320])
# allocation2.allocate_memory('w')

