import json, time, sys
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict

ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic(); checks=0
def ck(x):
    global checks
    checks+=1
    assert x, checks
    assert time.monotonic()-start<55, 'frozen runtime cap'
def ln_interval(x):
    x=F(x); k=0
    while x>=2: x/=2; k+=1
    while x<1: x*=2; k-=1
    def atanh(q):
        t=(q-1)/(q+1); s=sum((2*t**(2*j+1)/F(2*j+1) for j in range(24)), F())
        return s,s+2*t**49/(49*(1-t*t))
    a,b=atanh(x); l,h=atanh(F(2))
    return (a+k*l,b+k*h) if k>=0 else (a+k*h,b+k*l)
L2,H2=ln_interval(F(2))
def log2_upper(x):
    z=ln_interval(x)[1]/L2; scale=1<<40
    return F((z.numerator*scale+z.denominator-1)//z.denominator,scale)
def supports(r):
    return [((3 if j<r else 6)|(3<<(3+2*j))) for j in range(2*r)]
def masks(e):
    s=e; ans=[0]
    while s: ans.append(s); s=(s-1)&e
    return ans
def law(r,retuned):
    es=supports(r); d={0:1}; o={0:0}
    den=30*r if retuned else 240
    empty=15*(2*r-1) if retuned else 225
    for e in es:
        nd=defaultdict(int); no=defaultdict(int)
        for a,v in d.items():
            for b in masks(e):
                w=1 if b else empty; u=a|b
                nd[u]+=v*w; no[u]+=(o[a]+v*bool(b))*w
        d,o=nd,no
    rho=F(1) if retuned else F(r,8)
    q={a:F(v,den**(2*r))/rho for a,v in o.items() if a}
    ck(sum(q.values())==1)
    return q
def truth(r):
    n=4*r+3; es=supports(r)
    values=[2*int(all(x&e for e in es))-1 for x in range(1<<n)]
    wh=values.copy(); width=1
    while width<len(wh):
        for j in range(0,len(wh),2*width):
            for k in range(width):
                u,v=wh[j+k],wh[j+k+width]; wh[j+k]=u+v; wh[j+k+width]=u-v
        width*=2
    p={i:F(v*v,1<<(2*n)) for i,v in enumerate(wh)}
    influences=[F(sum(values[x]!=values[x^(1<<i)] for x in range(1<<n)),1<<n) for i in range(n)]
    inf=sum(influences); a=F(3,4)**r
    ck(sum(p.values())==1)
    ck(sum(i.bit_count()*v for i,v in p.items())==inf)
    ck(inf==F(5,4)-a/2-3*a*a/4+F(r,3)*a*(1+a))
    ck(p[5]==(1-a)**4/16)
    M=sum(v for i,v in p.items() if i&~7)
    ck(M==a*(1-a)+a*a*(1-a*a)/2)
    return p,inf,M
def scalar(r):
    a=F(3,4)**r; I=F(5,4)-a/2-3*a*a/4+F(r,3)*a*(1+a)
    ck(a<F(1,3)); ck(r*a<=F(81,64)); ck(r*r*a<7); ck(I>F(5,4)); ck(I<2)
    ck((1-a)**4/16>F(1,81)); ck(2*113**16<120**16)
    ck(F(3*(r+1)**2,4*r*r)<=1 if r>=7 else True)
    ck(11+F(7,3)*(5*r*a+r*r*a)<34*I)
    ck(4+F(119,6)*r*a<=F(3725,128))
rows=[]
pilot='--pilot' in sys.argv
boundary='--boundary' in sys.argv
for r in ([4] if boundary else ([1] if pilot else [1,2,3])):
    p,I,M=truth(r)
    row={'r':r,'I':str(I),'M_private':str(M)}
    if r<=2:
        for retuned in [False,True]:
            q=law(r,retuned)
            cost=sum((v*log2_upper(1/q[i]) for i,v in p.items() if i and v),F())
            row['retuned' if retuned else 'old']={'cost_upper':str(cost),'ratio_upper':str(cost/I),'outputs':len(q)}
            ck(all(q[i]>0 for i in p if i))
            if retuned:
                ck(all(q[i]>F(1,1350) for i in range(1,8)))
                ck(all(v>=F(1,30*r)**(2*r) for v in q.values()))
                ck(cost<34*I)
                ck(sum(F(1,2*r) for e in supports(r) if e&2)==1)
                b=F(15*(2*r-1)+1,30*r); pp=F(2*r-1,2*r)
                ck(q[5]==F(1,15)*b**(r-1)*(b**r-pp**r))
            else:
                b=F(113,120); pp=F(15,16)
                ck(q[5]==F(1,15)*b**(r-1)*(b**r-pp**r))
                ck(cost+log2_upper(2)<100*I)
        # Independent complete posterior-normalization law gives same target mass.
        # A010 joint core mixture's exact full cost (all other outputs unchanged).
        old=law(r,False); joint={i:(v+ (F(1,7) if i<8 else 0))/2 for i,v in old.items()}
        ck(sum(joint.values())==1)
        jointcost=sum((v*log2_upper(1/joint[i]) for i,v in p.items() if i and v),F())
        ck(jointcost<24*I)
    rows.append(row)
if not pilot and not boundary:
    for r in range(4,257): scalar(r)
    ck(F(8083,240)<34)
out={'status':'PASS','assertions':checks,'runtime_seconds':time.monotonic()-start,'pilot':pilot,'rows':rows,'arithmetic':'integers/Fraction; certified 24-term atanh log bounds'}
(ROOT/'out').mkdir(exist_ok=True)
(ROOT/'out'/('BOUNDARY.json' if boundary else ('PILOT.json' if pilot else 'CHECK.json'))).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
