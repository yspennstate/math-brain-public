import math

ETA0 = 1/32
C0 = math.log2(32/31)

def phi(d):
    return 4*d/math.log2(1/(2*d))

def root_for_a(a):
    lo, hi = 0.0, 0.49
    for _ in range(180):
        mid=(lo+hi)/2
        if phi(mid) <= 1/a:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

def old_root(r): return root_for_a(16*r+1)
def asym_root(r): return root_for_a(8*r+9)
def plus_a(r): return max(16,4*(r+1))
def plus_root(r): return root_for_a(plus_a(r))

max_eq = 0.0
max_alg_general = -1e9
max_alg_plus = -1e9
monotone = True
prev = float('inf')
for r in range(1,4097):
    dg=asym_root(r)
    max_eq=max(max_eq,abs(phi(dg)-1/(8*r+9)))
    a=1/(8*r+9)
    max_alg_general=max(max_alg_general,8*(r+1)*a-(1-a))
    ap=1/plus_a(r)
    max_alg_plus=max(max_alg_plus,ap-1/16, 4*(r+1)*ap-1)
    if dg > prev + 1e-15: monotone=False
    prev=dg

print(f'eta0={ETA0:.17g}')
print(f'c0={C0:.17g}')
print('r old_delta new_general_delta q_ge_j_delta new/old q_ge_j/old')
for r in [1,2,3,4,8,16,32,64,128,256,512,1024,2048,4096]:
    o=old_root(r); g=asym_root(r); p=plus_root(r)
    print(f'{r:4d} {o:.15g} {g:.15g} {p:.15g} {g/o:.12g} {p/o:.12g}')
print(f'max_root_equation_abs_error={max_eq:.3e}')
print(f'max_general_algebra_violation={max_alg_general:.3e}')
print(f'max_q_ge_j_algebra_violation={max_alg_plus:.3e}')
print(f'general_threshold_monotone_decreasing={monotone}')
print('low_defect_q_ge_j_codim_le_7_automatic=', all(1/32 <= min(1/16,1/(4*(r+1))) for r in range(1,8)))
