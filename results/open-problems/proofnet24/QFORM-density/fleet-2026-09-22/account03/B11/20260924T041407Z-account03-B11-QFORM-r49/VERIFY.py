import math

etas=[1/math.sqrt(63),0.05,0.01,1.0]
max_err=0.0
min_margin=10.0
print('eta,w0,Delta,length,proved_lower')
for eta in etas:
    w0=min(1e-8,1/(1024*eta))
    v0=0.25
    Delta=math.sqrt(eta*w0)/2
    for frac in (-1,-0.5,0,0.5,1):
        v=v0+frac*Delta
        t_line=-v0*v0/(2*eta*w0)-v0/(eta*w0)*(v-v0)
        lhs=t_line+v*v/(2*eta*w0)
        rhs=(v-v0)**2/(2*eta*w0)
        max_err=max(max_err,abs(lhs-rhs))
        min_margin=min(min_margin,0.5-abs(lhs))
    length=2*Delta*math.sqrt(1+(v0/(eta*w0))**2)
    lower=1/(4*math.sqrt(eta*w0))
    assert length+1e-10 >= lower
    assert Delta <= 1/8
    print(f'{eta:.16g},{w0:.3g},{Delta:.16g},{length:.16g},{lower:.16g}')

partner=2048*math.sqrt(2/7)
print('max_tangent_identity_float_error=',max_err)
print('minimum_support_margin=',min_margin)
print('partner_large_leaf_constant=',partner)
assert min_margin >= 0.374999
assert abs(partner-1094.7020468732903)<1e-9
print('QFORM_B11_R49_XRAY_SEPARATION_CHECK_PASS')
