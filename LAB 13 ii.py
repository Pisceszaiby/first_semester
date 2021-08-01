from tkinter import * #For GUI interface
window=Tk()
window.title("Calculator") #Calculator will be the window title
window.geometry('250x170')
window.maxsize(240,160) #Maximum size of window
e=Entry(window,width=37,borderwidth=5) #will be shown at the top spanning 4 columns
e.grid(columnspan=4)
for row, text in enumerate(("   Cls    ", "  7  ", "  4  ","  1  ", "  0  ")):
    button = Button(window, text=text)
    button.grid(row=row+1, column=0, sticky="ew") #All the buttons of column 0
for row, text in enumerate(("   Back    ", "8", "5","2", ".")):
    button = Button(window, text=text)
    button.grid(row=row+1, column=1, sticky="ew")#All the buttons of column 1
for row, text in enumerate(("             ", "9", "6","3", "=")):
    button = Button(window, text=text)
    button.grid(row=row+1, column=2, sticky="ew")#All the buttons of column 2
for row, text in enumerate(("   Close   ", "/", "*","-", "+")):
    button =Button(window, text=text,width=10)
    button.grid(row=row+1, column=3, sticky="ew")#All the buttons of column 3
window.mainloop()
