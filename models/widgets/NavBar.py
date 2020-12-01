import tkinter as tk

class NavBar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.global_nav_button = tk.Button(self, text="Global Cases", width="20", height="3", command=self.show_global)
        self.national_nav_button = tk.Button(self, text="National Cases", width="20", height="3", command=self.show_national)

        self.global_nav_button.pack(side="left")
        self.national_nav_button.pack(side="left")

    
    def show_global(self):
        print("Showing global cases!")

    
    def show_national(self):
        self.parent.show_national_cases()
        # print(data.head(5))
        # print(data['date'])
