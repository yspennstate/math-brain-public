import sys,json,time,itertools,hashlib
from functools import lru_cache
from fractions import Fraction as Q
import exact as e
checks=0
def eq(a,b):
    global checks
    checks+=1;assert a==b
def ge(v):
    global checks
    checks+=1
    assert not v or e.log_bounds(v)[0]>=0
def av(a,b):return e.scale(e.add(a,b),Q(1,2))
def pos(v):
    if not v:return ()
    lo,hi=e.log_bounds(v)
    if hi<=0:return ()
    assert lo>=0
    return v
def priced(v,d,c):return e.add(v,((2,-c*d),) if c*d else ())
@lru_cache(None)
def reserve(h,C):
    if len(h)==1:return ()
    return pos(e.add(priced(e.decrement(h,0),e.inf(h,0),C),av(reserve(e.child(h,0,0),C),reserve(e.child(h,0,1),C))))
def lifted(u,v,o,C):
    p=Q(1,4);r=Q(1,8) if o==0 else Q(1,4)
    return e.add(*(e.add(e.scale(reserve(h,C),q),e.scale(e.phi(q),1-e.walsh(h)[0]**2)) for h,q in ((u,p),(v,r))))
def meanprofile(f,nctrl):
    return tuple(sum(f[z|(a<<nctrl)] for a in range(len(f)>>nctrl))/Q(len(f)>>nctrl) for z in range(1<<nctrl))
@lru_cache(None)
def node(u,v,o):
    f=e.priority(u,v,o);p=Q(1,4);r=Q(1,8) if o==0 else Q(1,4)
    vu=1-e.walsh(u)[0]**2;vv=1-e.walsh(v)[0]**2;k=p*vu+r*vv
    g=meanprofile(f,3);g0=e.child(g,0,0);g1=e.child(g,0,1)
    mu=sum(g0)/4;nu=sum(g1)/4;V0=sum(x*x for x in g0)/4-mu*mu;V1=sum(x*x for x in g1)/4-nu*nu
    B=e.erasure(f,0);D=e.decrement(f,0);d=e.inf(f,0);resB=e.add(B,((2,-k),) if k else ())
    formula=e.add(((2,(V0+V1)/2),) if V0+V1 else (),e.packet(((mu+nu)/2)**2,((mu-nu)/2)**2))
    eq(resB,formula);ge(resB)
    price=3 if o==0 else 4
    residual=e.add(D,((2,-k),) if k else ())
    ge(residual)
    # (price+2/ln2)d in bits; multiply by ln2 for an exact sign vector.
    lo,hi=e.log_bounds(residual);eq(hi<=price*d*e.ln_interval(2)[0]+2*d,True)
    if o==0:eq(d,(1-mu)/2);eq(nu,Q(1))
    else:eq(d,(1-mu*nu)/2)
    for C in (0,2):
        parent=lifted(u,v,o,C)
        for j,h in enumerate((u,v)):
            if len(h)==1:continue
            i=3+(e.dimension(u) if j else 0)
            a=e.child(h,0,0);b=e.child(h,0,1)
            ra=lifted(a,v,o,C) if j==0 else lifted(u,a,o,C)
            rb=lifted(b,v,o,C) if j==0 else lifted(u,b,o,C)
            drift=e.add(parent,e.scale(av(ra,rb),-1))
            ge(e.add(drift,priced(e.scale(e.decrement(f,i),-1),-e.inf(f,i),Q(C)+Q(11,2))))
    return True
@lru_cache(None)
def prefix(u,v,o,C,policy):
    f=e.priority(u,v,o);alpha=Q(C)+Q(11,2)
    if len(u)==len(v)==1:
        # Boundary entropy is a valid declared controller potential.
        return (),e.entropy(f),e.entropy(f)
    j=0 if len(u)>1 and (len(v)==1 or policy==0 or e.walsh(u)[0]>=e.walsh(v)[0]) else 1
    h=(u,v)[j];kids=[]
    for bit in (0,1):
        hh=e.child(h,0,bit)
        kids.append(prefix(hh,v,o,C,policy) if j==0 else prefix(u,hh,o,C,policy))
    i=3+(e.dimension(u) if j else 0);inc=priced(e.decrement(f,i),e.inf(f,i),alpha)
    return pos(e.add(inc,av(kids[0][0],kids[1][0]))),pos(e.add(inc,av(kids[0][1],kids[1][1]))),av(kids[0][2],kids[1][2])
def point(h,r):
    return tuple(h[z>>r] if (z&((1<<r)-1))==0 else 1 for z in range((1<<r)*len(h)))
def pointcheck(h,r):
    f=point(h,r);q=Q(1,1<<r);m=e.walsh(h)[0];k=q*(1-m*m);d=e.inf(f,0)
    B=e.add(e.erasure(f,0),((2,-k),) if k else ());D=e.add(e.decrement(f,0),((2,-k),) if k else ())
    z=q*(1-m)
    eq(d,z);eq(B,e.add(((2,z*(1-m)-2*z*z),) if z else (),e.packet((1-z)**2,z*z)))
    ge(B);ge(D);eq(e.log_bounds(D)[1]<=3*d*e.ln_interval(2)[0]+2*d,True)
    # Profile identity checked directly, including actual unresolved controls.
    U=e.scale(e.add(e.entropy(h),e.scale(e.phi(m*m),-1)),q);R=e.scale(e.phi(q),1-m*m)
    profile=meanprofile(f,r);cg=e.walsh(tuple(int(z==0) for z in range(1<<r)))
    gamma=tuple(x*x/q for x in cg)
    G=e.add(*(e.phi(x*x) for x in e.walsh(profile)),e.scale(e.add(*(e.phi(x) for x in gamma)),q*(1-m*m)))
    eq(e.add(e.entropy(f),e.scale(U,-1),e.scale(R,-1)),G);ge(G)
def mux(a,b):return tuple((a[(z>>1)&(len(a)-1)] if z&1==0 else b[z>>(1+e.dimension(a))]) for z in range(2*len(a)*len(b)))
def generic(a,b):
    f=mux(a,b);mu=e.walsh(a)[0];nu=e.walsh(b)[0];k=(2-mu*mu-nu*nu)/2;d=e.inf(f,0)
    B=e.add(e.erasure(f,0),((2,-k),) if k else ())
    eq(B,e.packet(((mu+nu)/2)**2,((mu-nu)/2)**2));eq(d,(1-mu*nu)/2)
    D=e.add(e.decrement(f,0),((2,-k),) if k else ());ge(D);eq(e.log_bounds(D)[1]<=4*d*e.ln_interval(2)[0]+2*d,True)
def run(pilot):
    start=time.monotonic();roots=faces=0;fs=list(itertools.product((-1,1),repeat=4))
    for u,v,o in itertools.product(fs,fs,(0,1)):
        for a,b in itertools.product(e.faces(u),e.faces(v)):node(a,b,o);faces+=1
        for C,policy in itertools.product((0,2),(0,1)):
            qp,qf,bound=prefix(u,v,o,C,policy);R=lifted(u,v,o,C)
            ge(e.add(R,e.scale(qp,-1)));ge(e.add(R,bound,e.scale(qf,-1)))
        roots+=1
        if time.monotonic()-start>(55 if pilot else 240):raise RuntimeError('frozen runtime reached')
        if pilot and roots==8:break
    if not pilot:
        allh=[tuple(x) for n in range(3) for x in itertools.product((-1,1),repeat=1<<n)]
        for h,r in itertools.product(allh,(1,2)):pointcheck(h,r)
        for a,b in itertools.product(fs,fs):generic(a,b)
    out={'status':'PASS','priority_roots':roots,'physical_data_faces':faces,'distinct_priority_nodes':node.cache_info().currsize,'point_nodes':0 if pilot else 44,'generic_independent_branch_roots':0 if pilot else 256,'exact_assertions':checks,'seconds':time.monotonic()-start,'helper_sha256':hashlib.sha256(e.Path(__file__).read_bytes()).hexdigest(),'arithmetic_helper_sha256':hashlib.sha256(e.Path(e.__file__).read_bytes()).hexdigest(),'scope':'New shared controller residual, retained profile boundary, additional A064 v2 reserve lift/graft; no arbitrary core or controller entropy payment'}
    (e.ROOT/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':run(sys.argv[1]=='pilot')
