class Call:
    def __init__ (self, arrival_time, duration, complete_time):
        self.arrival_time = arrival_time # time the call arrives at the telephone office
        self.duration = duration # duration of the call
        self.complete_time = complete_time # time the call is completed

        # all times w.r.t. global time
