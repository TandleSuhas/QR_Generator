import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to generate QR code
def generate_qr(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    return img

# Function to handle the button click
def on_generate_button_click():
    data = entry.get()
    if not data:
        messagebox.showwarning("Input Error", "Please enter some data")
        return
    
    filename = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG files", "*.png"),
                                                       ("All files", "*.*")])
    if filename:
        img = generate_qr(data, filename)
        display_qr(img)
        messagebox.showinfo("Success", f"QR Code generated and saved as {filename}")

# Function to display the generated QR code in the UI
def display_qr(img):
    img = img.resize((200, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    qr_display.config(image=img)
    qr_display.image = img

# Set up the GUI
app = tk.Tk()
app.title("QR Code Generator")
app.geometry("400x500")
app.config(bg="#f0f0f0")

# Create and place the widgets
label = tk.Label(app, text="Enter Data:", font=("Arial", 14), bg="#f0f0f0")
label.pack(pady=20)

entry = tk.Entry(app, font=("Arial", 14), width=30)
entry.pack(pady=10)

generate_button = tk.Button(app, text="Generate QR Code", font=("Arial", 14), command=on_generate_button_click)
generate_button.pack(pady=20)

qr_display = tk.Label(app, bg="#f0f0f0")
qr_display.pack(pady=20)

# Start the GUI event loop
app.mainloop()
