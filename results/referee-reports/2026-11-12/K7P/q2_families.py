"""Exact near-sharp families, clone padding, and compact ratio formulas."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import json,time,resource
from fractions import Fraction as Q
import q2_search as s
from q1_core import exact,lump,serialize

def k5(t):
    w=[[Q(0)]*4 for _ in range(4)]
    w[0][2]=w[2][0]=w[1][2]=w[2][1]=1
    w[2][3]=w[3][2]=t*t;w[0][0]=w[1][1]=t-1;w[3][3]=t**6
    return w

def clone(w,c,k):
    """Replace c by k equal clones; original c retains its index."""
    old=len(w);origin=list(range(old))+[c]*(k-1);weights=[Q(1)]*old+[Q(1,k)]*(k-1);weights[c]=Q(1,k)
    return [[w[i][j]*a*b for j,b in zip(origin,weights)] for i,a in zip(origin,weights)]

def formula(N,t):
    if N==0:
        W=t**6+2*t*t+2*t+2
        T=(t**7+t**6+2*t**5+2*t**4+2*t**3+t*t+4*t+2)/W
        Th=(2*t**7+4*t**3+2*t*t+4*t)/W
    elif N==1:
        W=3*t**15+2*t**9+t**8+t**7+t**5+t**4+2*t**3+t+1
        U=t**3+t+1;S=W-(3*t**15+t**9);V=t**8+t**3+t+1
        T=t+U/t**3+S/t**9-(t*t+t**9+t**6+U*U/t**3+S*S/t**9)/W
        Th=2*t+V/(t**7+t**3)-(t*t+t**6+V*V/(t**7+t**3))/W
    else:
        W=4*t**18+2*t**12+t**11+t**10+t**8+t**7+2*t**6+t**5+t**4+2*t**3+t+1
        U=t**3+t+1;V=t**6+t**5+t**4+2*t**3+t+1;S=W-(4*t**18+t**12)
        A=t**5+t**3+t+1;B=t**11+t**6+t**5+t**4+2*t**3+t+1
        T=t+U/t**3+V/t**6+S/t**12-(t*t+t**6+t**9+t**12+U*U/t**3+V*V/t**6+S*S/t**12)/W
        Th=2*t+A/(t**4+t**3)+B/(t**10+t**6)-(t*t+t**9+A*A/(t**4+t**3)+B*B/(t**10+t**6))/W
    return T,Th

def run():
    begin=time.monotonic();best=s.loadbest();t=Q(10**12);out={}
    # Include exact iid examples, whose nontrivial quotients also have T=1.
    for n in range(4,9):
        w=[[Q(1)]*n for _ in range(n)]
        s.exact_scan(w,(2,3),best,'iid_all_conductances_1',audit=(n==4))
    # Padding preserves times here, checked by full exact hitting solves.
    cases=[(5,2,0),(6,3,0),(6,2,1),(7,2,1),(7,3,1),(8,2,1),(8,3,2)]
    for n,r,N in cases:
        base=k5(t) if N==0 else s.fork(N,t)
        host=3 if N==0 else (0 if r==2 else 2)
        w=clone(base,host,n-len(base)+1)
        if N==0:bs=[[0],[1],[2,3]+list(range(4,n))]
        elif N==1:
            bs=[[0],[1,3],[2,4],[5]]
            if r==3:bs[2]+=list(range(6,n))
            else:bs += [[i] for i in range(6,n)]
        else:bs=[[0],[1,4],[2,5],[3,6],[7]]
        x=exact(w);z=exact(lump(w,bs));a,b=formula(N,t)
        assert x['t']==a and z['t']==b,(n,r,'formula failed')
        assert s.correction(x['F'],bs)==z['F']
        out[f'{n},{r}']=serialize(dict(t=t,N=N,T=a,That=b,ratio=b/a,partition=bs,w=w,original_maximizers=x['pairs'],quotient_maximizers=z['pairs']))
        s.exact_scan(w,(r,),best,f'compact_family_R{N+2}_t10pow12_cloned_to{n}')
        print(n,r,'R'+str(N+2),float(b/a),'EXACT',b/a,flush=True)
        assert Q(best[f'{n},{r}']['ratio'])==b/a,('another partition wins',n,r,best[f'{n},{r}']['partition'])
    with open('q2_family_results.json','w') as f:json.dump(out,f,indent=2)
    s.log(f'Exact compact families at t=10^12, iid examples, and clone padding checked by independent hitting solves. Best ratios are exactly 1, 0, R2, R3, R4 as recorded in q2_family_results.json. Elapsed {time.monotonic()-begin:.3f}s; peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss} bytes.')
if __name__=='__main__':run()
