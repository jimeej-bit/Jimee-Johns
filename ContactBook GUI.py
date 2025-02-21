import tkinter as tk
from tkinter import messagebox

# Function to add a contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if not name or not phone or not email:
        messagebox.showwarning("Input Error", "Please fill out all fields")
        return

    contact = f"Name: {name}, Phone: {phone}, Email: {email}"
    contacts.append(contact)
    contacts_listbox.insert(tk.END, contact)

    # Clear the entry fields after adding the contact
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Function to delete a selected contact
def delete_contact():
    try:
        selected_contact = contacts_listbox.curselection()
        contacts_listbox.delete(selected_contact)
        contacts.pop(selected_contact[0])  # Remove from the contacts list
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a contact to delete")

# Function to clear all contacts
def clear_all_contacts():
    contacts_listbox.delete(0, tk.END)
    contacts.clear()

# Function to search for a contact
def search_contact():
    search_term = search_entry.get().lower()
    found = False

    # Clear the listbox
    contacts_listbox.delete(0, tk.END)

    # Search through the contacts
    for contact in contacts:
        if search_term in contact.lower():
            contacts_listbox.insert(tk.END, contact)
            found = True

    if not found:
        messagebox.showinfo("Search Result", "No matching contacts found.")

# Create the main window
root = tk.Tk()
root.title("Contact Book with Search")
root.geometry("500x500")
root.config(bg="lightblue")  # Background color for the window

# Create labels and entry fields for Name, Phone, and Email
name_label = tk.Label(root, text="Name:", font=("Arial", 12), bg="lightblue")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(root, width=30, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=10, pady=5)

phone_label = tk.Label(root, text="Phone:", font=("Arial", 12), bg="lightblue")
phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
phone_entry = tk.Entry(root, width=30, font=("Arial", 12))
phone_entry.grid(row=1, column=1, padx=10, pady=5)

email_label = tk.Label(root, text="Email:", font=("Arial", 12), bg="lightblue")
email_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
email_entry = tk.Entry(root, width=30, font=("Arial", 12))
email_entry.grid(row=2, column=1, padx=10, pady=5)

# Create buttons to add, delete, clear, and search contacts
add_button = tk.Button(root, text="Add Contact", command=add_contact, bg="lightgreen", font=("Arial", 12), width=15)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, bg="salmon", font=("Arial", 12), width=15)
delete_button.grid(row=4, column=0, columnspan=2, pady=5)

clear_button = tk.Button(root, text="Clear All Contacts", command=clear_all_contacts, bg="orange", font=("Arial", 12), width=15)
clear_button.grid(row=5, column=0, columnspan=2, pady=5)

# Search feature
search_label = tk.Label(root, text="Search Contact:", font=("Arial", 12), bg="lightblue")
search_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
search_entry = tk.Entry(root, width=30, font=("Arial", 12))
search_entry.grid(row=6, column=1, padx=10, pady=5)
search_button = tk.Button(root, text="Search", command=search_contact, bg="lightyellow", font=("Arial", 12), width=15)
search_button.grid(row=7, column=0, columnspan=2, pady=5)

# Listbox to display contacts with custom colors for each contact
contacts_listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 12), bg="white", selectmode=tk.SINGLE)
contacts_listbox.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# List to store contacts
contacts = []

# Run the application
root.mainloop()
