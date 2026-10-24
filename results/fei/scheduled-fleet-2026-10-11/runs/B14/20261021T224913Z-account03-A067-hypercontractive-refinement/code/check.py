from fractions import Fraction as Q
from pathlib import Path
from collections import Counter
import json,time,hashlib
R=Path(__file__).resolve().parents[1]
start=time.monotonic(); checks=0
def ck(b):
    global checks
    checks+=1
    assert b
    assert time.monotonic()-start<55
def ln_unit(x):
    z=(x-1)/(x+1); s=Q(0)
    for k in range(28): s+=2*z**(2*k+1)/(2*k+1)
    tail=2*z**57/(57*(1-z*z))
    return s,s+tail
L2=ln_unit(Q(2)); cache={}
def log2(x):
    if x in cache:return cache[x]
    orig=x;k=0
    while x<1:x*=2;k-=1
    while x>=2:x/=2;k+=1
    a,b=ln_unit(x); out=(Q(k)+a/L2[1],Q(k)+b/L2[0]);cache[orig]=out;return out
def H(groups):
    lo=hi=Q(0)
    for p,n in groups:
        if p:
            a,b=log2(1/p);lo+=n*p*a;hi+=n*p*b
    return lo,hi
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def encode(v):return {'lower':str(v[0]),'upper':str(v[1]),'approx':float(sum(v)/2)}
def walsh(v):
    a=v[:];h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return a
def table(m,z=None):
    n=2*m+1+(z is None);out=[]
    for x in range(1<<n):
        y=x&((1<<(2*m))-1);w=(x>>(2*m))&1
        b=(-1)**sum(((y>>(2*j))&3)==3 for j in range(m))
        zz=(1 if ((x>>(2*m+1))&1)==0 else -1) if z is None else z
        out.append(b+(zz-1 if y==0 and w==0 else 0))
    return out
def physical(v):
    n=len(v).bit_length()-1
    return Q(sum(v[x]!=v[x^(1<<j)] for x in range(len(v)) for j in range(n)),len(v))
rows=[]
for m in range(2,9):
    N=1<<(2*m);a=Q(1,1<<m);d=Q(1,2*N);np=(N+(1<<m))//2;nm=N-np
    pg=[((a-d)**2,np),((a+d)**2,nm),(d*d,3*N)]
    cg=[((a-2*d)**2,np),((a+2*d)**2,nm),(4*d*d,N)]
    tg=[((a-d)**2+d*d,np),((a+d)**2+d*d,nm),(2*d*d,N)]
    for g in (pg,cg,tg):ck(sum(p*n for p,n in g)==1)
    hp,hc,ht=H(pg),H(cg),H(tg);hb=(Q(2*m),Q(2*m));mean=((hc[0]+2*m)/2,(hc[1]+2*m)/2)
    avgI=Q(m)+(2*m+1)*d;ig=avgI+d
    bank=sub((2*avgI,2*avgI),mean);B=sub(hp,ht);JS=sub(ht,mean);debt=sub(hp,mean);reserve=sub(bank,debt)
    ck(B[0]>=0);ck(JS[0]>=0);ck(bank[0]>0)
    ck(reserve[0]>d/4);ck(B[0]/d>m+Q(3,2));ck(hp[1]<2*ig)
    if m==3:ck(reserve[0]>5*d/4)
    if m>=4:ck(reserve[0]>(m-Q(13,4))*d)
    if m<=4:
        vals=table(m);ck(all(v in (-1,1) for v in vals));ww=walsh(vals);den=len(vals)**2
        ck(Counter(Q(x*x,den) for x in ww)==Counter({p:sum(n for q,n in pg if q==p) for p,n in pg}))
        ck(physical(vals)==ig)
        for z,expectedI,expectedH,groups in [(1,Q(m),hb,[(Q(1,N),N)]),(-1,Q(m)+(4*m+2)*d,hc,cg)]:
            vv=table(m,z);cc=walsh(vv);dd=len(vv)**2
            actual=Counter(Q(x*x,dd) for x in cc if x)
            expected=Counter()
            for p,n in groups:
                if p:expected[p]+=n
            ck(actual==expected);ck(physical(vv)==expectedI)
            ck(Q(sum(i.bit_count()*x*x for i,x in enumerate(cc)),dd)==expectedI)
        ck(Q(sum(i.bit_count()*x*x for i,x in enumerate(ww)),den)==ig)
    rows.append({'m':m,'delta':str(d),'B_over_delta':encode((B[0]/d,B[1]/d)),'JS_over_delta':encode((JS[0]/d,JS[1]/d)),'bank_over_delta':encode((bank[0]/d,bank[1]/d)),'remaining_over_delta':encode((reserve[0]/d,reserve[1]/d))})
out={'status':'PASS','checks':checks,'runtime_seconds':time.monotonic()-start,'rows':rows,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'out/CHECK.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'],'checks':checks,'runtime_seconds':out['runtime_seconds'],'rows':[{k:(v['approx'] if isinstance(v,dict) else v) for k,v in x.items()} for x in rows]}))
