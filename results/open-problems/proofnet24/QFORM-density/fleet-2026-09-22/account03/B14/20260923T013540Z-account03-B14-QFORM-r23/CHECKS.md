# account03/B14 r23 quantitative checks

Run: `20260923T013540Z-account03-B14-QFORM-r23`

## 1. Fractional-potential constant

If `0<=p<=K` and `int p=1`, rearrangement against the symmetric decreasing kernel gives

`sup_t int |y-t|^{-alpha} p(y) dy
 <= 2K int_0^{1/(2K)} u^{-alpha} du
 = [2^alpha/(1-alpha)] K^alpha`, `0<alpha<1`.

At `alpha=1/2` this is exactly

`2 sqrt(2K)`.

## 2. Partner substitution

The account04/B14 r6 residual cap is

`K_H=1000(8+log 4) sqrt(s1(H)s2(H)) / [kappa sqrt(nu1 nu2)]`.

Multiplying the half-Riesz trace by the outer physical-square factor `|a|^{-1/2}` gives

`||p_Q||inf
 <= 2 sqrt(2*1000*(8+log 4))
    |a|^{-1/2}
    [s1(H)s2(H)]^{1/4}
    /[kappa^{1/2}(nu1 nu2)^{1/4}]`.

Numerically,

`2 sqrt(2*1000*(8+log 4)) = 274.0261938008101...`.

## 3. Diffuse-bank stress check

For `S_m=J_m/m direct_sum (-J_m/m)`, any rank-two three-coordinate principal block contains two coordinates from one constant bank and one from the other. Its kernel vector on the repeated-bank pair is proportional to `(1,-1,0)`. Every fourth-coordinate coupling vector is equal on those two repeated-bank coordinates, so `k^T c=0`. Thus the one-coordinate leakage gate fails identically on the known aggregate-before-inversion family, as it should.

These computations are checks of the algebra in `REPORT.md`; the universal statements there are proved symbolically and do not rely on numerical experimentation.
