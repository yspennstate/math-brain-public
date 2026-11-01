from fractions import Fraction as F
import json
from pathlib import Path
import sympy as sy
mult=[1,3,3,1]
w=[19,241,2299,361]
v=[343,637,1183,2197]
u=[-39,-241,121,399]
b=[-207,147,-87,27]
p=[F(k,8000) for k in w]
mu=[F(k,8000) for k in v]
g=[F(k,800) for k in u]
h=[F(k,40) for k in b]
r=[p0/m0 for p0,m0 in zip(p,mu)]
FI=sum(m*g0*g0/p0 for m,g0,p0 in zip(mult,g,p))
def Q(s):
    fisher=sum(m*g0*g0/m0/(r0+s)**2 for m,g0,m0,r0 in zip(mult,g,mu,r))
    frozen=sum(m*h0/(r0+s) for m,h0,r0 in zip(mult,h,r))
    return fisher-frozen,fisher,frozen
def R(s):
    fisher=sum(2*s*m*g0*g0/m0/(r0+s)**3 for m,g0,m0,r0 in zip(mult,g,mu,r))
    frozen=sum(s*m*h0/(r0+s)**2 for m,h0,r0 in zip(mult,h,r))
    return fisher-frozen,fisher,frozen
lim=sum(m*(g0*g0/m0+h0*r0) for m,g0,m0,h0,r0 in zip(mult,g,mu,h,r))
s=sy.symbols('s',nonnegative=True)
qs=sum(m*vi*(sy.Rational(ui**2,80)/(wi+s*vi)**2-sy.Rational(bi,40)/(wi+s*vi)) for m,wi,vi,ui,bi in zip(mult,w,v,u,b))
num,den=sy.fraction(sy.factor(qs))
poly=sy.Poly(num,s)
shiftpoly=sy.Poly(sy.expand(num.subs(s,s+5)),s)
print('FI',FI)
print('Q5, fisher density, frozen density',Q(F(5)))
print('Q5 < -1/20',Q(F(5))[0] < F(-1,20))
print('R5',R(F(5)))
print('limit s2 Q',lim)
print('factored Q',sy.factor(qs))
print('numerator shifted by5 coefficients',shiftpoly.all_coeffs())
# Independent determinant jets, with all 8 atoms retained.
t=sy.symbols('t',real=True)
K=sy.Matrix([[sy.Rational(13,20),-sy.Rational(3,10),-sy.Rational(3,10)],[-sy.Rational(3,10),sy.Rational(13,20),-sy.Rational(3,10)],[-sy.Rational(3,10),-sy.Rational(3,10),sy.Rational(13,20)]])
A=sy.eye(3)/2+sy.I*sy.Matrix([[0,1,-1],[-1,0,1],[1,-1,0]])
atoms=[]
for mask in range(8):
    bits=[bool(mask>>i&1) for i in range(3)]
    card=sum(bits)
    out=sy.diag(*[0 if z else 1 for z in bits])
    pol=sy.expand((-1)**(3-card)*(K+t*A-out).det())
    vals=[pol.subs(t,0),sy.diff(pol,t).subs(t,0),sy.diff(pol,t,2).subs(t,0)]
    expect=[sy.Rational(p[card].numerator,p[card].denominator),sy.Rational(g[card].numerator,g[card].denominator),sy.Rational(h[card].numerator,h[card].denominator)]
    assert vals==expect,(mask,vals,expect)
    atoms.append({'mask':mask,'polynomial':str(pol),'jet':[str(z) for z in vals]})
assert sy.simplify(sum(sy.sympify(z['polynomial']) for z in atoms)-1)==0
assert FI==F(300,19)
assert Q(F(5))[0]<F(-1,20)
assert R(F(5))[0]<F(-3,100)
assert all(z<0 for z in shiftpoly.all_coeffs())
assert (-num/300).subs(s,2)==-123086562892959921901875
assert (-num/300).subs(s,3)==1348009347580657745002496
assert 27*241**3 < 19**2*11**6 < 64*241**3
assert F(14400,43681)<F(1,3)
# Rational logarithm intervals from atanh series; inputs are >0.
def log_bounds(x,N=120):
    z=(x-1)/(x+1)
    if z<0:
        lo,hi=log_bounds(1/x,N)
        return -hi,-lo
    lo=2*sum(z**(2*k+1)/F(2*k+1) for k in range(N))
    tail=2*z**(2*N+1)/F(2*N+1)/(1-z*z)
    return lo,lo+tail
cl,ch=log_bounds(F(58081,43681),20)
# Reduce tau logarithm to ratio/32 then five log2 terms, giving rapid convergence.
ta=F(19**2*11**6,241**3)
t0l,t0h=log_bounds(ta/32,20);l2,h2=log_bounds(F(2),20)
tl,th=t0l+5*l2,t0h+5*h2
fl,fh=-F(9,2)*ch+F(27,40)*tl,-F(9,2)*cl+F(27,40)*th
assert fl>F(21,40) and fh<F(81,20)
results={
    'K':[[str(z) for z in row] for row in K.tolist()],
    'A':[[str(z) for z in row] for row in A.tolist()],
    'atoms':atoms,
    'fisher':str(FI),
    'Q_at_5':[str(z) for z in Q(F(5))],
    'R_at_5':[str(z) for z in R(F(5))],
    'tail_limit_s2_Q':str(lim),
    'Q_factored':str(sy.factor(qs)),
    'numerator_shift_5_coefficients':[str(z) for z in shiftpoly.all_coeffs()],
    'c_interval':[float(cl),float(ch)],
    'tau_interval':[float(tl),float(th)],
    'frozen_curvature_interval':[float(fl),float(fh)],
    'negative_entropy_curvature_interval':[float(FI-fh),float(FI-fl)],
}
Path('computations/C046/exact_results.json').write_text(json.dumps(results,indent=2)+'\n')
print('frozen rigorous interval',float(fl),float(fh),'negative H interval',float(FI-fh),float(FI-fl))
print('all exact assertions passed')
