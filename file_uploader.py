from tkinter import Tk, Button, filedialog, Label, OptionMenu, StringVar, IntVar, Checkbutton
import os
import shutil
from components.upload_to_s3 import *
from components.textract import *

filepath = ""  # Variable to store the file path
bucket_name = 'poe-textract'

def open_file_dialog():
    global filepath  # You need to access the global variable to save the path
    global bucket_name
    filetypes = (
        ("PDF Files", "*.pdf"),
        ("Image Files", "*.jpg;*.jpeg;*.png;*.gif")
    )
    filepath = filedialog.askopenfilename(filetypes=filetypes)
    if filepath:
        filename = os.path.basename(filepath)
        # Perform actions with the selected file
        print("Selected File:", filepath)
        
        input_file_path = filepath
        s3_output_key = 'sample/'+filename

        upload_to_s3(input_file_path, bucket_name, s3_output_key)

        file_label.config(text="Uploaded File: " + filename)

def start_textract():
    global filepath
    global bucket_name
    global language_var
    global translate_var

    filename = os.path.basename(filepath)
    s3_output_key = 'sample/'+filename

    require_translate = False
    selected_language_code = 'en'
    selected_language = language_var.get()
    
    if selected_language == "Spanish" and translate_var.get() == 1:
        selected_language_code = 'es'
        require_translate = True
    
    call_textract(bucket_name, s3_output_key, selected_language_code, require_translate)  # Passing selected language

def download_file():
    global filepath  # Access the global variable
    global language_var
    global translate_var

    require_translate = False
    selected_language_code = 'en'
    selected_language = language_var.get()
    
    if selected_language == "Spanish" and translate_var.get() == 1:
        selected_language_code = 'es'
        require_translate = True

    if(require_translate):
        result_filename = 'sample/'+os.path.splitext(os.path.basename(filepath))[0]+ f'_{selected_language_code}.csv'
    else:
        result_filename = 'sample/'+os.path.splitext(os.path.basename(filepath))[0]+'.csv'
    print(result_filename)
    if result_filename:
        download_path = filedialog.asksaveasfilename(defaultextension='*.*')
        if download_path:
            shutil.copy2(result_filename, download_path)

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

# Create the checkbox for translation
translate_var = IntVar()
translate_checkbox = Checkbutton(window, text="Translate to:",
                                variable=translate_var, onvalue=1, offvalue=0)
translate_checkbox.pack()

# Create a selection menu for choosing the language
language_var = StringVar(window)
language_var.set("English")  # Default language selection
language_menu = OptionMenu(window, language_var, "English", "Spanish")
language_menu.pack()

# Create the button to open the file dialog
upload_button = Button(window, text="Start Textract", command=start_textract)
upload_button.pack()

# Create the button to download the uploaded file
download_button = Button(window, text="Download File", command=download_file)
download_button.pack()

# Run the Tkinter event loop
window.mainloop()
