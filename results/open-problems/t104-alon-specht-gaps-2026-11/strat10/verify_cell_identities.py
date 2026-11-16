"""PROVED: symbolic directional identities and padded cubic residual audit."""
import sympy as S
from cells import DIRECTIONS,residual_blocks
from frame import A,B,C,d,e,f,h,a,r,formula

def main():
    x,y,X,Y=S.symbols('x y X Y');alpha,beta,lam=S.symbols('alpha beta lam')
    moments={(0,0):5,(1,0):0,(0,1):0,(2,0):1,(1,1):0,(0,2):1,
             (4,0):A,(0,4):B,(2,2):C,(3,0):d,(2,1):e,(1,2):f,(0,3):h}
    def mm(i,j):return moments.get((i,j),S.Symbol('m%d%d'%(i,j)))
    def edge_sum(expr):
        out=0
        for (i,j,k,l),c in S.Poly(S.expand(expr),x,y,X,Y).terms():out+=c*(mm(i,j)*mm(k,l)-mm(i+k,j+l))/2
        return S.expand(out)
    pij=alpha*x*X+beta*y*Y;weight=lam/5+a*x*X+a*r*y*Y
    diag=alpha*alpha*A+2*alpha*beta*C+beta*beta*B
    Z=a*(alpha*alpha*mm(6,0)+2*alpha*beta*mm(4,2)+beta*beta*mm(2,4))+a*r*(alpha*alpha*mm(4,2)+2*alpha*beta*mm(2,4)+beta*beta*mm(0,6))
    N=a*(alpha*alpha*d*d+2*alpha*beta*e*e+beta*beta*f*f)+a*r*(alpha*alpha*e*e+2*alpha*beta*f*f+beta*beta*h*h)
    ss=alpha*a+beta*a*r-a*(alpha*A+beta*C)-a*r*(alpha*C+beta*B)-lam*(alpha+beta)/5
    assert S.expand(2*edge_sum(weight*pij)-ss)==0
    assert S.expand(2*edge_sum(weight*pij*pij)-N+Z-lam*(alpha*alpha+beta*beta-diag)/5)==0
    td=S.Symbol('td');theta=S.symbols('theta0:4');zs=S.symbols('z0:4')
    vector=[]
    for v in theta:vector.extend((v,0,0,0,0))
    vector+=[td]+list(zs)
    df,eh=residual_blocks(r,vector)
    pol=df[0]*d*d+2*df[1]*d*f+df[2]*f*f+eh[0]*e*e+2*eh[1]*e*h+eh[2]*h*h
    R6=3*d*d+3*r*r*h*h+(1+4*r)*e*e+(r*r+4*r)*f*f+2*(1+r)*(d*f+r*h*e)
    Nr=d*d+(2+r)*e*e+(1+2*r)*f*f+r*h*h
    Jr=(d+f)**2+r*(e+h)**2
    expected=R6+td*(Nr-Jr)+zs[0]*(d*d+e*e)+zs[1]*(f*f+h*h)+zs[2]*e*e+zs[3]*f*f
    for v,(aa,bb)in zip(theta,DIRECTIONS):expected-=v*(aa*aa*d*d+(2*aa*bb+r*aa*aa)*e*e+(bb*bb+2*r*aa*bb)*f*f+r*bb*bb*h*h)
    assert S.expand(pol-expected)==0
    from cells import base_value
    assert S.expand(formula()-base_value((A,B,C),a,r)-a*a*R6)==0
    print('PROVED: directional first/second weighted moments and both padded cubic residual blocks matched exactly.')
if __name__=='__main__':main()
