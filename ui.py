from tkinter import *


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb 

root = Tk()
root.geometry("270x250")

enter_label = Label(root, text="Enter frequency: ", fg="grey")
title = Label(root, text="Dicord Bot", bg=_from_rgb((128, 128, 255)), fg="white", width=15, height=1 )
title1 = Label(root, text="", bg=_from_rgb((128, 128, 255)), fg="white", width=15, height=1 )
title.grid(row=0, column=0)
title1.grid(row=0, column=1)
txt = Text(root, width=15, height=1, wrap=WORD)

entry_1 = Entry(root)
entry_2 = Entry(root)
enter_label.grid(row=5, column=0)
txt.grid(row=5, column= 1)
root.mainloop()
