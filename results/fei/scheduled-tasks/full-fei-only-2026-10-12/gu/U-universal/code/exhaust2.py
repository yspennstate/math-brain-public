import numpy as np, json
from exhaust import scan
from feilib import binh
for n in [3,4]:
    r=scan(n); nc=r['I']>0
    H,I,B,TC,inf=r['H'][nc],r['I'][nc],r['B'][nc],r['TC'][nc],r['inf'][nc]
    DTC=H-B
    a=H/(I+DTC); b=H/(I+TC)
    k1=int(np.argmax(a)); k2=int(np.argmax(b))
    print(n,'max H/(I+DTC)=',a.max(),'at',r['T'][nc][k1].tolist(),' max H/(I+TC)=',b.max(),'at',r['T'][nc][k2].tolist())
    # how close can H get to sum h(Inf) relative to I: max over f of (H)/(sum h) restricted to sum h >= 3 I
    sh=binh(inf).sum(-1); m=sh>=2*I
    if m.any(): print('   among sum h >= 2I: max H/sum h =', (H[m]/sh[m]).max())
