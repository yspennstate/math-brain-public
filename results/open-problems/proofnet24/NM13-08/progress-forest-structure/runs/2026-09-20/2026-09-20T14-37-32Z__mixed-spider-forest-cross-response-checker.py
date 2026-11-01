import json, hashlib
from pathlib import Path
import sympy as sp

# Exact verifier actually executed in the research run.
# The staged symbolic generator wrote cross_mixed_spider_certificate.json;
# this verifier checks its SHA-256, every stored shifted coefficient sign,
# and independently proves the generic five-state algebra / cross-gap identity.

def kappa(x,y):
    return sp.expand(sum(x)*sum(y)-sum(x[i]*y[i] for i in range(3)))

def Cmat(x,z):
    t=sum(x)
    return sp.Matrix([
        [1,x[0],x[1],x[2],z],
        [0,1,0,0,t-x[0]],
        [0,0,1,0,t-x[1]],
        [0,0,0,1,t-x[2]],
        [0,0,0,0,1],
    ])

x=sp.symbols("x0:3"); y=sp.symbols("y0:3")
dlt=sp.symbols("d0:3"); eps=sp.symbols("e0:3")
z,w,alpha,beta,u,v,h=sp.symbols("z w alpha beta u v h")

assert sp.simplify(
    Cmat(x,z)*Cmat(y,w)
    - Cmat(tuple(x[i]+y[i] for i in range(3)), z+w+kappa(x,y))
)==sp.zeros(5)

def H(x,z,y,w):
    return 1+sum(x)+sum(y)+z+w+kappa(x,y)

def S(x,y):
    return 4+2*(sum(x)+sum(y))

E=tuple(x[i]+dlt[i] for i in range(3))
F=tuple(y[i]+eps[i] for i in range(3))

def L(a,za,b,zb):
    return H(a,za,b,zb)+S(a,b)*u+6*v

Delta=sp.expand(
    L(E,z+alpha,y,w)*L(x,z,F,w+beta)
    - L(x,z,y,w)*L(E,z+alpha,F,w+beta)
)
dt=sum(dlt); et=sum(eps); kk=kappa(dlt,eps)
aa=dt+alpha+kappa(dlt,y)
bb=et+beta+kappa(x,eps)
H0=H(x,z,y,w); s0=S(x,y)
strip=sp.expand(Delta.subs(v,u*u/2-h*u))
expected=sp.expand(
    (4*dt*et-3*kk)*u*u
    +(2*aa*et+2*bb*dt-kk*(s0-6*h))*u
    +(aa*bb-H0*kk)
)
assert sp.expand(strip-expected)==0

# Exact coefficient certificate generated in four staged SymPy batches.
# The certificate itself was a transient run artifact; its digest pins the
# exact bytes used for the executed sign verification below.
P=Path(__file__).with_name("cross_mixed_spider_certificate.json")
raw=P.read_text()
D=json.loads(raw)
assert hashlib.sha256(raw.encode()).hexdigest()=="8d698ab33fa8c259dc545089080b8253f78fe5221bbd1bf5f0ddd56d63d79f0b"
assert len(D)==38
mins={k:None for k in ("k","L2","L1lo","C")}
maxterms={k:0 for k in mins}
for scheme,rec in D.items():
    assert set(rec)==set(mins)
    for lab,polys in rec.items():
        nc=list(polys["num"].values())
        dc=list(polys["den"].values())
        assert nc and dc and all(c>0 for c in nc) and all(c>0 for c in dc)
        maxterms[lab]=max(maxterms[lab],len(nc))
        m=min(nc)
        if mins[lab] is None or m<mins[lab][0]:
            mins[lab]=(m,scheme)

print("NM13-08 T07 CROSS-MIXED-SPIDER EXACT CERTIFICATE")
print("generic_one_edge_algebra_closure=PASS")
print("generic_cross_component_strip_formula=PASS")
print("certificate_sha256=8d698ab33fa8c259dc545089080b8253f78fe5221bbd1bf5f0ddd56d63d79f0b")
print("schemes=38")
for lab in ("k","L2","L1lo","C"):
    print(lab,"min_num_coeff",mins[lab][0],"scheme",mins[lab][1],"max_terms",maxterms[lab])
print("all stored numerator and denominator coefficients are strict positive integers")
print("ALL_EXACT_CHECKS_PASS")
