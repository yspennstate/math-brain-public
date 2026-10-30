import json,time
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
BASE=Path(__file__).resolve().parents[1];COUNT=0;start=time.monotonic()
def ck(b):
    global COUNT
    COUNT+=1
    if not b:raise AssertionError(COUNT)
def plus(a,b):return (a[0]+b[0],a[1]+b[1])
def times(a,k):return (a[0]*k,a[1]*k)
def ln(x):
    z=(x-1)/(x+1);s=F(0);p=z
    for i in range(80):s+=2*p/(2*i+1);p*=z*z
    return s,s+2*p/(161*(1-z*z))
l2=ln(F(2));l15=ln(F(3,2));L=(1+l15[0]/l2[1],1+l15[1]/l2[0])
def bounds(a):
    if a[1]>=0:return (a[0]+a[1]*L[0],a[0]+a[1]*L[1])
    return (a[0]+a[1]*L[1],a[0]+a[1]*L[0])
def smaller(a,b):
    if a==b:return False
    lo,hi=bounds((a[0]-b[0],a[1]-b[1]))
    ck(hi<0 or lo>0)
    return hi<0
@lru_cache(None)
def rec(state):
    free=[i for i,b in enumerate(state) if b is None];tab=[]
    for z in range(1<<len(free)):
        v=list(state)
        for j,i in enumerate(free):v[i]=(z>>j)&1
        g=-1 if sum(v[3:])==0 else 1
        tab.append(g*(-1 if sum(v[i]*v[i+3] for i in range(3))%2 else 1))
    N=len(tab);w=[sum(a*(-1 if (s&t).bit_count()%2 else 1) for t,a in enumerate(tab)) for s in range(N)]
    ck(sum(a*a for a in w)==N*N)
    H=(F(2*len(free)),F(0))
    for a in w:
        a=abs(a)
        if not a:continue
        v=a;e2=0;e3=0
        while v%2==0:e2+=1;v//=2
        while v%3==0:e3+=1;v//=3
        ck(v==1)
        H=plus(H,(-F(2*e2*a*a,N*N),-F(2*e3*a*a,N*N)))
    I=sum((F(sum(tab[x]!=tab[x^(1<<i)] for x in range(N)),N) for i in range(len(free))),F(0))
    ck(I==F(sum(s.bit_count()*a*a for s,a in enumerate(w)),N*N))
    return H,I
def deficit(s):
    h,i=rec(s);return (2*i-h[0],-h[1])
@lru_cache(None)
def optimum(state,d):
    best=deficit(state)
    if d:
        for i,v in enumerate(state):
            if v is not None:continue
            s=list(state);s[i]=0;a=optimum(tuple(s),d-1);s[i]=1;b=optimum(tuple(s),d-1)
            c=times(plus(a,b),F(1,2))
            if smaller(c,best):best=c
    return best

leaves=[(0,0,0,None,None,None),(0,0,1,None,None,0),(0,0,1,None,None,1),
        (0,1,None,None,1,None),(0,1,None,0,0,None),(0,1,None,1,0,None),
        (1,None,None,0,None,None),(1,None,None,1,None,None)]
totalH=(F(0),F(0));totalI=F(0);weights=F(0)
for s in leaves:
    h,i=rec(s);p=F(1,2**sum(v is not None for v in s));weights+=p
    totalH=plus(totalH,times(h,p));totalI+=p*i
ck(weights==1);ck(totalH==(F(25,8),-F(9,64)));ck(totalI==F(45,32))
root=(None,)*6;ck(rec(root)==((F(6),F(0)),F(3)))
piH=(6-totalH[0],-totalH[1]);piI=3-totalI
ck(piH==(F(23,8),F(9,64)));ck(piI==F(51,32))
ratio=times(piH,1/piI);ck(ratio==(F(92,51),F(3,34)))
cut=(2*totalI-totalH[0],-totalH[1]);credit=(2*piI-piH[0],-piH[1])
ck(plus(cut,credit)==(0,0));ck(bounds(cut)[1]<0)
o3=optimum(root,3);o4=optimum(root,4)
ck(o3==(0,0));ck(o4==cut)
ck(3**5<2**8)
result={'status':'PASS','assertions':COUNT,'elapsed_seconds':time.monotonic()-start,
 'compact_ratio':['92/51','3/34'],'log_basis':['1','log2(3)'],
 'terminal_I':'45/32','Pi_I':'51/32','terminal_D2':list(map(str,cut)),
 'query_credit':list(map(str,credit)),'min_cut_D2_depth3':list(map(str,o3)),
 'min_cut_D2_depth4':list(map(str,o4)),
 'minimum_depth_gain_gt2_this_function':4,'strict_gain_lower':'524/255',
 'state_cache':rec.cache_info()._asdict(),'global_optimal_ratio_claimed':False,
 'independent_agent_review':False}
(BASE/'out'/'independent.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
