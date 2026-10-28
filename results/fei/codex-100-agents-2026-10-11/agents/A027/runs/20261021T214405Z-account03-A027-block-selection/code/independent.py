"""Independent direct character sums and separate log-enclosure implementation."""
from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
import json,time
start=time.monotonic();checks=0
def ck(v):
    global checks
    assert v
    checks+=1
    assert time.monotonic()-start<60
def combine(*pairs):
    z={}
    for c,a in pairs:
        for k,v in a.items():z[k]=z.get(k,F(0))+c*v
    return {k:v for k,v in z.items() if v}
def fac(n):
    d=2;r={}
    while d*d<=n:
        while n%d==0:r[d]=r.get(d,0)+1;n//=d
        d+=1
    if n>1:r[n]=r.get(n,0)+1
    return r
def lg(q):return combine((1,fac(q.numerator)),(-1,fac(q.denominator)))
def ent(q):return combine((-q,lg(q))) if q else {}
def esq(t):return ent(t*t)
@lru_cache(None)
def H(f):
    ans={};norm=len(f);ps=F(0)
    for mask in range(norm):
        a=F(sum(v*(-1 if (mask&j).bit_count()%2 else 1) for j,v in enumerate(f)),norm)
        ps+=a*a;ans=combine((1,ans),(1,ent(a*a)))
    ck(ps==1)
    return ans
def influence(f):
    return sum((F(sum(v!=f[j^(1<<i)] for j,v in enumerate(f)),len(f)) for i in range(len(f).bit_length()-1)),F(0))
def activated(u):return tuple(u)+tuple(1 for _ in u)
def direct_correction(u,g,h):
    return combine((1,H(activated(u))),(F(-1,2),H(activated(g))),(F(-1,2),H(activated(h))),(F(-1,2),H(u)),(F(1,4),H(g)),(F(1,4),H(h)))
def lnenclose(y):
    z=(y-1)/(y+1);total=F(0)
    for j in range(32):total+=2*z**(2*j+1)/(2*j+1)
    return total,total+2*z**65/(65*(1-z*z))
ln2=lnenclose(F(2))
def logenclose(n):
    y=F(n);k=0
    while y>=2:y/=2;k+=1
    lo,hi=lnenclose(y)
    return k+lo/ln2[1],k+hi/ln2[0]
def enclose(e):
    lo=hi=F(0)
    for n,c in e.items():
        a,b=logenclose(n);lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
    # Exact outward compactification; the series bound remains rational.
    den=1<<64
    return [str(F((lo*den).__floor__(),den)),str(F((hi*den).__ceil__(),den))]
def aval(d):return combine((4*d*(1-d),{2:F(1)}),(1,esq(d)),(1,esq(1-d)),(F(-1,2),esq(1-2*d)))
def ader(d):return combine((4-8*d,{2:F(1)}),(-4*d,lg(d)),(4*(1-d),lg(1-d)),(-4*(1-2*d),lg(1-2*d)))
s=F(1,16);b=F(3,10)
tangent=combine((1,aval(b)),(-1,aval(s)),(-(b-s),ader(s)))
ck(F(enclose(tangent)[0])>F(17,1000))
g=tuple(-1 if j<3 else 1 for j in range(16));h=tuple(-1 if j<4 else 1 for j in range(16))
v=tuple(g[j>>1] if not(j&1) else h[j>>1] for j in range(32))
u=tuple(v[j>>2] if not(j&3) else 1 for j in range(128))
z=(1,)*16
exit=direct_correction(v,g,h)
full=combine((1,H(activated(u))),(F(-1,8),H(activated(g))),(F(-1,8),H(activated(h))),(F(-1,2),H(u)),(F(1,16),H(g)),(F(1,16),H(h)))
ck(F(enclose(exit)[0])>0);ck(F(enclose(full)[1])<0)
# Independent full physical influence and complete terminal accounting.
leafI=(influence(activated(g))+influence(activated(h)))/8
rootI=influence(activated(u));d=F(u.count(-1),len(u))
ck(d==F(7,128));ck(leafI==(influence(g)+influence(h))/16+d)
other=json.loads((Path(__file__).resolve().parents[1]/'out/validation.json').read_text(encoding='utf-8'))
ck({str(k):str(v) for k,v in tangent.items()}==other['tangent_certificate']['prime_log'])
ck({str(k):str(v) for k,v in exit.items()}==other['witness']['positive_exit']['prime_log'])
ck({str(k):str(v) for k,v in combine((-1,full)).items()}==other['witness']['final_refund']['prime_log'])
result={'status':'PASS','method':'direct character sums; independent32-term atanh intervals; exact physical edge counts','assertions':checks,'elapsed_seconds':time.monotonic()-start,'tangent_interval':enclose(tangent),'positive_exit_interval':enclose(exit),'full_signed_correction_interval':enclose(full),'root_I':str(rootI),'terminal_I':str(leafI),'queried_I':str(rootI-leafI)}
(Path(__file__).resolve().parents[1]/'out/independent.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
