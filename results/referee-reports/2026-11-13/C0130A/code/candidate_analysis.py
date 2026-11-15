"""Test all rational functions of p of degrees <=d/<=d, d=1,2,3.

If such a function fits the true escape probabilities at 2d+2 points, the
matrix with columns 1,p,...,p^d,e,ep,...,ep^d must be singular. We certify
nonsingularity for the whole box of exact enclosures by ||I-R A||_inf<1,
using a rounded approximate inverse R and exact rational interval arithmetic.
"""
import json
from fractions import Fraction
from pathlib import Path
import mpmath as mp

mp.mp.dps=100

names=['m3_p07','m3_p075','m3_p08','m3_p085',
       'm3_p09','m3_p093','m3_p097','m3_p099']
data=[json.loads(Path(f'data/cert_{x}.json').read_text()) for x in names]

def outward(lo,hi,digits=40):
    scale=10**digits
    lower=(lo.numerator*scale)//lo.denominator
    upper=-((-hi.numerator*scale)//hi.denominator)
    return Fraction(lower,scale),Fraction(upper,scale)

results=[]
for degree in (1,2,3):
    # Spread points across the range, rather than using the first nearby ones.
    indices={1:[0,2,4,7],2:[0,1,2,4,6,7],3:list(range(8))}[degree]
    values=[data[i] for i in indices]
    matrix=[]
    inputs=[]
    mid=[]
    for value in values:
        p=Fraction(value['params'][0])
        lo,hi=Fraction(value['rational_lower']),Fraction(value['rational_upper'])
        elo,ehi=outward(lo,hi)
        inputs.append(dict(p=str(p),escape_lower=str(elo),escape_upper=str(ehi)))
        prow=[p**j for j in range(degree+1)]
        matrix.append([(x,x) for x in prow]+[(elo*x,ehi*x) for x in prow])
        m=mp.mpf((lo+hi).numerator)/((lo+hi).denominator*2)
        pp=mp.mpf(p.numerator)/p.denominator
        mid.append([pp**j for j in range(degree+1)]+
                   [m*pp**j for j in range(degree+1)])
    R=mp.inverse(mp.matrix(mid))
    RI=[[Fraction(mp.nstr(R[i,j],95)) for j in range(R.cols)]
        for i in range(R.rows)]
    row_norms=[]
    for i in range(R.rows):
        bound=Fraction(0)
        for j in range(R.cols):
            dot_lo=dot_hi=Fraction(0)
            for k in range(R.cols):
                v=RI[i][k]
                a,b=matrix[k][j]
                dot_lo+=v*(a if v>=0 else b)
                dot_hi+=v*(b if v>=0 else a)
            res_lo=Fraction(int(i==j))-dot_hi
            res_hi=Fraction(int(i==j))-dot_lo
            bound+=max(abs(res_lo),abs(res_hi))
        row_norms.append(bound)
    norm=max(row_norms)
    scale=10**30
    rounded=Fraction(-((-norm.numerator*scale)//norm.denominator),scale)
    results.append(dict(degree=degree,points=[names[i] for i in indices],
                        residual_norm_upper=str(rounded),
                        residual_norm_upper_decimal=str(float(rounded)),
                        exact_rational_residual_norm=str(norm),
                        inputs=inputs,
                        approximate_inverse_rational=[[str(x) for x in row] for row in RI],
                        excluded=bool(norm<1)))
    print(degree, 'excluded', results[-1]['excluded'], 'residual norm <=',
          results[-1]['residual_norm_upper_decimal'])

record=data[2]
lo,hi=Fraction(record['rational_lower']),Fraction(record['rational_upper'])
mid=(lo+hi)/2
near=mid.limit_denominator(10**6)
assert not lo<=near<=hi
small_den=dict(point='M=3,p=4/5',denominator_limit=10**6,
               nearest_to_midpoint=str(near),inside_interval=False)
Path('data/candidate_analysis.json').write_text(
    json.dumps(dict(rational_functions=results,small_denominator=small_den),indent=2)+'\n')
