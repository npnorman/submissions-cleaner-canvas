from tkinter import *
from tkinter import ttk, simpledialog, BooleanVar
import pathlib
import os
import sys
import numremover

root = Tk()
frm = ttk.Frame(root, padding=10)

root.title("Canvas Submissions Cleaner")

# button commands

inPath = pathlib.Path("./in/")
outPath = pathlib.Path("./out/")

saveFiles = BooleanVar()

def check_if_folder_exists(path):
    if path.exists() and path.is_dir():
        return True

    return False

def open_folder(path):
    if sys.platform == "win32":
        os.startfile(os.getcwd() + path)
    
    elif sys.platform == "darwin":   # macOS
        os.system(f'open "{path}"')
    else:                            # Linux
        os.system(f'xdg-open "{path}"')

def open_in_folder():
    if not check_if_folder_exists(inPath):
        # create a directory for in
        pathlib.Path("in").mkdir()
    
    #open directory
    open_folder("/in/")

    output.config(text="Opened in folder")

def open_out_folder():
    if not check_if_folder_exists(outPath):
        # create a directory for in
        pathlib.Path("out").mkdir()
    
    #open directory
    open_folder("/out/")

    output.config(text="Opened out folder")

def clean_submissions():

    uniqueOutPath = simpledialog.askstring("Input", "Assignment Name")
    uniqueOutPath = uniqueOutPath.strip()
    uniqueOutPath = uniqueOutPath.replace(" ", "-")

    numremover.cleanFiles(uniqueOutPath, "./in/", saveFiles.get())
    numremover.checkForOut("./out/")

    output.config(text="Cleaned files")

frm.grid()
ttk.Label(frm, text="Canvas Submissions Cleaner").grid(column=1, row=0)
ttk.Label(frm, text="By: Nicholas Norman").grid(column=1, row=1)

ttk.Button(frm, text="Open Input Folder", command=open_in_folder).grid(column=0, row=6)
ttk.Button(frm, text="Clean Submissions", command=clean_submissions).grid(column=1, row=6)
ttk.Button(frm, text="Open Output Folder", command=open_out_folder).grid(column=2, row=6)

checkbutton = ttk.Checkbutton(frm, text="Keep files in /in/ folder when cleaning", variable=saveFiles)

checkbutton.grid(column=1, row=3)

output = ttk.Label(frm, text="")

output.grid(column=0, row=100, columnspan=3)

root.mainloop()