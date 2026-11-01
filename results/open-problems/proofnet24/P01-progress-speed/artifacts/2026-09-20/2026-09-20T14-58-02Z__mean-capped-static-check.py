from fractions import Fraction as Q

PSTAR=Q(4941,12500)
LAM0=Q(13157,20000)
U=Q(14179,20000)
L=Q(2,3)
TARGET=Q(1,175000)

def support_margin(p,l):
    return 2*(1-p)*(1-l-2*p*l*l)/((1-l)*(1+l)**2)

def qpoly(D,p,l,u):
    return Q(D)*u*u+(l*(D+1)-D)*u+l*l-l*(1+p*(D-1))

def Pcrit(p):
    return 6561*p**4-9686*p**3+5262*p**2-1245*p+108

def Pcrit_prime(p):
    return 26244*p**3-29058*p**2+10524*p-1245

def Pcrit_second_inner(p):
    # Pcrit''(p)=12*Pcrit_second_inner(p)
    return 6561*p*p-4843*p+877

def Pcrit_second_inner_prime(p):
    return 13122*p-4843

support_slack=1-LAM0-2*PSTAR*LAM0*LAM0
lower_margin=support_margin(PSTAR,LAM0)

# Q_{D,p,lambda}(U) is affine in D.  These are the worst-D=3
# and D-slope checks needed for every D>=3 on the hard strip.
Q_coeff_D=U*U+(LAM0-1)*U-LAM0*PSTAR
Q_D3=qpoly(3,PSTAR,LAM0,U)
lambda_slope_coeff_D=U-PSTAR
lambda_slope_D3=4*U+2*LAM0-(1+2*PSTAR)

# For R_D(lambda,mu)=((D+1-mu)(lambda+2mu-1))/(D*mu*(D+lambda)),
# partial_mu R has numerator D(1-lambda)-lambda-2mu^2+1.
# D=3, lambda=2/3, mu=U is the worst corner for D>=3.
mu_monotone_slack_D3=Q(4,3)-2*U*U

# (D-1)R_D(2/3,U) <= K because
# (D-1)(D+1-U) <= D(D+2/3).
K=(L+2*U-1)/U
X=PSTAR*K/(1-PSTAR)
hard_margin=2*(1-X)/(1+X+L)**2

# D=2 is handled directly: min_{theta in [0,1]}
# (1-theta+2theta^2)=7/8 and r+lambda<=8/3.
D2_margin=Q(63,256)

# Ideal asymptotic frontier obstruction for this two-stage mechanism.
# Eliminating u and lambda from
# 2 p lambda^2+lambda=1,
# u^2+(lambda-1)u-lambda p=0,
# p/(1-p)*(2-1/(3u))=1
# gives Pcrit(p)=0.  The signs bracket the relevant root.
p_lo=PSTAR
p_hi=Q(39529,100000)
P_lo=Pcrit(p_lo)
P_hi=Pcrit(p_hi)
Pp_lo=Pcrit_prime(p_lo)
P2inner_hi=Pcrit_second_inner(p_hi)
P2innerprime_lo=Pcrit_second_inner_prime(p_lo)

assert support_slack>0
assert lower_margin>TARGET
assert Q_coeff_D>0 and Q_D3>0
assert lambda_slope_coeff_D>0 and lambda_slope_D3>0
assert mu_monotone_slack_D3>0
assert X<1
assert hard_margin>TARGET
assert D2_margin>TARGET
assert P_lo>0 and P_hi<0
# On [p_lo,p_hi], Pcrit_second_inner is increasing but remains negative,
# so Pcrit' is decreasing; Pcrit'(p_lo)<0 gives uniqueness of the bracketed root.
assert P2innerprime_lo>0 and P2inner_hi<0 and Pp_lo<0

print('ALL_EXACT_CHECKS_PASS')
print('pstar',PSTAR,float(PSTAR))
print('lambda0',LAM0,float(LAM0))
print('u',U,float(U))
print('support_slack',support_slack,float(support_slack))
print('lower_margin',lower_margin,float(lower_margin),'target',TARGET)
print('Q_coeff_D',Q_coeff_D,float(Q_coeff_D))
print('Q_D3',Q_D3,float(Q_D3))
print('lambda_slope_coeff_D',lambda_slope_coeff_D,float(lambda_slope_coeff_D))
print('lambda_slope_D3',lambda_slope_D3,float(lambda_slope_D3))
print('mu_monotone_slack_D3',mu_monotone_slack_D3,float(mu_monotone_slack_D3))
print('K',K,float(K))
print('X',X,float(X))
print('hard_margin',hard_margin,float(hard_margin))
print('D2_margin',D2_margin,float(D2_margin))
print('Pcrit_pstar',P_lo,float(P_lo))
print('Pcrit_39529e-5',P_hi,float(P_hi))
print('Pcrit_prime_pstar',Pp_lo,float(Pp_lo))
print('Pcrit_second_inner_39529e-5',P2inner_hi,float(P2inner_hi))
print('Pcrit_second_inner_prime_pstar',P2innerprime_lo,float(P2innerprime_lo))
