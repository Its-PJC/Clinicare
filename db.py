import os
import sqlite3 as sq
import pandas as pd
import csv


class Queries:
    def __init__(self,t1):
        self.table = "patientData"
        self.connection = sq.connect(t1)
        self.curs = self.connection.cursor()
        self.curs.execute(f"create table if not exists {self.table} (file_no int primary key,surname text,name text,father_name text,place text,age text, mobile_no text)")
        self.connection.commit()

        # def create(self):
        patients = pd.read_csv("export.csv")
        patients.to_sql(self.table,self.connection,if_exists='replace',index=False)
        self.curs.execute(f'delete from {self.table} where file_no=11088')

    def add_patient(self,file_no=None,surname=None,name=None,father_name=None,place=None,age=None,mobile_no=None):
        params = (file_no,surname,name,father_name,place,age,mobile_no)
        # print(params)
        self.curs.execute(f"INSERT INTO {self.table} VALUES (NULL,?,?,?,?,?,?,?)",params)
        self.connection.commit()
        self.export_table()
        # print("Hello")

    def search_patient(self,file_no=None,surname="",name="",mobile_no=""):
        params = (file_no,name,surname,mobile_no)
        self.curs.execute(f"SELECT * FROM {self.table} WHERE file_no=? OR (name=? OR surname=?) OR mobile_no=?",params)
        self.export_table()
        return self.curs.fetchall()

    def update(self,file_no=None,surname="",name="",father_name="",place="",age="",mobile_no=""):
        params = (surname, name, father_name, place, age, mobile_no,file_no)
        self.curs.execute(f"update {self.table} set surname=?,name=?,father_name=?,place=?,age=?,mobile_no=? where file_no = ?",params)
        self.connection.commit()
        self.export_table()

    def export_table(self):
        curs = self.connection.cursor()
        curs.execute(f"select * from {self.table}")
        with open("export.csv","w") as csv_file:
            csv_writer = csv.writer(csv_file,delimiter=",")
            csv_writer.writerow([i[0] for i in curs.description])
            csv_writer.writerows(curs)
        dirpath = os.getcwd()+"\export.csv"
        print("Data exported"+" "+dirpath)

    def __del__(self):
        self.connection.close()

def main():
    query = Queries('clinicare.db')
    # query.add_patient(file_no=11087,name="Pranav",surname="Chiddarwar")
    # query.search_patient(file_no=0,surname="Chiddarwar",name="Pranav",age=21)
    # curs.execute('select * from patientData where file_no=3203')

    # curs.execute('select * from patientData limit 10')
    records = query.search_patient(file_no=11087)

    for row in records:
        print(row)

if __name__=="__main__":
    main()
