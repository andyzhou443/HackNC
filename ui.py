from tkinter import *


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb 

def save():
    a = entry_1.get()
    with open('freq.txt', 'w') as file_object:
        file_object.write(a)

if __name__ == '__main__':

    root = Tk()
    root.geometry("270x250")

    enter_label = Label(root, text="Enter frequency: ", fg="grey")
    title = Label(root, text="Dicord Bot", bg=_from_rgb((128, 128, 255)), fg="white", width=15, height=1 )
    title1 = Label(root, text="", bg=_from_rgb((128, 128, 255)), fg="white", width=15, height=1 )
    title.grid(row=0, column=0)
    title1.grid(row=0, column=1)

    entry_1 = Entry(root, width=15)
    enter_label.grid(row=5, column=0)
    entry_1.grid(row=5, column= 1)

    tune_in = Button(root, text="Tune In", command=save)
    tune_in.grid(row=6, column=1)
    root.mainloop()

try:
    f = open( "freq.txt", "r", encoding="utf8" )
    lines = f.readlines()
    f.close() 
except ValueError:
    ...

