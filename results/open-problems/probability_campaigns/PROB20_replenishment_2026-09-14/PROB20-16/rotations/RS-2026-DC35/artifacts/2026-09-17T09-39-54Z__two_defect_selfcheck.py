#!/usr/bin/env python3
"""
RS-2026-DC35 exact symbolic self-check for the two-defect five-point spike theorem.

This script checks algebraic identities used in the report.  It does NOT certify
the source-complete Problem 35.  Positivity conclusions use the report's stated
assumptions:
    alpha > 1, 0<a,b<1,
    delta > max(a(1-b),(1-a)b).
All symbolic identities are exact (SymPy rational/algebraic manipulation).
"""
import sympy as sp

a,b,alpha,delta,s,t = sp.symbols("a b alpha delta s t", positive=True)
r = t + alpha*s
rstar = b + alpha*a

qN = sp.simplify(delta/(a*(1-b)) - 1)
qS = sp.simplify(delta/((1-a)*b) - 1)

USW = s*t + delta*(s/a)*(t/b)
UNW = s*t + delta*(s/a)*((1-t)/(1-b))
USE = s*t + delta*((1-s)/(1-a))*(t/b)
UNE = s*t + delta*((1-s)/(1-a))*((1-t)/(1-b))

def eq(x,y):
    z = sp.factor(sp.together(x-y))
    assert z == 0, z

# Defective-cell curvature along d=(1,-alpha).
def Dline(F):
    return sp.diff(F,s) - alpha*sp.diff(F,t)

eq(sp.diff(UNW.subs(t, sp.Symbol("R")-alpha*s),s,2), 2*alpha*qN)
eq(sp.diff(USE.subs(t, sp.Symbol("R")-alpha*s),s,2), 2*alpha*qS)
eq(sp.diff(USW.subs(t, sp.Symbol("R")-alpha*s),s,2),
   -2*alpha*(1+delta/(a*b)))
eq(sp.diff(UNE.subs(t, sp.Symbol("R")-alpha*s),s,2),
   -2*alpha*(1+delta/((1-a)*(1-b))))

# All four endpoint-choice chord formulae on each defective cell.
NW_endpoints = {
    "00": (sp.Integer(0), (r-b)/alpha),
    "01": (sp.Integer(0), a),
    "10": ((r-1)/alpha, (r-b)/alpha),
    "11": ((r-1)/alpha, a),
}
SE_endpoints = {
    "00": (a, r/alpha),
    "01": (a, sp.Integer(1)),
    "10": ((r-b)/alpha, r/alpha),
    "11": ((r-b)/alpha, sp.Integer(1)),
}
NWV = {k:sp.factor(UNW + alpha*qN*(s-L)*(R-s))
       for k,(L,R) in NW_endpoints.items()}
SEV = {k:sp.factor(USE + alpha*qS*(s-L)*(R-s))
       for k,(L,R) in SE_endpoints.items()}

# Endpoint interpolation is exact on a fixed line rho=t+alpha*s.
rho = sp.symbols("rho", real=True)
UNW_line = sp.expand(UNW.subs(t,rho-alpha*s))
USE_line = sp.expand(USE.subs(t,rho-alpha*s))
NW_line_endpoints = {
    "00": (sp.Integer(0), (rho-b)/alpha),
    "01": (sp.Integer(0), a),
    "10": ((rho-1)/alpha, (rho-b)/alpha),
    "11": ((rho-1)/alpha, a),
}
SE_line_endpoints = {
    "00": (a, rho/alpha),
    "01": (a, sp.Integer(1)),
    "10": ((rho-b)/alpha, rho/alpha),
    "11": ((rho-b)/alpha, sp.Integer(1)),
}
for k,(L,R) in NW_line_endpoints.items():
    Vline = sp.factor(UNW_line + alpha*qN*(s-L)*(R-s))
    eq(Vline.subs(s,L), UNW_line.subs(s,L))
    eq(Vline.subs(s,R), UNW_line.subs(s,R))
for k,(L,R) in SE_line_endpoints.items():
    Vline = sp.factor(USE_line + alpha*qS*(s-L)*(R-s))
    eq(Vline.subs(s,L), USE_line.subs(s,L))
    eq(Vline.subs(s,R), USE_line.subs(s,R))

# Interior coordinate concavity after chord replacement.
for k in ("00","11"):
    eq(sp.diff(NWV[k],s,2),0); eq(sp.diff(NWV[k],t,2),0)
    eq(sp.diff(SEV[k],s,2),0); eq(sp.diff(SEV[k],t,2),0)
eq(sp.diff(NWV["01"],s,2), -2*alpha*qN)
eq(sp.diff(NWV["01"],t,2), 0)
eq(sp.diff(NWV["10"],s,2), 0)
eq(sp.diff(NWV["10"],t,2), -2*qN/alpha)
eq(sp.diff(SEV["01"],s,2), -2*alpha*qS)
eq(sp.diff(SEV["01"],t,2), 0)
eq(sp.diff(SEV["10"],s,2), 0)
eq(sp.diff(SEV["10"],t,2), -2*qS/alpha)

# Slanted endpoint-switch interfaces.  Difference = (r-c)*Q.
# The report checks Q<=0 from 0<a,b<1 and qN,qS>0 in the indicated cells.
transitions = [
    ("NW_r1_Rmoving", NWV["10"]-NWV["00"], sp.Integer(1),
     (t-b)*(delta-a*(1-b))/(alpha*a*(b-1))),
    ("NW_r1_Rfixed", NWV["11"]-NWV["01"], sp.Integer(1),
     -(s-a)*(delta-a*(1-b))/(a*(b-1))),
    ("NW_rstar_L0", NWV["01"]-NWV["00"], rstar,
     s*(delta-a*(1-b))/(a*(b-1))),
    ("NW_rstar_Lmoving", NWV["11"]-NWV["10"], rstar,
     -(t-1)*(delta-a*(1-b))/(alpha*a*(b-1))),
    ("SE_rstar_Rmoving", SEV["10"]-SEV["00"], rstar,
     t*(delta-b*(1-a))/(alpha*b*(a-1))),
    ("SE_rstar_Rfixed", SEV["11"]-SEV["01"], rstar,
     -(s-1)*(delta-b*(1-a))/(b*(a-1))),
    ("SE_ralpha_Lfixed", SEV["01"]-SEV["00"], alpha,
     (s-a)*(delta-b*(1-a))/(b*(a-1))),
    ("SE_ralpha_Lmoving", SEV["11"]-SEV["10"], alpha,
     -(t-b)*(delta-b*(1-a))/(alpha*b*(a-1))),
]
for name,diff,c,Q in transitions:
    eq(diff,(r-c)*Q)

# Central-line NW-chord minus SE-chord slope: all three possible breakpoint orders.
tc = rstar-alpha*s
UNWc = sp.expand(UNW.subs(t,tc))
USEc = sp.expand(USE.subs(t,tc))
def chord_slope(F,L,R):
    return sp.simplify((F.subs(s,R)-F.subs(s,L))/(R-L))

mN_low = chord_slope(UNWc,0,a)
mS_low = chord_slope(USEc,a,rstar/alpha)
eq(mN_low-mS_low, (alpha*a+b)*(a*b+delta)/(a*b))

mN_mid = chord_slope(UNWc,(rstar-1)/alpha,a)
mS_mid = chord_slope(USEc,a,rstar/alpha)
eq(mN_mid-mS_mid, (alpha*delta+b*(1-b))/(b*(1-b)))

mN_hi = chord_slope(UNWc,(rstar-1)/alpha,a)
mS_hi = chord_slope(USEc,a,1)
eq(mN_hi-mS_hi,
   (alpha*(1-a)+(1-b))*((1-a)*(1-b)+delta)/((1-a)*(1-b)))

# Directional slope gaps at transitions through the middle SW/NE pieces.
# Each RHS is manifestly positive after the indicated nonnegative slack variable.
x,y,z = sp.symbols("x y z", nonnegative=True)

# NW -> SW at t=b.
gap = sp.factor((Dline(NWV["00"])-Dline(USW)).subs(t,b))
eq(gap, alpha*s*(a*b+delta)/(a*b))
gap = sp.factor((Dline(NWV["10"])-Dline(USW)).subs(t,b)
                .subs(s,(x+1-b)/alpha))
eq(gap, (a*b*(1-b)**2 + delta*((1-b)**2+x))/(a*b*(1-b)))

# SW -> SE at s=a.
gap = sp.factor((Dline(USW)-Dline(SEV["00"])).subs(s,a))
eq(gap, t*(a*b+delta)/(a*b))
gap = sp.factor((Dline(USW)-Dline(SEV["01"])).subs(s,a)
                .subs(t,alpha*(1-a)+y))
eq(gap, (alpha*(1-a)**2*(a*b+delta)+delta*y)/(a*b*(1-a)))

# NW -> NE at s=a.
gap = sp.factor((Dline(NWV["01"])-Dline(UNE)).subs(s,a)
                .subs(t,1-alpha*a-z))
eq(gap, (alpha*a**2*((1-a)*(1-b)+delta)+delta*z)/
        (a*(1-a)*(1-b)))
gap = sp.factor((Dline(NWV["11"])-Dline(UNE)).subs(s,a))
eq(gap, (1-t)*((1-a)*(1-b)+delta)/((1-a)*(1-b)))

# NE -> SE at t=b.
gap = sp.factor((Dline(UNE)-Dline(SEV["10"])).subs(t,b)
                .subs(s,(alpha-b-y)/alpha))
eq(gap, (b**2*((1-a)*(1-b)+delta)+delta*y)/
        (b*(1-a)*(1-b)))
gap = sp.factor((Dline(UNE)-Dline(SEV["11"])).subs(t,b))
eq(gap, alpha*(1-s)*((1-a)*(1-b)+delta)/((1-a)*(1-b)))

# Coordinate derivative gaps at the only cell boundaries that matter.
# At s=a, left derivative - right derivative is the same positive expression
# as the corresponding SW->SE or NW->NE cases above.
eq((sp.diff(USW,s)-sp.diff(SEV["00"],s)).subs(s,a),
   t*(a*b+delta)/(a*b))
eq(sp.factor((sp.diff(USW,s)-sp.diff(SEV["01"],s)).subs(s,a)
             .subs(t,alpha*(1-a)+y)),
   (alpha*(1-a)**2*(a*b+delta)+delta*y)/(a*b*(1-a)))
eq(sp.factor((sp.diff(NWV["01"],s)-sp.diff(UNE,s)).subs(s,a)
             .subs(t,1-alpha*a-z)),
   (alpha*a**2*((1-a)*(1-b)+delta)+delta*z)/(a*(1-a)*(1-b)))
eq((sp.diff(NWV["11"],s)-sp.diff(UNE,s)).subs(s,a),
   (1-t)*((1-a)*(1-b)+delta)/((1-a)*(1-b)))

# At t=b, lower derivative - upper derivative.
eq((sp.diff(USW,t)-sp.diff(NWV["00"],t)).subs(t,b),
   s*(a*b+delta)/(a*b))
eq(sp.factor((sp.diff(USW,t)-sp.diff(NWV["10"],t)).subs(t,b)
             .subs(s,(x+1-b)/alpha)),
   (a*b*(1-b)**2 + delta*((1-b)**2+x))/(alpha*a*b*(1-b)))
eq(sp.factor((sp.diff(SEV["10"],t)-sp.diff(UNE,t)).subs(t,b)
             .subs(s,(alpha-b-y)/alpha)),
   (b**2*((1-a)*(1-b)+delta)+delta*y)/(alpha*b*(1-a)*(1-b)))
eq((sp.diff(SEV["11"],t)-sp.diff(UNE,t)).subs(t,b),
   (1-s)*((1-a)*(1-b)+delta)/((1-a)*(1-b)))

print("RS-2026-DC35 TWO-DEFECT SYMBOLIC SELF-CHECK")
print("assumptions: alpha>1, 0<a,b<1, delta>max(a(1-b),(1-a)b)")
print("checked: exact defective/concave cell curvatures")
print("checked: all 8 endpoint-choice chord interpolation identities")
print("checked: all interior pure-second-derivative identities")
print("checked: all 8 slanted endpoint-switch factorizations")
print("checked: 3 central-line chord-slope order cases")
print("checked: all middle-cell directional slope-gap factorizations")
print("checked: all coordinate cell-boundary derivative-gap factorizations")
print("status=PASS")
print("scope: algebraic core only; this does not certify source-complete Problem 35")
