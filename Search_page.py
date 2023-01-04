import tkinter
from tkinter import *
# from PIL import ImageTk, Image
import Main_page as mp
from db import Queries
import subprocess
import newPDF

class searchPage():

    def search(self):
        srch = Toplevel()
        t1 = mp.mainPage()
        t2 =Queries('clinicare.db')

        def back():
            srch.destroy()
            t1.main_page()

        def searchPat():
            res = t2.search_patient(file_no=(file_text.get()),name=name_text.get(),surname=surname_text.get(),mobile_no=mob_text.get())
            pat_list.delete(0,tkinter.END)
            for row in res:
                pat_list.insert(tkinter.END,row[1:])
                # pat_list.insert(tkinter.END,str(row[1])+": "+row[3]+" "+row[4]+" "+row[2])#+", "+row[5]+", "+row[6]+", "+row[7])

        def select_item(event):
            try:
                index = pat_list.curselection()
                selected_pat = pat_list.get(index[0])

                file_entry.delete(0, tkinter.END)
                file_entry.insert(tkinter.END,selected_pat[0])
                name_entry.delete(0, tkinter.END)
                name_entry.insert(tkinter.END, selected_pat[2])
                father_name_entry.delete(0, tkinter.END)
                father_name_entry.insert(tkinter.END, selected_pat[3])
                surname_entry.delete(0, tkinter.END)
                surname_entry.insert(tkinter.END, selected_pat[1])
                age_entry.delete(0, tkinter.END)
                age_entry.insert(tkinter.END, selected_pat[5])
                addr_entry.delete(0, tkinter.END)
                addr_entry.insert(tkinter.END, selected_pat[4])
                mob_entry.delete(0, tkinter.END)
                mob_entry.insert(tkinter.END, selected_pat[6])

            except IndexError:
                pass

        def openFile():
            file_no = file_text.get()
            if file_no[-2:]==".0":
                file_no=file_no[:-2]
            rem = int(file_no)//1000
            path = 'C:/Pranav/Patient Data/'+str(rem)+'/'+str(file_no)+'.pdf'
            subprocess.Popen([path], shell=True)
            pat_list.delete(0, tkinter.END)
            searchPat()
            clear()

        def new():
            new_pdf = newPDF.NewPatPDF()
            new_pdf.write(file_no=(file_text.get()), name=name_text.get(), surname=surname_text.get(),
                          father_name=father_name_text.get(), mobile_no=mob_text.get(), age=age_text.get(),
                          place=addr_text.get())

        def updatePat():
            t2.update(file_no=(file_text.get()),name=name_text.get(),surname=surname_text.get(),father_name=father_name_text.get(),mobile_no=mob_text.get(),age=age_text.get(),place=addr_text.get())
            res = t2.search_patient(file_no=(file_text.get()), name=name_text.get(), surname=surname_text.get(),mobile_no=mob_text.get())
            pat_list.delete(0, tkinter.END)
            for row in res:
                pat_list.insert(tkinter.END, row[1:])
            clear()

        def clear():
            file_entry.delete(0, tkinter.END)
            name_entry.delete(0, tkinter.END)
            father_name_entry.delete(0, tkinter.END)
            surname_entry.delete(0, tkinter.END)
            age_entry.delete(0, tkinter.END)
            addr_entry.delete(0, tkinter.END)
            mob_entry.delete(0, tkinter.END)

        srch.title("Clinicare - Search")
        # srch.geometry("1250x500")

        app_width = 1170
        app_height = 550
        screen_width = srch.winfo_screenwidth()
        screen_height = srch.winfo_screenheight()

        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)

        srch.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        # back_img = Image.open("images/back.png")
        # resized = back_img.resize((30, 30), Image.Resampling.LANCZOS)
        # img = ImageTk.PhotoImage(resized)
        back_but = Button(srch,text="Back",font = ("bold", 18),command=back)
        back_but.grid(row=0,column=0,padx=20,pady=10,sticky=W)

        search_label = Label(srch,text = "Search", font = ("bold", 25))
        search_label.grid(row=1,column=0,padx=20,pady=10,sticky=W)

        file_text = StringVar()
        file_label = Label(srch, text="File No.", font=("bold", 15))
        file_label.grid(row=2, column=0, padx=20, pady=10, sticky=W)
        file_entry = Entry(srch, width=15, textvariable=file_text, font=("bold", 15))
        file_entry.grid(row=2, column=1, pady=10, sticky=W)

        name_text = StringVar()
        name_label = Label(srch, text="Name", font=("bold", 15))
        name_label.grid(row=3, column=0, padx=20, pady=10, sticky=W)
        name_entry = Entry(srch, width=15, textvariable=name_text, font=("bold", 15))
        name_entry.grid(row=3, column=1, pady=10, sticky=W)

        father_name_text = StringVar()
        father_name_label = Label(srch, text="Father's name", font=("bold", 15))
        father_name_label.grid(row=3, column=2, padx=20, pady=10, sticky=W,)
        father_name_entry = Entry(srch, width=15, textvariable=father_name_text, font=("bold", 15))
        father_name_entry.grid(row=3, column=3, pady=10, sticky=W)

        surname_text = StringVar()
        surname_label = Label(srch, text="Surname", font=("bold", 15))
        surname_label.grid(row=3, column=4, padx=20, pady=10, sticky=W)
        surname_entry = Entry(srch, width=20, textvariable=surname_text, font=("bold", 15))
        surname_entry.grid(row=3, column=5, pady=10, sticky=W)

        age_text = StringVar()
        age_label = Label(srch, text="Age", font=("bold", 15))
        age_label.grid(row=4, column=0, padx=20, pady=10, sticky=W)
        age_entry = Entry(srch, width=10, textvariable=age_text, font=("bold", 15))
        age_entry.grid(row=4, column=1, pady=10, sticky=W)

        addr_text = StringVar()
        addr_label = Label(srch, text="Address", font=("bold", 15))
        addr_label.grid(row=4, column=2, padx=20, pady=10, sticky=W)
        addr_entry = Entry(srch, width=20, textvariable=addr_text, font=("bold", 15))
        addr_entry.grid(row=4, column=3, pady=10, sticky=W)

        mob_text = StringVar()
        mob_label = Label(srch, text="Mobile no.", font=("bold", 15))
        mob_label.grid(row=4, column=4, padx=20, pady=10, sticky=W)
        mob_entry = Entry(srch, width=20, textvariable=mob_text, font=("bold", 15))
        mob_entry.grid(row=4, column=5, pady=10, sticky=W)

        pat_list = Listbox(srch,height=8,width=80,font=("bold",12))
        pat_list.grid(row=6,column=0,rowspan=6,columnspan=4,padx=20,sticky=W)

        pat_list.bind('<<ListboxSelect>>',select_item)

        srch_but = Button(srch, text="Search",font=("bold",10), command=searchPat)
        srch_but.grid(row=5, column=3, padx=20,pady=10, sticky=E)

        open_but = Button(srch, text="Open",font=("bold",10), command=openFile)
        open_but.grid(row=5, column=4, padx=20,pady=10)

        update_but = Button(srch, text="Update",font=("bold",10), command=updatePat)
        update_but.grid(row=5, column=5, padx=20,pady=10, sticky=W)

        new_but = Button(srch, text="New", font=("bold", 10), command=new)
        new_but.grid(row=5, column=5, padx=20, pady=10, sticky=E)

        srch.mainloop()


def main():
    start = searchPage()
    start.search()


if __name__ == "__main__":
    main()