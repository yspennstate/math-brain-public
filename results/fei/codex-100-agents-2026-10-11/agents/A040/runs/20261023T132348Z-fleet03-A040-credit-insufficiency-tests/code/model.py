from arithmetic import *
import arithmetic as ar

def fmt(v):return [str(x) for x in v]
def overlap(a,b):ck(max(a[0],b[0])<=min(a[1],b[1]))
def same(a,b):overlap(a,b)
def bern(t):return add(entterm(t),entterm(1-t))
def phi(t):return entterm(t)
def Fmix(m,alpha):
    beta=1-alpha
    return add(scale(log(1/beta),1-m),scale(log(m/(alpha+beta*m)),m))
def core(r):
    return tuple((1-2*((x>>1)&1))*(1-2*((x>>2)==0 or ((x&1) and (x>>2)==3))) for x in range(2**(r+2)))
def G(v,eps):return tuple(eps if not(x&1) else v[x>>1] for x in range(2*len(v)))
def priority(v):return tuple((1-2*((x>>1)&1)) if not(x&1) else v[x>>3] if (x>>2)&1 else 1 for x in range(8*len(v)))
def reference(v,alpha):
    p=law(v)
    if sum(x>0 for x in p)==1:return p
    return tuple(p[0] if t==0 else (1-alpha)*p[t]+alpha*(1-p[0])*(t==len(p)-1) for t in range(len(p)))
def lifted(g,v,alpha,shift):
    p=law(g);pv=law(v);q=reference(v,alpha)
    out=tuple(x if not(t>>shift) else x*q[t>>shift]/pv[t>>shift] if pv[t>>shift] else F(0) for t,x in enumerate(p))
    ck(sum(out)==1 and all((x>0)==(y>0) for x,y in zip(p,out)))
    return out
def branch(g,q,j):
    ps=law(g);children=[restrict(g,j,y) for y in (0,1)];pc=[law(x) for x in children];pb=[];qb=[]
    for t in range(len(pc[0])):
        lo=t%(1<<j)+(t>>j)*(1<<(j+1));hi=lo+(1<<j)
        pb.append(ps[lo]+ps[hi]);qb.append(q[lo]+q[hi])
    qs=[];zs=[]
    for y in (0,1):
        raw=[qq*(pp/(2*p) if p else F(1,2)) for p,qq,pp in zip(pb,qb,pc[y])]
        z=sum(raw);ck(z>0);qs.append(tuple(t/z for t in raw));zs.append(z)
    ck(sum(zs)==1)
    return children,qs,zs,tuple(pb),tuple(qb)

