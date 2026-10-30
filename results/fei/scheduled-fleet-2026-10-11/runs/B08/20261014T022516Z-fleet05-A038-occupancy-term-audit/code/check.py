import importlib.util,itertools,json,time,sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
ROOT=Path(__file__).resolve().parents[1]
P=ROOT.parents[0]/'20261013T223535Z-fleet05-A038-occupancy-term-audit'/'code'/'check.py'
spec=importlib.util.spec_from_file_location('a038_exact',P);E=importlib.util.module_from_spec(spec);spec.loader.exec_module(E)
START=time.monotonic();COUNT=0
def check(ok):
    global COUNT
    COUNT+=1
    if not ok:raise AssertionError(COUNT)
    if time.monotonic()-START>58:raise RuntimeError('58-second frozen watchdog')
def add(*pairs):return sum((c*(lo if c>=0 else hi) for c,(lo,hi) in pairs),F(0)),sum((c*(hi if c>=0 else lo) for c,(lo,hi) in pairs),F(0))
@lru_cache(None)
def ln(q):
    z=(q-1)/(q+1);v=sum((z**(2*k+1)/F(2*k+1) for k in range(20)),F(0))*2
    return v,v+2*z**41/(41*(1-z*z))
L2=ln(F(2))
@lru_cache(None)
def lg(q):
    shift=0
    while q<1:q*=2;shift-=1
    while q>=2:q/=2;shift+=1
    a,b=ln(q);return shift+a/L2[1],shift+b/L2[0]
def out(pair):return [str(x) for x in pair]
def h(q):return E.entropy([q,1-q])
def labels(o):return tuple(1 if x==0 and a else 2 if x==o and b else 0 for b in (0,1) for a in (0,1) for x in (0,1))
@lru_cache(None)
def node(labs,u,v,i):
    st=(labs,u,v);table=E.physical(st);kids=[E.child(st,i,b) for b in (0,1)];ps=[E.law(E.physical(s)) for s in kids];q=tuple((a+b)/2 for a,b in zip(*ps));n=len(q).bit_length()-1
    ds=[sum((p[t] for t in range(len(p)) if t&(1<<j)),F(0)) for p in [q]+ps for j in range(n)]
    par=ds[:n];ch=[ds[n:2*n],ds[2*n:]]
    Q=tuple(__import__('functools').reduce(lambda a,b:a*b,[(d if t&(1<<j) else 1-d) for j,d in enumerate(par)],F(1)) for t in range(len(q)))
    ks=[ps[0][t]/(2*q[t]) if q[t] else F(1,2) for t in range(len(q))]
    a=sum((Q[t]*ks[t] for t in range(len(q))),F(0));check(0<a<1);check(sum(Q)==1)
    check(all(q[t]*ks[t]==ps[0][t]/2 for t in range(len(q))))
    # Same kernel used for the source q and reference Q, including zero-fiber extension.
    Qpost=[[Q[t]*(ks[t] if y==0 else 1-ks[t])/(a if y==0 else 1-a) for t in range(len(q))] for y in (0,1)]
    check(all(sum(z)==1 for z in Qpost))
    gamma=E.vec(*[(1,h(d)) for d in par],*[(F(-1,2),h(d)) for row in ch for d in row])
    js=E.vec((1,E.entropy(q)),(-F(1,2),E.entropy(ps[0])),(-F(1,2),E.entropy(ps[1])))
    release=E.vec((1,E.reserve(st)),(-F(1,2),E.reserve(kids[0])),(-F(1,2),E.reserve(kids[1])))
    O=add((F(-1,2),lg(4*a*(1-a))));rho=add((1,O),(1,E.interval(js)),(-1,E.interval(gamma)))
    gap=add((1,rho),(-1,E.interval(release)))
    check(E.nonnegative(js));check(E.nonnegative(gamma));check(E.nonnegative(release))
    # Independently reconstruct the log part of the direct Bayes reset by
    # expanding Q into its individual Bernoulli factors; leave outcome logs explicit.
    direct=()
    for y in (0,1):
        for t,p in enumerate(ps[y]):
            if not p:continue
            k=ks[t] if y==0 else 1-ks[t]
            check(k>0 and Qpost[y][t]>0)
            direct=E.vec((1,direct),(p/2,E.lograt(k)))
            for j,d in enumerate(par):
                r=d if t&(1<<j) else 1-d;s=ch[y][j] if t&(1<<j) else 1-ch[y][j]
                check(r>0 and s>0)
                direct=E.vec((1,direct),(p/2,E.lograt(r)),(-p/2,E.lograt(s)))
    direct_out=add((1,E.interval(direct)),(F(-1,2),lg(a)),(F(-1,2),lg(1-a)))
    # The outcome term O=-1/2 log(a)-1/2 log(1-a)-1 exactly;
    # hence the remaining exact prime-log comparison is direct=JS-Gamma-1.
    check(direct==E.vec((1,js),(-1,gamma),(-1,E.rational(1))))
    check(direct_out[0]<=rho[1] and rho[0]<=direct_out[1])
    return {'q_reference_0':str(a),'outcome_KL':out(O),'JS':out(E.interval(js)),'Gamma':out(E.interval(gamma)),'rho':out(rho),'kappa':out(E.interval(release)),'rho_minus_kappa':out(gap),'query_influence':str(E.influence(table,i)),'parent_entropy':out(E.interval(E.entropy(E.law(table)))),'child_entropy_average':out(E.interval(E.vec((F(1,2),E.entropy(ps[0])),(F(1,2),E.entropy(ps[1]))))),'child_tables':[list(E.physical(s)) for s in kids]},gap
def main():
    pilot='--pilot' in sys.argv;cores=list(itertools.product((-1,1),repeat=4));uc=cores[:2] if pilot else cores;vc=cores[:4] if pilot else cores
    records=0;positive=negative=uncertain=0;best=None;worst=None;eligible=None;eligible_positive=0
    for ancestor_u,v,o,i,b,control in itertools.product(uc,vc,(0,1),(0,1),(0,1),range(3)):
        u=E.restrict(ancestor_u,i,b);row,gap=node(labels(o),u,v,control);records+=1
        positive+=gap[0]>0;negative+=gap[1]<0;uncertain+=gap[0]<=0<=gap[1] and gap!=(F(0),F(0))
        fixture={'ancestor_u':list(ancestor_u),'v':list(v),'orientation':o,'data_exposure':[i,b],'control_query':control,'restricted_u':list(u),'row':row}
        if best is None or gap[0]>F(best['row']['rho_minus_kappa'][0]):best=fixture
        if worst is None or gap[1]<F(worst['row']['rho_minus_kappa'][1]):worst=fixture
        if E.influence(ancestor_u,i)>0 and len(set(u))>1 and len(set(v))>1:
            eligible_positive+=gap[0]>0
            if eligible is None or gap[0]>F(eligible['row']['rho_minus_kappa'][0]):eligible=fixture
    result={'status':'PASS','records':records,'cached_nodes':node.cache_info().currsize,'assertions':COUNT,'runtime_seconds':time.monotonic()-START,'positive_gap_records':positive,'negative_gap_records':negative,'uncertain_gap_records':uncertain,'essential_exposure_both_nonconstant_positive_records':eligible_positive,'best_essential_exposure_both_nonconstant':eligible,'largest_certified_gap':best,'smallest_certified_gap':worst}
    (ROOT/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in result.items() if 'gap' not in k}))
if __name__=='__main__':main()
