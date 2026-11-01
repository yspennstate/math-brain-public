import math

tau = 0.0766562902983031
assert tau > 3/40

# If T2 >= d^2/64, the collective-tail bound multiplies its source
# constant 9*sqrt(3)*e/2 by 64^(1/6)=2.
tail_per_d = 9*math.sqrt(3)*math.e
assert tail_per_d < 42.374
assert tail_per_d/tau < 552.777

# If s3 > sqrt(T2)/15 and sqrt(T2)>=d/8, then s3>d/120.
robust_per_d = 720*math.sqrt(math.e)
assert robust_per_d < 1187.080
assert robust_per_d/tau < 15485.740

partner_per_d = 987*120
assert partner_per_d == 118440
assert partner_per_d/tau < 1.546e6

assert tau/8 < 0.009582037
assert tau/math.sqrt(2) > 0.05420418
assert tau/(120*math.sqrt(6)) > 2.60789e-4
assert tau/120 > 6.38802e-4

S_L3 = 0.0526286782826*(tau/120)**3
G_L = 0.0372140952985*tau/120
E2_L4 = 3.5960948148e-7*(tau/120)**4
reserve_L4 = 2.2475592592e-8*(tau/120)**4
bicore_L = 0.0101283938578*tau/120

assert S_L3 > 1.37189e-11
assert G_L > 2.37724e-5
assert E2_L4 > 5.98821e-20
assert reserve_L4 > 3.74263e-21
assert bicore_L > 6.47004e-6

print('QFORM_B08_AUTO11_TWO_CROSS_TAIL_CHECK_PASS')
print('tau =', tau)
print('tail_per_d =', tail_per_d)
print('tail_per_L =', tail_per_d/tau)
print('robust_per_d =', robust_per_d)
print('robust_per_L =', robust_per_d/tau)
print('partner_per_L =', partner_per_d/tau)
print('tube_L =', tau/8)
print('top2_hub_L =', tau/math.sqrt(2))
print('robust_bilateral_L =', tau/(120*math.sqrt(6)))
print('heavy_star_L =', tau/120)
print('S_L3 =', S_L3)
print('G_L =', G_L)
print('E2_L4 =', E2_L4)
print('reserve_L4 =', reserve_L4)
print('bicore_L =', bicore_L)
