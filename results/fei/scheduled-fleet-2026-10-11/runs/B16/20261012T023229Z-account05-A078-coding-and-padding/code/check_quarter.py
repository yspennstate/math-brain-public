from pathlib import Path
from fractions import Fraction as F
from math import comb,isqrt
from functools import lru_cache
import time,json,sys
from check_overlap import coefficients,fwht
ROOT=Path(__file__).resolve().parents[1];BITS=64;SCALE=1<<BITS
NTEST=0
DEADLINE=None
def check(p):
    global NTEST
    NTEST+=1
    if DEADLINE is not None and time.perf_counter()>DEADLINE:raise TimeoutError('55-second frozen helper deadline')
    assert p
def radical(a,b):
    if not a or not b:return (0,0)
    z=(a*a)*(b**6)<<(4*BITS)
    low=isqrt(isqrt(z));high=low if low**4==z else low+1
    check(low**4<=z<=high**4)
    return low,high
@lru_cache(None)
def threshold(m,t):
    U,V,c=coefficients(m,t);low=high=0;D=1<<m
    for k in range(m):
        a,b=radical(abs(U[k]),abs(V[k]));low+=c[k]*a;high+=c[k]*b
        if k:check(k*c[k]*U[k]**2==(m-k)*c[k-1]*V[k-1]**2)
    alpha=2*comb(m-1,t-1)
    # L = 6*quarter; analytic upper bound is (69/2)*alpha.
    check(12*high<=69*alpha*D*SCALE)
    if m<=6:
        tab=[1-2*(x.bit_count()>=t) for x in range(D)];wa=fwht(tab)
        for s,a in enumerate(wa):check(a==(V[(s>>1).bit_count()] if s&1 else U[(s>>1).bit_count()]))
    return low,high,alpha
def tree(n):
    root_t=(n+1)//2;lo=hi=paid=0;D=1<<n
    for m in range(1,n+1):
        d=n-m
        for j in range(d+1):
            t=root_t-j
            if not 1<=t<=m:continue
            a,b,alpha=threshold(m,t);w=comb(d,j)*(1<<(n-m))
            lo+=w*a;hi+=w*b;paid+=comb(d,j)*alpha
    I=F(n*2*comb(n-1,(n-1)//2),D)
    check(F(paid,D)==I)
    lower=F(6*lo,SCALE*D*D);upper=F(6*hi,SCALE*D*D)
    check(upper<=F(69,2)*I)
    return {'n':n,'I':str(I),'L_over_I_lower':str(lower/I),'L_over_I_upper':str(upper/I)}
def move_first(tab,n,i):
    order=[i]+[j for j in range(n) if j!=i]
    return [tab[sum(((x>>j)&1)<<v for j,v in enumerate(order))] for x in range(1<<n)]
def admitted(tab):
    m=len(tab).bit_length()-1;out=[]
    for i in range(m):
        t=move_first(tab,m,i);r=m-1;D=1<<m;a=fwht(t)
        support=[x for x in range(1<<r) if t[2*x]!=t[2*x+1]]
        anti=all(not ((x&y)==x or (x&y)==y) for j,x in enumerate(support) for y in support[j+1:])
        A=[0]*(r+1);V=[0]*(r+1)
        low=high=0
        for s in range(1<<r):
            k=s.bit_count();u,v=a[2*s],a[2*s+1]
            A[k]+=u*u;V[k]+=v*v
            l,h=radical(abs(u),abs(v));low+=l;high+=h
        transport=all(k*A[k]<=(r-k+1)*V[k-1] for k in range(1,r+1))
        alpha=F(len(support),1<<r)
        if anti and transport:check(F(6*high,SCALE*D*D)<=F(69,2)*alpha)
        out.append({'coordinate':i,'antichain':anti,'degree_transport':transport,'influence':str(alpha),'admitted':anti and transport,'first_failed_level':next((k for k in range(1,r+1) if k*A[k]>(r-k+1)*V[k-1]),None)})
    return out
def mixed():
    rows=[];attempt=0;passcoords=0;totalcoords=0;children=0
    fixtures=[]
    for k in range(3):
        for mask in range(1<<(1<<k)):fixtures.append((k,mask))
    fixtures +=[(3,v) for v in [0,1,7,15,23,105,150,255]]
    check(len(fixtures)==30)
    for k,mask in fixtures:
        g=[1-2*((mask>>x)&1) for x in range(1<<k)]
        for m in [2,4]:
            n=m+k
            tab=[1 if m-2*(x&((1<<m)-1)).bit_count()+g[x>>m]>0 else -1 for x in range(1<<n)]
            coords=admitted(tab);attempt+=1;passcoords+=sum(x['admitted'] for x in coords);totalcoords+=len(coords)
            child_rows=[]
            for i in range(n):
                t=move_first(tab,n,i)
                for z in [0,1]:
                    child=t[z::2]
                    if len(set(child))==1:continue
                    c=admitted(child);children+=1
                    if not any(v['admitted'] for v in c):child_rows.append({'fixed_coordinate':i,'fixed_value':z,'remaining_coordinates':c})
            if not any(x['admitted'] for x in coords) or child_rows:
                rows.append({'core_dimension':k,'core_mask':mask,'outer_sign_inputs':m,'root_coordinates':coords,'children_with_no_admitted_coordinate':child_rows})
    return {'roots':attempt,'coordinate_cases':totalcoords,'admitted_root_coordinates':passcoords,'nonconstant_first_children':children,'obstructions':rows}
def main():
    global DEADLINE
    start=time.perf_counter();DEADLINE=start+55;pilot='--pilot' in sys.argv;maximum=6 if pilot else 33;mx=F(0);wit=None
    for m in range(1,maximum+1):
        for t in range(1,m+1):
            lo,hi,a=threshold(m,t);ratio=F(6*hi,SCALE*(1<<m)*a)
            if ratio>mx:mx=ratio;wit=[m,t]
    ns=[3,5,9,17] if pilot else [3,5,9,17,33]
    rows=[tree(n) for n in ns]
    mix={} if pilot else mixed()
    out={'status':'PASS','helper':'A078-quarter-profile-v2-bounded','mode':'pilot' if pilot else 'full','assertions':NTEST,'thresholds':maximum*(maximum+1)//2,'maximum_node_L_over_Inf_upper':str(mx),'maximum_node_witness':wit,'tree_rows':rows,'mixed_admission':mix,'fourth_root_enclosure_bits':BITS,'seconds':time.perf_counter()-start}
    (ROOT/'out'/('quarter_pilot.json' if pilot else 'quarter_full.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='mixed_admission'},indent=2));print('mixed_summary',json.dumps({k:v for k,v in mix.items() if k!='obstructions'}))
if __name__=='__main__':main()
