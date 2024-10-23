from tkinter import *
def meow(num):
    global equation_text
    equation_text += str(num)
    equation_label.set(equation_text)

def equal():
    global equation_text
    total = str(eval(equation_text))
    equation_label.set(total)
    equation_text =total
def clear():
    global equation_text
    equation_label.set('')
    equation_text = ""
window = Tk()
window.geometry('700x700')
equation_text =''

equation_label = StringVar()
label = Label(window, textvariable=equation_label, font=('consolas',20), bg="white", width=24, height=2)
label.pack()
button =Button(window,text=1,command=lambda : meow(1),width=5,height=3,borderwidth=3,)
button.place(x=200,y=100)
button_1 =Button(window,text=2,command=lambda : meow(2),width=5,height=3,borderwidth=3,)
button_1.place(x=260,y=100)
button_2=Button(window,text=3,command=lambda :meow(3),width=5,height=3,borderwidth=3,)
button_2.place(x=320,y=100)
button_plus = Button(window,text='+',command=lambda: meow('+'),width=5,height=3,borderwidth=3,)
button_plus.place(x=380,y=100)



button_3 =Button(window,text=4,command=lambda :meow(4),width=5,height=3,borderwidth=3,)
button_3.place(x=200,y=170)
button_4 =Button(window,text=5,command=lambda :meow(5),width=5,height=3,borderwidth=3,)
button_4.place(x=260,y=170)
button_5=Button(window,text=6,command=lambda :meow(6),width=5,height=3,borderwidth=3,)
button_5.place(x=320,y=170)
button_multi = Button(window,text='*',command=lambda :meow('*'),width=5,height=3,borderwidth=3,)
button_multi.place(x=380,y=170)

button_6 =Button(window,text=7,command=lambda :meow(7),width=5,height=3,borderwidth=3,)
button_6.place(x=200,y=240)
button_7 =Button(window,text=8,command=lambda :meow(8),width=5,height=3,borderwidth=3,)
button_7.place(x=260,y=240)
button_8 =Button(window,text=9,command=lambda :meow(9),width=5,height=3,borderwidth=3,)
button_8.place(x=320,y=240)
button_divide =Button(window,text='/',command=lambda :meow('/'),width=5,height=3,borderwidth=3,)
button_divide.place(x=380,y=240)


button_0 =Button(window,text=0,command=lambda :meow(0),width=5,height=3,borderwidth=3,)
button_0.place(x=200,y=310)
button_dot =Button(window,text='.', command=lambda :meow('.'),width=5,height=3,borderwidth=3,)
button_dot.place(x=260,y=310)
button_equal =Button(window,text='=',command= equal,width=5,height=3,borderwidth=3,)
button_equal.place(x=320,y=310)
button_minus =Button(window,text='-',command=lambda :meow('-'),width=5,height=3,borderwidth=3,)
button_minus.place(x=380,y=310)

button_clear =Button(window,text='C',command= clear,width=5,height=3,borderwidth=3,)
button_clear.place(x=260,y=380)
window.mainloop()