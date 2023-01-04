import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import Main_page as mp
from db import Queries
import newPDF

t1 = Queries('clinicare.db')

class newPatient:
    def new_patient(self):
        srch = Toplevel()

        def back():
            temp = mp.mainPage()
            srch.destroy()
            temp.main_page()

        def add():
            # temp = db.Queries()
            if file_text.get()=='' and name_text.get()=='' and surname_text.get()=='' and father_name_text.get()==''and mob_text.get()=='' and age_text.get()=='' and addr_text.get()=='':
                messagebox.showerror('Required field','Please include some of the fields')
                return
            # print(file_text.get(),name_text.get(),surname_text.get())
            t1.add_patient(file_no=int(file_text.get()),name=name_text.get(),surname=surname_text.get(),father_name=father_name_text.get(),mobile_no=mob_text.get(),age=age_text.get(),place=addr_text.get())

            message = Label(srch,text="Patient Added Successfully!",font=("bold",18))
            message.grid(row=6,column=0,columnspan=2)

            new_pdf = newPDF.NewPatPDF()
            new_pdf.write(file_no=int(file_text.get()),name=name_text.get(),surname=surname_text.get(),father_name=father_name_text.get(),mobile_no=mob_text.get(),age=age_text.get(),place=addr_text.get())

            file_entry.delete(0,tkinter.END)
            name_entry.delete(0, tkinter.END)
            father_name_entry.delete(0, tkinter.END)
            surname_entry.delete(0, tkinter.END)
            age_entry.delete(0, tkinter.END)
            addr_entry.delete(0, tkinter.END)
            mob_entry.delete(0, tkinter.END)

        srch.title("Clinicare - New Patient")
        # srch.geometry("1250x350")
        app_width = 1250
        app_height = 350
        screen_width = srch.winfo_screenwidth()
        screen_height = srch.winfo_screenheight()

        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)

        srch.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        # back_img = Image.open("images/back.png")
        # resized = back_img.resize((60, 30), Image.Resampling.LANCZOS)
        # img = ImageTk.PhotoImage(resized)
        back_but = Button(srch, text="Back", command=back)
        back_but.grid(row=0, column=0, padx=20, pady=10, sticky=W)

        new_label = Label(srch, text="New Patient", font=("bold", 20))
        new_label.grid(row=1, column=0, padx=20, pady=10, sticky=W)

        file_text = StringVar()
        file_label = Label(srch, text="File No.", font=("bold", 15))
        file_label.grid(row=2, column=0, padx=20, pady=10, sticky=W)
        file_entry = Entry(srch, width=15, textvariable=file_text, font=("bold", 15))
        file_entry.grid(row=2, column=1, padx=20, pady=10, sticky=W)

        name_text = StringVar()
        name_label = Label(srch, text="Name", font=("bold", 15))
        name_label.grid(row=3, column=0, padx=20, pady=10, sticky=W)
        name_entry = Entry(srch, width=15, textvariable=name_text, font=("bold", 15))
        name_entry.grid(row=3, column=1, padx=20, pady=10, sticky=E)

        father_name_text = StringVar()
        father_name_label = Label(srch, text="Father's name", font=("bold", 15))
        father_name_label.grid(row=3, column=2, padx=20, pady=10, sticky=W)
        father_name_entry = Entry(srch, width=15, textvariable=father_name_text, font=("bold", 15))
        father_name_entry.grid(row=3, column=3, padx=20, pady=10, sticky=W)

        surname_text = StringVar()
        surname_label = Label(srch, text="Surname", font=("bold", 15))
        surname_label.grid(row=3, column=4, padx=20, pady=10, sticky=W)
        surname_entry = Entry(srch, width=20, textvariable=surname_text, font=("bold", 15))
        surname_entry.grid(row=3, column=5, padx=20, pady=10, sticky=W)

        age_text = StringVar()
        age_label = Label(srch, text="Age", font=("bold", 15))
        age_label.grid(row=4, column=0, padx=20, pady=10, sticky=W)
        age_entry = Entry(srch, width=10, textvariable=age_text, font=("bold", 15))
        age_entry.grid(row=4, column=1, padx=20, pady=10, sticky=W)

        addr_text = StringVar()
        addr_label = Label(srch, text="Address", font=("bold", 15))
        addr_label.grid(row=4, column=2, padx=20, pady=10, sticky=W)
        addr_entry = Entry(srch, width=20, textvariable=addr_text, font=("bold", 15))
        addr_entry.grid(row=4, column=3, padx=20, pady=10, sticky=W)

        mob_text = StringVar()
        mob_label = Label(srch, text="Mobile no.", font=("bold", 15))
        mob_label.grid(row=4, column=4, padx=20, pady=10, sticky=W)
        mob_entry = Entry(srch, width=20, textvariable=mob_text, font=("bold", 15))
        mob_entry.grid(row=4, column=5, padx=20, pady=10, sticky=E)

        add_but = Button(srch,text="Add",command=add)
        add_but.grid(row=5,column=5,padx=20,sticky=E)

        srch.mainloop()

def main():
    new = newPatient()
    new.new_patient()

if __name__=="__main__":
    main()

