"""Independent FLINT reconstruction of the displayed K_n barrier algebra."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os
os.environ.setdefault("OMP_NUM_THREADS","1")
os.environ.setdefault("OPENBLAS_NUM_THREADS","1")
import psutil
ROOT=Path(__file__).resolve().parent
OUT=ROOT/"output";OUT.mkdir(parents=True,exist_ok=True)
free=psutil.virtual_memory().available
assert free>=2*1024**3,"HOLD: less than 2 GB available; do not start certificate"
from flint import fmpz_mpoly_ctx, fmpz_poly
ctx=fmpz_mpoly_ctx.get(("n","t","r","c","u","x"),"lex")
n,t,r,c,u,x=ctx.gens()
h=(n-2)*(n-3);delta=t*h
a=t-2*(n-4)*t*t
b=-1+(2*n-9)*t+n*(n-4)*t*t
F=delta*r*r-b*r-a
B=-1+(2*n+1)*t+n*n*t*t
phi=t-2*n*t*t+B*r-n*(n-1)*t*r*r
# Derivatives are taken from the displayed definitions, not imported JSON.
Ft=h*r*r-((2*n-9)+2*n*(n-4)*t)*r-1+4*(n-4)*t
Fr=2*delta*r-b
G=2*t*t*Ft+Fr*phi
L=n**3*(n-4)*t**4+2*n*(n*n-4*n-6)*t**3+3*(n*n-9*n+3)*t*t+2*(n*n-9*n+9)*t-(2*n-3)
C=2*n*n*(n-4)*t**3+3*n*(n-6)*t*t+(2*n*n-16*n+15)*t-(2*n-3)
quot=-2*h*n*(n-1)*t*r+2*h*t+2*h*B-n*(n-1)*b
assert h*G-F*quot-2*(L*r-t*C)==0,"boundary remainder"
A=n*(n-4)
J=2*A*A*t**3-6*A*(n-2)*t*t+6*(n-1)*(n-3)*t-(2*n-3)
assert delta*t*t*C*C-b*t*L*C-a*L*L+h*h*t**5*J==0,"root-product identity"
assert (6*A*A*t*t-12*A*(n-2)*t+6*(n-1)*(n-3))-6*((A*t-(n-2))**2-1)==0,"cubic derivative"
jcoef=[-(2*n-3),6*(n-1)*(n-3),-6*A*(n-2),2*A*A]
eval1=sum(jcoef[k]*(n-3)**k*A**(3-k) for k in range(4))
eval2=sum(jcoef[k]*(n-1)**k*A**(3-k) for k in range(4))
assert (n-4)*eval1+(n-6)*A**3==0,"local maximum"
assert n*eval2+(n-2)*A**3==0,"local minimum"

def dcoef(v):
    return [v*0+1,18-4*v,6*v*v-48*v+105,-4*v**3+38*v*v-136*v+192,v*v*(v-4)**2]
disc=b*b+4*delta*a
assert disc==sum(v*t**k for k,v in enumerate(dcoef(n)))
dc=dcoef(c+3)
lower=sum(dc[k]*c**(4-k)*u**k*(1+u)**(4-k) for k in range(5))
upper=sum(dc[k]*c**(4-k)*(1+u)**k for k in range(5))
lc=[c**4,6*c**3,c*c*(6*c+15),-2*c*(c+1)*(2*c-9),-3*(c-3)*(c+1)]
uc=[-3*(c-3)*(c+1),2*(2*c**3-13*c*c+3*c+18),9*(2*c**3-5*c*c-2*c+6),6*(c-1)*(3*c*c-c-6),(c+3)**2*(c-1)**2]
assert lower==sum(v*u**k for k,v in enumerate(lc)),"lower discriminant map"
assert upper==sum(v*u**k for k,v in enumerate(uc)),"upper discriminant map"
assert 2*(x+4)**3-5*(x+4)**2-2*(x+4)+6==2*x**3+19*x*x+54*x+46
assert 3*(x+4)**2-(x+4)-6==3*x*x+23*x+38

tt=fmpz_poly([0,1])
base=[]
expected={4:[2,4],5:[2,24,84,100],6:[2,48,462,2172,5184,5184]}
for nv in [4,5,6]:
    rr=[fmpz_poly([1]),1+nv*tt]
    for k in range(2,nv):rr.append((1+nv*tt)*rr[-1]-(k-1)*tt*rr[-2])
    zz=rr[nv-1]-(nv-1)*tt*rr[nv-2]
    ee=tt*rr[nv-2]-(nv-2)*tt**2*rr[nv-3]
    dd=tt**2*rr[nv-3]-(nv-4)*tt**3*rr[nv-4]
    gap=ee*ee-zz*dd
    wanted=tt**4*fmpz_poly(expected[nv])
    assert gap==wanted,(nv,"base numerator")
    base.append({"n":nv,"Z":[int(q) for q in zz],"E":[int(q) for q in ee],"D":[int(q) for q in dd],"gap_div_t4":expected[nv]})
def terms(poly):return [{"powers":[int(e) for e in k],"coefficient":int(v)} for k,v in sorted(poly.to_dict().items())]
data={"result":"PASS","at":datetime.now(timezone.utc).isoformat(),"source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),"engine":"python-flint exact integer polynomials; no imported producer artifacts","estimated_mb":100,"admission_free_bytes":free,"cpu_threads":1,"assertions":["boundary division identity","root-product factorization","cubic derivative and two extremal values","discriminant expansion","both discriminant maps","positive coefficient expansions for c>=4","all three finite base Rayleigh numerators"],"base_cases":base,"variables":["n","t","r","c","u","x"],"L":terms(L),"C":terms(C),"J":terms(J),"lower_coefficients":[terms(v) for v in lc],"upper_coefficients":[terms(v) for v in uc]}
(OUT/"exact_certificate.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps({"result":"PASS","assertion_groups":len(data["assertions"]),"base_cases":[v["n"] for v in base],"source_sha256":data["source_sha256"],"receipt":"output/exact_certificate.json"}),flush=True)
