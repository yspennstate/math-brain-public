from pathlib import Path
from fractions import Fraction as F
import time,sys,json,hashlib
import algebra as A
import log_intervals as V
R=Path(__file__).resolve().parents[1]
start=time.monotonic(); pilot='--pilot' in sys.argv
counts={'roots':0,'prefix_nodes':0,'converted_leaves':0,'complete_post_children':0,'seed_only_prefix_nodes':0,'projection_cases':0,'dyadic_cases':0}
def ck(x):
    A.ck(x)
    if time.monotonic()-start>55:raise TimeoutError('frozen 55-second cap')
def save(name,x):A.save(name,x)
def seed(L):
    return tuple(-1 if len({((x>>(j*L))&((1<<L)-1)).bit_count()%2 for j in range(3)})==1 else 1 for x in range(1<<(3*L)))
def independent_coeff(h,blocks):
    # Three-term pair polynomial, directly expanded; no transform is used here.
    masks=[sum(1<<i for i in b) for b in blocks]
    q={0:F(1,2)}
    for j,k in ((0,1),(0,2),(1,2)):q[masks[j]^masks[k]]=F(-1,2)
    return tuple(q.get(i,F(0)) for i in range(len(h)))
def subtree(h,q,s,left,depth,L,c0):
    v=A.wrap(A.ROW,bb,h,s);p=A.law(v)
    ck(A.ce(p,q)==c0)
    if left:
        counts['prefix_nodes']+=1
        ck(A.coef(h)[1]==0 and q==p)
        ck(all(A.coef(h)[i]*A.coef(h)[i^1]==0 for i in range(0,len(h),2)))
        pb=A.marginal(p,4);qb=A.marginal(q,4)
        ck(A.ent(p)==A.ent(pb) and pb==qb)
        for bit in (0,1):
            hh=A.restrict(h,0,bit);pp=A.law(A.wrap(A.ROW,bb,hh,s))
            ck(pp==pb)
            subtree(hh,qb,s,left-1,depth+1,L,c0)
    else:
        counts['converted_leaves']+=1
        ph=A.law(h);target=((1<<(2*L))-1)
        ck(ph[0]==F(1,4) and ph[target]==F(1,4))
        rr=tuple(F(1,4) if j==0 else F(1,3) if j==target else x*F(5,6) for j,x in enumerate(ph))
        ck(sum(rr)==1)
        qq=A.coherent(A.ROW,bb,h,rr,s)
        cost=A.add((1,A.ce(p,qq)),(-1,c0))
        ck(cost==delta)
        reserve=A.add((F(35,4)-F(1,4)-F(77,32),A.log(F(2))),(-1,c0),(-1,cost))
        ck(A.sign(reserve)>0)
        # Actual installed reference, actual next physical query, BOTH full children.
        pb=A.marginal(p,4);qb=A.marginal(qq,4)
        occ=A.add((1,A.kl(p,qq)),(-1,A.kl(pb,qb)))
        ck(A.sign(occ)>=0)
        childcost=[]
        for bit in (0,1):
            vv=A.restrict(v,4,bit);pp=A.law(vv)
            childcost.append(A.ce(pp,qb));counts['complete_post_children']+=1
            ck(sum(qb)==1 and sum(pp)==1)
        expr=A.add((1,A.ent(p)),(-1,A.ent(pb)),(F(1,2),childcost[0]),(F(1,2),childcost[1]),(-1,A.ce(p,qq)))
        ck(expr==A.add((-1,occ)))
bb=tuple(1-x*x for x in A.ROW)
ck(A.coef(A.ROW)==A.direct(A.ROW));ck(A.coef(bb)==A.direct(bb));ck(A.beta(bb)==F(3,8))
delta=A.add((F(3,32),A.log(F(27,25))))
source=[]
for L in ((1,) if pilot else (1,2)):
    h=seed(L);ck(A.coef(h)==independent_coeff(h,[range(j*L,(j+1)*L) for j in range(3)]))
    for s in (1,-1):
        counts['roots']+=1;v=A.wrap(A.ROW,bb,h,s);p=A.law(v);c0=A.ent(p)
        ac,bc=A.direct(A.ROW),A.direct(bb);hc=A.coef(h)
        expected=tuple(ac[u]+s*hc[0]*bc[u] if t==0 else s*bc[u]*hc[t] for t in range(len(h)) for u in range(16))
        ck(A.coef(v)==expected)
        influences=tuple(F(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v)) for i in range(4+3*L))
        ck(influences==((F(5,16),F(5,16),F(1,2),F(1,2)) if s==1 else (F(7,16),F(7,16),F(1,2),F(1,2)))+(F(3,16),)*(3*L))
        ck(F(35,4)<=4*sum(influences))
        ck(A.sign(A.add((6,A.log(F(2))),(-1,c0)))>=0)
        subtree(h,p,s,L,0,L,c0)
        if L==1:source.append((s,c0))
if not pilot:
    def seedwalk(h,left):
        if not left:return
        counts['seed_only_prefix_nodes']+=1
        c=A.coef(h);p=A.law(h);pb=A.marginal(p,0)
        ck(c[1]==0 and all(c[i]*c[i^1]==0 for i in range(0,len(h),2)))
        ck(A.ent(p)==A.ent(pb))
        for bit in (0,1):
            hh=A.restrict(h,0,bit);ck(A.law(hh)==pb);seedwalk(hh,left-1)
    for L in (3,4):seedwalk(seed(L),L)
# The exact projection theorem's previously excluded endpoints, including a ghost-only A.
endpoint=[]
for r in (F(0),F(1,4),F(1,2)):
    t=1-r
    for j in range(int(4*t)+1):
        a=F(j,4);b=t-a;p=(r,a,F(0),b)
        for e in range(int(8*a),int(8*t)+1):
            ell=F(e,8);counts['projection_cases']+=1
            if ell==t and b>0:
                # All admissible q have q(complement)=0 on positive actual mass.
                endpoint.append({'r':r,'a':a,'ell':ell,'cost':'INFINITE'})
                ck(b>0);continue
            if ell<=a:q=p
            elif a==0:q=(r,F(0),ell,t-ell) # The entire floor sits on a reference-only atom.
            else:q=(r,ell,F(0),t-ell)
            ck(sum(q)==1 and q[1]+q[2]>=ell)
            cost=A.kl(p,q)
            if ell>a:ck(A.sign(cost)>0)
            else:ck(cost=={})
            # Check every eighth-grid coherent target with fixed vacuum and floor.
            for z in range(e,int(8*t)+1):
                for ghost in range(z+1):
                    qq=(r,F(z-ghost,8),F(ghost,8),t-F(z,8))
                    if any(x and y==0 for x,y in zip(p,qq)):continue
                    ck(A.sign(A.add((1,A.kl(p,qq)),(-1,cost)))>=0)
            endpoint.append({'r':r,'a':a,'ell':ell,'minimum_prime_log':cost})
save('ENDPOINTS.json',{'status':'PASS','cases':endpoint,'zero_tail':'r=1, only ell=0 feasible, cost0; positive floor infeasible','ell_below_actual':'q=p already admissible; minimum0'})
# A finite original budget cannot pay arbitrary strengthening of the declared floor.
frontier=[]
for s,c0 in source:
    c_iv=A.interval(c0)
    for omega in (F(0),F(1,4)):
        first=None;records=[]
        for k in range(1,65):
            ell=F(3,4)-F(1,1<<k)
            # k1 gives ell=a; exact cost0. All subsequent floors are strict interior.
            costiv=V.mul(V.exact(F(3,32)),V.add(V.exact(F(2*k-4)),V.neg(V.lg(ell))))
            margin=V.diff(V.exact(F(35,4)-omega),V.add(c_iv,costiv))
            if k==1:ck(costiv[0]<=0<=costiv[1]);paid=True
            else:ck(margin[0]>0 or margin[1]<0);paid=margin[0]>0
            if not paid and first is None:first=k
            counts['dyadic_cases']+=1
            if k in (1,64) or not paid and (not records or records[-1].get('paid',True)):
                records.append({'k':k,'floor':ell,'cost_interval':V.serial(costiv),'margin_interval':V.serial(margin),'paid':paid})
        ck(first is not None)
        frontier.append({'sign':s,'old_booking':omega,'source_ce_prime_log':c0,'source_ce_interval':V.serial(c_iv),'first_unpaid_k_within_fixed_dyadic_family':first,'records':records})
save('FLOOR_FRONTIER.json',{'status':'PASS','family':'ell_k=3/4-2^-k; k=1..64, fixed in advance','rows':frontier,'interpretation':'No change to A097 fixed1/3 theorem; arbitrary-floor extension fails on SAME original account; no claim of global necessity or FEI counterexample'})
out={'status':'PASS','pilot':pilot,'assertions':A.checks,'counts':counts,'seconds':time.monotonic()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'formal_verification':'NOT_CLAIMED'}
save('PILOT.json' if pilot else 'VALIDATION.json',out);print(json.dumps(out))
