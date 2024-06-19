import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk

# Function to save passwords to a file
def save_passwords():
    with open("passwords.txt", "w") as file:
        for (website, username), password in passwords.items():
            file.write(f"{website},{username},{password}\n")

# Function to load passwords from a file
def load_passwords():
    try:
        with open("passwords.txt", "r") as file:
            for line in file:
                website, username, password = line.strip().split(",")
                passwords[(website, username)] = password
    except FileNotFoundError:
        pass

# Function to add a new password
def add_password():
    website = simpledialog.askstring("Add Password", "Enter website:")
    if not website:
        messagebox.showerror("Error", "Website cannot be empty!")
        return
    username = simpledialog.askstring("Add Password", f"Enter username for {website}:")
    if not username:
        messagebox.showerror("Error", "Username cannot be empty!")
        return
    password = simpledialog.askstring("Add Password", "Enter password:")
    if not password:
        messagebox.showerror("Error", "Password cannot be empty!")
        return
    passwords[(website, username)] = password
    save_passwords()
    messagebox.showinfo("Success", "Password added successfully!")

# Function to remove an existing password
def remove_password():
    website = simpledialog.askstring("Remove Password", "Enter website:")
    if not website:
        messagebox.showerror("Error", "Website cannot be empty!")
        return
    username = simpledialog.askstring("Remove Password", f"Enter username for {website}:")
    if (website, username) in passwords:
        del passwords[(website, username)]
        save_passwords()
        messagebox.showinfo("Success", "Password removed successfully!")
    else:
        messagebox.showerror("Error", "Password not found!")

# Function to view all saved passwords
def view_passwords():
    key = simpledialog.askstring("View Passwords", "Enter security key:")
    if key == "VIDHI24":
        if passwords:
            password_info = "Saved Passwords:\n\n"
            for (website, username), password in passwords.items():
                password_info += f"Website: {website}\nUsername: {username}\nPassword: {password}\n\n"
            messagebox.showinfo("Password List", password_info)
        else:
            messagebox.showinfo("Password List", "No passwords saved yet.")
    else:
        messagebox.showerror("Error", "Invalid security key!")

# Function to edit an existing password
def edit_password():
    website = simpledialog.askstring("Edit Password", "Enter website:")
    if not website:
        messagebox.showerror("Error", "Website cannot be empty!")
        return
    username = simpledialog.askstring("Edit Password", f"Enter username for {website}:")
    if (website, username) in passwords:
        new_password = simpledialog.askstring("Edit Password", "Enter new password:")
        if not new_password:
            messagebox.showerror("Error", "Password cannot be empty!")
            return
        passwords[(website, username)] = new_password
        save_passwords()
        messagebox.showinfo("Success", "Password updated successfully!")
    else:
        messagebox.showerror("Error", "Password not found!")

# Initialize the passwords dictionary and load existing passwords
passwords = {}
load_passwords()

# Set up the main application window
root = tk.Tk()
root.title("Your Personal Password Manager")
root.geometry("500x450")
root.configure(bg="light blue")

# Add a heading label
heading_label = tk.Label(root, text="Password Manager", font=("Helvetica", 20), bg="light blue", fg="black")
heading_label.pack(pady=10)

# Add an image to the window
try:
    img = Image.open("password_image.png")
    img = img.resize((300, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(root, image=img)
    panel.image = img
    panel.pack(pady=10)
except FileNotFoundError:
    messagebox.showerror("Error", "Image file not found!")

# Add buttons for different functionalities
button_frame = tk.Frame(root, bg="light blue")
button_frame.pack(pady=20)

add_button = tk.Button(button_frame, text="Add Password", command=add_password)
add_button.grid(row=0, column=0, padx=10, pady=5)

remove_button = tk.Button(button_frame, text="Remove Password", command=remove_password)
remove_button.grid(row=0, column=1, padx=10, pady=5)

edit_button = tk.Button(button_frame, text="Edit Password", command=edit_password)
edit_button.grid(row=1, column=0, padx=10, pady=5)

view_button = tk.Button(button_frame, text="View Passwords", command=view_passwords)
view_button.grid(row=1, column=1, padx=10, pady=5)

# Start the Tkinter event loop
root.mainloop()
