from tkinter import *
from PIL import ImageTk, Image
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)


def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y


def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)


def getImage(path):
    img = Image.open(path)
    img = img.resize((40, 53,), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return img


def reset(panels):
    x = 565
    y = 300
    for panel in panels:
        panel.place(x=x, y=y)
        if y != 420:
            y = 420
        else:
            x += 75
            y = 300


root = Tk()
root.title("Among Us Helper")

menubar = Menu(root)
menubar.add_command(label="Hello!", command=reset)
root.config(menu=menubar)

frame = LabelFrame(root, text="Sus", padx=250, pady=100)
frame.grid(row=0, column=0, padx=10, pady=10)
frame2 = LabelFrame(root, text="Normal", padx=250, pady=100)
frame2.grid(row=1, column=1, padx=10, pady=10)
frame3 = LabelFrame(root, text="Dead/Not in Game", padx=250, pady=100)
frame3.grid(row=2, column=1, padx=10, pady=10)
frame4 = LabelFrame(root, text="Targets", padx=250, pady=100)
frame4.grid(row=0, column=2, padx=10, pady=10)
frame5 = LabelFrame(root, text="Confirmed Good", padx=250, pady=100)
frame5.grid(row=1, column=0, padx=10, pady=10)
frame6 = LabelFrame(root, text="Keep Alive", padx=250, pady=100)
frame6.grid(row=1, column=2, padx=10, pady=10)

path = resource_path("AmongUs\\red.png")
img = getImage(path)
panel = Label(root, image=img)
make_draggable(panel)
panel.grid(row=2, column=0)

path2 = resource_path("AmongUs\\lime.png")
img2 = getImage(path2)
panel2 = Label(root, image=img2)
make_draggable(panel2)
panel2.grid(row=2, column=0)

path3 = resource_path("AmongUs\\cyan.png")
img3 = getImage(path3)
panel3 = Label(root, image=img3)
make_draggable(panel3)
panel3.grid(row=2, column=0)

path4 = resource_path("AmongUs\\brown.png")
img4 = getImage(path4)
panel4 = Label(root, image=img4)
make_draggable(panel4)
panel4.grid(row=2, column=0)

path5 = "AmongUs\\purple.png"
img5 = getImage(path5)
panel5 = Label(root, image=img5)
make_draggable(panel5)
panel5.grid(row=2, column=0)

path6 = resource_path("AmongUs\\white.png")
img6 = getImage(path6)
panel6 = Label(root, image=img6)
make_draggable(panel6)
panel6.grid(row=2, column=0)

path7 = resource_path("AmongUs\\black.png")
img7 = getImage(path7)
panel7 = Label(root, image=img7)
make_draggable(panel7)
panel7.grid(row=2, column=0)

path8 = resource_path("AmongUs\\yellow.png")
img8 = getImage(path8)
panel8 = Label(root, image=img8)
make_draggable(panel8)
panel8.grid(row=2, column=0)

path9 = resource_path("AmongUs\\orange.png")
img9 = getImage(path9)
panel9 = Label(root, image=img9)
make_draggable(panel9)
panel9.grid(row=2, column=0)

path0 = resource_path("AmongUs\\pink.png")
img0 = getImage(path0)
panel0 = Label(root, image=img0)
make_draggable(panel0)
panel0.grid(row=2, column=0)

path11 = resource_path("AmongUs\\green.png")
img11 = getImage(path11)
panel11 = Label(root, image=img11)
make_draggable(panel11)
panel11.grid(row=2, column=0)

path12 = resource_path("AmongUs\\blue.png")
img12 = getImage(path12)
panel12 = Label(root, image=img12)
make_draggable(panel12)
panel12.grid(row=2, column=0)

panels = [panel, panel2, panel3, panel4, panel5, panel6, panel7, panel8, panel9, panel0, panel11, panel12]

reset(panels)

menubar = Menu(root)
menubar.add_command(label="Reset", command=lambda : reset(panels))
root.config(menu=menubar)

b = Label(frame, text="")
b2 = Label(frame2, text="")
b3 = Label(frame3, text="")
b4 = Label(frame4, text="")
b5 = Label(frame5, text="")
b6 = Label(frame6, text="")

b.grid(row=0, column=0)
b2.grid(row=0, column=0)
b3.grid(row=0, column=0)
b4.grid(row=0, column=0)
b5.grid(row=0, column=0)
b6.grid(row=0, column=0)
root.mainloop()