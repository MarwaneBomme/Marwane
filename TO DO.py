from tkinter import * 
from tkinter import ttk

class todo:
    def __init__(self, window):
        self.window = window
        self.window.title('ME MADE IT')
        self.window.geometry('800x400')
        self.window.configure(bg='black')
        
        self.Label = Label(self.window, text='TASK APP', font='Helvetica, 25 bold', width=10, bd=4, bg='orange', fg='black')
        self.Label.pack(side='top', fill=BOTH)

        self.Label2 = Label(self.window, text='ADD TASK', font='ariel, 22 bold', width=10, bd=4, bg='orange', fg='black')
        self.Label2.place(x=20, y=54)

        self.Label3 = Label(self.window, text='TASK ', font='ariel, 22 bold', width=10, bd=4, bg='orange', fg='black')
        self.Label3.place(x=500, y=52)

        self.main_text = Listbox(self.window, height=9, width=24, font='ariel, 23 italic bold', bd=4, bg='grey')
        self.main_text.place(x=380, y=100)

        self.text = Text(self.window, bd=4, height=1, width=16, font='ariel, 15 bold',bg='grey')
        self.text.place(x=20, y=110)

        # ADD TASK FUNCTION #

        def add():
           content = self.text.get(1.0, END)
           self.main_text.insert(END, content)
           with open('dataa.txt', 'a') as file:
                file.write(content)
                file.seek(0)
                file.close()
           self.text.delete(1.0, END)

        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open ('dataa.txt', 'r+') as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)    
        
        with open('dataa.txt','r') as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)
            file.close()   

        self.button = Button(self.window, text='ADD', font='ariel, 20 bold', 
                     width=10, bd=4, bg='orange', fg='black',command=add)
        self.button.place(x=30, y=180)

        self.button2 = Button(self.window, text='DELETE', font='ariel, 20 bold', 
                     width=10, bd=4, bg='orange', fg='black',command=delete)
        self.button2.place(x=30, y=280)                  
     
def main():
    window = Tk()
    ui = todo(window)
    window.mainloop()

if __name__ == "__main__":
    main()