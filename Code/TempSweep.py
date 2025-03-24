import os
import shutil
import threading
import time
import customtkinter as ctk
from tkinter import messagebox
from pathlib import Path

# Initialize CustomTkinter
ctk.set_appearance_mode("Dark")  # Default theme
ctk.set_default_color_theme("blue")  # Default color scheme

# Define the paths for the temp directories
TEMP_LOCATIONS = [
    Path("C:/Windows/Temp"),
    Path.home() / "AppData" / "Local" / "Temp"
]

# Function to count total temp files
def count_temp_files():
    total = 0
    for folder in TEMP_LOCATIONS:
        if folder.exists():
            total += sum(1 for _ in folder.iterdir())
    return total

# Function to log deleted files
def log_deleted_files(file_path):
    with open("cleanup_log.txt", "a") as log:
        log.write(f"Deleted: {str(file_path)}\n")

# Function to clear temp files
def clear_temp_files():
    processed_files = 0
    total_before = count_temp_files()

    for folder in TEMP_LOCATIONS:
        if folder.exists():
            for item in folder.iterdir():
                try:
                    if item.is_file():
                        item.unlink()
                        log_deleted_files(item)
                    elif item.is_dir():
                        shutil.rmtree(item)
                        log_deleted_files(item)
                    processed_files += 1
                except Exception:
                    continue

    total_after = count_temp_files()
    root.after(0, update_file_count, total_after)  # Safe UI update from thread
    root.after(0, lambda: messagebox.showinfo("Success", "Temporary files cleared successfully!"))
    root.after(0, lambda: clear_btn.configure(state="normal"))  # Re-enable button

# Function to update UI file count
def update_file_count(count=None):
    if count is None:
        count = count_temp_files()
    total_files_label.configure(text=f"Remaining Temp Files: {count}")

# Function to ask for confirmation before cleaning
def confirm_cleanup():
    if messagebox.askyesno("Confirm", "Are you sure you want to delete all temp files?"):
        clear_btn.configure(state="disabled")  # Disable button to prevent multiple clicks
        threading.Thread(target=clear_temp_files, daemon=True).start()

# Function to show cleanup history
def show_cleanup_history():
    try:
        with open("cleanup_log.txt", "r") as log:
            history = log.read()
    except FileNotFoundError:
        history = "No history available."
    
    history_window = ctk.CTkToplevel(root)
    history_window.title("Cleanup History")
    history_label = ctk.CTkLabel(history_window, text=history, justify="left", wraplength=300)
    history_label.pack(padx=20, pady=20)

# Function to change theme
def change_theme():
    ctk.set_appearance_mode(theme_var.get())

# Function to open settings window
def open_settings():
    settings_window = ctk.CTkToplevel(root)
    settings_window.title("Settings")
    settings_window.geometry("300x200")

    theme_label = ctk.CTkLabel(settings_window, text="Select Theme:")
    theme_label.pack(pady=10)

    theme_menu = ctk.CTkOptionMenu(settings_window, variable=theme_var, values=["Light", "Dark", "System"], command=lambda _: change_theme())
    theme_menu.pack(pady=5)

    history_btn = ctk.CTkButton(settings_window, text="View Cleanup History", command=show_cleanup_history)
    history_btn.pack(pady=10)

# Function to update window opacity
def update_opacity(value):
    root.attributes("-alpha", float(value))

# UI Setup
root = ctk.CTk()
root.geometry("450x400")
root.title("Temp File Cleaner")
root.resizable(False, False)

root.iconbitmap("icon.ico")  

# Set the theme variable before using it
theme_var = ctk.StringVar(value="Dark")

# Create Frame
frame = ctk.CTkFrame(root, corner_radius=20)
frame.pack(fill="both", expand=True, padx=20, pady=20)

# Title Label
title_label = ctk.CTkLabel(frame, text="TempSweep", font=("Arial", 20, "bold"))
title_label.pack(side="top", pady=10)

# Settings Button 
settings_btn = ctk.CTkButton(frame, text="⚙️", width=40, height=40, command=open_settings)
settings_btn.place(x=350, y=10)

# Cleanup Button with confirmation
clear_btn = ctk.CTkButton(frame, text="Clear Temp Files", command=confirm_cleanup, fg_color="red", hover_color="darkred")
clear_btn.pack(pady=10)

# Label to show total temp files count
total_files_label = ctk.CTkLabel(frame, text="Remaining Temp Files: 0")
total_files_label.pack(pady=20)

# Selective Cleanup Checkboxes (Future Functionality)
cache_check = ctk.CTkCheckBox(frame, text="Clean Cache Files")
cache_check.pack(pady=5)

log_check = ctk.CTkCheckBox(frame, text="Clean Log Files")
log_check.pack(pady=5)

# Exit Button with confirmation
def confirm_exit():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        if os.path.exists("cleanup_log.txt"):
            os.remove("cleanup_log.txt")
        root.destroy()

exit_btn = ctk.CTkButton(frame, text="Exit", command=confirm_exit, fg_color="gray")
exit_btn.pack(side="bottom", pady=10)

# Initial File Count Update
update_file_count()

# Run UI
root.mainloop()
