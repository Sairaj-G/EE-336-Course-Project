import math

# Implementation of Erlang C formula

def erlang_c(num_operators, arrival_rate, avg_call_duration):

    lam = arrival_rate 
    meu = avg_call_duration
    c = num_operators

    rho = lam/(meu*c)
    r = lam/meu

    sum = 0

    for i in range(0, c):
        sum = sum + pow(r, i)/math.factorial(i)
    
    numerator = pow(r,c)/(math.factorial(c)*(1-rho))
    prob = numerator/(numerator + sum)

    return prob
    