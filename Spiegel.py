#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function
from tkinter import *
import tkinter.font as tkf
import time
import os



def tick():
        time2 = time.strftime('%H:%M:%S')
        date2 = time.strftime('%d.%m.%Y')
        clock.config(text=time2)
        date.config(text=date2)
        try:
                open("RAM/refresh")
                os.system("rm RAM/refresh")
                refresh()
        except:
                pass
        clock.after(200, tick)



def refresh():
        try:
                webuntisT.config(text=open("RAM/Arbeiten.txt").read())
                kalender.config(text=open("RAM/Kalender.txt").read())
                email.config(text=open("RAM/Mail.txt").read())
                news.config(text=open("RAM/RSS.txt").read())
                wetterte.config(text=open("RAM/Temperatur.txt").read())
                wetter.config(text=open("RAM/Vorhersage.txt").read())
                StundenplanT.config(text=open("RAM/Stundenplan.txt").read())

                if(open("RAM/Arbeiten.txt").read() == "\n"):
                        webuntisl.config(fg="black")
                else:
                        webuntisl.config(fg="white")
                if(open("RAM/Stundenplan.txt").read() == ""):
                        Stundenplanl.config(fg="black")
                else:
                        Stundenplanl.config(fg="white")
                if(open("RAM/Mail.txt").read() == ""):
                        emailL.config(fg="black")
                else:
                        emailL.config(fg="white")
        except:
                pass


mywin = Tk()
mywin
mywin.attributes("-fullscreen", True)
mywin.configure(background='black')



clock = Label(mywin, font=('times', 40, 'bold'), fg='white', bg='black')

date = Label(mywin, font=('times', 20, 'bold'), fg='white', bg='black')

wettert = Label(mywin, font=('times', 20, 'bold'), fg='white', bg='black', text="Wetter: ")
wetter = Label(mywin, font=('times', 10, 'bold'), fg='white', bg='black', justify=LEFT, wraplength=300)
wetterte = Label(mywin, font=('times', 20, 'bold'), fg='white', bg='black')

spacer1 = Label(mywin, font=('times', 20, 'bold'), fg='white', bg='black', text="   ")
spacer2 = Label(mywin, font=('times', 20, 'bold'), fg='white', bg='black', text="   ")
spacer3 = Label(mywin, font=('times', 20, 'bold'), fg='white', bg='black', text="   ")
spacer4 = Label(mywin, font=('times', 20, 'bold'), fg='white', bg='black', text="   ")
spacer5 = Label(mywin, font=('times', 20, 'bold'), fg='white', bg='black', text="   ")
spacer6 = Label(mywin, font=('times', 20, 'bold'), fg='white', bg='black', text="   ")

newst = Label(mywin, font=('times', 20, 'bold'), fg='white', bg='black', text="News:")
news = Label(mywin, font=('times', 10, 'bold'), fg='white', bg='black', justify=LEFT)

emailL = Label(mywin, font=('times', 20, 'bold'), fg='white', bg='black', text="E-Mails:")
email = Label(mywin, font=('times', 10, 'bold'), fg='white', bg='black', justify=LEFT, compound = LEFT)

kalenderl = Label(mywin, font=('times', 20, 'bold'), fg='white', bg='black', text="Kalender:")
kalender = Label(mywin, font=('times', 10, 'bold'), fg='white', bg='black', justify=LEFT, compound = LEFT)

webuntisl = Label(mywin, font=('times', 20, 'bold'), fg='white', bg='black', text="Arbeiten:")
webuntisT = Label(mywin, font=('times', 10, 'bold'), fg='white', bg='black', justify=LEFT, compound = LEFT)

Stundenplanl = Label(mywin, font=('times', 20, 'bold'), fg='white', bg='black', text="Stundenplan:")
StundenplanT = Label(mywin, font=('times', 10, 'bold'), fg='white', bg='black', justify=LEFT, compound = LEFT)



clock.grid(row=0, column=0, sticky=W)

date.grid(row=1, column=0, sticky=W)

spacer1.grid(row=3, column=0, sticky=W)

newst.grid(row=4, column=0, sticky=W)
news.grid(row=5, column=0, sticky=W, columnspan=3, rowspan=3)

spacer2.grid(row=8, column=0, sticky=W)

kalenderl.grid(row=9, column=0, sticky=W, columnspan=4)
kalender.grid(row=10, column=0, sticky=W, columnspan=4, rowspan=3)

spacer3.grid(row=13, column=0, sticky=W)

wettert.grid(row=14, column=0, sticky=W)
wetter.grid(row=15, column=0, sticky=W, columnspan=2)
wetterte.grid(row=15, column=2, sticky=W)

spacer4.grid(row=16, column=0, sticky=W)

emailL.grid(row=17, column=0, sticky=W, columnspan=4)
email.grid(row=18, column=0, sticky=W, columnspan=6, rowspan=6)

spacer5.grid(row=0, column=2, sticky=W, rowspan=2)

webuntisl.grid(row=0, column=3, sticky=SW)
webuntisT.grid(row=1, column=3, sticky=NW, columnspan=4, rowspan=6)

spacer6.grid(row=7, column=2, sticky=W, rowspan=2)

Stundenplanl.grid(row=7, column=3, sticky=SW)
StundenplanT.grid(row=8, column=3, sticky=NW, columnspan=4, rowspan=9)

tick()
refresh()
mywin.mainloop()
