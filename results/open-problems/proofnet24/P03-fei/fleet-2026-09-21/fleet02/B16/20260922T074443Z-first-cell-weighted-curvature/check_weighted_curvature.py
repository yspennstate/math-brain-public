from decimal import Decimal, getcontext

getcontext().prec = 120
D = Decimal

a1 = D('0.61030398707805656333804043717432505118320642677587327396454109514028117918611171')
a2 = D('0.38969601292194343666195956282567494881679357322412672603545890485971882081388829')
b2 = D('0.21980996079028513074589362025944838394472194410974804040169895489781938141871307')
b3 = D('0.60798262962681679156829236636922458349219603487659822334523927974936998428228596')
b4 = D('0.17220740958289807768581401337132703256308202101365373625306176535281063429900097')
qlo = D('0.999599660938737401432340239630242384364398154263826596748193326851263222362652769671793794')
qhi = D('0.999599660938737401432340239630242384364398154263826596748203275313631173833727945601271399')
tlo = D('0.00505221312246045939434655084170303695806690469020713564802098136946390390674655961205924090')
thi = D('0.00505221312246045939434655084171251509323056376160455332539176967559630087008270123646436340')

assert a1 + a2 == 1
assert b2 + b3 + b4 == 1

c2 = a1
c3 = b3 + b4
c4 = b4

def kappa_safe(m1):
    return ((1 - qhi) * m1 - thi) / qhi

def kappa_fail(m1):
    return ((1 - qlo) * m1 - tlo) / qlo

# Exact identity test on several decimal slope quadruples.
for s1, s2, s3, s4 in [
    (D('30'), D('30.001'), D('30.002'), D('30.003')),
    (D('-7.25'), D('2.125'), D('19.75'), D('4.5')),
    (D('0'), D('0'), D('0'), D('0')),
]:
    m1 = a1*s1 + a2*s2
    m12 = b2*s2 + b3*s3 + b4*s4
    d2, d3, d4 = s2-s1, s3-s2, s4-s3
    kappa = c2*d2 + c3*d3 + c4*d4
    assert m12 - m1 == kappa

print('PASS')
print('kappa_coeff_d2 =', c2)
print('kappa_coeff_d3 =', c3)
print('kappa_coeff_d4 =', c4)
print('kappa_coeff_sum =', c2+c3+c4)
for m in (D(29), D(30), D(31)):
    print('kappa_safe_at_m1_%d =' % int(m), kappa_safe(m))
    print('kappa_fail_at_m1_%d =' % int(m), kappa_fail(m))
print('critical_m1_if_kappa_nonpositive =', thi/(1-qhi))
safe30 = kappa_safe(D(30))
print('equal_forward_jump_allowance_at_m1_30 =', safe30/(c2+c3+c4))
print('d2_only_allowance_at_m1_30 =', safe30/c2)
print('d3_only_allowance_at_m1_30 =', safe30/c3)
print('d4_only_allowance_at_m1_30 =', safe30/c4)
print('corridor_width_at_m1_30 =', kappa_fail(D(30))-safe30)
