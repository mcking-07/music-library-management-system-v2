from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def BinaryToDecimal(binary):
    
    string = int(binary, 2)
    return string

def deletesong():

    title = songInfo1.get()

    try:
        filename = "music_data.txt"
        binary_rows = list()
        with open(filename, "r") as f:
            binary_rows = f.readlines()

        for row_data in binary_rows:
            str_data = ""
            single_row = list()
            rows = list()
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

        found = False
        for index in range(0,len(rows)):
            for item in rows[index]:
                if item == title:
                    rows.pop(index)
                    found = True
                    break
            if found == True:
                break

        filename = "music_data.txt"
        opfile = open(filename, 'w')
        for arow in rows:
            for item in arow:
                res = ''.join(format(i, '08b') for i in bytearray(item, encoding ='utf-8'))
                res += ''.join(format(i, '08b') for i in bytearray(",", encoding ='utf-8'))
                opfile.write(res)
            opfile.write("00001010") 

        messagebox.showinfo("Success", "Song Data Deleted Successfully")

    except:
        messagebox.showinfo("Error","Please Check Song Title")

    songInfo1.delete(0, END)
    root.destroy()

def delete():

    global img,songInfo1,songInfo2,songInfo3,songInfo4,songInfo5,Canvas1,root

    root = Toplevel()
    root.title("Delete Music Record")
    root.minsize(width=400,height=400)
    root.geometry("800x600")

    background_image = Image.open("delete.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size
    newImageSizeWidth = int(imageSizeWidth*0.8)
    newImageSizeHeight = int(imageSizeHeight*0.8)
    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)
    Canvas1.create_image(300,340,image = img)
    Canvas1.config(bg="black", width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#dfdee2",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Song Record",font='Helvetica 14 bold', bg="#010103", fg='white',)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg="#010103")
    labelFrame.place(relx=0.25,rely=0.4,relwidth=0.5,relheight=0.2)

    lb2 = Label(labelFrame,text="Song Title:", font='Helvetica 11 bold', bg="#000000", fg='white')
    lb2.place(relx=0.05,rely=0.5)

    songInfo1 = Entry(labelFrame)
    songInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)

    SubmitBtn = Button(root,text="Submit",font='Helvetica 11 bold',bg="#010103", fg='white',command=deletesong)
    SubmitBtn.place(relx=0.28,rely=0.75, relwidth=0.18,relheight=0.08)

    quitBtn = Button(root,text="Quit",font='Helvetica 11 bold',bg="#010103", fg='white', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.75, relwidth=0.18,relheight=0.08)

    root.mainloop()
