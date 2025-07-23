import tkinter as tk
from tkinter import messagebox
from ContactManager import ContactManager

class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.resizable(False, False)
        self.root.geometry("400x200")
        
        tk.Label(root, text="Name:").grid(
            row=0, column=0, padx=10, pady=5, sticky='e')
        
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.grid(
            row=0, column=1, padx=10, pady=5, columnspan=3, sticky='we')
        self.name_entry.focus()
        
        tk.Label(root, text="Number:").grid(
            row=1, column=0, padx=10, pady=5, sticky='e')
        
        self.number_entry = tk.Entry(root, width=30)
        self.number_entry.grid(
            row=1, column=1, padx=10, pady=5, columnspan=3, sticky='we')
        
        buttons = [
            ("Create", self.create),
            ("Read", self.read),
            ("Update", self.update),
            ("Delete", self.delete)
        ]
        
        for i, (text, command) in enumerate(buttons):
            tk.Button(
                root, 
                text=text, 
                width=10,
                command=command
            ).grid(row=3, column=i, padx=5, pady=20)
    
    def get_inputs(self):
        name = self.name_entry.get().strip()
        number = self.number_entry.get().strip()
        return name, number
    
    def clear_number(self):
        self.number_entry.delete(0, tk.END)
    
    def create(self):
        name, number = self.get_inputs()
        if not name:
            messagebox.showwarning("Invalid input", "Name is required")
            return
        if not number:
            messagebox.showwarning("Invalid input", "Number is required")
            return
        
        try:
            number = int(number)
            success, message = ContactManager.create_contact(name, number)
            if success:
                messagebox.showinfo("Success", message)
                self.name_entry.delete(0, tk.END)
                self.number_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", message)
        except ValueError:
            messagebox.showerror("Error", "Number must be an integer")
    
    def read(self):
        name, _ = self.get_inputs()
        if not name:
            messagebox.showwarning("Invalid input", "Name is required")
            return
        
        number, error = ContactManager.find_contact(name)
        if error:
            messagebox.showinfo("Information", error)
            self.clear_number()
        elif number:
            self.clear_number()
            self.number_entry.insert(0, number)
            messagebox.showinfo("Success", "Contact found")
        else:
            self.clear_number()
            messagebox.showinfo("Information", "Contact not found")
    
    def update(self):
        name, number = self.get_inputs()
        if not name:
            messagebox.showwarning("Invalid input", "Name is required")
            return
        if not number:
            messagebox.showwarning("Invalid input", "Number is required")
            return
        
        try:
            number = int(number)
            success, message = ContactManager.update_contact(name, number)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showwarning("Warning", message)
        except ValueError:
            messagebox.showerror("Error", "Number must be an integer")
    
    def delete(self):
        name, _ = self.get_inputs()
        if not name:
            messagebox.showwarning("Invalid input", "Name is required")
            return
        
        success, message = ContactManager.delete_contact(name)
        if success:
            messagebox.showinfo("Success", message)
            self.name_entry.delete(0, tk.END)
            self.clear_number()
        else:
            messagebox.showwarning("Warning", message)