"""A076 private-admission v1: exact private rows and one-use antichain reserve."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,argparse
ROOT=Path(__file__).resolve().parents[1]
exec(compile((ROOT/'code/arithmetic.py').read_text(encoding='utf-8'),str(ROOT/'code/arithmetic.py'),'exec'))
ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
start=time.perf_counter();limit=55 if args.pilot else 600
H=lru_cache(maxsize=8192)(H);B=lru_cache(maxsize=16384)(B);inf=lru_cache(maxsize=8192)(inf)
def enc(e):return [[str(x),str(c)] for x,c in sorted(e.items())]
def mux(g,h):return tuple(v for a,b in zip(g,h) for v in [a,b])
def embed(h):return tuple(v for a in h for v in [a,a])
def delta(g,h):return F(sum(a!=b for a,b in zip(g,h)),len(g))
def edges(t,i):return F(sum(t[z]!=t[z^(1<<i)] for z in range(len(t))),len(t))
def terminal_R(g,h):return plus((H(mux(g,h)),F(1)),(H(g),F(-1,2)),(H(h),F(-1,2)))
@lru_cache(maxsize=8192)
def admission(g,h):
    f=mux(g,h);cg=coeff(g);ch=coeff(h);dd=inf(g,0);de=delta(g,h)
    eq(inf(h,0),F(0));eq(dd,edges(g,0));eq(inf(f,1),dd/2);eq(inf(f,0),de);eq(inf(f,0),edges(f,0))
    E=sum(((cg[s]-ch[s])**2 for s in range(0,len(g),2)),F(0))
    eq(E,4*de-dd);eq(dd<=2*de,True)
    raw={}
    for s in range(0,len(g),2):
        u,a,v=cg[s],cg[s+1],ch[s]
        raw=plus((raw,F(1)),(Phi((u+v)**2,a*a),F(1,4)),(Phi((u-v)**2,a*a),F(1,4)))
    bf=B(f,1);bg=B(g,0)
    equal_expr(plus((bf,F(1)),(raw,F(-1))))
    A=plus((bf,F(1)),(bg,F(-1,4)))
    leq(plus((A,F(-1))),F(0));leq(A,4*de)
    leq(plus((A,F(1)),(Phi(E,dd),F(-1,2))),dd)
    return A,bg,bf,de
def tree(g0,h0,policy):
    todo=[(g0,h0,F(1),0)];A={};bg={};bf={};term={};coreterm={};rterm={};mass=F(0);query_nodes=0
    while todo:
        if time.perf_counter()-start>limit:raise RuntimeError('frozen runtime limit')
        g,h,w,parity=todo.pop();n=len(g).bit_length()-2
        expose=policy=='first' or n==0 or (policy=='adaptive' and parity==1)
        if expose:
            a,cost,bc,de=admission(g,h);query_nodes+=1;mass+=w*de
            A=plus((A,F(1)),(a,w));bg=plus((bg,F(1)),(cost,w/4));bf=plus((bf,F(1)),(bc,w))
            for bit in [0,1]:
                gg=child(g,0,bit);hh=child(h,0,bit);ff=mux(gg,hh)
                term=plus((term,F(1)),(H(ff),w/2))
                coreterm=plus((coreterm,F(1)),(H(gg),w/4),(H(hh),w/4))
                rterm=plus((rterm,F(1)),(terminal_R(gg,hh),w/2))
        else:
            # Query first remaining shared coordinate; x stays coordinate zero.
            todo.extend((child(g,1,b),child(h,1,b),w/2,parity^b) for b in [0,1])
    eq(mass,delta(g0,h0));leq(A,4*mass)
    equal_expr(plus((bf,F(1)),(bg,F(-1)),(A,F(-1))))
    equal_expr(plus((term,F(1)),(coreterm,F(-1)),(rterm,F(-1))))
    return dict(policy=policy,query_nodes=query_nodes,selector_account=str(mass),admission=enc(A),
                inherited_quarter_B=enc(bg),actual_B=enc(bf),terminal_entropy=enc(term))
scalar_cases=0
for u in map(F,[-2,-1,F(-1,2),0,F(1,2),1,2]):
    for v in map(F,[-2,-1,F(-1,2),0,F(1,2),1,2]):
        for a in map(F,[0,F(1,4),F(1,2),1,2]):
            q=a*a;e=u-v
            lhs=plus((Phi((u+v)**2,q),F(1)),(Phi(e*e,q),F(1)),(Phi(u*u,q),F(-1)))
            leq(plus((lhs,F(-1))),F(0));leq(plus((lhs,F(1)),(Phi(e*e,q),F(-2))),4*q)
            scalar_cases+=1
records=[];roots=0
for n in range(2 if args.pilot else 3):
    for gm in range(1<<(1<<(n+1))):
        g=tuple(1-2*((gm>>z)&1) for z in range(1<<(n+1)))
        for hm in range(1<<(1<<n)):
            h=embed(tuple(1-2*((hm>>z)&1) for z in range(1<<n)))
            admission(g,h);rr=[tree(g,h,p) for p in ['first','last','adaptive']]
            records.append(dict(n=n,Gmask=gm,Hmask=hm,trees=rr));roots+=1
        if roots and roots%512==0:
            (ROOT/'out/CHECKPOINT.json').write_text(json.dumps(dict(roots=roots,elapsed_seconds=time.perf_counter()-start))+'\n',encoding='utf-8')
sharp=[]
if not args.pilot:
    for k in [2,4,6,8,16,32,64]:
        N=1<<k;a=F(1,N);b=F(1,1<<(k//2));np=(N+(1<<(k//2)))//2;nm=N-np
        bg=plus((Phi((b-a)**2,a*a),F(np)),(Phi((b+a)**2,a*a),F(nm)))
        bf=plus((Phi((2*b-a)**2,a*a),F(np,4)),(Phi((2*b+a)**2,a*a),F(nm,4)),({F(2):a/2},F(1)))
        leq(plus((bg,F(-1))),-a*(k-2));leq(plus((bg,F(1,4)),(bf,F(-1))),-a/2)
        leq(plus((bf,F(1)),(bg,F(-1,4))),2*a)
        if k<=8:
            hs=tuple((-1)**sum(((s>>j)&1)*((s>>(j+1))&1) for j in range(0,k,2)) for s in range(N))
            g=tuple(hs[z>>1]*(-1 if z==0 else 1) for z in range(2*N));h=embed(hs)
            A,BG,BF,de=admission(g,h);eq(de,a/2)
            equal_expr(plus((BG,F(1)),(bg,F(-1))));equal_expr(plus((BF,F(1)),(bf,F(-1))))
        lo,hi=bounds(plus((bf,F(1)),(bg,F(-1,4))))
        # Save only dyadic enclosures; avoid huge raw endpoint serialization.
        sc=1<<90;ll=F((lo.numerator*sc)//lo.denominator,sc);uu=F(-((-hi.numerator*sc)//hi.denominator),sc)
        assert ll<=lo<=hi<=uu
        sharp.append(dict(k=k,delta=str(a/2),B_G_over_delta_lower=2*(k-2),
                          admission_lower=str(ll),admission_upper=str(uu)))
name='PILOT' if args.pilot else 'FULL'
(ROOT/'out'/f'{name}_LEDGERS.json').write_text(json.dumps(records,separators=(',',':'))+'\n',encoding='utf-8')
result=dict(status='PASS',helper_version='private-admission-v1',roots=roots,antichain_trees=roots*3,scalar_cases=scalar_cases,
            exact_assertions=checks,elapsed_seconds=time.perf_counter()-start,memory_estimate_MB=180,
            sharp_fixtures=sharp,arithmetic='Fraction spectra/edges; exact prime-exponent identities; rigorous rational log intervals')
(ROOT/'out'/f'{name}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='sharp_fixtures'}))
