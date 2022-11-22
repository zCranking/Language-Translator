from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from googletrans import Translator, LANGUAGES

list = list(LANGUAGES.values())

language1 = ""
language2 = ""
text = ""

def Translate():
    global language1, language2, text
    language1 = combobox1.get()
    language2 = combobox2.get()
    text = text.get()

translate = translate()

translated = try: translate(text, 0, END, language1, language2)

insert(END, translated.text)
print("try again")
button = (command = Translate())

