from simulation import simulate
from erlang import erlang_c
import matplotlib.pyplot as plt

num_calls = 1000000 # Number of calls
arrival_rate = 5 # Interarrival rate
avg_call_duration = 10 # Average call duration


simulation_results = []
theoretical_results = []

for num_operators in range(1, 11):
    simulation_results.append(simulate(num_calls, arrival_rate, avg_call_duration, num_operators))
    theoretical_results.append(erlang_c(num_operators, arrival_rate, avg_call_duration))

print(simulation_results)
print(theoretical_results)

plt.plot(range(0, 10), simulation_results, 'b-', label = "Simulation")
plt.plot(range(0, 10), theoretical_results, 'r-', label = "Theoretical") 
plt.xlabel("Number of Operators")
plt.ylabel("Probability of Waiting")
plt.legend()
plt.show()