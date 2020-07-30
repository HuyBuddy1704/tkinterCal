from tkinter import *
from tkinter import StringVar
from tkinter import messagebox
import pyperclip
def clearinputoutput():
	a.set('')
	b.set('')
	c.set('')
def cong():
	So1 = float(a.get())
	So2 = float(b.get())
	if int(So1) != So1 or int(So2) != So2:
		c.set(round(float(So1)+float(So2),1))
	else:
		c.set(int(So1)+int(So2))
def tru():
	So1 = float(a.get())
	So2 = float(b.get())
	if int(So1) != So1 or int(So2) != So2:
		c.set(round(float(So1)-float(So2),1))
	else:
		c.set(int(So1)-int(So2))
def nhan():
	So1 = float(a.get())
	So2 = float(b.get())
	if int(So1) != So1 or int(So2) != So2:
		c.set(round(float(So1)*float(So2),1))
	else:
		c.set(int(So1)*int(So2))
def chia():
	So1 = float(a.get())
	So2 = float(b.get())
	if So2 == 0:
		messagebox.showinfo('Lỗi!','Can\'t devide to 0')
	else:
		if int(So1) != So1 or int(So2) != So2:
			c.set(round(float(So1)/float(So2),1))
		else:
			c.set(int(So1)/int(So2))
def copyresult():
	tmp = c.get()
	pyperclip.copy(tmp)
	tmp1 = pyperclip.paste()
maytinh = Tk()
a = StringVar()
b = StringVar()
c = StringVar()
maytinh.title('Basic Calculator')
maytinh.resizable(height = False,width = False)
maytinh.minsize(height = 150,width = 250)
Label(maytinh,text = 'BASIC CALCULATOR',font = ('Consolas',16),fg = 'Black',bg = 'White',justify = CENTER).grid(row = 0,columnspan = 3)
FrameButton = Frame(maytinh)
Button(FrameButton,text = '+',command = cong,width = 5).pack(side = TOP,fill = X)
Button(FrameButton,text = '-',command = tru,width = 5).pack(side = TOP,fill = X)
Button(FrameButton,text = 'x',command = nhan,width = 5).pack(side = TOP,fill = X)
Button(FrameButton,text = '/',command = chia,width = 5).pack(side = TOP,fill = X)
FrameButton.grid(row = 1,column = 0,rowspan = 4)
Label(maytinh,text = 'Số thứ nhất:').grid(row = 1,column = 1)
Entry(maytinh,width = 25,textvariable = a).grid(row = 1,column = 2)
Label(maytinh,text = 'Số thứ hai:').grid(row = 2,column = 1)
Entry(maytinh,width = 25,textvariable = b).grid(row = 2,column = 2)
Label(maytinh,text = 'Kết quả: ').grid(row = 3,column = 1)
Entry(maytinh,width = 25,textvariable = c).grid(row = 3,column = 2)
InputOutput = Frame()
Button(InputOutput,text = 'Exit',command = maytinh.quit).pack(side=LEFT)
Button(InputOutput,text = 'Clear I/O',command = clearinputoutput).pack(side = LEFT)
Button(InputOutput,text = 'Copy Result',command = copyresult).pack(side = LEFT)
InputOutput.grid(row = 4,column = 2)
maytinh.mainloop()