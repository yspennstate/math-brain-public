from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,sys
R=Path(__file__).resolve().parents[1];START=time.monotonic();MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
CAP=55 if MODE=='pilot' else 180;checks=0;negative_banks=0;states=0;queries=0
def ck(ok):
    global checks
    checks+=1
    assert ok,checks
    assert time.monotonic()-START<CAP,'frozen runtime exceeded'
def ln_unit(x):
    z=(x-1)/(x+1);s=sum((2*z**(2*j+1)/(2*j+1) for j in range(28)),F(0))
    return s,s+2*z**57/(57*(1-z*z))
L2=ln_unit(F(2))
@lru_cache(None)
def log2(x):
    k=0
    while x<1:x*=2;k-=1
    while x>=2:x/=2;k+=1
    a,b=ln_unit(x);return F(k)+a/L2[1],F(k)+b/L2[0]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,t):return (a[0]*t,a[1]*t) if t>=0 else (a[1]*t,a[0]*t)
def scalar(x):return F(x),F(x)
def ce(p,q):
    out=scalar(0)
    for a,b in zip(p,q):
        if a:out=add(out,mul(log2(1/b),a))
    return out
def walsh(v):
    a=v[:];j=1
    while j<len(a):
        for k in range(0,len(a),2*j):
            for l in range(k,k+j):a[l],a[l+j]=a[l]+a[l+j],a[l]-a[l+j]
        j*=2
    return a
def spectrum(v):return [F(a*a,len(v)**2) for a in walsh(v)]
def drop(v,j,bit):
    low=(1<<j)-1
    return [v[(a&low)|((a&~low)<<1)|(bit<<j)] for a in range(len(v)//2)]
def marginal(q,j):return [a+b for a,b in zip(drop(q,j,0),drop(q,j,1))]
def infl(v,j):return F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v))),len(v))
def totalI(v):return sum((infl(v,j) for j in range(len(v).bit_length()-1)),F(0))
def root_tables(m):
    b=[];c=[]
    for x in range(1<<(2*m+1)):
        y=x&((1<<(2*m))-1)
        bb=(-1)**sum(((y>>(2*j))&3)==3 for j in range(m))
        b.append(bb);c.append(bb-2*(x==0))
    return b,c
def grouped_root(m):
    N=1<<(2*m);A=F(1,1<<m);d=F(1,2*N);np=(N+(1<<m))//2;nm=N-np
    g=[((A-d)**2,np),((A+d)**2,nm),(d*d,3*N)]
    h=scalar(0)
    for p,n in g:h=add(h,mul(log2(1/p),p*n))
    return h
def grouped_ce(m,t):
    A=F(1,1<<m);d=F(1,1<<(2*m+1));k=m-t;N=1<<(2*k);dt=(1<<t)*d
    np=(N+(1<<k))//2;nm=N-np;flat=4*dt*dt
    b=(1<<t)*(A*A+4*d*d);a=4*d*A*(1<<t)
    groups=[(((1<<t)*(b-a)),b-a,np),(((1<<t)*(b+a)),b+a,nm),(flat,b,((1<<t)-1)*N),(flat,(1<<t)*4*d*d,(1<<t)*N)]
    ck(sum(p*n for p,q,n in groups)==1)
    out=scalar(0)
    for p,q,n in groups:
        if n:out=add(out,mul(log2(1/q),p*n))
    return out
def encoded(x):return {'lo':str(x[0]),'hi':str(x[1]),'approx':float(sum(x)/2)}
group_rows=[]
for m in ([2] if MODE=='pilot' else range(2,13)):
    d=F(1,1<<(2*m+1));hg=grouped_root(m);hbar=mul(add(scalar(2*m),grouped_ce(m,0)),F(1,2))
    oldD=sub(hg,hbar);S=sub(scalar(2*(m+(2*m+1)*d)),hbar);r=sub(S,oldD)
    ck(r[0]>d/4);E=scalar(0);exitbank=scalar(0)
    for t in range(m+1):
        k=m-t;dt=(1<<t)*d;n=2*m+1-t;ct=grouped_ce(m,t);it=F(k)+2*n*dt;reach=F(1,1<<(t+1))
        bank=add(exitbank,mul(sub(scalar(2*it),ct),reach));left=sub(bank,add(oldD,E))
        ck(left[0]>d/4);ck(not(left[1]<r[0] or r[1]<left[0]))
        group_rows.append({'m':m,'t':t,'residual':encoded(left),'signed_debit':encoded(E),'frontier_bank':encoded(bank)})
        if t<m:
            exitce=sub(scalar(2*m-t-1),log2(1+F(1,1<<(2*m))))
            nex=grouped_ce(m,t+1);inf=F(1,2)+2*dt
            debit=sub(sub(ct,mul(add(nex,exitce),F(1,2))),scalar(2*inf))
            ck(debit[1]<-4*dt)
            E=add(E,mul(debit,reach))
            exitbank=add(exitbank,mul(sub(scalar(2*k),exitce),reach/2))

def literal(m):
    global states,queries,negative_banks
    bv,cv=root_tables(m);qc=spectrum(cv);qb=spectrum(bv);d=F(1,1<<(2*m+1));hg=grouped_root(m)
    hb=ce(qb,qb);hc=ce(qc,qc);hbar=mul(add(hb,hc),F(1,2));oldD=sub(hg,hbar)
    S=sub(scalar(2*(m+(2*m+1)*d)),hbar);r=sub(S,oldD)
    def walk(v,q,labels,prefix,exits,E):
        global states,queries,negative_banks
        states+=1;t=len(prefix);k=m-t;dt=(1<<t)*d;n=len(labels);p=spectrum(v)
        ck(all(a>0 for a in q));ck(sum(q)==1);ck(sum(p)==1)
        ck(totalI(v)==k+2*n*dt)
        ct=ce(p,q);expect=grouped_ce(m,t);ck(not(ct[1]<expect[0] or expect[1]<ct[0]))
        partial={x//2 for x in prefix};reach=F(1,1<<(t+1))
        # Exact likelihood sufficiency on the full incoming source, including dummy occupancy.
        A=F(1,1<<m)
        for mask,(pp,qq) in enumerate(zip(p,q)):
            w=bool(mask&(1<<labels.index(2*m)))
            occupied=any(mask&(1<<labels.index((x^1))) for x in prefix)
            ratio=F(1<<t) if w or not occupied else F(1<<t)*A*A/(1+A*A)
            ck(pp==ratio*qq)
        bank=add(exits,mul(sub(scalar(2*totalI(v)),ct),reach));left=sub(bank,add(oldD,E))
        ck(left[0]>d/4);ck(not(left[1]<r[0] or r[1]<left[0]))
        if t:ck(E[1]<-2*t*d)
        for j,label in enumerate(labels):
            if label==2*m or label//2 in partial:continue
            queries+=1
            qrow=marginal(q,j);pr=marginal(p,j)
            for mask in range(len(p)):
                row=(mask&((1<<j)-1))|((mask>>(j+1))<<j)
                ck(p[mask]*qrow[row]==q[mask]*pr[row])
            v0,v1=drop(v,j,0),drop(v,j,1);p0,p1=spectrum(v0),spectrum(v1)
            ck(all((a+b)/2==c for a,b,c in zip(p0,p1,pr)))
            ck(infl(v,j)==F(1,2)+2*dt)
            ck(totalI(v1)==k)
            c0,c1=ce(p0,qrow),ce(p1,qrow)
            exitexpected=sub(scalar(2*m-t-1),log2(1+A*A))
            ck(not(c1[1]<exitexpected[0] or exitexpected[1]<c1[0]))
            B=sub(ce(p,p),ce(pr,pr));deltaCE=sub(ct,mul(add(c0,c1),F(1,2)))
            ck(not(B[1]<deltaCE[0] or deltaCE[1]<B[0]))
            debit=sub(deltaCE,scalar(2*infl(v,j)));ck(debit[1]<-4*dt)
            b1=sub(scalar(2*totalI(v1)),c1)
            if t>=2:ck(b1[1]<0);negative_banks+=1
            walk(v0,qrow,labels[:j]+labels[j+1:],prefix+(label,),add(exits,mul(b1,reach/2)),add(E,mul(debit,reach)))
    walk(cv,qc,list(range(2*m+1)),(),scalar(0),scalar(0))
for m in ([2] if MODE=='pilot' else [2,3,4]):literal(m)
out={'status':'PASS','mode':MODE,'checks':checks,'literal_states':states,'literal_queries':queries,'grouped_states':len(group_rows),'negative_clean_exit_banks':negative_banks,'runtime_seconds':time.monotonic()-START,'rows':group_rows}
(R/f'out/{MODE.upper()}.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
