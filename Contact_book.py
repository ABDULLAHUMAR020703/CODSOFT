import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        # Labels and Entry Widgets
        self.label_name = tk.Label(root, text="Name:")
        self.entry_name = tk.Entry(root)

        self.label_phone = tk.Label(root, text="Phone:")
        self.entry_phone = tk.Entry(root)

        self.label_email = tk.Label(root, text="Email:")
        self.entry_email = tk.Entry(root)

        self.label_address = tk.Label(root, text="Address:")
        self.entry_address = tk.Entry(root)

        # Buttons
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)

        # Packing Widgets
        self.label_name.grid(row=0, column=0, padx=10, pady=5, sticky="E")
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.label_phone.grid(row=1, column=0, padx=10, pady=5, sticky="E")
        self.entry_phone.grid(row=1, column=1, padx=10, pady=5)

        self.label_email.grid(row=2, column=0, padx=10, pady=5, sticky="E")
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)

        self.label_address.grid(row=3, column=0, padx=10, pady=5, sticky="E")
        self.entry_address.grid(row=3, column=1, padx=10, pady=5)

        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=5)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=5)
        self.update_button.grid(row=7, column=0, columnspan=2, pady=5)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=5)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone are required fields.")

    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in self.contacts])
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("Contacts", "No contacts available.")

    def search_contact(self):
        search_term = self.entry_name.get()
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact['Name'].lower()]
        if found_contacts:
            contact_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in found_contacts])
            messagebox.showinfo("Search Results", contact_list)
        else:
            messagebox.showinfo("Search Results", "No matching contacts found.")

    def update_contact(self):
        search_term = self.entry_name.get()
        found_contact = next((contact for contact in self.contacts if search_term.lower() in contact['Name'].lower()), None)

        if found_contact:
            # Update contact details
            found_contact["Phone"] = self.entry_phone.get()
            found_contact["Email"] = self.entry_email.get()
            found_contact["Address"] = self.entry_address.get()
            messagebox.showinfo("Success", "Contact updated successfully!")
            self.clear_entries()
        else:
            messagebox.showinfo("Error", "Contact not found.")

    def delete_contact(self):
        search_term = self.entry_name.get()
        found_contact = next((contact for contact in self.contacts if search_term.lower() in contact['Name'].lower()), None)

        if found_contact:
            self.contacts.remove(found_contact)
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.clear_entries()
        else:
            messagebox.showinfo("Error", "Contact not found.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

# Create the main Tkinter window
root = tk.Tk()
contact_book_app = ContactBook(root)

# Run the Tkinter event loop
root.mainloop()
