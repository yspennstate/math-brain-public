import math, json

Vn = [
[14,-2,-3,-4],
[-2,11,-6,-8],
[-3,-6,6,-12],
[-4,-8,-12,-1],
]
for i in range(4):
    for j in range(4):
        s=sum(Vn[k][i]*Vn[k][j] for k in range(4))
        assert s == (225 if i==j else 0)

H4rows=[
[1,1,1,1],
[1,-1,1,-1],
[1,1,-1,-1],
[1,-1,-1,1],
[1,1,1,1],
[1,-1,1,-1],
[1,1,-1,-1],
[1,-1,-1,1],
]
for h in H4rows:
    row=[sum(h[k]*Vn[j][k] for k in range(4)) for j in range(4)]
    assert all(x != 0 for x in row)
assert all(all(x != 0 for x in Vn[i]) for i in range(3))

y_half=(math.sqrt(17)-1)/2
assert abs(y_half**2+y_half-4)<1e-12
P=lambda y:4+9*y+6*y*y+y**3
Pp=lambda y:9+12*y+3*y*y
hfun=lambda y:y*Pp(y)/(3*P(y))
C3=P(y_half)/y_half**1.5
Ccomp=4+6*math.sqrt(6)
assert C3 >= Ccomp
assert abs(hfun(y_half)-.5)<1e-12

L=64.0
a=L*L+1
E3=a*a*(a+3)
E4=a**3
H12=L**4*a
qcanon=L**2*(L**2+3)/((L**2+1)*(L**2+4))
BD=6*math.sqrt(math.e)*(C3*L**3)**(-1/6)

y75=(3+math.sqrt(57))/2
def Fprime_y(y):
    h=hfun(y)
    return -1/(2*h)+4/(3-4*h)-math.log(L)+0.5*math.log(y)
lo,hi=y_half,y75*(1-1e-13)
assert Fprime_y(lo)<0 and Fprime_y(hi)>0
for _ in range(200):
    mid=(lo+hi)/2
    if Fprime_y(mid)>0: hi=mid
    else: lo=mid
yo=(lo+hi)/2
ho=hfun(yo)
Go=P(yo)*(L*L/yo)**(3*ho)
BDp=6*math.sqrt(math.e)*(2*ho)**(-.5)/(3-4*ho)*Go**(-1/6)
light=3*(1-ho)/8
assert .5<ho<.75 and light<.5 and BDp<BD

Bpair=2**(17/8)*H12**(-1/8)

g=L**-8
kc=L**2/(a+g)
kl=(3/(a+g)+1/(1+g))/8
q=2*kc
theta=3*a/(a+g)+1/(1+g)
assert kc>kl and 1<=q<=2
assert g < 4/(L*L-4)
assert theta>2*q
D=(1+a/g)**3*(1+1/g)
Bridge=math.e/(math.sqrt(2*q)*math.sqrt(g))*theta/(theta-2*q)*D**(-1/(2*theta))

out={
"marker":"QFORM_B04_R19_THREE_CARRIER_CUBE_CHECK_PASS",
"y_half":y_half,
"complement_lower_constant":Ccomp,
"exact_D_constant_C3":C3,
"L":L,
"E3":E3,
"E4":E4,
"H12":H12,
"canonical_heavy_marginal":qcanon,
"pinned_D_bound":BD,
"Dprime_y_opt":yo,
"Dprime_h_opt":ho,
"Dprime_G_opt":Go,
"Dprime_light_marginal":light,
"Dprime_bound_opt":BDp,
"partner_r48_pair_bound":Bpair,
"ridge_g":g,
"ridge_q":q,
"ridge_theta":theta,
"ridge_bound":Bridge,
"all_44_cross_entries_nonzero":True,
}
print(json.dumps(out,indent=2,sort_keys=True))
