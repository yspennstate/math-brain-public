"""PROVED: exact identities behind the edge-sum bounds and equal-gap theorem."""
import sympy as s
ui,wi,uj,wj=s.symbols('ui wi uj wj')
a,b,la=s.symbols('a b lambda')
A,B,C,d,e,f,h=s.symbols('A B C d e f h')
known={(0,0):5,(1,0):0,(0,1):0,(2,0):1,(0,2):1,(1,1):0,
       (4,0):A,(0,4):B,(2,2):C,(3,0):d,(2,1):e,(1,2):f,(0,3):h}
def moment(i,j):return known.get((i,j),s.Symbol('m'+str(i)+str(j)))
def pair_sum(poly):
    ans=0
    for (i,j,k,l),coef in s.Poly(s.expand(poly),ui,wi,uj,wj).terms():
        ans+=coef*(moment(i,j)*moment(k,l)-moment(i+k,j+l))/2
    return s.expand(ans)
qi,qj=ui*ui+wi*wi,uj*uj+wj*wj
qij=ui*uj+wi*wj
weights=la/5+a*ui*uj+b*wi*wj
K=A+B+2*C
Na=a*(d*d+2*e*e+f*f)+b*(e*e+2*f*f+h*h)
Ja=a*(d+f)**2+b*(e+h)**2
Z=a*(moment(6,0)+2*moment(4,2)+moment(2,4))+b*(moment(4,2)+2*moment(2,4)+moment(0,6))
assert s.expand(2*pair_sum(weights*qij*qij)-Na+Z-la*(2-K)/5)==0
assert s.expand(2*pair_sum(weights*qi*qj)-Ja+Z-la*(4-K)/5)==0
R=s.Rational(8,3)*a*a*d*d+s.Rational(8,3)*b*b*h*h+s.Rational(2,3)*a*(a+5*b)*e*e+s.Rational(2,3)*b*(b+5*a)*f*f+2*(a+b)*(a*d*f+b*h*e)
rem=s.Rational(8,3)*(a-b)*(a*d*d+(a+b)*e*e+b*f*f)
assert s.expand(R-(5*b/3-a)*Na-(a+b)*Ja-rem)==0
print('PROVED: both nonnegative edge-sum identities and the cubic remainder identity checked exactly.')

# The lower bound used in the quartic SOS has a concave dependence on r.
v,D,E,F,H,I,J=s.symbols('v D E F H I J')
Q=s.Rational(2,9)*(A+B+2*C-s.Rational(2,5))-s.Rational(4,3)*C+s.Rational(10,3)*(e*e+f*f)+2*d*f+2*h*e
qlower=-(A+B-s.Rational(2,5))/18-s.Rational(8,9)*C
qcert=s.Rational(5,18)*((d+s.Rational(18,5)*f)**2+(h+s.Rational(18,5)*e)**2)+s.Rational(1,90)*(e*e+f*f)
qcert+=s.Rational(5,18)*(A+B-s.Rational(2,5)-d*d-e*e-f*f-h*h)
assert s.expand(Q-qlower-qcert)==0
P=s.Rational(58,45)-s.Rational(40,9)*A-s.Rational(34,9)*C+s.Rational(8,3)*d*d+s.Rational(2,3)*e*e+2*d*f
plower=s.Rational(58,45)-s.Rational(40,9)*A-s.Rational(299,72)*C
assert s.expand(P-plower-s.Rational(8,3)*(d+s.Rational(3,8)*f)**2-s.Rational(2,3)*e*e-s.Rational(3,8)*(C-f*f))==0
concavity=s.Rational(73,18)-s.Rational(565,36)/4-s.Rational(7,12)*s.Rational(7,30)
assert concavity==-s.Rational(1,240)
print('PROVED: coefficient lower bounds and the -1/240 concavity bound checked exactly.')

k,g=s.symbols('k g')
G=(209+3*s.sqrt(305))/476
kstar=(s.sqrt(305)-5)/10
pn=15*g*k*k+(73-187*g)*k+106*g-34
pnj=60*g*k*k+(82-178*g)*k+70*g-70
assert s.simplify(pn.subs({g:G,k:kstar}))==0
assert s.simplify(pnj.subs({g:G,k:kstar}))==0
assert s.Rational(6,5)<kstar<s.Rational(5,4)
assert s.Rational(1,2)<G<1
print('PROVED: equal-gap split point and threshold identities checked exactly.')
