# TempSweep

**TempSweep** is a lightweight desktop application that allows users to clean up temporary files from their system. The app helps improve system performance and free up disk space by removing files from commonly used temporary file directories in Windows. It features an easy-to-use interface built with **Python** and the **CustomTkinter** library for a modern look and feel.

---

## Features

- **Clear Temporary Files:** One-click removal of temp files and directories in common Windows temp locations.
- **History Tracking:** Keep a log of deleted files for later review.
- **Theme Support:** Switch between Dark, Light, and System themes for a personalized experience.
- **Progress Update:** View the number of remaining temp files after cleanup.
- **Selective Cleanup (Future Work):** Clean specific types of files like cache and log files.
- **Exit Confirmation:** Ensure accidental closure is prevented with a confirmation prompt.

---

## Requirements

Before running the app, ensure you have Python installed along with the necessary libraries.

### Python Version:
- Python 3.6 or higher

### Dependencies:
The app uses the following Python packages:
- `customtkinter`
- `shutil`
- `threading`
- `os`
- `tkinter`

You can install the required dependencies using `pip`:

```bash
pip install customtkinter 
```

### Installation

**Clone the repository:**

```bash
Copy
Edit
git clone https://github.com/NRJ900/TempSweep.git
cd TempSweep
```

**Install Dependencies:**

Ensure you have Python and the required libraries installed. You can create a virtual environment and install the dependencies as shown above.

The solution for removing temporary files with out manually navigating the folders.
For better and easy experience download the [release TempSweep](https://github.com/NRJ900/TempSweep/releases/download/disk-space-optimization/TempSweep.zip).
