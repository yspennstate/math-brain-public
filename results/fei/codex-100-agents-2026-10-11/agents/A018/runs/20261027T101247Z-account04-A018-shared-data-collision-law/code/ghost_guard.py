"""Actual all-width failure of bounded per-connected-block ghost payment."""
from pathlib import Path
from fractions import Fraction as F
import json,time
root=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def chk(b):
    global checks
    checks+=1
    assert b,checks
def fw(v):
    a=list(v);h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for l in range(j,j+h):
                x,y=a[l],a[l+h];a[l],a[l+h]=x+y,x-y
        h*=2
    return a
records=[]
for r in (2,3,4):
    n=2*r+1;N=2**n
    v=[]
    for x in range(N):
        parity=sum(not(x&1) and not(x&(3<<(2*j+1))) for j in range(r))
        v.append((-1)**parity)
    orig=fw(v);coords=[1,2]+[2*j+2 for j in range(1,r)]
    q=[F(0)]*(1<<len(coords))
    for s,z in enumerate(orig):
        t=sum(((s>>i)&1)<<l for l,i in enumerate(coords));q[t]+=F(z*z,N*N)
    # a=0; for every later pair fix b_j=1, leave c_j irrelevant and unqueried.
    fixed=sum(1<<(2*j+1) for j in range(1,r))
    child=[v[fixed+sum(((x>>l)&1)<<i for l,i in enumerate(coords))] for x in range(len(q))]
    w=fw(child);P=[F(z*z,len(child)**2) for z in w]
    chk(P[:4]==[F(1,4)]*4);chk(all(z==0 for z in P[4:]))
    d=r+1;chk(q[0]==(1+F(1,2**d))/2)
    chk(all(z==F(1,2**(d+1)) for z in q[1:]))
    I=sum(F(sum(child[x]!=child[x^(1<<l)] for x in range(len(child))),len(child)) for l in range(len(coords)))
    chk(I==1)
    if r==4:
        chk(q[0]==F(33,64));chk(q[1]*q[2]*q[3]*q[0]<F(1,2**16));chk(33<256)
    records.append({'r':r,'remaining_coords':coords,'P':[[z.numerator,z.denominator] for z in P],
                    'Q':[[z.numerator,z.denominator] for z in q],'influence':[I.numerator,I.denominator]})
for r in range(2,65):
    # Exact floor in D = 3(r-1)/4 + log2(5/[4(1+2^-r-1)])/4.
    chk(F(5,4)/(1+F(1,2**(r+1)))>1)
    if r>=4:chk(F(3,4)*(r+2)>4)
out={'status':'PASS','checks':checks,'seconds':time.perf_counter()-start,'records':records,
     'all_width_statement':'D>3(r-1)/4 for r>=2; CE_unclean>3(r+2)/4>4I for r>=4, I=1',
     'smallest_certified_failure':'r4, actual normalized row product33/2^24<2^-16 iff33<256'}
(root/'out/GHOST_GUARD.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='records'}))
