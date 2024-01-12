import tkinter as tk

def on_entry_change(*args):
    # Function to get the entry text whenever it changes
    entry_text = entry_var.get()
    print("Entry Text:", entry_text)

# Create the main Tkinter window
root = tk.Tk()
root.title("Entry Update Example")

# Create a StringVar to track the Entry content
entry_var = tk.StringVar()

# Create an Entry widget and associate it with the StringVar
entry = tk.Entry(root, width=30, textvariable=entry_var)
entry.pack(padx=10, pady=10)

# Set up the trace to call the on_entry_change function whenever the content changes
entry_var.trace_add("write", on_entry_change)

# Run the Tkinter event loop
root.mainloop()
