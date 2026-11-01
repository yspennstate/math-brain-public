import math

d0=((math.sqrt(105)-8)/64)**2
rho=d0/4
case_b=((math.sqrt(217)-2)/128)**2
scalar=128*math.sqrt(2/rho)
pair=8*math.sqrt(5)*(3*rho**3/8)**(-0.25)

print(f"d0={d0:.17g}")
print(f"rho={rho:.17g}")
print(f"case_b_area_sq={case_b:.17g}")
print(f"case_b_gt_d0={case_b>d0}")
print(f"scalar_bound={scalar:.17g}")
print(f"pair_bound={pair:.17g}")
assert case_b>d0
assert scalar<10312
assert pair<9829
