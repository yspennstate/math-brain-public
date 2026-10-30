from pathlib import Path
from fractions import Fraction as Q
from math import comb, factorial
from itertools import product
import json, time, hashlib

ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter(); checks=0
def ck(v):
    global checks
    checks+=1
    assert v, checks
    assert time.perf_counter()-start<55, 'frozen runtime exceeded'
def logbounds(x):
    x=Q(x); k=0
    while x>=2: x/=2; k+=1
    while x<1: x*=2; k-=1
    def raw(z):
        t=(z-1)/(z+1); s=sum((t**(2*j+1)/Q(2*j+1) for j in range(45)),Q(0))*2
        return s,s+2*t**91/(91*(1-t*t))
    lo,hi=raw(x); l2,h2=raw(Q(2))
    return Q(k)+lo/h2,Q(k)+hi/l2
def klbounds(p,q):
    lo=hi=Q(0)
    for a,b in zip(p,q):
        if not a: continue
        ck(b>0)
        l,h=logbounds(a/b); lo+=a*l; hi+=a*h
    return lo,hi
def walsh(t):
    # Direct character summation, not the author's FWHT.
    return [sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)) for s in range(len(t))]
def spectrum(t):
    w=walsh(t); n=len(t)
    p=[Q(a*a,n*n) for a in w]; ck(sum(p)==1); return p
def influence(t):
    n=(len(t)-1).bit_length()
    return sum(Q(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(n))
def marg(p,i): return [sum(a for x,a in enumerate(p) if ((x>>i)&1)==b) for b in (0,1)]

# Independent multinomial expansion with opposite orientation to A079's code.
c=[0]*85
for k in range(13): c[7*k]+=16*comb(12,k)*3**k
for k0 in range(8):
 for k1 in range(8-k0):
  for k2 in range(8-k0-k1):
   k3=7-k0-k1-k2
   c[4*(k1+2*k2+3*k3)]-=factorial(7)//(factorial(k0)*factorial(k1)*factorial(k2)*factorial(k3))*3**(k1+k2)*9**k3
cones=[]
for row in (c,c[::-1]):
    # Horner translation t -> 1+w without binomial transform.
    shifted=[0]
    for a in row[::-1]:
        out=[0]*(len(shifted)+1)
        for i,v in enumerate(shifted): out[i]+=v; out[i+1]+=v
        out[0]+=a; shifted=out
    shifted=shifted[:85]; ck(all(a>=0 for a in shifted)); cones.append(shifted)
for u,v in [(0,0),(0,1),(1,0),(1,1),(10,11),(11,10)]:
    val=16*(3*u**7+v**7)**12-(8*u**12+(u**4+v**4)**3)**7
    ck(val==sum(a*u**j*v**(84-j) for j,a in enumerate(c))); ck(val>=0)

P=[Q(9 if s==0 else 1,16) for s in range(8)]; mu=[Q(3,4),Q(1,4)]
x,y=1000,1331; A=8*x**3+(x+y)**3
endpoint=A**5-4*(3*10**5+11**5)**9; ck(endpoint>0)
R=[a*x**(3-s.bit_count())*y**s.bit_count()*16/A for s,a in enumerate(P)]; ck(sum(R)==1)
dlo,dhi=klbounds(R,P); ml=mh=Q(0)
for i in range(3):
    lo,hi=klbounds(marg(R,i),mu); ml+=lo; mh+=hi
gap=ml-Q(5,3)*dhi; ck(gap>0)
upper_slack=Q(7,4)*dlo-mh; ck(upper_slack>0)

defect=[]
for r in (1,2):
    t=[(-1)**sum(((z>>(3*j))&7)==0 for j in range(r)) for z in range(1<<(3*r))]
    p=spectrum(t)
    ck(all(a==Q(1,16**r)*9**sum(((s>>(3*j))&7)==0 for j in range(r)) for s,a in enumerate(p)))
    ck(influence(t)==Q(3*r,4)); defect.append({'r':r,'influence':str(influence(t))})

family=[]
for m in (1,2,3,4):
    mask=(1<<m)-1
    def value(x,y): return (-1)**((x&y).bit_count()+((y&1)*((y>>1).bit_count())))
    parent=[value(z&mask,z>>m) for z in range(1<<(2*m))]
    pp=spectrum(parent); ck(all(a==Q(1,1<<(2*m)) for a in pp)); ck(influence(parent)==m)
    leaves=[]
    for fixed in range(1<<(m-1)):
        # Residual order x1,y1,y2,...,ym; all discarded x assignments retained.
        t=[value((fixed<<1)|(z&1),z>>1) for z in range(1<<(m+1))]
        p=spectrum(t); support=[s for s,a in enumerate(p) if a]
        expected=[]
        for a,b in product((0,1),repeat=2):
            s=a|(b<<1)
            for j in range(1,m): s|=(a^((fixed>>(j-1))&1))<<(j+1)
            expected.append(s)
        ck(sorted(support)==sorted(expected)); ck(all(p[s]==Q(1,4) for s in support))
        ck(influence(t)==Q(m+1,2))
        ck(sum(a*s.bit_count() for s,a in enumerate(p))==influence(t))
        # Tilt the duplicated frequency bit to1; exact D=1 and each copied marginal D=1.
        rlaw=[2*a if s&1 else Q(0) for s,a in enumerate(p)]; ck(sum(rlaw)==1)
        ck(all(not a or a==2*p[s] for s,a in enumerate(rlaw)))
        single_ratios=[]
        for i in range(m+1):
            pm=marg(p,i); rm=marg(rlaw,i)
            ck(pm==[Q(1,2),Q(1,2)])
            single_ratios.append(0 if rm==pm else 1)
        ck(sum(single_ratios)==m)
        leaves.append({'fixed':fixed,'truth_table':t,'walsh_integers':walsh(t),'support':support,'influence':str(influence(t)),'D_bits':1,'sum_marginal_D_bits':m})
    ck(Q(m-1,2)+sum(Q(1,len(leaves))*Q(a['influence']) for a in leaves)==m)
    family.append({'m':m,'parent_truth_table':parent,'parent_influence':m,'parent_entropy':2*m,'terminal_entropy':2,'contraction_exact':m,'leaves':leaves})

gap_floor=Q((gap.numerator*(1<<100))//gap.denominator,1<<100)
ck(0<gap_floor<=gap)
out={'checks':checks,'seconds':time.perf_counter()-start,'arithmetic':'integer/Fraction;45-term outward atanh bounds','scalar_coefficients':list(map(str,c)),'ordered_cones':[[str(a) for a in row] for row in cones],'endpoint_positive_integer':str(endpoint),'endpoint_entropy_gap_lower':str(gap_floor),'defects':defect,'family':family}
(ROOT/'out'/'validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks':checks,'seconds':out['seconds'],'status':'PASS','parents':4,'full_terminals':15,'endpoint_gap_positive':gap>0}))
