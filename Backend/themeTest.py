import tkinter as tk

def on_mouse_motion(event, canvas):
    x, y = event.x, event.y
    print(f"Mouse moved to ({x}, {y}) on canvas {canvas}")

root = tk.Tk()
root.title("Mouse Movement Tracker")

canvas1 = tk.Canvas(root, width=400, height=300, bg="white")
canvas1.pack()

canvas2 = tk.Canvas(root, width=400, height=300, bg="lightgray")
canvas2.pack()

# Bind the motion event to the specific canvas
canvas1.bind("<Motion>", lambda event: on_mouse_motion(event, canvas1))
canvas2.bind("<Motion>", lambda event: on_mouse_motion(event, canvas2))

root.mainloop()
