import sympy as sp

eps=sp.symbols("eps")
A,B,d,c,s,t,x,h=sp.symbols("A B d c s t x h", real=True)
C,S=sp.symbols("C S", real=True)

q2=1+d*eps**2
q=sp.sqrt(q2)
r=q2*(1+A*eps)*c**2 + (1/(1+A*eps))*(s+q*B*eps*c)**2
ell=sp.series(sp.log(r), eps, 0, 3).removeO()

coef1=sp.simplify(sp.together(ell.coeff(eps,1)).subs(c**2+s**2,1).subs(s**2,1-c**2))
coef2=sp.simplify(sp.together(ell.coeff(eps,2)).subs(c**2+s**2,1).subs(s**2,1-c**2))

Ccs=2*c**2-1
Scs=2*c*s
want1=A*Ccs+B*Scs
want2=(sp.Rational(1,2)*A**2*(1-Ccs-Ccs**2)
       -A*B*Scs*(1+Ccs)
       +sp.Rational(1,2)*B**2*Ccs*(1+Ccs)
       +sp.Rational(1,2)*d*(1+Ccs))

assert sp.simplify((coef1-want1).subs(s**2,1-c**2)) == 0
assert sp.simplify(sp.expand(coef2-want2).subs(s**2,1-c**2)) == 0

# Leading beta=4 moments:
# E A = 1/(8j), E A^2 = E B^2 = 1/(2j), q_j^2-1 = 1/j.
mean_coeff = (C*sp.Rational(1,8)
    + sp.Rational(1,2)*(1-C-C**2)*sp.Rational(1,2)
    + sp.Rational(1,2)*C*(1+C)*sp.Rational(1,2)
    + sp.Rational(1,2)*(1+C))
var_coeff = sp.Rational(1,2)*(C**2+S**2)
mean_coeff = sp.factor(mean_coeff)
var_coeff = sp.factor(var_coeff.subs(S**2,1-C**2))
cgf_coeff = sp.factor(t*mean_coeff+t**2*var_coeff/2)

assert sp.simplify(mean_coeff-(sp.Rational(3,4)+sp.Rational(5,8)*C)) == 0
assert sp.simplify(var_coeff-sp.Rational(1,2)) == 0
assert sp.simplify(cgf_coeff-(sp.Rational(3,4)*t+sp.Rational(1,4)*t**2+sp.Rational(5,8)*t*C)) == 0

# Inf-convolution of the beta=4 bulk rate with the positive-prefix cost 2h.
a=sp.Rational(3,4)
rate=2*h+(x-h-a)**2
hstar=sp.solve(sp.Eq(sp.diff(rate,h),0),h)[0]
assert sp.simplify(hstar-(x-sp.Rational(7,4))) == 0
assert sp.solve(sp.Eq(hstar,0),x)[0] == sp.Rational(7,4)
assert sp.simplify(sp.expand(rate.subs(h,0))-(x-a)**2) == 0
assert sp.simplify(sp.expand(rate.subs(h,hstar))-(2*x-sp.Rational(5,2))) == 0

print("PASS exact zero-energy amplitude Taylor polynomial")
print("PASS beta=4 conditional mean = 3/4 + (5/8) cos(2theta)")
print("PASS beta=4 leading conditional variance = 1/2")
print("PASS one-step CGF = (3t/4+t^2/4+(5t/8)cos(2theta))/j + O(j^-3/2)")
print("PASS inf-convolution switch x*=7/4")
print("PASS rate: (x-3/4)^2 for x<=7/4; 2x-5/2 for x>=7/4")
