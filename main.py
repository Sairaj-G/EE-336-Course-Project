import random
from call_class import Call
from call_operator_class import CallOperator
from erlang import erlang_c

num_calls = 1000000 # Number of calls
arrival_rate = 5 # Interarrival rate
avg_call_duration = 10 # Average call duration
num_operators = 10 # Number of operators at the telephone exchange
curr_time = 0 # For keeping track of time

calls = []
list_operator = []

for i in range(0, num_calls):
    arrival_time = curr_time + random.expovariate(arrival_rate) # Actual arrival time
    curr_time = arrival_time # Update current time
    call_duration = random.expovariate(avg_call_duration) 
    call = Call(arrival_time, call_duration, 0) 
    calls.append(call)

for i in range(0, num_operators):
    operator = CallOperator([])
    list_operator.append(operator)

for i in range(0, num_calls):
   
    min_size = 1e7
    index = 0

    for j in range(0, num_operators):
        if len(list_operator[j].assigned_calls) > 0: # Remove completed calls
            while(len(list_operator[j].assigned_calls) and list_operator[j].assigned_calls[0].complete_time < calls[i].arrival_time):
                list_operator[j].assigned_calls.pop(0)

        if min_size >= len(list_operator[j].assigned_calls): # Find the operator with the minimum number of calls and assign the call to that operator
            index = j
            min_size = len(list_operator[j].assigned_calls)

    if len(list_operator[index].assigned_calls) > 0: # If the operator has calls, then the call will be completed after the last call is completed
        calls[i].complete_time = list_operator[j].assigned_calls[-1].complete_time + calls[i].duration
        num_waiting = num_waiting + 1
    else: # If the operator is free, then the call will be completed after the arrival time + call duration
        calls[i].complete_time = calls[i].arrival_time + calls[i].duration

    list_operator[index].assigned_calls.append(calls[i]) # Assign the call to the operator

print(num_waiting/num_calls, "Simulated") 
print(erlang_c(num_operators, arrival_rate, avg_call_duration), "Formula")