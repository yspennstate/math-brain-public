import math
import random


def det3(rows):
    (a,b,c),(d,e,f),(g,h,i)=rows
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

random.seed(20260923)
max_det_err=0.0
max_switch_err=0.0
for _ in range(1000):
    th=[random.uniform(-math.pi,math.pi) for _ in range(3)]
    rows=[(math.cos(t),math.sin(t),1.0) for t in th]
    det=det3(rows)
    rhs=4*math.sin((th[0]-th[1])/2)*math.sin((th[1]-th[2])/2)*math.sin((th[2]-th[0])/2)
    max_det_err=max(max_det_err,abs(det-rhs))
    i,j=th[0],th[1]
    lhs=math.cos(i)*math.cos(j)+math.sin(i)*math.sin(j)-1.0
    rhs2=-2.0*math.sin((i-j)/2)**2
    max_switch_err=max(max_switch_err,abs(lhs-rhs2))

eta_constant=(2*math.pi+1)**2/8
light_mass_constant=(2*math.pi+1)**3/8
partner_volume_constant=184/64

print('max_det_err',repr(max_det_err))
print('max_switch_err',repr(max_switch_err))
print('eta_constant',repr(eta_constant))
print('light_mass_constant',repr(light_mass_constant))
print('partner_volume_constant',repr(partner_volume_constant))
assert max_det_err < 2e-14
assert max_switch_err < 2e-14
assert eta_constant < 6.631
assert light_mass_constant < 48.292
assert partner_volume_constant == 2.875
print('QFORM_B11_LORENTZ_ANGULAR_CHECK_PASS')
