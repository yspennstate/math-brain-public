import numpy as np
from itertools import combinations

TRI=list(combinations(range(4),3))
PAIR=list(combinations(range(4),2))

def quantities(r, phases):
    a,b,c=phases
    Q=np.array([[0,1,1,1],[1,0,np.exp(1j*a),np.exp(1j*b)],
                [1,np.exp(-1j*a),0,np.exp(1j*c)],
                [1,np.exp(-1j*b),np.exp(-1j*c),0]],complex)
    L=np.eye(4)+r*Q
    if np.linalg.eigvalsh(L)[0] <= 0: return None
    K=np.eye(4)-np.linalg.inv(np.eye(4)+L)
    R=K-.5*np.eye(4)
    dd=np.array([np.linalg.det(L[np.ix_(t,t)]).real for t in TRI])
    p=-np.log1p(-r*r)
    bts=-np.log(dd)-3*p
    w4=-np.log(np.linalg.det(L).real)-6*p-bts.sum()
    bp=np.array([p+.5*sum(bts[j] for j,t in enumerate(TRI) if set(e)<=set(t))+.25*w4 for e in PAIR])
    et=bts+.5*w4
    r3=[]
    for t,ee in zip(TRI,et):
        ev=np.linalg.eigvalsh(ee*R[np.ix_(t,t)])
        M=np.array([[0,ev[2],ev[1]],[ev[2],0,ev[0]],[ev[1],ev[0],0]])
        r3.append(np.linalg.eigvalsh(M)[-1])
    ev=np.linalg.eigvalsh(R)
    M=np.zeros((4,4))
    off=[]
    for i,j in PAIR:
        vv=w4*np.prod([ev[k] for k in range(4) if k not in (i,j)])
        M[i,j]=M[j,i]=vv
        off.append(-vv)
    r4=max(np.linalg.eigvalsh(M)[-1],max(off))
    residual=sum(r3)-min(r3)+r4
    t=min(bp)
    v=np.trace(K-K@K).real
    budget=t*v+sum(bp-t)/4
    return dict(t=t,residual=residual,ratio=residual/t,budget=budget,
                pair=bp.tolist(),eta=et.tolist(),w4=w4,r3=r3,r4=r4,
                minL=np.linalg.eigvalsh(L)[0],phase=phases)

if __name__=='__main__':
    rng=np.random.default_rng(79)
    for r in [.2,.3,.4,.5,.6,.7,.8]:
        for rad in [0,.2,.5,1.,np.pi]:
            vals=[quantities(r,rng.uniform(-rad,rad,3)) for _ in range(2000 if rad else 1)]
            vals=[v for v in vals if v]
            if not vals: continue
            q=max(vals,key=lambda x:x['ratio'])
            print(r,rad,len(vals),round(q['ratio'],5),round(max(v['budget'] for v in vals),5),q['phase'])
