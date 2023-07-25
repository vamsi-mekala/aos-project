# importing Queue module
import queue
from inputs import process_prr


def process_wait_time(processes, quantum):
    priority = 1
    processList = []
    runtime = 0
    while(1):
        rem_bt = []
        processBatch = []
        for i in processes:

            if i[2] == priority:
                processBatch.append(i)
                rem_bt.append(i[1])
        while(1):
            done = True
            for i in range(len(processBatch)):
                if (rem_bt[i] > 0):
                    done = False
                    if (rem_bt[i] > quantum):
                        runtime += quantum
                        rem_bt[i] -= quantum
                        processList.append({
                            "P": processBatch[i][0],
                            "time": runtime
                        })
                        # print(processList);

                    else:

                        runtime += rem_bt[i]
                        processList.append({
                            "P": processBatch[i][0],
                            "time": runtime
                        })
                        rem_bt[i] = 0
            # If all processes are done
            if (done == True):
                break
        priority += 1
        if(len(processBatch) == 0):
            break
    return processList


def all_avg_time(processes, quantum):

    processList = process_wait_time(processes, quantum)

    print("\nGExecution Order of \"Priority Round Robin Scheduling\"\n")
    newprocessList = []
    for i in range(len(processList)):

        if (i != len(processList)-1 and processList[i]["P"] == processList[i+1]["P"]):
            newprocessList.append(
                {"P": processList[i]["P"], "time": processList[i]["time"] + processList[i+1]["time"]})
        else:
            newprocessList.append(
                {"P": processList[i]["P"], "time": processList[i]["time"]})
    prrList = []
    for i in range(len(newprocessList)):
        if(i != len(newprocessList)-1 and newprocessList[i]["P"] != newprocessList[i+1]["P"]):
            prrList.append(
                {"P": newprocessList[i]["P"], "time": newprocessList[i]["time"]})
        if(i == len(newprocessList)-1):
            prrList.append(
                {"P": newprocessList[i]["P"], "time": newprocessList[i]["time"]})
    for i in prrList:
        print("P{}-->({}sec)".format(i["P"], i["time"]), end=" ")


def priorityScheduling(proc, n):

    # Sort processes by priority
    proc_new = sorted(proc, key=lambda proc: proc[2],
                      reverse=False)
    quantum = 2
    all_avg_time(proc_new, quantum)


if __name__ == "__main__":

    proc = process_prr
    n = len(proc)
    print("\nProcess"+"\t\t"+"Priority"+"\t"+"Burst Time")
    for i in range(len(proc)):
        print(str(proc[i][0])+"\t\t" +
              str(proc[i][2])+"\t\t" +
              str(proc[i][1]))
    priorityScheduling(proc, n)
