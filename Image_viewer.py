from tkinter import *
from PIL import ImageTk,Image
from pdf2image import convert_from_path

class ImageViewer:
    def __init__(self):
        self.root = Toplevel()
        self.root.title("Clinicare - View")

        self.root.geometry("700x700")

        self.images = convert_from_path(str("C:/Users/Pranav J Chiddarwar/PycharmProjects/Clinicare/tc1.pdf"))
