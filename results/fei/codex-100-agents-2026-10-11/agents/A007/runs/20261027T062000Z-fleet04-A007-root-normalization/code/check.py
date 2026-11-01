"""Independent exact physical checks; no source executable is imported."""
import argparse, hashlib, json, math, time
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter()
CHECKS=0
def ck(p, label):
    global CHECKS
    CHECKS+=1
    if not p: raise AssertionError(label)
    if time.perf_counter()-START>55: raise RuntimeError('frozen55s')
def fw(a):
    a=list(a); step=1
    while step<len(a):
        for j in range(0,len(a),2*step):
            for k in range(j,j+step):
                u,v=a[k],a[k+step];a[k],a[k+step]=u+v,u-v
        step*=2
    return a
def mono(g,s):
    return all(g[z]<=g[z|(1<<i)] for z in range(1<<s) for i in range(s))
def anchors(g,s):
    return [((1<<s)-1)^z for z in range(1<<s) if g[z]<0 and all(g[z|(1<<i)]>0 for i in range(s) if not(z>>i&1))]
def fac(n):
    out={};p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p=3 if p==2 else p+2
    if n>1:out[n]=out.get(n,0)+1
    return out
def logq(x):
    d=fac(x.numerator)
    for p,k in fac(x.denominator).items():d[p]=d.get(p,0)-k
    return {p:Q(k) for p,k in d.items() if k}
def add(*terms):
    d={}
    for c,t in terms:
        for p,k in t.items():d[p]=d.get(p,Q(0))+c*k
    return {p:k for p,k in d.items() if k}
def ce(p,r):
    return add(*[(v,logq(1/r[k])) for k,v in p.items() if v])
def entropy(p):return ce(p,p)
def lnq(x):
    power=0
    while x>=2:x/=2;power+=1
    while x<1:x*=2;power-=1
    def series(y):
        t=(y-1)/(y+1);z=Q(0)
        for k in range(24):z+=2*t**(2*k+1)/(2*k+1)
        return z,z+2*t**49/(49*(1-t*t))
    lo,hi=series(x);a,b=series(Q(2))
    return (lo+power*a,hi+power*b) if power>=0 else (lo+power*b,hi+power*a)
def log_interval(d):
    low=high=Q(0);l2,h2=lnq(Q(2))
    for p,c in d.items():
        l,h=lnq(Q(p));l,h=l/h2,h/l2
        low+=c*(l if c>=0 else h);high+=c*(h if c>=0 else l)
    return low,high
def binary_entropy(x):return entropy({0:x,1:1-x})

def check_lift(g,s,L,duplicate):
    cs=anchors(g,s)
    if duplicate:cs=cs+[cs[0]]
    t=len(cs);n=s+t*L;N=1<<n;eps=Q(1,1<<L)
    b=[sum(not(z&c) for c in cs) for z in range(1<<s)]
    a=[eps**k for k in b]
    f=[]
    for x in range(N):
        z=x&((1<<s)-1);y=x>>s
        literal=all((z&c) or (y>>(j*L+l)&1) for j,c in enumerate(cs) for l in range(L))
        direct=all((y>>(j*L+l)&1) for j,c in enumerate(cs) if not(z&c) for l in range(L))
        ck(bool(literal)==bool(direct),'literal CNF')
        f.append(1 if literal else -1)
    # Independent physical-edge counts, compared with Fourier and anchor formulas.
    flips=[Q(sum(f[x]!=f[x^(1<<i)] for x in range(N)),N) for i in range(n)]
    W=fw(f);wg=fw(g);pg={k:Q(v*v,1<<(2*s)) for k,v in enumerate(wg)}
    pf={k:Q(v*v,N*N) for k,v in enumerate(W)}
    q=Q(sum(v<0 for v in g),1<<s)
    ig=sum(Q(k.bit_count()*v*v,1<<(2*s)) for k,v in enumerate(wg))
    ck(sum(pf.values())==1,'Parseval')
    ck(sum(flips)==sum(k.bit_count()*p for k,p in pf.items()),'physical/Fourier I')
    ip=2*L*sum(k*eps**k for k in b)/(1<<s)
    ic=sum(sum(abs(a[z]-a[z^(1<<i)]) for z in range(1<<s))/(1<<s) for i in range(s))
    ck(sum(flips[s:])==ip,'private I')
    ck(sum(flips[:s])==ic,'nested core I')
    ck(abs(sum(flips)-ig)<=2*q*(s+L)*eps,'I error')
    # Exact phase-sensitive private spectrum, core and group incidence.
    for k,v in enumerate(W):
        S=k&((1<<s)-1);T=k>>s
        J=[j for j in range(t) if (T>>(j*L))&((1<<L)-1)]
        expected=sum(((-1)**((S&z).bit_count()))*(2*a[z]-1 if not T else 2*((-1)**T.bit_count())*a[z]*all(not(z&cs[j]) for j in J)) for z in range(1<<s))/(1<<s)
        ck(Q(v,N)==expected,'signed coefficient')
    mass=sum(p for k,p in pf.items() if k>>s)
    ck(mass==4*sum(x*(1-x) for x in a)/(1<<s),'private Parseval mass')
    ck(mass<=4*q*eps,'private mass bound')
    # Clauses prime and irredundant; direct truth witnesses, not a completeness claim.
    for j,c in enumerate(cs):
        for l in range(L):
            bit=s+j*L+l;all_y=((1<<(t*L))-1)<<s
            x=all_y^(1<<bit)
            ck(f[x]<0 and f[x^(1<<bit)]>0,'private relevance/deletion')
            for i in range(s):
                if c>>i&1:ck(f[x|(1<<i)]>0,'core literal deletion')
    # A015 fixed-size entropy law and explicit finite error.
    collapsed={k:pf[k] for k in range(1<<s)};collapsed[1<<s]=mass
    hc=entropy(collapsed);hf=entropy(pf)
    ck(log_interval(add((1,hf),(-1,hc)))[0]>=0,'entropy collapse lower')
    ck(log_interval(add((1,hc),(mass*n,logq(Q(2))),(-1,hf)))[0]>=0,'entropy tail upper')
    tv=(sum(abs(pf[k]-pg[k]) for k in range(1<<s))+mass)/2
    ck(tv<=4*eps,'fixed alphabet TV')
    if L>=3:
        err=add((1,binary_entropy(4*eps)),(4*eps*s+4*q*eps*n,logq(Q(2))))
        diff=add((1,hf),(-1,entropy(pg)))
        ck(log_interval(add((1,err),(-1,diff)))[0]>=0,'entropy finite upper')
        ck(log_interval(add((1,err),(1,diff)))[0]>=0,'entropy finite lower')
    # Nonzero granularity and dominance, with its exact side condition.
    rho=(1<<s)*q*eps
    for k in range(1,1<<s):
        if wg[k]:ck(abs(Q(wg[k],1<<s))>=Q(2,1<<s),'granularity')
        ck(abs(Q(W[k],N)-Q(wg[k],1<<s))<=2*q*eps,'amplitude perturbation')
        if rho<1:ck(pf[k]>=(1-rho)**2*pg[k],'domination')
    E=range(1,1<<s);p={k:pg[k] for k in E};u={k:pf[k] for k in E}
    # Algebra holds without dominance; the upper bound is used only when rho<1.
    aa=(1-rho)**2 if rho<1 else Q(1,16)
    for profile in (0,1):
        weights={k:1 if profile==0 else k+1 for k in E};total=sum(weights.values())
        r={k:Q(v,total) for k,v in weights.items()};cp=ce(p,r);v=sum(p.values())
        for j in (1,7,128):
            Z=Q(1,1<<j);R={k:Z*r[k] for k in E}
            D=ce(u,R);B=ce({k:u[k]-aa*p[k] for k in E},R)
            rhs=add((1/aa,D),(-1/aa,B),(v,logq(Z)))
            ck(cp==rhs,'exact refund plus surplus')
            if rho<1:
                ck(all(u[k]-aa*p[k]>=0 for k in E),'surplus positive')
                ck(log_interval(B)[0]>=0,'surplus bill nonnegative')
    return {'s':s,'L':L,'duplicate':duplicate,'n':n,'truth_inputs':N}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--pilot',action='store_true');args=parser.parse_args()
    rows=[];cores=0
    for s in range(1,3 if args.pilot else 4):
        for table in range(1, (1<<(1<<s))-1):
            g=[1 if table>>z&1 else -1 for z in range(1<<s)]
            if not mono(g,s):continue
            cores+=1
            for L in ((1,2) if args.pilot else (1,2,3)):rows.append(check_lift(g,s,L,False))
            if not args.pilot:
                for L in (1,2):rows.append(check_lift(g,s,L,True))
    scalar=0
    for s in range(1,5 if args.pilot else 65):
        for j in range(3 if args.pilot else 17):
            delta=Q(1,1<<j);A=4+j;L=2*s+2*A;eps=Q(1,1<<L)
            rho=(1<<s)*eps/2;aa=(1-rho)**2;d=(s+L)*eps
            ck(rho<1 and d<=delta/16,'finite parameters')
            ck((1+d)<=aa*(1+delta),'finite source ratio')
            scalar+=1
    # Missing dominance really invalidates the asserted bound.
    # p=(1,0),u=(1/4,3/4), a=1, r=(1/16,15/16).
    p={0:Q(1),1:Q(0)};u={0:Q(1,4),1:Q(3,4)};r={0:Q(1,16),1:Q(15,16)}
    ck(log_interval(add((1,ce(p,r)),(-1,ce(u,r))))[0]>0,'no domination countercontrol')
    # Signed anchor edge: active disjoint singleton groups have equal a but disagree.
    ck(Q(1,2)+Q(1,2)-2*Q(1,4)>abs(Q(1,2)-Q(1,2)),'signed nesting countercontrol')
    # AND2 fails the common-scaling shortcut at epsilon=1/2.
    ck(1-Q(1,2)**2 != (1-Q(1,2))**2,'AND2 unequal scaling')
    result={'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'pilot':args.pilot,'cores':cores,'lifts':len(rows),'scalar_pairs':scalar,'checks':CHECKS,'truth_inputs':sum(r['truth_inputs'] for r in rows),'maximum_dimension':max(r['n'] for r in rows),'elapsed_seconds':time.perf_counter()-START,'verdict':'PASS','cases':rows}
    path=ROOT/'out'/('pilot.json' if args.pilot else 'checks.json');path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
if __name__=='__main__':main()
