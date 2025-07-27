from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os

root = Tk()
root.geometry("1000x700")
root.title("Check N Pay")
root.resizable(False, False)

# Reset function
def Reset():
    # Clear all entry fields
    NikeMercurial.set('')
    NikePhantom.set('')
    NikeTiempo.set('')
    PumaFuture.set('')
    PumaKing.set('')
    AdidasNemeziz.set('')
    AdidasF50.set('')
    AdidasPredator.set('')

    # Reset total, tax, and discount to zero
    Total.set('')
    Tax.set('')
    Discount.set('')

# Variables to store quantity, total, tax, and discount
NikeMercurial = StringVar()
NikePhantom = StringVar()
NikeTiempo = StringVar()
PumaFuture = StringVar()
PumaKing = StringVar()
AdidasNemeziz = StringVar()
AdidasF50 = StringVar()
AdidasPredator = StringVar()
Total = StringVar()
Tax = StringVar()
Discount = StringVar()

# Tax rate and discount rate
tax_rate = 0.13  # 13% tax
discount_rate = 0.15  # 15% discount

# Function to calculate total, tax, and discount
def calculate_total():
    # Get quantities from entry fields
    try:
        a1 = int(NikeMercurial.get())
    except ValueError:
        a1 = 0
    try:
        a2 = int(NikePhantom.get())
    except ValueError:
        a2 = 0
    try:
        a3 = int(NikeTiempo.get())
    except ValueError:
        a3 = 0
    try:
        a4 = int(PumaFuture.get())
    except ValueError:
        a4 = 0
    try:
        a5 = int(PumaKing.get())
    except ValueError:
        a5 = 0
    try:
        a6 = int(AdidasNemeziz.get())
    except ValueError:
        a6 = 0
    try:
        a7 = int(AdidasF50.get())
    except ValueError:
        a7 = 0
    try:
        a8 = int(AdidasPredator.get())
    except ValueError:
        a8 = 0

    # Calculate subtotal
    subtotal = (15000 * a1) + (22000 * a2) + (19000 * a3) + (20500 * a4) + (20200 * a5) + (28100 * a6) + (17500 * a7) + (10200 * a8)

    # Calculate tax and discount
    tax = subtotal * tax_rate

    # Condition of Discount
    if subtotal > 40000:
        discount = subtotal * discount_rate
    else:
        discount = 0

    # Calculate total amount
    total_amount = subtotal + tax - discount

    # Update the entry fields
    Total.set(f"Rs. {total_amount:.2f}")
    Tax.set(f"Rs. {tax:.2f}")
    Discount.set(f"Rs. {discount:.2f}")

    # Open new window for the bill
    show_message_box(total_amount, tax, discount)

# Function to show message box (in new window)
def show_message_box(total, tax, discount):
    top = Toplevel(root)  # New window
    top.title("Total Bill")
    top.geometry("400x300")
    
    Label(top, text="Total Bill", font=("Arial", 20, "bold")).pack(pady=10)
    Label(top, text=f"Total: Rs. {total:.2f}", font=("Arial", 14)).pack(pady=10)
    Label(top, text=f"Tax: Rs. {tax:.2f}", font=("Arial", 14)).pack(pady=10)
    Label(top, text=f"Discount: Rs. {discount:.2f}", font=("Arial", 14)).pack(pady=10)

# Load images
def load_image(path, filename, size=(50, 50)):
    img = Image.open(os.path.join(path, filename))
    img = img.resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)

image_path = r"C:\Roshaan's Work\Programming Fundamental Projects\image"

# Menu Card Frame:
Label(text="MHR Soccer Cleats Store", bg="black", fg="white", font=("Stencil Std", 34, "italic", "bold"), width="300", height="2").pack()
f = Frame(root, bg="grey", highlightbackground="white", highlightthickness=2, width="300", height="370")
f.place(x=10, y=118)
Label(f, text="ITEMS", font=("Gabriola", 40, "bold"), fg="black", bg="grey").place(x=80, y=0)
Label(f, font=("Helvetica", 13, "bold"), text="1. Nike Mercurial ----> Rs.15000", fg="white", bg="grey").place(x=10, y=80)
Label(f, font=("Helvetica", 13, "bold"), text="2. Nike Phantom ----> Rs.22000", fg="white", bg="grey").place(x=10, y=110)
Label(f, font=("Helvetica", 13, "bold"), text="3. Nike Tiempo ----> Rs.19000", fg="white", bg="grey").place(x=10, y=140)
Label(f, font=("Helvetica", 13, "bold"), text="4. Puma Future ----> Rs.20500", fg="white", bg="grey").place(x=10, y=170)
Label(f, font=("Helvetica", 13, "bold"), text="5. Puma King ----> Rs.20200", fg="white", bg="grey").place(x=10, y=200)
Label(f, font=("Helvetica", 13, "bold"), text="6. Adidas Nemeziz ----> Rs.28100", fg="white", bg="grey").place(x=10, y=230)
Label(f, font=("Helvetica", 13, "bold"), text="7. Adidas F50 ----> Rs.17500", fg="white", bg="grey").place(x=10, y=260)
Label(f, font=("Helvetica", 13, "bold"), text="8. Adidas Predator ----> Rs.10200", fg="white", bg="grey").place(x=10, y=290)

# Entry Frame with padding for alignment
f1 = Frame(root, bd=3, height=370, width=300, relief=RAISED)
f1.pack()

# Labels for items
lbl_NikeMercurial = Label(f1, font=("aria", 18, "bold"), text=" Nike Mercurial ", width=12, fg="black")
lbl_NikePhantom = Label(f1, font=("aria", 18, "bold"), text=" Nike Phantom ", width=12, fg="black")
lbl_NikeTiempo = Label(f1, font=("aria", 18, "bold"), text=" Nike Tiempo ", width=12, fg="black")
lbl_PumaFuture = Label(f1, font=("aria", 18, "bold"), text=" Puma Future ", width=12, fg="black")
lbl_PumaKing = Label(f1, font=("aria", 18, "bold"), text=" Puma King ", width=12, fg="black")
lbl_AdidasNemeziz = Label(f1, font=("aria", 18, "bold"), text=" Adidas Nemeziz ", width=12, fg="black")
lbl_AdidasF50 = Label(f1, font=("aria", 18, "bold"), text=" Adidas F50 ", width=12, fg="black")
lbl_AdidasPredator = Label(f1, font=("aria", 18, "bold"), text=" Adidas Predator ", width=12, fg="black")

lbl_NikeMercurial.grid(row=1, column=0, padx=10, pady=5)
lbl_NikePhantom.grid(row=2, column=0, padx=10, pady=5)
lbl_NikeTiempo.grid(row=3, column=0, padx=10, pady=5)
lbl_PumaFuture.grid(row=4, column=0, padx=10, pady=5)
lbl_PumaKing.grid(row=5, column=0, padx=10, pady=5)
lbl_AdidasNemeziz.grid(row=6, column=0, padx=10, pady=5)
lbl_AdidasF50.grid(row=7, column=0, padx=10, pady=5)
lbl_AdidasPredator.grid(row=8, column=0, padx=10, pady=5)

# Images for items
img_NikeMercurial = load_image(image_path, "nike_mercurial.png")
img_NikePhantom = load_image(image_path, "nike_phantom.png")
img_NikeTiempo = load_image(image_path, "nike_tiempo.png")
img_PumaFuture = load_image(image_path, "puma_future.png")
img_PumaKing = load_image(image_path, "puma_king.png")
img_AdidasNemeziz = load_image(image_path, "adidas_nemeziz.png")
img_AdidasF50 = load_image(image_path, "adidas_f50.png")
img_AdidasPredator = load_image(image_path, "adidas_predator.png")

Label(f1, image=img_NikeMercurial).grid(row=1, column=2)
Label(f1, image=img_NikePhantom).grid(row=2, column=2)
Label(f1, image=img_NikeTiempo).grid(row=3, column=2)
Label(f1, image=img_PumaFuture).grid(row=4, column=2)
Label(f1, image=img_PumaKing).grid(row=5, column=2)
Label(f1, image=img_AdidasNemeziz).grid(row=6, column=2)
Label(f1, image=img_AdidasF50).grid(row=7, column=2)
Label(f1, image=img_AdidasPredator).grid(row=8, column=2)

# Entry fields for quantity
entry_NikeMercurial = Entry(f1, font=("aria", 18, "bold"), textvariable=NikeMercurial, width=8, bg="lightyellow")
entry_NikePhantom = Entry(f1, font=("aria", 18, "bold"), textvariable=NikePhantom, width=8, bg="lightyellow")
entry_NikeTiempo = Entry(f1, font=("aria", 18, "bold"), textvariable=NikeTiempo, width=8, bg="lightyellow")
entry_PumaFuture = Entry(f1, font=("aria", 18, "bold"), textvariable=PumaFuture, width=8, bg="lightyellow")
entry_PumaKing = Entry(f1, font=("aria", 18, "bold"), textvariable=PumaKing, width=8, bg="lightyellow")
entry_AdidasNemeziz = Entry(f1, font=("aria", 18, "bold"), textvariable=AdidasNemeziz, width=8, bg="lightyellow")
entry_AdidasF50 = Entry(f1, font=("aria", 18, "bold"), textvariable=AdidasF50, width=8, bg="lightyellow")
entry_AdidasPredator = Entry(f1, font=("aria", 18, "bold"), textvariable=AdidasPredator, width=8, bg="lightyellow")

entry_NikeMercurial.grid(row=1, column=1, padx=10, pady=5)
entry_NikePhantom.grid(row=2, column=1, padx=10, pady=5)
entry_NikeTiempo.grid(row=3, column=1, padx=10, pady=5)
entry_PumaFuture.grid(row=4, column=1, padx=10, pady=5)
entry_PumaKing.grid(row=5, column=1, padx=10, pady=5)
entry_AdidasNemeziz.grid(row=6, column=1, padx=10, pady=5)
entry_AdidasF50.grid(row=7, column=1, padx=10, pady=5)
entry_AdidasPredator.grid(row=8, column=1, padx=10, pady=5)

# Button to calculate total and show the bill in new window
btn_total = Button(f1, padx=10, pady=8, bd=5, fg="black", font=("ariel", 16, "bold"), width=10, text="Total", bg="powder blue", command=calculate_total)
btn_total.grid(row=9, column=0, columnspan=2, pady=10)

# Reset button to clear all fields
btn_reset = Button(f1, padx=10, pady=8, bd=5, fg="black", font=("ariel", 16, "bold"), width=10, text="Reset", bg="powder blue", command=Reset)
btn_reset.grid(row=10, column=0, columnspan=2, pady=10)

root.mainloop()
