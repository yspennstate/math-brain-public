from fractions import Fraction as F
from math import sqrt, asin, pi

# Degree-six base, q=d-1.
d=6
q=5
D2=d*q
D=2*d + D2*D2
assert D2==30
assert D==912
alpha=F(d,D)
beta=F(D2*D2,D)
assert alpha==F(1,152)
assert beta==F(75,76)
assert 2*alpha+beta==1

# Exact-distance-two normalized shell polynomial k2(lambda)=6/5 lambda^2 - 1/5.
def k2_sq_rational(x2):
    return F(6,5)*x2-F(1,5)
assert k2_sq_rational(F(1,1))==1
rho0_sq=F(5,9) # (sqrt(5)/3)^2
assert k2_sq_rational(rho0_sq)==F(7,15)

# Spectral upper bounds.
# one stationary coordinate, one Ramanujan bulk coordinate: q1=(71+sqrt(5)/3)/152.
q1_rat=F(71,152)
q1_sqrt_coeff=F(1,456) # coefficient of sqrt(5)
gap_rat=1-q1_rat
gap_sqrt_coeff=-q1_sqrt_coeff
q2_rat=F(49,228)
q2_sqrt_coeff=F(1,228) # rho0/76=sqrt(5)/228
# q1-q2=(115-sqrt(5))/456 > 0.
diff_rat=F(115,456)
diff_sqrt_coeff=F(-1,456)
assert float(diff_rat)+float(diff_sqrt_coeff)*sqrt(5)>0
assert float(gap_rat)+float(gap_sqrt_coeff)*sqrt(5)>0

# One coordinate's interior radial increment laws.
# Base step xi: +1 (5/6), -1 (1/6).
v1=F(2,3)
a1=F(1,1)
# Exact-distance-two shell eta: +2 (25/30), 0 (4/30), -2 (1/30).
p_eta={2:F(5,6),0:F(2,15),-2:F(1,30)}
assert sum(p_eta.values(),F(0))==1
v2=sum(F(k)*p for k,p in p_eta.items())
a2=sum(F(k*k)*p for k,p in p_eta.items())
assert v2==F(8,5)
assert a2==F(52,15)

# Full two-coordinate one-jump vector: private coordinate 1 (alpha), private coordinate 2 (alpha),
# synchronized K2 x K2 (beta), with independent eta coordinates in synchronized event.
v=alpha*v1 + beta*v2
A=alpha*a1 + beta*a2
C=beta*v2*v2
assert v==F(19,12)
assert A==F(521,152)
assert C==F(48,19)
corr=C/A
assert corr==F(384,521)

# Marginal increment distribution, including zero when only the other coordinate moves.
p={0:alpha, 1:alpha*F(5,6), -1:alpha*F(1,6),
   2:beta*F(5,6), -2:beta*F(1,30)}
p[0]+=beta*F(2,15)
assert p=={0:F(21,152),1:F(5,912),-1:F(1,912),2:F(125,152),-2:F(5,152)}
assert sum(p.values(),F(0))==1
assert sum(F(k)*vv for k,vv in p.items())==v
assert sum(F(k*k)*vv for k,vv in p.items())==A

# Explicit exponential supermartingale test s=1/2 for interior marginal radial chain.
s=F(1,2)
M=sum(vv*(s**k) for k,vv in p.items())
assert M==F(73,152)
assert M<1

# Orthant profile constants.
beta_sq=v**3/A
assert beta_sq==F(130321,112536)
kappaN_sq=2*beta_sq
assert kappaN_sq==F(130321,56268)
center_coeff_N=F(1,2)/v # ell=(1/2)log_5 N, center=ell/v
assert center_coeff_N==F(6,19)

# Long-range branching mismatch.
cover_growth=5**4 # each coordinate base radius <=2r, product growth <=5^(4r)
out_branch=D-1
assert cover_growth==625
assert out_branch==911
assert cover_growth<out_branch

# Center profile value for the correlated bivariate normal.
rho=float(corr)
center_tv=F(3,4)-asin(rho)/(2*pi)

print('P26_T08_SPHERICAL_SYNCHRONIZED_GREEN_EXACT_PASS')
print('degree=',D,'D2=',D2,'alpha=',alpha,'beta=',beta)
print('spectral_gap_lower=(243-sqrt(5))/456 =', float(F(243,456)-sqrt(5)/456))
print('q1_nontrivial_top=(213+sqrt(5))/456 =', float(F(213,456)+sqrt(5)/456))
print('q2_crude_upper=', float(q2_rat)+float(q2_sqrt_coeff)*sqrt(5))
print('radial_marginal=',p)
print('v=',v,'A=',A,'C=',C,'corr=',corr)
print('supermartingale_E_2^-Delta=',M)
print('beta_ell^2=',beta_sq,'kappa_N^2=',kappaN_sq)
print('center_coeff_log5N=',center_coeff_N)
print('center_profile=',float(center_tv))
print('branching=',cover_growth,'<',out_branch)
