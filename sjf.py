import json

from time import time, sleep
import sched


class SJF:

    def invoke_Scheduler(self, process_info):
        process_info.sort(key=lambda x: x[1])
        for i in range(len(process_info)):
            s = sched.scheduler()
            event = s.enterabs(0, i, sjf.nextTask, argument=(process_info[i]),)
            s.run()

    def nextTask(self, *processInfo):
        num_of_secs = processInfo[1]
        while num_of_secs:
            num_of_secs -= 1
        print(f"p", processInfo[0], "(",
              processInfo[1], "sec)", end="->")

    def schedulingAlgo(self, processInfo):
        # sort processess based on the Burst time
        startTime = []
        endTime = []
        initialTime = 0
        # this loop is for calculating process completion time
        for i in range(len(processInfo)):
            startTime.append(initialTime)
            initialTime = initialTime + processInfo[i][1]
            completionTime = initialTime
            endTime.append(completionTime)
            processInfo[i].append(completionTime)

        turnAroundTime = SJF.calculateTurnaroundTime(self, processInfo)
        waitingTime = SJF.calculateWaitingTime(self, processInfo)
        SJF.printData(self, processInfo, turnAroundTime, waitingTime)

    # Turn Around Time ---- The time since the process entered into ready queue for execution till the process completed it’s execution
    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][2] - 0
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        return average_turnaround_time
#

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][3] - process_data[i][1]
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        return average_waiting_time
#
#

    def printData(self, process_data, average_turnaround_time, average_waiting_time):
        process_data.sort(key=lambda x: x[0])
        print("\n\nProcessID  BurstTime  CompletionTime  TurnaroundTime  WaitingTime")

        for i in range(len(process_data)):
            for j in range(len(process_data[i])):

                print(process_data[i][j], end="             ")
            print()
        print(f'\n\nAverage Turnaround Time: {average_turnaround_time}')
        print(f'Average Waiting Time: {average_waiting_time}')
        print("\n")
        process_data.sort(key=lambda x: x[1])
        # print("Order of execution of the process:")
        # for i in range(len(process_data)):
        #     print(f'P{process_data[i][0]}')


if __name__ == "__main__":
    process_data = []
    f = open('sjf.json',)
    data = json.load(f)
    for i in data['process_information']:
        processDetails = []
        processDetails.extend([i['process_id'], i['burst_time']])
        process_data.append(processDetails)
    sjf = SJF()
    sjf.invoke_Scheduler(process_data)
    sjf.schedulingAlgo(process_data)
    f.close()
