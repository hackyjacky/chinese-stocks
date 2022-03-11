import subprocess
import easyquotation
from notify_run import Notify
import time
subprocess.call('',shell=True)
notify=Notify()
notify.endpoint='https://notify.run/j9RQeKLYox4EPYkS'
vlimit=int(open('limit.txt').read())
old=0
previous=''
oldnow=0
oldask=0
accask=0
oldbid=0
accbid=0
while True:
  quotation=easyquotation.use('sina')
  stock=quotation.stocks('600352')
  data=stock['600352']
  vol=data['turnover']-old
  current='ask5: '+str(data['ask5'])+' volume: '+str(data['ask5_volume'])+'\nask4: '+str(data['ask4'])+' volume: '+str(data['ask4_volume'])+'\nask3: '+str(data['ask3'])+' volume: '+str(data['ask3_volume'])+'\nask2: '+str(data['ask2'])+' volume: '+str(data['ask2_volume'])+'\nask1: '+str(data['ask1'])+' volume: '+str(data['ask1_volume'])+'\nnow: '+str(data['now'])+' dealvolume: '+str(vol)+'\nbid1: '+str(data['bid1'])+' volume: '+str(data['bid1_volume'])+'\nbid2: '+str(data['bid2'])+' volume: '+str(data['bid2_volume'])+'\nbid3: '+str(data['bid3'])+' volume: '+str(data['bid3_volume'])+'\nbid4: '+str(data['bid4'])+' volume: '+str(data['bid4_volume'])+'\nbid5: '+str(data['bid5'])+' volume: '+str(data['bid5_volume'])+'\ndate: '+str(data['date'])+' time: '+str(data['time'])+'\n'
  if vol==0:
    continue
  if vol>vlimit and oldnow>0:
    notify.send('now: '+str(data['now'])+' dealvolume: '+str(vol))
    f=open('oldlog.txt','a')
    f.write(previous)
    if time.gmtime().tm_hour+8>9 or time.gmtime().tm_min>45:
      if data['now']>oldnow:
        accask=accask+vol
      elif data['now']<oldnow:
        accbid=accbid+vol
      elif data['now']==oldnow==oldask:
        accask=accask+vol
      elif data['now']==oldnow==oldbid:
        accbid=accbid+vol
      f.write(current+'accask: '+str(accask)+' accbid: '+str(accbid)+'\n\n')
    else:
      f.write(current+'\n')
    f.close()
  print('\033[1;32;40mask5:',data['ask5'],'volume:',data['ask5_volume'],'\nask4:',data['ask4'],'volume:',data['ask4_volume'],'\nask3:',data['ask3'],'volume:',data['ask3_volume'],'\nask2:',data['ask2'],'volume:',data['ask2_volume'],'\nask1:',data['ask1'],'volume:',data['ask1_volume'],'\n\033[1;37;40mnow:',data['now'],'dealvolume:',vol,'\n\033[1;31;40mbid1:',data['bid1'],'volume:',data['bid1_volume'],'\nbid2:',data['bid2'],'volume:',data['bid2_volume'],'\nbid3:',data['bid3'],'volume:',data['bid3_volume'],'\nbid4:',data['bid4'],'volume:',data['bid4_volume'],'\nbid5:',data['bid5'],'volume:',data['bid5_volume'],'\n\033[1;33;40mdate:',data['date'],'time:',data['time'],'\n')
  f=open('olddump.txt','a')
  f.write(current+'\n')
  f.close()
  previous=current+'\n'
  old=data['turnover']
  oldnow=data['now']
  oldask=data['ask1']
  oldbid=data['bid1']
  time.sleep(1)