"""Deterministic audits of PROOF.md; standard library only, small bounded work.

Run: python -B verify.py
Writes verification.json and verification_output.txt beside this script.
"""
import os
for _key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_key] = "1"
import ctypes
if os.name == "nt":
    kernel = ctypes.windll.kernel32
    kernel.GetCurrentProcess.restype = ctypes.c_void_p
    kernel.SetPriorityClass.argtypes = (ctypes.c_void_p, ctypes.c_uint)
    if not kernel.SetPriorityClass(kernel.GetCurrentProcess(), 0x4000):
        raise OSError("Could not set BelowNormal priority")
import json
import math
import time
from decimal import Decimal, getcontext
from fractions import Fraction as Q
from pathlib import Path

START = time.monotonic()
HERE = Path(__file__).resolve().parent
getcontext().prec = 75
out = []

def say(s):
    out.append(s)
    print(s, flush=True)

def deadline():
    if time.monotonic() - START > 120:
        raise RuntimeError("Audit exceeded its two-minute internal budget")

def partitions(items):
    if not items:
        yield []
        return
    head, *tail = items
    for rest in partitions(tail):
        yield [[head]] + rest
        for j in range(len(rest)):
            yield rest[:j] + [[head] + rest[j]] + rest[j+1:]

Y = [Q(1), Q(1), Q(6), Q(60), Q(840)]

def raw_mean_partition(n, r):
    # Sum over equality partitions of the r ordered summation indices.
    total = Q(0)
    for blocks in partitions(list(range(r))):
        falling = math.prod(n-j for j in range(len(blocks)))
        total += falling * math.prod(Y[len(block)] for block in blocks)
    return total / n**r

def raw_mean_formula(n):
    return [Q(1), Q(1), 1+Q(5,n),
            1+Q(15,n)+Q(44,n*n),
            1+Q(30,n)+Q(251,n*n)+Q(558,n**3)]

def central_from_raw(raw, r):
    return sum(math.comb(r,j)*(-1)**(r-j)*raw[j] for j in range(r+1))

def central_product_recursion(n, h):
    # Independent route: D_new=D+(1+D)U; use central moments of U=B-1.
    raw = [raw_mean_partition(n,r) for r in range(5)]
    U = [central_from_raw(raw,r) for r in range(5)]
    D = [Q(1), Q(0), Q(0), Q(0), Q(0)]
    for _ in range(h):
        nxt = []
        for r in range(5):
            nxt.append(sum(math.comb(r,k)*U[k]*sum(
                math.comb(k,l)*D[r-k+l] for l in range(k+1))
                for k in range(r+1)))
        D = nxt
    return D

exact = []
for n in (1,2,3,7,20,100):
    a = raw_mean_formula(n)
    for r in range(5):
        assert raw_mean_partition(n,r) == a[r], (n,r)
    for h in (1,2,3,7):
        central = central_product_recursion(n,h)
        d2 = a[2]**h-1
        d4 = a[4]**h-4*a[3]**h+6*a[2]**h-3
        assert central[2] == d2 and central[4] == d4
        assert d4 >= 0
        exact.append({"n":n,"h":h,"D2":str(d2),"D4":str(d4)})
deadline()
say("PASS exact rational moments: set partitions vs formulas (30 comparisons)")
say("PASS product centered moments: independent recursion vs powers (24 cases)")

# Re-derive the leading n^-2 coefficient of D4 without floating point.
def poly_mul(p,q):
    ans = [Q(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            ans[i+j] += a*b
    return ans

def poly_pow(p,h):
    ans = [Q(1)]
    for _ in range(h):
        ans = poly_mul(ans,p)
    return ans

polys = []
for h in range(1,9):
    parts = [(1,poly_pow([1,30,251,558],h)),
             (-4,poly_pow([1,15,44],h)),
             (6,poly_pow([1,5],h)),(-3,[1])]
    coef = [sum(s*(p[j] if j<len(p) else 0) for s,p in parts)
            for j in range(3*h+1)]
    assert coef[0] == coef[1] == 0
    assert coef[2] == 75*h*h
    assert all(c>=0 for c in coef)
    polys.append({"h":h,"coefficients":[str(c) for c in coef]})
say("PASS independent polynomial expansion: D4 leading coefficient 75*h^2 (h=1..8)")

assert 36**2+4*16**2+6*5**2 == 2470
assert 536+4*88 == 888
assert (2470+888)//2 == 1679
say("PASS derivative-bound arithmetic: 2470 + 888 = 3358; half = 1679")

grid = []
for n in (100,1000,10000,1000000):
    for h in sorted({1,2,10,max(1,n//100),max(1,n//10),n}):
        nd,hd = Decimal(n),Decimal(h)
        rho = hd/nd
        a2=1+5/nd
        a3=1+15/nd+44/nd**2
        a4=1+30/nd+251/nd**2+558/nd**3
        d2=a2**h-1
        d4=a4**h-4*a3**h+6*a2**h-3
        bound=1679*(33*rho).exp()*rho*rho
        assert d4>=0 and d4<=bound
        assert d2>=5*rho and d2<=(5*rho).exp()-1+Decimal("1e-65")
        grid.append({"n":n,"h":h,"D2":str(d2),"D4":str(d4),
                     "D4_over_rho2":str(d4/(rho*rho)),"bound":str(bound)})
say(f"PASS depth-bound grid: {len(grid)} cases, including h=n and n=1000000")

# h=1 has a closed Laplace transform, independently of the product formulas.
smooth=[]
target=Decimal(5)*(-Decimal(1)/2).exp()/8
for n in (1,10,100,1000,10000,1000000):
    nd=Decimal(n)
    laplace=((1+(1+2/nd).sqrt()**(-1))/2)**n
    gap=laplace-(-Decimal(1)/2).exp()
    d2=5/nd
    d4=75/nd**2+558/nd**3
    remainder=(d2*d4).sqrt()/48
    main=(-Decimal(1)/2).exp()*d2/8
    assert abs(gap-main)<=remainder
    smooth.append({"n":n,"gap":str(gap),"n_gap":str(nd*gap),
                   "main":str(main),"remainder_bound":str(remainder)})
say("PASS one-layer exact Laplace transform vs Taylor remainder (6 widths)")
say(f"cosine coefficient target = {target:.15f}")
say(f"n*gap at n=1000000 = {Decimal(smooth[-1]['n_gap']):.15f}")

# Independent numerical integral for the density overlap in equation (16).
def overlap_integral(v,w):
    limit=12.0
    steps=12000
    dx=2*limit/steps
    pref=1/math.sqrt(2*math.pi*v*w)
    precision=1/v+1/w-1
    def integrand(x):
        return pref*math.exp(-precision*x*x/2)
    s=integrand(-limit)+integrand(limit)
    for j in range(1,steps):
        s+=(4 if j%2 else 2)*integrand(-limit+j*dx)
    return s*dx/3

overlaps=[]
for v,w in ((.75,.75),(.75,1.25),(1.25,1.25),(1,1.25),(.91,1.13)):
    numerical=overlap_integral(v,w)
    exact_kernel=1/math.sqrt(v+w-v*w)
    error=abs(numerical-exact_kernel)
    assert error<1e-10
    overlaps.append({"v":v,"w":w,"integral":numerical,
                     "kernel":exact_kernel,"absolute_error":error})
say(f"PASS Gaussian overlap: independent Simpson integral (5 pairs), max error {max(x['absolute_error'] for x in overlaps):.3g}")

for j in range(2001):
    z=-1/16+j/16000
    rem=(1-z)**(-.5)-1-z/2
    assert -5e-16<=rem<=z*z+5e-16
say("PASS chi-square Taylor bound on 2001 grid points in [-1/16,1/16]")

# n=1,h=1 is adversarial: the field has an atom of mass 1/2 at zero.
atom_gap=Decimal(1)/2+Decimal(1)/(2*Decimal(3).sqrt())-(-Decimal(1)/2).exp()
assert abs(atom_gap-Decimal(smooth[0]["gap"]))<Decimal("1e-70")
say("PASS n=1 atom check: exact mass 1/2; characteristic gap matches mixture formula")

# Check the arithmetic in the independent absolute-moment depth lower bound.
assert (math.sqrt(2)+1)**2 < 6
for n in (100,101,1000,1000000):
    fourth=Q(75,n*n)+Q(558,n**3)
    assert fourth<=Q(81,n*n)
    retained=Q(5,n)-Q(81,n*n)
    assert retained>=Q(4,n)
    assert retained/12>=Q(1,3*n)
say("PASS independent depth lower bound: variance truncation constants (4 widths)")

deadline()
data={"exact_moments":exact,"polynomial_coefficients":polys,"depth_grid":grid,
      "one_layer_smooth_gap":smooth,"cosine_coefficient":str(target),
      "gaussian_overlap":overlaps,"elapsed_seconds":time.monotonic()-START,
      "method":"deterministic exact rational/decimal identities and diagnostic quadrature; no simulation"}
(HERE/"verification.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
say("ALL CHECKS PASSED; data saved to verification.json")
(HERE/"verification_output.txt").write_text("\n".join(out)+"\n",encoding="utf-8")
