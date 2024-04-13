import random
from call_class import Call
from call_operator_class import CallOperator
from erlang import erlang_c


num_calls = 1000000
arrival_rate = 5
avg_call_time = 10
curr_time = 0
num_lines = 10
line_num = 0
num_waiting = 0

calls = []
list_operator = []

for i in range(0, num_calls):
    arrival_time = curr_time + random.expovariate(arrival_rate)
    curr_time = arrival_time
    call_duration = random.expovariate(avg_call_time)
    call = Call(arrival_time, call_duration, 0) 
    calls.append(call)


for i in range(0, num_lines):
    operator = CallOperator([])
    list_operator.append(operator)


for i in range(0, num_calls):
   
    min_size = 1e7
    index = 0

    for j in range(0, num_lines):
        if len(list_operator[j].assigned_calls) > 0:
            while(len(list_operator[j].assigned_calls) and list_operator[j].assigned_calls[0].complete_time < calls[i].arrival_time):
                list_operator[j].assigned_calls.pop(0)

        if min_size >= len(list_operator[j].assigned_calls):
            index = j
            min_size = len(list_operator[j].assigned_calls)

   

    if len(list_operator[index].assigned_calls) > 0:
        calls[i].complete_time = list_operator[j].assigned_calls[-1].complete_time + calls[i].duration
        num_waiting = num_waiting + 1
    else:
        calls[i].complete_time = calls[i].arrival_time + calls[i].duration

    list_operator[index].assigned_calls.append(calls[i])



   
    

print(num_waiting/num_calls, "Simulated")
print(erlang_c(num_lines, arrival_rate, avg_call_time), "Formula")