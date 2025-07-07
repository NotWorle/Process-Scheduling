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