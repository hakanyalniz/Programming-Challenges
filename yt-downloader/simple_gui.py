import tkinter as tk

# from tkinter import messagebox
from actions import download_youtube_video


def on_button_click():
    user_url = entry.get()
    download_youtube_video(user_url)


# 1. Create the main window
root = tk.Tk()
root.title("Youtube Downloader")
root.geometry("400x200")

# 2. Add a Label widget
label = tk.Label(root, text="URL:", font=("Arial", 10))
label.pack(pady=10)

# 3. Add an Entry widget (Input field)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# 4. Add a Button widget
button = tk.Button(root, text="Download", command=on_button_click)
button.pack(pady=10)

# 5. Start the application loop
root.mainloop()
