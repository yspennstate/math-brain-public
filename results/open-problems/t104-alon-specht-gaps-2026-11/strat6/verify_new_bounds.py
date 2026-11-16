"""PROVED: exact symbolic replay of edge variance and Bessel certificates."""
import sympy as s

ui,wi,uj,wj=s.symbols('ui wi uj wj')
a,b,la,t=s.symbols('a b lambda t')
A,B,C,d,e,f,h=s.symbols('A B C d e f h')
known={(0,0):5,(1,0):0,(0,1):0,(2,0):1,(0,2):1,(1,1):0,
       (4,0):A,(0,4):B,(2,2):C,(3,0):d,(2,1):e,(1,2):f,(0,3):h}
def moment(i,j):
    return known.get((i,j),s.Symbol('m'+str(i)+str(j)))
def pair_sum(poly):
    ans=0
    for (i,j,k,l),coef in s.Poly(s.expand(poly),ui,wi,uj,wj).terms():
        ans+=coef*(moment(i,j)*moment(k,l)-moment(i+k,j+l))/2
    return s.expand(ans)
qi,qj=ui*ui+wi*wi,uj*uj+wj*wj
qij=ui*uj+wi*wj
weight=la/5+a*ui*uj+b*wi*wj
K=A+B+2*C
F=a*(A+C)+b*(B+C)
Na=a*(d*d+2*e*e+f*f)+b*(e*e+2*f*f+h*h)
Ja=a*(d+f)**2+b*(e+h)**2
Z=a*(moment(6,0)+2*moment(4,2)+moment(2,4))+b*(moment(4,2)+2*moment(2,4)+moment(0,6))
S=a+b-F-2*la/5
assert s.expand(pair_sum(weight)-(2*la-(a+b)/2))==0
assert s.expand(2*pair_sum(weight*qij)-S)==0
assert s.expand(2*pair_sum(weight*(qi*qj-qij*qij))-Ja+Na-2*la/5)==0
expected=Na-Z+la*(2-K)/5-2*t*S+2*t*t
assert s.expand((2*pair_sum(weight*(qij-t)**2)-expected).subs(la,(2+a+b)/4))==0
assert s.expand(expected.subs(t,S/2)-Na+Z-la*(2-K)/5+S*S/2)==0
print('PROVED: edge variance identity and the determinant-square edge identity matched exactly.')

# Match the two 2-by-2 residual blocks used in every cell.
r,tn,tj,td,z1,z2,z3,z4=s.symbols('r tn tj td z1 z2 z3 z4')
R=s.Rational(8,3)*d*d+s.Rational(8,3)*r*r*h*h
R+=s.Rational(2,3)*(1+5*r)*e*e+s.Rational(2,3)*r*(r+5)*f*f
R+=2*(1+r)*(d*f+r*h*e)
Nr=d*d+(2+r)*e*e+(1+2*r)*f*f+r*h*h
Jr=(d+f)**2+r*(e+h)**2
x,y=tn-td,tj+td
residual=R-x*Nr-y*Jr+z1*(d*d+e*e)+z2*(f*f+h*h)+z3*e*e+z4*f*f
from moment_bounds import blocks
df,eh=blocks(r,tn,tj,td,(z1,z2,z3,z4))
expanded=df[0]*d*d+2*df[1]*d*f+df[2]*f*f
expanded+=eh[0]*e*e+2*eh[1]*e*h+eh[2]*h*h
assert s.expand(residual-expanded)==0
print('PROVED: every residual-block coefficient and Bessel penalty matched exactly.')

# The two strengthened lower bounds at equal gaps.
g,k=s.symbols('g k')
sig=g*(s.Rational(9,5)-k)-s.Rational(1,5)
base=70*k-28+g*(112-190*k)
n=g*k*k/2-(1+g)*(2-k)/10+sig*sig/2
j=g*k*k/2-(1+g)*(4-k)/10+sig*sig/2
pn=15*g*k*k+(73-187*g)*k+106*g-34+15*sig*sig
pnj=60*g*k*k+(82-178*g)*k+70*g-70+60*sig*sig
assert s.expand(pn-base-30*n)==0
assert s.expand(pnj-base-30*n-90*j)==0
print('PROVED: strengthened equal-gap polynomials matched the radial formula exactly.')
