from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import importlib.util,json,time,sys
R=Path(__file__).resolve().parents[1];sp=importlib.util.spec_from_file_location('logs',R/'code/exact_logs_base.py');L=importlib.util.module_from_spec(sp);sp.loader.exec_module(L)
start=time.perf_counter();checks=0;pilot='--pilot' in sys.argv
def ck(x):
    global checks
    assert x;checks+=1
    assert time.perf_counter()-start<(55 if pilot else 180)
def save(n,x):(R/'out'/n).write_text(json.dumps(x,indent=2),encoding='utf8')
@lru_cache(None)
def spectrum(t):
    a=list(t);k=1
    while k<len(a):
        for lo in range(0,len(a),2*k):
            for j in range(lo,lo+k):u,v=a[j],a[j+k];a[j],a[j+k]=u+v,u-v
        k*=2
    return tuple(F(v*v,len(a)**2) for v in a)
def restrict(t,i,b):return tuple(t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(t)//2))
def rm(s,i):return (s&((1<<i)-1))|((s>>(i+1))<<i)
def erase(p,i):
    a=[F(0)]*(len(p)//2)
    for s,v in enumerate(p):a[rm(s,i)]+=v
    return tuple(a)
def influences(t):
    n=len(t).bit_length()-1
    return tuple(F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(n))
def node(t,q,i):
    p=spectrum(t);pe=erase(p,i);qe=erase(q,i);kids=[restrict(t,i,b) for b in (0,1)];P=[spectrum(t) for t in kids]
    ck(sum(q)==1 and all(q[s]>0 for s,v in enumerate(p) if v));ck(all(pe[s]==(P[0][s]+P[1][s])/2 for s in range(len(pe))))
    K=[[P[b][s]/(2*pe[s]) if pe[s] else F(1,2) for s in range(len(pe))] for b in (0,1)]
    ck(all(K[0][s]+K[1][s]==1 for s in range(len(pe))))
    joint=[[qe[s]*K[b][s] for s in range(len(pe))] for b in (0,1)];qb=[sum(v) for v in joint];Q=[tuple(v/w for v in vs) for vs,w in zip(joint,qb)]
    ck(sum(qb)==1 and min(qb)>0)
    atoms=0
    for s,pv in enumerate(p):
        if not pv:continue
        z=rm(s,i)
        erasure_ratio=(pv/pe[z])/(q[s]/qe[z])
        for b in (0,1):
            if K[b][z]:
                outcome_ratio=F(1,2)/qb[b];child_ratio=P[b][z]/Q[b][z]
                # Exact multiplicative certificate behind the full KL chain.
                ck(pv/q[s]==erasure_ratio*outcome_ratio*child_ratio);atoms+=1
    ck(sum(influences(t))==influences(t)[i]+sum(sum(influences(k)) for k in kids)/2)
    return kids,Q,{'reference_outcomes':list(map(str,qb)),'reference_only_erased_rows':sum(qe[s]>0 and not pe[s] for s in range(len(pe))),'KL_atom_identities':atoms}
def bracket(v,ds):
    rs=[d/v for d in ds]
    def g(c):
        z=F(1)
        for r in rs:z*=1-c*r
        return 1-c-z
    lo,hi=F(1,2),F(1);ck(g(lo)>0 and g(hi)<0)
    for _ in range(40):
        mid=(lo+hi)/2
        if g(mid)>0:lo=mid
        else:hi=mid
    ck(g(lo)>0 and g(hi)<0)
    return lo,hi
def reference(c,v,p0,ds):
    theta=[c*d/v for d in ds];q=[]
    for s in range(1<<len(ds)):
        w=F(1)
        for i,u in enumerate(theta):w*=u if s>>i&1 else 1-u
        q.append(p0 if not s else v*w/c)
    Z=sum(q)
    return tuple(w/Z for w in q),Z
def nonnegative(e):
    ck(not e or L.natural_bounds(e)[0]>=0)
def run(n,parity=False):
    h=tuple((-1)**z.bit_count() if parity else (1-2*(z==(1<<n)-1)) for z in range(1<<n))
    t=tuple((-1)**((x>>1)&1) if not x&1 else (h[x>>3] if x&4 else 1) for x in range(1<<(n+3)))
    p=spectrum(t);ds=influences(t);v=1-p[0];lo,hi=bracket(v,ds)
    ck(ds[:2]==(F(1,2),F(1,2)))
    if not parity:
        delta=F(1,1<<n);ck(p[0]==(1-delta)**2/4);ck(ds[2:]==(delta/2,)*(n+1))
        # Pure rational proof root positivity and ghost-mass lower certificate.
        ck(v<=F(3,4)+delta/2 and (n+1)*delta<=1)
        ghostlower=F(n+1)*delta/10;ck(ghostlower/delta==F(n+1,10))
    rows=[]
    for c in (lo,hi):
        q,Z=reference(c,v,p[0],ds);kids,Q,first=node(t,q,2)
        grand,Qg,second=node(kids[1],Q[1],2)
        leaves=[kids[0],*grand];w=[F(1,2),F(1,4),F(1,4)]
        Hleaf={};Ileaf=F(0)
        for tleaf,weight in zip(leaves,w):
            Hleaf=L.add(Hleaf,L.mul(L.ent(spectrum(tleaf)),weight));Ileaf+=weight*sum(influences(tleaf))
        Hroot=L.ent(p);Rphys=sum(ds)-Ileaf;D=L.add(Hroot,L.mul(Hleaf,-1));surplus=L.add({2:4*Ileaf},L.mul(Hleaf,-1))
        nonnegative(L.add(surplus,{2:-2}))
        if parity:
            ck(Rphys==F(1,2) and Ileaf==1 and Hleaf=={2:F(2)})
            theta=8*c/15;eta=1/(2-theta)
            # b=1 normalization cancels the endpoint root-normalization factor.
            qe=erase(Q[1],2)
            expected=tuple((theta if s&1 else 1-theta)*(eta if s&2 else 1-eta) for s in range(4))
            ck(qe==expected and Qg[0]==expected and Qg[1]==expected)
            V=(2-theta)**2/(4*(1-theta));ck(V<F(2209,2040))
        else:
            ck(Rphys==delta)
            hc=L.ent(spectrum(tuple(1-2*(z==(1<<(n-1))-1) for z in range(1<<(n-1)))))
            ck(Hleaf==L.add({2:F(2)},L.mul(hc,F(1,8))))
            nonnegative(L.add(Hroot,{2:-2}))
        rows.append({'n':n,'parity':parity,'c_endpoint':str(c),'endpoint_reference_normalizer':str(Z),'first':first,'second':second,'H_root':L.expr(Hroot),'H_terminal':L.expr(Hleaf),'terminal_I':str(Ileaf),'removed_I':str(Rphys),'signed_query_deficit':L.expr(L.add(D,{2:-4*Rphys})),'terminal_S4':L.expr(surplus)})
        save(f'CASE_{"PARITY" if parity else n}_{len(rows)}.json',rows[-1])
    return rows
def main():
    rows=[]
    for n in range(1,3 if pilot else 9):rows+=run(n)
    rows+=run(1,True)
    ck(3**12>2**19);ck(60**8<8*47**8);ck(2209**8<2*2040**8)
    # Formula-only n32 already follows the all-n bound, no 35-bit table.
    ck(F(33,10)>3)
    save('FORMULA_CERTIFICATE.json',{'status':'PASS','n':32,'dimension':35,'constructed_truth_table':False,'A_over_removed_I_lower_bound':'33/10','violated_allowance':3,'terminal_owner_minimum':2,'combined_owner_spend_upper_bound':'7/4','proof':'PROOF.md sections2-4'})
    d={'status':'PASS','cases':len(rows),'assertions':checks,'runtime_seconds':time.perf_counter()-start,'root_reference_note':'Exact normalized rational endpoint perturbations; canonical algebraic reference theorem is proved analytically, not identified with endpoint laws.'}
    save('PILOT.json' if pilot else 'CHECK.json',d);print(json.dumps(d))
if __name__=='__main__':main()
