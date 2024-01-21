import tkinter as tk
import tkinter.filedialog as tfd

PATH=r"C:\Users\Nikita-Wlad\Desktop\Python\notes\\"

#functions
def read():
    filename=tfd.askopenfilename()
    with open(file=filename,mode="r",encoding="utf-8") as file:
        contentText.insert(1.0,file.read())

def new_file():
    contentText.delete(1.0,"end")

def save():
    filename=tfd.asksaveasfilename()
    with open(file=filename,mode="w",encoding="utf-8") as file:
        content=contentText.get(1.0,"end")
        file.write(content)

#end functions

#window
window=tk.Tk()
window.title("Notes")
window.geometry("400x400")

#textfield
contentText=tk.Text(window,wrap="word")
contentText.place(x=0,y=0,relwidth=1,relheight=1)

#mainmenu
mainmenu=tk.Menu(window)
window.configure(menu=mainmenu)

#filemenu
filemenu=tk.Menu(mainmenu)
mainmenu.add_cascade(label="File",menu=filemenu)
newfileicon=tk.PhotoImage(file=PATH+"new_file.gif")
openfileicon=tk.PhotoImage(file=PATH+"open_file.gif")
savefileicon=tk.PhotoImage(file=PATH+"save_file.gif")
filemenu.add_command(label="New File",image=newfileicon, compound="left",command=new_file)
filemenu.add_command(label="Open File",image=openfileicon,compound="left",command=read)
filemenu.add_command(label="Save",image=savefileicon,compound="left",command=save)
filemenu.add_command(label="Save as",image=savefileicon,compound="left",command=save)
































































































































































































































































































window.mainloop()