from fractions import Fraction as R
from functools import lru_cache
from pathlib import Path
import json, time

BASE=Path(__file__).resolve().parents[1]
checks=0
def require(test):
    global checks
    assert test
    checks+=1

def walsh(t):
    w=list(t); step=1
    while step<len(w):
        for start in range(0,len(w),2*step):
            for j in range(start,start+step):
                a,b=w[j],w[j+step]; w[j],w[j+step]=a+b,a-b
        step*=2
    return [R(a,len(w)) for a in w]

def table(bits,label):
    return [1 if label>>j&1 else -1 for j in range(1<<bits)]

def influence(t):
    n=(len(t)-1).bit_length()
    return [R(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(n)]

@lru_cache(None)
def factors(n):
    out={}; p=2
    while p*p<=n:
        while n%p==0: out[p]=out.get(p,0)+1; n//=p
        p+=1
    if n>1: out[n]=out.get(n,0)+1
    return out

def addlog(out,q,c):
    if not c: return
    assert q>0
    for n,sgn in [(q.numerator,1),(q.denominator,-1)]:
        for p,a in factors(n).items():
            out[p]=out.get(p,R(0))+c*sgn*a
            if not out[p]: del out[p]

def ce(p,q):
    out={}
    for x,y in zip(p,q):
        if x: addlog(out,y,-x)
    return out

def combine(*terms):
    out={}
    for c,expr in terms:
        for p,a in expr.items():
            out[p]=out.get(p,R(0))+c*a
            if not out[p]: del out[p]
    return out

def lnunit(x):
    z=(x-1)/(x+1); z2=z*z; power=z; total=R(0)
    for j in range(40):
        total+=2*power/(2*j+1); power*=z2
    return total,total+2*power/(81*(1-z2))

L2,U2=lnunit(R(2))
@lru_cache(None)
def logbounds(p):
    k=p.bit_length()-1
    lo,hi=lnunit(R(p,1<<k))
    return R(k)+lo/U2,R(k)+hi/L2

def bounds(expr):
    lo=hi=R(0)
    for p,c in expr.items():
        a,b=logbounds(p)
        lo+=c*(a if c>=0 else b); hi+=c*(b if c>=0 else a)
    return lo,hi

def calibrate(p,raw):
    v=1-p[0]-p[1]; rem=sum(raw[2:]); out=[p[0],p[1]]
    out.extend(v*x/rem if v else R(0) for x in raw[2:])
    require(sum(out)==1)
    require(all(not x or y>0 for x,y in zip(p,out)))
    diff=combine((1,ce(p,raw)),(-1,ce(p,out)))
    require(not diff or bounds(diff)[0]>=0)
    return out

def main():
    start=time.perf_counter(); cases=0; refcases=0; maxdim=0
    for gx,hy in [(1,1),(2,1)]:
        ng,nh=1+gx,1+hy
        gt=[table(ng,i) for i in range(1<<(1<<ng))]
        ht=[table(nh,i) for i in range(1<<(1<<nh))]
        for tg in gt:
            ag=walsh(tg); pg=[a*a for a in ag]; ig=influence(tg)
            for th in ht:
                ah=walsh(th); ph=[a*a for a in ah]; ih=influence(th)
                # s index 0, private X indices 1..gx, private Y thereafter, z last.
                n=2+gx+hy; N=1<<(n-1); maxdim=max(maxdim,n)
                a=[R(0)]*N; b=[R(0)]*N
                for j,x in enumerate(ag): a[j]=x
                for j,x in enumerate(ah): b[(j&1)|((j>>1)<<(1+gx))]=x
                tf=[]
                for j in range(1<<n):
                    gi=j&((1<<ng)-1)
                    hj=(j&1)|(((j>>(1+gx))&((1<<hy)-1))<<1)
                    tf.append(tg[gi] if not (j>>(n-1)) else th[hj])
                af=walsh(tf); pf=[x*x for x in af]; edges=influence(tf)
                require(all(af[j]==(a[j]+b[j])/2 and af[j+N]==(a[j]-b[j])/2 for j in range(N)))
                d=edges[-1]; dot=a[0]*b[0]+a[1]*b[1]
                require(d==(1-dot)/2)
                require(sum(edges)==(sum(ig)+sum(ih))/2+d)
                require(sum(j.bit_count()*p for j,p in enumerate(pf))==sum(edges))
                require(edges[0]==(ig[0]+ih[0])/2)
                require(sum(abs(x) for x in a[:2])<=1 and sum(abs(x) for x in b[:2])<=1)
                require(sum(abs(a[j]-b[j]) for j in (0,1))<=4*d)
                require(max(abs(a[j]-b[j]) for j in (0,1))<=2*d)
                require(sum(abs(a[j]**2-b[j]**2) for j in (0,1))<=4*d)
                vg=1-pg[0]-pg[1]; vh=1-ph[0]-ph[1]
                require((vg+vh)/2<=2*d)
                hf=ce(pf,pf); hg=ce(pg,pg); hh=ce(ph,ph)
                delta=combine((1,hf),(-R(1,2),hg),(-R(1,2),hh))
                if d: require(bounds(delta)[1]<=(2+4/U2)*d)
                else: require(not delta)
                for mode in range(3):
                    def raw(p):
                        if mode==0: return p
                        if mode==1: return [R(1,len(p))]*len(p)
                        return [R(j+1,len(p)*(len(p)+1)//2) for j in range(len(p))]
                    rg=calibrate(pg,raw(pg)); rh=calibrate(ph,raw(ph))
                    eg=[R(0)]*N; eh=[R(0)]*N
                    for j,x in enumerate(rg): eg[j]=x
                    for j,x in enumerate(rh): eh[(j&1)|((j>>1)<<(1+gx))]=x
                    qf=[R(0)]*(2*N)
                    for j in range(N):
                        q=(a[j]**2+b[j]**2)/2; r=(eg[j]+eh[j])/2
                        qf[j]=r*pf[j]/q if q else r
                        qf[j+N]=r*pf[j+N]/q if q else R(0)
                        if q:
                            require((a[j]**2*eh[j])==(b[j]**2*eg[j]))
                    require(sum(qf)==1)
                    cf=ce(pf,qf); cg=ce(pg,rg); ch=ce(ph,rh)
                    require(not combine((1,cf),(-1,hf),(-R(1,2),cg),(R(1,2),hg),(-R(1,2),ch),(R(1,2),hh)))
                    require(not combine((1,cf),(-R(1,2),cg),(-R(1,2),ch),(-1,delta)))
                    refcases+=1
                cases+=1
    result={'status':'PASS','family_cases':cases,'reference_cases':refcases,'assertions':checks,'max_root_dimension':maxdim,'seconds':time.perf_counter()-start,'arithmetic':'Fraction + formal prime-log identities + outward rational 40-term atanh certificates','no_dimension_escalation':True}
    require(cases==4352 and refcases==13056 and maxdim==5)
    result['assertions']=checks
    (BASE/'out'/'EXACT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))

if __name__=='__main__': main()
