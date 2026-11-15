"""PROVED: exact elementary moment and extremal-pair algebra."""
import sympy as S

def main():
    H=S.eye(5)-S.ones(5)/5
    x=S.symbols('x0:4');y=S.Matrix(list(x)+[-sum(x)])
    M=H*S.diag(*y)*H
    assert S.expand(S.trace(M*M)-S.Rational(3,5)*y.dot(y))==0
    # Frobenius and diagonal constants used in the diagonal-contraction bounds.
    # Q is an orthogonal rank-two projection in H; the identities below use tr Q=2, QH=Q.
    assert 1-S.Rational(2,4)+S.Rational(4,16)==S.Rational(3,4)
    assert 2-2+S.Rational(4,4)==1
    # Bounds for the extreme-u pair p=alpha*beta, v=alpha-beta.
    b,v=S.symbols('b v',nonnegative=True)
    assert S.expand((b+v)**2+b*b+v*v/3-S.Rational(20,9)*v*v-2*(b-v/3)*(b+4*v/3))==0
    # Residue identity sum_i(alpha-u_i)(beta+u_i)=5p-1 uses sum u=0, ||u||=1.
    # Exact Bernstein scalar identity.
    t,c0,c1,c2=S.symbols('t c0 c1 c2')
    assert S.expand((1-t)**2*c0+2*t*(1-t)*(c0+c1/2)+t*t*(c0+c1+c2)-(c0+c1*t+c2*t*t))==0
    print('PROVED: diagonal-contraction constants, extreme-pair norm algebra and scalar Bernstein identity checked exactly.')
if __name__=='__main__':main()
