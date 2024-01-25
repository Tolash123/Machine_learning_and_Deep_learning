import time
from tkinter import *
from tkinter import messagebox

### Create Object Interface
clockWindow = Tk()
clockWindow.geometry("500x500")
clockWindow.title("Countdown Timer")
clockWindow.configure(background="brown")

hourString = StringVar()
minString = StringVar()
secString = StringVar()

### Setting Strings to initial values
hourString.set("00")
minString.set("00")
secString.set("00")

#Getting Data from User
hourTextbox = Entry(clockWindow, width=3, font=("Calibri", 20, ""), textvariable=hourString)
minTextbox = Entry(clockWindow, width=3, font=("Calibri", 20, ""), textvariable=minString)
secTextbox = Entry(clockWindow, width=3, font=("Calibri", 20, ""), textvariable=secString)

##Centring TextBox
hourTextbox.place(x=170, y=180)
minTextbox.place(x=220, y=180)
secTextbox.place(x=270, y=180)

#Function that powers Timer
def runTimer():
    try:
        clockTime = int(hourString.get())*3600 + int(minString.get())*60 + int(secString.get())
    except:
        print("Incorrect Values")

    while (clockTime > -1):
        totalMins, totalSecs = divmod(clockTime, 60)

        totalHours = 0
        if (totalMins > 60):
            totalHours, totalMins = divmod(totalMins, 60)

        hourString.set("{0:2d}".format(totalHours))
        minString.set("{0:2d}".format(totalMins))
        secString.set("{0:2d}".format(totalSecs))

        ###Updating the Interface
        clockWindow.update()
        time.sleep(1)

        ###Updating User with Timer
        if(clockTime == 0):
            messagebox.showinfo("", "Time Up!")

        clockTime -= 1

setTimer = Button(clockWindow, text="Set Time", bd="5", command=runTimer)
setTimer.place(relx=0.5, rely=0.5, anchor=CENTER)

###Loop ClockWindow
clockWindow.mainloop()
