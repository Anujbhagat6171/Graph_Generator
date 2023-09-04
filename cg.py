from tkinter import *
from tkinter.messagebox import *
import matplotlib.pyplot as plt 


splash = Tk()
splash.after(4000, splash.destroy)
splash.wm_attributes('-fullscreen','true')
msg = Label(splash,text="Chart Generatr\nby \nkamal sir",font=('Calibri',100,'bold'), fg='red')
msg.pack()
splash.mainloop()


root = Tk()
root.geometry("500x500+400+100")
root.title("Chart Generator")

def f1():
	name = ent_name.get()
	phy = int(ent_phy.get())
	chem = int(ent_chem.get())
	maths = int(ent_maths.get())
	subject = ['phy','chem','maths']
	marks = [phy,chem,maths]
	plt.plot(subject,marks,linewidth=4)
	plt.xlabel("Subjects")
	plt.ylabel("Marks")
	plt.title(name.title() + "'s performance")
	plt.show()

def f2():
	name = ent_name.get()
	phy = int(ent_phy.get())
	chem = int(ent_chem.get())
	maths = int(ent_maths.get())
	subject = ['phy','chem','maths']
	marks = [phy,chem,maths]
	plt.bar(subject,marks,linewidth=4)
	plt.xlabel("Subjects")
	plt.ylabel("Marks")
	plt.title(name.title() + "'s performance")
	plt.show()
f = ('Calibri', 20, 'bold')
lbl_name = Label(root,text="name", font=f)
ent_name = Entry(root,bd=5, font=f)
lbl_phy = Label(root,text="phy",font=f)
ent_phy = Entry(root,bd=5,font=f)
lbl_chem = Label(root,text="chem",font=f)
ent_chem = Entry(root,bd=5,font=f)
lbl_maths = Label(root,text="maths",font=f)
ent_maths = Entry(root,bd=5,font=f)


btn_line = Button(root,text="line chart",width=10, font=f, command=f1)
btn_bar = Button(root,text="Bar chart",width=10,font=f,command=f2)

lbl_name.pack()
ent_name.pack()
lbl_phy.pack()
ent_phy.pack()
lbl_chem.pack()
ent_chem.pack()
lbl_maths.pack()
ent_maths.pack()
btn_line.pack()
btn_bar.pack()

def f3():
	if askokcancel("Quit", "do u want to exit"):
		root.destroy()

root.protocol("WM_DELETE_WINDOW",f3)
root.mainloop()




	