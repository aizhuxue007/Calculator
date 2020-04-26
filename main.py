from tkinter import *  # the GUI package

# set up a display window
window = Tk()
window.title("Calculator")

# set the size of GUI window
window.geometry("300x400")

display_string = ''


# Every time a button is clicked, it adds it into an
# expression string and prints the value to console
# check out the console when you press the buttons
# not sure how to display
def clicked(char):
    global display_string
    if char == '=':
        equation.set(str(eval(display_string)))
        display_string = ''
    elif char == 'c':
        display_string = ''
        equation.set(display_string)
    else:
        display_string = display_string + str(char)
        print(display_string)
        equation.set(display_string)


# A class is a blueprint for an object
class Buttons:
    # list of Button objects
    buttons = []

    def __init__(self, gui):
        self.gui = gui

    def create_button(self, char):
        display_text = ' ' + char + ' '
        return Button(self.gui, text=display_text,
                      fg='black', command=lambda: clicked(char))

    # create all the buttons on screen
    def create_buttons(self):
        for char in '1234567890+-*/=c.()':
            self.buttons.append(self.create_button(char))
        self.display_layout()

    def display_layout(self):
        layout_row = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 2, 3, 4, 5, 5, 5, 6, 6, 6]
        layout_column = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 3, 3, 3, 3, 2, 1, 0, 1, 2]
        index = 0
        for button in self.buttons:
            button.grid(row=layout_row[index],
                        column=layout_column[index])
            index += 1


equation = StringVar()
# the text display
text_field = Entry(window, textvariable=equation)

# grid method is used for placing widgets
# at respective positions
# in a table like structure
text_field.grid(columnspan=4)

buttons = Buttons(window)

buttons.create_buttons()

window.mainloop()
