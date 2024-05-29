import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os
 
 
def generate_key(key_filename='key.key'):
   return Fernet.generate_key()
 
 
def write_key_to_file(key, filename='key.key'):
   with open(filename, 'wb') as f:
       f.write(key)
 
 
def load_key_from_file(filename='key.key'):
   if os.path.exists(filename):
       with open(filename, 'rb') as f:
           return f.read()
   else:
       raise FileNotFoundError(f"Key file '{filename}' not found.")
 
 
def encrypt_file(key, filename):
   cipher = Fernet(key)
   with open(filename, 'rb') as f:
       data = f.read()
       encrypted_data = cipher.encrypt(data)
   encrypted_filename = filename + '.encrypted'
   with open(encrypted_filename, 'wb') as f:
       f.write(encrypted_data)
   return encrypted_filename
 
 
def decrypt_file(key, encrypted_filename):
   cipher = Fernet(key)
   with open(encrypted_filename, 'rb') as f:
       encrypted_data = f.read()
       decrypted_data = cipher.decrypt(encrypted_data)
   decrypted_filename = os.path.splitext(encrypted_filename)[0]
   with open(decrypted_filename, 'wb') as f:
       f.write(decrypted_data)
   return decrypted_filename
 
 
def generate_key_handler():
   key = generate_key()
   write_key_to_file(key)
   messagebox.showinfo("Key Generated", "Key generated and saved to 'key.key'")
 
 
def encrypt_file_handler():
   try:
       key = load_key_from_file()
       filename = filedialog.askopenfilename(title="Select File to Encrypt")
       if filename:
           encrypted_filename = encrypt_file(key, filename)
           messagebox.showinfo("File Encrypted", f"File encrypted successfully.\nEncrypted file: {encrypted_filename}")
   except Exception as e:
       messagebox.showerror("Error", f"An error occurred: {e}")
 
 
def decrypt_file_handler():
   try:
       key = load_key_from_file()
       filename = filedialog.askopenfilename(title="Select File to Decrypt")
       if filename:
           decrypted_filename = decrypt_file(key, filename)
           messagebox.showinfo("File Decrypted", f"File decrypted successfully.\nDecrypted file: {decrypted_filename}")
   except Exception as e:
       messagebox.showerror("Error", f"An error occurred: {e}")
 
 
if __name__ == "__main__":
   root = tk.Tk()
   root.title("File Encryptor - The Pycodes")
   root.geometry("350x200")
   root.resizable(False,False)
 
 
   generate_key_button = tk.Button(root, text="Generate Key", command=generate_key_handler)
   generate_key_button.pack(pady=10)
 
 
   encrypt_button = tk.Button(root, text="Encrypt File", command=encrypt_file_handler)
   encrypt_button.pack(pady=5)
 
 
   decrypt_button = tk.Button(root, text="Decrypt File", command=decrypt_file_handler)
   decrypt_button.pack(pady=5)
 
 
   root.mainloop()
