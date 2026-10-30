from fractions import Fraction as F

eta=F(16333,500000)
k=F(56351,10_000_000)
u=eta+eta*eta
su=F(18367,100000)
sk=F(751,10000)
eps=F(31849,100000)
C=F(7262,25)
d0=1-3*eta-2*eps*(1-eta+su)

checks={
"sqrt_u":su*su-u,
"sqrt_k":sk*sk-k,
"sqrt_18k":eps*eps-18*k,
"order1_margin":1-eta-su-4*sk,
"delta0":d0,
"two_high_margin":d0*d0/F(6)-4*u*u,
"one_high_diag_margin":((F(2,5)-eta)/2)**2-u,
"W_dis_gt_1_5300":d0*d0/F(150)-F(1,5300),
"large_V3_sixth_power":C**6*k**3-F(2**6*6**8),
"scalar_pivot_margin":eta-(F(105,2)/C)**2,
"eta_above_1_44":eta-F(1,44),
}
for name,v in checks.items():
    print(name, v, float(v))
    assert v>0
print("ALL_EXACT_MARGINS_POSITIVE")
