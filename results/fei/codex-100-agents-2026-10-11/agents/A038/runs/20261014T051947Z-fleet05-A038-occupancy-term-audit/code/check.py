import json,time,sys
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
R=Path(__file__).resolve().parents[1];START=time.monotonic();COUNT=0
def check(x):
    global COUNT
    COUNT+=1
    assert x,COUNT
    if time.monotonic()-START>58:raise RuntimeError('frozen watchdog')
def add(*terms):return sum((c*(a if c>=0 else b) for c,(a,b) in terms),F(0)),sum((c*(b if c>=0 else a) for c,(a,b) in terms),F(0))
@lru_cache(None)
def ln(q):
    t=(q-1)/(q+1);a=2*sum((t**(2*j+1)/F(2*j+1) for j in range(24)),F(0));return a,a+2*t**49/(49*(1-t*t))
L2=ln(F(2))
@lru_cache(None)
def lg(q):
    shift=0
    while q<1:q*=2;shift-=1
    while q>=2:q/=2;shift+=1
    a,b=ln(q);return shift+a/L2[1],shift+b/L2[0]
def eta(q):return add((-q,lg(q))) if q else (F(0),F(0))
def h(q):return add((1,eta(q)),(1,eta(1-q)))
def hi(a,b):
    vals=[h(a),h(b)];return min(z[0] for z in vals), F(1) if a<=F(1,2)<=b else max(z[1] for z in vals)
def enc(z):
    grid=10**30;a,b=z
    lo=(a*grid).numerator//(a*grid).denominator
    hi=-((-b*grid).numerator//(-b*grid).denominator)
    return [str(F(lo,grid)),str(F(hi,grid))]
def g(n,c):return 1-c-(1-F(8,15)*c)**2*(1-F(4,15)*c)**(n+1)
def root(n):
    a,b=F(3,4),F(1);check(g(n,a)>0 and g(n,b)<0)
    for _ in range(48):
        m=(a+b)/2
        if g(n,m)>0:a=m
        else:b=m
    check(g(n,a)>0 and g(n,b)<0);return a,b
def physical(n):
    # Direct actual reached function, x,a,b,y_1..y_n; no large tables.
    tab=[]
    for t in range(1<<(n+3)):
        x,a,b=[(t>>j)&1 for j in range(3)];v=-1 if (t>>3).bit_count()%2 else 1
        tab.append(-1 if x==0 and a else v if x==1 and b else 1)
    return tuple(tab)
def spectrum(t):return tuple(F(sum(v*(-1 if (a&s).bit_count()%2 else 1) for a,v in enumerate(t))**2,len(t)**2) for s in range(len(t)))
def influence(t,i):return F(sum(t[a]!=t[a^(1<<i)] for a in range(len(t))),len(t))
def raw(n):
    t=physical(n);children=[tuple(v for a,v in enumerate(t) if ((a>>1)&1)==b) for b in (0,1)];p=spectrum(t);ps=[spectrum(z) for z in children]
    check(sorted(z for z in p if z)==[F(1,16)]*8+[F(1,4)]*2)
    check(all(sorted(z for z in s if z)==[F(1,16)]*7+[F(9,16)] for s in ps))
    check(sum(influence(t,i) for i in range(n+3))==F(n+5,4))
    check([sum(influence(z,i) for i in range(n+2)) for z in children]==[F(n+2,4),F(n+4,4)])
    check(influence(t,1)==F(1,2))
    return {'n':n,'direct_character_sum':'PASS','parent_table':list(t),'child_tables':[list(z) for z in children]}
def main():
    pilot='--pilot' in sys.argv;ns=[1,2] if pilot else [1,2,3,4,8,16,32,64,128]
    check(2**159*11**44>3**108*5**60);check(2**79*11**22<3**54*5**30)
    check(2**16*7**14>3**9*5**15);check(7**7<3*2**19);check(3**9>2**14)
    K=add((1,h(F(1,4))),(-F(15,16),h(F(4,15))))
    check(K[0]>F(1,64) and K[1]<F(1,32))
    HC=add((1,(F(4),F(4))),(-F(9,8),lg(F(3))))
    rows=[]
    for n in ns:
        a,b=root(n);j1=hi(F(8,15)*a,F(8,15)*b);j2=hi(F(4,15)*a,F(4,15)*b);hc=hi(a,b)
        numerator=add((2,j1),(n+1,j2),(-1,hc));check(numerator[0]>0)
        Hmax=(numerator[0]/b,numerator[1]/a)
        Ent=add((1,h(F(15,16))),(F(15,16),Hmax));A=add((1,Ent),(-1,(F(3),F(3))))
        wa=(1-F(4,15)*b)**(n+1);wb=(1-F(4,15)*a)**(n+1)
        # Outcome q0=21/40-(8/75)c(1-4c/15)^(n+1), exact inherited root M.
        qlo=F(21,40)-F(8,75)*b*wb;qhi=F(21,40)-F(8,75)*a*wa
        def output(q):return add((-F(1,2),lg(4*q*(1-q))))
        oo=[output(qlo),output(qhi)];O=(F(0) if qlo<=F(1,2)<=qhi else min(v[0] for v in oo),max(v[1] for v in oo))
        TC=add((n+2,h(F(1,4))),(-1,HC));D=add((1,O),(1,TC),(-1,A))
        check(D[1]<F(n,8));check(D[0]>(F(n+1,64)-1))
        S=add((1,(F(n+3),F(n+3))),(-1,HC))
        check(F(n,8)<S[0]/8);check(S[0]>0)
        check(O[0]>=0 and A[0]>=0)
        rows.append({'n':n,'c_bracket':enc((a,b)),'root_occupancy_bank_A':enc(A),'O_occ':enc(O),'mean_child_TC':enc(TC),'conversion_debit_D':enc(D),'mean_child_entropy':enc(HC),'mean_child_influence':str(F(n+3,4)),'mean_price_four_child_surplus':enc(S),'max_conversion_payment':str(F(n,8)),'certified_child_surplus_fraction':'1/8'})
    result={'status':'PASS','arithmetic':'Fraction outward entropy/root intervals and exact integer signs','parameters':ns,'assertions':COUNT,'runtime_seconds':time.monotonic()-START,'k_interval':enc(K),'rows':rows,'direct_fixtures':[raw(n) for n in [1,2]]}
    result['assertions']=COUNT;result['runtime_seconds']=time.monotonic()-START
    (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:result[k] for k in ['status','parameters','assertions','runtime_seconds']}))
if __name__=='__main__':main()
