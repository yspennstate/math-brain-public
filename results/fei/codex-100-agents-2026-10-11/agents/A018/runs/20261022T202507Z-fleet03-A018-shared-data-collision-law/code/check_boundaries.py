"""Independent physical Boolean and boundary checks for the frozen equal-mean theorem."""
from check_equal_mean import *
import check_equal_mean as c
# Frozen: one nonbalanced essential pair, one balanced pair, constants, and four
# mask truth tables (constant signs and signed three-bit point defects).
# No search: 2*3*3*4*2=144 explicitly prescribed complete-reference cases.
start=time.perf_counter();count=0
for ta,tb in [((-1,1,1,1),(1,-1,1,1)),((1,-1,1,-1),(-1,1,1,-1))]:
    aa,ab=walsh(ta),walsh(tb)
    for Qa in refs(probs(aa)):
        for Qb in refs(probs(ab)):
            ah,Qh=lift(aa,ab,Qa,Qb);Dcore=add(sc(F(1,2),add(kl(probs(aa),Qa),kl(probs(ab),Qb))),sc(-1,kl(probs(ah),Qh)))
            th=tuple(v for pair in zip(ta,tb) for v in pair)
            for ts in [(1,),(-1,),(-1,1,1,1,1,1,1,1),(1,-1,-1,-1,-1,-1,-1,-1)]:
                ss=walsh(ts);PP=probs(ss)
                tf=tuple(v for s in ts for h in th for v in (1,h*s))
                af=walsh(tf);ck(all(v in (-1,1) for v in tf))
                for Qs in (PP,tuple(F(1,len(PP)) for _ in PP)):
                    C,D=activation(ah,Qh,ss,Qs);Ca,Da=activation(aa,Qa,ss,Qs);Cb,Db=activation(ab,Qb,ss,Qs)
                    ck(ent(probs(af))==add(sc(F(1,2),add(ent(probs(ah)),ent(PP))),psi(ah[0]*ss[0])))
                    lam=add(sc(F(1,2),add(Da,Db)),sc(-1,D),sc(-F(1,2),Dcore));ck(nonneg(sc(-1,lam)))
                    count+=1
# Guard to equality hypothesis: opposed tiny means from A020's actual Boolean family.
# Prescribed k=3; no search or automatic enlargement.
k=3;N=2**(k+1);d=F(1,2**k)
t0=tuple(1 if x//2==0 else (1-2*(x%2)) for x in range(N))
t1=tuple(-1 if x//2==0 else (1-2*(x%2)) for x in range(N))
a0,a1=walsh(t0),walsh(t1);ck(a0[0]==d and a1[0]==-d)
Q0,Q1=refs(probs(a0))[1],refs(probs(a1))[1];ah,Qh=lift(a0,a1,Q0,Q1)
ss=walsh((-1,1,1,1));Qs=probs(ss)
dc=add(sc(F(1,2),add(kl(probs(a0),Q0),kl(probs(a1),Q1))),sc(-1,kl(probs(ah),Qh)))
_,D=activation(ah,Qh,ss,Qs);_,D0=activation(a0,Q0,ss,Qs);_,D1=activation(a1,Q1,ss,Qs)
L=add(sc(F(1,2),add(D0,D1)),sc(-1,D),sc(-F(1,2),dc));ck(interval(L)[0]>0)
result={'status':'PASS','boundary_cases':count,'opposed_mean_guard':{'k':k,'means':[str(d),str(-d)],'Lambda_positive':True,'Lambda':{str(p):str(v) for p,v in L.items()}},'assertions':c.checks,'seconds':time.perf_counter()-start}
(ROOT/'out'/'BOUNDARIES.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
