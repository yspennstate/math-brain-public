from fractions import Fraction as F
from functools import lru_cache
from math import comb

TERMS = 140
C = F("6.5218512")

T_NUM = {
    1:20, 2:22, 3:24, 4:25, 5:26,
    6:27, 7:28, 8:28, 9:29, 10:29,
    11:29, 12:29, 13:29, 14:29, 15:28,
}
LAMBDA = {
    1:0, 2:1, 3:1, 4:1, 5:1,
    6:1, 7:1, 8:1, 9:1, 10:2,
    11:2, 12:2, 13:2, 14:2, 15:2,
}

def log_unit_interval(x, terms=TERMS):
    assert F(1) <= x <= F(2)
    if x == 1:
        return F(0), F(0)
    z = (x - 1) / (x + 1)
    z2 = z*z
    power = z
    s = F(0)
    for k in range(terms):
        s += power / (2*k + 1)
        power *= z2
    lo = 2*s
    rem = 2*power / ((2*terms + 1)*(1-z2))
    return lo, lo + rem

@lru_cache(maxsize=None)
def log2_interval(x):
    x = F(x)
    if x < 1:
        lo, hi = log2_interval(1/x)
        return -hi, -lo
    e = x.numerator.bit_length() - x.denominator.bit_length()
    if x < F(2)**e:
        e -= 1
    m = x / F(2)**e
    a,b = log_unit_interval(m)
    c,d = log_unit_interval(F(2))
    return F(e) + a/d, F(e) + b/c

def phi_interval(x):
    x = F(x)
    if x == 0:
        return F(0), F(0)
    lo, hi = log2_interval(1/x)
    return x*lo, x*hi

@lru_cache(maxsize=None)
def beta(n,m):
    # Cube edge-isoperimetric recursion after coordinate compression.
    if m < 0 or m > 2**n:
        raise ValueError
    if n == 0:
        return 0
    cap = 2**(n-1)
    ans = None
    for a in range(max(0,m-cap), min(cap,m)+1):
        b = m-a
        v = beta(n-1,a) + beta(n-1,b) + abs(a-b)
        ans = v if ans is None else min(ans,v)
    return ans

def z_lambda(lam):
    # All 63 nonempty spectral atoms except the fixed level-one atom.
    return sum(F(comb(6,k), 2**(lam*k)) for k in range(1,7)) - F(1,2**lam)

def dec(x, digits=15):
    return f"{float(x):.{digits}f}"

def main():
    print("BAL6_GIBBS_COLLAR_CHECK")
    print("C="+str(float(C)))
    beta_row = [beta(5,m) for m in range(1,17)]
    assert beta_row == [5,8,11,12,15,16,17,16,19,20,21,20,21,20,19,16]
    print("beta5=" + ",".join(map(str,beta_row)))

    worst_hi = None
    for m in range(1,16):
        mu = F(16-m,16)
        a = mu*mu
        R = 1-a
        T = F(T_NUM[m],16)
        lam = LAMBDA[m]
        Z = z_lambda(lam)
        I_floor = F(beta(5,m),16) + mu
        assert T >= I_floor
        plo, phi = phi_interval(a)
        llo, lhi = log2_interval(Z/R)
        Ulo = C + plo - lam*a + R*llo - (C-lam)*T
        Uhi = C + phi - lam*a + R*lhi - (C-lam)*T
        assert Uhi < 0
        if worst_hi is None or Uhi > worst_hi[0]:
            worst_hi = (Uhi,m)
        print(
            f"m={m:2d} beta={beta(5,m):2d} I_floor={dec(I_floor,6)} "
            f"T={dec(T,6)} lambda={lam} U_upper={dec(Uhi,15)} PASS"
        )

    assert worst_hi[1] == 15
    assert worst_hi[0] < F(-8,1000)
    print("worst_m=15")
    print("worst_U_upper="+dec(worst_hi[0],15))
    print("all_threshold_rows_PASS=True")

    import itertools
    expected_counts = {16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,
                       24:40,25:26,26:795,27:915,28:253}
    total_profiles = 0
    for K in range(16,29):
        surviving_j = []
        for m in range(1,16):
            mu = F(16-m,16)
            I_floor = F(beta(5,m),16) + mu
            if I_floor <= F(K,16) < F(T_NUM[m],16):
                surviving_j.append(16-m)
        count = 0
        for js in itertools.combinations_with_replacement(sorted(surviving_j),6):
            if sum(js) > K:
                continue
            sq = sum(j*j for j in js)
            if sq < 16*(32-K) or sq > 256:
                continue
            count += 1
        assert count == expected_counts[K]
        total_profiles += count
        print(f"K={K:2d} I={K/16:.4f} surviving_centroid_profiles={count}")
    assert total_profiles == 2029
    print("necessary_I_levels=24/16,25/16,26/16,27/16,28/16")
    print("total_sorted_centroid_profiles=2029")
    print("full_FEI_status=OPEN")

if __name__ == "__main__":
    main()
