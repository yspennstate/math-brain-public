from math import e, sqrt

def cinf(r,q):
    k=r+1
    N=q+2*k
    assert 1 <= q <= 2
    assert q < 2*k/3
    return (N/(2*k-3*q))*2**((q+2*r)/(2*N))*(e/q)**(k/N)

def l2(r,q):
    k=r+1
    N=q+2*k
    return (N/(2*k-q))*2**((q+2*r)/(2*N))*(e/q)**(k/N)

def half_riesz(r,q):
    k=r+1
    N=q+2*k
    return (2*sqrt(2)*N/(2*k-q))*2**((q+2*r)/(4*N))*(e/q)**(k/(2*N))

for r in range(1,8):
    for q in (1.0, 1.25, 1.5, 2.0):
        k=r+1
        N=q+2*k
        beta=0.5+k/q
        assert abs(beta-N/(2*q)) < 1e-12
        assert abs((0.5+k/q)/beta-1.0) < 1e-12
        assert abs((-1/(2*q))/beta + 1/N) < 1e-12
        assert abs((-1/4)/beta + q/(2*N)) < 1e-12
        assert abs((1/4-1/(2*q))/beta + (2-q)/(2*N)) < 1e-12

for q in (1.0, 1.2, 1.5, 2.0):
    invariant_power = 2 - q - (2-q)
    assert abs(invariant_power) < 1e-12

assert 1.0 < 2*(1+1)/3
assert not (4/3 < 4/3)
assert 1.999 < 2*(2+1)/3
assert 2.0 < 2*(3+1)/3

vals = {
    "r1_q1_Cinf": cinf(1,1),
    "r1_q1_L2": l2(1,1),
    "r2_q1_Cinf": cinf(2,1),
    "r2_q1p5_Cinf": cinf(2,1.5),
    "r3_q2_Cinf": cinf(3,2),
    "r3_q2_L2": l2(3,2),
    "r3_q2_collision": 2*l2(3,2),
    "r2_q2_half_riesz_endpoint": half_riesz(2,2),
}
assert abs(vals["r3_q2_Cinf"] - 5*e**(2/5)) < 1e-12
assert abs(vals["r3_q2_L2"] - (5/3)*e**(2/5)) < 1e-12
assert abs(vals["r2_q2_half_riesz_endpoint"] - 4*sqrt(2)*e**(3/16)) < 1e-12

for key,val in vals.items():
    print(f"{key}={val:.15f}")
print("QFORM_B03_R24_CHECK_PASS")
