import requests
import customtkinter
from threading import  *
import tkinter as tk
quotes = []
quotes_number=0
def preload():
    global quotes

    for x in range(10):

        v = requests.get('http://api.quotable.io/random').json()
        cont = v["content"]
        b = v['author']
        quote = cont+"\n\n"+b
        quotes.append(quote)
preload()



def c():
    global lbl
    global quotes
    global quotes_number
    lbl.config(text=quotes[quotes_number])
    quotes_number = quotes_number+1
    if quotes[quotes_number] == quotes[-3]:
        thread = Thread(target=preload)
        thread.start()


m = customtkinter.CTk()
lbl = tk.Label(master=m,text='click on button to generate')
lbl.pack()
but = customtkinter.CTkButton(m,text='c',command=c).pack()

m.mainloop()