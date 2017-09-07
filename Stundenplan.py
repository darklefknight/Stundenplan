"""
Program for creating a roster (just for week-usage)

"""

import matplotlib.patches as patches
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator


class subject:  # the subjects. Each subject should have at least one event.

    def __init__(self, name: str, color: str = "blue"):
        self.name = name  # name of the subject
        self.days = []
        self.subject_events = []
        self.color = color

    def add_event(self, event_type: str, day_name: str, start_time, event_duration, day_count=1):
        self.subject_events.append(event(event_type=event_type, subject_name=self.name, begin=start_time, day=day_name))

    def events(self):
        eventlist = []
        for s in self.subject_events:
            eventlist.append(s.get_info())
        return eventlist

    def get_color(self):
        return self.color


class event():  # event of an subject

    def __init__(self, event_type: str, subject_name: str, begin, day, duration=1.5):
        self.name = subject_name
        self.event_type = event_type
        self.begin = begin
        self.duration = duration
        self.day = day

    def get_info(self):
        return [self.name, self.event_type, self.day, self.begin]

    def get_label(self):
        return self.name + "\n" + self.event_type

    def get_begin(self):
        return self.begin

    def get_duration(self):
        return self.duration

    def get_day(self):
        daylist = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
        return_day = [i for i, x in enumerate(daylist) if x == self.day]
        print("returning day", return_day)
        return return_day[0]


if __name__ == "__main__":

    # Set up the subjects
    Strahlung = subject("Strahlung", color="blue")
    Strahlung.add_event("Vorlesung", "Montag", 6.5, 1.5)
    Strahlung.add_event("Übung", "Freitag", 9, 1.5)

    Theorie = subject("Theorie", color="green")
    Theorie.add_event("Vorlesung", "Dienstag", 10, 1.5)
    Theorie.add_event("Übung", "Montag", 9, 1.5)

    MPI = subject("MPI", color="orange")
    MPI.add_event("Site Meeting", "Mittwoch", 11, 1)
    MPI.add_event("Scientific Meeting", "Donnerstag", 11, 1)

    Stundenplan = [Strahlung, Theorie, MPI]  # DO NOT FORGET TO ADD THE SUBJECT IN THIS LIST!!!

    # Setting up the Roster
    fig1 = plt.figure(num=1, figsize=(16, 9))
    ax1 = fig1.add_subplot(1, 1, 1)
    ax1.set_xlim(-0.5, 6.5)
    ax1.set_ylim(6, 18)
    xminor_locator = AutoMinorLocator(2)
    ax1.xaxis.set_minor_locator(xminor_locator)
    ymajor_locator = AutoMinorLocator(2)
    ax1.yaxis.set_minor_locator(ymajor_locator)

    ax1.xaxis.grid(which='minor', alpha=1, lw=1, color="black")
    ax1.yaxis.grid(which='both', alpha=0.5, lw=0.7, color="black")

    ax1.set_xticklabels(["", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"])

    for i, modul in enumerate(Stundenplan):
        for j, element in enumerate(modul.subject_events):
            x = element.get_day() - 0.5
            y = element.get_begin()
            ax1.add_patch(
                patches.Rectangle(
                    xy=(x, y),
                    width=(1),
                    height=(element.get_duration()),
                    facecolor=modul.get_color(),
                    alpha=0.7
                )
            )
            ax1.text(x + 0.5, y + (element.get_duration() / 2), element.get_label(),
                     verticalalignment="center",
                     horizontalalignment="center",
                     fontsize=13
                     )
