from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pw():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_let = [choice(letters) for _ in range(randint(8, 10))]
    password_sym = [choice(symbols) for _ in range(randint(2, 4))]
    password_num = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_let + password_sym + password_num

    shuffle(password_list)

    password = "".join(password_list)
    entry_pw.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def password_add():

    website = entry_website.get().lower()
    uname = entry_uname.get()
    pw = entry_pw.get()
    new_data = {
        website: {
            "email": uname,
            "password": pw
        }
    }

    if len(website) < 1 or len(uname) < 1 or len(pw) < 1:
        messagebox.askquestion(title="Oops", message="Please don't leave any fields emtpy!")
    else:
            try:
                with open("data.json", 'r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                entry_website.delete(0, END)
                entry_pw.delete(0, END)


def find_password():
    website = entry_website.get().lower()
    try:
        with open("data.json", 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="File not found", message="No entries available!")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showerror(title=website, message=f"No details found")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

cv = Canvas(width=200, height=200)
pw_image = PhotoImage(file="logo.png")
cv.create_image(100, 100, image=pw_image)
cv.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
entry_website = Entry(width=18)
entry_website.focus()
entry_website.grid(row=1, column=1)

label_uname = Label(text="Email/Username:")
label_uname.grid(row=2, column=0)
entry_uname = Entry(width=42)
entry_uname.insert(0, "dummy@email.com")
entry_uname.grid(row=2, column=1, columnspan=2)

label_pw = Label(text="Password:")
label_pw.grid(row=3, column=0)
entry_pw = Entry(width=18)
entry_pw.grid(row=3, column=1)
button_pw = Button(text="Generate Password", width=18, command=gen_pw)
button_pw.grid(row=3, column=2)

button_add = Button(text="Add", width=42, command=password_add)
button_add.grid(row=4, column=1, columnspan=2)

button_search = Button(text="Search", width=18, command=find_password)
button_search.grid(row=1, column=2)
window.mainloop()
