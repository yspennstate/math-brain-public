"""Frozen stage7 exact certificate, all writes within this run."""
from pathlib import Path
import sys, json, hashlib, time
exec(compile((Path(__file__).parent/'arithmetic.py').read_text(encoding='utf-8'), 'arithmetic.py', 'exec'))
pilot='--pilot' in sys.argv
def cn(q): return {} if not q else {F(2):F(q)}
def ser(e): return [[str(x),str(c)] for x,c in sorted(e.items())]
def save(name,v): (ROOT/'out'/name).write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
def form(h,v): return tuple(h[s]*(v[x] if s==0 else 1) for s in range(len(h)) for x in range(len(v)))
def mean(v): return F(sum(v),len(v))
def dimension(t): return len(t).bit_length()-1
def profile(h,mu):
    ep=F(1,len(h));d=dimension(h);r=d*ep*(1-mu*mu)
    row=plus(*[(phi((c-ep*(1-mu))**2),F(1)) for c in coeff(h)])
    j=plus((row,F(1)),(H(h),F(-1)),(cn(r),F(1)),(phi(mu*mu),-ep))
    return r,j
def delta(t,i): return plus((H(t),F(1)),(H(child(t,i,0)),F(-1,2)),(H(child(t,i,1)),F(-1,2)))
def direct(t):
    return tuple(F(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)),len(t)) for s in range(len(t)))
roots=queries=direct_checks=0
def checkroot(h,v,reproduce=False):
    global roots,queries,direct_checks
    ep=F(1,len(h));mu=mean(v);d=dimension(h);n=dimension(v);f=form(h,v);r,j=profile(h,mu)
    equal_expr(plus((H(f),F(1)),(H(v),-ep),(H(h),F(-1)),(cn(r),F(-1)),(j,F(-1))))
    lh=sum(h[1<<i] for i in range(d))
    eq(I(f),I(h)+ep*I(v)+ep*(1-mu)*lh)
    for i in range(n):
        a=coeff(v)[1<<i];di=inf(v,i);vv=[child(v,i,c) for c in [0,1]]
        ff=[child(f,i,c) for c in [0,1]]
        eq(inf(f,i),ep*di)
        for v1,f1 in zip(vv,ff):eq(f1,form(h,v1))
        pcs=[profile(h,mean(v1)) for v1 in vv]
        release=r-sum(p[0] for p in pcs)/2;eq(release,d*ep*a*a)
        jd=plus((j,F(1)),(pcs[0][1],F(-1,2)),(pcs[1][1],F(-1,2)))
        equal_expr(plus((delta(f,i),F(1)),(delta(v,i),-ep),(cn(release),F(-1)),(jd,F(-1))))
        leq(jd,11*ep*di)
        leq(plus((delta(f,i),F(1)),(delta(v,i),-ep)),release+11*ep*di)
        leq(plus((B(f,i),F(1)),(B(v,i),-ep)),release+14*ep*di)
        # Every signed source-surplus term is retained, even if negative.
        sroot=plus((cn(5*I(f)),F(1)),(H(f),F(-1)))
        schild=plus(*[(plus((cn(5*I(f1)),F(1)),(H(f1),F(-1))),F(1,2)) for f1 in ff])
        equal_expr(plus((sroot,F(1)),(schild,F(-1)),(cn(5*ep*di),F(-1)),(delta(f,i),F(1))))
        queries+=1
    if reproduce:
        eq(coeff(f),direct(f));eq(I(f),sum((F(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f)) for i in range(n+d)),F(0)))
        direct_checks+=2
    roots+=1;coeff.cache_clear()
for d in range(3 if pilot else 4):
    for label in range(1<<((1<<d)-1)):
        h=(1,)+tuple(1-2*((label>>(s-1))&1) for s in range(1,1<<d))
        for n in range(2 if pilot else 3):
            for table in range(1<<(1<<n)):
                v=tuple(1-2*((table>>x)&1) for x in range(1<<n))
                checkroot(h,v,reproduce=(d<=2 and n<=1))
hmaj=tuple(1 if s.bit_count()<=2 else -1 for s in range(32))
eq({x:coeff(hmaj).count(x) for x in set(coeff(hmaj))},{F(0):16,F(3,8):6,F(-1,8):10})
for n in range(2 if pilot else 4):
    for table in range(1<<(1<<n)):
        v=tuple(1-2*((table>>x)&1) for x in range(1<<n));checkroot(hmaj,v,reproduce=(n<=1))

# Same booked history: x1,x2,s1,x3; keep every sibling and final child.
h=hmaj;v=(-1,)+(1,)*15;froot=form(h,v);rroot=5*F(1,32)*(1-mean(v)**2)
weight=F(1);leafh={};leafi=F(0);leafr=F(0);cost={};inputcost={};release_total=F(0);pp=ps=F(0);nodes=[]
for kind in ['private','private','shared','private']:
    d=dimension(h);n=dimension(v);ep=F(1,len(h));mu=mean(v);f=form(h,v);r,j=profile(h,mu)
    if kind=='private':
        vv=[child(v,0,c) for c in [0,1]];hh=[h,h];ff=[form(h,v1) for v1 in vv];rs=[profile(h,mean(v1))[0] for v1 in vv]
        ic=plus((delta(v,0),ep));di=inf(f,0);pp+=weight*di
        gcore=form(h,(-1,)+(1,)*((1<<(n-1))-1));quarter=plus((B(gcore,0),F(1,4)))
        admission=plus((B(f,0),F(1)),(quarter,F(-1)))
        leq(plus((admission,F(-1))),F(0));leq(admission,4*inf(f,n-1))
        eq(len(set(gcore)),2);eq(len(set(h)),2)
        eq(sum(inf(c,n-2) for c in ff)/2,inf(f,n-1))
    else:
        hh=[child(h,0,c) for c in [0,1]];vv=[v,v];ff=[child(f,n,c) for c in [0,1]]
        eq(ff[0],form(hh[0],v));eq(ff[1],tuple(hh[1][s] for s in range(len(hh[1])) for x in range(len(v))))
        rs=[(d-1)*2*ep*(1-mu*mu),F(0)];ic={};di=inf(f,n);ps+=weight*di;quarter=None;admission=None
        eq(di>=F(3,8),True);eq(r-sum(rs)/2,ep*(1-mu*mu))
    bill=plus((H(f),F(1)),(H(ff[0]),F(-1,2)),(H(ff[1]),F(-1,2)))
    rel=r-sum(rs)/2;eq(rel>=0,True)
    leq(plus((bill,F(1)),(ic,F(-1))),rel+11*di if kind=='private' else 6*di)
    eq(all(len(set(t))==2 for t in ff),True)
    # Exact C=5 surplus conservation including all actual child deficits.
    equal_expr(plus((cn(5*I(f)),F(1)),(H(f),F(-1)),
        (plus(*[(plus((cn(5*I(c)),F(1)),(H(c),F(-1))),F(1,2)) for c in ff]),F(-1)),
        (cn(5*di),F(-1)),(bill,F(1))))
    leafh=plus((leafh,F(1)),(H(ff[1]),weight/2));leafi+=weight*I(ff[1])/2;leafr+=weight*rs[1]/2
    cost=plus((cost,F(1)),(bill,weight));inputcost=plus((inputcost,F(1)),(ic,weight));release_total+=weight*rel
    nodes.append(dict(kind=kind,weight=str(weight),query_influence=str(di),incoming_R=str(r),child_R=[str(t) for t in rs],
        full_bill=ser(bill),inherited_quarter=None if quarter is None else ser(quarter),admission=None if admission is None else ser(admission),
        signed_surplus_parent=ser(plus((cn(5*I(f)),F(1)),(H(f),F(-1)))),
        signed_surplus_children=[ser(plus((cn(5*I(c)),F(1)),(H(c),F(-1)))) for c in ff],both_children_nonconstant=True))
    h,v=hh[0],vv[0];weight/=2
f=form(h,v);leafh=plus((leafh,F(1)),(H(f),weight));leafi+=weight*I(f);leafr+=weight*profile(h,mean(v))[0]
eq(rroot,release_total+leafr);eq(I(froot),pp+ps+leafi)
equal_expr(plus((H(froot),F(1)),(cost,F(-1)),(leafh,F(-1))))
leq(plus((cost,F(1)),(inputcost,F(-1))),release_total+11*pp+6*ps)
save('MIXED_HISTORY'+('_PILOT' if pilot else '')+'.json',dict(nodes=nodes,R_root=str(rroot),R_release=str(release_total),R_terminal=str(leafr),
    P_private=str(pp),P_shared=str(ps),terminal_entropy=ser(leafh),terminal_influence=str(leafi),full_bill=ser(cost),inherited_input_cost=ser(inputcost),
    selector='z remains unqueried',root_entropy=ser(H(froot)),root_influence=str(I(froot))))
result=dict(status='PASS',mode='PILOT' if pilot else 'FULL',roots=roots,private_queries=queries,exact_assertions=checks,
    independent_direct_assertions=direct_checks,elapsed_seconds=time.perf_counter()-start,
    helper_sha256=hashlib.sha256((ROOT/'code/arithmetic.py').read_bytes()).hexdigest(),memory='180 MB estimate; actual peak not measured')
save('PILOT.json' if pilot else 'FULL.json',result);print(json.dumps(result))
