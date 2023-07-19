from tkinter import *

FONT = ("Arial", 16)


def button_clicked():
    miles = float(in_field.get())
    km = round(miles * 1.609, 2)
    res_label.config(text=f"{km}")


window = Tk()
window.title("Mile to KM Converter")
window.config(padx=10, pady=10)

# Labels
is_equal_label = Label(text="is equal to ", font=FONT)
is_equal_label.grid(column=0, row=1)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

km_label = Label(text="KM", font=FONT)
km_label.grid(column=2, row=1)

res_label = Label(text="0", font=FONT)
res_label.grid(column=1, row=1)

# Entry
in_field = Entry(width=10)
in_field.grid(column=1, row=0)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
