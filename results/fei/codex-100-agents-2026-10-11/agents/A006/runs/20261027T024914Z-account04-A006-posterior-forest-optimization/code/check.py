from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, product, permutations
from math import comb, prod
import json, time, sys

R=Path(__file__).resolve().parents[1]
start=time.monotonic(); checks=0
def ck(ok):
    global checks
    checks+=1
    if not ok: raise AssertionError(checks)

E=((0,1),(0,2),(1,2))
def runs(A):
    """Own reconstruction; a key records root draw and every chronological draw."""
    found={}
    for mask in range(8):
        M=tuple(i for i in range(3) if mask>>i&1)
        vertices=[v for i in M for v in E[i]]
        if len(vertices)!=len(set(vertices)) or not set(vertices)<=set(A):continue
        if any(set(e)<=set(A)-set(vertices) for e in E):continue
        matched={v:i for i in M for v in E[i]}
        U=tuple(v for v in A if v not in matched)
        options=[tuple(i for i,e in enumerate(E) if u in e) for u in U]
        for chosen in product(*options):
            own={i:E[i] for i in M}; roots=set(M);children={}
            for u,i in zip(U,chosen):
                ck(i not in own);own[i]=(u,)
                other=next(v for v in E[i] if v!=u)
                if other in matched:children.setdefault((matched[other],other),[]).append(i)
                else:roots.add(i)
            slots=[(i,u) for i in sorted(own) for u in own[i]]
            for ordering in product(*(tuple(permutations(children.get(k,[]))) for k in slots)):
                draws=dict(zip(slots,ordering));queue=sorted(roots);visits=[]
                c=F(1,4**len(roots))
                while queue:
                    i=queue.pop(0); B=own[i];s=len(B)
                    ch=tuple((u,j) for u in sorted(B) for j in draws[i,u]);k=len(ch)
                    c/=s*(s+1)*comb(2,s)*(k+1)*(k+2)*comb(s+k-1,k)
                    visits.append((i,tuple(B),ch));queue.extend(j for u,j in ch)
                key=(tuple(sorted(roots)),tuple(visits))
                ck(key not in found);found[key]=(sum(1<<i for i in own),c)
    return found

def monomial(mask,w):return prod((w[i] for i in range(3) if mask>>i&1),start=F(1))
def numer(rr,w):return sum((c*monomial(m,w) for m,c in rr.values()),F(0))
def D(w):return prod((1+x/4 for x in w),start=F(1))-1
def elementary(w):
    return sum(w),sum((w[i]*w[j] for i,j in combinations(range(3),2)),F(0)),prod(w)
def residual(w):
    s1,s2,s3=elementary(w);return 117*s1-242*s2+48*s3

# Small exact polynomial engine, four barycentric variables.
def add(*pp):
    out={}
    for p in pp:
        for k,v in p.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}
def scale(p,c):return {k:v*c for k,v in p.items() if v*c}
def mul(p,q):
    out={}
    for a,x in p.items():
        for b,y in q.items():
            k=tuple(u+v for u,v in zip(a,b));out[k]=out.get(k,F(0))+x*y
    return {k:v for k,v in out.items() if v}
def ev(p,x):return sum((v*prod((a**k for a,k in zip(x,e)),start=F(1)) for e,v in p.items()),F(0))

def ln_unit(x):
    z=(x-1)/(x+1);v=z;s=F(0)
    for j in range(30):s+=2*v/(2*j+1);v*=z*z
    return s,s+2*v/(61*(1-z*z))
LN2=ln_unit(F(2))
def lg(x):
    ck(x>0);k=x.numerator.bit_length()-x.denominator.bit_length();y=x/F(2)**k
    if y<1:k-=1;y*=2
    ck(1<=y<2);lo,hi=ln_unit(y)
    return F(k)+lo/LN2[1],F(k)+hi/LN2[0]

def main():
    allruns={A:runs(tuple(i for i in range(3) if A>>i&1)) for A in range(1,8)}
    ck(sum(map(len,allruns.values()))==15)
    truth=[1 if sum((x>>i)&1 for i in range(3))>=2 else -1 for x in range(8)]
    W=[sum(truth[x]*(-1)**((x&A).bit_count()) for x in range(8)) for A in range(8)]
    P={A:F(W[A]**2,64) for A in range(1,8) if W[A]}
    ck(P=={1:F(1,4),2:F(1,4),4:F(1,4),7:F(1,4)})
    I=F(sum(truth[x]!=truth[x^(1<<i)] for x in range(8) for i in range(3)),8)
    ck(I==F(3,2));ck(I==sum(p*A.bit_count() for A,p in P.items()))
    w0=(F(1,2),)*3
    q0={A:numer(allruns[A],w0)/D(w0) for A in range(1,8)}
    ck(all(q0[A]==F(16,217) for A in [1,2,4]));ck(q0[7]==F(1,651))
    rows=[]
    for w in [(F(1,2),)*3,(F(1,4),F(1,3),F(2,5)),(F(1,8),F(1,8),F(1,8))]:
        s1,s2,s3=elementary(w);qs={}
        for A,rr in allruns.items():
            expected=(sum(w[i] for i,e in enumerate(E) if (A.bit_length()-1) in e)/32 if A.bit_count()==1 else (w[E.index(tuple(i for i in range(3) if A>>i&1))]/48 if A.bit_count()==2 else s2/1152))
            ck(numer(rr,w)==expected)
            qs[A]=numer(rr,w)/D(w)
            # Aliases are duplicate descriptions, never extra generator events.
            descriptions=list(rr.items())+list(reversed(list(rr.items())))
            rebuilt=dict(descriptions)
            ck(rebuilt==rr);ck(numer(rebuilt,w)==numer(rr,w))
            ck(sum(c*monomial(m,w) for _,(m,c) in descriptions)==2*numer(rr,w))
        ck(sum(qs.values())<=1)
        score=sum((p*qs[A]/q0[A] for A,p in P.items()),F(0))
        ck(score==F(217,3072)*(3*s1+2*s2)/D(w))
        ck((1-score)*3072*D(w)==residual(w))
        ck(score<=1)
        rows.append({'weights':list(map(str,w)),'score':str(score),'residual':str(residual(w)),'subreference_mass':str(sum(qs.values()))})
    # Upper tetrahedron conv(e1,e2,e3,h), h=(1/2,1/2,1/2).
    variables=[{tuple(int(i==j) for i in range(4)):F(1)} for j in range(4)]
    L=add(*variables); lam=[add(variables[i],scale(variables[3],F(1,2))) for i in range(3)]
    s1=add(*lam);s2=add(*(mul(lam[i],lam[j]) for i,j in combinations(range(3),2)));s3=mul(mul(lam[0],lam[1]),lam[2])
    poly=add(scale(mul(s1,mul(L,L)),117),scale(mul(s2,L),-242),scale(s3,48))
    ck(all(v>=0 for v in poly.values()))
    ck(poly.get((0,0,0,3),0)==0)
    # Exact identities, also sampled at the boundary of each tetrahedron.
    grids=[(F(a,4),F(b,4),F(c,4),F(4-a-b-c,4)) for a in range(5) for b in range(5-a) for c in range(5-a-b)]
    for bary in grids:
        w=tuple(bary[i]+bary[3]/2 for i in range(3))
        ck(ev(poly,bary)==residual(w));ck(residual(w)>=0)
        w=tuple(bary[i] for i in range(3)); s1,s2,s3=elementary(w)
        sq=sum(x*x for x in w)
        cert=117*s1*(1-s1)+F(109,3)*s1*s1+F(242,3)*(sq-s2)+48*s3
        ck(residual(w)==cert);ck(residual(w)>=0)
    # Exact rational points cover the lower simplex checks; proof covers continua.
    ck(sum(q0.values())<1)
    # The old unconstrained used-root simplex still has a strictly positive gap.
    h=[]
    for mask in range(1,8):
        h.append(sum((p*sum((c for m,c in allruns[A].values() if m==mask),F(0))*4**mask.bit_count()/q0[A] for A,p in P.items()),F(0)))
    ck(max(h)-1==F(121,96))
    # Hypotheses matter: removing physical pair caps invalidates the dual.
    ck(residual((F(1),)*3)==-327)
    # A valid omitted all-singleton, three-root run changes the collection.
    omitted=(tuple(range(3)),((0,(0,),()),(1,(2,),()),(2,(1,),())))
    ck(omitted not in allruns[7])
    added=prod(w0)/F(32768)/D(w0)
    ck(added>0);ck(q0[7]+added>q0[7])
    lo1,hi1=lg(F(217,16));lo3,hi3=lg(F(651))
    cost=(F(3,4)*lo1+lo3/4,F(3,4)*hi1+hi3/4)
    refund_lo,refund_hi=lg(F(6))
    refund=(F(3,4)+refund_lo/4,F(3,4)+refund_hi/4)
    # Posterior is uniform among 2 runs for each singleton, 6 for the triple.
    for A,p in P.items():
        masses=[c*monomial(m,w0)/D(w0) for m,c in allruns[A].values()]
        ck(all(x==masses[0] for x in masses));ck(sum(masses)==q0[A])
        ck(len(masses)==(6 if A==7 else 2))
    result={'status':'PASS','helper_version':'A006-actual-run-polynomial-dual-v1','assertions':checks,'seconds':time.monotonic()-start,'actual_distinct_runs':sum(map(len,allruns.values())),'Boolean_truth':truth,'spectrum':{str(A):str(p) for A,p in P.items()},'I':str(I),'weight_cases':rows,'upper_tetrahedron_nonnegative_coefficients':{','.join(map(str,k)):str(v) for k,v in sorted(poly.items())},'candidate_Q':{str(A):str(q) for A,q in q0.items()},'optimal_cost_interval':list(map(str,cost)),'optimal_cost_over_I_interval':[str(x/I) for x in cost],'posterior_refund_interval':list(map(str,refund)),'old_root_simplex_gap_nats':'121/96','new_all_weight_and_mixture_gap':'0','boundary_grid_points_per_tetrahedron':len(grids),'controls':{'drop_incidence_caps_residual':'-327','omitted_valid_three_root_run_added_mass':str(added),'duplicate_description_naive_mass_factor':'2'}}
    ck(time.monotonic()-start<55)
    name='PILOT.json' if '--pilot' in sys.argv else 'CHECK.json'
    (R/'out'/name).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['status','assertions','seconds','actual_distinct_runs']}))
if __name__=='__main__':main()
