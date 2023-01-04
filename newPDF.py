from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,A4
import subprocess
from datetime import date


class NewPatPDF:
    def __init__(self):
        self.packet = io.BytesIO()
        # create a new PDF with Reportlab
        self.can = canvas.Canvas(self.packet, pagesize=A4)

    def write(self,file_no=None,name=None,surname="",father_name="",age="",place="",mobile_no=""):
        file_no=str(file_no)
        if file_no[-2:]==".0":
            file_no=file_no[:-2]
        self.can.drawString(100, 796, str(file_no))
        if father_name=="None":
            father_name=""
        self.can.drawString(150, 660, name+" "+father_name+" "+surname)
        if place=="None":
            place=""
        self.can.drawString(120, 639, place)
        if age=="None":
            age=""
        self.can.drawString(520, 660, str(age))
        if mobile_no=="None":
            mobile_no=""
        self.can.drawString(450, 616, mobile_no)
        Today=(str(date.today()))
        Today=Today[-2:]+"/"+Today[5:7]+"/"+Today[:4]
        self.can.drawString(498,680,Today)
        self.can.save()

        #move to the beginning of the StringIO buffer
        self.packet.seek(0)
        new_pdf = PdfFileReader(self.packet)
        # read your existing PDF
        existing_pdf = PdfFileReader(open("Case papers/Case Paper.pdf", "rb"))
        output = PdfFileWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)
        # finally, write "output" to a real file
        # num=int(file_no[:-2])
        rem = int(file_no) // 1000
        path = 'C:/Pranav/Patient Data/' + str(rem) + '/' + str(file_no) + '.pdf'
        outputStream = open(path, "wb")
        output.write(outputStream)
        outputStream.close()

        # path = 'destination.pdf'
        subprocess.Popen([path],shell=True)

def main():
    temp = NewPatPDF()
    temp.write(file_no=11087,name="Pranav",surname="Chiddarwar",father_name="Jayant",place="Akola",age=21,mobile_no="7057196930")

if __name__=="__main__":
    main()