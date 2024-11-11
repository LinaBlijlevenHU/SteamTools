"""
tkinter_example_app

Note that this app does not look very nice with long texts.
"""
# Import TKinter
import tkinter as tk
from tkinter import ttk

# Import a helper function we've implemented somewhere else
from AI.binary_converter import binary_converter

# The root window is the starter screen
root = tk.Tk()                                  # Create the base screen
root.title('Binary Converter')                  # Set a title for the window
root.geometry('500x100')                         # Set the size of the app in pixels

# Create a frame inside the window to add our elements to
frame = ttk.Frame(root)

# This option object will add a little bit of padding
options = {'padx': 5, 'pady': 5}

# Add an input label for the text we are going to convert to binary
input_label = ttk.Label(frame, text='Text')
input_label.grid(
    column=0,           # Place the input in the first column
    row=0,              # and first row
    sticky='W',         # and align to left
    **options           # Add the padding we just created to let it breathe
)

# Create an entry object to let the user enter their input
toconvert = tk.StringVar()
text_entry = ttk.Entry(frame, textvariable=toconvert)
text_entry.grid(column=1, row=0, **options)
text_entry.focus()                                      # Focus on only editable field

# Logic for the convert button
def convert_button_clicked():
    """  Handle convert button click event """
    # Get the text currently in the box and convert
    f = toconvert.get()
    c = binary_converter(f)
    # Update the label
    result = f'Your text in binary: {c}'
    result_label.config(text=result)

# Now we can create the button and place it on the right (1 column further)
# than the text entry box.
convert_button = ttk.Button(frame, text='Convert')
convert_button.grid(column=2, row=0, sticky='W', **options)
# Link the logic from the function to the button itself
convert_button.configure(command=convert_button_clicked)

# Create the result label below everything we have built above,
# make it take up three columns since we need some space.
result_label = ttk.Label(frame)
result_label.grid(row=1, columnspan=3, **options)

# Add padding to the frame and show it
frame.grid(padx=10, pady=10)

# Start the Tkinter main loop now that we have everything set up.
root.mainloop()