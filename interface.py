#!/usr/bin/python3

from tkinter import *
from piece import Piece


class MyFirstGUI:
   def __init__(self, root):
      self.root = root
      root.title("Ara Bul Kütüphane")
      self.piece = Piece()

      self.b1 = Button(root, text='Tüm Kataloğu Göster', command=(lambda: self.show()))
      self.b1.pack(side=LEFT, padx=5, pady=5)
      self.b2 = Button(root, text='Ekle', command=(lambda: self.add()))
      self.b2.pack(side=LEFT, padx=5, pady=5)
      self.b3 = Button(root, text='Ara', command=(lambda: self.search()))
      self.b3.pack(side=LEFT, padx=5, pady=5)
      self.b4 = Button(root, text='Çık', command=root.quit)
      self.b4.pack(side=LEFT, padx=5, pady=5)

      self.b6 = Button(root, text='Ara', command=(lambda: self.get_result()))

      self.row = Frame(root)
      self.lab = Label(self.row, width=15, text="Yazar", anchor='w')
      self.ent = Entry(self.row)
      self.row1 = Frame(root)
      self.lab1 = Label(self.row1, width=15, text="Eser Adı", anchor='w')
      self.ent1 = Entry(self.row1)
      self.row2 = Frame(root)
      self.lab2 = Label(self.row2, width=15, text="Tarih", anchor='w')
      self.ent2 = Entry(self.row2)
      self.b5 = Button(root, text='Ekle', command=(lambda: self.save()))

      self.row3 = Frame(root)
      self.lab3 = Label(self.row3, width=15, text="Arama Sözcüğü ", anchor='w')
      self.ent3 = Entry(self.row3)

      self.listbox = Listbox(root, width=50, height=20)
      self.listbox2 = Listbox(root, width=50, height=20)

      OPTIONS = [
         "Eser Adı",
         "Yazar",
         "Tarih"
      ]
      self.variable = StringVar(root)
      self.variable.set(OPTIONS[0])
      self.w = OptionMenu(root, self.variable, *OPTIONS)

   def close_all(self):
      self.ent.pack_forget()
      self.ent1.pack_forget()
      self.ent2.pack_forget()
      self.ent3.pack_forget()
      self.row.pack_forget()
      self.row1.pack_forget()
      self.row2.pack_forget()
      self.row3.pack_forget()
      self.lab.pack_forget()
      self.lab1.pack_forget()
      self.lab2.pack_forget()
      self.lab3.pack_forget()
      self.b5.pack_forget()
      self.b6.pack_forget()
      self.listbox.pack_forget()
      self.listbox2.pack_forget()
      self.w.pack_forget()
      self.listbox.delete(0, 'end')
      self.listbox2.delete(0, 'end')
      self.ent3.delete(0, 'end')

   def add(self):
      self.close_all()
      self.row.pack(side=TOP, fill=X, padx=5, pady=5)
      self.lab.pack(side=LEFT)
      self.ent.pack(side=RIGHT, expand=YES, fill=X)

      self.row1.pack(side=TOP, fill=X, padx=5, pady=5)
      self.lab1.pack(side=LEFT)
      self.ent1.pack(side=RIGHT, expand=YES, fill=X)

      self.row2.pack(side=TOP, fill=X, padx=5, pady=5)
      self.lab2.pack(side=LEFT)
      self.ent2.pack(side=RIGHT, expand=YES, fill=X)

      self.b5.pack(side=LEFT, padx=5, pady=5)

   def save(self):
      self.piece.add(self.ent1.get(), self.ent.get(), self.ent2.get())
      self.ent.delete(0,'end')
      self.ent1.delete(0,'end')
      self.ent2.delete(0,'end')

   def search(self):
      self.close_all()
      self.row3.pack(side=TOP, fill=X, padx=5, pady=5)
      self.lab3.pack(side=LEFT)
      self.ent3.pack(side=RIGHT, expand=YES, fill=X)
      self.w.pack(fill =X)
      self.b6.pack(side=LEFT, padx=5, pady=5)

   def type_number(self, type):
      return {
         'Eser Adı':"1",
         'Yazar':"2",
         'Tarih':"3"
      }[type]

   def get_result(self):
      self.listbox2.delete(0, 'end')
      if(self.ent3.get()):
         print(self.variable.get())
         result = self.piece.search(self.ent3.get(), self.type_number(self.variable.get()))
         self.listbox2.pack()
         for item in result:
            self.listbox2.insert(END, item)

   def show(self):
      self.close_all(),
      self.listbox.pack()
      for item in self.piece.all():
         self.listbox.insert(END, item)

root = Tk()

my_gui = MyFirstGUI(root)

root.mainloop()

