import tkinter as tk

r=tk.Tk()

def cl(i):
  with open(f'log{i+1}.txt','w') as f:
    f.write('')

def cd(i):
  with open(f'dump{i+1}.txt','w') as f:
    f.write('')

for i in range(5):
  b=tk.Button(text='log',command=lambda i=i :cl(i))
  b.grid(row=0,column=i)
  b1=tk.Button(text='dump',command=lambda i=i :cd(i))
  b1.grid(row=1,column=i)

r.mainloop()