"""Frozen exact flat-carrier certificate; only writes in this run."""
exec(compile((__import__('pathlib').Path(__file__).parent/'arithmetic.py').read_text(),str(__import__('pathlib').Path(__file__).parent/'arithmetic.py'),'exec'))
import sys, hashlib
PILOT='--pilot' in sys.argv
def const(q): return {} if not q else {F(2):F(q)}
def sub(a,b):return plus((a,F(1)),(b,F(-1)))
def carrier(s,k):return -1 if sum(((s>>(2*j))&1)*((s>>(2*j+1))&1) for j in range(k//2))%2 else 1
def phase(v,k):
    return tuple(carrier(s,k)*(v[x] if s==0 else 1) for s in range(1<<k) for x in range(len(v)))
def profile(k,mu):
    ep=F(1,1<<k);b=F(1,1<<(k//2));r=1-mu
    np=((1<<k)+(1<<(k//2)))//2;nm=(1<<k)-np
    row=plus((phi((b-ep*r)**2),F(np)),(phi((-b-ep*r)**2),F(nm)))
    R=k*ep*(1-mu*mu)
    J=plus((row,F(1)),(const(k*(1-ep*(1-mu*mu))),F(-1)),(phi(mu*mu),-ep))
    return R,J
def formula(v,k):
    ep=F(1,1<<k);mu=F(sum(v),len(v));r,j=profile(k,mu)
    return plus((H(v),ep),(const(k+r),F(1)),(j,F(1)))
def edges(t,i):
    return F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t))
def serial(e):return [[str(x),str(c)] for x,c in sorted(e.items())]
def enclosure(e):
    lo,hi=bounds(e);sc=1<<90
    return [str(F(lo.numerator*sc//lo.denominator,sc)),str(F(-((-hi.numerator*sc)//hi.denominator),sc))]
roots=queries=0
for k in ([4] if PILOT else [4,6]):
    ep=F(1,1<<k)
    for n in range(3 if PILOT else 4):
        for table in range(1<<(1<<n)):
            v=tuple(1-2*((table>>x)&1) for x in range(1<<n));f=phase(v,k)
            mu=F(sum(v),len(v));r,j=profile(k,mu);hv=H(v);hf=H(f)
            equal_expr(sub(hf,formula(v,k)))
            eq(I(f),F(k,2)+k*ep*(1-mu)+ep*I(v))
            leq(j,80*ep);leq(plus((j,F(-1))),80*ep)
            leq(hv,5*I(v));leq(hf,5*I(f))
            u=plus((const(F(3*k,2)+5*k*ep*(1-mu)-r),F(1)),(j,F(-1)))
            leq(plus((u,F(-1))),-F(3*k,16))
            for i in range(n):
                d=inf(v,i);a=coeff(v)[1<<i]
                eq(edges(v,i),d);eq(edges(f,i),ep*d);eq(inf(f,i),ep*d)
                vs=[child(v,i,c) for c in [0,1]];fs=[child(f,i,c) for c in [0,1]]
                for vv,ff in zip(vs,fs):eq(ff,phase(vv,k))
                mus=[F(sum(vv),len(vv)) for vv in vs]
                rsjs=[profile(k,m) for m in mus]
                release=r-sum(x[0] for x in rsjs)/2
                eq(release,k*ep*a*a);eq(release>=0,True)
                dhf=plus((hf,F(1)),(H(fs[0]),F(-1,2)),(H(fs[1]),F(-1,2)))
                dhv=plus((hv,F(1)),(H(vs[0]),F(-1,2)),(H(vs[1]),F(-1,2)))
                jd=plus((j,F(1)),(rsjs[0][1],F(-1,2)),(rsjs[1][1],F(-1,2)))
                equal_expr(plus((dhf,F(1)),(dhv,-ep),(const(release),F(-1)),(jd,F(-1))))
                leq(jd,40*ep*d);leq(plus((jd,F(-1))),40*ep*d)
                leq(plus((B(f,i),F(1)),(B(v,i),-ep)),43*ep*d+release)
                # Exact signed target-C child-deficit transport, no clipping.
                scroot=plus((const(5*I(f)),F(1)),(hf,F(-1)))
                scchildren=plus(*[(plus((const(5*I(ff)),F(1)),(H(ff),F(-1))),F(1,2)) for ff in fs])
                equal_expr(plus((scroot,F(1)),(scchildren,F(-1)),(const(5*ep*d),F(-1)),(dhf,F(1))))
                queries+=1
            for i in range(k):eq(edges(f,n+i),F(1,2)+ep*(1-mu))
            roots+=1
            coeff.cache_clear()
ledger=[]
if not PILOT:
    for k in [4,6]:
        ep=F(1,1<<k)
        for m in [2,3,4]:
            v=tuple([-1]+[1]*((1<<(m+1))-1));fr=phase(v,k);f=fr
            mu=F(sum(v),len(v));rroot,jroot=profile(k,mu)
            release=F(0);p=F(0);cost={};btotal={};qtotal={};jcost={};leafh={};leafi=F(0);rleaf=F(0);nodes=[]
            for depth in range(m):
                rem=m-depth;weight=F(1,1<<depth);mu=F(sum(v),len(v));r,j=profile(k,mu)
                d=inf(v,0);a=coeff(v)[1];ff=[child(f,0,c) for c in [0,1]];vv=[child(v,0,c) for c in [0,1]]
                rs=[profile(k,F(sum(t),len(t)))[0] for t in vv]
                rel=r-sum(rs)/2;release+=weight*rel;p+=weight*ep*d
                dhf=plus((H(f),F(1)),(H(ff[0]),F(-1,2)),(H(ff[1]),F(-1,2)))
                cost=plus((cost,F(1)),(dhf,weight));btotal=plus((btotal,F(1)),(B(f,0),weight))
                g=phase(tuple([-1]+[1]*((1<<rem)-1)),k);quarter=plus((B(g,0),F(1,4)))
                admission=sub(B(f,0),quarter);delta=inf(f,rem)
                leq(plus((admission,F(-1))),F(0));leq(admission,4*delta)
                # Original selector reserve does not release, unlike R.
                eq(sum(inf(t,rem-1) for t in ff)/2,delta)
                eq(delta,ep/F(1<<rem));eq(all(len(set(t))==2 for t in ff),True)
                eq(len(set(g))==2,True)
                qtotal=plus((qtotal,F(1)),(quarter,weight))
                leafh=plus((leafh,F(1)),(H(ff[1]),weight/2));leafi+=weight*I(ff[1])/2;rleaf+=weight*rs[1]/2
                nodes.append(dict(depth=depth,weight=str(weight),selector_mass=str(delta),private_influence=str(ep*d),
                    incoming_R=str(r),weighted_release=str(weight*rel),B=serial(B(f,0)),inherited_quarter=serial(quarter),admission=serial(admission)))
                v,f=vv[0],ff[0]
            w=F(1,1<<m);leafh=plus((leafh,F(1)),(H(f),w));leafi+=w*I(f);rleaf+=w*profile(k,F(sum(v),len(v)))[0]
            eq(p,m*ep/F(1<<m));eq(rleaf,k*ep/F(1<<m));eq(release,k*ep*(F(1,1<<m)-F(1,1<<(2*m))))
            eq(release+rleaf,rroot);equal_expr(plus((H(fr),F(1)),(cost,F(-1)),(leafh,F(-1))))
            eq(I(fr),p+leafi)
            leq(plus((btotal,F(1)),(qtotal,F(-1))),4*m*ep/F(1<<m))
            ledger.append(dict(k=k,m=m,private_cost=serial(cost),private_B=serial(btotal),inherited_quarter=serial(qtotal),
                terminal_H=serial(leafh),terminal_I=str(leafi),P=str(p),R_root=str(rroot),R_leaf=str(rleaf),released_R=str(release),nodes=nodes))
            coeff.cache_clear()
    compressed=[]
    for k in [4,6,8,16,32,64]:
        ep=F(1,1<<k)
        # Literal input: both phase-edit children nonconstant, residual/Inf grows with k.
        r,j=profile(k,F(0));end=[profile(k,F(m))[1] for m in [-1,1]]
        jd=plus((j,F(1)),(end[0],F(-1,2)),(end[1],F(-1,2)))
        residual=plus((const(r),F(1)),(jd,F(1)))
        leq(jd,40*ep);leq(plus((jd,F(-1))),40*ep)
        leq(plus((residual,F(-1))),-(k-40)*ep)
        # Parity input: no first release; both reached second queries release the SAME bank.
        eq(r-k*ep,F(0));eq(r-(r+r)/2,F(0));eq(r-F(0),k*ep)
        compressed.append(dict(k=k,private_influence=str(ep),no_bank_residual_ratio=enclosure(plus((residual,1/ep))),
            parity_first_release='0',parity_second_total_release=str(k*ep)))
    (ROOT/'out/HISTORY_LEDGERS.json').write_text(json.dumps(ledger,indent=2)+'\n')
    (ROOT/'out/COMPRESSED.json').write_text(json.dumps(compressed,indent=2)+'\n')
result=dict(status='PASS',mode='PILOT' if PILOT else 'FULL',roots=roots,private_queries=queries,point_history_roots=len(ledger),
    exact_assertions=checks,elapsed_seconds=time.perf_counter()-start,helper_sha256=hashlib.sha256((ROOT/'code/arithmetic.py').read_bytes()).hexdigest(),
    memory='180 MB frozen estimate; caches of spectra cleared per root; peak not measured')
(ROOT/('out/PILOT.json' if PILOT else 'out/FULL.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
