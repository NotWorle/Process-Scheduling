# Process-Scheduling
Mô phỏng lại các lý thuyết về lập trình CPU dưới dạng các giải thuật, các trúc dữ liệu trên ngôn ngữ python 3

    program_counter = ProgramCounter([])
    cpu_scheduler = CPUScheduler()

    '''Example for how a program be bornt'''
    # game = Program('a=2;b=3;c=4;obs=223')
    # assembly = Assembly(game)
    # pcb0 = ProcessControlBlock([0,3],[0,4], assembly.data,[0,1], [0,5])
    # process0 = Process(pcb0,'1', 0,4,4)
    '''Example for how a program be bornt'''

    Example = input_processes(namefile='input.csv')
    #
    cpu_scheduler.first_come_served()
    print('----------------------')
    # cpu_scheduler.shortest_job_first()