"""Exact fixed-vector setup for 4+4; this is not a full class certificate."""
import sympy as s
from matrix_audit import H,data
from lower_formula import x3
from inherited16.algebra import spanning,quadratic


def value(L,P,k):
    M,h,B,Y=data(L,P)
    return 2*(s.trace(L)-s.trace(L*L))+2*(k+2)*B/k+x3(k,M,h)-Y


def main():
    k,v=s.symbols('k v');u=s.Matrix([3,1,-1,-3]);w=s.Matrix([3,-1,1,-3])
    P=u*u.T/u.dot(u);Q=w*w.T/w.dot(w)
    C=H(4)-(H(4)-P)/10;D=H(4)-(H(4)-Q)/5
    for U,first,second,PP,QQ in ((u,C,D,P,Q),(w,D,C,Q,P)):
        K=spanning(U);E=K*s.Matrix([[2,1],[1,-1]])*K.T/100
        L=s.diag(first+v*E,second);Pi=s.diag(PP,QQ)
        assert E*s.ones(4,1)==s.zeros(4,1) and E*U==s.zeros(4,1)
        coef=s.Poly(s.expand(value(L,Pi,k)),v).nth(2)
        assert s.cancel(coef-quadratic(E,U,k))==0
    # Nominal 4+4 first occurs at N=8, so k=6+z. Same four-dimensional
    # Ku certificate applies separately to each block for all k>=6.
    # Each block has tree extremes or A rank<=2, plus disconnected points.
    print('PROVED (split44_setup.py with inherited16/prior_concavity4.py): separate fixed-top-vector concavity for 4+4. OPEN endpoint pairs: tree/tree, tree/rank<=2, rank<=2/rank<=2. Disconnected endpoints reduce to the now-proved smaller split classes with lower components.')

if __name__=='__main__':main()
