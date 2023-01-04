from tkinter import *
import Search_page as sp
import New_patient as np


class mainPage:

    def main_page(self):
        app = Toplevel()

        def old_but():
            temp = sp.searchPage()
            app.destroy()
            temp.search()

        def new_but():
            temp = np.newPatient()
            app.destroy()
            temp.new_patient()

        app.title("Clinicare")
        # app.geometry("830x200")
        app_width = 830
        app_height = 200
        screen_width = app.winfo_screenwidth()
        screen_height = app.winfo_screenheight()

        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)

        app.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        bg = PhotoImage(file="images/Main_page_bg.png")
        # Create canvas
        my_canvas = Canvas(app, width=830, height=200)
        # my_canvas.pack(fill="both", expand=True)
        my_canvas.grid(row=0, column=0, columnspan=2)
        # Set image in canvas
        my_canvas.create_image(0, 0, image=bg, anchor="nw")

        # Configure rows and columns
        Grid.rowconfigure(app, 0, weight=1)
        Grid.columnconfigure(app, 0, weight=1)
        Grid.columnconfigure(app, 1, weight=1)

        # Add buttons
        old_pat = Button(app, text="Old\nPatient", font=("Bold", 30), fg="#ffffff", bg="#183479", borderwidth=0,
                         command=old_but)
        old_pat.grid(row=0, column=0)

        new_pat = Button(app, text="New\nPatient", font=("Bold", 30), fg="#ffffff", bg="#183479", borderwidth=0,
                         command=new_but)
        new_pat.grid(row=0, column=1)

        app.mainloop()


def main():
    start = mainPage()
    start.main_page()


if __name__ == "__main__":
    main()