import math

K3 = 3 * 2 ** (4/3) * math.exp(1/3)
diffuse = K3 * 1000 / 19
anchor = 47045881 / (3 * 10**18)
anchor_bound = K3 * anchor ** (-1/6)
heavy_paid = 800 * 2 ** (4/3) * math.exp(1/3)
partner = 5 * math.sqrt(2*math.e) * 120 ** (1/10) * 64 ** (2/5) * (1083/10**6) ** (-1/2)
g = 1/2 - 1/math.sqrt(19)
light_s3 = g * (19/20) * (1597/2000) - 403/2000
exact_gap = 19 * 13923**2 - 60686**2

print('K3', K3)
print('diffuse_R5_bound', diffuse)
print('old_double_anchor_bound', anchor_bound)
print('heavy_lightcut_bound', heavy_paid)
print('partner_r10_bound', partner)
print('g', g)
print('light_cross_s3_floor', light_s3)
print('exact_squared_gap', exact_gap)

assert K3 < 10.551
assert diffuse < 555.273
assert anchor_bound < 666.847
assert heavy_paid < 2813.379
assert partner < 3017.923
assert light_s3 > 3/800
assert exact_gap > 0
print('STATUS=PASS')
