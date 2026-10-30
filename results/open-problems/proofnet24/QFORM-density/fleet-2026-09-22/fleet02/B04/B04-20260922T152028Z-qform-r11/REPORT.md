# fleet02/B04 — elementary-symmetric determinant aggregation for square-assisted QFORM

Run: `B04-20260922T152028Z-qform-r11`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Assignment: Product Fourier rearrangement  
Outcome: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and first unpaid implication

The target remains the full arbitrary-dimensional conjecture: independent real coordinates with probability densities bounded by one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, and one universal finite bound on the density of `X^T A X`. No moment, support, diagonal-basis, sign, or post-rotation-independence assumption is added.

The first unpaid B04 implication at startup was partner fleet03/B04's

`QFORM-SQUARE-ASSISTED-DETERMINANT-MIXTURE-v1`:

> replace the reciprocal cost of one selected second/third cross singular value by an aggregate determinant/exterior-mass quantity before taking reciprocals, and then combine that aggregate with a genuine original-coordinate square.

This report pays the analytic part of that implication. The remaining obstruction is structural: forcing one of the resulting aggregate currencies, or routing its failure to an already controlled hyperbolic/diffuse branch.

## 2. Source-pinned dependencies and corrections

Fresh owner control before publication: `yspennstate/math-research-brain@9c0ba5941ed05ec989c00bd4e4d9d50eeadbc672`, owner revision `2026-09-22.5`; protected README Git blob `433b2d57345823967480245b59a7c47d51019c37`.

Required corrections consumed: law-uniform scalar pointwise quadratic-phase decay is false; fiber-sup arguments can lose dimension; spectral rotation does not preserve coordinate independence; one good local cross minor is not exhaustive; one scalar pivot with rank-two Schur extraction is not forced; generic conditional-cap substitutions are invalid; a uniformly good small principal block/rank-three cut is not forced; and a single physical triple can have divergent reciprocal rank-two aggregate cost. None of those claims is used positively.

Named partner actually applied: fleet03/B04,

`yspennstate/math-open-problems@a6cdaaf6e0723f54cc591269183029423cd77154:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/B04-20260922T145033Z-r12/REPORT.md`,

with machine-readable completion at `f447c650e04ef27d14be3380ac541c1cec60ab0c`.

The partner theorem uses the completed regularized determinant estimate: for an original-coordinate cut with cross block `B`, if `1<=q<2` and the left range-projection diagonal is at most `q/2` (or `q=2` unconditionally), then for the residual quadratic form `R`,

`|phi_R(t)| <= det(I + kappa t^2 B B^T)^(-1/(4q)),`

where

`kappa = 2q/(pi^2 e^2).`                                            (2.1)

The same partner report supplies the square-assisted `L^(3/2)_t -> L^3_x -> half-Riesz` closure with a genuine original coordinate. In particular, if `Q=a(X+m(Y))^2+R(Y)`, where `X` is an untouched original coordinate independent of `Y`, then

`||p_Q||_infinity <= H_3 |a|^(-1/2) ||p_R||_3^(3/4),`

`H_3 = 8 sqrt(2) / 3^(3/4).`                                        (2.2)

No scalar Fresnel pointwise estimate is used below.

## 3. Aggregate determinant theorem

Let the nonzero singular values of `B` be `s_1,s_2,...`, and put

`E_k(B) = e_k(s_1^2,s_2^2,...)`

for the `k`th elementary symmetric polynomial. Thus

`E_2(B) = sum_{i<j} s_i^2 s_j^2
        = ((tr BB^T)^2-tr((BB^T)^2))/2.`                           (3.1)

### Theorem 3.1 — `QFORM-SQUARE-ASSISTED-EK-AGGREGATE-v1`

Fix `1<=q<=2`. For `q<2`, assume the regularized-determinant leverage hypothesis `max diag P_range(B) <= q/2`; for `q=2` no leverage condition is required. Let `k` be an integer satisfying

`k > 4q/3`,                                                         (3.2)

and assume `E_k(B)>0`.

Let

`Q = a (X+m(Y))^2 + R(Y),    a != 0,`                              (3.3)

where `X` is one original coordinate with density at most one, independent of the remaining original coordinates `Y`, and `R` is any real quadratic form in `Y` whose physical cross block is `B`. Then `Q` has an essentially bounded density and

`||p_Q||_infinity
 <= C_E(q,k) |a|^(-1/2) E_k(B)^(-1/(4k)),`                         (3.4)

where

`J(q,k)
 = (1/k) Gamma(1/(2k))
       Gamma(3/(8q)-1/(2k)) / Gamma(3/(8q)),`                     (3.5)

and

`C_E(q,k)
 = 2^(5/2) 3^(-5/8) q^(-1/4) sqrt(e J(q,k)).`                     (3.6)

All self-block quadratic phases and all additional small singular/eigen directions are retained. No individual lower bound on the `k`th singular value is assumed.

### Proof

Expand the determinant in (2.1):

`det(I+kappa t^2 BB^T)
 = 1 + kappa t^2 E_1(B) + ... + (kappa t^2)^k E_k(B)+...`.

All coefficients are nonnegative, so

`|phi_R(t)|
 <= [1+kappa^k E_k(B)t^(2k)]^(-1/(4q)).`                           (3.7)

This is a symmetric decreasing product-space envelope. Hence its decreasing rearrangement controls `|phi_R|^*` as well; no law-uniform scalar pointwise decay is being asserted.

Put

`gamma = kappa^(1/2) E_k(B)^(1/(2k)),`

so that `gamma^(2k)=kappa^k E_k(B)`. Raising (3.7) to the `3/2` power and integrating,

`int_R |phi_R(t)|^(3/2) dt
 <= gamma^(-1) J(q,k),`                                           (3.8)

because

`int_R (1+|u|^(2k))^(-alpha) du
 = (1/k) B(1/(2k),alpha-1/(2k)),`

with `alpha=3/(8q)`. The integral is finite exactly when (3.2) holds.

Sharp inverse Hausdorff--Young in the partner normalization gives

`||p_R||_3
 <= (2pi)^(-2/3) C_HY gamma^(-2/3) J(q,k)^(2/3),`

`C_HY=3^(1/6)2^(-1/3).`                                          (3.9)

Apply the partner square-assisted half-Riesz bound (2.2). Since

`gamma^(-1/2)
 = [pi^2 e^2/(2q)]^(1/4) E_k(B)^(-1/(4k)),`

the constants simplify exactly to (3.4)-(3.6). QED.

## 4. Two important endpoints

### 4.1 Leverage-valid two-exterior-mass endpoint

For `q=1,k=2`, only aggregate rank-two exterior mass is required:

`||p_Q||_infinity
 <= 11.26662855015649
    |a|^(-1/2) E_2(B)^(-1/8).`                                   (4.1)

Here

`J(1,2)=Gamma(1/4)Gamma(1/8)/(2 Gamma(3/8))
       =5.761625958998023... .`

This is strictly different from selecting two singular values `>=sigma`: if such a selection exists then `E_2>=sigma^4` and (4.1) recovers the correct `sigma^(-1/2)` scale, but (4.1) can stay bounded when every individual singular value tends to zero.

The structural currency is therefore

`Theta_2 = |a|^4 E_2(B)`.                                         (4.2)

A universal lower bound on `Theta_2` would yield a universal density bound without paying a reciprocal second singular value.

### 4.2 Unconditional three-exterior-mass endpoint

At the unconditional regularized-determinant value `q=2`, take `k=3`. Then

`||p_Q||_infinity
 <= 16.70346480643532
    |a|^(-1/2) E_3(B)^(-1/12).`                                  (4.3)

Thus lack of a leverage-valid `q<3/2` cut does not force selection of three individually large singular values; aggregate cubic exterior mass is enough. The corresponding currency is `|a|^6 E_3(B)`.

## 5. A genuinely rotated indefinite family where aggregation is essential

The next construction is an exact source-valid stress family for the old `sigma_2` selection interface.

Let `m=2^r>=2` and `N=4m`. Take a normalized `N x N` Walsh matrix. Choose `m` Walsh columns to form `U`, another unused Walsh column `u_0`, and independently choose `m` Walsh columns `V` and an unused Walsh column `v_0` on a second bank. Thus

`U^T U=V^T V=I_m`,

`u_0 perp range(U)`, `v_0 perp range(V)`, and every row leverage of `U` and `V` is exactly

`m/N=1/4.`                                                        (5.1)

Define

`B = m^(-1/2) U V^T`                                              (5.2)

and the `2N x 2N` residual symmetric matrix

`S = [[u_0 u_0^T, B],
      [B^T,       -v_0 v_0^T]].`                                  (5.3)

Its spectrum is exactly

`{+1,-1} union {+m^(-1/2),-m^(-1/2) each m times} union {0's}.`   (5.4)

Now take a fresh original coordinate `Z`, set `a=2`, choose `b=(u_1,0)` for any selected Walsh column `u_1` in `U`, and define the full matrix by

`A = [[S + bb^T/a, b],
      [b^T,         a]].`                                         (5.5)

Pivoting the last original coordinate recovers Schur complement exactly `S`, while the pivot is genuinely coupled to all `N` coordinates of the first Walsh bank. The vectors `(u_0,0,0)` and `(0,v_0,0)` remain eigenvectors with eigenvalues `+1` and `-1`; moreover the Rayleigh quotient on the pivot coordinate is `2`, so `lambda_max(A)>=2`. Hence `A` is genuinely rotated, indefinite, and has at least three eigenvalues of modulus at least one.

For the physical cut between the two Walsh banks, `range(B)=range(U)` and every range leverage is `1/4<1/2`, so `q=1` is valid. All `m` singular values of `B` equal `m^(-1/2)`, hence

`E_2(B) = C(m,2)/m^2 = (m-1)/(2m).`                               (5.6)

The new aggregate theorem therefore gives, for every allowed independent input law,

`||p_(X^T A X)||_infinity
 <= 11.26662855015649
    / [sqrt(2) ((m-1)/(2m))^(1/8)]
 <= 9.474067560.`                                                  (5.7)

The bound is uniform in `m`.

By contrast, the named partner's previous two-selected-singular-value endpoint sees only `sigma=m^(-1/2)` and gives

`10.748739899781292 / sqrt(2 m^(-1/2))
 = 7.600506873... m^(1/4),`                                      (5.8)

which diverges. Thus (5.7) is a genuine determinant-mixture gain, not a reparameterization of the selected-`sigma_2` theorem.

For the concrete genuinely rotated `m=64`, `N=256` instance (dimension `513`),

`E_2=63/128`

and

`boxed(||p||_infinity <= 8.704877343).`                           (5.9)

The old selected-two-singular bound on the same instance is `21.49747980`.

## 6. Exact computation used

Only constants in Sections 4-5 were numerically evaluated. Exact code/output:

```python
import mpmath as mp
mp.mp.dps = 30

def J(q,k):
    q=mp.mpf(q); k=mp.mpf(k)
    return (mp.gamma(1/(2*k))*
            mp.gamma(mp.mpf(3)/(8*q)-1/(2*k)) /
            (k*mp.gamma(mp.mpf(3)/(8*q))))

def C(q,k):
    q=mp.mpf(q)
    return (2**(mp.mpf(5)/2)*3**(-mp.mpf(5)/8)*q**(-mp.mpf(1)/4)
            * mp.sqrt(mp.e*J(q,k)))

print("J(1,2) =", J(1,2))
print("C(1,2) =", C(1,2))
print("J(2,3) =", J(2,3))
print("C(2,3) =", C(2,3))
for m in [2,64]:
    E=(mp.mpf(m)-1)/(2*m)
    new=C(1,2)/(mp.sqrt(2)*E**(mp.mpf(1)/8))
    old=mp.mpf('10.748739899781292')/mp.sqrt(2/mp.sqrt(m))
    print(m,E,new,old)
```

Output:

```text
J(1,2) = 5.7616259589980233046
C(1,2) = 11.266628550156485788
J(2,3) = 17.909573298032626646
C(2,3) = 16.703464806435312814
2 0.25 9.4740675598217441023 9.0385768502206593587
64 0.4921875 8.7048773420503248977 21.497479799562584
```

## 7. What is now paid and what remains unpaid

Paid in this run:

1. the selected-cross-singular-value requirement in the partner square-assisted theorem can be replaced by aggregate elementary-symmetric determinant mass `E_k`;
2. the key `q=1,k=2` endpoint depends only on `E_2`, an exterior-mass/stable-rank quantity;
3. the unconditional `q=2,k=3` endpoint depends only on `E_3`;
4. an explicit rotated indefinite target family has uniformly bounded density although every individual cross singular value tends to zero.

The full conjecture is still OPEN. The first structural implication is now sharpened to:

`QFORM-AGGREGATE-PIVOT-CURRENCY-v1`:

> From the sole hypothesis of at least three eigenvalues with modulus at least one, prove that some original-coordinate scalar pivot and physical cut have either (i) leverage-valid `|a|^4 E_2(B)>=delta`, or (ii) unconditional `|a|^6 E_3(B)>=delta`, for one universal `delta>0`, OR route the failure of both aggregate currencies into an already controlled diffuse/hyperbolic/fresh-square branch without paying a reciprocal local minor.

A pivot-only statement cannot be universally true because the known isotropic rank-three Fourier family can have every physical scalar pivot zero; that branch must be routed to a bilinear/aggregate mechanism rather than hidden in (7.1).

No full-proof claim, no continuity claim, and no novelty claim is made.
