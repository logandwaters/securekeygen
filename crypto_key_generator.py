# crypto_key_generator.py
# A lightweight application to generate secure keys for cryptographic operations.

import tkinter as tk
from tkinter import font
import webbrowser
import secrets

def generate_keys():
    """Generate a 32-byte hexadecimal key and a 16-byte IV."""
    key = secrets.token_hex(32)  # 32 bytes -> 64 hex characters
    iv = secrets.token_hex(16)   # 16 bytes -> 32 hex characters
    key_var.set(key)             # Update key display
    iv_var.set(iv)               # Update IV display

def copy_to_clipboard(text):
    """Copy the provided text to the clipboard."""
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()  # Keep clipboard updated

def open_github():
    """Open the developer's GitHub profile in the browser."""
    webbrowser.open("https://github.com/logandwaters")

def report_issue():
    """Open the GitHub repository's issues page."""
    webbrowser.open("https://github.com/logandwaters/crypto_key_generator/issues")

# Initialize the main window
root = tk.Tk()
root.title("SecureKeyGen - Secure Cryptographic Key Generator")
root.geometry("800x450")

# Set application icon (update path as needed)
icon_path = r"C:\Users\lwate\Documents\coding_projects\crypto_key_generator\key_pixel_art_32x32.png"
root.iconphoto(False, tk.PhotoImage(file=icon_path))

# Define custom fonts
large_font = font.Font(family="Ubuntu Mono", size=14, weight="bold")
button_font = font.Font(family="Arial", size=16, weight="bold")  # Bold font for the button
small_font = font.Font(family="Helvetica", size=10)

# Initialize key and IV variables
key_var = tk.StringVar()
iv_var = tk.StringVar()

# Add a description label
description_label = tk.Label(
    root, 
    text="Generate secure keys for cryptographic operations.", 
    font=large_font
)
description_label.pack(pady=(10, 5))

# Create and place the Generate Keys button
generate_button = tk.Button(
    root, 
    text="Generate Keys", 
    font=button_font,     
    height=1,  
    bg="lightgrey",       
    command=generate_keys
)
generate_button.pack(pady=(15, 10))

# Create a frame to center the content
frame = tk.Frame(root)
frame.pack(expand=True)

# Add Key Label and Display
key_label = tk.Label(
    frame, 
    text="32-byte Hexadecimal Key:\nA 32-byte key used for encryption and decryption.", 
    font=("Arial", 10), 
    justify="center"
)
key_label.pack(pady=5)

key_frame = tk.Frame(frame, relief="sunken", bd=2, padx=2, pady=2, width=700, height=50)
key_frame.pack(pady=5, padx=10)
key_frame.pack_propagate(False)

key_display = tk.Label(key_frame, textvariable=key_var, font=("Courier", 12), justify="center")
key_display.pack(expand=True, fill="both")

copy_key_button = tk.Button(frame, text="Copy Key", command=lambda: copy_to_clipboard(key_var.get()))
copy_key_button.pack(pady=(5, 10))

# Add IV Label and Display
iv_label = tk.Label(
    frame, 
    text="16-byte Initialization Vector (IV):\nA 16-byte vector used to ensure uniqueness.", 
    font=("Arial", 10), 
    justify="center"
)
iv_label.pack(pady=5)

iv_frame = tk.Frame(frame, relief="sunken", bd=2, padx=2, pady=2, width=700, height=50)
iv_frame.pack(pady=5, padx=10)
iv_frame.pack_propagate(False)

iv_display = tk.Label(iv_frame, textvariable=iv_var, font=("Courier", 12), justify="center")
iv_display.pack(expand=True, fill="both")

copy_iv_button = tk.Button(frame, text="Copy IV", command=lambda: copy_to_clipboard(iv_var.get()))
copy_iv_button.pack(pady=(5, 10))

# Create a bottom frame for footer links
footer_frame = tk.Frame(root)
footer_frame.pack(side="bottom", fill="x", pady=(10, 10))

# Add "Built by" label aligned to the left
built_by_label = tk.Label(
    footer_frame, 
    text="Built by: logandwaters", 
    font=small_font, 
    fg="blue", 
    cursor="hand2"
)
built_by_label.pack(side="left", padx=(10, 0))
built_by_label.bind("<Button-1>", lambda e: open_github())

# Add "Report a Problem" link aligned to the right
report_issue_label = tk.Label(
    footer_frame, 
    text="Report a Problem", 
    font=small_font, 
    fg="blue", 
    cursor="hand2"
)
report_issue_label.pack(side="right", padx=(0, 10))
report_issue_label.bind("<Button-1>", lambda e: report_issue())

# Start the Tkinter main event loop
root.mainloop()