"""Preserved v1: finite checks reached interval stage, then frozen 60s cap; NOT a passing certificate."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import hashlib, importlib.util, json, time

R=Path(__file__).resolve().parents[1]
OLD=R.parent/'20261014T053514Z-account05-A083-formal-core'
spec=importlib.util.spec_from_file_location('prior', OLD/'code/reference_rows.py')
prior=importlib.util.module_from_spec(spec); spec.loader.exec_module(prior)
E=prior.E
START=time.perf_counter(); checks=0
def ck(v):
    global checks
    checks+=1
    if not v: raise AssertionError(checks)
    if time.perf_counter()-START>60: raise TimeoutError('frozen 60 seconds')
def save(name,v):
    (R/'out'/name).write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
def add(a,b): return a[0]+b[0],a[1]+b[1]
def scale(a,c): return a[0]*c,a[1]*c
def div(a,b):
    ck(b[0]>0)
    corners=[x/y for x in a for y in b]
    return min(corners),max(corners)
def kliv(p,q):
    out=(F(0),F(0))
    for a,(l,u) in zip(p,q):
        if a:
            ck(l>0)
            out=add(out,scale((E.log2_interval(a/u)[0],E.log2_interval(a/l)[1]),a))
    return out
def sumiv(xs):
    out=(F(0),F(0))
    for x in xs: out=add(out,x)
    return out
def eraseiv(q,i):
    out=[(F(0),F(0)) for _ in range(len(q)//2)]
    for s,a in enumerate(q):out[prior.erase(s,i)]=add(out[prior.erase(s,i)],a)
    return out
def branch(t,q,i):
    p=prior.spectral(t); pcs=[prior.spectral(prior.child(t,i,b)) for b in (0,1)]
    pe=[(pcs[0][s]+pcs[1][s])/2 for s in range(len(p)//2)]
    qe=eraseiv(q,i)
    K=[[pcs[b][s]/(2*pe[s]) if pe[s] else F(1,2) for s in range(len(pe))] for b in (0,1)]
    ck(all(K[0][s]+K[1][s]==1 for s in range(len(pe))))
    joint=[[scale(qe[s],K[b][s]) for s in range(len(pe))] for b in (0,1)]
    qb=[sumiv(row) for row in joint]
    refs=[[div(v,qb[b]) for v in joint[b]] for b in (0,1)]
    er=(F(0),F(0))
    for s,a in enumerate(p):
        if a:
            z=prior.erase(s,i)
            qr=div(q[s],qe[z])
            er=add(er,scale((E.log2_interval((a/pe[z])/qr[1])[0],E.log2_interval((a/pe[z])/qr[0])[1]),a))
    return pcs,refs,qb,K,er
def ref_interval(lo,hi):
    r=[F(8,15),F(8,15),F(4,15),F(4,15)]
    def prod(c):
        v=F(1)
        for a in r:v*=1-c*a
        return v
    Z=(1-prod(lo),1-prod(hi));out=[(F(1,16),F(1,16))]
    for s in range(1,16):
        l=u=F(15,16)
        for j,a in enumerate(r):
            l*=lo*a if s>>j&1 else 1-hi*a
            u*=hi*a if s>>j&1 else 1-lo*a
        out.append(div((l,u),Z))
    return out
def exact_reference(c):
    r=[F(8,15),F(8,15),F(4,15),F(4,15)]
    weights=[]
    for s in range(16):
        v=F(1)
        for j,a in enumerate(r):v*=c*a if s>>j&1 else 1-c*a
        weights.append(v)
    return [F(1,16)]+[F(15,16)*v/(1-weights[0]) for v in weights[1:]]
def spectral_direct(t):
    N=len(t)
    return tuple(F(sum(v*(-1)**((s&x).bit_count()) for x,v in enumerate(t)),N)**2 for s in range(N))
def influence(t):
    return F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t)) for i in range(len(t).bit_length()-1)),len(t))
def main():
    t=tuple((-1)**(x>>1&1) if not x&1 else 2*(x>>3&1)-1 if x>>2&1 else 1 for x in range(16))
    p=prior.spectral(t);ck(p==spectral_direct(t))
    ck(influence(t)==F(3,2))
    # Frozen domain: 17 rational c endpoints/interior; three fallback rules each.
    cases=[]
    for j in range(17):
        c=F(3,4)+F(j,256); q=exact_reference(c)
        ck(sum(q)==1)
        for mode in ['fair','0','1']:
            row,data=prior.query(t,2,4,q,mode)
            _,_,_,pcs,_,joint=data
            qb=[sum(x) for x in joint]
            refs=[[x/qb[b] for x in joint[b]] for b in (0,1)]
            tb=prior.child(t,2,1)
            row2,data2=prior.query(tb,2,3,refs[1],mode)
            _,pe2,_,pcs2,K2,_=data2
            ck(all(a==F(1,4) for a in pe2))
            ck(all(a==F(1,2) for rowk in K2 for a in rowk))
            ck(pcs2[0]==pcs2[1]==(F(1,4),)*4)
            ck(not row2['outcome_KL'])
            # Independent truth-table/character-sum and physical-edge checks.
            for leaf in [prior.child(t,2,0),prior.child(tb,2,0),prior.child(tb,2,1)]:
                ck(prior.spectral(leaf)==spectral_direct(leaf))
                ck(E.entropy_vector(prior.spectral(leaf))=={2:F(2)})
                ck(influence(leaf)==1)
            D=prior.kl(p,q)
            D0=prior.kl(pcs[0],refs[0]); D1=prior.kl(pcs[1],refs[1])
            Dleaf=E.mul(E.add(*(prior.kl(pcs2[b],[x/sum(data2[5][b]) for x in data2[5][b]]) for b in (0,1))),F(1,2))
            # y erasure cost equals the old conditional b=1 bill, hence half the mean booked bill after reach weighting.
            Y=E.add(D1,E.mul(Dleaf,F(-1)))
            if mode=='fair':
                C=E.mul(prior.vec_log(1/(1-4*c/15)),F(1,2))
                ck(Y==C)
                ck(prior.conditional(pcs[0],refs[0],4)==C)
            cases.append({'c':str(c),'fallback':mode,'Droot_log_vector':prior.serial(D),'Y_log_vector':prior.serial(Y)})
    # All-real c in [3/4,13/16], including the exact canonical root: interval splitting, no sample-to-continuum inference.
    bounds=[]
    for j in range(16):
        lo=F(3,4)+F(j,256);hi=lo+F(1,256)
        qi=ref_interval(lo,hi);D=kliv(p,qi)
        ck(D[1]<2)
        pcs,refs,qb,K,Eb=branch(t,qi,2)
        tb=prior.child(t,2,1)
        pc2,ref2,qby,Ky,Ey=branch(tb,refs[1],2)
        ck(all(k==F(1,2) for row in Ky for k in row))
        outcome=kliv([F(1,2)]*2,qb)
        leaves=add(scale(kliv(pcs[0],refs[0]),F(1,2)),scale(add(kliv(pc2[0],ref2[0]),kliv(pc2[1],ref2[1])),F(1,4)))
        separate=add(add(Eb,outcome),add(scale(Ey,F(1,2)),leaves))
        ck(separate[1]<2)
        bounds.append({'c_interval':[str(lo),str(hi)],'Droot':E.outward(D),'separate_full_tree_bills':E.outward(separate)})
    save('RESULT.json',{'status':'PASS','rational_cases':len(cases),'continuum_boxes':16,'assertions':checks,'prior_helper_assertions':prior.CHECKS,'seconds':time.perf_counter()-START,'arithmetic':'Fraction and certified log2 intervals; no floating point signs','same_owner_initial':3,'previous_conditional_booking':'C=-(1/2)log2(1-4c/15)','new_energy_booking':1,'full_tree_reference_debt_strict_upper':2,'remaining_reserve':'2-D(P||Q_c)>0','cases':cases,'continuum_bounds':bounds})
    print(json.dumps({'status':'PASS','assertions':checks,'prior_helper_assertions':prior.CHECKS,'rational_cases':len(cases),'continuum_boxes':16,'seconds':time.perf_counter()-START}))
if __name__=='__main__':main()
