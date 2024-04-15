The Erlang C formula calculates the probability (P) that a call arriving at a call center will have to wait for service. It takes into account the number of operators, the arrival rate of calls, and the average duration of calls.

- **Traffic Intensity (r)**: Ratio of the arrival rate to the service rate.
- **Utilization (ρ)**: Ratio of the traffic intensity to the number of operators.
- **Summation Term**: Represents the sum of the probabilities of having 'i' customers in the system, where 'i' ranges from 0 to 'c-1' (number of operators).
- **Probability of Delay (P)**: Probability that an arriving call will have to wait for service.

The Erlang C formula is given by:

![Erlang C Formula](https://latex.codecogs.com/png.latex?P%20%3D%20%5Cfrac%7B%5Cfrac%7Br%5Ec%7D%7Bc%21%20%5Ccdot%20%281%20-%20%5Crho%29%7D%7D%7B%5Cfrac%7Br%5Ec%7D%7Bc%21%20%5Ccdot%20%281%20-%20%5Crho%29%7D%20%2B%20%5Csum_%7Bi%3D0%7D%5E%7Bc-1%7D%20%5Cfrac%7Br%5Ei%7D%7Bi%21%7D%7D)

Where:
- P is the probability of delay.
- c is the number of operators.
- r is the traffic intensity (arrival rate / service rate).
- ρ is the utilization factor (arrival rate / (service rate * c)).
- The summation term represents the sum of the probabilities of having 'i' customers in the system.
