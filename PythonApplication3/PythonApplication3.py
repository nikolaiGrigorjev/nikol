from tkinter import *
from math import *

def lahenda():
	if (a.get()!=""and b.get()!=""and c.get()!=""):
		a_=int(a.get())
		b_=int(b.get())
		c_=int(c.get())
		D=b_*b_-4*a_*c_
		if D>0:
			x1_=(-1*b_+sqrt(D))/(2*a_)
			x2_=(-1*b_+sqrt(D))/(2*a_)
			t=f"X1={x1_},\nX2={x2_}"
		elif D==0:
			x1_=(-1*b_)/(2*a_)
			t=f"X1={x1_}"
		else:
			t="нету корней"
	vastus.configure(text=f"D={D}\n{t}")
	a.configure(bg="lightblue")
	b.configure(bg="lightblue")
	c.configure(bg="lightblue")



	
	





okno=Tk()
okno.title("Квадратное уравнение")
okno.geometry("1280x960")
lbl=Label(okno,text="Решение квадратного уравнения",font="Calibri 20",fg="purple",bg="orange")
lbl.pack()


a=Entry(okno,font="Calibri 15",fg="green",bg="lightblue",width=5)
a.pack(side=LEFT,padx=30)
x2=Label(okno,text="x**2+",font="Calibri 17",fg="purple")
x2.pack(side=LEFT,padx=30)
b=Entry(okno,font="Calibri 15",fg="green",bg="lightblue",width=5)
b.pack(side=LEFT,padx=30)
y2=Label(okno,text="x+",font="Calibri 17",fg="purple")
y2.pack(side=LEFT,padx=30)
c=Entry(okno,font="Calibri 15",fg="green",bg="lightblue",width=5)
c.pack(side=LEFT,padx=30)
q2=Label(okno,text="=0",font="Calibri 17",fg="purple")
q2.pack(side=LEFT,padx=30)
btn=Button(okno,text="Решения",font="Calibri 20",bg="yellow",command=lahenda)
btn.pack(side=LEFT,pady=20)
vastus=Label(okno,text="Ответ",font="Calibri 30",fg="blue",bg="red")
vastus.pack(side=BOTTOM)



okno.mainloop()





