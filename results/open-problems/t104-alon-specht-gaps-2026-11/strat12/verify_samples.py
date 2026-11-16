"""Replay ten rational sample signs; sample selection is NUMERICAL only."""
import json
from pathlib import Path
from fractions import Fraction as F
from exact_bernstein import data,active_constraints

HERE=Path(__file__).resolve().parent

def evaluate(poly,point):
    powers=[[x**k for k in range(9)] for x in point]
    out=F(0)
    for m,c in poly.items():
        v=F(c)
        for i,k in enumerate(m):v*=powers[i][k]
        out+=v
    return out

def main():
    records=json.loads((HERE/'exact_samples.json').read_text())['records']
    p,gs=data()
    for r in records:
        point=list(map(F,r['point']))
        value=evaluate(p,point)
        assert str(value)==r['T_numerator'] and value>0
        for key,g in gs.items():
            if key in ('scale14','scale_guard'):continue
            v=evaluate(g,point)
            assert str(v)==r['constraints'][key]
            assert v>0 if key in ('connected','rank','ratio') else v>=0
        # Independent direct rational zero-face formula for N=6.
        t,v1,z1,v2,z2,z=point
        V=[(v1,z1),(v2,z2),(1-t-v1-v2,-z-z1-z2),(t,F(0)),(F(-1),z)]
        R=[[sum(V[i][a]*V[j][a] for a in range(2)) for j in range(5)] for i in range(5)]
        M=[[sum(V[i][a]*V[i][b] for i in range(5)) for b in range(2)] for a in range(2)]
        delta=M[0][0]*M[1][1]-M[0][1]**2;tau=M[0][0]+M[1][1];D=20*t-tau
        adj=[[M[1][1],-M[0][1]],[-M[0][1],M[0][0]]]
        Q=[[sum(V[i][a]*adj[a][b]*V[j][b] for a in range(2) for b in range(2)) for j in range(5)] for i in range(5)]
        P=[[delta*(5*int(i==j)-1)-5*Q[i][j] for j in range(5)] for i in range(5)]
        tr2=sum(x*x for row in R for x in row)
        pr2=sum(P[i][j]*R[i][j]**2 for i in range(5) for j in range(5))
        pr=sum(P[i][i]*R[i][i] for i in range(5))
        edge=sum((t+R[i][j])*(2*delta-Q[i][i]-Q[j][j]+2*Q[i][j])*(R[i][i]+R[j][j]-2*R[i][j])
                 for i in range(5) for j in range(i+1,5))
        direct=(160*delta*(40*t*tau-8*tr2)+384*pr2
                +(D-10*t)*(2000*t*delta-160*D*delta+1920*t*delta-48*pr)-1280*edge)/8
        assert direct==value and D>0 and delta>0
    print('PROVED (verify_samples.py): ten exact rational chart samples have positive numerator; independent direct formula agrees. NUMERICAL: selection came from diag_all.json. OPEN: unsampled points.')

if __name__=='__main__':main()
