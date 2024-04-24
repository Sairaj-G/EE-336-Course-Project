import math

# Implementation of Erlang C formula

def erlang_c(num_operators, arrival_rate, avg_call_duration):

    if num_operators == 1:
        return arrival_rate/avg_call_duration

    rho = arrival_rate/(avg_call_duration*num_operators)
    r = arrival_rate/avg_call_duration
    sum = 0
    
    for i in range(0, num_operators):
        sum = sum + pow(r, i)/math.factorial(i)
    
    numerator = pow(r,num_operators)/(math.factorial(num_operators)*(1-rho))
    prob = numerator/(numerator + sum)

    return prob
    