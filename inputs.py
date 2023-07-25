
process_prr = [[1, 4, 3],
               [2, 5, 2],
               [3, 8, 2],
               [4, 7, 1],
               [5, 3, 3]]


#SJTF   (P,BT,AT)
# proc = [[1, 8, 0],
#         [2, 4, 1],
#         [3, 9, 2],
#         [4, 5, 3]]

# Input for Priority Round Robin Scheduling
#              (P,BT,Priority)

# Input for First Come First Serve Scheduling
processes_fcfs = [1, 2, 3]
burst_time_fcfs = [24, 3, 3]

# Input for Priority Scheduling
#                     (P,BT,P)
# processes_priority = [[1,10,3],
#                       [2,1,1],
#                       [3,2,4],
#                       [4,1,5],
#                       [5,5,2]]

# Input for Round Robin Scheduling
process_rrb = [1, 2, 3]
burst_time_rrb = [24, 3, 3]

# Input for Shortest Job First Scheduling ([process],[AT],[BT])
ain_sjf = [[1, 2, 3, 4],
           [0, 1, 2, 3],
           [6, 8, 7, 3]]

for i in range(3):
    ain_sjf.append([0]*len(ain_sjf[1]))
