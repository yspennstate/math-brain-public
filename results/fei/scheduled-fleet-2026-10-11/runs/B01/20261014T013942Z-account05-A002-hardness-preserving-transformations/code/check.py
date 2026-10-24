from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from collections import Counter
import sys,json,time,argparse
sys.dont_write_bytecode=True
import arithmetic as M
RUN=Path(__file__).resolve().parents[1]
checks=0;deadline=0
VERIFY_GROUPING=False
RAW_H=M.H;RAW_BV=M.Bvec
def grouped_H(p):return M.add(*[(count,M.phi(mass)) for mass,count in Counter(p.values()).items()])
def grouped_BV(p,n):
    out=[]
    for i in range(n):
        pairs=Counter((mass,p.get(s|(1<<i),Q(0))) for s,mass in p.items() if not s>>i&1)
        out.append(M.add(*[(count,M.E(x,y)) for (x,y),count in pairs.items()]))
    return out
M.H=grouped_H;M.Bvec=grouped_BV;M.E=lru_cache(None)(M.E)
def ck(ok):
    global checks
    checks+=1
    if time.perf_counter()>deadline:raise TimeoutError('Frozen runtime exceeded')
    assert ok,checks
def vec(q):return () if not q else ((2,Q(q)),)
def sub(a,b):return M.add((1,a),(-1,b))
@lru_cache(None)
def ln_bounds(q):
    z=(q-1)/(q+1);s=Q(0);power=z
    for j in range(64):s+=power/(2*j+1);power*=z*z
    lo=2*s;hi=lo+2*power/(129*(1-z*z))
    return lo,hi
@lru_cache(None)
def log_bounds(prime):
    k=prime.bit_length()-1;q=Q(prime,1<<k)
    lo,hi=ln_bounds(q);l2,u2=ln_bounds(Q(2))
    scale=1<<128
    a=Q(k)+lo/u2;b=Q(k)+hi/l2
    return Q((a*scale).numerator//(a*scale).denominator,scale),Q(-((-b*scale).numerator//(-b*scale).denominator),scale)
def interval(expr):
    lo=Q(0);hi=Q(0)
    for p,c in expr:
        l,u=log_bounds(p)
        if c<0:l,u=u,l
        lo+=c*l;hi+=c*u
    return lo,hi
def sign(expr):
    if not expr:return 0
    lo,hi=interval(expr)
    assert lo>0 or hi<0,('unresolved sign',expr,lo,hi)
    return 1 if lo>0 else -1
def positive(expr):return expr if sign(expr)>0 else ()
def max_expr(a,b):return a if sign(sub(a,b))>=0 else b
def scaled(x,expr):return M.add((x,expr))
def vals(n,mask):return [1 if mask>>x&1 else -1 for x in range(1<<n)]
def child(v,n,i,b):
    return [v[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(1<<(n-1))]
@lru_cache(None)
def measure(v):
    n=len(v).bit_length()-1;a=M.fwht(v);p=M.probabilities(a)
    if VERIFY_GROUPING:
        ck(M.H(p)==RAW_H(p));ck(M.Bvec(p,n)==RAW_BV(p,n))
    return a,p,M.H(p),sum(M.inf(p,n))
@lru_cache(None)
def kernel(v):
    _,p,_,_=measure(v);n=len(v).bit_length()-1
    return M.Bvec(p,n),M.inf(p,n)
def root(v,C):
    n=len(v).bit_length()-1;a,p,h,I=measure(tuple(v));bv,ds=kernel(tuple(v));delta=sub(h,vec(C*I));out=[]
    for i,d in enumerate(ds):
        if not d:continue
        children=[measure(tuple(child(v,n,i,b))) for b in [0,1]]
        avh=M.add(*[(Q(1,2),g[2]) for g in children]);avi=sum(g[3] for g in children)/2
        sigma=sub(vec(C*avi),avh);L=sub(h,avh);js=sub(L,bv[i])
        ck(avi==I-d)
        ck(M.add((1,delta),(1,sigma))==sub(L,vec(C*d)))
        corrected=scaled(1/d,M.add((1,bv[i]),(1,positive(scaled(-1,sigma)))))
        mx=max_expr(scaled(1/d,bv[i]),M.add((1,vec(C)),(1/d,sub(delta,js))))
        ck(corrected==mx)
        out.append({'i':i,'d':d,'B':bv[i],'JS':js,'sigma':sigma,'q':corrected,'individual_slacks':[sub(vec(C*g[3]),g[2]) for g in children]})
    return delta,out
def tensor_values(seed,n,t):
    out=[]
    for x in range(1<<(n*t)):
        val=1
        for j in range(t):val*=seed[(x>>(n*j))&((1<<n)-1)]
        out.append(val)
    return out
def main(pilot):
    global deadline,VERIFY_GROUPING
    VERIFY_GROUPING=pilot
    start=time.perf_counter();deadline=start+(60 if pilot else 120)
    count={'tensor_roots':0,'activation_roots':0,'edited_activation_roots':0,'witness_roots':0}
    nmax=2 if pilot else 3
    for n in range(1,nmax+1):
        for mask in range(1<<(1<<n)):
            seed=vals(n,mask);base={C:root(seed,C) for C in [Q(0),Q(2),Q(8,3),Q(3),Q(4)]}
            for t in ([1,2] if n==3 else [1,2,3]):
                count['tensor_roots']+=1;tv=tensor_values(seed,n,t)
                for C,(delta,src) in base.items():
                    dd,rr=root(tv,C);ck(dd==scaled(t,delta))
                    for o in rr:
                        s=next(x for x in src if x['i']==o['i']%n)
                        ck(o['B']==s['B'] and o['JS']==s['JS'] and o['d']==s['d'])
                        ck(o['sigma']==M.add((1,s['sigma']),(-(t-1),delta)))
                        expected=max_expr(scaled(1/s['d'],s['B']),M.add((1,vec(C)),(1/s['d'],sub(scaled(t,delta),s['JS']))))
                        ck(expected==o['q'])
    for n in ([1] if pilot else [1,2]):
        for mask in range(1<<(1<<n)):
            seed=vals(n,mask);sp=M.probabilities(M.fwht(seed));sh=M.H(sp);si=sum(M.inf(sp,n))
            for t in ([1] if pilot else [1,2]):
                core=tensor_values(seed,n,t);g=[core[x&((1<<(n*t))-1)]*(-1 if x>>(n*t) else 1) for x in range(1<<(n*t+1))]
                for k in [1,2]:
                    count['activation_roots']+=1;p=Q(1,1<<k);dim=n*t+1+k
                    v=[g[x&((1<<(n*t+1))-1)] if x>>(n*t+1)==0 else 1 for x in range(1<<dim)]
                    aa,pp,h,I=measure(tuple(v));ds=M.inf(pp,dim)
                    ck(I==p*(t*si+1+k));ck(max(ds)==p);ck(aa.get(0,Q(0))==1-p)
                    ck(h==M.add((p*t,sh),(1,vec(2*k*p*(2-p))),(1,M.phi((1-p)**2))))
                    # Two dummies and one vertex edit: direct physical reconstruction.
                    edited=[v[x&((1<<dim)-1)] for x in range(1<<(dim+2))];edited[0]*=-1
                    count['edited_activation_roots']+=1;ea,ep,eh,eI=measure(tuple(edited));alpha=Q(1,1<<(dim+1))
                    ck(len(ea)==1<<(dim+2));ck(abs(eI-I)<=(dim+2)*alpha)
                    for i,d in enumerate(M.inf(ep,dim+2)):
                        ck(abs(d-(ds[i] if i<dim else 0))<=alpha)
                    for C in [Q(2),Q(8,3)]:root(edited,C)
    witness={}
    if not pilot:
        N=12;C=Q(8,3);v=[-1 if x&7==0 else 1 for x in range(1<<N)];v[0]*=-1
        a,p,h,I=measure(tuple(v));delta,rows=root(v,C);count['witness_roots']=1
        ck(len(a)==4096);ck(I==Q(771,1024));ck(sign(delta)>0)
        for o in rows:
            ck(o['d']<Q(1,4))
            if o['i']<3:
                ck(sign(o['sigma'])>0);ck(all(sign(s)>=0 for s in o['individual_slacks']))
                ck(sign(sub(o['B'],vec(Q(5,2)*o['d'])))>0)
            else:
                ck(sign(o['sigma'])<0);ck(all(sign(s)<0 for s in o['individual_slacks']))
                ck(sign(sub(o['B'],vec(Q(5,2)*o['d'])))<0)
                ck(sign(sub(o['q'],vec(400)))>0)
        witness={'dimension':12,'C':'8/3','root_delta_interval':[str(x) for x in interval(delta)],'old_erasure_ratio_interval':[str(x) for x in interval(scaled(1/rows[0]['d'],rows[0]['B']))],'fresh_erasure_ratio_interval':[str(x) for x in interval(scaled(1/rows[3]['d'],rows[3]['B']))],'fresh_corrected_price_interval':[str(x) for x in interval(rows[3]['q'])]}
        (RUN/'out/WITNESS.json').write_text(json.dumps(witness,indent=2)+'\n',encoding='utf-8')
    result={'helper_version':'A002-signed-price-v2','pilot':pilot,'counts':count,'root_executions':sum(count.values()),'exact_assertions':checks,'failures':0,'seconds':time.perf_counter()-start,'max_dimension':6 if pilot else 12,'arithmetic':'Integer physical truth tables/FWHT, Fraction spectra/influence, grouped formal prime-log equalities (pilot compared exactly to original per-edge implementation), rational 64-term atanh tail bounds rounded outward to2^-128','peak_memory':'not measured; estimated below100MB'}
    (RUN/'out'/('PILOT.json' if pilot else 'EXACT_CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');main(ap.parse_args().pilot)
