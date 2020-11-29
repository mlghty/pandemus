
import tkinter as tk

class CaseList():
    def __init__(self, _):
        self.scrollbar = tk.Scrollbar(self)
        self.listbox = tk.Listbox(self, yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill=tk.Y)
        self.listbox.pack(side='left', fill="both")

        for l in range(20):
            self.listbox.insert(tk.END, "Line number " + str(l+1))

    

class RegionCaseList(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.title_label = tk.Label(self, text="Cases by State:", width="42", height="3")
        self.case_list = CaseList(self)

        self.title_label.pack()
        self.case_list.pack(side="left")
