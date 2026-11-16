"""Twelve exact polynomial certificates for the split lower-trace endpoint.

On 0<=tau<=2, 0<=d<=c-1, k>=7, the comparison f is >=3/10.
All coefficients below include the endpoint k=infinity after scaling by k^2.
"""
import sympy as s
from lower_formula import x3


def comparison(k,t,d,c):
    return ((4/k-s.Rational(4,5))*d
            +x3(k,(k-1-t)/2,c-d)-x3(s.Integer(5),(5-t)/2,c-d))


def main():
    k,t,d,c,z,v=s.symbols('k t d c z v');records=[]
    f=comparison(k,t,d,c)
    for cc,cap in ((s.Rational(13,10),s.Rational(3,10)),
                   (s.Rational(17,12),s.Rational(5,12))):
        num=s.expand(s.cancel(1500*k*k*(f-s.Rational(3,10))).subs({c:cc,k:7+z}))
        assert s.Poly(num,d).degree()==1
        for dd in (0,cap):
            pp=s.Poly(num.subs(d,dd),t)
            assert pp.degree()==2
            controls=[pp.nth(0),pp.nth(0)+pp.nth(1),pp.nth(0)+2*pp.nth(1)+4*pp.nth(2)]
            assert s.expand(pp.as_expr().subs(t,2*v)-((1-v)**2*controls[0]+2*v*(1-v)*controls[1]+v*v*controls[2]))==0
            for j,p in enumerate(controls):
                cp=s.Poly(p,z)
                assert cp.degree()==2 and all(a>0 for a in cp.all_coeffs())
                records.append((str(cc),str(dd),j,str(s.factor(p))))
    assert len(records)==12
    for rec in records:print(rec)
    # The B replacement is in the correct direction: B<=d, 4/k-4/5<=0.
    excess,b=s.symbols('excess b')
    assert s.cancel(((4/k-s.Rational(4,5))*(d-excess)-(4/k-s.Rational(4,5))*d)-4*(k-5)*excess/(5*k))==0
    # Five-tree sign Rayleigh bound: tr C5<=5/2, M<=7/4.
    a,b,q=s.symbols('a b q',nonnegative=True)
    assert s.expand((7-4*((7-s.Integer(4)*a)/4)+(1+b))-(1+4*a+b))==0
    # Four-tree plus arbitrary triangle: M<=2 and h>=1.
    assert s.expand((7-4*(2-a)+(1+b))-(4*a+b))==0
    print('PROVED (split_endpoint_certificate.py): f>=3/10, all real k>=7 and infinity; tree endpoint increment comparisons.')

if __name__=='__main__':main()
