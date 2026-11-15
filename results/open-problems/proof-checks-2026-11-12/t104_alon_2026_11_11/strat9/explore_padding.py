"""NUMERICAL: explore padding comparison on the enhanced moment polytope."""
from moment_polytope import vertices
import numpy as np

def diff(a,r,p):
    A,B,C=map(float,p);s=a*(1+r);la=(2+s)/4;F=a*(A+C)+a*r*(B+C)
    K=a*a*(A+r*r*B+2*r*C-(1+r*r)/5)
    return -K/3+(1-la)*(162+169*s-260*F)/720
if __name__=='__main__':
    vs=vertices(True)
    for r in [0,.05,.12,.2,.4,.6,.8,1]:
        aa=2/(3-r)
        vals=[(diff(aa,r,p),p)for p in vs]
        print('NUMERICAL: r',r,'amax',aa,'minimum Delta lower bound',min(vals))
