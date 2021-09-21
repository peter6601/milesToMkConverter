from tkinter import *

window = Tk()
window.title("miles to kem convert")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


equal_label = Label(text= "is equal to")
equal_label.grid(row=1, column=0)

miles_label = Label(text= "Miles")
miles_label.grid(row=0, column=2)

km_label = Label(text= "Km")
km_label.grid(row=1, column=2)

show_label = Label(text="0")
show_label.grid(row=1, column=1)

input = Entry(width=5)
input.grid(row=0, column=1)

def click_button():
    miles = input.get()
    km = float(miles) * 1.699
    show_label.config(text=km)

button = Button(text="click", command=click_button)
button.grid(column=1, row=2)
window.mainloop()