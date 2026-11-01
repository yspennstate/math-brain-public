"""A052 v1: exact spectra and natural-unit prime-log certificates."""
import argparse, itertools, json, math, time
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
COUNT=0
def check(ok):
    global COUNT
    COUNT+=1
    if not ok: raise AssertionError(COUNT)

def fwht(v):
    v=list(v); h=1
    while h<len(v):
        for j in range(0,len(v),2*h):
            for k in range(j,j+h):
                a,b=v[k],v[k+h]; v[k],v[k+h]=a+b,a-b
        h*=2
    return v

def direct(v):
    return [sum(a*(-1 if (x&s).bit_count()%2 else 1) for x,a in enumerate(v)) for s in range(len(v))]

@lru_cache(None)
def factors(n):
    out={}; p=2
    while p*p<=n:
        while n%p==0: out[p]=out.get(p,0)+1; n//=p
        p+=1
    if n>1: out[n]=out.get(n,0)+1
    return out

def add(a,b,c=Q(1)):
    out=dict(a)
    for p,x in b.items():
        out[p]=out.get(p,Q(0))+c*x
        if not out[p]: del out[p]
    return out

def scale(a,c): return {p:x*c for p,x in a.items() if x*c}

def entropy(ps):
    out={}
    for z in ps:
        if z:
            for p,k in factors(z.numerator).items(): out[p]=out.get(p,Q(0))-z*k
            for p,k in factors(z.denominator).items(): out[p]=out.get(p,Q(0))+z*k
    return {p:x for p,x in out.items() if x}

def atanh_ln(z):
    cur=z; lo=Q(0); terms=24
    for j in range(terms): lo+=2*cur/(2*j+1); cur*=z*z
    return lo,lo+2*cur/((2*terms+1)*(1-z*z))

@lru_cache(None)
def ln_bound(p):
    k=p.bit_length()-1; unit=1<<k
    a,b=atanh_ln(Q(1,3)); c,d=atanh_ln(Q(p-unit,p+unit))
    return k*a+c,k*b+d

def interval(a):
    lo=hi=Q(0)
    for p,c in a.items():
        l,h=ln_bound(p)
        lo+=c*(l if c>=0 else h); hi+=c*(h if c>=0 else l)
    return lo,hi

def nonnegative(a,constant=Q(0)):
    if not a: return constant>=0
    lo,hi=interval(a)
    if lo+constant>=0: return True
    if hi+constant<0: return False
    raise RuntimeError('unresolved rational interval')

def pspec(v):
    N=len(v); w=fwht(v)
    return [Q(x*x,N*N) for x in w]

def energy(p): return sum((s.bit_count()*z for s,z in enumerate(p)),Q(0))

def edges(v):
    N=len(v); n=N.bit_length()-1
    return Q(sum((v[x]-v[x^(1<<i)])**2 for x in range(N) for i in range(n)),4*N)

def positions(mask,n): return [i for i in range(n) if mask>>i&1]
def pack(s,loc): return sum(((s>>i)&1)<<j for j,i in enumerate(loc))
def unpack(s,loc): return sum(((s>>j)&1)<<i for j,i in enumerate(loc))

def restricted(v,A,x):
    n=len(v).bit_length()-1; ai=positions(A,n); ci=positions(((1<<n)-1)^A,n)
    return [v[unpack(x,ai)|unpack(y,ci)] for y in range(1<<len(ci))]

def small(nmax):
    tables=cases=critical=0
    for n in range(nmax+1):
        N=1<<n
        for truth in range(1<<N):
            v=[1 if truth>>x&1 else -1 for x in range(N)]
            w=fwht(v); check(w==direct(v)); p=pspec(v); H=entropy(p); I=energy(p)
            check(sum(p)==1); check(I==edges(v)); tables+=1
            descendants=[]
            blocks=[]
            for A in range(1,N):
                ai=positions(A,n); ci=positions((N-1)^A,n); r=len(ai); c=len(ci)
                childp=[pspec(restricted(v,A,x)) for x in range(1<<r)]
                marginal=[sum((p[s] for s in range(N) if pack(s,ci)==t),Q(0)) for t in range(1<<c)]
                for t in range(1<<c): check(marginal[t]==sum(z[t] for z in childp)/(1<<r))
                avgH={}
                for cp in childp:
                    avgH=add(avgH,entropy(cp),Q(1,1<<r)); descendants.append((entropy(cp),energy(cp)))
                marginalH=entropy(marginal); J=add(marginalH,avgH,-1); B=add(H,marginalH,-1)
                IA=sum((p[s]*pack(s,ai).bit_count() for s in range(N)),Q(0))
                check(I==IA+sum(energy(z) for z in childp)/(1<<r))
                blocks.append((A,ai,ci,r,c,IA,B,J))
            iscrit=bool(I and H) and all(nonnegative(add(scale(H,ic),scale(hc,I),-1)) for hc,ic in descendants)
            if iscrit: critical+=1
            for A,ai,ci,r,c,IA,B,J in blocks:
                # Systematic rows: Y=S_A+L*S_C. All possible L; row operations cover all invertible V_A.
                for L in itertools.product(range(1<<c),repeat=r):
                    synd=[pack(s,ai)^sum(((pack(s,ci)&row).bit_count()%2)<<j for j,row in enumerate(L)) for s in range(N)]
                    yp=[sum((p[s] for s in range(N) if synd[s]==y),Q(0)) for y in range(1<<r)]
                    joint=[sum((p[s] for s in range(N) if synd[s]==y and pack(s,ci)==t),Q(0)) for t in range(1<<c) for y in range(1<<r)]
                    check(add(entropy(joint),marginal_entropy(p,ci),-1)==B)
                    check(nonnegative(add(entropy(yp),B,-1)))
                    for y0 in range(1<<r):
                        b=sum((p[s]*(synd[s]^y0).bit_count() for s in range(N)),Q(0))
                        eps=1-yp[y0]
                        check(b<=r*eps); check(nonnegative(scale(J,-1),2*b))
                        if iscrit:
                            # natural-unit form: R_nat I_A <= B_nat + 2b
                            check(nonnegative(add(scale(B,I),scale(H,IA),-1),2*b*I))
                        cases+=1
    return {'truth_tables':tables,'syndrome_cases':cases,'restriction_ratio_critical_positive_entropy_tables':critical}

def marginal_entropy(p,loc):
    return entropy([sum((p[s] for s in range(len(p)) if pack(s,loc)==t),Q(0)) for t in range(1<<len(loc))])

def comps(points,n):
    rest=set(points); out=[]
    while rest:
        todo=[rest.pop()]; comp=set(todo)
        while todo:
            x=todo.pop()
            for i in range(n):
                y=x^(1<<i)
                if y in rest: rest.remove(y); comp.add(y); todo.append(y)
        out.append(comp)
    return out

def pruning(d,c):
    n=d+c; N=1<<n
    A={x for x in range(N) if (x&((1<<d)-1)).bit_count()<=1}; B={(1<<d)-1}; G=A|B
    check(sorted(map(len,comps(G,n)))==[1,len(A)])
    vals=[[int(x in Z) for x in range(N)] for Z in (A,B,G)]
    allp=[pspec(v) for v in vals]; hs=[entropy(p) for p in allp]; es=[energy(p) for p in allp]
    for v,p in zip(vals,allp): check(fwht(v)==direct(v)); check(energy(p)==edges(v))
    check(es[0]+es[1]==es[2]); excess=add(add(hs[2],hs[0],-1),hs[1],-1)
    check(nonnegative(excess)); elo,ehi=interval(excess)
    child=[int(x.bit_count()<=1) for x in range(4)]; hc=entropy(pspec(child)); ec=energy(pspec(child))
    # Fix d-2 data bits to zero; controls remain irrelevant; source orientation retained.
    check(all(vals[2][unpack(x,[0,1])+unpack(z,list(range(d,n)))]==child[x] for x in range(4) for z in range(1<<c)))
    gap=add(scale(hc,es[2]),scale(hs[2],ec),-1); check(nonnegative(gap))
    if d==4:
        check(es==[Q(3,8),Q(7,256),Q(103,256)])
        check(3**45*5**25>2**128)
        check(2**23552>3**1620*23**2645*41**1681)
        check(nonnegative(add(scale(hs[2],es[1]),scale(hs[1],es[2]),-1)))
    else:
        check(es==[Q(5,16),Q(9,1024),Q(329,1024)])
        check(nonnegative(excess,Q(-1,5000)))
        check(nonnegative(add(scale(hs[1],es[2]),scale(hs[2],es[1]),-1)))
    ratios=[]
    for h,e in zip(hs,es):
        l,u=interval(h); ratios.append([str(l/e),str(u/e)])
    l,u=interval(gap); descgap=[str(l/(ec*es[2])),str(u/(ec*es[2]))]
    # Raw indicator quantities cannot be silently substituted for sign H/I.
    signv=[1-2*a for a in vals[2]]; sp=pspec(signv)
    return {'data':d,'controls':c,'component_sizes':[len(A),1],'energy':[str(e) for e in es],
            'raw_ratios_ln_intervals':ratios,'raw_entropy_excess_interval':[str(elo),str(ehi)],
            'proper_raw_descendant_ratio_gap_interval':descgap,
            'sign_influence':str(energy(sp)), 'sign_entropy_ln_vector':{str(p):str(z) for p,z in entropy(sp).items()}}

def activations():
    out=[]
    for k in (1,2):
        n=2*k+1
        core=[]
        for x in range(1<<n):
            h=math.prod(-1 if ((x>>(2*j))&3)==3 else 1 for j in range(k))
            core.append((-1 if x>>(2*k)&1 else 1)*h)
        check(energy(pspec(core))==k+1); check(entropy(pspec(core))=={2:Q(2*k)})
        for r in (1,2,3):
            # all controls zero activates core
            v=[core[x&((1<<n)-1)] if x>>n==0 else 1 for x in range(1<<(n+r))]
            p=pspec(v); a=Q(1,1<<r)
            check(energy(p)==a*(k+1+r))
            expected=add({2:a*2*k+2*r*a*(2-a)},entropy([(1-a)**2]))
            check(entropy(p)==expected)
            # After activation, fixing balance z gives the original tensor core, a smaller physical descendant.
            derived=[v[x] for x in range(1<<(2*k))]
            check(energy(pspec(derived))==k); check(entropy(pspec(derived))=={2:Q(2*k)})
            out.append({'tensor_copies':k,'controls':r,'I':str(energy(p)),'smaller_descendant_ratio_bits':'2'})
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pilot',action='store_true'); args=ap.parse_args()
    start=time.monotonic(); result={'helper_version':'A052-affine-disorder-v1','pilot':args.pilot}
    result['small']=small(2 if args.pilot else 3)
    result['pruning']=[pruning(4,3),pruning(5,4)]
    if not args.pilot: result['activations']=activations()
    result.update(assertions=COUNT,runtime_seconds=time.monotonic()-start,status='PASS')
    filename='PILOT_OUTPUT.json' if args.pilot else 'CHECK_OUTPUT.json'
    (ROOT/'out'/filename).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('pruning','activations')}))

if __name__=='__main__': main()
