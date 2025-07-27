import random
import string
import json
import tkinter as tk
from tkinter import messagebox, filedialog

#CORE LOGIC 
class Cipher:
    def __init__(self, seed=42):
        self.seed = seed
        self.char = list(" " + string.punctuation + string.digits + string.ascii_letters)
        self.key = self.generate_key()
        print(f"Generated key: {self.key}")  
        
    def generate_key(self):
        key = self.char.copy()
        random.seed(self.seed)  # Fixed seed for consistent key
        random.shuffle(key)
        return key
    
    def super_encrypt(self, text, shift=3):
       # Double encryption: substitution + Caesar shift

        # First layer: substitution cipher
        sub_encrypted = "".join([self.key[self.char.index(c)] for c in text])

        # Second layer: Caesar shift
        caesar_encrypted = "".join([
            self.char[(self.char.index(c) + shift) % len(self.char)] 
            for c in sub_encrypted
        ])
        return caesar_encrypted
    
    def super_decrypt(self, text, shift=3):
     #Reverse the double encryption with error handling

     try:
        # First reverse Caesar shift (shift LEFT)
        caesar_decrypted = "".join([
            self.char[(self.char.index(c) - shift) % len(self.char)]
            for c in text
        ])
        
        # Then reverse substitution
        plain_text = "".join([
            self.char[self.key.index(c)] 
            for c in caesar_decrypted
            if c in self.key  # Skip unknown characters
        ])
        return plain_text
     except Exception as e:
        print(f"Decryption error: {e}")
        return "Decryption failed - invalid input"

#GUI CLASS
class CipherApp:
    def __init__(self, root):
        self.cipher = Cipher()
        self.root = root
        self.root.title("IS Project - Super Cipher")
        
        # Key management
        self.key_label = tk.Label(root, text="Encryption Key:")
        self.key_label.pack()
        
        self.key_entry = tk.Entry(root, width=50)
        self.key_entry.insert(0, "SHH!! This is a secret key!")
        self.key_entry.config(state='disabled')
        self.key_entry.pack()
        
        # Text input
        self.input_label = tk.Label(root, text="Enter Text:")
        self.input_label.pack()
        
        self.input_text = tk.Text(root, height=5, width=50)
        self.input_text.pack()
        
        # Buttons
        self.encrypt_btn = tk.Button(root, text="Encrypt", command=self.encrypt)
        self.encrypt_btn.pack(side=tk.LEFT, padx=5)
        
        self.decrypt_btn = tk.Button(root, text="Decrypt", command=self.decrypt)
        self.decrypt_btn.pack(side=tk.LEFT, padx=5)
        
        self.clear_btn = tk.Button(root, text="Clear", command=self.clear)
        self.clear_btn.pack(side=tk.RIGHT, padx=5)
        
        # Output
        self.output_label = tk.Label(root, text="Result:")
        self.output_label.pack()
        
        self.output_text = tk.Text(root, height=5, width=50)
        self.output_text.pack()
        
    def encrypt(self):
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter text to encrypt!")
            return
        encrypted = self.cipher.super_encrypt(text)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, encrypted)
        
    def decrypt(self):
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter text to decrypt!")
            return
        try:
            decrypted = self.cipher.super_decrypt(text)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, decrypted)
        except:
            messagebox.showerror("Error", "Decryption failed! Invalid cipher text.")
        
    def clear(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)

#MAIN
if __name__ == "__main__":
    root = tk.Tk()
    app = CipherApp(root)
    root.mainloop()