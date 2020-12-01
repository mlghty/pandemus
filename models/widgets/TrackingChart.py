import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

style.use("ggplot")

class TrackingChart(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.figure = Figure(figsize=(5,4))
        self.subplot = self.figure.add_subplot()
        
        self.subplot.set_ylabel('Date')
        self.subplot.set_xlabel('Cases')
        self.subplot.set_xlim(10**6)
        self.subplot.set_ylim(20210000)

        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack()

    def plot(self, xList, yList):
        self.subplot.clear()
        self.subplot.plot(xList, yList)