import random
from call_class import Call
from queue_class import Queue


num_calls = 10000
arrival_rate = 5
avg_call_time = 3
curr_time = 0
num_lines = 3
line_num = 0

calls = []
line_queue = []

for i in range(0, num_calls):
    arrival_time = curr_time + random.expovariate(1/arrival_rate)
    curr_time = arrival_time
    call_duration = random.expovariate(1/avg_call_time)
    call = Call(arrival_time, call_duration) 
    calls.append(call)


for i in range(0, num_lines):
    queue = Queue(0)
    line_queue.append(queue)


for i in range(0, num_calls):
    call_arrival_time = calls[i].arrival_time
    call_duration_time = calls[i].call_duration