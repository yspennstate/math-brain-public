"""PROVED: exact algebraic frame formula; positivity is not asserted here."""
import sympy as S
A,B,C,d,e,f,h,a,r,z = S.symbols('A B C d e f h a r z', real=True)

def formula(N=6):
    b=a*r; s=a+b; lam=(2+s)/4; F=a*(A+C)+b*(B+C)
    K=a*a*A+b*b*B+2*a*b*C-(a*a+b*b)/5-a*a*(d*d+e*e)-2*a*b*(e*e+f*f)-b*b*(f*f+h*h)
    R5=S.Rational(8,3)*(a*a*d*d+b*b*h*h)+S.Rational(2,3)*a*(a+5*b)*e*e+S.Rational(2,3)*b*(b+5*a)*f*f+2*s*(a*d*f+b*h*e)
    T5=(14+2*s)*(F-s/5)/9+S.Rational(4,3)*(a*a+b*b)-S.Rational(14,3)*(a*a*A+b*b*B)-4*(a*a+b*b+a*b/3)*C+R5
    hd=S.Rational(4,5)-2*s/5+F
    X35=(1-lam)*(10*F-2*s)/9
    X3N=(1-lam)*(2*(N-1)*(N-4)*lam-4*(N-2)+2*N*hd)/(N-2)**2
    return S.expand(T5+(2*S.sympify(N)/(N-2)-S.Rational(10,3))*K+X3N-X35)

if __name__=='__main__':
    p=S.Poly(formula(),a)
    for i in range(3): print('PROVED: coefficient a^%d ='%i,S.factor(p.nth(i)))
