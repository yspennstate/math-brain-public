"""Stage10: actual signed core Walsh, fixed prior fusion, exact receipts."""
import argparse,collections,hashlib,itertools,json,math,runpy,time
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; AGENT=ROOT.parents[1]
OLD=AGENT/'runs/20261023T110145Z-account03-A015-minterm-barrier-analysis/code/check.py'
assert hashlib.sha256(OLD.read_bytes()).hexdigest()=='04ce00b6f18a13ad6f91be3c53c128e4f84407bdac6ca0394ceee603aca70eba'
H=runpy.run_path(str(OLD)); fw=H['fw']; inf=H['inf']; cevec=H['cevec']; addvec=H['addvec']; cost_bounds=H['cost_bounds']
START=time.monotonic(); counts=collections.Counter(); checks=0
def ck(x,tag):
    global checks
    assert x,tag
    checks+=1; counts[tag]+=1
    if time.monotonic()-START>55:raise RuntimeError('frozen55s runtime cap')
def expand(a,positions):return sum(((a>>j)&1)<<p for j,p in enumerate(positions))
def fusion(vals,core,mode,override=None,logs=True):
    n=(len(vals)-1).bit_length(); data=[i for i in range(n) if i not in core]; s=len(core); d=len(data)
    slices=[[vals[expand(z,core)|expand(x,data)] for x in range(1<<d)] for z in range(1<<s)]
    coeff=[fw(v) for v in slices]; q=[]; active=[]
    for z,v in enumerate(slices):
        if all(t==v[0] for t in v):q.append({}); continue
        if override is not None:qr=override[z]
        elif mode==0:qr={a:F(1,(1<<d)-1) for a in range(1,1<<d)}
        else:
            L=(1<<d)-1; qr={a:F((a+z)%L+1,L*(L+1)//2) for a in range(1,1<<d)}
        ck(sum(qr.values())==1,'slice_reference_normalized'); q.append(qr); active.append(z)
    k=len(active)
    qb={a:sum(q[z].get(a,F(0)) for z in active)/k if k else F(1,(1<<d)-1) for a in range(1,1<<d)}
    ck(sum(qb.values())==1 and all(t>0 for t in qb.values()),'qbar_positive_normalized')
    physical=fw(vals); pq=[]; M=N=Ix=Iz=F(0); sumQ=F(0)
    for a in range(1<<d):
        mass=F(0)
        for b in range(1<<s):
            t=expand(a,data)|expand(b,core)
            want=sum(((-1)**((z&b).bit_count()))*coeff[z][a] for z in range(1<<s))/(1<<s)
            ck(physical[t]==want,'signed_physical_Walsh')
            p=physical[t]**2; mass+=p
            if t==0:continue
            prob=qb[a]/(1<<(s+1)) if a else F(1,2*((1<<s)-1))
            pq.append((p,prob)); sumQ+=prob; Ix+=p*a.bit_count(); Iz+=p*b.bit_count()
            if a:M+=p
            else:N+=p
        ck(mass==sum(c[a]**2 for c in coeff)/(1<<s),'physical_Parseval_A')
    ck(sumQ==1,'full_Q_normalization')
    ck(Ix==sum(inf(v) for v in slices)/(1<<s),'actual_private_influence')
    ck(Ix+Iz==inf(vals),'actual_total_influence')
    ck(M<=Ix and N<=Iz,'physical_mass_budget')
    gamma=[]; avg=[]
    for z in active:
        for a in range(1,1<<d):
            p=coeff[z][a]**2/(1<<s)
            if not p:continue
            ck(qb[a]>=q[z][a]/k,'mixture_pointwise_header')
            avg.append((p,q[z][a])); gamma.append((p,qb[a]/q[z][a]))
    if logs:
        rhs=addvec((F(1),cevec(avg)),(F(1),cevec(gamma)),((s+1)*M,{2:F(1)}),(N,cevec([(F(1),F(1,2*((1<<s)-1)))])))
        ck(cevec(pq)==rhs,'complete_log_cost_identity')
    counts['fusion_cases']+=1
    return {'M':M,'N':N,'Ix':Ix,'Iz':Iz,'k':k,'q':q,'slices':slices,'physical':physical}
LOCAL={}
def local(widths):
    widths=tuple(widths)
    if widths in LOCAL:return LOCAL[widths]
    n=sum(widths); blocks=[]; sh=0
    for w in widths:blocks.append(((1<<w)-1)<<sh); sh+=w
    vals=[1 if all(x&B for B in blocks) else -1 for x in range(1<<n)]
    eps=[F(1,1<<w) for w in widths]; rho=[e/2 for e in eps]; Z=1-math.prod(1-t for t in rho)
    q={}
    for x in range(1,1<<n):
        q[x]=math.prod(rho[j]/((1<<w)-1) if x&blocks[j] else 1-rho[j] for j,w in enumerate(widths))/Z
    ck(sum(q.values())==1,'local_mask_normalized')
    a=math.prod(1-e for e in eps); I=2*a*sum(w*e/(1-e) for w,e in zip(widths,eps)); coeff=fw(vals)
    ck(inf(vals)==I,'local_pivotal_identity')
    moment=sum(coeff[x]**2*sum(w for w,B in zip(widths,blocks) if x&B) for x in range(1,1<<n))
    ck(moment==4*a*sum(w*e for w,e in zip(widths,eps)) and moment<=2*I,'local_occupation_identity')
    ck(4*a*(1-a)*sum(eps)<=2*I,'local_inactive_budget')
    ck(all((2*w+1)<=3*w for w in widths),'local_active_length_budget')
    LOCAL[widths]=(vals,q,blocks); return LOCAL[widths]
def physical(anchors,widths):
    s=2; sh=s; blocks=[]
    for w in widths:blocks.append(((1<<w)-1)<<sh); sh+=w
    vals=[1 if all((x&a) or (x&B) for a,B in zip(anchors,blocks)) else -1 for x in range(1<<sh)]
    refs=[]
    for z in range(4):
        active=[j for j,a in enumerate(anchors) if not z&a]
        if not active:refs.append({});continue
        ww=[widths[j] for j in active]; _,q,bb=local(ww)
        positions=[i-2 for j in active for i in range(blocks[j].bit_length()) if blocks[j]&(1<<i)]
        refs.append({expand(a,positions):p for a,p in q.items()})
    f=fusion(vals,[0,1],0,refs,False)
    for z,sl in enumerate(f['slices']):
        if not refs[z]:ck(inf(sl)==0,'constant_slice_zero_bill')
    counts['physical_core_functions']+=1
def source_review(widths):
    n=1+sum(widths); masks=[]; sh=1
    for w in widths:masks.append(1|(((1<<w)-1)<<sh));sh+=w
    mu={0:F(1)}; weighted={0:F(0)}; rho=F(0)
    for w,B in zip(widths,masks):
        t=F(1,1<<(w+1));rho+=t; coords=[i for i in range(n) if B>>i&1]
        localprob={expand(m,coords):(1-t if m==0 else t*t/(1-t)) for m in range(1<<len(coords))}
        nm=collections.defaultdict(F); nw=collections.defaultdict(F)
        for old,p in mu.items():
            for m,prob in localprob.items():
                nm[old|m]+=p*prob; nw[old|m]+=(weighted[old]+p*(m!=0))*prob
        mu=dict(nm);weighted=dict(nw)
    Q={a:p/rho for a,p in weighted.items() if a}; ck(sum(Q.values())==1,'source_union_DP_normalized')
    a=math.prod(1-F(1,1<<w) for w in widths)
    exact_atom=sum(F(1,(1<<(w+1))**2)/(1-F(1,1<<(w+1)))*math.prod((1-F(1,1<<(v+1))+F(1,(1<<(v+1))**2)/(1-F(1,1<<(v+1)))) for j,v in enumerate(widths) if j!=i) for i,w in enumerate(widths))/rho
    ck(Q[1]==exact_atom,'source_core_atom')
    vals=[1 if x&1 or all(x&(B^1) for B in masks) else -1 for x in range(1<<n)]
    P=fw(vals); J=a*sum(F(w,(1<<w)-1) for w in widths); I=inf(vals)
    ck(I==1-a+J,'source_physical_influence')
    bounds=cost_bounds((P[A]**2,(Q[A]+(A==1))/2) for A in Q)
    ck(F(bounds[1])<=F(29,2)*I,'source_complete_cost_interval')
    counts['source_review_functions']+=1
    return {'widths':widths,'cost_interval':bounds,'influence':str(I)}
def main():
    p=argparse.ArgumentParser();p.add_argument('--pilot',action='store_true'); pilot=p.parse_args().pilot
    if pilot:
        generic=[([1 if mask>>x&1 else -1 for x in range(4)],[i]) for mask in range(16) for i in range(2)]
    else:
        generic=[]
        for mask in range(256):
            v=[1 if mask>>x&1 else -1 for x in range(8)]
            for c in range(1,7):generic.append((v,[i for i in range(3) if c>>i&1]))
        for j in range(1024):
            mask=(j*65521)%65536; generic.append(([1 if mask>>x&1 else -1 for x in range(16)],[0,1]))
    for vals,core in generic:
        for mode in [0,1]:fusion(vals,core,mode)
    generic_count=counts['fusion_cases']
    lists=[(1,),(2,),(1,2)] if pilot else [w for r in range(1,4) for w in itertools.product(range(1,4),repeat=r)]
    for widths in lists:local(widths);counts['local_clause_functions']+=1
    if pilot:fixtures=[([1,2,3],[1,1,1]),([1,2,3],[1,2,1])]
    else:fixtures=[(aa,[w]*r) for r in range(1,4) for aa in itertools.product(range(4),repeat=r) for w in [1,2]]+[([1,2,3],[1,2,1])]
    for aa,ww in fixtures:physical(aa,ww)
    receipts=[]
    review=[(1,2)] if pilot else [w for r in range(1,4) for w in itertools.product([1,2],repeat=r)]
    for w in review:receipts.append(source_review(w))
    for r in ([4] if pilot else range(4,65)):
        q=F(1,7)*F(25,28)**(r-1); a=F(3,4)**r; I=1-a+F(r,2)*F(3,4)**(r-1)
        ck(a<F(1,2) and I<2 and q<F(1,1),'source_singleton_obstruction')
        counts['source_scalar_r']+=1
    for m in range(1,5 if pilot else 129):
        s=2*m+1; central=F(math.comb(2*m,m),4**m)
        ck(central*central*(m+1)<=1,'majority_dimension_certificate')
        ck(2*((1<<s)-1)>=(1<<s),'majority_uniform_cost_at_least_s')
        ck((2*m+1)**2*(m+2)<=4*(m+1)**3,'majority_induction_step')
        counts['majority_scalar']+=1
    for s in ([3] if pilot else [3,5,7,9]):
        vals=[1 if x.bit_count()>s//2 else -1 for x in range(1<<s)]
        ck(inf(vals)==F(s*math.comb(s-1,(s-1)//2),1<<(s-1)),'majority_actual_influence'); counts['majority_physical']+=1
    ck(inf([-1,1,1,1])==1 and F(2)*F(3,4)==F(3,2),'negative_independent_clone')
    ck(F(18,16)>1,'local_log_endpoint_certificate')
    out={'status':'PASS','helper_version':'A015-BOUNDED-CORE-FUSION@1','pilot':pilot,'assertions':checks,'generic_fusion_cases':generic_count,'counts':dict(counts),'source_cost_certificates':receipts,'elapsed_seconds':round(time.monotonic()-START,4),'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'pure_helper_sha256':hashlib.sha256(OLD.read_bytes()).hexdigest()}
    (ROOT/'out').mkdir(exist_ok=True);(ROOT/'out'/('pilot.json' if pilot else 'checks.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='source_cost_certificates'},indent=2))
if __name__=='__main__':main()
