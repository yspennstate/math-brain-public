from pathlib import Path
source=Path(__file__).with_name('check.py').read_text(encoding='utf-8')
exec(compile(source.split('graphfixtures=0;graphatoms=0')[0],str(Path(__file__).with_name('check.py')),'exec'))

def project(p,i):
    q={}
    for a,x in p.items():q[a&~(1<<i)]=q.get(a&~(1<<i),F(0))+x
    return q
def law(f,state):
    free=[i for i,x in enumerate(state) if x<0];fixed=sum((x<<i) for i,x in enumerate(state) if x>=0)
    vals=[f[fixed+sum(((j>>k&1)<<i) for k,i in enumerate(free))] for j in range(1<<len(free))]
    w=fwht(vals)
    return {sum(((j>>k&1)<<i) for k,i in enumerate(free)):F(x*x,4**len(free)) for j,x in enumerate(w)}
def plus(*vals):return add(*vals)
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def scale(z,t):return (t*z[0],t*z[1]) if t>=0 else (t*z[1],t*z[0])
def DD(p,q):
    if p==q:return F(0),F(0)
    return plus(*(logcost(x/q[a],x) for a,x in p.items() if x))
def HH(p):return plus(*(logcost(1/x,x) for x in p.values() if x))
def CC(p,q):return plus(*(logcost(1/q[a],x) for a,x in p.items() if x))
def lvadd(*terms):
    out={}
    for k,vec in terms:
        for key,x in vec.items():
            if key!=1:out[key]=out.get(key,F(0))+k*x
    return {key:x for key,x in out.items() if x}
def DV(p,q):
    vec={}
    for a,x in p.items():
        if x:
            ck(q.get(a,0)>0)
            vec[x]=vec.get(x,F(0))+x;vec[q[a]]=vec.get(q[a],F(0))-x
    return {a:x for a,x in vec.items() if a!=1 and x}
def profiles(p,q,t):
    pp={c:sum((x for a,x in p.items() if bool(a)==c),F(0)) for c in [False,True]}
    qq={c:sum((x for a,x in q.items() if bool(a)==c),F(0)) for c in [False,True]}
    rr={c:(1-t)*qq[c]+t*pp[c] for c in pp}
    r={a:x*rr[bool(a)]/qq[bool(a)] if qq[bool(a)] else F(0) for a,x in q.items()}
    ck(sum(r.values())==1);ck(all(r[a]>0 for a,x in p.items() if x))
    for a,x in q.items():
        if qq[bool(a)]:ck(r[a]*qq[bool(a)]==x*rr[bool(a)])
    if 0<t<1:
        lhs={}
        for c,x in rr.items():
            if x:
                z=pp[c]-rr[c];lhs[x]=lhs.get(x,F(0))+z;lhs[qq[c]]=lhs.get(qq[c],F(0))-z
        rhs=lvadd(((1-t)/t,DV(rr,qq)),((1-t)/t,DV(qq,rr)))
        ck(not lvadd((1,lhs),(-1,rhs)))
        if rr!=qq:
            slack=sub(sub(DD(p,q),DD(p,r)),DD(r,q));ck(slack[0]>=0)
    elif t==0:ck(r==q)
    else:
        # Complete fee is the exact cell KL since within-cell likelihood is constant.
        for a,x in r.items():
            if x:ck(x/q[a]==rr[bool(a)]/qq[bool(a)])
    return r

states=queries=updates=trees=0
for m in ([1] if PILOT else [1,2]):
    n=2*m+1;edges=[e for j in range(m) for e in [(0,2*j+1),(0,2*j+2),(2*j+1,2*j+2)]]
    f=[1-2*int(not any((x>>u&1) and (x>>v&1) for u,v in edges)) for x in range(1<<n)]
    root=law(f,(-1,)*n);v=1-root[0];mass={}
    for mask in range(1,1<<n):
        u=sum(((mask>>(2*j+1)&1)+(mask>>(2*j+2)&1))==1 for j in range(m))
        d=sum(((mask>>(2*j+1)&1)+(mask>>(2*j+2)&1))==2 for j in range(m))
        mass[mask]=masses(m,u,d,F(1,2),F(1,2*m))[mask&1]
    Z=sum(mass.values());qroot={0:1-v,**{a:v*x/Z for a,x in mass.items()}}
    def Qstate(state):
        q=qroot
        for i,x in enumerate(state):
            if x>=0:q=project(q,i)
        return q
    for state in product([-1,0,1],repeat=n):
        p=law(f,state);q=Qstate(state);states+=1
        ck(sum(p.values())==sum(q.values())==1)
        for t in [F(0),F(1,2),F(1)]:profiles(p,q,t);updates+=1
        for i,x in enumerate(state):
            if x>=0:continue
            pp=project(p,i);qq=project(q,i);kids=[]
            for b in [0,1]:
                child=list(state);child[i]=b;kids.append(law(f,child))
            ck(all(pp.get(a,0)==sum(c.get(a,0) for c in kids)/2 for a in pp))
            Jvec=lvadd((F(1,2),DV(kids[0],pp)),(F(1,2),DV(kids[1],pp)))
            Lvec=lvadd((1,DV(p,q)),(-1,DV(pp,qq)))
            ck(not lvadd((F(1,2),DV(kids[0],qq)),(F(1,2),DV(kids[1],qq)),(-1,DV(p,q)),(-1,Jvec),(1,Lvec)))
            influence=sum((z for a,z in p.items() if a>>i&1),F(0))
            jinterval=scale(plus(DD(kids[0],pp),DD(kids[1],pp)),F(1,2))
            if influence:ck(jinterval[1]<=(2/LN2[1])*influence)
            else:ck(all(c==pp for c in kids))
            queries+=1
    def tree(state,q,order):
        p=law(f,state)
        if not order:return CC(p,q)
        r=profiles(p,q,F(1,2));fee=DD(r,q);i=order[0]
        pp=project(p,i);qq=project(r,i);L=sub(DD(p,r),DD(pp,qq))
        childP=[];future=[]
        for b in [0,1]:
            st=list(state);st[i]=b;childP.append(law(f,st));future.append(tree(tuple(st),qq,order[1:]))
        delta=sub(HH(p),scale(plus(*(HH(z) for z in childP)),F(1,2)))
        return plus(fee,L,delta,scale(plus(*future),F(1,2)))
    rootI=sum((a.bit_count()*x for a,x in root.items()),F(0));b=F(1,7)
    for order in [(0,1),(1,0)]:
        bill=tree((-1,)*n,qroot,order)
        ck(b+bill[1]<=b+CC(root,qroot)[0]+(2/LN2[1])*rootI);trees+=1
out={'helper_version':'A014-windmill-original-full-history-v1','mode':'pilot' if PILOT else 'main','physical_restriction_states':states,'actual_query_edges':queries,'profile_updates':updates,'complete_depth2_trees':trees,'assertions':CHECKS,'elapsed_seconds':time.monotonic()-START,'scope':'full projection/profile bill only; no true-kernel substitution or mandatory floors'}
(RUN/'out'/('history_pilot.json' if PILOT else 'history.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
