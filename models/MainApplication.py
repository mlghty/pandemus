from datetime import date
import tkinter as tk

from .widgets.NavBar import NavBar
from .widgets.TotalCaseTracker import TotalCaseTracker
from .widgets.RegionCaseList import RegionCaseList
from .widgets.TrackingChart import TrackingChart

from .database.Databases import GlobalDataBase
from .database.CovidTracker import CovidTracker

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.winfo_toplevel().title("COVID-19 Case Tracker")

        self.nav_bar = NavBar(self)
        self.total_case_tracker = TotalCaseTracker(self, borderwidth=2, relief="ridge")
        self.region_case_list = RegionCaseList(self, borderwidth=2, relief="ridge")

        self.tracking_chart = TrackingChart(self, borderwidth=2, relief="ridge")

        self.nav_bar.grid(column=0, columnspan=2, row=0)
        self.total_case_tracker.grid(column=0, row=1)
        self.region_case_list.grid(column=0, row=2)

        self.tracking_chart.grid(column=3, row=1, rowspan=2)
 
        # self.global_database = GlobalDataBase('global_database.db')
        self.covid_tracker = CovidTracker()

    def show_national_cases(self):
        national_data = self.covid_tracker.get_national_data().head(5)
        self.total_case_tracker.set(national_data['positive'][0])
        self.tracking_chart.plot(national_data['positive'].tolist(), national_data['date'].tolist())
        