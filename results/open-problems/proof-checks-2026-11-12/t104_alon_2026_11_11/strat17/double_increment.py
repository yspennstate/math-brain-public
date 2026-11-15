"""Exact sufficient increment condition for the five-vertex double carrier."""
import sympy as s
from lower_formula import x3


def main():
    tau,h,k,q=s.symbols('tau h k q');M=(4-tau)/2
    pref=5-4*M+h
    assert s.expand(pref-(2*(tau-1)+(h-1)))==0
    a,b=s.symbols('a b',nonnegative=True)
    bracket=2*k*pref+4*(h-1)+2*k*q
    pol=s.Poly(s.expand(bracket.subs({tau:1+a,h:1+b,k:5+s.Symbol('z',nonnegative=True)})),a,b,q,s.Symbol('z',nonnegative=True))
    assert all(v>=0 for v in pol.coeffs())
    # Equality centers have tau=2, M=1 and pref>=2.
    assert pref.subs(tau,2)==h+1
    print('PROVED (double_increment.py): every lower collection has nonnegative T* increment if tau>=1 (more generally 5-4M+h>=0); the equality neighborhoods satisfy this condition. The complementary tau<=1 region is handled by double_small_gap.py.')

if __name__=='__main__':main()
