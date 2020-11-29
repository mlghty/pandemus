import tkinter as tk

class NavBar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.global_nav_button = tk.Button(self, text="Global Cases", width="20", height="3")
        self.national_nav_button = tk.Button(self, text="National Cases", width="20", height="3")

        self.global_nav_button.pack(side="left")
        self.national_nav_button.pack(side="left")