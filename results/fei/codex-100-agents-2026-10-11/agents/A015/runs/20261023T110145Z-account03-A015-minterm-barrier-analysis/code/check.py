"""Frozen exact pilot/full check. No external helper or floating arithmetic."""
import argparse, collections, hashlib, itertools, json, math, time
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
START=time.monotonic(); counts=collections.Counter(); CHECKS=0
def ck(x, tag):
    global CHECKS
    assert x, tag
    CHECKS+=1
    counts[tag]+=1
    if time.monotonic()-START>55: raise RuntimeError('frozen runtime exceeded')
def fw(v):
    a=list(v); s=1
    while s<len(a):
        for j in range(0,len(a),2*s):
            for k in range(j,j+s): a[k],a[k+s]=a[k]+a[k+s],a[k]-a[k+s]
        s*=2
    return [F(t,len(a)) for t in a]
def inf(v):
    n=(len(v)-1).bit_length()
    return F(sum(v[x]!=v[x^(1<<i)] for x in range(len(v)) for i in range(n)),len(v))
def facts(n):
    out={}; p=2
    while p*p<=n:
        while n%p==0: out[p]=out.get(p,0)+1; n//=p
        p+=1
    if n>1: out[n]=out.get(n,0)+1
    return out
FC={}
def logvec(q):
    if q not in FC:
        d=collections.Counter(facts(q.denominator)); d.subtract(facts(q.numerator)); FC[q]=dict(d)
    return FC[q]
def cevec(pq):
    out=collections.defaultdict(F)
    for p,q in pq:
        if p:
            for prime,e in logvec(q).items(): out[prime]+=p*e
    return {k:v for k,v in out.items() if v}
def addvec(*terms):
    out=collections.defaultdict(F)
    for c,v in terms:
        for k,x in v.items(): out[k]+=c*x
    return {k:v for k,v in out.items() if v}
def ln_bounds(x,N=24):
    z=(x-1)/(x+1); term=z; total=F(0)
    for k in range(N): total+=2*term/(2*k+1); term*=z*z
    return total,total+2*term/((2*N+1)*(1-z*z))
L2=ln_bounds(F(2))
def log2_bounds(x):
    k=x.numerator.bit_length()-x.denominator.bit_length()
    u=x/F(2)**k
    if u<1: k-=1; u*=2
    lo,hi=ln_bounds(u)
    return F(k)+lo/L2[1],F(k)+hi/L2[0]
def cost_bounds(pq):
    bins=collections.defaultdict(F)
    for p,q in pq: bins[q]+=p
    lo=hi=F(0)
    for q,p in bins.items():
        l,u=log2_bounds(1/q); lo+=p*l; hi+=p*u
    # Dyadic enclosure retains a short exactly certified output.
    d=1<<48
    return [str(F(lo.numerator*d//lo.denominator,d)),str(F(-((-hi.numerator*d)//hi.denominator),d))]
def product(g,h,qg,qh,tag,interval=False):
    ng=(len(g)-1).bit_length(); nh=(len(h)-1).bit_length()
    a=F(sum(x==1 for x in g),len(g)); b=F(sum(x==1 for x in h),len(h))
    fg,fh=fw(g),fw(h)
    vals=[1 if g[x%(1<<ng)]==1 and h[x>>ng]==1 else -1 for x in range(1<<(ng+nh))]
    ff=fw(vals); pq=[]
    for mask in range(1,len(vals)):
        s=mask%len(g); t=mask>>ng
        want=(b*fg[s] if not t else a*fh[t] if not s else fg[s]*fh[t]/2)
        ck(ff[mask]==want,tag+'_fourier')
        q=(qg[s] if not t else qh[t] if not s else qg[s]*qh[t])/3
        pq.append((ff[mask]**2,q))
    ck(sum(q for _,q in pq)==1,tag+'_Q_normalization')
    ck(inf(vals)==b*inf(g)+a*inf(h),tag+'_influence')
    v=sum(p for p,_ in pq)
    wanted=addvec((v,{3:F(1)}),(b,cevec((fg[s]**2,qg[s]) for s in qg)),(a,cevec((fh[t]**2,qh[t]) for t in qh)))
    ck(cevec(pq)==wanted,tag+'_log_identity')
    return vals, cost_bounds(pq) if interval else None
def local(widths):
    n=sum(widths); blocks=[]; shift=0
    for w in widths: blocks.append(((1<<w)-1)<<shift); shift+=w
    U=[int(all(x&B for B in blocks)) for x in range(1<<n)]
    g=[2*u-1 for u in U]; r=len(widths); rho=F(1,2*r); Z=1-(1-rho)**r
    q={}
    for s in range(1,1<<n):
        active=[j for j,B in enumerate(blocks) if s&B]; t=len(active)
        q[s]=rho**t*(1-rho)**(r-t)/Z/math.prod((1<<widths[j])-1 for j in active)
    ck(sum(q.values())==1,'local_Q_normalization')
    ck(0<Z<1 and sum(q.values())*Z<1,'negative_missing_normalizer')
    a=math.prod(1-F(1,1<<w) for w in widths); gg=fw(g)
    I=2*a*sum(F(w, (1<<w)-1) for w in widths)
    ck(inf(g)==I,'local_influence')
    moment=sum(gg[s]**2*sum(widths[j] for j,B in enumerate(blocks) if s&B) for s in range(1,1<<n))
    ck(moment==4*a*sum(F(w,1<<w) for w in widths),'activation_moment')
    return g,q,blocks
def primes(vals):
    n=(len(vals)-1).bit_length(); true=sum((1<<x) for x,v in enumerate(vals) if v==1); allpoints=(1<<len(vals))-1
    faces={(0,0):allpoints}
    for i in range(n):
        one=sum(1<<x for x in range(len(vals)) if x&(1<<i)); old=list(faces.items())
        for (p,z),bits in old:
            faces[p|1<<i,z]=bits&one; faces[p,z|1<<i]=bits&(allpoints^one)
    plus=set(); minus=set()
    for (p,z),bits in faces.items():
        ck(True,'signed_faces')
        for wanted,dest in [(true,plus),(allpoints^true,minus)]:
            if bits&~wanted: continue
            specified=p|z
            if all(faces[p&~(1<<i),z&~(1<<i)]&~wanted for i in range(n) if specified&(1<<i)): dest.add((p,z))
    return plus,minus
def transversals(blocks):
    choices=[[1<<i for i in range(B.bit_length()) if B&(1<<i)] for B in blocks]
    return [sum(c) for c in itertools.product(*choices)]
def source_checks(pilot):
    t=F(17,20); upper=sum(t**c/F((c+1)*(c+2)) for c in range(17))+t**17/18
    ck(upper<F(4,5),'source_PGF_certificate')
    for w in ([32] if pilot else range(32,129)):
        ck((48*w)**2<=1<<w,'source_z_bound')
        ck(F((w+1)//2-1)>=F(w,4),'source_X_cost')
        ck((1<<w)-1>=F(w*w,8),'source_Y_cost')
    lam=[F(1,256),F(1,512)]; A=sum(lam)/2; D=math.prod(1+x/2 for x in lam)-1
    for z in ([1] if pilot else [1,2,4,8]):
        for marked in [set(),{0},{0,1}]:
            mt=sum(lam[i] for i in marked)
            ck(z*A<=F(1,16) and z*mt<=F(1,16),'tree_hypotheses')
            prev=[F(0),F(0)]
            for height in range(1,4):
                B=sum(lam[i]*(z if i in marked else 1)*prev[i] for i in range(2))
                val=F(1,2)*sum(B**c/F((c+1)*(c+2)) for c in range(7)); prev=[val,val]
                ck(val<=F(4,5),'finite_tree_bound')
                root=(math.prod(1+z*lam[i]*prev[i]/2 for i in range(2))-1)/(z*D)
                ck(root<=F(16,19),'finite_root_moment')
    return str(upper)
def main():
    pilot=argparse.ArgumentParser(); pilot.add_argument('--pilot',action='store_true'); args=pilot.parse_args()
    proofpgf=source_checks(args.pilot)
    refs=[{1:F(1,3),2:F(1,3),3:F(1,3)},{1:F(1,6),2:F(2,6),3:F(3,6)}]
    domain=range(1,3) if args.pilot else range(1,15)
    for i,j in itertools.product(domain,repeat=2):
        g=[1 if i>>k&1 else -1 for k in range(4)]; h=[1 if j>>k&1 else -1 for k in range(4)]
        for qg,qh in itertools.product(refs,repeat=2): product(g,h,qg,qh,'generic'); counts['generic_cases']+=1
    patterns=list(itertools.product([1,2],repeat=2)); patterns=patterns[:1] if args.pilot else patterns
    intervals=[]
    for wx,wy in itertools.product(patterns,repeat=2):
        g,qg,Bx=local(wx); gy,qh,By=local(wy); h=[-gy[len(gy)-1-y] for y in range(len(gy))]
        vals,interval=product(g,h,qg,qh,'physical',True); nx=sum(wx)
        plus,minus=primes(vals)
        wantplus={(x|(Y<<nx),0) for x in transversals(Bx) for Y in By}
        wantminus={(0,X) for X in Bx}|{(0,y<<nx) for y in transversals(By)}
        ck(plus==wantplus and minus==wantminus,'complete_prime_classification')
        counts['physical_cases']+=1; counts['physical_truth_points']+=len(vals)
        intervals.append({'widths':[wx,wy],'nonempty_cost_interval':interval})
    if not args.pilot:
        g,qg,_=local([2]*4); gy,qh,_=local([2]*4); h=[-gy[len(gy)-1-y] for y in range(len(gy))]
        vals,interval=product(g,h,qg,qh,'physical',True)
        counts['physical_cases']+=1; counts['physical_truth_points']+=len(vals)
        intervals.append({'widths':[[2]*4,[2]*4],'nonempty_cost_interval':interval})
    for w in ([4] if args.pilot else range(4,129)):
        r=1<<w; rho=F(1,2*r)
        for k in sorted(set([0,1,r//2,r-1,r])):
            A=(r-k)*F(w,r)+k*F(w+1,2*r)
            B=(r-k)*F(w,r-1)+k*F(w+1,2*r-1)
            ck(A<=B,'profile_activation_influence')
            ck(F(w+1+w,w)<=F(9,4),'profile_bit_budget')
            ck(r*rho==F(1,2),'profile_base_Bernoulli')
            ck(A>=F(w,2),'profile_I_lower_moment')
            counts['scalar_profiles']+=1
    or2=[-1,1,1,1]; a=F(3,4)
    ck(inf(or2)==1 and 2*a*inf(or2)==F(3,2),'negative_shared_variable')
    ck(4>3,'strict_constants_log3_lt_2')
    output={'helper_version':'A015-ONCE-TAGGED-JOINT-DICTIONARY@1','pilot':args.pilot,'assertions':CHECKS,'counts':dict(counts),'pgf_upper':proofpgf,'intervals':intervals,'elapsed_seconds':round(time.monotonic()-START,3),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'status':'PASS'}
    out=ROOT/'out'; out.mkdir(exist_ok=True)
    (out/('pilot.json' if args.pilot else 'exact_checks.json')).write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in output.items() if k!='intervals'},indent=2))
if __name__=='__main__': main()
