import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from cryptography.fernet import Fernet
from stegano import lsb
import pyperclip

# Functions from Code 1
def hide_text_in_image():
    input_image_path = input_image_entry.get()
    output_image_path = output_image_entry.get()
    secret_text = secret_text_entry.get()
    encryption_key = encryption_key_entry.get()

    cipher_suite = Fernet(encryption_key.encode())
    encrypted_text = cipher_suite.encrypt(secret_text.encode())

    try:
        secret_image = lsb.hide(input_image_path, encrypted_text.decode())
        secret_image.save(output_image_path)
        messagebox.showinfo("Success", "Text hidden successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def extract_text_from_image():
    input_image_path = input_image_entry.get()
    decryption_key = decryption_key_entry.get()

    try:
        secret_image = lsb.reveal(input_image_path)
        cipher_suite = Fernet(decryption_key.encode())
        decrypted_text = cipher_suite.decrypt(secret_image.encode()).decode()
        extracted_text_label.config(text=f"Hidden Text: {decrypted_text}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def browse_input_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
    input_image_entry.delete(0, tk.END)
    input_image_entry.insert(0, file_path)

def browse_output_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    output_image_entry.delete(0, tk.END)
    output_image_entry.insert(0, file_path)

def clear_input_fields():
    input_image_entry.delete(0, tk.END)
    output_image_entry.delete(0, tk.END)
    secret_text_entry.delete(0, tk.END)
    encryption_key_entry.delete(0, tk.END)
    decryption_key_entry.delete(0, tk.END)
    extracted_text_label.config(text="Hidden Text:")

# Function from Code 2
def generate_key():
    key = Fernet.generate_key()
    url_safe_key = key.decode('utf-8')
    print("Generated 32-byte URL-safe base64-encoded key:", url_safe_key)
    messagebox.showinfo("Key Generated", "Generated 32-byte URL-safe base64-encoded key:\n" + url_safe_key)
    
    # Copy key to clipboard
    pyperclip.copy(url_safe_key)

# Create the main application window
app = tk.Tk()
app.title("Steganography with Encryption/Decryption")

style = ttk.Style()
style.configure('TButton', font=('Arial', 12), foreground='black')

frame = ttk.Frame(app)
frame.grid(row=0, column=0, padx=20, pady=20)

input_image_label = ttk.Label(frame, text="Input Image Path:")
input_image_entry = ttk.Entry(frame)
browse_input_button = ttk.Button(frame, text="Browse", command=browse_input_image)
output_image_label = ttk.Label(frame, text="Output Image Path:")
output_image_entry = ttk.Entry(frame)
browse_output_button = ttk.Button(frame, text="Browse", command=browse_output_image)
secret_text_label = ttk.Label(frame, text="Secret Text:")
secret_text_entry = ttk.Entry(frame)
encryption_key_label = ttk.Label(frame, text="Encryption Key:")
encryption_key_entry = ttk.Entry(frame, show='*')
hide_button = ttk.Button(frame, text="Hide Text", command=hide_text_in_image)
decryption_key_label = ttk.Label(frame, text="Decryption Key:")
decryption_key_entry = ttk.Entry(frame, show='*')
extract_button = ttk.Button(frame, text="Extract Text", command=extract_text_from_image)
extracted_text_label = ttk.Label(frame, text="Hidden Text:")
refresh_button = ttk.Button(frame, text="Refresh", command=clear_input_fields)
generate_key_button = ttk.Button(frame, text="Generate Key", command=generate_key)

input_image_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
input_image_entry.grid(row=0, column=1, padx=10, pady=5)
browse_input_button.grid(row=0, column=2, padx=10, pady=5)
output_image_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
output_image_entry.grid(row=1, column=1, padx=10, pady=5)
browse_output_button.grid(row=1, column=2, padx=10, pady=5)
secret_text_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
secret_text_entry.grid(row=2, column=1, padx=10, pady=5)
encryption_key_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')
encryption_key_entry.grid(row=3, column=1, padx=10, pady=5)
hide_button.grid(row=4, column=1, padx=10, pady=10)
decryption_key_label.grid(row=5, column=0, padx=10, pady=5, sticky='w')
decryption_key_entry.grid(row=5, column=1, padx=10, pady=5)
extract_button.grid(row=6, column=1, padx=10, pady=10)
extracted_text_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky='w')
refresh_button.grid(row=8, column=1, padx=10, pady=10)
generate_key_button.grid(row=9, column=1, padx=10, pady=10)

# Start the GUI main loop
app.mainloop()


