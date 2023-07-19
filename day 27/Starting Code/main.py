from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24))
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="Newer Text")


#Button

def button_clicked():
    new_text = input_field.get()
    print("Button got clicked")
    my_label["text"] = new_text
    my_label.grid(column=0, row=0)


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="Button 2")
button2.grid(column=2, row=0)

# Entry
input_field = Entry(width=10)
input_field.grid(column=3, row=2)



window.mainloop()
