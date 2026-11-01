from math import sqrt, e

C_small_mu = 288*sqrt(3*e)/13
C_heavy_a = 2*sqrt(3*e)*(1088*4096)**(1/6)

print('ridge_window_constant=', repr(C_small_mu))
print('heavy_fourth_and_|a|>=1/64_constant=', repr(C_heavy_a))
assert C_small_mu < 64
assert C_heavy_a < 73.27
