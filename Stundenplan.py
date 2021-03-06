"""
Program for creating a roster (just for week-usage)

"""

import matplotlib.patches as mpatches
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator


class Subject:  # the subjects. Each subject should have at least one event.

    def __init__(self, name: str, color: str = "blue"):
        self.name = name  # name of the subject
        self.days = []
        self.subject_events = []
        self.color = color

    def add_event(self, event_type: str, day_name: str, start_time, event_duration):
        self.subject_events.append(Event(event_type=event_type, subject_name=self.name, begin=start_time, day=day_name,
                                         duration=event_duration))

    def events(self):
        eventlist = []
        for s in self.subject_events:
            eventlist.append(s.get_info())
        return eventlist

    def get_color(self):
        return self.color


class Event:  # event of an subject

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
    Frei = Subject(" ",color="grey")
    Frei.add_event(" ","Samstag",6,12)
    Frei.add_event(" ", "Sonntag", 6, 12)

    MPI = Subject("MPI", color="orange")
    MPI.add_event("Site Meeting", "Mittwoch", 11, 1)
    # MPI.add_event("Scientific Meeting", "Donnerstag", 11, 1)
    MPI.add_event("Arbeiten", "Montag", 7, 7)
    # MPI.add_event("Arbeiten", "Dienstag", 13, 1)
    # MPI.add_event("Arbeiten", "Donnerstag", 7, 3)


    Strahlung = Subject("Strahlung - A", color="cyan")
    Strahlung.add_event("Vorlesung", "Donnerstag", 12.25, 1.5)

    Theorie = Subject("Theorie - A", color="red")
    Theorie.add_event("Vorlesung", "Dienstag", 10.25, 1.5)
    Theorie.add_event("Vorlesung", "Donnerstag", 10.25, 1.5)
    Theorie.add_event("Übung", "Mittwoch", 9, 2)

    Modellierung = Subject("Modellierung - A", color="red")
    Modellierung.add_event("Vorlesung", "Freitag",10.25,1.5)
    Modellierung.add_event("Übung", "Mittwoch", 13, 2)

    SE1 = Subject("Software Entwicklung", color = "cyan")
    SE1.add_event("Vorlesung","Mittwoch",14.25,1.5)
    SE1.add_event("Übung", "Montag", 9, 3)

    HL = Subject("HochleistungsRech.", color="yellow")
    HL.add_event("Vorlesung","Dienstag",14,2)
    HL.add_event("Vorlesung", "Donnerstag", 12, 2)

    BigData = Subject("BigData", color ="#798EF6" )
    BigData.add_event("Project","Montag",16.25,1.5)

    RemoteSensing = Subject("Remote Sensing - A", color="yellow")
    RemoteSensing.add_event("Vorlesung", "Dienstag", 12.5, 1.5)

    DataAssimilation = Subject("Data Assimilation", color="cyan")
    DataAssimilation.add_event("Vorlesung", "Freitag", 12.25, 1.5)

    METRAS = Subject("METRAS - A", color="yellow")
    METRAS.add_event("Vorlesung", "Freitag", 8.25, 1.5)

    BDA = Subject("Big Data Analytics", color="lime")
    BDA.add_event("Vorlesung +\n Übung", "Freitag", 12.25, 3.25)

    ModellEval = Subject("Modell Evaluation", color="cyan")
    ModellEval.add_event("Vorlesung", "Montag", 12.5, 1.5)

    Chemie = Subject("Chemie", color="cyan")
    Chemie.add_event("Vorlesung", "Dienstag", 8.5, 1.5)

    Stundenplan = [Frei, MPI, Strahlung, Theorie, Modellierung, RemoteSensing, METRAS, BDA, ModellEval,
                   Chemie]  # DO NOT FORGET TO ADD THE SUBJECT IN THIS LIST!!!


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
                    width=1,
                    height=(element.get_duration()),
                    facecolor=modul.get_color(),
                    alpha=0.7
                )
            )
            ax1.text(x + 0.5, y + (element.get_duration() / 2), element.get_label(),
                     verticalalignment="center",
                     horizontalalignment="center",
                     fontsize=10
                     )
            red_patch = mpatches.Patch(color='red', label='Pflicht')
            cyan_patch = mpatches.Patch(color='cyan', label="Vertiefung")
            lime_patch = mpatches.Patch(color='lime', label="Ergänzung")
            yellow_patch = mpatches.Patch(color='yellow', label="Wahlfach")
            orange_patch = mpatches.Patch(color='orange', label="MPI")

            plt.legend(handles=[red_patch, cyan_patch, lime_patch, yellow_patch, orange_patch], loc="upper right",
                       fontsize=12)

    plt.gca().invert_yaxis()
    fig1.show()
    plt.savefig("C:/Users/darkl/Desktop/Stundeplan.png", dpi=400)
