"""Exact finite sign-space enumeration and independent analytical checks."""
import os
os.environ.update(OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1")
import csv
import itertools
import json
import math
from pathlib import Path
import sympy as sp
from scipy.special import gammaln, digamma, polygamma

ROOT = Path(__file__).resolve().parents[1]
x = sp.Symbol("x")

def enumerate_signs(n, random_diagonal):
    positions = [(i,j) for i in range(n) for j in range(i if random_diagonal else i+1,n)]
    total = simple = zero = 0
    witness = None
    for signs in itertools.product((-1,1), repeat=len(positions)):
        a = sp.zeros(n)
        for (i,j), s in zip(positions,signs): a[i,j] = a[j,i] = s
        total += 1
        p = a.charpoly(x).as_poly()
        if sp.gcd(p,p.diff()).degree(): continue
        simple += 1
        # For simple spectrum, p_minor(lambda)/p'(lambda) = |u_i(lambda)|^2.
        for i in range(n):
            minor = a.minor_submatrix(i,i).charpoly(x).as_poly()
            if sp.gcd(p,minor).degree():
                zero += 1
                if witness is None: witness = dict(matrix=[list(a.row(k)) for k in range(n)],
                                                  charpoly=str(p.as_expr()),coordinate=i)
                break
    return dict(n=n,diagonal="Rademacher" if random_diagonal else "zero",total=total,
                simple=simple,simple_with_zero=zero,
                exists_some_zero_eigenvector=zero+total-simple,witness=witness)

def main():
    out = ROOT / "data"; out.mkdir(exist_ok=True)
    records=[]
    for random_diagonal, sizes in ((True,(2,3,4)), (False,(2,3,4,5))):
        for n in sizes:
            r = enumerate_signs(n,random_diagonal)
            records.append(r)
            print({k:v for k,v in r.items() if k != "witness"},flush=True)
    (out/"exact_zeros.json").write_text(json.dumps(records,indent=2,default=int)+"\n")
    # Check the entropy derivative algebra symbolically, treating psi symbols as functions.
    z,u=sp.symbols("z u",positive=True)
    b=z-u
    D=sp.loggamma(z)-sp.loggamma(b)-u*sp.log(z)+(b-1)*(sp.polygamma(0,b)-sp.polygamma(0,z))+u
    target=sp.polygamma(0,z)-sp.log(z)+1-(b-1)*sp.polygamma(1,b)
    assert sp.simplify(sp.diff(D,u)-target)==0
    audit=[]
    c=math.sqrt(2/math.pi)
    for n in (16,128,512,2000,8192):
        for r in (1,2,3,4):
            pref=math.exp(gammaln(n/2)-gammaln((n-r)/2)-r/2*math.log(math.pi*n))
            upper=2**r*pref
            lower=upper*math.exp((n-r-2)/2*math.log1p(-r/n**3))
            audit.append(dict(n=n,r=r,t=1,lower=lower,upper=upper,target=c**r))
    (out/"math_checks.json").write_text(json.dumps(dict(rate=c,
        cdf_derivative=math.erf(1e-7/math.sqrt(2))/1e-7,
        entropy_derivative_symbolic=True,spherical_bounds=audit),indent=2)+"\n")

if __name__ == "__main__": main()
