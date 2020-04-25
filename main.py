from tkinter import *

window = Tk()
window.title("Calculator")
label1 = Label(window, text="Label 1")
label2 = Label(window, text="Label 2")

def clicked():
    label1.configure(text=str())

def create_button(char):
    return Button(window, text=char,highlightbackground="orange",
                highlightthickness=30, fg='red', value=int(char), command=lambda: press(int(char))))

#def create_buttons_layout():
    #lst = []
    #for char in '0123456789':
        #lst.append(create_button(char))
    #return lst





label1.grid(column=0, row=0)
label2.grid(column=0, row=1)

create_buttons_layout()



