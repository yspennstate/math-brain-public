import itertools, math, json
import numpy as np

TOL = 2e-10

def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p*math.log2(p) - (1-p)*math.log2(1-p)

def phi(x,y):
    if x == 0.0 and y == 0.0:
        return 0.0
    s = x*x+y*y
    p = (x-y)*(x-y)/(2*s)
    return 0.5*s*h2(p)

def fwht(a):
    a = np.asarray(a, dtype=float).copy()
    n = len(a); h=1
    while h<n:
        for i in range(0,n,2*h):
            x=a[i:i+h].copy(); y=a[i+h:i+2*h].copy()
            a[i:i+h]=x+y; a[i+h:i+2*h]=x-y
        h*=2
    return a/n

def one_exception_reps(hat):
    mags=np.abs(hat)
    reps=[]
    N=len(hat)
    for e in range(N):
        vals=[round(float(mags[t]),12) for t in range(N) if t!=e and mags[t]>1e-11]
        if not vals:
            reps.append((e,None))
        else:
            a=vals[0]
            if all(abs(v-a)<1e-10 for v in vals):
                reps.append((e,a))
    return reps

def split_metrics(ghat,hhat):
    x=np.abs(ghat); y=np.abs(hhat)
    B=sum(phi(float(a),float(b)) for a,b in zip(x,y))
    P=x*x; Q=y*y
    TV=0.5*float(np.abs(P-Q).sum())
    M=0.25*float(((x-y)**2).sum())
    inner=float(np.dot(ghat,hhat))
    inf=0.5*(1-inner)
    j=min(inf,1-inf)
    return B,TV,M,j,inf

scalar_checks=0
scalar_viol=0
# Tail inequality: if ratio >=2 (or one zero), Phi <= 5/4 (x-y)^2.
grid=[0.0]+[2.0**(-k) for k in range(0,15)]
for x in grid:
    for y in grid:
        if x==y: continue
        if x==0 or y==0 or max(x,y)/min(x,y)>=2-1e-15:
            scalar_checks += 1
            if phi(x,y) > 1.25*(x-y)**2 + 1e-12:
                scalar_viol += 1

# Exceptional scalar two-case bounds sampled densely in p.
exc_checks=0
exc_viol=0
for p in np.linspace(1e-10,0.5,200001):
    exc_checks += 1
    hp=h2(float(p))
    if p < 1/64:
        if hp > math.sqrt(p*(1-p)) + 1e-12:
            exc_viol += 1
    else:
        if hp > 7.5*p + 1e-12:
            exc_viol += 1

# Exhaustive Boolean child pairs through residual dimension 3 modulo global sign.
pair_cases=0
unequal_cases=0
same_cases=0
max_ratio8=0.0
max_ratio4=0.0
max_tv_ratio=0.0
pair_viol=0

for d in range(0,4):
    N=1<<d
    funcs=[]
    # modulo global sign: first truth-table value fixed +1
    for mask in range(1<<(N-1)):
        vals=np.ones(N)
        for j in range(1,N):
            if (mask>>(j-1))&1:
                vals[j]=-1
        hat=fwht(vals)
        funcs.append((vals,hat,one_exception_reps(hat)))
    for valsg,ghat,repg in funcs:
        for valsh,hhat,reph in funcs:
            common=[]
            for e,a in repg:
                for ee,b in reph:
                    if e==ee:
                        common.append((e,a,b))
            if not common: continue
            B,TV,M,j,inf=split_metrics(ghat,hhat)
            # certify if any common-exception representation has equal or binary-separated tails
            cert8=False; cert4=False
            for e,a,b in common:
                if a is None or b is None:
                    cert8=True
                elif abs(a-b)<1e-10:
                    cert4=True; cert8=True
                else:
                    r=max(a,b)/min(a,b)
                    if r>=2-1e-9:
                        cert8=True
            if cert8:
                pair_cases += 1
                if M>1e-14:
                    max_ratio8=max(max_ratio8,B/M)
                    max_tv_ratio=max(max_tv_ratio,TV/M)
                if B > 8*M + 2e-10 or M > j + 2e-10:
                    pair_viol += 1
            if cert4:
                same_cases += 1
                if M>1e-14:
                    max_ratio4=max(max_ratio4,B/M)
                if B > 4*M + 2e-10:
                    pair_viol += 1
            if cert8 and not cert4:
                unequal_cases += 1

# GF(2^r) multiplication for small checks.
PRIM = {1:0b11, 2:0b111, 3:0b1011, 4:0b10011}
def gf_mul(a,b,r):
    mod=PRIM[r]
    out=0
    aa=a; bb=b
    while bb:
        if bb&1: out ^= aa
        bb >>= 1
        aa <<= 1
        if aa & (1<<r):
            aa ^= mod
    return out & ((1<<r)-1)

def graph_truth(r, ambient=None):
    # full graph if ambient=r; lifted quotient graph if ambient>r using low r bits.
    if ambient is None: ambient=r
    N=1<<(3*ambient)
    vals=np.empty(N)
    mask=(1<<r)-1
    for idx in range(N):
        x=idx & ((1<<ambient)-1)
        z=(idx>>ambient) & ((1<<ambient)-1)
        y=(idx>>(2*ambient)) & ((1<<ambient)-1)
        xr=x&mask; zr=z&mask; yr=y&mask
        vals[idx] = -1.0 if yr==gf_mul(xr,zr,r) else 1.0
    return vals

def influence_from_truth(vals,d):
    N=len(vals)
    s=0.0
    for i in range(d):
        diff=0
        bit=1<<i
        for x in range(N):
            if vals[x]!=vals[x^bit]:
                diff+=1
        s += diff/N
    return s

graph_cases=[]
graph_viol=0
for m,n in [(1,2),(1,3),(2,3),(2,4),(3,4)]:
    g=graph_truth(m,n)
    h=graph_truth(n,n)
    gh=fwht(g); hh=fwht(h)
    # tail structure
    ax=sorted(set(round(abs(v),12) for v in gh[1:] if abs(v)>1e-10))
    ay=sorted(set(round(abs(v),12) for v in hh[1:] if abs(v)>1e-10))
    expected_a=2**(1-2*m); expected_b=2**(1-2*n)
    B,TV,M,j,inf=split_metrics(gh,hh)
    Hg=sum((v*v)*math.log2(1/(v*v)) for v in gh if abs(v)>1e-15)
    Hh=sum((v*v)*math.log2(1/(v*v)) for v in hh if abs(v)>1e-15)
    Ig=influence_from_truth(g,3*n)
    Ih=influence_from_truth(h,3*n)
    # support nesting away from zero
    suppg={i for i,v in enumerate(gh) if i!=0 and abs(v)>1e-10}
    supph={i for i,v in enumerate(hh) if i!=0 and abs(v)>1e-10}
    nested=suppg.issubset(supph)
    # selector parent spectrum
    parent_hat=np.empty(2*len(gh))
    # index convention: lower residual labels, selector bit is high bit.
    parent_hat[:len(gh)]=(gh+hh)/2
    parent_hat[len(gh):]=(gh-hh)/2
    unit=2**(-2*n)
    R=sum(1 for v in parent_hat if abs(v)>unit+1e-10)
    lower_R=2*(2**(2*m))*(2**m-1)
    ok=(len(ax)<=1 and len(ay)<=1 and
        (not ax or abs(ax[0]-expected_a)<1e-9) and
        (not ay or abs(ay[0]-expected_b)<1e-9) and
        nested and B<=8*M+2e-10 and M<=j+2e-10 and
        Hg<= (8/3)*Ig+2e-9 and Hh<= (8/3)*Ih+2e-9 and
        R>=lower_R)
    if not ok: graph_viol+=1
    graph_cases.append({
        "m":m,"n":n,"B_over_j": (B/j if j>0 else 0),
        "B_over_M": (B/M if M>0 else 0),
        "tail_ratio": expected_a/expected_b,
        "Hg_over_Ig": Hg/Ig if Ig else 0,
        "Hh_over_Ih": Hh/Ih if Ih else 0,
        "parent_exceptional_R":R,
        "lower_R":lower_R,
        "nested_support":nested
    })

out={
    "status":"PASS" if scalar_viol==0 and exc_viol==0 and pair_viol==0 and graph_viol==0 else "FAIL",
    "tail_scalar_checks":scalar_checks,
    "tail_scalar_violations":scalar_viol,
    "exception_scalar_grid_checks":exc_checks,
    "exception_scalar_violations":exc_viol,
    "exhaustive_certified_pair_cases_d_le_3":pair_cases,
    "unequal_or_character_certified_cases":unequal_cases,
    "same_tail_certified_cases":same_cases,
    "pair_violations":pair_viol,
    "max_B_over_M_certified8":max_ratio8,
    "max_B_over_M_same_tail":max_ratio4,
    "max_TV_over_M_certified8":max_tv_ratio,
    "graph_cases":graph_cases,
    "graph_violations":graph_viol
}
print(json.dumps(out,indent=2,sort_keys=True))
