from simulation import simulate_round_robin, simulate_shortest_queue
from erlang import erlang_c
import matplotlib.pyplot as plt

num_calls = 1000 # Number of calls
arrival_rate = 5 # Interarrival rate
avg_call_duration = 10 # Average call duration


simulation_results_sq = [1]
simulation_results_rr = [1]
theoretical_results = [1]

for num_operators in range(1, 6):
    simulation_results_sq.append(simulate_shortest_queue(num_calls, arrival_rate, avg_call_duration, num_operators))
    simulation_results_rr.append(simulate_round_robin(num_calls, arrival_rate, avg_call_duration, num_operators))
    theoretical_results.append(erlang_c(num_operators, arrival_rate, avg_call_duration))

print(simulation_results_sq)
print(simulation_results_rr)
print(theoretical_results)

plt.plot(range(0, 6), simulation_results_sq, 'b-', label = "Simulation Shortest Queue")
plt.plot(range(0, 6), simulation_results_rr, 'g-', label = "Simulation Round Robin")
plt.plot(range(0, 6), theoretical_results, 'r-', label = "Theoretical") 
plt.xlabel("Number of Operators")
plt.ylabel("Probability of Waiting")
plt.legend()
plt.show()