from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

def find_password():
    website = entry_website.get()
    try:
        with open("data.json", mode="r") as file1:
            file_info = json.load(file1)
    except FileNotFoundError:
        messagebox.showerror(title="json error", message="no data file found")
    else:
        if website in file_info:
            file_data_email = file_info[website]["email"]
            file_data_password = file_info[website]["password"]
            messagebox.showinfo(title="website info", message=f"Your data\nWebsite: {website}\nEmail: {file_data_email}\nPassword: {file_data_password}")
        else:
            messagebox.showerror(title="json error", message="no details for the website exists")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    entry_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for i in range(randint(8, 12))]
    password_symbols = [choice(symbols) for i in range(randint(2, 6))]
    password_numbers = [choice(numbers) for i in range(randint(2, 6))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    entries_list = [entry_website, entry_username, entry_password]
    data_list = [new_data.get() for new_data in entries_list]
    new_data = {
        data_list[0]: {
            "email": data_list[1],
            "password": data_list[2]
        }
    }
    if data_list[0] != "" and data_list[2] != "":
        message_is_ok = messagebox.askokcancel(title="are you sure?", message=f"Your credentials\nWebsite: {data_list[0]}\nEmail: {data_list[1]}\nPassword: {data_list[2]}")
        if message_is_ok:
            try:
                with open("data.json", mode="r") as file:
                    loaded = json.load(file)
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                loaded.update(new_data)
                with open("data.json", mode="w") as file:
                    json.dump(loaded, file, indent=4)
            finally:
                for entry in entries_list:
                    if entry != entry_username:
                        entry.delete(0, END)
    else:
        messagebox.showwarning(title="empty fields", message="please input your credentials!")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

lock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=190, highlightthickness=0)
canvas.create_image(100, 95, image=lock_image)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:", font=("Arial", 8, "bold"))
label_website.grid(column=0, row=1)
label_email = Label(text="Email/Username:", font=("Arial", 8, "bold"))
label_email.grid(column=0, row=2)
label_email = Label(text="Password:", font=("Arial", 8, "bold"))
label_email.grid(column=0, row=3)

entry_website = Entry(width=32)
entry_website.grid(column=1, row=1)
entry_website.focus()
entry_username = Entry(width=48)
entry_username.grid(column=1, row=2, columnspan=2)
entry_username.insert(END, "yevgene.kornienko@gmail.com")
entry_password = Entry(width=32)
entry_password.grid(column=1, row=3)

button_search = Button(text="Search", font=("Arial", 8, "bold"), command=find_password, width=12)
button_search.grid(column=2, row=1)
button_generate = Button(text="Generate", font=("Arial", 8, "bold"), command=generate_password, width=12)
button_generate.grid(column=2, row=3)
button_add = Button(text="Add", font=("Arial", 8, "bold"), command=add_password, width=41)
button_add.grid(column=1, row=4, columnspan=2)


window.mainloop()
