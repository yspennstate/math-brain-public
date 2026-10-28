import json, itertools, time, sys
from functools import lru_cache
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
checks=0
def ck(v):
    global checks
    checks+=1
    assert v, checks
def walsh(a):
    return _walsh(tuple(a))
@lru_cache(maxsize=4096)
def _walsh(a):
    a=list(map(F,a)); n=len(a); h=1
    while h<n:
        for j in range(0,n,2*h):
            for k in range(j,j+h):
                x,y=a[k],a[k+h]; a[k],a[k+h]=x+y,x-y
        h*=2
    return tuple(x/n for x in a)
def law(a): return [x*x for x in walsh(a)]
def prod(vs):
    out=[F(1)]
    for v in vs: out=[a*b for b in v for a in out]
    return out
def mix(comps,c):
    out=[F(0)]*len(prod(comps[0][1]))
    for w,vs in comps:
        for k,z in enumerate(prod(vs)): out[k]+=w*z
    out[0]+=c
    return out
def cal(p,comps,c,x):
    q=mix(comps,c); rho=p[0]
    if rho==1:
        cs=[(F(0),vs) for _,vs in comps]
        return cs,F(1)
    z=sum(q[s]*x**s.bit_count() for s in range(1,len(q)))
    ck(z>0); A=(1-rho)/z; out=[]
    for w,vs in comps:
        nv=[]; nw=w*A
        for v in vs:
            t=[a*x**s.bit_count() for s,a in enumerate(v)]; mass=sum(t)
            ck(mass>0); nw*=mass; nv.append([a/mass for a in t])
        out.append((nw,nv))
    nc=A*c+rho-A*q[0]; u=mix(out,nc)
    expected=[rho]+[A*q[s]*x**s.bit_count() for s in range(1,len(q))]
    ck(u==expected); ck(sum(u)==1); ck(min(u)>=0)
    ck(all(not a or b>0 for a,b in zip(p,u)))
    return out,nc
def delete(s,i): return (s&((1<<i)-1))|((s>>(i+1))<<i)
def branch(a,i,s):
    n=(len(a)).bit_length()-1
    return [a[(t&((1<<i)-1))|((t>>i)<<(i+1))|((0 if s==1 else 1)<<i)] for t in range(1<<(n-1))]
def kernel(a,i,s):
    co=walsh(a); out=[]
    for t in range(len(a)//2):
        k=(t&((1<<i)-1))|((t>>i)<<(i+1)); aa,bb=co[k],co[k|(1<<i)]
        out.append((aa+s*bb)**2/(2*(aa*aa+bb*bb)) if aa*aa+bb*bb else F(1,2))
    return out
def push(v,i,k):
    out=[F(0)]*(len(v)//2)
    for t,a in enumerate(v): out[delete(t,i)]+=a*k[delete(t,i)]
    return out
def query(fs,comps,c,j,i,s):
    k=kernel(fs[j],i,s); out=[]
    for w,vs in comps:
        v=push(vs[j],i,k); z=sum(v); nv=list(vs)
        nv[j]=[a/z for a in v] if z else [F(1)]+[F(0)]*(len(v)-1)
        out.append((w*z,nv))
    nc=c*k[0]; mass=sum(w for w,_ in out)+nc
    ck(mass>0); out=[(w/mass,vs) for w,vs in out]; nc/=mass
    nf=list(fs); nf[j]=branch(fs[j],i,s)
    # independent full-table kernel, including every ghost row
    q=mix(comps,c); full=prod(fs); gi=i+sum((len(v)).bit_length()-1 for v in fs[:j])
    # On ghost rows global convention need not equal local completion: explicitly use local k.
    expected=[F(0)]*(len(q)//2)
    shift=sum((len(v)).bit_length()-1 for v in fs[:j]); mask=len(fs[j])-1
    for t,a in enumerate(q):
        lt=(t>>shift)&mask; expected[delete(t,gi)]+=a*k[delete(lt,i)]
    ck(sum(expected)==mass); expected=[a/mass for a in expected]
    ck(mix(out,nc)==expected); ck(min(expected)>=0); ck(sum(expected)==1)
    ck(law(prod(nf))==prod([law(f) for f in nf]))
    truepush=[F(0)]*(len(q)//2); pp=law(full)
    for t,a in enumerate(pp):
        lt=(t>>shift)&mask; truepush[delete(t,gi)]+=a*k[delete(lt,i)]
    ck(truepush==[a/2 for a in law(prod(nf))])
    return nf,out,nc
def main():
    start=time.monotonic(); choices=[]
    for n in (1,2):
        choices.extend(itertools.product((-1,1),repeat=1<<n))
    pairs=list(itertools.product(choices,repeat=2))
    if len(sys.argv)>1 and sys.argv[1]=='pilot': pairs=pairs[:16]
    lo,hi=0,len(pairs)
    if len(sys.argv)>3:
        lo,hi=int(sys.argv[2]),int(sys.argv[3]); pairs=pairs[lo:hi]
    negative_c=0; queries=0
    for fs in pairs:
        ck(time.monotonic()-start<55)
        ps=[law(f) for f in fs]; p=prod(ps)
        comps=[(F(1,2),ps),(F(1,2),[[F(0)]*(len(f)-1)+[F(1)] for f in fs])]
        for x in (F(1,3),F(1),F(2)):
            cs,c=cal(p,comps,F(0),x); negative_c+=c<0
            for j in range(2):
                for i in range((len(fs[j])).bit_length()-1):
                    for s in (-1,1):
                        nf,ns,nc=query(fs,cs,c,j,i,s); queries+=1
                        ns,nc=cal(law(prod(nf)),ns,nc,F(2,3))
                        for jj in range(2):
                            for ii in range((len(nf[jj])).bit_length()-1):
                                for ss in (-1,1):
                                    query(nf,ns,nc,jj,ii,ss); queries+=1
        # Exactly matched finite-tilt fixture: inverse tilt of actual product P.
        x=F(2,3); inv=[]
        for v in ps:
            vv=[a*x**(-s.bit_count()) for s,a in enumerate(v)]; z=sum(vv)
            inv.append([a/z for a in vv])
        cs,c=cal(p,[(F(1),inv)],F(0),x)
        ck(mix(cs,c)==p)
    for n in (4,6,8):
        M=1<<n; x=F(1,3); A=2*F(M-1)/((1+x)**n-1+M*x**n)
        u=[A*(1+x)**n/(2*M)*(x/(1+x))**s.bit_count()*(1/(1+x))**(n-s.bit_count()) for s in range(M)]
        u[-1]+=A*x**n/2; u[0]+=(1-A/2)/M
        ck(u[0]==F(1,M)); ck(sum(u)==1); ck(min(u)>=0)
        ck(all(u[s]==A*x**s.bit_count()/(2*M)+(A*x**n/2 if s==M-1 else 0) for s in range(1,M)))
    result={'status':'PASS','roots':len(pairs),'queries':queries,'assertions':checks,'negative_vacuum_coefficients':negative_c,'seconds':time.monotonic()-start,'arithmetic':'Fraction; no floating probability/sign comparisons'}
    result['root_range']=[lo,hi]
    name='pilot.json' if len(pairs)==16 else f'main_{lo:03}_{hi:03}.json'
    (ROOT/'out'/name).write_text(json.dumps(result,indent=2),encoding='utf-8'); print(json.dumps(result))
if __name__=='__main__': main()
