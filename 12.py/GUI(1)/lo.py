import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk

# --- Tkinter setup ---
root = tk.Tk()
root.title("Professional Login")
root.geometry("900x600")
root.resizable(True, True)  # allow resizing

# --- Video setup ---
cap = cv2.VideoCapture(r"eating.mp4")  # use full path if needed

# Background label
bg_label = tk.Label(root)
bg_label.pack(fill="both", expand=True)

# Frame for login box
login_frame = tk.Frame(root, bg="#ffffff", bd=0, highlightthickness=0)
login_frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=250)

# Title
tk.Label(login_frame, text="Login", font=("Segoe UI", 20, "bold"), bg="#ffffff").pack(pady=10)

# Username field
username = ttk.Entry(login_frame, font=("Segoe UI", 12))
username.pack(pady=10, padx=20, fill="x")

# Password field
password = ttk.Entry(login_frame, font=("Segoe UI", 12), show="*")
password.pack(pady=10, padx=20, fill="x")

# Login button
ttk.Button(login_frame, text="Login", command=lambda: print("Login clicked")).pack(pady=15)


# --- Update video function ---
def update_frame():
    ret, frame = cap.read()
    if not ret or frame is None:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # restart video
        root.after(30, update_frame)
        return

    # Get current window size
    win_w = root.winfo_width()
    win_h = root.winfo_height()

    # Resize video to window
    frame = cv2.resize(frame, (win_w, win_h))

    # Blur only login box area
    x, y, w, h = (win_w // 2 - 175, win_h // 2 - 125, 350, 250)
    roi = frame[y:y+h, x:x+w]
    roi = cv2.GaussianBlur(roi, (35, 35), 30)
    frame[y:y+h, x:x+w] = roi

    # Convert to PhotoImage
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)

    bg_label.imgtk = imgtk
    bg_label.config(image=imgtk)

    root.after(30, update_frame)


update_frame()
root.mainloop()
