
import tkinter as tk

class TotalCaseTracker(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        self.title_label = tk.Label(self, text="Total Cases:", width="42", height="3")
        self.total_cases = tk.Label(self, text="000000000", width="42", height="2")
        
        self.title_label.pack()
        self.total_cases.pack()
    
    def set(self, amount):
        self.total_cases.configure(text=str(amount))