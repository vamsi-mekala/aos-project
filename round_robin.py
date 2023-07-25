import json


class RoundRobin:

    def processData(self, process_data):
        time_quantum = 4
        RoundRobin.schedulingProcess(self, process_data, time_quantum)

    def schedulingProcess(self, process_data, time_quantum):
        start_time = []
        exit_time = []
        executed_process = []
        ready_queue = []
        s_time = 0
        print("The order in which processes executed completely:")
        while 1:
            temp = []
            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][3] == 0:
                    present = 0
                    if len(ready_queue) != 0:
                        for k in range(len(ready_queue)):
                            if process_data[i][0] == ready_queue[k][0]:
                                present = 1
                    '''
                    The above if loop checks that the next process is not a part of ready_queue
                    '''
                    if present == 0:
                        temp.extend([process_data[i][0], process_data[i]
                                    [1], process_data[i][2], process_data[i][4]])
                        ready_queue.append(temp)
                        temp = []
                    '''
                    The above if loop adds a process to the read_queue only if it is not already present in it
                    '''
                    if len(ready_queue) != 0 and len(executed_process) != 0:
                        for k in range(len(ready_queue)):
                            if ready_queue[k][0] == executed_process[len(executed_process) - 1]:
                                ready_queue.insert(
                                    (len(ready_queue) - 1), ready_queue.pop(k))
                    '''
                    The above if loop makes sure that the recently executed process is appended at the end of ready_queue
                    '''
            if len(ready_queue) == 0:
                break
            if len(ready_queue) != 0:
                if ready_queue[0][2] > time_quantum:
                    '''
                    If process has remaining burst time greater than the time slice, it will execute for a time period equal to time slice and then switch
                    '''
                    start_time.append(s_time)
                    s_time = s_time + time_quantum
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            break
                    process_data[j][2] = process_data[j][2] - time_quantum
                    ready_queue.pop(0)
                elif ready_queue[0][2] <= time_quantum:
                    '''
                    If a process has a remaining burst time less than or equal to time slice, it will complete its execution
                    '''
                    start_time.append(s_time)
                    s_time = s_time + ready_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])

                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            print("Process:", process_data[j][0])
                            break
                    process_data[j][2] = 0
                    process_data[j][3] = 1
                    process_data[j].append(e_time)
                    ready_queue.pop(0)
        t_time = RoundRobin.calculateTurnaroundTime(self, process_data)
        w_time = RoundRobin.calculateWaitingTime(self, process_data)
        RoundRobin.printData(self, process_data, t_time,
                             w_time, executed_process, time_quantum)

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            '''
            turnaround_time = completion_time - arrival_time
            '''
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        '''
        average_turnaround_time = total_turnaround_time / no_of_processes
        '''
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][4]
            '''
            waiting_time = turnaround_time - burst_time
            '''
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        '''
        average_waiting_time = total_waiting_time / no_of_processes
        '''
        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time, executed_process, time_quantum):
        process_data.sort(key=lambda x: x[0])
        '''
        Sort processes according to the Process ID
        '''
        for column in process_data:
            del column[1], column[2]
        print(
            "Process_ID  Arrival_Time  Burst_Time  Completion_Time  Turnaround_Time  Waiting_Time")
        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                print(process_data[i][j], end="\t\t")
            print()
        print(f'\n\nAverage Turnaround Time: {average_turnaround_time}')
        print(f'Average Waiting Time: {average_waiting_time}')
        # print(f'Execution order: {executed_process}')
        print("Order of Execution:", end=" ")
        print("->".join(str(item) for item in executed_process))
        print("")


if __name__ == "__main__":
    process_data = []
    f = open('rr.json',)
    data = json.load(f)
    for i in data['process_information']:
        processDetails = []
        processDetails.extend(
            [i['process_id'], 0, i['burst_time'], 0, i['burst_time']])
        process_data.append(processDetails)
    rr = RoundRobin()
    rr.processData(process_data)
    f.close()
