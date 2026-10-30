from math import log2
from pathlib import Path
import json

def ent(u): return -u*log2(u) if u else 0
def phi(a,b): return ent(a)+ent(b)-ent(a+b)
def dec(a,b): return ent(a*a)+ent(b*b)-(ent((a+b)**2)+ent((a-b)**2))/2
rows=[]
for k in [4,6,8,10,12,20,40]:
    delta=2.0**(-k); s=2.0**(-k/2); p=delta**2; m=s-delta; a=1-m; t=p*a
    N=1<<k; plus=(N+(1<<(k//2)))//2-1; minus=(N-(1<<(k//2)))//2
    Bx=.5-delta/2+phi((s-delta)**2,(s+delta)**2)/(4*delta)
    Dx=1-delta+dec(s-delta,s+delta)/(4*delta)
    By=(plus+1)*phi((s-delta)**2,delta**2)+minus*phi((s+delta)**2,delta**2)
    Dy=(plus+1)*dec(s-delta,delta)+minus*dec(s+delta,delta)
    out=dict(k=k,X009=dict(B_data=Bx/(.5+delta),D_data=Dx/(.5+delta),B_selector=By/delta,D_selector=Dy/delta))
    out['B05']=dict(B_data=(p*(Bx-2*m*m)+(p-p*p)*phi(a*a,m*m)+phi((1-t)**2,p*p*m*m))/(p*(.5+delta)),D_data=(p*(Dx-4*m*m)+(p-p*p)*dec(a,m)+dec(1-t,p*m))/(p*(.5+delta)),B_control=(2*t-2*t*t+phi((1-t)**2,t*t))/t,D_control=(4*t-4*t*t+dec(1-t,t))/t,B_selector=((plus*phi((s-delta)**2,delta**2)+minus*phi((s+delta)**2,delta**2))*p+(p-p*p)*phi(a*a,delta**2)+phi((1-t)**2,p*p*delta**2))/(p*delta),D_selector=((plus*dec(s-delta,delta)+minus*dec(s+delta,delta))*p+(p-p*p)*dec(a,delta)+dec(1-t,p*delta))/(p*delta))
    rows.append(out)
print(json.dumps(rows,indent=2))
(Path(__file__).resolve().parents[1]/'out'/'PILOT_FLOATING.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
