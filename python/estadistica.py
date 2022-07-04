import os
import pathlib 
import path
from tkinter import Tk, Tcl
from tkinter.filedialog import askdirectory

Tk().withdraw()
filename = askdirectory(
    initialdir= "C:\Users\USUARIO\Code\proymaestria"
)
path = pathlib.Path(filename).absolute()
archivos = os.listdir(path)

archivos= list(
    filter(
        lambda name: ".pdf" in name,
        archivos
    )
)
for index, content in enumerate(archivos):
    print(
        f"archivo {index}: {content}" 
    )


