from fractions import Fraction
import math
import numpy as np

h = Fraction(83,125)
outer = Fraction(38,125)
packet = outer * (2*h - 1)
assert packet == Fraction(1558,15625)

hf=float(h); a=float(outer)
q=2*hf
kbar=2+hf
C_partner=(math.e*q**(-0.5)*kbar/(kbar-2*q)
           *a**(-1/(2*kbar))
           *(hf**hf*(1-hf)**(1-hf))**(1/(2*kbar)))
assert C_partner < 872

c=float(packet)
sqrtc=math.sqrt(c)
prodcoef=sqrtc/6
jointconst=2*math.sqrt(2)/prodcoef
gcoef=sqrtc/(6*math.sqrt(2))
C_vol=(27*math.e/2)/gcoef
bicorecoef=math.sqrt(2/27)*gcoef
e2coef=3*gcoef**4/16
matchcoef=3*gcoef**4/256
assert jointconst < 53.744
assert C_vol < 987
assert gcoef > 0.03721
assert bicorecoef > 0.01012
assert e2coef > 3.596e-7
assert matchcoef > 2.247e-8

beta=(3/16)*math.sqrt(3/5)
zetas=[beta,
       beta/(14400**(1/6)),
       (beta/120)/(225**(1/6))]

print('QFORM_B08_R23_CHECK_PASS')
print('h=',float(h),'packet_fraction=',float(packet))
print('partner_constant=',C_partner)
print('three_bank_product_coefficient=',prodcoef)
print('three_bank_joint_cap_constant=',jointconst)
print('core_floor_coefficient=',gcoef)
print('core_VOL_constant=',C_vol)
print('bicore_star_coefficient=',bicorecoef)
print('E2_coefficient=',e2coef)
print('matching_coefficient=',matchcoef)
for k,z in enumerate(zetas):
    print('k=',k,'zeta_over_L=',z,
          'partner_over_L=',C_partner/z,
          'VOL_over_L=',C_vol/z,
          'G_over_L=',gcoef*z,
          'BICORE_over_L=',bicorecoef*z)

for m in [2,3,8,17]:
    M=np.zeros((m+2,m+2))
    M[0,0]=1
    M[1,2:]=1/math.sqrt(m)
    M[2:,1]=1/math.sqrt(m)
    s=np.linalg.svd(M,compute_uv=False)
    assert np.allclose(s[:3],[1,1,1])
    assert np.allclose(s[3:],0)

    C=M[:2,:2]
    U=M[:2,2:]
    V=M[2:,:2]
    N=M[2:,2:]
    adj=np.array([[C[1,1],-C[0,1]],[-C[1,0],C[0,0]]])
    schur_packet=np.linalg.det(C)*N - V@adj@U
    P=float(np.sum(schur_packet*schur_packet))
    assert abs(np.linalg.det(C))<1e-12
    assert np.linalg.norm(N)<1e-12
    assert abs(P-1)<1e-10

    vals=[]
    for rr in range(2,m+2):
        for cc in range(2,m+2):
            vals.append(float(np.linalg.det(M[[0,1,rr]][:,[0,1,cc]])))
    assert all(abs(abs(v)-1/m)<1e-10 for v in vals)
    assert abs(sum(v*v for v in vals)-1)<1e-10
    print('stress_m=',m,'packet=',P,'minor_abs=',abs(vals[0]))
