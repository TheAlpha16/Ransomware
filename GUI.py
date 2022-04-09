from tkinter import *
from tkinter.font import Font, BOLD
import time


# Initial Window Setup
window = Tk()
window.title("Piracy Warning!!!")
window.geometry("700x500")
window.minsize(760, 500)
window.maxsize(760, 500)
window.config(bg='black')


# TITLE
title = 'YOUR COMPUTER HAS BEEN LOCKED'
title_font = Font(window, size=36, weight=BOLD)
title_label = Label(window, text=title, font=title_font, foreground='red', background='black')
title_label.place(relx=0.076, rely=0.065)


# IMAGE
img = PhotoImage(file='fbi.png')
img_label = Label(window, image=img, background='black')
img_label.place(relx=0.7, rely=0.2)


# MESSAGE
message = f"""
This operating system is locked due to the violation of the federal laws of
the United States of America! (Article 1, Section 8, Clause 8; Article 202;
Article 210 of the Criminal Code of U.S.A. provides for a deprivation of
liberty for four to twelve years.)

Following violations were detected:
Your IP address was used to visit websites containing pornography.
Spam-messages with terrorist motives were also sent from your computer.
This computer lock is aimed to stop your illegal activity.

As a first time offender you are required to pay $100 USD.
Send BitCoin to the following address:

"""
msg_label = Label(window, text=message, foreground='green', background='black', font='Helvetica 16')
msg_label.place(x=25, y=100)


# ADDRESS
address = 'Qh6jHed3sh9tUIstB1sR2fG40KoPrJd3'
add_label = Label(window, text=address, foreground='black', background='white', font='Ariel 14')
add_label.place(relx=0.195, rely=0.73)

# ENTRY
entry = Entry(window, background='black', fg='white')
entry.place(relx=0.675, rely=0.6)


# BUTTON
button = Button(window, text="OK", command=window.destroy, background='black', foreground='black')
button.config(width=1, height=1)
button.place(relx=0.771, rely=0.665)


# TIMER
time_label = Label(window, text='TIME LEFT:', font='Helvetica 18 bold', foreground='red', background='black')
time_label.place(relx=0.195, rely=0.8)

hour=StringVar()
minute=StringVar()
second=StringVar()

hour.set("00")
minute.set("00")
second.set("00")


hourEntry = Entry(window, text=f'{hour}:{minute}:{second}', font='Helvetica 18 bold', foreground='red', background='black')
hourEntry.place(relx=2.4, rely=0.6)

temp = 60
hours = 0
while temp > -1:
    mins, secs = divmod(temp, 60)

    if mins > 60:
        hours, mins = divmod(mins, 60)

    hour.set("{0:2d}".format(hours))
    minute.set("{0:2d}".format(mins))
    second.set("{0:2d}".format(secs))

    window.update()
    time.sleep(1)
    temp -= 1


window.mainloop()
