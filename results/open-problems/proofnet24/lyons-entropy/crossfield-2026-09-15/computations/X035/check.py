"""Exact algebra checks for X035; finite diagnostics do not prove uniformity."""
from pathlib import Path
import json
import sympy as S
import mpmath as mp

eta, eps = S.symbols('eta eps', real=True)
j, k, ell = S.symbols('j k ell', positive=True)
theta = S.symbols('theta', real=True)
a, s, t, xr, xi, yr, yi, zr, zi = S.symbols(
    'a s t xr xi yr yi zr zi', real=True)
variables = (a, s, t, xr, xi, zr, zi, yr, yi)
x, y, z = xr+S.I*xi, yr+S.I*yi, zr+S.I*zi
AA = S.Matrix([[a,S.conjugate(x),S.conjugate(y)],
               [x,s,z],[y,S.conjugate(z),t]])
p, d = 1-eta, j*ell-k*k
KK = S.Matrix([[p,0,0],[0,eps*j,eps*k],[0,eps*k,eps*ell]])
U = S.Matrix([[S.Rational(3,5),-S.Rational(4,5),0],
              [S.Rational(4,5),S.Rational(3,5),0],[0,0,1]])
q, r = S.Rational(9,25), S.Rational(16,25)
physical = U*(KK+theta*AA)*U.T
count = 0
def check_zero(expr):
    global count
    answer = S.cancel(S.expand(expr))
    assert answer == 0, answer
    count += 1

moments = {0: S.Integer(1)}
for mask in range(1,8):
    ids = [i for i in range(3) if mask & (1<<i)]
    moments[mask] = S.Poly(physical.extract(ids,ids).det(),theta)
moments = {m: (v.as_expr() if hasattr(v,'as_expr') else v)
           for m,v in moments.items()}
atoms = {}
for mask in range(8):
    atoms[mask] = S.expand(sum(
        (-1)**((sup^mask).bit_count())*moments[sup]
        for sup in range(8) if sup & mask == mask))
prob = {m: S.expand(v.subs(theta,0)) for m,v in atoms.items()}
first = {m: S.expand(S.diff(v,theta).subs(theta,0))
         for m,v in atoms.items()}
second = {m: S.expand(S.diff(v,theta,2).subs(theta,0))
          for m,v in atoms.items()}
coefs = {
    0: 1-eps*(j+ell)+eps*eps*d,
    4: ell-eps*d,
    3: p*(j-eps*d),
    5: p*q*ell-eps*(q-eta)*d,
    6: p*r*ell-eps*(r-eta)*d,
    1: p*q*(1-eps*ell)-eps*(q-eta)*(j-eps*d),
    2: p*r*(1-eps*ell)-eps*(r-eta)*(j-eps*d),
    7: p*d,
}
eta_exp={m:int(m in (0,4)) for m in range(8)}
eps_exp={0:0,1:0,2:0,3:1,4:1,5:1,6:1,7:2}
for m in range(8):
    check_zero(prob[m]-eta**eta_exp[m]*eps**eps_exp[m]*coefs[m])
check_zero(sum(prob.values())-1)
check_zero(sum(first.values()))
check_zero(sum(second.values()))
R = prob[0]+prob[4]
check_zero(R-eta*(1-eps*j))
check_zero(first[0]+first[4]+(1-eps*j)*a+eta*s)
check_zero(second[0]+second[4]-2*(a*s-xr*xr-xi*xi))
check_zero(sum(eps_exp[m]*second[m] for m in range(8))
           -second[0]-second[4])
check_zero(sum(first[m] for m in (4,5,6,7))-t)
check_zero(first[3]-(p*(1-eps*ell)*s-p*eps*j*t
                    +2*p*eps*k*zr+eps*(j-eps*d)*a))
D = (p*(s*t-zr*zr-zi*zi)+eps*j*(a*t-yr*yr-yi*yi)
     +eps*ell*(a*s-xr*xr-xi*xi)
     +2*eps*k*(xr*yr+xi*yi-a*zr))
check_zero(second[7]-2*D)

ordered = (0,4,3,5,6,1,2,7)
yy = (-(1-eps*j),1-eps*j,eps*j,eps*j-q,eps*j-r,
      q-eps*j,r-eps*j,-eps*j)
zz0 = (-eta,eta,p,q-eta,r-eta,-(q-eta),-(r-eta),-p)
zero_direction = {v:0 for v in variables}
for m,cy,cz in zip(ordered,yy,zz0):
    for yv in (yr,yi):
        check_zero(second[m].subs({**zero_direction,yv:1})-2*cy)
    for zv in (zr,zi):
        check_zero(second[m].subs({**zero_direction,zv:1,eps:0})-2*cz)

# Every y-normal acceleration coefficient is exactly zero; y-x has eps.
for m in range(8):
    for yv in (yr,yi):
        for normal in (a,s,t):
            check_zero(S.diff(second[m],yv,normal))
        for xv in (xr,xi):
            check_zero(S.diff(second[m],yv,xv).subs(eps,0))

# C's logarithms at eps=0, represented with independent formal logarithms.
# The substitutions are exact because all factors are positive near the corner.
lp,lq,lr,lj,ll,ld = S.symbols('lp lq lr lj ll ld', real=True)
log0 = {0:0,4:ll,3:lp+lj,5:lp+lq+ll,6:lp+lr+ll,
        1:lp+lq,2:lp+lr,7:lp+ld}
C0 = S.expand(-sum(second[m].subs(eps,0)*log0[m] for m in range(8)))
for yv in (yr,yi):
    check_zero(C0.subs({**zero_direction,yv:1}))
    for zv in (zr,zi):
        check_zero(S.diff(C0,yv,zv))
for zv in (zr,zi):
    check_zero(C0.subs({**zero_direction,zv:1})+2*p*(lj+ll-ld))

# Differentiate C in eps, evaluating the quotient C(y)/eps at eps=0.
dlog = {m:S.cancel(S.diff(coefs[m],eps).subs(eps,0)
                   /coefs[m].subs(eps,0)) for m in range(8)}
for yv in (yr,yi):
    derivative = -sum(
        S.diff(second[m],eps).subs({**zero_direction,yv:1,eps:0})*log0[m]
        +second[m].subs({**zero_direction,yv:1,eps:0})*dlog[m]
        for m in range(8))
    check_zero(derivative+2*(j*(lj+ll-ld)+eta*k*k/(p*ell)))

# Finite full-Hessian checks, computed from exact probabilities and jets.
shape={j:2,k:1,ell:3}
prob_functions={m:S.lambdify((eta,eps),prob[m].subs(shape),'mpmath')
                for m in range(8)}
first_vecs={m:[S.lambdify((eta,eps),S.diff(first[m],v).subs(shape),'mpmath')
               for v in variables] for m in range(8)}
second_mats={m:[[S.lambdify((eta,eps),S.diff(second[m],u,v).subs(shape)/2,
                          'mpmath') for v in variables] for u in variables]
             for m in range(8)}
mp.mp.dps=110
diagnostics=[]
for se,sp in [('1e-4','1e-7'),('1e-7','1e-4'),
              ('1e-12','1e-40'),('1e-40','1e-12')]:
    ee, ep = mp.mpf(se),mp.mpf(sp)
    L=mp.log(1/ee)+mp.log(1/ep)
    scales=[mp.sqrt(ee),mp.sqrt(ep),mp.sqrt(ep),1/mp.sqrt(L),
            1/mp.sqrt(L),mp.mpf(1),mp.mpf(1),1/mp.sqrt(ep),1/mp.sqrt(ep)]
    hessian=mp.matrix(9)
    for m in range(8):
        ps=prob_functions[m](ee,ep)
        assert ps>0
        v=[first_vecs[m][i](ee,ep)*scales[i] for i in range(9)]
        for i in range(9):
            for h in range(9):
                hessian[i,h] -= v[i]*v[h]/ps
                hessian[i,h] -= second_mats[m][i][h](ee,ep)*scales[i]*scales[h]*mp.log(ps)
    eigenvalues=mp.eigsy(hessian,eigvals_only=True)
    largest=eigenvalues[8]
    assert largest<0
    diagnostics.append({'eta':se,'epsilon':sp,
                        'largest_scaled_hessian_eigenvalue':mp.nstr(largest,30)})
out={'exact_assertions':count,'q':'9/25','shape':[[2,1],[1,3]],
     'finite_diagnostics':diagnostics,
     'uniform_proof':'agents/X035.md; finite checks are not a uniform certificate'}
Path(__file__).with_name('checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
