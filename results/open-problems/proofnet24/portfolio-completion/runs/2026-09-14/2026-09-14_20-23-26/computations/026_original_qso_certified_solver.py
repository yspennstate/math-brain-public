"""Compute a four-type strictly non-Volterra fixed point with an exact residual certificate.

The search uses ordinary floating point. The final rational candidate and its
residual are checked exactly with fractions.Fraction. The certificate uses
Theorem 2 and equation (10) of FOUR_TYPE_UNIQUENESS.md at q=2/5.
This is not a Lean or interval-arithmetic proof of the universal theorem.

Input JSON: {"pairs": [{"i":0,"j":0,"p":["0","1/3","1/3","1/3"]}, ...]}
Include exactly the ten unordered parent pairs (0<=i<=j<4). Probabilities must
be integers or rational/decimal strings; JSON floating-point numbers are rejected.
Without an input file, use the equiprobable four-type operator.
"""
import argparse
from fractions import Fraction as F
import json
import math
from pathlib import Path

N=4
CAP=F(2,5)

def exact_number(value):
    if isinstance(value,bool) or not isinstance(value,(int,str)):
        raise ValueError('Use integers or exact probability strings, not JSON floats')
    return F(value)

def validate_pairs(data):
    if not isinstance(data,dict):
        raise ValueError('Input must be a JSON object')
    rows=data.get('pairs')
    if not isinstance(rows,list):
        raise ValueError('Input must contain a pairs list')
    P=[[[F(0) for _ in range(N)] for _ in range(N)] for _ in range(N)]
    seen=set()
    for row in rows:
        if not isinstance(row,dict):
            raise ValueError('Each parent-pair entry must be a JSON object')
        i,j=row['i'],row['j']
        if type(i) is not int or type(j) is not int or not 0<=i<=j<N:
            raise ValueError('Parent indices must satisfy 0<=i<=j<4')
        if (i,j) in seen:
            raise ValueError('Duplicate parent pair')
        seen.add((i,j))
        if not isinstance(row['p'],list) or len(row['p'])!=N:
            raise ValueError('Each parent pair requires four offspring probabilities')
        p=[exact_number(v) for v in row['p']]
        if any(v<0 for v in p) or sum(p)!=1:
            raise ValueError('Each probability row must be nonnegative and sum exactly to one')
        if p[i] or p[j]:
            raise ValueError('Strict non-Volterra condition violated')
        P[i][j]=p
        P[j][i]=p[:]
    if seen!={(i,j) for i in range(N) for j in range(i,N)}:
        raise ValueError('Exactly ten unordered parent pairs are required')
    return P

def equiprobable_input():
    return {'pairs':[{'i':i,'j':j,'p':[str(F(1,N-len({i,j}))) if k not in (i,j) else '0'
                                           for k in range(N)]}
                     for i in range(N) for j in range(i,N)]}

def apply_exact(P,x):
    return [sum((P[i][j][k]*x[i]*x[j] for i in range(N) for j in range(N)),F(0))
            for k in range(N)]

def rational_simplex_candidate(x,digits):
    if not all(math.isfinite(t) and t>=0 for t in x) or sum(x)<=0:
        raise ValueError('Numerical search produced an invalid candidate')
    # Treat each binary float exactly, then normalize and round by largest remainders.
    y=[F.from_float(t) for t in x]
    total=sum(y)
    D=10**digits
    scaled=[t*D/total for t in y]
    nums=[t.numerator//t.denominator for t in scaled]
    remaining=D-sum(nums)
    order=sorted(range(N),key=lambda i:(scaled[i]-nums[i],-i),reverse=True)
    for i in order[:remaining]:
        nums[i]+=1
    out=[F(t,D) for t in nums]
    if sum(out)!=1 or min(out)<0:
        raise ArithmeticError('Rational candidate is outside the simplex')
    return out

def certify(P,x):
    """Certify a candidate for an array previously returned by validate_pairs."""
    if len(x)!=N or min(x)<0 or sum(x)!=1 or max(x)>CAP:
        raise ValueError('Certificate requires a rational probability vector in K_(2/5)')
    vx=apply_exact(P,x)
    residual=sum(abs(v-xi) for v,xi in zip(vx,x))
    radius=min(F(2),5*residual)
    # The difference of probability vectors is zero-sum, so each coordinate
    # error is at most half its l1 norm.
    intervals=[[max(F(0),xi-radius/2),min(CAP,xi+radius/2)] for xi in x]
    return {'candidate':[str(t) for t in x],
            'exact_residual_l1':str(residual),
            'certified_error_l1_upper':str(radius),
            'coordinate_intervals':[[str(a),str(b)] for a,b in intervals],
            'certificate_basis':'FOUR_TYPE_UNIQUENESS.md, equation (10), q=2/5',
            'arithmetic':'exact rational residual; floating-point candidate search'}

def solve(P,tolerance=F(1,10**8),digits=12,max_steps=500):
    if not 1<=digits<=30 or not 0<=max_steps<=100000 or tolerance<=0:
        raise ValueError('Invalid digits, maximum steps, or tolerance')
    Pf=[[[float(v) for v in row] for row in plane] for plane in P]
    x=[.25]*N
    best=None
    for step in range(max_steps+1):
        candidate=rational_simplex_candidate(x,digits)
        if max(candidate)<=CAP:
            result=certify(P,candidate)
            error=F(result['certified_error_l1_upper'])
            if best is None or error<F(best['certified_error_l1_upper']):
                best=result|{'search_step':step}
            if error<=tolerance:
                return best|{'requested_tolerance':str(tolerance),'tolerance_met':True}
        if step==max_steps:
            break
        vx=[sum(Pf[i][j][k]*x[i]*x[j] for i in range(N) for j in range(N)) for k in range(N)]
        x=[.6*xi+.4*vi for xi,vi in zip(x,vx)]
        s=sum(x)
        x=[t/s for t in x]  # Search stabilization; the final exact certificate is independent of this step.
    if best is None:
        raise ArithmeticError('No candidate in the certified cap was found')
    return best|{'requested_tolerance':str(tolerance),'tolerance_met':False}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',nargs='?',type=Path)
    parser.add_argument('--tolerance',default='1e-8')
    parser.add_argument('--digits',type=int,default=12)
    parser.add_argument('--max-steps',type=int,default=500)
    args=parser.parse_args()
    try:
        data=json.loads(args.input.read_text()) if args.input else equiprobable_input()
        result=solve(validate_pairs(data),exact_number(args.tolerance),args.digits,args.max_steps)
    except (ValueError,KeyError,TypeError,ArithmeticError,OSError) as exc:
        parser.error(str(exc))
    print(json.dumps(result,indent=2))
    return 0 if result['tolerance_met'] else 2

if __name__=='__main__':
    raise SystemExit(main())
