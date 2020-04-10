from tkinter import *
import sqlite3
from tkinter import messagebox
con = sqlite3.connect('Music Recommandation.db')
cur = con.cursor()
class Application(object):
    def __init__(self,master):
        self.master=master

        #frames
        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=500, bg='#ebb134')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='icon_new.png')
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=130, y=25)

        self.heading = Label(self.top, text="Music Recommendation System", font='arial 15 bold', bg='white', fg='#34baeb')
        self.heading.place(x=260, y=60)

        #  bottom frame design
        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)
        self.scroll.grid(row=0,column=1, sticky=N+S)

        self.listBox = Listbox(self.bottom, width=40, height=27)
        self.listBox.grid(row=0,column=0, padx=(40,0))
        self.listBox.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.listBox.yview)

        persons = cur.execute("select * from 'Music'").fetchall()
        count=0
        for person in persons:
            self.listBox.insert(count,str(person[0]))
            count+=1

        #buttons


        btnDetail = Button(self.bottom, text='Play', width=12, font='Sans 12 bold', command = self.play_function)
        btnDetail.grid(row=0, column=2, padx=20, pady=90, sticky=N)

    def play_function(self):
            selected_item = self.listBox.curselection()
            music = self.listBox.get(selected_item)
            music_name = music.split(".")[0]
            query = "select * from Music where Name like '%{}%'".format(music_name)
            result = cur.execute(query).fetchone()
            song = result[0]
            language = result[1]
            artist = result[2]
            genere = result[3]
            mood = result[4]
            year = result[5]
            value = result[6]
            score = result[7]

            query = "select * from Music where Language like '%{}%'".format(language)
            result1 = cur.execute(query).fetchall()
            result=list(result1)
            for results in result:
                results=list(results)
                results[7] = results[7] + 8
                query = "update Music set score = {} where Name like '%{}%'".format(results[7], results[0])
                cur.execute(query)
                con.commit()

            query = "select * from Music where Artist like '%{}%'".format(artist)
            result1 = cur.execute(query).fetchall()
            result = list(result1)
            for results in result:
                results = list(results)
                results[7]=results[7]+5
                query="update Music set score = {} where Name like '%{}%'".format(results[7],results[0])
                cur.execute(query)
                con.commit()

            query = "select * from Music where Genere like '%{}%'".format(genere)
            result1 = cur.execute(query).fetchall()
            result = list(result1)
            for results in result:
                results = list(results)
                results[7] = results[7] + 4
                query = "update Music set score = {} where Name like '%{}%'".format(results[7], results[0])
                cur.execute(query)
                con.commit()

            query = "select * from Music where Mood like '%{}%'".format(mood)
            result1 = cur.execute(query).fetchall()
            result = list(result1)
            for results in result:
                results = list(results)
                results[7] = results[7] + 2
                query = "update Music set score = {} where Name like '%{}%'".format(results[7], results[0])
                cur.execute(query)
                con.commit()

            year1=year-5
            year2=year+5

            query = "select * from Music where Year between {} and {}".format(year1,year2)
            result1 = cur.execute(query).fetchall()
            result = list(result1)
            for results in result:
                results = list(results)
                results[7] = results[7] + 1
                query = "update Music set score = {} where Name like '%{}%'".format(results[7], results[0])
                cur.execute(query)
                con.commit()

            query = "select * from Music order by Score DESC"
            cur.execute(query)
            con.commit()

            root = Toplevel()
            app = play(root)
            root.title("Music Recommadation System")
            root.geometry("650x550+350+200")
            root.resizable(False, False)
            root.mainloop()

class play(object):
    def __init__(self,master):
        self.master = master

        #frames
        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=500, bg='#ebb134')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='icon_new.png')
        self.top_image_label = Label(self.top, image=self.top_image)
        self.top_image_label.place(x=130, y=25)

        self.heading = Label(self.top, text="PlayList", font='arial 15 bold', bg='white', fg='#34baeb')
        self.heading.place(x=260, y=60)

        #  bottom frame design
        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)
        self.scroll.grid(row=0,column=1, sticky=N+S)

        self.listBox = Listbox(self.bottom, width=40, height=27)
        self.listBox.grid(row=0,column=0, padx=(40,0))
        self.listBox.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.listBox.yview)

        persons = cur.execute("select * from 'Music'").fetchall()
        count=0
        for i in range (0,10):
            self.listBox.insert(count,str(persons[i][0]))

        #buttons


        btnDetail = Button(self.bottom, text='Like', width=12, font='Sans 12 bold', command = self.like)
        btnDetail.grid(row=0, column=2, padx=20, pady=90, sticky=N)

        btnDelete = Button(self.bottom, text='Delete', width=12, font='Sans 12 bold', command = self.delete)
        btnDelete.grid(row=0, column=2, padx=20, pady=130, sticky=N)

    def delete(self):
        pass


    def like(self):
       pass

def main():
    root = Tk()
    app = Application(root)
    root.title("Music Recommadation System")
    root.geometry("650x550+350+200")
    root.resizable(False,False)
    root.mainloop()

if __name__=='__main__':
    main()
