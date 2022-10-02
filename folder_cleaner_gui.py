#.......gui for folder managar.......

from cProfile import label
from email.mime import image
from multiprocessing.sharedctypes import Value
from sqlite3 import Row
from tkinter import *
from tkinter.ttk import *
from xml.dom.minidom import Document
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#........all imported modules............

main_root = Tk() #tkinder starting command
head_frame = Frame(main_root)
#.......body main head.........

pic = Image.open("logo.jpg")
photo = ImageTk.PhotoImage(pic)
main_root.iconphoto(False, photo)
#...............**************functions**********.................
def browse_button():
    filename = filedialog.askdirectory()
    global location
    location.set(filename)
    loc = location.get()
    
    return filename
def enable(children):
   for child in children:
      child.configure(state='enable')
def disable_it():
    for child in folder_frame.winfo_children():

        child.configure(state='disable')

#***************************....program code....**************************************
from multiprocessing import Value
import os
import shutil
folder_name  = ["Music","Compressed","Documents","Pictures","Videos","Programs","Coding_Programs"]
done = 0
def file_creater(folder_name):
    
    folder_path = location.get()
    folder_path = folder_path.replace("\\","/")

    os.chdir(folder_path)

    global folder_location
    folder_location = {}
    existed_file = os.listdir()
    for folders in folder_name:
            #by using join function we are joining path 
        path = os.path.join(folder_path, folders)
        if folders not in existed_file:
            os.mkdir(path)
        folder_location[folders] = str(path)
        global done
        done +=1

    


def file_mover(file_type,folder_location):
    folder_path = location.get()
    list_of_itams = os.listdir()
    def lowermk(n):
        return n.lower()

    list_of_itams = list(map(lowermk, list_of_itams))
    # print(list_of_itams)
    for itams in list_of_itams:
        # itams = itams.lower
        if itams.endswith(file_type):
            itams_path = os.path.join(folder_path, itams)
            new_path = os.path.join(folder_location, itams)
            shutil.move(itams_path,new_path)


def Submit():
    if var.get() == 2:
        try:
            folder_name[0] = Music_ver.get()
            folder_name[1] = Compressed_ver.get()
            folder_name[2] = Document_ver.get()
            folder_name[3] = Picture_ver.get()
            folder_name[4] = Video_ver.get()
            folder_name[5] = Program_ver.get()
            folder_name[6] = Coding_ver.get()
        except Exception as non_box:
            messagebox.showwarning("showwarning", Exception)
    try:
        file_creater(folder_name)
    except Exception as path_error:
        messagebox.showwarning("show warning", "folder location is empty or incarrect")

    list_of_doc = [".pdf",".txt","docx","doc",".csv",".psd",".xls",".xlsx"]
    list_of_pic = [".img",".jpeg",".png",".gif",".psd",".jpg"]
    list_of_prog = [".exe",".msi"]
    list_of_vdo = [".mp4",".mkv"]
    list_of_cpd = ['.rar',"7zip",".win",".tgz","tar","7z"]
    list_of_msc = [".mp3"]
    list_of_pro = [".py",".html",".htm",".c",".java",".cpp"]
    try:
        for type_doc in list_of_doc:
            file_mover(type_doc, folder_location[folder_name[2]])

        for type_pic in list_of_pic:
            file_mover(type_pic, folder_location[folder_name[3]])

        for type_prog in list_of_prog:
            file_mover(type_prog, folder_location[folder_name[5]])

        for type_vdo in list_of_vdo:
            file_mover(type_vdo, folder_location[folder_name[4]])

        for type_cpd in list_of_cpd:
            file_mover(type_cpd, folder_location[folder_name[1]])

        for type_msc in list_of_msc:
            file_mover(type_msc, folder_location[folder_name[0]])

        for type_pro in list_of_pro:
            file_mover(type_pro, folder_location[folder_name[6]])
    except Exception as move_error:
        messagebox.showwarning("show warning", "Same box are empty")
    if done == 7:

        messagebox.showinfo("Info", "Done")




#******************************************************************************************
#.......body size with min and max value.............
main_root.title("Folder Managar",)
main_root.geometry('400x450')
main_root.minsize(400,450)
main_root.maxsize(400,450)
#.......heading...............
Label(head_frame, text="Folders and Files Managar",font="comic 13 bold",foreground='#393c40',).grid(row=0,column=1,padx=5,pady=15)
#......main head.........
Label(head_frame,text="File location",).grid(row=1,column=0,padx=3) 
#file location is a input box which take input for browse buttom fuction which set the location of folther in location file 
location = StringVar()
file_location = tk.Entry(head_frame,textvariable=location,width=35) 

file_location.grid(row=1,column=1)

Button(head_frame,text="Browse..",command=browse_button).grid(row=1,column=2)
#change directory........


#......main head ending .............
head_frame.grid(row=0)

#.......body start........
#...body title...

main_head_frame = Frame(main_root)
Label(main_head_frame,text="What you want to do if you want to use default folder  select (Yes)\n\totherwise you can set file name select (No)",font="comic 9 bold",foreground='#393c40').pack(pady=20,padx=15)
main_head_frame.grid(row=1)

#.....***this frame contain radio buttom option***.......

main_body_rio_frame = Frame(main_root)
Label(main_body_rio_frame,text="Use default folder",font="comic 10 bold",foreground='#393c40').grid(row=0)
var = IntVar()
R1 = Radiobutton(main_body_rio_frame, text="Yes", variable=var, value=1,command=disable_it).grid(row=0,column=1)
R2 = Radiobutton(main_body_rio_frame, text="No", variable=var, value=2,
command=lambda: enable(folder_frame.winfo_children())).grid(row=0,column=2)

main_body_rio_frame.grid(row=2,pady=10)

#......end of radio buttom option.........
#.....folder name frame started.....
folder_frame = Frame(main_root)
Document_ver = StringVar()
Picture_ver = StringVar()
Video_ver = StringVar()
Music_ver = StringVar()
Coding_ver = StringVar()
Program_ver = StringVar()
Compressed_ver = StringVar()
Label(folder_frame,text="Music").grid(row=0,column=1)
Entry(folder_frame,textvariable = Music_ver, font=('calibre',10,'normal')).grid(row=0,column=2,pady=2)
Label(folder_frame,text="Video").grid(row=1,column=1)
Entry(folder_frame,textvariable = Video_ver, font=('calibre',10,'normal')).grid(row=1,column=2,pady=2)
Label(folder_frame,text="Picture").grid(row=2,column=1)
Entry(folder_frame,textvariable = Picture_ver, font=('calibre',10,'normal')).grid(row=2,column=2,pady=2)
Label(folder_frame,text="Document").grid(row=3,column=1)
Entry(folder_frame,textvariable = Document_ver, font=('calibre',10,'normal')).grid(row=3,column=2,pady=2)
Label(folder_frame,text="Coding").grid(row=4,column=1)
Entry(folder_frame,textvariable = Coding_ver, font=('calibre',10,'normal')).grid(row=4,column=2,pady=2)
Label(folder_frame,text="Compressed").grid(row=5,column=1)
Entry(folder_frame,textvariable = Compressed_ver, font=('calibre',10,'normal')).grid(row=5,column=2,pady=2)
Label(folder_frame,text="Program").grid(row=6,column=1)
Entry(folder_frame,textvariable = Program_ver, font=('calibre',10,'normal')).grid(row=6,column=2,pady=2)



folder_frame.grid(row=3)

#.....
for child in folder_frame.winfo_children():
   child.configure(state='disable')

#folder name frame ends here....................
# This will create style object
style = Style()

# This will be adding style, and
# naming that style variable as
# W.Tbutton (TButton is used for ttk.Button).
style.configure('W.TButton', font =('calibri', 10, 'bold', 'underline'),foreground = '#393c40')
# footer start......
footer = Frame(main_root)
Button(footer, text = 'Submit',width=30,style='W.TButton',command=Submit).grid(row=0,pady=20)
footer.grid(row=4)
#fooder end........
main_root.mainloop() #tkinder ending command

#*************************>>>>>>>>>end<<<<<<<<<<<<<<<<*****************************

