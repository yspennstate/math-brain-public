# Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED.
# GPT-6 maximum is the owner's requested preference, not authenticated telemetry.
#
# Exact symbolic certificate for new P0434 cells in
# X in {1,2,2+d}, P(X=1)=p, P(X=2)=q, P(X=2+d)=r.
# This supersedes the unexecuted 013600Z draft: its final displayed
# threshold identity accidentally carried one extra factor t.

import sympy as sp

t, r, d, lam = sp.symbols('t r d lam', positive=True)
p = 1-t
q = t-r
mu = 1+t
m = mu+r*d
alpha = 1-lam
rho = lam*m
M2 = p+4*q+r*(2+d)**2

# Cell A: r>t^2, d0<d<=d1, where d0=t^2/(p*r), d1=t/q.
# M-SERPT is m on [0,1) and H=1+r*d/t thereafter.
h0 = 1/p
ell = q/(p*t)
z = q*d/t
ell0 = h0-r*d/t
WH = lam*M2/(2*(1-rho)*alpha)

TM1 = 1+lam/(2*alpha)
TM2 = WH+2/alpha
TML = WH+(2+d)/alpha
EM = sp.expand(p*TM1+q*TM2+r*TML)

# Lower wedge d<h0.
C0L = 1+q*ell0**2+r*(h0+z)**2
TG1L = 1+lam*C0L/(2*alpha)
TG2L = WH+(2-ell0)/alpha+ell0
TGLL = WH+(2-ell0)/alpha+d+ell0
EGL = sp.expand(p*TG1L+q*TG2L+r*TGLL)
DL = sp.factor(sp.cancel(EM-EGL))
DL_target = lam*(t**2-p**2*q*r*d**2)/(2*t*p*alpha)
assert sp.simplify(DL-DL_target) == 0
print('LOWER_WEDGE_IDENTITY_PASS')
print('D_lower =', sp.factor(DL_target))

# Upper wedge d>h0.
C0U = 1+t*ell**2+r*h0**2
TG1U = 1+lam*C0U/(2*alpha)
TG2U = WH+(2-ell)/alpha+ell
TGLU = WH+(2+d-h0)/alpha+h0
EGU = sp.expand(p*TG1U+q*TG2U+r*TGLU)
DU = sp.factor(sp.cancel(EM-EGU))
DU_target = lam*(t**2-q*r)/(2*t*p*alpha)
assert sp.simplify(DU-DU_target) == 0
print('UPPER_WEDGE_IDENTITY_PASS')
print('D_upper =', sp.factor(DU_target))

# The exact policy-gap formulas meet continuously at d=h0.
assert sp.simplify(DL_target.subs(d,h0)-DU_target) == 0
print('CONTACT_CONTINUITY_PASS')

# Cell B: r<=t^2 and h<d<=d0, h=mu/(1-r).
# M-SERPT is flat through age two and has one terminal demotion;
# Gittins has one terminal hill.
beta = 1-lam*mu
V = 1+3*t
h = mu/(1-r)
Winf = lam*M2/(2*(1-rho)*beta)
Wh = lam*(V+r*h**2)/(2*beta)

TM1C = 1+lam*V/(2*beta)
TM2C = 2+lam*V/(2*beta)
TMLC = Winf+(2+d)/beta
TGC1 = 1+Wh
TGC2 = 2+Wh
TGCL = Winf+(2+d-h)/beta+h
EMC = sp.expand(p*TM1C+q*TM2C+r*TMLC)
EGC = sp.expand(p*TGC1+q*TGC2+r*TGCL)
DC = sp.factor(sp.cancel(EMC-EGC))
DC_target = lam*r*mu**2/(2*(1-r)*beta)
assert sp.simplify(DC-DC_target) == 0
print('TERMINAL_CELL_IDENTITY_PASS')
print('D_terminal =', sp.factor(DC_target))

# Exact ordering identities for the thresholds.
d0 = t**2/(p*r)
d1 = t/q
assert sp.simplify((d0-h0) - (t**2-r)/(p*r)) == 0
assert sp.simplify((h-d1) - (t**2-r)/(q*(1-r))) == 0
assert sp.simplify((d0-h) - (t**2-r)/(p*r*(1-r))) == 0
assert sp.simplify((h-h0) - (r-t**2)/(p*(1-r))) == 0
print('THRESHOLD_ORDER_IDENTITIES_PASS')

print('ALL_EXACT_CHECKS_PASS')
