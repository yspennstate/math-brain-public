"""Exact vertex/rectangle certificate for a region of the 5+1 case."""
import itertools
import sympy as s

A,B,C,a,r,u=s.symbols('A B C a r u')
# Every constraint is >=0. All have elementary proofs in RESULT.md.
constraints=[A-s.Rational(1,5),B-s.Rational(1,5),s.Rational(13,20)-A,s.Rational(13,20)-B,C,s.Rational(3,10)-C,s.Rational(4,5)-A-C,s.Rational(4,5)-B-C,s.Rational(7,5)-A-B-2*C,A+B-2*C]

def vertices():
    out=set()
    for ids in itertools.combinations(range(len(constraints)),3):
        M,bb=s.linear_eq_to_matrix([constraints[i] for i in ids],[A,B,C])
        if M.det()==0:continue
        v=tuple(M.inv()*bb)
        sub=dict(zip([A,B,C],v))
        if all(e.subs(sub)>=0 for e in constraints):out.add(v)
    return sorted(out)

def lower(c):
    b=a*r;ss=a+b;lm=(2+ss)/4;F=a*(A+C)+b*(B+C)
    T5=(14+2*ss)/9*(F-ss/5)+s.Rational(4,3)*(a*a+b*b)-s.Rational(14,3)*(a*a*A+b*b*B)-4*(a*a+b*b+a*b/3)*C
    K=a*a*A+b*b*B+2*a*b*C-(a*a+b*b)/5
    k=4+u;N=k+2
    hd=s.Rational(4,5)-s.Rational(2,5)*ss+F
    X35=(1-lm)/9*(10*F-2*ss)
    X3N=(1-lm)/k**2*(2*(N-1)*(N-4)*lm-4*k+2*N*hd)
    # The cubic contribution only increases from N=6 to larger N.
    return s.Poly(s.expand(s.cancel(k*k*(T5+(2*N/k-s.Rational(10,3))*K+X3N-X35-a*a*c*C))),u)

def minquad(expr,var,lo,hi):
    poly=s.Poly(expr,var);c2=poly.coeff_monomial(var**2);c1=poly.coeff_monomial(var)
    values=[expr.subs(var,lo),expr.subs(var,hi)]
    if c2>0:
        critical=-c1/(2*c2)
        if lo<critical<hi:values.append(expr.subs(var,critical))
    return min(values)

def main():
    vs=vertices(); print('PROVED: moment vertices',len(vs))
    amin=s.Rational(11,25);minimum=None
    for lo,hi,c in [(0,s.Rational(1,10),(1-10*r)/3),(s.Rational(1,10),1,0)]:
        L=lower(c)
        for v in vs:
            for uc in L.all_coeffs():
                P=s.Poly(uc.subs(dict(zip([A,B,C],v))),a)
                # Degree-two Bernstein coefficients in a/amin.
                c0=P.coeff_monomial(1);c1=P.coeff_monomial(a)
                bernstein=[c0,c0+c1*amin/2,P.as_expr().subs(a,amin)]
                for coefficient in bernstein:
                    m=minquad(coefficient,r,lo,hi)
                    minimum=m if minimum is None else min(minimum,m)
                    assert m>0
    print('PROVED: T_N > 0 for a five-vertex double carrier with internal a<=11/25, padded to N>=6; coefficient margin',minimum)
if __name__=='__main__':main()
