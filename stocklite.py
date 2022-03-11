import easyquotation
from notify_run import Notify
import time
from tkinter.tix import *

notify=Notify()
notify.endpoint='https://notify.run/j9RQeKLYox4EPYkS'
l=[]

def ss(i):
  if l[13*i+2]['text']=='⏵':
    l[13*i+2]['text']='⏸'
    if l[13*i].get()!=c[2*i]:
      l[13*i+11]=0
      l[13*i+12]=0
      l[13*i+8]=0
      l[13*i+6]=0
      l[13*i+3].text.insert(END,'\n'+l[13*i].get()+'\n\n\n')
      l[13*i+4].text.insert(END,'\n'+l[13*i].get()+'\n\n\n')
      with open(f"log{i+1}.txt",'a') as f:
        f.write('\n'+l[13*i].get()+'\n\n\n')
      with open(f"dump{i+1}.txt",'a') as f:
        f.write('\n'+l[13*i].get()+'\n\n\n')
    c[2*i]=l[13*i].get()
    c[2*i+1]=l[13*i+1].get()
    with open('cfg.txt','w') as f:
      f.write(','.join(c))
    l[13*i+3].text.tag_config('g',foreground='green3')
    l[13*i+3].text.tag_config('r',foreground='red')
    l[13*i+3].text.tag_config('b',foreground='blue')
    l[13*i+4].text.tag_config('g',foreground='green3')
    l[13*i+4].text.tag_config('r',foreground='red')
    l[13*i+4].text.tag_config('b',foreground='blue')
    log(i)
  else:
    l[13*i+2]['text']='⏵'
    r.after_cancel(l[13*i+5])

def log(i):
  q=easyquotation.use('sina')
  s=q.stocks(c[2*i])
  d=s[c[2*i]]
  v=d['turnover']-int(l[13*i+6])
  n=f"ask5: {d['ask5']} volume: {d['ask5_volume']}\nask4: {d['ask4']} volume: {d['ask4_volume']}\nask3: {d['ask3']} volume: {d['ask3_volume']}\nask2: {d['ask2']} volume: {d['ask2_volume']}\nask1: {d['ask1']} volume: {d['ask1_volume']}\n"
  n1=f"now: {d['now']} dealvolume: {v} {round((d['ask1_volume']+d['ask2_volume']+d['ask3_volume']+d['ask4_volume']+d['ask5_volume'])/(d['bid1_volume']+d['bid2_volume']+d['bid3_volume']+d['bid4_volume']+d['bid5_volume']),1)}\n"
  n2=f"bid1: {d['bid1']} volume: {d['bid1_volume']}\nbid2: {d['bid2']} volume: {d['bid2_volume']}\nbid3: {d['bid3']} volume: {d['bid3_volume']}\nbid4: {d['bid4']} volume: {d['bid4_volume']}\nbid5: {d['bid5']} volume: {d['bid5_volume']}\n"
  n3=f"date: {d['date']} time: {d['time']}\n"
  if v>0:
    if v>int(c[2*i+1]) and l[13*i+8]>0:
      notify.send(f"now: {d['now']} dealvolume: {v}")
      l[13*i+3].text.insert(END,l[13*i+7])
      f=open(f"log{i+1}.txt",'a')
      f.write(l[13*i+7])
      if time.gmtime().tm_hour+8>9 or time.gmtime().tm_min>45:
        if d['now']>l[13*i+8]:
          l[13*i+11]+=v
        elif d['now']<l[13*i+8]:
          l[13*i+12]+=v
        elif d['now']==l[13*i+8]==l[13*i+9]:
          l[13*i+11]+=v
        elif d['now']==l[13*i+8]==l[13*i+10]:
          l[13*i+12]+=v
        l[13*i+3].text.insert(END,n,'g',n1,'',n2,'r',n3+f"accask: {l[13*i+11]} accbid: {l[13*i+12]}\n\n",'b')
        f.write(n+n1+n2+n3+f"accask: {l[13*i+11]} accbid: {l[13*i+12]}\n\n")
      else:
        l[13*i+3].text.insert(END,n,'g',n1,'',n2,'r',n3+'\n','b')
        f.write(n+n1+n2+n3+'\n')
      f.close()
    l[13*i+4].text.insert(END,n,'g',n1,'',n2,'r',n3+'\n','b')
    with open(f"dump{i+1}.txt",'a') as f:
      f.write(n+n1+n2+n3+'\n')
    l[13*i+6]=d['turnover']
    l[13*i+7]=n+n1+n2+n3+'\n'
    l[13*i+8]=d['now']
    l[13*i+9]=d['ask1']
    l[13*i+10]=d['bid1']
  l[13*i+5]=r.after(1000,lambda:log(i))

r=Tk()
r.title('stock')
win=ScrolledWindow(r)
win.pack()
w=win.window
w.rowconfigure([0,1],weight=0,minsize=35)

Label(w,text='stock').grid(row=0,sticky='w',padx=(25,0))
Label(w,text='limit').grid(row=1,sticky='w',padx=(27,0))
for i in range(5):
  e=Entry(w)
  l.append(e)
  e.grid(row=0,column=i)
  e1=Entry(w)
  l.append(e1)
  e1.grid(row=1,column=i)
  with open('cfg.txt') as f:
    c=f.read().split(',')
    e.insert(0,c[2*i])
    e1.insert(0,c[2*i+1])
  b=Button(w,text='⏵',command=lambda i=i :ss(i))
  l.append(b)
  b.grid(row=0,rowspan=2,column=i,sticky='e',padx=(0,40))
  t=ScrolledText(w,height=(r.winfo_screenheight()-136)/2,width=r.winfo_screenwidth()/5-1)
  l.append(t)
  t.grid(row=2,column=i)
  t1=ScrolledText(w,height=(r.winfo_screenheight()-136)/2,width=r.winfo_screenwidth()/5-1)
  l.append(t1)
  t1.grid(row=3,column=i)
  l.append(0)
  l.append(0)
  l.append(0)
  l.append(0)
  l.append(0)
  l.append(0)
  l.append(0)
  l.append(0)

r.mainloop()