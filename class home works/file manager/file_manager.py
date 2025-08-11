from tkinter import filedialog, messagebox, Button , Tk, Label
import shutil
import os
import easygui

def file_open_box():
    path = easygui.fileopenbox()
    return path

file