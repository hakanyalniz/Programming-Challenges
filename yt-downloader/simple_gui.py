import tkinter as tk

# from tkinter import messagebox
from actions import download_youtube_video


def on_button_click():
    user_url = entry.get()
    status_label.config(text="Downloading...")
    root.update_idletasks()  # Update the GUI to fix the button clicked effect and update the status

    download_youtube_video(user_url)

    status_label.config(text="Complete!")
    root.after(3000, clear_status_message)


def clear_status_message():
    status_label.config(text="")


# Create the main window
root = tk.Tk()
root.title("Youtube Downloader")
root.geometry("400x200")

# Label widget
label = tk.Label(root, text="URL:", font=("Arial", 10))
label.pack(pady=10)

# Entry widget (Input field)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Button widget
button = tk.Button(root, text="Download", command=on_button_click)
button.pack(pady=10)

# Label widget
status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.pack(pady=10)

# Application loop
root.mainloop()
