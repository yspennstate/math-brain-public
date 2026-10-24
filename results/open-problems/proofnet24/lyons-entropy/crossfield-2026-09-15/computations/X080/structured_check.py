from verify import *
D=real_design();th=5/16
for m in [3,4,6,12,24]:
    ang=np.arange(m)*np.pi/m
    V0=np.vstack([np.sqrt(2/m)*np.column_stack([np.cos(ang),np.sin(ang),np.zeros(m)]),[0,0,1.]])
    V=np.vstack([np.sqrt(th)*D,np.sqrt(1-th)*V0])
    W,tau,fv,fw=geom(V);c=np.trace(W).real/3; E=W-c*I
    dm=min(c,c+tau);dp=max(c,c+tau)
    g=dm-2*np.linalg.eigvalsh(E)[-1]-np.trace(E@E).real/(3*(4-2*dp))
    print(m,np.linalg.eigvalsh(W),tau,g)
