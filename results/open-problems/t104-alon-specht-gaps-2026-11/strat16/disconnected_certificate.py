"""Exact padding comparison for the extra edge in a disconnected extreme point."""
import sympy as s


def main():
    g,t,z=s.symbols('g t z',nonnegative=True);k=5+z
    mass=(3-g)/2;h=(7-g)/6;delta=t/2
    C=2*(k+1)*(k-2)+2*(k+2)*h
    def X3(m):return (m-1)*(C-4*k*m)/k**2
    bracket=s.expand(C-4*k*(2*mass+delta-1))
    assert s.cancel(X3(mass+delta)-X3(mass)-delta*bracket/k**2)==0
    q=s.symbols('q',nonnegative=True)
    expected=s.Rational(7,3)+s.Rational(31,3)*z+2*z*z+(s.Rational(53,3)+s.Rational(11,3)*z)*g+(10+2*z)*q
    assert s.expand(bracket.subs(t,1-q)-expected)==0
    assert all(c>0 for c in s.Poly(expected,z,g,q).coeffs())
    # A lower edge also adds X1*=2t(1-t), nonnegative on [0,1].
    # It vanishes at the extreme endpoints t=0,1 used in the reduction.
    total_increment=2*t*(1-t)+X3(mass+delta)-X3(mass)
    assert s.cancel(total_increment-2*t*(1-t)-delta*bracket/k**2)==0
    # More generally let s0=tr L_lower on r lower vertices. Since each
    # component has a zero eigenvalue and all its eigenvalues are <=1,
    # s0<=r-1<=k-4. This covers arbitrary nontrivial lower components.
    s0=s.symbols('s0',nonnegative=True)
    general_bracket=s.expand(C-4*k*(2*mass+s0/2-1))
    general=s.expand(general_bracket.subs(s0,k-4-q))
    expected_general=s.Rational(7,3)+z/3+(s.Rational(53,3)+s.Rational(11,3)*z)*g+(10+2*z)*q
    assert s.expand(general-expected_general)==0
    assert all(c>0 for c in s.Poly(expected_general,z,g,q).coeffs())
    # Selected rank-two S5=0 equality on a disconnected five-part:
    # X1=0 makes L a graph projection. Its rank including the external edge
    # is 2, 3 or 4; every selected carrier has degree >=1/2, hence h>=1.
    # The X3 bracket is strictly positive for ranks 3 and 4, k>=5.
    for rank in (3,4):
        f=s.Poly(s.expand(2*(k+1)*(k-2)-2*k*rank+2*(k+2)),z)
        assert all(c>0 for c in f.coeffs())
    print('PROVED (disconnected_certificate.py): split edge+triangle remains nonnegative with arbitrary lower components, k>=5 and infinity, strictly positive for any nontrivial lower component; selected S5=0 equality on disconnected five-parts requires two equal edges.')

if __name__=='__main__':main()
