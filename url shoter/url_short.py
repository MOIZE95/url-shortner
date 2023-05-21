# pip install pyshorteners
#pip install pyperclip
# install the above libraries

import tkinter as tk
import pyshorteners
import pyperclip

def shorten_url():
    url = url_entry.get()
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    pyperclip.copy(short_url)
    result_label.config(text="Shortened URL: " + short_url)
    copy_button.config(state=tk.NORMAL)

def copy_url():
    short_url = result_label.cget("text").split(": ")[1]
    pyperclip.copy(short_url)

# Create the main window
window = tk.Tk()
window.title("URL Shortener")

# Create URL entry widget
url_entry = tk.Entry(window, width=50, font=("Arial", 14))
url_entry.pack(pady=10)

# Create shorten button widget
shorten_button = tk.Button(window, text="Shorten URL", command=shorten_url, font=("Arial", 14))
shorten_button.pack(pady=5)

# Create result label widget
result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack()

# Create copy button widget
copy_button = tk.Button(window, text="Copy", command=copy_url, state=tk.DISABLED, font=("Arial", 14))
copy_button.pack(pady=5)

# Run the main event loop
window.mainloop()
