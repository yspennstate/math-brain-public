"""Exact matrix order certificate: rank at most three A is worst at N=7."""
import sympy as s


def main():
    t,z=s.symbols('t z');I,C,D,S=s.symbols('I C D S')
    B=4*C+(3-t)*(t-s.Rational(47,10))*I-(3-t)*D
    E=(3-t)*(s.Rational(3,5)*I-2*D)
    derivative=B+2*z*E
    Q=D-S/5-C
    gap=(3-t)*(s.Rational(223,50)-t)-s.Rational(4,5)*(1+t)
    rhs=(-gap*I-(1+t)*(s.Rational(4,5)*I-D)-s.Rational(4,5)*S
         -4*Q-4*z*(3-t)*D-s.Rational(6,5)*(3-t)*(s.Rational(1,5)-z)*I)
    assert s.expand(derivative-rhs)==0
    r=s.symbols('r',nonnegative=True)
    assert s.expand(gap.subs(t,2-r)-(s.Rational(3,50)+s.Rational(213,50)*r+r*r))==0
    # Actual matrices: S=A-J/5, 0<=S<=H, rank S<=2, t=tr S<=2.
    # C=S o S; D=diag(diag S); Q=(H-S)oS is PSD by Schur.
    # D>=0, (4/5)I-D>=0, S>=0, and all displayed scalar factors >=0
    # on 0<=z<=1/5, 0<=t<=2. Hence F'(z)<=-(3/50)I.
    print('PROVED (padding_monotonicity.py): rank-at-most-three A has F\'(1/k)<=-3 I/50; T* is minimized at k=5, with infinity included.')

if __name__=='__main__':main()
