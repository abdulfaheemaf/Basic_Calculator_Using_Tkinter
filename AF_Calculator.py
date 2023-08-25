#Calculator with GUI
import tkinter as tk
from tkinter import *
def event(value):
    symbols=['+', '-', '*', '/', '%', '**']
    global ans
    text=value.widget.cget('text')
    if text=='=':
        if scr_val.get().isdigit():
            ans=(scr_val.get())
            scr_val.set('')
        else:
            #eval()-Evaluate the given source in the context of globals and locals
            try:
                    ans=eval(scr_val.get())
            except Exception as e:
                ans='Syntax Error...!'
                expression_field.config(state="disabled")
            
        scr_val.set(ans)
    elif text=="Clear":
        scr_val.set('')
    elif text=='Del':
        val=scr_val.get()
        if val!='Syntax Error...!':
            if val!='':
                scr_val.set(val.removesuffix(val[-1]))
    elif text=='Ans':
        scr_val.set(scr_val.get()+str(ans))
    elif text=='^':
        scr_val.set(scr_val.get()+'**')
    else:
            scr_val.set(scr_val.get()+text)
    expression_field.update()



root=tk.Tk(screenName='CALCULATOR')
root.configure(background='sky blue')
root.title('Calculator')
root.geometry("335x520")
root.minsize(335, 520)
root.maxsize(335, 520)
root.wm_iconbitmap('E:/Python/Tkinter/Projects/Calci.ico')
scr_val=StringVar()
ans=0
#scr_val.set('')
expression_field=Entry(root, textvar=scr_val, font=('Tekton Pro', 35 ,'bold'))
expression_field.pack(fill=X, padx=10, pady=10)

#Creating Frame-1
frame1=Frame(root, bg='gray')
frame1.pack()
label=Label(frame1, text="AF's", font=('broadway', 30, 'bold'), bg='sky blue')
label.pack(side=LEFT)
button=Button(frame1, text='Clear', font=('Tekton Pro', 25, 'bold'), bg='orange')
button.pack(side=LEFT, padx=5, pady=5)
button.bind('<Button-1>', event)
button=Button(frame1, text='Del', font=('Tekton Pro', 25, 'bold'), bg='red', fg='orange')
button.pack(side=LEFT, padx=5, pady=5)
button.bind('<Button-1>', event)
#Creating Frame-2 
frame1=Frame(root, bg='gray', padx=5)
frame1.pack(anchor='w')
button=Button(frame1, text='9', font=('Tekton Pro', 30, 'bold'))
button.pack(side=LEFT, padx=5, pady=5)
button.bind('<Button-1>', event)
button=Button(frame1, text='8', font=('Tekton Pro', 30, 'bold'))
button.pack(side=LEFT, padx=5, pady=5)
button.bind('<Button-1>', event)
button=Button(frame1, text='7', font=('Tekton Pro', 30, 'bold'))
button.pack(side=LEFT, padx=5, pady=5)
button.bind('<Button-1>', event)
button=Button(frame1, text='*', font=('Tekton Pro', 30, 'bold'))
button.pack(side=LEFT, padx=9, pady=5)
button.bind('<Button-1>', event)
button=Button(frame1, text='/', font=('Tekton Pro', 30, 'bold'))
button.pack(side=LEFT, padx=5, pady=5)
button.bind('<Button-1>', event)
#Creating Frame-3
frame1=Frame(root, bg='gray', padx=5)
frame1.pack(anchor='w')
button=Button(frame1, text='6', font=('Tekton Pro', 30, 'bold'))
button.pack(side=LEFT, padx=5, pady=5)
button.bind('<Button-1>', event)
button=Button(frame1, text='5', font=('Tekton Pro', 30, 'bold'))
button.pack(side=LEFT, padx=5, pady=5)
button.bind('<Button-1>', event)
button=Button(frame1, text='4', font=('Tekton Pro', 30, 'bold'))
button.pack(side=LEFT, padx=5, pady=5)
button.bind('<Button-1>', event)
button=Button(frame1, text='+', font=('Tekton Pro', 30, 'bold'))
button.pack(side=LEFT, padx=5, pady=5)
button.bind('<Button-1>', event)
button=Button(frame1, text='-', font=('Tekton Pro', 30, 'bold'), padx=5)
button.pack(side=LEFT, padx=5, pady=5)
button.bind('<Button-1>', event)
#Creating Frame-4
frame1=Frame(root, bg='gray', padx=5)
frame1.pack(anchor='w')
button=Button(frame1, text='3', font=('Tekton Pro', 30, 'bold'))
button.pack(side=LEFT, padx=5, pady=5)
button.bind('<Button-1>', event)
button=Button(frame1, text='2', font=('Tekton Pro', 30, 'bold'))
button.pack(side=LEFT, padx=5, pady=5)
button.bind('<Button-1>', event)
button=Button(frame1, text='1', font=('Tekton Pro', 30, 'bold'))
button.pack(side=LEFT, padx=5, pady=5)
button.bind('<Button-1>', event)
button=Button(frame1, text='^', font=('Tekton Pro', 30, 'bold'))
button.pack(side=LEFT, padx=5, pady=5)
button.bind('<Button-1>', event)
button=Button(frame1, text='%', font=('Tekton Pro', 30, 'bold'))
button.pack(side=LEFT, padx=5, pady=5)
button.bind('<Button-1>', event)
#Creating Frame-5
frame1=Frame(root, bg='gray', padx=5)
frame1.pack(anchor='w')
button=Button(frame1, text='.', font=('Tekton Pro', 30, 'bold'), padx=9)
button.pack(side=LEFT, padx=5, pady=5)
button.bind('<Button-1>', event)
button=Button(frame1, text='0', font=('Tekton Pro', 30, 'bold'), padx=1)
button.pack(side=LEFT, padx=5, pady=5)
button.bind('<Button-1>', event)
button=Button(frame1, text='Ans', font=('Tekton Pro', 30, 'bold'))
button.pack(side=LEFT, padx=5, pady=5)
button.bind('<Button-1>', event)
button=Button(frame1, text='=', font=('Tekton Pro', 30, 'bold'), padx=11)
button.pack(side=LEFT, padx=5, pady=5)
button.bind('<Button-1>', event)
root.mainloop()
