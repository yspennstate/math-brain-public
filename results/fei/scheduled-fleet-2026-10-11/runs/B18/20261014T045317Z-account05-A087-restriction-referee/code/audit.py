import sys,itertools,json,time,hashlib
from fractions import Fraction as Q
from functools import lru_cache
import exact as e
checks=0
def eq(a,b):
    global checks
    checks+=1;assert a==b
def ge(v):
    global checks
    checks+=1;assert not v or e.log_bounds(v)[0]>=0
def leprice(v,d,k,extra=0):
    global checks
    checks+=1;assert e.log_bounds(v)[1]<=k*d*e.ln_interval(2)[0]+extra*d
def avg(a,b):return e.scale(e.add(a,b),Q(1,2))
def clear():
    for f in (e.walsh,e.entropy,e.child,e.inf):f.cache_clear()
def point_f(u,G,r):
    return tuple(u[(z>>r)&(len(u)-1)] if z&((1<<r)-1)==0 else G[z>>(r+e.dimension(u))] for z in range((1<<r)*len(u)*len(G)))
def activation(v,s):return tuple(v[z>>s] if z&((1<<s)-1)==0 else 1 for z in range((1<<s)*len(v)))
def release(p,W,Vu):return e.add(((2,p*Vu),) if p*Vu else (),e.scale(e.add(e.phi(1-p),e.scale(e.phi(1-2*p),Q(-1,2))),W))
def pointcheck(u,G,r,W):
    f=point_f(u,G,r);p=Q(1,1<<r);y=e.walsh(u)[0];x=e.walsh(G)[0];V=1-x*x;Vu=1-y*y;t=y-x;M=x+p*t;d=p*(1-x*y)
    kp=release(p,W,Vu);B=e.erasure(f,0);D=e.decrement(f,0)
    formula=e.add(((2,p*Vu+(p-2*p*p)*(V+t*t)),),e.scale(e.packet((1-p)**2,p*p),V),e.packet(M*M,p*p*t*t))
    eq(B,formula);eq(e.inf(f,0),d);ge(kp)
    residual=e.add(D,e.scale(kp,-1));leprice(residual,d,8,2)
    # Check source-owned 11-priced reserve drift and separately priced 8+2/ln2.
    leprice(residual,d,11)
    return f,kp
def bank(p,k,u,v):return e.add(e.scale(e.phi(p),1-e.walsh(u)[0]**2),e.scale(e.phi((1-p)*k),1-e.walsh(v)[0]**2))
def pointphase(pilot):
    hs=[tuple(x) for n in range(3) for x in itertools.product((-1,1),repeat=1<<n)];cases=0
    for u,v,(r,s) in itertools.product(hs,hs,((2,1),(3,1),(2,2))):
        G=activation(v,s);p=Q(1,1<<r);k=Q(1,1<<s);W=k*(1-e.walsh(v)[0]**2)
        f,kp=pointcheck(u,G,r,W)
        eq(kp,e.add(bank(p,k,u,v),e.scale(avg(bank(2*p,k,u,v),bank(Q(0),k,u,v)),-1)))
        # Independently compute actual first fresh u-data drift with inherited H reserves.
        root=e.add(e.scale(e.entropy(u),p),e.scale(e.entropy(v),(1-p)*k),bank(p,k,u,v))
        if len(u)>1:
            ru=e.child(u,0,0);rv=e.child(u,0,1)
            ca=e.add(e.scale(e.entropy(ru),p),e.scale(e.entropy(v),(1-p)*k),bank(p,k,ru,v))
            cb=e.add(e.scale(e.entropy(rv),p),e.scale(e.entropy(v),(1-p)*k),bank(p,k,rv,v))
            debit=e.add(e.decrement(f,r),e.scale(root,-1),avg(ca,cb))
            leprice(debit,e.inf(f,r),Q(11,2))
        cases+=1
        if cases%32==0:clear()
        if pilot and cases==8:break
    return cases
def fallback(labels,v,w):
    return tuple(1 if labels[z&3]==0 else v[(z>>2)&1] if labels[z&3]==1 else w[z>>3] for z in range(16))
def manyphase(pilot):
    hs=list(itertools.product((-1,1),repeat=2));cases=0
    for labels,u,v,w in itertools.product(itertools.product(range(3),repeat=4),hs,hs,hs):
        G=fallback(labels,v,w);qs=(Q(labels.count(1),4),Q(labels.count(2),4));W=sum(q*(1-e.walsh(h)[0]**2) for q,h in zip(qs,(v,w)))
        f,kp=pointcheck(u,G,2,W);p=Q(1,4)
        def R(prob):return e.add(e.scale(e.phi(prob),1-e.walsh(u)[0]**2),*(e.scale(e.phi((1-prob)*q),1-e.walsh(h)[0]**2) for q,h in zip(qs,(v,w))))
        eq(kp,e.add(R(p),e.scale(avg(R(2*p),R(Q(0))),-1)))
        cases+=1
        if cases%32==0:clear()
        if pilot and cases==8:break
    return cases
def betaB(b,m,n):
    q=(1+b)/2;p=1-q;a=(m+n)/2;c=(m-n)/2;delta=(1-m*n)/2;Vu=1-m*m;Vv=1-n*n
    return e.add(e.phi((a+c*b)**2),e.scale(e.phi(b*b),-delta),e.scale(e.phi(c*c),1-b*b),((2,(Vu+Vv)*(1-b*b)/2),),e.scale(e.phi(q*q),Vu),e.scale(e.phi(p*p),Vv),e.scale(e.phi(m*m),-q),e.scale(e.phi(n*n),-p))
def compose(h,u,v):
    return tuple(u[(z>>e.dimension(h))&(len(u)-1)] if h[z&(len(h)-1)]==1 else v[z>>(e.dimension(h)+e.dimension(u))] for z in range(len(h)*len(u)*len(v)))
def potential(h,u,v):
    b=e.walsh(h)[0];m=e.walsh(u)[0];n=e.walsh(v)[0];q=(1+b)/2;p=1-q;delta=(1-m*n)/2
    return e.add(e.scale(e.entropy(u),q),e.scale(e.entropy(v),p),e.scale(e.phi(q),1-m*m),e.scale(e.phi(p),1-n*n),e.scale(e.entropy(h),delta))
def binaryphase(pilot):
    hs=list(itertools.product((-1,1),repeat=4));cases=0
    for h,u,v in itertools.product(hs,hs,hs):
        b=e.walsh(h)[0];m=e.walsh(u)[0];n=e.walsh(v)[0];q=(1+b)/2;p=1-q;delta=(1-m*n)/2;f=compose(h,u,v)
        eq(e.entropy(f),e.add(e.scale(e.entropy(h),delta),e.scale(e.entropy(u),q),e.scale(e.entropy(v),p),betaB(b,m,n)))
        eq(betaB(Q(1),m,n),());eq(betaB(Q(-1),m,n),())
        for i in (0,1):
            a=e.child(h,i,0);c=e.child(h,i,1);ba=e.walsh(a)[0];bc=e.walsh(c)[0]
            correction=e.add(betaB(b,m,n),e.scale(avg(betaB(ba,m,n),betaB(bc,m,n)),-1))
            eq(e.decrement(f,i),e.add(e.scale(e.decrement(h,i),delta),correction));eq(e.inf(f,i),delta*e.inf(h,i));leprice(correction,e.inf(f,i),22)
        P=potential(h,u,v)
        for j,hj in enumerate((h,u,v)):
            ff=0 if j==0 else 2 if j==1 else 4;other=[h,u,v];kids=[]
            for bit in (0,1):
                arr=other.copy();arr[j]=e.child(hj,0,bit);kids.append(potential(*arr))
            debit=e.add(e.decrement(f,ff),e.scale(P,-1),avg(*kids))
            leprice(debit,e.inf(f,ff),22 if j==0 else Q(11,2))
        cases+=1
        if cases%32==0:clear()
        if pilot and cases==8:break
    return cases
def run(phase,pilot):
    start=time.monotonic();cases={'point':pointphase,'many':manyphase,'binary':binaryphase}[phase](pilot)
    elapsed=time.monotonic()-start;assert elapsed<=(55 if pilot else 240)
    result={'status':'PASS','phase':phase,'Boolean_cases':cases,'exact_assertions':checks,'seconds':elapsed,'helper_sha256':hashlib.sha256(e.Path(__file__).read_bytes()).hexdigest(),'arithmetic_helper_sha256':hashlib.sha256(e.Path(e.__file__).read_bytes()).hexdigest(),'scope':'Source claims at explicit inherited-reserve/terminal scope; no universal FEI admission'}
    (e.ROOT/'out'/f'{phase.upper()}_{"PILOT" if pilot else "CHECK"}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':run(sys.argv[1],sys.argv[2]=='pilot')
