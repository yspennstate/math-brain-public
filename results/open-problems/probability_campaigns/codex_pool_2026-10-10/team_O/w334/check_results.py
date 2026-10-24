"""Independent exact arithmetic and finite boundary checks for campaign proofs."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import acos, acosh, comb, factorial, log, pi, sin, sqrt
from pathlib import Path
import json
import random
import time

HERE = Path(__file__).resolve().parent
started = time.monotonic()
rows = []

def save(problem, name, values):
    rows.append({"problem_id": problem, "check": name, "values": values})
    (HERE / "experiments.json").write_text(json.dumps({"command": "python -B -X utf8 check_results.py", "checks": rows}, indent=2), encoding="utf-8")

def fkernel(C, y, c):
    return (C*y-c)/(2*(y*y-2*c*C*y+c*c+C*C-1))

cases = []
for C in [F(201,100), F(21,10), F(5,2), F(3), F(101,20)]:
    m, M = 1/(2*(C+1)), C*C/(8*(C*C-1))
    assert M-m == (C-2)**2/(8*(C*C-1))
    h = (m+M)/2
    q = C-1/(2*h)
    c0 = min(F(0), (q-1)/2)
    ystar = C-2/C
    assert -1 < c0 <= 0 and c0 < q and ystar > 1
    for c in [c0, (c0-1)/2, (c0-3)/4]:
        assert fkernel(C, F(1), c) < h < M <= fkernel(C, ystar, c)
        # These signs certify two distinct roots above y=1 for the quadratic;
        # each yields two distinct u-roots. No numerical root grid is used.
        poly1 = 2*h*(1-2*c*C+c*c+C*C-1)-C+c
        polystar = 2*h*(ystar**2-2*c*C*ystar+c*c+C*C-1)-C*ystar+c
        assert poly1 > 0 and polystar < 0
    R0 = acos(float(c0))
    cases.append({"C": str(C), "a": acosh(float(C)), "h": str(h), "c0": str(c0), "T": R0/(float(h)*sin(R0)), "crossings": 4})
assert F(2)**2/(8*(F(2)**2-1)) == 1/(2*(F(2)+1))
assert 1/(2*F(101,20)) < F(1,10) < F(1,8)
save("P0193", "exact uniform witnesses and C=2 boundary", {"parameter_cases": cases, "old_a": log(10), "new_sufficient_a": acosh(2), "old_example_T": 5*pi})

N = 8
def mul(a,b):
    return [sum((a[k]*b[j-k] for k in range(j+1)), F(0)) for j in range(N+1)]
def reciprocal(a):
    b=[F(1)/a[0]]+[F(0)]*N
    for j in range(1,N+1):
        b[j]=-sum((a[k]*b[j-k] for k in range(1,j+1)),F(0))/a[0]
    return b
cosh=[F(1,factorial(j)) if j%2==0 else F(0) for j in range(N+1)]
sinh=[F(1,factorial(j)) if j%2 else F(0) for j in range(N+1)]
eminus=[F((-1)**j,factorial(j)) for j in range(N+1)]
sech=reciprocal(cosh)
S=[F(0)]+[sech[j-1]/j for j in range(1,N+1)]
cosh2=mul(cosh,cosh)
alpha=mul(eminus,cosh2)
inner=[a+b for a,b in zip(mul(cosh2,S),sinh)]
beta=[2*x for x in mul(eminus,inner)]
assert alpha[6] == F(61,240) and beta[6] == F(-4,5)
assert alpha[6]+beta[6]*F(7,22) == F(-1,2640)

def beta_integer(a,b):
    return F(factorial(a-1)*factorial(b-1),factorial(a+b-1))
def choose(n,k):
    return comb(n,k) if 0<=k<=n else 0
poly_cases=[]
for m in range(1,13):
    closed=[]
    for k in range(m+1):
        val=choose(m-1,k)*(beta_integer(2*m+k,m)-beta_integer(2*m+k+1,m)/2)+choose(m-1,k-1)*beta_integer(2*m+k,m)/2
        closed.append(2*val/beta_integer(m,m))
    # Independently expand the radial integrand as powers of w and q,
    # then integrate w^(power-4m) from 1 to infinity term by term.
    raw=[F(0)]*(m+1)
    for i in range(m):
        left=F(comb(m-1,i)*(-1)**(m-1-i))
        for j in range(m):
            coeff=left*comb(m-1,j)
            power=i+(m-1-j)
            raw[j]+=coeff*(F(1,4*m-power-2)-F(1,2*(4*m-power-1)))
            raw[j+1]+=coeff*F(1,2*(4*m-power-1))
    normalized=[x/sum(raw) for x in raw]
    assert normalized == closed and sum(closed)==1 and all(x>0 for x in closed)
    poly_cases.append({"m":m,"coefficients":[str(x) for x in closed]})
assert poly_cases[0]["coefficients"] == ["2/3","1/3"]
save("P0411", "independent series and radial polynomial calculations", {"sixth_alpha":str(alpha[6]), "sixth_beta_over_pi":str(beta[6]), "negative_upper_bound":str(F(-1,2640)), "polynomials":poly_cases})

network=[]
for M in [F(10),F(100),F(1000),F(1000000)]:
    # Direct solution of t0=1+t1/2 and t1=1+t0/(M+1).
    t0=(F(1)+F(1,2))/(1-F(1,2*(M+1)))
    reff=(M+1)/(2*M+1)
    assert t0==3*reff
    network.append({"M":str(M),"expected_exit":str(t0),"ratio_to_resistance_times_volume":str(t0/(reff*(M+3)))})
tails=[]
for L in [10,100,1000]:
    expectation=F(L-1,L)+F(L**3,L)
    assert 1<expectation/2<L**3
    tails.append({"L":L,"mean":str(expectation),"probability_above_half_mean":str(F(1,L))})
save("C0012", "killed-chain equations and wrong-tail counterexample", {"networks":network,"tail_examples":tails})

cover=[]
for p in [F(1,10),F(1,4),F(1,2),F(3,4),F(9,10)]:
    q=1-p
    optimum=(p*p+q*q)/min(p,q)
    for j in range(1,21):
        k=min(p,q)*F(j,20)
        a,b=k/p,k/q
        direct=p/a+q/b
        assert direct==(p*p+q*q)/k and direct>=optimum
    cover.append({"p":str(p),"minimum":str(optimum)})
save("P0245", "fixed stationary law feasible transition grid", {"laws":cover,"feasible_chains":100})

lo=[]
for n in [2,4,6,8,10]:
    counts=Counter(sum(signs)**2 for signs in product([-1,1],repeat=n))
    assert counts[0]==comb(n,n//2)
    assert max(counts.values())<=2*comb(n,n//2)
    # An arbitrary nonsymmetric matrix with every entry nonzero is degenerate.
    for signs in product([-1,1],repeat=n):
        value=sum((1 if i<=j else -1)*signs[i]*signs[j] for i in range(n) for j in range(n))
        assert value==n
    lo.append({"n":n,"rank_one_max_atom":str(F(max(counts.values()),2**n)),"rank_one_zero_atom":str(F(counts[0],2**n)),"skew_cancellation_atom":1})
save("C0108", "exhaustive sign vectors and nonsymmetric degeneracy", {"cases":lo})

def spread(values):
    return sum((a-b)**2 for i,a in enumerate(values) for b in values[i+1:])
survivors=[F(3,4),F(1,100),F(1,100)]
before=spread([F(0)]+survivors)
deltas=[spread([clone]+survivors)-before for clone in survivors]
direct=sum(deltas)/3
formula=sum(x*x for x in survivors)-F(2,3)*sum(survivors)**2
assert direct==formula==F(5023,30000)>0
save("P0026", "enumerated rebirth choices", {"survivors":[str(x) for x in survivors],"clone_deltas":[str(x) for x in deltas],"mean_delta":str(direct)})

boundary=[]
for d in [2,3,7]:
    for n in [8,16,32,64]:
        size=n**d-(n-2)**d
        boundary.append({"d":d,"n":n,"p":0,"normalized_boundary":float(F(size,n**(d-1))),"predicted_limit":2*d})
save("C0072", "p=0 exact boundary control", {"cases":boundary,"scope":"Tests geometry and normalization only; the probabilistic proof requires a blind audit."})

rng=random.Random(334)
violations=0
for _ in range(20000):
    x,y=rng.expovariate(1),rng.expovariate(1)
    violations+= y>2*x+2
save("C0155", "finite index-gap failure illustration", {"seed":334,"gap_pairs":20000,"violations_A2_B2":violations,"scope":"Numerical illustration; the all-shift almost-sure statement is proved by Borel-Cantelli."})

def kruskal(vertices,edges):
    parents={x:x for x in vertices}
    def root(x):
        while parents[x]!=x:
            x=parents[x]
        return x
    chosen=[]
    for weight,a,b in sorted(edges):
        ra,rb=root(a),root(b)
        if ra!=rb:
            parents[ra]=rb
            chosen.append((weight,a,b))
    return chosen
ladder=[]
for Ncols in [2,3,5,10,20]:
    vertices=[(side,i) for side in [0,1] for i in range(1,Ncols+1)]
    edges=[(F(1,2),(side,i),(side,i+1)) for side in [0,1] for i in range(1,Ncols)]
    edges += [(1+F(1,i),(0,i),(1,i)) for i in range(1,Ncols+1)]
    mst=kruskal(vertices,edges)
    rungs=[a[1] for weight,a,b in mst if a[0]!=b[0]]
    assert rungs==[Ncols] and len(mst)==2*Ncols-1
    ladder.append({"columns":Ncols,"selected_rungs":rungs})
save("C0113", "finite ladder MSTs", {"cases":ladder,"scope":"This is not a Poisson process counterexample."})
save("P0039", "quantitative exponents", {"alpha_and_distance_exponent":[{"alpha":a,"exponent":1/(2-a)} for a in [.25,.5,.75]],"scope":"Algebraic consequence; no random-walk simulation proves the theorem."})

receipt={"command":"python -B -X utf8 check_results.py","seconds":round(time.monotonic()-started,3),"passed_check_groups":len(rows),"problem_ids":sorted({r['problem_id'] for r in rows}),"checks":rows,"all_mathematical_claims_independently_audited":False}
(HERE / "experiments.json").write_text(json.dumps(receipt,indent=2),encoding="utf-8")
print(json.dumps({k:v for k,v in receipt.items() if k!='checks'},indent=2))
