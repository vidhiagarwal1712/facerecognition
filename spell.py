from cProfile import label
from email import header
from logging import root
from tkinter import *
from regex import P
from textblob import TextBlob
import textblob
def Correct():
    input=word1.get()
    obj=TextBlob(input)
    cw=obj.correct()
    word2.delete(0,END)
    word2.insert(10,cw)
def Clear():
    word1.delete(0,END)
    word2.delete(0,END)
if __name__=='__main__':
    root=Tk()
    root.configure(background='lightgreen')
    root.geometry('500x300')
    root.title('Spellcheck App')
    Header=Label(root,text='WELCOME TO THE SPELLCHECK APP',fg='black',bg='white')
    Header.grid(row=0,column=1)
    L1=Label(root,text='Input Word',fg='black',bg='white')
    L1.grid(row=1,column=1,pady=10)
    word1=Entry()
    L2=Label(root,text='Corrected Word',fg='black',bg='white')
    L2.grid(row=3,column=1,pady=10)
    word2=Entry()
    word1.grid(row=1,column=2)
    word2.grid(row=3,column=2)
    Button1=Button(root,text='Correct',bg='white',fg='black',command=Correct)
    Button1.grid(row=2,column=2,pady=10)
    Button2=Button(root,text='Clear All',bg='white',fg='black',command=Clear)
    Button2.grid(row=4,column=2,pady=10)
    root.mainloop() 