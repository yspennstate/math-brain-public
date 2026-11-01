# PROB10-05 corrected idea checkpoint — parity split after the cycle-scale correction

**Supersedes the 13:42Z idea as a theorem route, without deleting it.** After that checkpoint was written, I read the newer neighboring report `proofnet24/NM13-09/progress-persistence/runs/2026-09-20/2026-09-20T1312Z__corrected_mesh22_trace_17207285.md`. It identifies a decisive normalization error in the recent PROB10 four-cycle trace calculations: under the normalized AR four-cycle trace measure the cycle-vertex variance is `G0=(1+r^4)/(1-r^4)`, not 1. Therefore the own-track trace caps `1.15053`, `1.13442`, and the derived endpoints `0.172052`, `0.172096247...` are **withdrawn as certified baselines**. The immutable 13:42Z idea and 13:54Z checker artifacts are retained as failed/superseded work and must not be cited as source-model certificates. Failure count for this run: +1 normalization-dependent route discarded.

The valid incoming source-model candidate is the corrected neighboring certificate

    theta_{2,1/4} > 3441457/20000000 = 0.17207285,

with width `0.07792715`. The corrected neighbor preserves the all-lag r=22/25 covariance comparator and the direct same-operator degree-56 moment bounds, and recomputes the four-cycle trace at the correct `G0` scale.

## Three attacks after correction

1. **Exact parity split of the corrected Hermite trace — main attack.** The corrected worker writes the opposite-pair term as `p(q)=m^2+sum_{n>=1}q^n d_n^2/n!`, with `q=23422525/23431822`. Its M=500 checker controls the entire unresolved Hermite tail by `q^501`, which is about 0.82. I will exploit the half-line support of the scalar function `g_A` to sum the full odd sector exactly and reduce the remaining even sector to an O(M) rational recurrence. This is nonduplicating: it begins after, and consumes, the peer's scale correction rather than overwriting it.

2. **New same-operator Perron quasimode — distinct spectral attack.** Recompute a higher-degree witness for the corrected r=22/25 operator to reduce `eps^2<2.70154e-5`. This could have larger eventual leverage but requires a fresh eigensearch and full direct moment recertification; it is deferred in this bounded iteration.

3. **Continuous reverse interpolation — distinct endpoint attack.** Use a negative grid safety margin plus a derivative/modulus event. I will record a rigorous finite-horizon interpolation inequality, but it does not move the upper exponent until the margin/modulus event is controlled under long survival with subexponential loss.

## Corrected trace identity before code

The peer's corrected opposite-pair reduction uses

    g_A(z)=1_{z>0}(2 Phi(sqrt(A) z)-1),
    A=(1+rho_opp)/(1-rho_opp),

and for standard correlated `(X,Y)` with correlation q,

    p(q)=E[g_A(X)g_A(Y)]
        =m^2+sum_{n>=1} q^n d_n^2/n!,

where `m=E g_A(X)` and `d_n=E[g_A(X) He_n(X)]`.

Because `g_A(x)g_A(-x)=0` identically, Hermite parity gives

    m^2 + sum_{n even, n>=2} d_n^2/n!
      = sum_{n odd} d_n^2/n!
      = E[g_A(X)^2]/2.

The odd weighted sector can be summed in closed form. Put `h=1+A` and `a=A/h`. One integration by parts gives

    d_n=(sqrt(A)/pi) I_{n-1},
    I_k=int_0^infty He_k(x) exp(-h x^2/2) dx.

For n=2j+1,

    I_{2j}=sqrt(pi/(2h)) (2j)! (-a/2)^j/j!,

so the central-binomial arcsine series yields

    sum_{j>=0} q^(2j+1) d_{2j+1}^2/(2j+1)!
      = asin(q a)/(2 pi).

For the even sector define `J_j=I_{2j-1}`. Gaussian integration by parts gives

    J_j=(-1)^(j-1)(2j-3)!! P_j/h,
    P_1=1,
    P_j=1+[(2j-2)/(2j-3)] a P_{j-1}.

Therefore

    w_j := d_{2j}^2/(2j)!
      = [A/(pi^2 h^2)] D_j P_j^2,
    D_1=1/2,
    D_j=D_{j-1}(2j-3)^2/[(2j)(2j-1)].

This makes the corrected even coefficients O(M) exact-rational computations. If `E2=E[g_A^2]`, then after K even modes,

    p(q) <= m^2 + asin(q a)/(2pi)
             + sum_{j=1}^K q^(2j) w_j
             + q^(2K+2)(E2/2-m^2-sum_{j=1}^K w_j).

The plan is K=1000 with outward pi/arctan/arcsin intervals, re-certify the all-lag covariance bridge in the same checker, and then combine the sharpened corrected trace with the inherited direct degree-56 `(mu,eps^2)` certificate by Kato-Temple.

No claim is made yet. Source exact value and the upper endpoint remain UNKNOWN.