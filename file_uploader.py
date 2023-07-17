from tkinter import Tk, Button, filedialog, Label
from PIL import Image

def open_file_dialog():
    filetypes = (
        ("PDF Files", "*.pdf"),
        ("Image Files", "*.jpg;*.jpeg;*.png;*.gif")
    )
    filepath = filedialog.askopenfilename(filetypes=filetypes)
    if filepath:
        # Perform actions with the selected file
        print("Selected File:", filepath)
        
        # For image files, you can also use PIL to open and display the image
        if filepath.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image = Image.open(filepath)
            image.show()

# Create the Tkinter window
window = Tk()
window.title("Upload File to Textract")
window.geometry("400x300")

# Create a label at the top of the window
label = Label(window, text="Upload file to Textract")
label.pack(pady=10)

# Create the button to open the file dialog
button = Button(window, text="Upload File", command=open_file_dialog)
button.pack()

# Run the Tkinter event loop
window.mainloop()