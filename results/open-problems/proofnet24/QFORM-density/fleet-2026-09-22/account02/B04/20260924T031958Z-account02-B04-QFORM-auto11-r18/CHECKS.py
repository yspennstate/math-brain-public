#!/usr/bin/env python3
import json, math

L=64
C=[
 [14,-2,-3,-4],
 [-2,11,-6,-8],
 [-3,-6,6,-12],
 [-4,-8,-12,-1],
]
# V=C/15 is the Householder reflector I-vv^T/15, v=(1,2,3,4).
for i in range(4):
    for j in range(4):
        assert sum(C[i][k]*C[j][k] for k in range(4)) == (225 if i==j else 0)

def hadamard(n):
    H=[[1]]
    while len(H)<n:
        H=[r+r for r in H]+[r+[-x for x in r] for r in H]
    return H
H=hadamard(8)
P=[r[:4] for r in H]
# The eight light rows are P/sqrt(8); after V every physical coefficient is nonzero.
PC=[[sum(P[i][k]*C[j][k] for k in range(4)) for j in range(4)] for i in range(8)]
assert min(abs(x) for row in PC for x in row)>0
assert min(abs(x) for row in C for x in row)>0

x=L*L
W00=4
W10=W01=3*x
W11=2*x*x
E3=W00+W10+W01+W11
assert E3==2*(x+1)*(x+2)
E4=(x+1)**2

K=math.sqrt(W00*W11)
r=K/(2*(W10+K))
s=W10/(2*(W10+K))
assert abs(2*(r+s)-1)<1e-15
G=2*(W10+K)
assert abs(G-2*(1+math.sqrt(2))**2*x)<1e-10
# Conditional natural-volume light marginals in categories 00,10,01,11 are 3/8,1/4,1/4,1/8.
light_marg=r*(3/8)+s*(1/4)+s*(1/4)+r*(1/8)
assert abs(light_marg-0.25)<1e-15

end_derivative=3-(2/3)*math.log(L)+math.log(2)/6
assert end_derivative>0  # convexity then makes h=1/2 the global D/D' optimum.

B_D=6*math.sqrt(math.e)*G**(-1/6)
C_star=8.45302122552817687470491804598
c4=(32/3)**0.25
C4=C_star*c4**(-1/6)
B_r47=C4*E4**(-1/8)
B_E3=C_star*E3**(-1/6)

# One explicit valid ridge certificate, gamma^2=L^{-4}, q=2*carrier_leverage.
g=L**-4
D0=x+1+g
carrier=x/D0
light=0.25*(1/D0+1/(1+g))
assert carrier>light
q=2*carrier
theta=2*(x+1)/D0+2/(1+g)
assert 1<=q<=2 and carrier<=q/2+1e-15 and theta>2*q
Ddet=(D0*(1+g)/(g*g))**2
B_ridge=math.e/(math.sqrt(2*q)*math.sqrt(g))*theta/(theta-2*q)*Ddet**(-1/(2*theta))
# Necessary ridge gate: theta>4*carrier iff g<2/(L^2-2).
assert g < 2/(x-2)

out={
 "marker":"QFORM_B04_R18_TWO_CARRIER_BALANCE_CHECK_PASS",
 "L":L,
 "W00":W00,"W10":W10,"W01":W01,"W11":W11,
 "E3":E3,"E4":E4,
 "q00=q11":r,"q10=q01":s,
 "light_marginal":light_marg,
 "G_D_opt":G,
 "Dprime_endpoint_log_derivative":end_derivative,
 "bound_pinned_D_global_D_Dprime":B_D,
 "C4_down":C4,
 "bound_partner_r47_E4":B_r47,
 "bound_partner_r42_direct_E3":B_E3,
 "ridge_gamma2":g,
 "ridge_carrier_leverage":carrier,
 "ridge_light_leverage":light,
 "ridge_theta":theta,
 "ridge_q":q,
 "bound_ridge_displayed":B_ridge,
 "min_abs_light_integer_coefficient":min(abs(x) for row in PC for x in row),
}
print(json.dumps(out,indent=2,sort_keys=True))
