#!/usr/bin/env python3
import sympy as sp

s,t,alpha,q,r = sp.symbols("s t alpha q r", positive=True)
half = sp.Rational(1,2)
c = q+1
r0 = (alpha+1)/2
A = 1+q/2
R = t+alpha*s

USW = (q+2)*s*t
UNW = s*(c-q*t)
USE = t*(c-q*s)
UNE = s*t + c*(1-s)*(1-t)

NW1 = A*s
NW2 = UNW + (q/alpha)*(1-t)*(t-half)
NW3 = s + (q/2)*(1-t)
SE1 = A*t
SE2 = USE + (q/alpha)*t*(half-t)
SE3 = t + (q/2)*(1-s)

def z(expr):
    return sp.simplify(expr) == 0

# Exact chord identities on a fixed d-line t=r-alpha*s.
ts = r-alpha*s
UNW_line = sp.expand(UNW.subs(t,ts))
USE_line = sp.expand(USE.subs(t,ts))
nw_endpoints = [
    (sp.Integer(0), (r-half)/alpha, NW1),
    ((r-1)/alpha, (r-half)/alpha, NW2),
    ((r-1)/alpha, half, NW3),
]
se_endpoints = [
    (half, r/alpha, SE1),
    ((r-half)/alpha, r/alpha, SE2),
    ((r-half)/alpha, sp.Integer(1), SE3),
]
for i,(s0,s1,V) in enumerate(nw_endpoints,1):
    corr = alpha*q*(s-s0)*(s1-s)
    assert z(UNW_line+corr-V.subs(t,ts)), ("NW chord", i)
for i,(s0,s1,V) in enumerate(se_endpoints,1):
    corr = alpha*q*(s-s0)*(s1-s)
    assert z(USE_line+corr-V.subs(t,ts)), ("SE chord", i)

# Interior coordinate concavity.
pieces = {"SW":USW,"NE":UNE,"NW1":NW1,"NW2":NW2,"NW3":NW3,
          "SE1":SE1,"SE2":SE2,"SE3":SE3}
expected_tt = {"SW":0,"NE":0,"NW1":0,"NW2":-2*q/alpha,"NW3":0,
               "SE1":0,"SE2":-2*q/alpha,"SE3":0}
for name,V in pieces.items():
    assert z(sp.diff(V,s,2)), ("ss", name)
    assert z(sp.diff(V,t,2)-expected_tt[name]), ("tt", name)

# Slanted regime-change factorisations.
assert z((NW2-NW1) - (-q*(2*t-1)*(R-1)/(2*alpha)))
assert z((NW3-NW2) - (q*(t-1)*(R-r0)/alpha))
assert z((SE2-SE1) - (-q*t*(R-r0)/alpha))
assert z((SE3-SE2) - (q*(2*t-1)*(R-alpha)/(2*alpha)))

# Third-direction slope-gap identities at interfaces with the concave middle piece.
# r<r0: NW -> SW -> SE.
mN_lo = A
fSW_at_NW = (q+2)*(1-r)
assert z(mN_lo-fSW_at_NW-(q+2)*(r-half))

mN_mid = 1+q*(r-half)
gap = sp.expand(mN_mid-fSW_at_NW)
assert z(sp.diff(gap,r)-(2*q+2))
assert z(gap.subs(r,1)-A)

fSW_at_SE = (q+2)*(r-alpha)
mS_lo = -alpha*A
assert z(fSW_at_SE-mS_lo-(q+2)*(r-alpha/2))

# r>r0: NW -> NE -> SE.
mN_hi = 1+alpha*q/2
fNE_at_NW = (q+2)*(r-alpha) + (q+1)*(alpha-1)
assert z(mN_hi-fNE_at_NW-(q+2)*(alpha+2-2*r)/2)

fNE_at_SE = (alpha-1)*(q+1) - (q+2)*(r-1)
mS_mid = q*r-q/2-alpha*(q+1)
assert z(fNE_at_SE-mS_mid-(2*(q+1)*(alpha-r)+(q+2)/2))

mS_hi = -alpha-q/2
assert z(fNE_at_SE-mS_hi-(q+2)*(alpha+half-r))

# Coordinate-boundary derivative jumps.
assert z((sp.diff(SE1,s)-sp.diff(USW,s)) + (q+2)*t)
assert z((sp.diff(UNE,s)-sp.diff(NW3,s)).subs(s,half) - (q+2)*(t-1))
assert z((sp.diff(NW1,t)-sp.diff(USW,t)).subs(t,half) + (q+2)*s)
assert z((sp.diff(NW2,t)-sp.diff(USW,t)).subs(t,half)
         - (q/(2*alpha)-2*(q+1)*s))
assert z((sp.diff(UNE,t)-sp.diff(SE2,t)).subs(t,half)
         - (2*(q+1)*(s-1)+q/(2*alpha)))
assert z((sp.diff(UNE,t)-sp.diff(SE3,t)).subs(t,half)
         - (q+2)*(s-1))

print("C29 centered two-defect symbolic checker")
print("assumptions: alpha>1, q>0; c=q+1=4*delta; r0=(alpha+1)/2")
print("six_chord_identity_checks=PASS")
print("interior_coordinate_second_derivatives=PASS")
print("slanted_regime_jump_factorizations=PASS")
print("third_direction_slope_gap_identities=PASS")
print("coordinate_boundary_jump_identities=PASS")
print("sign_domains:")
print("  NW1->NW2: t>=1/2 gives both coordinate jumps <=0")
print("  NW2->NW3: t<=1 gives both coordinate jumps <=0")
print("  SE1->SE2: t>=0 gives both coordinate jumps <=0")
print("  SE2->SE3: t<=1/2 gives both coordinate jumps <=0")
print("  linewise gaps use r>=1/2, r>=1, r>=alpha/2, r>=r0, r<=alpha, r<=alpha+1/2")
print("  coordinate cell-boundary gaps use s>=1/(2alpha) and s<=1-1/(2alpha) in middle regimes")
print("ALL_EXACT_SYMBOLIC_CHECKS_PASS")
