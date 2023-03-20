import tkinter as tk
from tkinter import filedialog, PhotoImage

root = tk.Tk()

photo = PhotoImage(file = "ninja.png")
root.iconphoto(False, photo)

blank_space = " "
root.title(80*blank_space + "DIY Text-Editor")

text = tk.Text(root)
text["bg"] = "black"
text["fg"] = "white"
text.grid()

root["bg"] = "black"

def saveas():
    global text  

    t = text.get("1.0", "end-1c")
    savelocation=filedialog.asksaveasfilename()
 
    file1=open(savelocation, "w+")
    file1.write(t)

    file1.close()


button = tk.Button(root,text="Save Text",command=saveas,bg="black",fg="white")
button.grid()

root.mainloop()

