"""Construct and check C081's exact multivariate SOS / univariate Bernstein certificate.

All sign decisions use fractions or integers. NumPy and floating point are absent.
The entropy reduction and six two-site coefficients are proved in agents/C081.md.
This file constructs the remaining central coefficient directly from principal
minors, inverse-gradient numerators, and the adjugate quadratic form.
"""
from fractions import Fraction as F
from math import comb, gcd, lcm
from pathlib import Path
import argparse
import json
import sympy as s

HERE=Path(__file__).resolve().parent
y=s.Symbol('y', real=True)
R=s.Matrix([[1,s.Rational(1,2),s.Rational(1,10)-s.I*y],
            [s.Rational(1,2),1,s.Rational(3,5)],
            [s.Rational(1,10)+s.I*y,s.Rational(3,5),1]])
PAIRS=[(0,1),(0,2),(1,2)]
BASIS=[]
for i in range(3):
    E=s.zeros(3); E[i,i]=1; BASIS.append(E)
for i,j in PAIRS:
    E=s.zeros(3); E[i,j]=E[j,i]=1; BASIS.append(E)
for i,j in PAIRS:
    E=s.zeros(3); E[i,j]=s.I; E[j,i]=-s.I; BASIS.append(E)
DF=s.diag(1,1,1,2,2,2,2,2,2)
ADJ=[[((BASIS[i]+BASIS[j]).adjugate()-BASIS[i].adjugate()-BASIS[j].adjugate())
      for j in range(9)] for i in range(9)]

def qf(N):
    """b^T qf(N)b = 2 tr(N adj(B)), for B=sum b_i BASIS_i."""
    return s.Matrix(9,9,lambda i,j:s.expand(s.trace(N*ADJ[i][j])))

def frac(q):
    q=s.Rational(q)
    return F(int(q.p),int(q.q))

def encode(q):
    q=F(q)
    return str(q.numerator) if q.denominator==1 else f'{q.numerator}/{q.denominator}'

def log_bracket(r, digits=10):
    """Exact rational endpoints enclosing log(r), for the arguments used here."""
    r=F(r)
    assert r>=1
    z=(r-1)/(r+1)
    n=16
    low=2*sum((z**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
    high=low+2*z**(2*n+1)/(F(2*n+1)*(1-z*z))
    scale=10**digits
    lo=(low.numerator*scale)//low.denominator
    hi=(high.numerator*scale+high.denominator-1)//high.denominator
    lower,upper=F(lo,scale),F(hi,scale)
    assert lower<=low<=high<=upper
    # Retain the exact positive atanh tail, not a transcendental evaluation.
    return lower,upper

def log_ranges(a,b):
    d13=lambda t:F(99,100)-t*t
    det=lambda t:F(11,25)-t*t
    # Order: c23,c13,c12,tau. The two moving functions are increasing.
    return [log_bracket(F(25,16)),
            (log_bracket(1/d13(a))[0],log_bracket(1/d13(b))[1]),
            log_bracket(F(4,3)),
            (log_bracket(F(12,25)*d13(a)/det(a))[0],
             log_bracket(F(12,25)*d13(b)/det(b))[1])]

def construct_polynomials():
    weights={}; nums={}
    for mask in range(8):
        ids=[i for i in range(3) if mask>>i&1]
        V=s.zeros(3)
        if ids:
            sub=R.extract(ids,ids); w=s.expand(sub.det()); adj=sub.adjugate()
            for j,i in enumerate(ids):
                for k,h in enumerate(ids): V[i,h]=adj[j,k]
        else: w=s.Integer(1)
        weights[mask]=w
        nums[mask]=s.Matrix([s.expand(s.trace(V*E)) for E in BASIS])
    assert weights[3]==s.Rational(3,4)
    assert weights[6]==s.Rational(16,25)
    assert weights[5]==s.Rational(99,100)-y*y
    assert weights[7]==s.Rational(11,25)-y*y
    W=s.expand(weights[3]*weights[5]*weights[6]*weights[7])
    P=s.zeros(9)
    for mask in [0,1,2,4]:
        comp=7^mask
        # wS wT (vS-vT)(vS-vT)^T, with the W denominator cleared.
        v=weights[comp]*nums[mask]-weights[mask]*nums[comp]
        mult=s.cancel(W/(weights[mask]*weights[comp]))
        P+=mult*(v*v.T)
    G=[]
    for i in range(3):
        E=s.zeros(3);E[i,i]=1
        G.append(qf(R*E+E*R))
    G.append(qf(R))
    mats=[P]+[W*g for g in G]+[W*DF]
    coeffs=[]
    for M in mats:
        polys=[[s.Poly(s.expand(M[i,j]),y) for j in range(9)] for i in range(9)]
        assert all(p.degree()<=6 for row in polys for p in row)
        coeffs.append([[[frac(polys[i][j].nth(k)) for j in range(9)] for i in range(9)] for k in range(7)])
    return weights,W,coeffs

def scaled_ldl(M, factors=False):
    """Integer Bareiss elimination yields exact positive LDL pivots."""
    scale=1
    for row in M:
        for q in row: scale=lcm(scale,q.denominator)
    A=[[q.numerator*(scale//q.denominator) for q in row] for row in M]
    prev=1; piv=[]; L=[[F(int(i==j)) for j in range(9)] for i in range(9)]
    for k in range(9):
        p=A[k][k]
        if p<=0: return None
        piv.append(F(p,prev*scale))
        if factors:
            for j in range(k+1,9): L[j][k]=F(A[j][k],p)
        if k<8:
            new=[row[:] for row in A]
            for i in range(k+1,9):
                for j in range(i,9):
                    v=p*A[i][j]-A[i][k]*A[k][j]
                    q,r=divmod(v,prev)
                    assert r==0
                    new[i][j]=new[j][i]=q
            A=new
        prev=p
    if factors:
        for i in range(9):
            for j in range(9):
                assert sum((L[i][k]*piv[k]*L[j][k] for k in range(9)),F(0))==M[i][j]
        return piv,L
    return piv

def bernstein_factors(a,b,n=6):
    h=b-a
    return [[sum((F(comb(j,t),comb(n,t))*comb(k,t)*a**(k-t)*h**t
                  for t in range(min(j,k)+1)),F(0)) for k in range(n+1)]
            for j in range(n+1)]

def cell_certificate(a,b,coeffs,gap=F(1,100),save_factors=False):
    logs=log_ranges(a,b)
    mids=[(u+v)/2 for u,v in logs]
    radii=[(v-u)/2 for u,v in logs]
    # |qf(R Ei+Ei R)| <= (5,26/5,26/5) DF and |qf(R)| <= 211/50 DF.
    error=sum((c*r for c,r in zip([F(5),F(26,5),F(26,5),F(211,50)],radii)),F(0))
    multipliers=[F(1)]+[-q for q in mids]+[-error-gap]
    poly=[[[sum((multipliers[t]*coeffs[t][k][i][j] for t in range(6)),F(0))
             for j in range(9)] for i in range(9)] for k in range(7)]
    Bs=[]; results=[]
    for j,facs in enumerate(bernstein_factors(a,b)):
        B=[[sum((facs[k]*poly[k][i][h] for k in range(7)),F(0))
             for h in range(9)] for i in range(9)]
        out=scaled_ldl(B,factors=save_factors)
        if out is None: return None
        piv,L=out if save_factors else (out,None)
        result={'index':j,'pivot_lower_1e9':[int(q*10**9) for q in piv]}
        assert min(result['pivot_lower_1e9'])>0
        if save_factors:
            result['B']=[[encode(q) for q in row] for row in B]
            result['L']=[[encode(q) for q in row] for row in L]
            result['D']=[encode(q) for q in piv]
        results.append(result)
    return {'a':encode(a),'b':encode(b),'log_intervals':[[encode(q) for q in z] for z in logs],
            'error':encode(error),'bernstein':results}

def check_side_thresholds():
    lr=log_ranges(F(1,5),F(1,2))
    assert all(a>0 for a,b in lr)
    assert lr[0][1]<F(9,20)
    assert lr[1][1]<F(1,3)
    assert lr[2][1]<F(3,10)
    assert lr[3][1]<F(2,3)
    assert max(b for a,b in lr[:3])+lr[3][1]<2
    return [[encode(q) for q in z] for z in lr]

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--verify',action='store_true');ap.add_argument('--full-factors',action='store_true')
    args=ap.parse_args()
    weights,W,coeffs=construct_polynomials()
    thresholds=check_side_thresholds()
    if args.verify:
        cert=json.loads((HERE/'certificate.json').read_text())
        spans=[(F(c['a']),F(c['b'])) for c in cert['cells']]
        assert spans[0][0]==F(1,5) and spans[-1][1]==F(1,2)
        assert all(u[1]==v[0] for u,v in zip(spans,spans[1:]))
    else:
        spans=[(F(1,5)+F(3*k,640),F(1,5)+F(3*(k+1),640)) for k in range(64)]
    cells=[]; count=0
    while spans:
        a,b=spans.pop(0)
        cell=cell_certificate(a,b,coeffs,save_factors=args.full_factors)
        if cell is None:
            if args.verify: raise AssertionError(('failed stored cell',a,b))
            assert b-a>F(1,100000)
            m=(a+b)/2;spans[:0]=[(a,m),(m,b)];continue
        cells.append(cell);count+=1
        if count%20==0: print(f'Certified {count} exact cells through y={b}',flush=True)
    if args.verify:
        assert len(cells)==len(cert['cells'])
        for got,stored in zip(cells,cert['cells']):
            for key in ['a','b','log_intervals','error']: assert got[key]==stored[key]
            for G,S in zip(got['bernstein'],stored['bernstein']):
                assert G['index']==S['index'] and G['pivot_lower_1e9']==S['pivot_lower_1e9']
    result={'status':'PASS','gamma':'1/100','central_polynomial_degree':6,
            'phase_interval':['1/5','1/2'],'external_fields':'all x1,x2,x3 > 0',
            'side_log_intervals':thresholds,'cell_count':len(cells),
            'bernstein_matrix_count':7*len(cells),'positive_pivot_count':63*len(cells),
            'minimum_pivot_lower_1e9':min(min(b['pivot_lower_1e9']) for c in cells for b in c['bernstein']),
            'cells':cells}
    if not args.verify:
        (HERE/'certificate.json').write_text(json.dumps(result,indent=2)+'\n')
        data={'basis':['a1','a2','a3','Re12','Re13','Re23','Im12','Im13','Im23'],
              'W':str(W),'weights':{str(k):str(v) for k,v in weights.items()},
              'coefficient_components':[[[[encode(q) for q in row] for row in mat] for mat in comp] for comp in coeffs]}
        (HERE/'polynomial_data.json').write_text(json.dumps(data,indent=2)+'\n')
    summary={k:v for k,v in result.items() if k!='cells'}
    print(json.dumps(summary,indent=2))

if __name__=='__main__': main()
