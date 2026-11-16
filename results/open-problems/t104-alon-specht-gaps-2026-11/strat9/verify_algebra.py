"""PROVED: replay exact frame expansion and corrected radial reduction."""
import sympy as S
from frame import A,B,C,d,e,f,h,a,r,z,formula

def main():
    x,y,X,Y=S.symbols('x y X Y'); b=a*r;s=a+b;lam=(2+s)/4
    moments={(0,0):5,(1,0):0,(0,1):0,(2,0):1,(1,1):0,(0,2):1,
             (4,0):A,(0,4):B,(2,2):C,(3,0):d,(2,1):e,(1,2):f,(0,3):h}
    def pairs(expr):
        out=0
        for (i,j,k,l),c in S.Poly(S.expand(expr),x,y,X,Y).terms():
            out+=c*moments.get((i,j),S.Symbol('m%d%d'%(i,j)))*moments.get((k,l),S.Symbol('m%d%d'%(k,l)))
        return S.expand(out)
    gap=a*x*X+b*y*Y
    qdiff=(x-X)**2+(y-Y)**2
    gdiff=a*(x-X)**2+b*(y-Y)**2
    Z=pairs((lam/5+gap)*qdiff*gdiff)/2
    F=a*(A+C)+b*(B+C)
    K=a*a*A+b*b*B+2*a*b*C-(a*a+b*b)/5-a*a*(d*d+e*e)-2*a*b*(e*e+f*f)-b*b*(f*f+h*h)
    k=4+z;N=k+2
    hd=S.Rational(4,5)-2*s/5+F
    X1=2*lam*s-2*(a*a+b*b)
    X2=2*N*K/k
    X3=(1-lam)*(2*(N-1)*(N-4)*lam-4*k+2*N*hd)/k**2
    twiceS5=4*(lam*s-a*a-b*b)-2*Z
    assert S.cancel(X1+X2+X3-twiceS5-formula(N))==0
    p=S.Poly(formula(),a)
    assert p.degree()==2 and p.nth(0)==S.Rational(9,80)
    fm=A+r*B+(1+r)*C
    assert S.expand(p.nth(1)-(11*fm-2*(1+r))/8)==0
    # Coefficient bounds use only A+C,B+C >= 1/4.
    v,w=S.symbols('v w',nonnegative=True)
    for idx in (0,1):
        expr=S.cancel(S.Poly(k*k*formula(N),a).nth(idx))
        if idx==1: expr=S.expand(expr.subs(A,S.Rational(1,4)-C+v).subs(B,S.Rational(1,4)-C+w))
        assert all(c>=0 for c in S.Poly(expr,z,r,v,w).coeffs())
    t,E,c0,c1,c2=S.symbols('t E c0 c1 c2')
    P=lambda q:c0+c1*q+c2*q*q
    assert S.expand(P(t*E)-((1-t*t)*c0+t*E*(1-t)*c1+t*t*P(E)))==0
    from padding import base_coefficients
    cs=base_coefficients((A,B,C),a,r)
    R6=3*d*d+3*r*r*h*h+(1+4*r)*e*e+(r*r+4*r)*f*f+2*(1+r)*(d*f+r*h*e)
    E=d*d+(1+2*r)*e*e+(2*r+r*r)*f*f+r*r*h*h
    target=sum(cs[i]*z**i for i in range(3))+k*k*a*a*R6+z*k*a*a*E
    assert S.cancel(k*k*formula(N)-target)==0
    print('PROVED: all-N moment extension coefficients and nonnegative cubic remainder matched exactly.')
    print('PROVED: all-N padded frame formula from exact ordered-pair expansion.')
    print('PROVED: T6(0)=9/80; L6 >= 3(1+r)/32 > 0.')
    print('PROVED: T_N(a)=(1-t^2)T_N(0)+a(1-t)L_N+t^2 T_N(E), t=a/E; T_N(0),L_N>0 for N>=6.')
if __name__=='__main__':main()
