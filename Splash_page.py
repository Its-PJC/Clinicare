# from tkinter import *
# from PIL import ImageTk, Image
# import Main_page as mp
#
# root = Toplevel()
# root.title("Clinicare")
# app_width = 850
# app_height = 144
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
#
# x = (screen_width / 2) - (app_width / 2)
# y = (screen_height / 2) - (app_height / 2)
# root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
# root.overrideredirect(True)
#
# temp = mp.mainPage()
#
# class Splash:
#     def __init__(self,master):
#         myFrame = Frame(master)
#         img = Image.open("images/clinicare title.png")
#         resized = img.resize((850, 144), Image.Resampling.LANCZOS)
#         t_img = ImageTk.PhotoImage(resized)
#
#         myFrame = Label(root, image=t_img)
#         myFrame.grid(row=0, column=0)
#
#         root.after(2000, self.splash_end)
#
#     def splash_end(self):
#         root.destroy()
#         temp.main_page()
#
# e = Splash(root)
#
# root.mainloop()

from tkinter import *
from PIL import ImageTk, Image
import Main_page as mp


class splashPage:
    def __init__(self):
        # self.splash_root=Toplevel()
        self.temp = mp.mainPage()

    def splash_page(self):
        splash_root = Toplevel()
        splash_root.title("Clinicare_splash")

        def splash_end():
            splash_root.destroy()
            self.temp.main_page()

        # Bring Splash_page to the center of the window
        app_width = 850
        app_height = 144
        screen_width = splash_root.winfo_screenwidth()
        screen_height = splash_root.winfo_screenheight()

        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)

        splash_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        # Hide title bas of splash screen
        splash_root.overrideredirect(True)

        # Grid.rowconfigure(self.splash_root, 0, weight=1)
        # Grid.columnconfigure(self.splash_root, 0, weight=1)

        # Title of the main page
        img = Image.open("images/clinicare title.png")
        resized = img.resize((850, 144), Image.Resampling.LANCZOS)
        t_img = ImageTk.PhotoImage(resized)

        t_Label = Label(splash_root, image=t_img)
        t_Label.grid(row=0, column=0)

        # Splash Screen timer
        splash_root.after(2000, splash_end)


        # Start program
        splash_root.mainloop()

def main():
    start = splashPage()
    start.splash_page()


if __name__ == "__main__":
    main()
