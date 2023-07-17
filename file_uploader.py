from tkinter import Tk, Button, filedialog, Label
import os
import shutil

filepath = ""  # Variable to store the file path

def open_file_dialog():
    global filepath  # You need to access the global variable to save the path
    filetypes = (
        ("PDF Files", "*.pdf"),
        ("Image Files", "*.jpg;*.jpeg;*.png;*.gif")
    )
    filepath = filedialog.askopenfilename(filetypes=filetypes)
    if filepath:
        # Perform actions with the selected file
        print("Selected File:", filepath)
        file_label.config(text="Uploaded File: " + os.path.basename(filepath))

def download_file():
    global filepath  # Access the global variable
    if filepath:
        download_path = filedialog.asksaveasfilename(defaultextension='*.*')
        if download_path:
            shutil.copy2(filepath, download_path)

# Create the Tkinter window
window = Tk()
window.title("Upload File to Textract")
window.geometry("400x300")

# Create a label at the top of the window
label = Label(window, text="Upload file to Textract")
label.pack(pady=10)

# Create the button to open the file dialog
upload_button = Button(window, text="Upload File", command=open_file_dialog)
upload_button.pack()

# Create a label to display the file name
file_label = Label(window, text="Uploaded File:")
file_label.pack(pady=10)

# Create the button to download the uploaded file
download_button = Button(window, text="Download File", command=download_file)
download_button.pack()

# Run the Tkinter event loop
window.mainloop()
