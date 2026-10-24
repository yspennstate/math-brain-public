#!/usr/bin/env python3
from fractions import Fraction as F
from hashlib import sha256

# New arithmetic uses the exact Numaro truth table already certified by
# account03/B17/20260922T073143Z-prime-bellman-dent-transport.
# The peer report proves at p=223/456:
#   p_out=1019/2048 and D_{Gamma^dagger} < -38023/10^6.
# This checker independently reconstructs the truth table, verifies the pivotal
# counts needed for the universally-safe tilted-quartic direction, and proves
# that TILTED-QUARTIC-GATE-REPAIR-v1 remains negative.

EXPECTED_SHA='f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839'
TOP='fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00'
BOT='fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000'
SLICES=[
 (TOP,BOT),
 (TOP,'fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000'),
 (TOP,'fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000'),
 ('fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00','fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000'),
 (TOP,'fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000'),
 (TOP,'fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000'),
 ('fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00',BOT),
 ('fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00',BOT),
 ('fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00',BOT),
 ('fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00',BOT),
]
N=1<<18

def reconstruct():
    base=int(''.join(SLICES[0]),16)
    masks=[int(''.join(r),16)^base for r in SLICES[1:]]
    seen=base; hosts=[]
    for m in masks:
        assert not(seen&m) and m.bit_count()==2
        seen |= m
        hosts.append([x for x in range(512) if (m>>x)&1])
    core=[-1 if (base>>x)&1 else 1 for x in range(512)]
    tab=[]
    for a in range(1<<9):
        row=core.copy()
        for j,cells in enumerate(hosts):
            if a & (1<<j):
                for c in cells:
                    row[c]=-1
        tab.extend(row)
    assert sha256(','.join(map(str,tab)).encode()).hexdigest()==EXPECTED_SHA
    return tab

TAB=reconstruct()

def pivotal_counts():
    # Coordinate 0 pivotal count over the other 17 uniform bits.
    c0=0
    for x in range(N):
        if (x&1)==0 and TAB[x]!=TAB[x|1]:
            c0+=1
    # For coordinates 1..17, separate pivotal pairs according to x_0=0,1.
    s0=s1=0
    for j in range(1,18):
        bit=1<<j
        for x in range(N):
            if x&bit:
                continue
            if TAB[x]!=TAB[x|bit]:
                if x&1: s1+=1
                else: s0+=1
    return c0,s0,s1

c0,s0,s1=pivotal_counts()
assert (c0,s0,s1)==(29184,119040,119040)
alpha=F(c0,1<<17)
rest0=F(s0,1<<16)
rest1=F(s1,1<<16)
assert alpha==F(57,256)
assert rest0==rest1==F(465,256)
# Hence the sum of normalized influences of the other 17 coordinates is
# 465/256 for every bias of coordinate 0.

p=F(223,456)
pout=F(1019,2048)

def eta_star(u):
    m=1-2*u
    return (1-m**4-F(1,36)*(1-m*m)**2)/8

Deta=alpha*eta_star(p)+rest0*eta_star(F(1,2))-eta_star(pout)
assert Deta==F(7405187762554608605,58643094782223581184)
assert Deta>0

lam=F(34877,250000)
inc=lam*Deta
assert inc==F(51654146718923416863317,2932154739111179059200000)
assert inc<F(17617,10**6)

# Source-certified peer bound for the same truth table and bias:
Ddag_upper=-F(38023,10**6)
Dstar_upper=Ddag_upper+inc
assert Dstar_upper<-F(20406,10**6)

# Necessary scale/cap for repairing even this one witness within the proved-safe
# theta=1/36 direction.
lam_required=F(38023,10**6)/Deta
assert lam_required>F(30111,100000)
eta_center=eta_star(F(1,2))
assert eta_center==F(35,288)
Cdag=F(3260925607,500000000)
cap_required=Cdag+lam_required*eta_center
assert cap_required>F(65584446,10000000)

print('PASS')
print('truth_sha256',EXPECTED_SHA)
print('pivotal_coordinate0',alpha)
print('pivotal_rest_sum',rest0)
print('D_eta_star_exact',f'{Deta.numerator}/{Deta.denominator}')
print('D_eta_star_decimal',format(float(Deta),'.18g'))
print('lambda_star_D_eta_decimal',format(float(inc),'.18g'))
print('Gamma_star_defect_upper',format(float(Dstar_upper),'.18g'))
print('required_lambda_from_peer_bound',format(float(lam_required),'.18g'))
print('required_center_cap_from_peer_bound',format(float(cap_required),'.18g'))
