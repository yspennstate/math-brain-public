"""Deterministic numerical diagnostics for PROOF.md; standard library only.

Run with: python -B resource_guard.py verify_reduction.py
Numerical quadrature is a diagnostic, not the proof of a uniform inequality.
"""
import json
import math
from fractions import Fraction
from pathlib import Path
import time

START = time.monotonic()
ROOT = Path(__file__).resolve().parent


def simpson(fn, left, right, n=12000):
    assert n % 2 == 0
    step = (right-left)/n
    return step/3 * (fn(left)+fn(right)+math.fsum(
        (4 if j % 2 else 2)*fn(left+j*step) for j in range(1, n)))


def check(condition, message):
    if not condition:
        raise AssertionError(message)
    if time.monotonic()-START > 180:
        raise RuntimeError("Three-minute diagnostic deadline reached")


data = {"purpose": "independent constant and quadrature checks, not a proof by experiment"}
check(Fraction(480,512) == Fraction(15,16), "final exact rational constant")
check(Fraction(3)*(1+38+1) == 120, "Cauchy--Schwarz coefficient")
data["exact_constants"] = {"squared_error_factor": str(Fraction(480,512)),
                           "cauchy_coefficient": 120, "radius_coefficient": 38}

# Cover tiny tolerances, large dimensions, poor centers, and arbitrary m.
grid = []
for d in (1,2,3,10,100,10000,1000000):
    for h in (0.0,1e-6,1.0,10.0,1e6,1e20,1e100):
        for eps in (1.0,0.5,0.1,1e-3,1e-12,1e-100):
            A = d+h+math.log(1/eps)
            delta = eps*eps*d/(512*A)
            s = -math.log(delta)
            a = d*math.log(2)/2
            mr2 = 4*(a+s)
            ratio = 2*math.sqrt(delta)*(math.sqrt(h)+math.sqrt(mr2)+1)/(eps*math.sqrt(d))
            # An independent computation of the same number in logarithms.
            log_ratio = (math.log(2)+math.log(delta)/2+
                         math.log(math.sqrt(h)+math.sqrt(mr2)+1)-
                         math.log(eps)-math.log(d)/2)
            check(abs(math.log(ratio)-log_ratio)<2e-12, "independent ratio computation")
            check(s <= 9*A*(1+1e-14), "logarithm allocation")
            check(mr2 <= 38*A*(1+1e-14), "radius allocation")
            check(ratio*ratio <= 15/16*(1+1e-13), "normalized Wasserstein allocation")
            check(abs((a-mr2/4)+s)<1e-8, "tail cancellation in logarithms")
            for m in (1e-6,1.0,1e6):
                D = math.sqrt(h/m)
                R = math.sqrt(mr2/m)
                physical_ratio = 2*math.sqrt(delta)*(D+R+1/math.sqrt(m))/(eps*math.sqrt(d/m))
                check(abs(physical_ratio-ratio)<1e-12, "scale invariance")
            grid.append({"d":d,"mD2":h,"epsilon":eps,"A":A,
                         "delta":delta,"normalized_error_upper_ratio":ratio})
data["allocation_grid"] = grid
data["allocation_summary"] = {
    "cases":len(grid), "physical_scale_cases":3*len(grid),
    "max_error_upper_ratio":max(row["normalized_error_upper_ratio"] for row in grid)}

# Gaussian moments: integration-by-parts recurrence versus gamma function,
# and summing the moment series versus the closed-form moment generating function.
mgf_checks = []
for d in (1,2,3,10,100):
    product = 1.0
    for k in range(1,9):
        product *= d+2*k-2
        gamma_moment = math.exp(k*math.log(2)+math.lgamma(d/2+k)-math.lgamma(d/2))
        check(abs(product/gamma_moment-1)<2e-13, "radial moment recurrence")
    term, terms = 1.0, [1.0]
    for k in range(1,2001):
        term *= 0.25*(d+2*k-2)/k
        terms.append(term)
        if k>100 and term<1e-16*math.fsum(terms):
            break
    series = math.fsum(terms)
    exact = 2**(d/2)
    check(abs(series/exact-1)<5e-14, "Gaussian MGF series")
    mgf_checks.append({"d":d,"series":series,"closed_form":exact,"terms":len(terms)})
data["independent_gaussian_mgf"] = mgf_checks

# Nonquadratic and asymmetric targets, each with mode zero and Hessian in [1,2].
models = [
    ("Gaussian",lambda x:x*x/2,lambda x:x),
    ("nonquadratic_even",lambda x:x*x/2+0.75*(math.sqrt(1+x*x)-1),
     lambda x:x+0.75*x/math.sqrt(1+x*x)),
    ("nonquadratic_asymmetric",lambda x:0.75*x*x+0.25*(x-math.atan(x)),
     lambda x:1.5*x+0.25*x*x/(1+x*x))]
quadratures = []
for name,f,grad in models:
    weight = lambda x:math.exp(-f(x))
    Z = simpson(weight,-16,16)
    mgf = simpson(lambda x:math.exp(-f(x)+x*x/4),-16,16)/Z
    mean = simpson(lambda x:x*weight(x),-16,16)/Z
    ibp_errors = []
    for k in range(1,5):
        lhs = simpson(lambda x:x**(2*k-1)*grad(x)*weight(x),-16,16)/Z
        rhs = (2*k-1)*simpson(lambda x:x**(2*k-2)*weight(x),-16,16)/Z
        ibp_errors.append(abs(lhs-rhs)/max(1,abs(rhs)))
        check(ibp_errors[-1]<2e-11,"independent integration-by-parts recurrence")
    check(mgf<=math.sqrt(2)*(1+1e-12),"nonquadratic MGF inequality")
    tail_rows = []
    for delta in (0.1,0.001,1e-8):
        R = 2*math.sqrt(math.log(2)/2+math.log(1/delta))
        tail = (simpson(lambda x:(x-R)**2*weight(x),R,20)+
                simpson(lambda x:(x+R)**2*weight(x),-20,-R))/Z
        check(tail <= 4*delta*(1+1e-12), "integrated projection tail")
        tail_rows.append({"delta":delta,"R":R,"projection_error_squared":tail,
                          "proved_upper_bound":4*delta})
    for c in (-10,-1,0,1,10):
        check(abs(c)<=abs(grad(c))*(1+1e-14),"gradient distance certificate at m=1")
    quadratures.append({"target":name,"mean":mean,"mgf_at_one_quarter":mgf,
                        "Gaussian_mgf_bound":math.sqrt(2),
                        "max_ibp_relative_error":max(ibp_errors),"tails":tail_rows})
data["nonquadratic_quadrature"] = quadratures

# Reverse-transfer obstruction: constant TV, vanishing normalized W2,
# with one common sqrt(2)-warm start and actual condition number exactly 2.
crossing = math.sqrt(math.log(2))
Phi = lambda x:(1+math.erf(x/math.sqrt(2)))/2
tv_formula = 2*(Phi(math.sqrt(2)*crossing)-Phi(crossing))
p = lambda x:math.exp(-x*x/2)/math.sqrt(2*math.pi)
q = lambda x:math.exp(-x*x)/math.sqrt(math.pi)
tv_integral = simpson(lambda x:q(x)-p(x),-crossing,crossing)
check(abs(tv_formula-tv_integral)<1e-12,"independent Gaussian TV calculations")
w2 = 1-1/math.sqrt(2)
data["reverse_transfer_obstruction"] = {
    "TV_formula":tv_formula,"TV_quadrature":tv_integral,"W2_exact":w2,
    "common_warmness_bound":math.sqrt(2),
    "normalized_W2":[{"d":d,"error":w2/math.sqrt(d)} for d in (3,10,100,10000,1000000)]}

# Verify the polynomial bookkeeping independently on a separate grid.
query_cases = 0
for d in (2,10,1000):
    for kappa in (1,2,1000):
        for G0 in (0,1,1e9):
            for eps in (1,0.01,1e-10):
                B = d+kappa+1/eps+G0
                A = d+kappa*G0+math.log(1/eps)
                inv_delta = 512*A/(eps*eps*d)
                check(A<=2*B*B,"query allocation A")
                check(d+kappa+G0+inv_delta<=1025*B**4,"query allocation exponent four")
                query_cases += 1
data["query_bookkeeping_cases"] = query_cases
data["elapsed_seconds"] = time.monotonic()-START

path = ROOT/"verification.json"
path.write_text(json.dumps(data,indent=2,allow_nan=False)+"\n",encoding="utf-8")
print("PASS: exact constant 480/512 = 15/16")
print(f"PASS: {len(grid)} accuracy allocations and {3*len(grid)} physical-scale checks")
print("Maximum normalized error bound on grid:",format(data["allocation_summary"]["max_error_upper_ratio"],".15g"))
print("PASS: 5 Gaussian MGF series and gamma-function moment checks")
print("PASS: 3 target quadratures, asymmetric mode/mean check, 9 tail integrals")
print("PASS: Gaussian TV by CDF and quadrature:",format(tv_formula,".15g"))
print("PASS:",query_cases,"query-exponent allocations")
print("Data: verification.json")
print("Elapsed seconds:",round(data["elapsed_seconds"],3))
