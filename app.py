import tkinter as tk
from tkinter import ttk

class ErlangCSimulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Erlang C Simulation")
        self.root.configure(bg="#f9f9f9")  # Set background color
        
        # Variables for sliders
        self.servers = tk.IntVar()
        self.arrival_rate = tk.DoubleVar()
        self.service_rate = tk.DoubleVar()
        
        # Set default values
        self.servers.set(1)
        self.arrival_rate.set(0.5)
        self.service_rate.set(0.5)
        
        # Frame to contain widgets
        self.frame = ttk.Frame(self.root, padding="30", style="App.TFrame")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Label and entry for number of servers
        ttk.Label(self.frame, text="Number of Servers:", font=("Segoe UI", 14), background="#f9f9f9").grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
        self.servers_entry = ttk.Entry(self.frame, textvariable=self.servers, font=("Segoe UI", 14))
        self.servers_entry.grid(row=0, column=1, sticky=tk.W)
        
        # Slider for arrival rate
        ttk.Label(self.frame, text="Arrival Rate:", font=("Segoe UI", 14), background="#f9f9f9").grid(row=1, column=0, sticky=tk.W, pady=(10, 10))
        self.arrival_rate_slider = ttk.Scale(self.frame, from_=0.1, to=10, orient=tk.HORIZONTAL, variable=self.arrival_rate, length=400)
        self.arrival_rate_slider.grid(row=1, column=1, sticky=tk.W)
        self.arrival_rate_slider_label = ttk.Label(self.frame, textvariable=self.arrival_rate, font=("Segoe UI", 14), background="#f9f9f9")
        self.arrival_rate_slider_label.grid(row=1, column=2, sticky=tk.W, padx=(10, 0))
        
        # Slider for service rate
        ttk.Label(self.frame, text="Service Rate:", font=("Segoe UI", 14), background="#f9f9f9").grid(row=2, column=0, sticky=tk.W, pady=(10, 10))
        self.service_rate_slider = ttk.Scale(self.frame, from_=0.1, to=10, orient=tk.HORIZONTAL, variable=self.service_rate, length=400)
        self.service_rate_slider.grid(row=2, column=1, sticky=tk.W)
        self.service_rate_slider_label = ttk.Label(self.frame, textvariable=self.service_rate, font=("Segoe UI", 14), background="#f9f9f9")
        self.service_rate_slider_label.grid(row=2, column=2, sticky=tk.W, padx=(10, 0))
        
        # Button to start simulation
        self.simulate_button = ttk.Button(self.frame, text="Simulate", command=self.start_simulation, style="Accent.TButton")
        self.simulate_button.grid(row=3, columnspan=3, pady=(20, 0))
        
        # Set row and column weights to make components expand
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        
        # Define style
        self.style = ttk.Style()
        self.style.configure("App.TFrame", background="#f9f9f9")
        self.style.map("TButton", background=[('active', '#007bff')], foreground=[('active', '#f9f9f9')])
        self.style.configure("Accent.TButton", foreground="#f9f9f9", background="#007bff", font=("Segoe UI", 14), padding=10)
        self.style.map("Accent.TButton", background=[("active", "#0056b3")])

    def start_simulation(self):
        # You can put your simulation logic here
        num_servers = self.servers.get()
        arrival_rate = self.arrival_rate.get()
        service_rate = self.service_rate.get()
        print("Starting simulation with:")
        print("Number of Servers:", num_servers)
        print("Arrival Rate:", arrival_rate)
        print("Service Rate:", service_rate)

def main():
    root = tk.Tk()
    app = ErlangCSimulationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
