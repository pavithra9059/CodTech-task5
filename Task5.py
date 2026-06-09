import tkinter as tk
from tkinter import messagebox

# ---------------- Window ----------------
root = tk.Tk()
root.title("📇 Contact Manager - Pink Theme")
root.geometry("750x650")
root.configure(bg="#FFC0CB")   

contacts = []


# ---------------- Add Contact ----------------
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning("Warning", "Name and Phone required!")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    update_list()
    clear_fields()


# ---------------- Clear Fields ----------------
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


# ---------------- Update List ----------------
def update_list(data=None):
    listbox.delete(0, tk.END)

    show = data if data else contacts

    for c in show:
        listbox.insert(
            tk.END,
            f"👤 {c['name']} | 📞 {c['phone']}"
        )


# ---------------- Search ----------------
def search_contact():
    q = search_entry.get().lower()

    result = [
        c for c in contacts
        if q in c["name"].lower() or q in c["phone"]
    ]

    update_list(result)


# ---------------- Delete ----------------
def delete_contact():
    try:
        i = listbox.curselection()[0]
        contacts.pop(i)
        update_list()

    except:
        messagebox.showwarning("Warning", "Select contact")


# ---------------- Load Contact ----------------
def load_contact(event):
    try:
        i = listbox.curselection()[0]
        c = contacts[i]

        clear_fields()

        name_entry.insert(0, c["name"])
        phone_entry.insert(0, c["phone"])
        email_entry.insert(0, c["email"])
        address_entry.insert(0, c["address"])

    except:
        pass


# ---------------- Update Contact ----------------
def update_contact():
    try:
        i = listbox.curselection()[0]

        contacts[i] = {
            "name": name_entry.get(),
            "phone": phone_entry.get(),
            "email": email_entry.get(),
            "address": address_entry.get()
        }

        update_list()
        clear_fields()

    except:
        messagebox.showwarning("Warning", "Select contact")


# ---------------- TITLE ----------------
title = tk.Label(
    root,
    text="📇 CONTACT MANAGER",
    font=("Segoe UI", 22, "bold"),
    bg="#FFC0CB",
    fg="#8B004B"   # dark pink text
)
title.pack(pady=10)


# ---------------- INPUT FRAME ----------------
frame = tk.Frame(root, bg="#FFC0CB")
frame.pack(pady=10)


def label(text):
    return tk.Label(
        frame,
        text=text,
        font=("Verdana", 11, "bold"),
        bg="#FFC0CB",
        fg="#5A0033"
    )


label("Name").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(frame, font=("Arial", 12), width=30)
name_entry.grid(row=0, column=1, pady=5)

label("Phone").grid(row=1, column=0, sticky="w")
phone_entry = tk.Entry(frame, font=("Arial", 12), width=30)
phone_entry.grid(row=1, column=1, pady=5)

label("Email").grid(row=2, column=0, sticky="w")
email_entry = tk.Entry(frame, font=("Arial", 12), width=30)
email_entry.grid(row=2, column=1, pady=5)

label("Address").grid(row=3, column=0, sticky="w")
address_entry = tk.Entry(frame, font=("Arial", 12), width=30)
address_entry.grid(row=3, column=1, pady=5)


# ---------------- BUTTONS ----------------
btn_frame = tk.Frame(root, bg="#FFC0CB")
btn_frame.pack(pady=10)


def btn(color):
    return {
        "font": ("Verdana", 11, "bold"),
        "fg": "white",
        "bg": color,
        "bd": 0,
        "width": 12,
        "cursor": "hand2"
    }


tk.Button(btn_frame, text="➕ Add", command=add_contact, **btn("#FF4D6D")).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="✏️ Update", command=update_contact, **btn("#C9184A")).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="🗑 Delete", command=delete_contact, **btn("#FF006E")).grid(row=0, column=2, padx=5)


# ---------------- SEARCH ----------------
search_frame = tk.Frame(root, bg="#FFC0CB")
search_frame.pack(pady=10)

search_entry = tk.Entry(search_frame, font=("Arial", 12), width=25)
search_entry.grid(row=0, column=0, padx=5)

tk.Button(
    search_frame,
    text="🔍 Search",
    font=("Verdana", 11, "bold"),
    bg="#FFB3C6",
    fg="#5A0033",
    command=search_contact
).grid(row=0, column=1)


# ---------------- LISTBOX ----------------
listbox = tk.Listbox(
    root,
    width=60,
    height=12,
    font=("Consolas", 12),
    bg="#FFF0F5",
    fg="#3A0033",
    selectbackground="#FF69B4"
)

listbox.pack(pady=15)

listbox.bind("<<ListboxSelect>>", load_contact)


# ---------------- RUN ----------------
root.mainloop()
