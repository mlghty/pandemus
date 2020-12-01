import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

style.use("fivethirtyeight")

class TrackingChart(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.figure = Figure(figsize=(5,5), dpi=100)
        self.x = self.figure.add_subplot(111)
        self.x.plot([1,2,3], [5,6,7])

        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack()

