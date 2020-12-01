
import tkinter as tk
import time

class CaseList(tk.Listbox):
    def __init__(self, parent, *args, **kwargs):
        
        self.listbox = tk.Listbox(parent)
        self.scrollbar = tk.Scrollbar(parent)

        self.scrollbar.pack(side="right", fill="both")

        for l in range(20):
            self.listbox.insert(tk.END, "Line number " + str(l+1))

        self.listbox.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

class RegionCaseList(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.title_label = tk.Label(self, text="Cases by State:", width="42", height="3")
        self.case_list = CaseList(self)

        self.title_label.pack()
        self.case_list.listbox.pack(side="left")