from datetime import datetime
# import time
ti=str(time.ctime())
dt=str(datetime.today())
Da=ti[0:3]
Y=dt[0:4]
M=dt[6:7]
nM=['Jan','Feb','Mar','Apr','May','Jun','jul','Aug','Sep','Oct','Nov','Dec'][int(M)-1] or ti[4:7]
D=dt[8:10]
h=int(dt[10:13])+1
if h>12 :
    h-=12
    p_a='P.M'
else :
    p_a='A.M'
m_s=dt[14:19]
# print("%s, %s %s, %s, %d:%s %s"%(Da,nM,Y,D,h,m_s,p_a) or "FAILED TO FIND TIME AND DATE :(")
print(Da,nM,Y,D,h,m_s,p_a) or "FAILED TO FIND TIME AND DATE :()"
