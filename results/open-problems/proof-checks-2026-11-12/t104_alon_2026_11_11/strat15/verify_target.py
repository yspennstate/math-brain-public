"""Exact quadratic extraction and compactification, including u=0."""
import json,sys
from pathlib import Path
from fractions import Fraction as F
from exact_bernstein import chart_data,base,HERE

def main():
    rr,t,V,R,M,delta,Q,tau,D,edges,P,C=base.construct()
    q=rr.gens[-1];c=[C.coeff_wrt(6,j)for j in range(3)]
    assert C==sum(p*q**j for j,p in enumerate(c))
    # Expanded q coefficients, independently from the compact invariant formula.
    tr2=sum(R[i][j]**2 for i in range(5)for j in range(5))
    pr2=sum(P[i][j]*R[i][j]**2 for i in range(5)for j in range(5))
    pr=sum(P[i][i]*R[i][i]for i in range(5))
    e=sum(g*(2*delta-Q[i][i]-Q[j][j]+2*Q[i][j])*(R[i][i]+R[j][j]-2*R[i][j])for(i,j),g in edges.items())
    A=10*delta*(40*t*tau-8*tr2)-80*e
    B=16*pr2
    Z=D-10*t
    expected=[16*A+24*B+Z*(2000*t*delta-160*D*delta+1920*t*delta-48*pr),
              8*A+10*B+Z*(1400*t*delta-40*D*delta+320*t*delta-8*pr),
              A+B+200*Z*t*delta]
    assert c==expected
    # Use q's slot for u. Multiplication by u^2 cancels its denominator.
    H=c[2]+(c[1]-2*c[2])*q+(c[0]-c[1]+c[2])*q*q
    controls=[c[2],(c[1]+2*c[2])/4,(c[0]+c[1]+c[2])/4]
    assert H==controls[0]*(1-2*q)**2+2*controls[1]*(2*q)*(1-2*q)+controls[2]*(2*q)**2
    # Independent sign implication using q-1, with no compactification.
    assert C==(c[0]+c[1]+c[2])+(q-1)*(c[1]+2*c[2])+(q-1)**2*c[2]
    targets,gs,cs=chart_data()
    for j,p in enumerate(c):assert {m[:6]:F(str(v))for m,v in p.items()}=={m:8*v for m,v in cs[j].items()}
    record=dict(label='PROVED (verify_target.py)',
        statement='C(q)>=0 for every real q>=1 and c2>=0 at infinity, by nonnegative Bernstein controls on 0<=u<=1/2',
        compactification='u^2*C(1/u-1); controls c2,(c1+2c2)/4,(c0+c1+c2)/4',
        normalization='T_N=C(q)/(10*(q+4)^2*D^2*Delta); T_infinity=c2/(10*D^2*Delta)',
        coefficient_terms=[len(p)for p in c],
        coefficients=[[[list(m[:6]),str(v)]for m,v in sorted(p.items())]for p in c])
    (HERE/'target.json').write_text(json.dumps(record,separators=(',',':'))+'\n')
    print(record['label']+': exact c0,c1,c2 and compactification identities; u=0 included.')
if __name__=='__main__':main()
