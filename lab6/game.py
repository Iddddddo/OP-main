from tkinter import *
import time

main = Tk()
main.resizable(width = False, height = False)
main.title("Happy Helicopter :)")
main.geometry('520x700')

PL_Y = 200
sky_x=200

w = Canvas(main, width = 520, height = 700, background = "#A4B2EC", bd=0, highlightthickness=0)
w.pack()

skyimg=PhotoImage(file="C:\\Users\\Даниэль\\Documents\\Проекты\\OP-main\\lab6\\images\\sky.gif")
skyimg=skyimg.zoom(x=3, y=1)
sky=w.create_image(sky_x, 75,image=skyimg)

PlaneImg = PhotoImage(file="C:\\Users\\Даниэль\\Documents\\Проекты\\OP-main\\lab6\\images\\plane.gif")
PlaneImg = PlaneImg.subsample(x=2,y=2)
plane = w.create_image(250, PL_Y, image=PlaneImg)

def plUp(event = None):
	global PL_Y
	PL_Y -= 100
	w.coords(plane, 100, PL_Y)
	if PL_Y<0:PL_Y=0

def PlDown():
	global PL_Y
	PL_Y += 5
	if PL_Y >= 700: PL_Y = 700
	w.coords(plane, 250, PL_Y)
	main.after(20,PlDown)

def sky_drive():
	global sky_x
	sky_x-=1
	if sky_x<-130: sky_x=650
	w.coords(sky, sky_x, 75)
	main.after(20,sky_drive)

main.after(20, PlDown)
main.after(20, sky_drive)
main.bind("<space>", plUp)

main.mainloop()