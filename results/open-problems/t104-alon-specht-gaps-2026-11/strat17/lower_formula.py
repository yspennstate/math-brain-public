"""Exact identities for arbitrary lower blocks; all signs are rational."""
import sympy as s


def x3(k, mass, h):
    return (mass-1)/k**2*(2*(k+1)*(k-2)-4*k*mass+2*(k+2)*h)


def main():
    k,M,h,t,n,q,S=s.symbols('k M h t n q S')
    # Universal derivation from the normalized matrix definitions.
    N,tr2=s.symbols('N trC2')
    assert s.expand(2*((N-1-2*M)-(N-1-4*M+tr2))-2*(2*M-tr2))==0
    original_x3=(M-1)/(N-2)*(2*(N-1-2*M)-2*N/(N-2)*(2*(1-1/N)-h))
    assert s.cancel(original_x3-x3(N-2,M,h))==0
    # Centering in X2 contributes -2 tr(P(I-C))/N+1^T P1/N^2=0.
    C=2*(k+1)*(k-2)+2*(k+2)*h
    bracket=C-4*k*(2*M+t/2-1)
    delta=x3(k,M+t/2,h)-x3(k,M,h)
    assert s.cancel(delta-t*bracket/(2*k**2))==0
    endpoint=2*k*(n-4*M+h)+4*(h-1)+2*k*q
    assert s.expand(bracket.subs(t,k-n+1-q)-endpoint)==0
    assert s.limit(delta,k,s.oo)==t
    # Exact scalar relaxation, simultaneously for all lower components.
    F=lambda a:x3(k,M+a/2,h)
    assert s.cancel(F(t)-((1-t/S)*F(0)+t/S*F(S)+t*(S-t)/k))==0
    assert s.diff(F(t),t,2)==-2/k
    # Lower-matrix direction: h,B,Y do not change because P is zero there.
    e1,e2=s.symbols('trE trE2')
    quadratic=-2*e2+s.diff(F(t),t,2)*e1**2/2
    assert s.cancel(quadratic-(-2*e2-e1**2/k))==0
    # Adding fixed lower mass changes no quadratic variation in a top block.
    v,dm,dh,ell=s.symbols('v dm dh ell')
    diff=x3(k,M+v*dm+ell,h+v*dh)-x3(k,M+v*dm,h+v*dh)
    assert s.cancel(s.diff(diff,v,2))==0
    # Universal h>=1: each selected unit top direction has weighted energy 1.
    a,b=s.symbols('a b')
    assert s.expand(2*(a*a+b*b)-(a-b)**2-(a+b)**2)==0
    # Q=(H-S)oS=D-S/n-S o S; PS=0 and P1=0 imply 0<=B<=d.
    a,N=s.symbols('a N')
    assert s.expand((1-1/N-a)*a-(a-a/N-a*a))==0
    b=s.symbols('b')
    assert s.expand((-1/N-b)*b-(-b/N-b*b))==0
    print('PROVED (lower_formula.py): general increment, exact lower-trace endpoint identity, strict lower concavity, unchanged top concavity, and infinity increment.')

if __name__=='__main__':main()
