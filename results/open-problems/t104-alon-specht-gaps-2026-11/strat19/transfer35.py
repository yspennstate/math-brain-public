"""Transfer rank-at-most-three five-parts from the inherited 2+5 k=5 theorem."""
import sys,json
from pathlib import Path
from math import comb
import sympy as s
sys.path.insert(0,str(Path(__file__).resolve().parent/'inherited18'/'inherited17'))
from lower_formula import x3

def bernstein(p,variables,degrees):
    import itertools
    p=s.Poly(p,*variables);out=[]
    for ids in itertools.product(*(range(n+1) for n in degrees)):
        value=sum(coef*s.prod(s.Rational(comb(i,a),comb(n,a)) for i,a,n in zip(ids,es,degrees))
                  for es,coef in p.terms() if all(a<=i for a,i in zip(es,ids)))
        out.append((ids,value))
    # Reconstruct independently in the Bernstein basis.
    rebuilt=sum(value*s.prod(comb(n,i)*v**i*(1-v)**(n-i) for i,n,v in zip(ids,degrees,variables)) for ids,value in out)
    assert s.expand(rebuilt-p.as_expr())==0
    return out

def main():
    tau,d,l,u,v,k,r,a=s.symbols('tau d l u v k r a');records=[]
    # Five-part: C5=H5-S, rank S<=2, tau=tr S<=2,
    # d=sum u_i^2 S_ii<=3/10 and 0<=B5<=d (Schur product).
    # At k=6, changing B5's coefficient from k=5 costs at most 2d/15.
    balanced=-s.Rational(2,15)*d+x3(s.Integer(6),(6-tau)/2,s.Rational(22,15)-d)-x3(s.Integer(5),(5-tau)/2,s.Rational(13,10)-d)
    expected=(-390*d*tau-1230*d+225*tau*tau+317*tau+1099)/6750
    assert s.cancel(balanced-expected)==0
    # Affine d: both endpoints have nonnegative tau coefficients after the margin.
    for dd in (s.Integer(0),s.Rational(3,10)):
        p=s.Poly(s.expand((balanced-s.Rational(73,675)).subs(d,dd)),tau)
        assert all(c>=0 for c in p.all_coeffs())
        records.append({'corner':'balanced','d':str(dd),'Tstar_increment_margin':'73/675','coefficients':[str(c) for c in p.all_coeffs()]})
    # Path: l is its second eigenvalue, 0<=l<=1/3.
    # B3=l^2(3-l)/(6(1-l)); 2(tr C3-tr C3^2)-Y3=l(1-l)-6B3.
    B3=l*l*(3-l)/(6*(1-l))
    triangle=l*(1-l)-s.Rational(10,3)*B3
    path=triangle-s.Rational(2,15)*d+x3(s.Integer(6),(5+l-tau)/2,s.Rational(13,10)+l/6-d)-x3(s.Integer(5),(5-tau)/2,s.Rational(13,10)-d)
    # Independent cancellation of all unchanged five-part moments.
    v5,b5,y5=s.symbols('v5 b5 y5')
    old=2*(tau-v5)+s.Rational(14,5)*b5-y5+x3(s.Integer(5),(5-tau)/2,s.Rational(13,10)-d)
    new_balanced=2*(tau-v5)+s.Rational(8,3)*b5-y5+x3(s.Integer(6),(6-tau)/2,s.Rational(22,15)-d)
    new_path=2*(tau-v5)+triangle+s.Rational(8,3)*b5-y5+x3(s.Integer(6),(5+l-tau)/2,s.Rational(13,10)+l/6-d)
    assert s.cancel(new_balanced-old-balanced-s.Rational(2,15)*(d-b5))==0
    assert s.cancel(new_path-old-path-s.Rational(2,15)*(d-b5))==0
    for dd in (s.Integer(0),s.Rational(3,10)):
        p=s.cancel((1-l)*(path-s.Rational(1,20))).subs({l:u/3,tau:2*v,d:dd})
        controls=bernstein(p,(u,v),(3,2))
        assert all(value>0 for ids,value in controls)
        records.append({'corner':'path','d':str(dd),'Tstar_increment_margin':'1/20','Bernstein_controls':[[list(ids),str(value)] for ids,value in controls]})
    # Scale-free triangle identities from the standard p chart.
    p,g=s.symbols('p g');m=9*p*p*(s.Rational(1,2)-p)
    assert s.cancel((g*g*(s.Rational(1,6)-m)).subs({g:1/(3*p),p:1/(3*(1-l))},simultaneous=True).subs(p,1/(3*(1-l)))-B3)==0
    # Padding for all such 3+5 pairs, including intermediate triangles:
    # M>=3/2, h=22/15-d_total>=1, 0<=B<=d_total<=7/15.
    M,h,B,dt=s.symbols('M h B dt');X=s.expand(x3(1/r,M,h)+2*(1+2*r)*B)
    derivative=s.diff(X,r)
    upper=4*dt+(M-1)*(-s.Rational(10,3)-4*M+s.Rational(10,3)*h)
    assert s.expand(upper.subs({dt:B})-derivative-(s.Rational(4,3)-8*r)*(M-1)*(h-1))==0
    # Substitute M=3/2+a: upper decreases with a>=0 when 1<=h<=22/15.
    reduced=upper.subs({M:s.Rational(3,2)+a,h:s.Rational(22,15)-dt})
    at0=s.expand(reduced.subs(a,0))
    assert at0==-s.Rational(20,9)+s.Rational(7,3)*dt
    assert at0.subs(dt,s.Rational(7,15))==-s.Rational(17,15)
    assert s.expand(reduced-at0+4*a*a+a*(s.Rational(58,9)+s.Rational(10,3)*dt))==0
    Path('transfer35_checks.json').write_text(json.dumps({'checks':records,'negative_inverse_padding_derivative_margin':'17/15','inherited_rank_at_most_three_margin':'1/400000','new_path_margin':'20001/400000','balanced_margin':'73/675 + 1/400000'},indent=2)+'\n')
    print('PROVED (transfer35.py): rank(A5)<=3 transfers from 2+5 at k=5 with extra >=1/20 for path, >=73/675 for balanced triangle; inverse-padding derivative <=-17/15, k>=6 and infinity.')

if __name__=='__main__':main()
