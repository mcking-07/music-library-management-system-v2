from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk

def BinaryToDecimal(binary):
    
    string = int(binary, 2)
    return string
    
def viewrap(): 
    
    root = Tk()
    root.title("View Rap Songs")
    root.minsize(width=400,height=400)
    root.geometry("1000x400")
    
    tree = ttk.Treeview(root, column=("c1","c2","c3","c4","c5",),show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Title")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Artist")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Album")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="Genre")
    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="Release Year")
    tree.grid(sticky = (N,S,W,E))
    root.treeview = tree
    root.grid_rowconfigure(0, weight = 1)
    root.grid_columnconfigure(0, weight = 1)
    tree.pack(expand=True,fill=BOTH)

    genre = "Rap"
    try:
        filename = "music_data.txt"
        binary_rows = list()
        rows = list()
        single_row = list()
        with open(filename, "r") as f:
            binary_rows = f.readlines()

        for row_data in binary_rows:
            str_data = "" 
            for i in range(0, len(row_data), 8):
                temp_data = row_data[i:i + 8]
                if temp_data == "00101100":
                    single_row.append(str_data)
                    str_data = ""
                    continue
                if temp_data == "00001010":
                    import copy
                    rows.append(copy.deepcopy(single_row))
                    single_row.clear()                    
                    continue
                    
                decimal_data = BinaryToDecimal(temp_data)
                str_data = str_data + chr(decimal_data)

        rap = list()
        for srow in rows:
            if genre in srow:
                rap.append(srow)

        for i in rap:
            tree.insert("", tk.END, values=i)

    except:
        messagebox.showinfo('Error',"Failed To Fetch Songs From The Database")

    quitBtn = Button(root,text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
