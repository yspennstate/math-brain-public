from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import prod
import json,time
root=Path(__file__).resolve().parents[1];(root/'out').mkdir(exist_ok=True)
start=time.perf_counter();checks=0
def ck(x):
    global checks
    assert x
    checks+=1
def raw(v):
    return [sum(x*(-1)**((s&y).bit_count()) for y,x in enumerate(v)) for s in range(len(v))]
rejections=[]
for ratio,c in [(2,2),(3,1)]:
    magnitudes=[c*ratio**((s&3).bit_count()) for s in range(8)]
    ck(sum(x*x for x in magnitudes)==8*25)
    for phase in range(256):
        W=[x*(-1 if phase>>s&1 else 1) for s,x in enumerate(magnitudes)]
        inv=raw(W)
        bad=next((y for y,x in enumerate(inv) if x%8 or abs(x)>16),None)
        ck(bad is not None)
        rejections.append({'ratio':ratio,'scale':c,'phase':phase,'first_bad_point':bad,'inverse_numerator':inv[bad],'denominator':8})
(root/'out'/'endpoint_rejections.json').write_text(json.dumps(rejections,indent=2),encoding='utf-8')
norm125=[]
for ratios in product((2,3),repeat=3):
    B=ratios.count(3)
    if B not in (1,3):reason='Parseval scale squared is not an integer square power of two'
    elif B==1:
        c=2;mag=[c*prod(ratios[i] if s>>i&1 else 1 for i in range(3)) for s in range(32)]
        ck(sum(x*x for x in mag)==32*125);ck(all(x%2==0 for x in mag));reason='All raw coefficients even; singleton mixed mask forces every coefficient odd'
    else:
        c=1;mag=[3**(s&7).bit_count() for s in range(32)]
        ck(sum(x*x for x in mag)==32*125);ck(96%27!=0);reason='Full-complement magnitude27 does not divide required signed sum96'
    norm125.append({'ratios':ratios,'B':B,'reason':reason})
onebit=[]
for h in product(range(-2,3),repeat=2):
    W=raw(h)
    if not all(W) or abs(W[0])==abs(W[1]):continue
    ck(F(max(map(abs,W)),min(map(abs,W)))==3)
    ck(sorted(map(abs,h))==[1,2]);onebit.append({'h':h,'W':W})
ck(5**4>2*4**4);ck(F(5,4)>1);ck(125>64);ck(25>16)
ck(128>121);ck(5**10>2**23);ck(3**5<2**8);ck(65**2<2*64**2)
# Explicit regression for the withdrawn summation inference, not Boolean admission.
t=1;te=(2,2,2,-7);D=9
ck(sum(te)==-t);ck(all((t+4*x)%D==0 for x in te));ck((3*t)%D!=0)
regression={'t':t,'t_J':te,'D_J':[D]*4,'sum_individual_terms':sum(t+4*x for x in te),'coupled_clause':'withdrawn; arithmetic nonimplication only, not a Boolean counterexample'}

# Rational log bounds: atanh remainder after20 terms, scale into[1,2].
def ln_unit(x):
    z=(x-1)/(x+1);v=2*sum(z**(2*j+1)/F(2*j+1) for j in range(20))
    return v,v+2*z**41/(41*(1-z*z))
ln2=ln_unit(F(2))
def log2(x):
    k=0
    while x<1:x*=2;k-=1
    while x>2:x/=2;k+=1
    lo,hi=ln_unit(x)
    return F(k)+lo/ln2[1],F(k)+hi/ln2[0]
def ent(ps):
    lo=hi=F(0)
    for p in ps:
        if p:
            a,b=log2(p);lo-=p*b;hi-=p*a
    return lo,hi
def ser(v):return [str(x) for x in v]
b=ent([F(1,10),F(9,10)]);Kc=(F(3,2)+F(5,2)*b[0],F(3,2)+F(5,2)*b[1])
l=log2(F(65,64));Ka=(6+2*l[0],6+2*l[1])
ck(Kc[0]>F(5,2));ck(Kc[1]<7);ck(Ka[1]<7)
source=Path(r'~\brain_workers\FEI100_20261011\agents\A032\runs\20261013T221334Z-fleet05-A032-boolean-phase-realizability\out\witness.json')
fixtures=[('three_bit_point_defect',[-1]+[1]*7),('A032_six_bit_cubic',json.loads(source.read_text(encoding='utf-8'))['truth_table'])]
actual=[]
for name,f in fixtures:
    L=len(f);n=L.bit_length()-1;P=L//4;m=n-2
    ck(all(abs(x)==1 for x in f));WF=raw(f);ck(sum(x*x for x in WF)==L*L)
    influence=[sum(F(WF[s]**2,L*L) for s in range(L) if s>>i&1) for i in range(n)]
    edges=[F(sum(f[x]!=f[x^(1<<i)] for x in range(L)),L) for i in range(n)]
    ck(influence==edges);IX=sum(influence[:2]);IY=sum(influence[2:])
    rows=[];conditional_lo=conditional_hi=F(0);Q=F(0);mass=[]
    for J in range(4):
        h=[]
        for y in range(P):
            numerator=sum(f[x+4*y]*(-1)**((x&J).bit_count()) for x in range(4))
            ck(numerator%2==0);h.append(numerator//2)
        W=raw(h);ck(all(WF[J+4*s]==2*W[s] for s in range(P)))
        w=F(sum(x*x for x in h),4*P);mass.append(w)
        if not w:continue
        sq=[F(x*x,sum(v*v for v in W)) for x in W]
        q=[sum(sq[s] for s in range(P) if s>>i&1) for i in range(m)]
        ck(all(sq[s]==prod(q[i] if s>>i&1 else 1-q[i] for i in range(m)) for s in range(P)))
        N=sum(x not in (0,F(1,2),1) for x in q);fair=q.count(F(1,2))
        ck(fair>=N or (N==1 and fair==0))
        ep=ent(sq);conditional_lo+=w*ep[0];conditional_hi+=w*ep[1];Q+=w*N
        rows.append({'J':J,'w':str(w),'N':N,'fair':fair,'marginals':[str(x) for x in q]})
    full=ent([F(x*x,L*L) for x in WF]);address=ent(mass)
    ck(address[0]+conditional_lo<=full[1]);ck(full[0]<=address[1]+conditional_hi)
    ck(full[1]<Ka[0]*(IX+IY));ck(Q<=F(5,2)*IY)
    if name=='three_bit_point_defect':
        ck(IY==F(1,4));ck(Q==F(5,8));ck(mass==[F(5,8),F(1,8),F(1,8),F(1,8)])
        # Equality is an exact entropy signature, not a rounded interval sign.
        ck(F(5,8)/IY==F(5,2) and F(3,8)/IY==F(3,2))
    else:ck(conditional_hi<Kc[0]*IY)
    actual.append({'name':name,'rows':rows,'I_X':str(IX),'I_Y':str(IY),'Q':str(Q),'full_entropy_interval':ser(full),'conditional_entropy_interval':ser((conditional_lo,conditional_hi))})
out={'status':'PASS','phase_endpoint_cases':len(rejections),'norm125_templates':norm125,'one_bit_nonfair_rows':onebit,'regression':regression,'actual_fixtures':actual,'Kcond_interval':ser(Kc),'Kall_interval':ser(Ka),'assertions':checks,'runtime_seconds':time.perf_counter()-start}
(root/'out'/'validation.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':'PASS','phase_endpoint_cases':len(rejections),'norm125_templates':len(norm125),'actual_Boolean_fixtures':len(actual),'assertions':checks,'runtime_seconds':out['runtime_seconds']},indent=2))
