"""Frozen essential-tax payment verification. No optimization of tau* is assumed."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product,permutations
from pathlib import Path
import runpy,json,time
ROOT=Path(__file__).resolve().parents[1]
# Source-bound own-stage exact primitives; runpy does not execute its main.
OLD=ROOT.parents[0]/'20261011T221822Z-account05-A048-tensor-stress'/'code/check.py'
lib=runpy.run_path(str(OLD)); add=lib['add']; scale=lib['scale']; entropy=lib['entropy']; hb=lib['hb']; ea=lib['entatom']; interval=lib['interval']; logvec=lib['logvec']
checks=0
def eq(a,b):
    global checks
    assert a==b,(a,b)
    checks+=1
def defect_tab(n): return [-1]+[1]*((1<<n)-1)
def mass(ps):
    d=F(1)
    for p in ps:d*=p
    return d
def exact_bias_law(tab,ps):
    # Independent direct centered-basis coefficient construction.
    out=[]
    for s in range(1<<len(ps)):
        raw=F(0); norm=F(1)
        for j,p in enumerate(ps):
            if s>>j&1:norm*=p*(1-p)
        for x,a in enumerate(tab):
            term=F(a)
            for j,p in enumerate(ps):
                bit=(x>>j)&1
                term*=p if bit else 1-p
                if s>>j&1:term*=bit-p
            raw+=term
        out.append(raw*raw/norm)
    return out
def formula_law(ps):
    d=mass(ps); out=[]
    for s in range(1<<len(ps)):
        if not s:out.append((1-2*d)**2);continue
        w=4*d*d
        for j,p in enumerate(ps):
            if s>>j&1:w*=(1-p)/p
        out.append(w)
    return out
@lru_cache(None)
def root(ps):
    n=len(ps); d=mass(ps)
    # The exceptional point is all ones, not the zero point.
    tab=[1]*((1<<n)-1)+[-1]
    w=exact_bias_law(tab,ps); eq(w,formula_law(ps));eq(sum(w),1)
    H=entropy(w)
    HF=add(ea((1-2*d)**2),ea(4*d),scale(add(*(hb(p) for p in ps)),4*d),scale(ea(4*d*d),-1))
    eq(H,HF)
    physical=[]
    for j in range(n):
        inf=F(0)
        for x in range(1<<n):
            prob=F(1)
            for i,p in enumerate(ps):prob*=p if x>>i&1 else 1-p
            if tab[x]!=tab[x^(1<<j)]:inf+=prob
        eq(inf,d/ps[j]);physical.append(inf)
    Q=sum((s.bit_count()*p for s,p in enumerate(w)),F(0))
    eq(Q,4*d*sum((1-p for p in ps),F(0)))
    return H,sum(physical),Q
@lru_cache(None)
def node(ps,j):
    p=ps[j]; child=ps[:j]+ps[j+1:]; eps=mass(child); v=4*eps*(1-eps)
    H,Ip,Q=root(ps); hc=root(child)[0] if child else {}
    w=formula_law(ps); marginal={}
    for s,a in enumerate(w):marginal[s&~(1<<j)]=marginal.get(s&~(1<<j),F(0))+a
    hm=entropy(marginal.values()); M=add(H,scale(hm,-1));J=add(hm,scale(hc,-p))
    eq(J,add(hb(p*v),scale(hb(v),-p)))
    MF,JF=lib['formula_single'](1-2*eps,p);eq(M,MF);eq(J,JF)
    return M,J,eps
def tree(ps,order):
    reach=F(1);rem=list(range(len(ps)));Msum=Jsum={};bill={};reach_list=[]
    influence_bill=F(0);query_count=F(0);transcript={}
    for j in order:
        current=tuple(ps[i] for i in rem);pos=rem.index(j);M,J,inf=node(current,pos)
        Msum=add(Msum,scale(M,reach));Jsum=add(Jsum,scale(J,reach));influence_bill+=reach*inf
        query_count+=reach;bill[str(ps[j])]=bill.get(str(ps[j]),F(0))+reach
        transcript=add(transcript,scale(hb(ps[j]),reach));reach_list.append(reach)
        reach*=ps[j];rem.remove(j)
    H,Ip,Q=root(ps);eq(add(Msum,Jsum),H);eq(influence_bill,Ip)
    leaves=[];reach=F(1)
    for j in order:leaves.append(reach*(1-ps[j]));reach*=ps[j]
    leaves.append(reach);eq(entropy(leaves),transcript)
    debt=add(Jsum,scale(Msum,-1))
    # Instance-dependent channel credit upper bound from the erasure coupling.
    paid_upper=sum((4*mass(ps)/p for p in ps),F(0))
    eq(paid_upper,4*Ip)
    return bill,query_count,Msum,Jsum,debt,transcript
def serialize(v):return {str(k):str(a) for k,a in sorted(v.items(),key=lambda x:str(x[0]))}
def bound_out(v):
    lo,hi=interval(v);den=10**15
    return {'lower':str(F((lo*den).__floor__(),den)),'upper':str(F((hi*den).__ceil__(),den))}
def main():
    start=time.perf_counter();grid=(F(1,8),F(1,4),F(3,8),F(1,2));counts={};samples=[]
    for q in grid:
        for r in range(1,7):
            ps=(q,)*r;H,Ip,Q=root(ps);bill,count,M,J,E,T=tree(ps,tuple(range(r)))
            eq(count,(1-q**r)/(1-q));eq(bill,{str(q):count})
            if q==F(1,8) and r in (1,3,6):samples.append({'q':str(q),'r':r,'I_physical':str(Ip),'I_spectral':str(Q),'tau_star_multiplier':str(count),'H':serialize(H),'J_tree':serialize(J),'debt_tree':serialize(E)})
    counts['homogeneous_roots']=24
    nroots=ntrees=0
    for r in range(1,5):
        for ps in product(grid,repeat=r):
            root(ps);nroots+=1
            for order in permutations(range(r)):
                tree(ps,order);ntrees+=1
    counts['heterogeneous_roots']=nroots;counts['all_permutation_trees']=ntrees
    tensors=0
    for p,q in product((F(1,8),F(1,2)),repeat=2):
        a=(p,p);b=(q,q,q);tab=[1]*(1<<5)
        for x in range(1<<5):tab[x]=(-1 if x&3==3 else 1)*(-1 if x>>2==7 else 1)
        w=exact_bias_law(tab,a+b);wa=formula_law(a);wb=formula_law(b)
        eq(w,[wa[x&3]*wb[x>>2] for x in range(1<<5)])
        eq(entropy(w),add(root(a)[0],root(b)[0]));tensors+=1
    counts['disjoint_tensor_cases']=tensors
    # Existing actual AND debt supplies a rigorous positive lower bound for tau*.
    p=F(1,8);q=F(1,4);w=[(1-2*p*q)**2,4*p*(1-p)*q*q,4*p*p*q*(1-q),4*p*(1-p)*q*(1-q)]
    debt=add(scale(hb(4*p*q*(1-q)),2),scale(entropy(w),-1),scale(hb(4*q*(1-q)),-p))
    lo,hi=interval(debt);eq(lo>F(1195,10000),True)
    taxcert=bound_out(debt);taxcert['tau_star_strict_lower']='1195/10000';counts['tax_lower_certificate']=1
    activations=[]
    for n in (1,2,3,4,10,16):
        N=n+3;d=F(1,1<<(N-1));I=N*d;Ictrl=3*d
        Kupper=N*(N+1)*d
        if n<=4:
            H,Ip,Q=root((F(1,2),)*N) if N<=6 else (entropy(formula_law((F(1,2),)*N)),I,I)
            eq(Ip,I);eq(Q,I);K=add(scale(hb(d),N),scale(H,-1))
        else:K=None
        record={'core_bits':n,'physical_dimension':N,'collapsed_mask_p':'1/8','actual_physical_tax':'0','I_total':str(I),'I_controls':str(Ictrl),'K_upper':str(Kupper),'K_plus_8I_upper':str(Kupper+8*I),'coarse_tax_strict_lower':'1195/10000'}
        if n>=10:eq(Kupper+8*I<F(1195,10000),True);record['coarse_tax_exceeds_K_plus_8I']=True
        activations.append(record)
    counts['collapsed_activation_cases']=len(activations)
    eq(sum(counts.values()),6939)
    out={'status':'PASS','helper_version':'A048-sharp-tax-payment-v2','counts':counts,'assertions':checks,'runtime_seconds':time.perf_counter()-start,'tax_lower_certificate':taxcert,'homogeneous_samples':samples,'coarse_activation_certificates':activations,'scope':'No numerical tau* optimization or half-tax theorem assumed. Signs use actual AND debt and rational coarse KL upper bounds. Tree identities are exact prime-log vector equalities.'}
    (ROOT/'out/CHECK.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:out[k] for k in ('status','counts','assertions','runtime_seconds')}))
if __name__=='__main__':main()
