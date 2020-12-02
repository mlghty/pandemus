import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import requests # changed

from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# changed
response = requests.get("https://api.covidtracking.com/v1/us/daily.json")
data = response.json()

style.use("ggplot")

# changed
def date():
    dates = []
    count = 0 
    for y in data:
        date = y['date']
        if count == 7:
            break
        else:
            dates.append(str(date))
            count +=1
    dates.reverse()
    return dates
            
def case():
    cases = []
    count1 = 0  
    for x in data:
        case = x['positive']
        if count1 == 7:
            break
        else:
            cases.append(case)
            count1 +=1
    cases.reverse()
    return cases

# changed

class TrackingChart(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.figure = Figure(figsize=(6,5))
        self.subplot = self.figure.add_subplot()
        self.subplot.set_ylabel('Cases')
        self.subplot.set_xlabel('Date')
        self.subplot.plot(date(), case())
        #self.subplot.set_xlim(10**6)
        #self.subplot.set_ylim(20210000)

        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack()

    def plot(self, xList, yList):
        self.subplot.clear()
        #self.subplot.plot(date(), case())