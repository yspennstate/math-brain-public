"""Literal six-bit Boolean audit. No marked-point state reduction."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json,time
from arithmetic import Q,log2,scale,plus
ROOT=Path(__file__).resolve().parents[1];checks=0
def ck(b):
    global checks
    assert b;checks+=1
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def maximum(xs):return max(x[0] for x in xs),max(x[1] for x in xs)
truth=tuple((-1 if (x&7).bit_count()%2 else 1)*(-1 if not x else 1) for x in range(64))
@lru_cache(None)
def data(assignment):
    free=[i for i,a in enumerate(assignment) if a<0]
    table=tuple(truth[x] for x in range(64) if all(a<0 or x>>i&1==a for i,a in enumerate(assignment)));N=len(table)
    W=[sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(table)) for s in range(N)]
    ck(sum(w*w for w in W)==N*N)
    ck(all(sum(w*(-1 if (x&s).bit_count()%2 else 1) for s,w in enumerate(W))==N*v for x,v in enumerate(table)))
    I=sum((F(s.bit_count()*w*w,N*N) for s,w in enumerate(W)),F(0));edge=[]
    for i in range(len(free)):
        d=F(sum(table[x]!=table[x^(1<<i)] for x in range(N)),N);edge.append(d)
        ck(d==sum((F(w*w,N*N) for s,w in enumerate(W) if s>>i&1),F(0)))
    ck(sum(edge,F(0))==I);H=(0,0)
    for w in W:
        p=F(w*w,N*N)
        if p:H=plus(H,scale(log2(1/p),p))
    B=sub(H,scale((Q,Q),I));return (max(0,B[0]),max(0,B[1])),H,I,W,edge
def kids(ass,mask,i):
    out=[]
    for b in (0,1):a=list(ass);a[i]=b;out.append((tuple(a),mask&~(1<<i)))
    return out
@lru_cache(None)
def rho(ass,mask):
    ans=[data(ass)[0]]
    for i in range(6):
        if mask>>i&1:
            a,b=kids(ass,mask,i);ans.append(scale(plus(rho(*a),rho(*b)),F(1,2)))
    return maximum(ans)
@lru_cache(None)
def robust(ass,mask):
    ans=[data(ass)[0]]
    for i,a in enumerate(ass):
        if a>=0:continue
        if not mask>>i&1:ans.append(robust(ass,mask|1<<i))
        else:
            cs=kids(ass,mask,i);r=[rho(*c) for c in cs];avg=scale(plus(*r),F(1,2))
            for c,rr in zip(cs,r):ans.append(sub(robust(*c),sub(rr,avg)))
    return maximum(ans)
def main():
    start=time.perf_counter();root=(-1,)*6;R=rho(root,63);T=robust(root,0)
    ck(T[0]*10000>5078*Q);ck(T[1]*10000<5079*Q)
    allstates=[]
    for pattern in product(range(4),repeat=6):
        ass=tuple(-1 if x<2 else x-2 for x in pattern);mask=sum(1<<i for i,x in enumerate(pattern) if x==1)
        rr=rho(ass,mask);tt=robust(ass,mask);allstates.append({'assignment':ass,'mask':mask,'local_hull':rr,'robust_capital':tt})
    ck(len(allstates)==4096);b,h,i,W,edges=data(root)
    model=json.loads((ROOT/'out/CAPITAL.json').read_text(encoding='utf-8'))['results'][3]
    ck(R[0]<=model['global_hull'][1] and model['global_hull'][0]<=R[1]);ck(T[0]<=model['robust_capital'][1] and model['robust_capital'][0]<=T[1])
    ck(time.perf_counter()-start<55)
    result={'version':'literal-six-bit-admission-v1','augmented_states':len(allstates),'literal_restrictions':data.cache_info().currsize,'checks':checks,'root_global_hull':R,'root_robust_capital':T,'root_Walsh_integer':W,'root_H':h,'root_I':str(i),'direct_coordinate_influences':list(map(str,edges)),'strict_capital_bracket':['5078/10000','5079/10000'],'runtime_seconds':time.perf_counter()-start,'states':allstates}
    (ROOT/'out/RAW_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in result.items() if k not in ['states','root_Walsh_integer']}))
if __name__=='__main__':main()
