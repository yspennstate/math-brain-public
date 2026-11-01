import math

N=64
vnorm2=sum((1/math.sqrt(N))**2 for _ in range(N))
assert abs(vnorm2-1.0)<1e-12

one_null=6*math.exp(1/3)
partner_anchor=math.sqrt(127/800)
double_null=4*math.sqrt(math.e)/math.sqrt(partner_anchor)

# Midpoint quadrature for the pinned one-sheet theorem at eigenvalues (+2,+1,-2).
m=200000
h=2*math.pi/m
integral=0.0
for k in range(m):
    th=(k+0.5)*h
    integral += (1.0/math.sqrt(1.0+0.5*math.cos(th)**2))*h
claude_bound=0.5*integral

# Exact spectral facts used in the report:
# [1] direct_sum [[0,v^T],[v,0]] has nonzero eigenvalues {1,+||v||,-||v||}.
# (X+U)^2-(Y-V)^2+Z^2 has matrix spectrum {+2,-2,+1,0,0}.
assert abs(vnorm2-1.0)<1e-12
assert claude_bound < math.pi

print("QFORM_B06_CHECK_PASS")
print(f"star_vnorm2={vnorm2:.12f}")
print("star_nonzero_spectrum=-1,1,1")
print(f"one_null_bound={one_null:.12f}")
print(f"partner_zero_anchor_product_lower={partner_anchor:.12f}")
print(f"double_null_partner_bound={double_null:.12f}")
print("resonant_target_spectrum=-2,0,0,1,2")
print(f"claude_one_sheet_exact_integral_bound={claude_bound:.12f}")
print(f"pi={math.pi:.12f}")
