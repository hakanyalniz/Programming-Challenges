import tkinter as tk

# from tkinter import messagebox
from actions import download_youtube_video


def on_button_click():
    user_url = input_field.get(
        "1.0", tk.END
    ).strip()  # Get from character 0 and strip newline

    print(user_url)
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

# Create paned window
paned_window = tk.PanedWindow(
    root, orient=tk.VERTICAL, sashrelief=tk.RAISED, sashwidth=6
)
paned_window.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Create an input frame to put both scrollbar and text widget together
input_frame = tk.Frame(paned_window)

# Create a scrollbar widget inside the frame
scrollbar = tk.Scrollbar(input_frame, orient="vertical")
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create the input field, Text widget
# Also add the scrollbar to text widget
input_field = tk.Text(
    input_frame,
    wrap=tk.WORD,
    height=4,
    font=("Arial", 10),
    yscrollcommand=scrollbar.set,
)
input_field.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Adjust the config
scrollbar.config(command=input_field.yview)

# Add the input field to the paned window
paned_window.add(input_frame, stretch="never")

# Button widget
button = tk.Button(root, text="Download", command=on_button_click)
button.pack(pady=10)

# Label widget
status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.pack(pady=10)

# Application loop
root.mainloop()
