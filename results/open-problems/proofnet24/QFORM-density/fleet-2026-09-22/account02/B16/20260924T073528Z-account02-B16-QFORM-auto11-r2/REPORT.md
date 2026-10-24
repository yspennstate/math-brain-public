SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B16, 2026-09-24T07:35:28Z.
attacking: the shared-bank punctured hub endpoint after account03/B16 r43 by testing every absolute Holder pairing of the exact hub-star frequency fiber, then forcing the next proof to retain pre-absolute phase coupling.

# account02/B16 — dependent-projection all-Holder hub-fiber barrier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T073528Z-account02-B16-QFORM-auto11-r2`  
Role: Projection-product interaction / complementary constructions and source-valid counterexamples  
Status: **NEW SOURCE-VALID MECHANISM OBSTRUCTION + STRICT TARGET FAMILY WITH GLOBAL BOUND / FULL QFORM OPEN**  
Continuity: not claimed by the global pair-log bound below; the unrestricted continuity problem remains separate.

## 1. Fresh boundary and first unpaid implication

Fresh brain control was read from main and refreshed before publication; OWNER CONTROL remains revision `2026-09-22.15`, QFORM remains the sole target, and no stop or pause applies to account02/B16. The current live correction from designated partner account03/B16 is r43, canonical commit `6f62a39a272ff590cd13d6dfd2de98651bb9d99d`, which disproves the proposed universal `L2` hub-star mixed-norm closure on a strict target family while preserving the exact hub-star Plancherel identity.

The required pinned package was read at exactly `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`: `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. In particular, the completed ruled one-sheet theorem is applied below to a real strict-target inequality. No independence after projection is inferred.

The first unpaid implication after this run is:

**`QFORM-HUBSTAR-PREABSOLUTE-OSCILLATORY-PAIRING-v1`.** In the genuine shared-bank small-pivot collar, no ordinary Holder choice in the star-frequency variable can repair the r43 endpoint once absolute values have been taken separately on the hub and residual fibers. A successful compiler must retain the oscillatory pairing `int F_t(z)G_t(z)dz` itself, or extract a genuinely source-separated third smoother before that absoluteization. In particular, changing `L2-L2` to another conjugate `Lq-Lp` pair is now ruled out even when the residual two-dimensional projection is genuinely dependent.

## 2. A strict target with a genuinely dependent projected pair

Let `H,X_1,X_2` be independent `Uniform[-1/2,1/2]` variables and set

`L=(X_1+X_2)/sqrt(2)`,
`V=(X_1-X_2)/sqrt(2)`.

The pair `(L,V)` is an orthonormal two-dimensional projection of the original product source, but it is **not independent**. Its joint density is exactly

`rho(l,v)=1_{|l|+|v|<=1/sqrt(2)}`.                                (2.1)

Thus the dependence is explicit: the support is a diamond, not a Cartesian product. It is nevertheless a legitimate product projection; in particular the pinned two-dimensional projection theorem applies to it as a joint-density statement.

For `0<epsilon<=1/64`, define

`Q_epsilon=epsilon H^2+2HL-epsilon L^2+V^2`.                      (2.2)

The transformation `(H,X_1,X_2)->(H,L,V)` is orthogonal. In this carrier the matrix is

`B_epsilon=[[epsilon,1,0],[1,-epsilon,0],[0,0,1]]`,               (2.3)

so

`spec(B_epsilon)={-sqrt(1+epsilon^2),1,+sqrt(1+epsilon^2)}`.       (2.4)

Hence every member of (2.2) is an exact-rank-three instance of the full owner target.

## 3. Exact hub-star factors

Use the literal physical hub `H` and the star variable `L`. The characteristic function has the exact pairing

`phi_epsilon(t)=int_R F_t(z) G_t(z) dz`,                           (3.1)

where

`F_t(z)=int_{-1/2}^{1/2} exp(i t(epsilon h^2+2zh)) dh`,            (3.2)

and, because of the diamond density (2.1),

`G_t(z)=1_{|z|<=1/sqrt(2)} exp(-i epsilon t z^2)
        int_{-a(z)}^{a(z)} exp(i t v^2) dv`,                       (3.3)

with

`a(z)=1/sqrt(2)-|z|`.                                             (3.4)

No conditional independence of `L,V` is used. Formula (3.3) is obtained by integrating the original product density through the orthogonal map; the dependence is retained exactly.

## 4. The all-Holder barrier

### Theorem `QFORM-DEPENDENT-PROJECTION-ALL-HOLDER-HUBFIBER-BARRIER-v1`

For every Holder-conjugate pair

`1<=q<=infinity`, `1<=p<=infinity`, `1/p+1/q=1`,                 (4.1)

the strict target family (2.2) satisfies

`boxed: int_T^infinity ||F_t||_q ||G_t||_p dt = infinity`          (4.2)

for a finite `T=T(epsilon)`. Consequently no proof can close the hub-star Fourier integral by first taking separate absolute `Lq` and `Lp` norms of the two factors in (3.1), regardless of the Holder exponents.

### Proof: lower bound for the hub factor

For `|z|<=epsilon/4`, complete the square:

`F_t(z)=exp(-it z^2/epsilon)
        int_{-1/2+z/epsilon}^{1/2+z/epsilon} exp(i kappa u^2)du`,   (4.3)

where `kappa=t epsilon`. Both endpoints in (4.3) lie at distance at least `1/4` from the stationary point zero.

For `R>0`, one integration by parts gives

`|int_R^infinity exp(i kappa u^2)du|<=1/(kappa R)`.                (4.4)

The complete Fresnel integral is

`int_R exp(i kappa u^2)du=sqrt(pi/kappa) exp(i pi/4)`.             (4.5)

The two omitted tails in (4.3) therefore have total modulus at most `8/kappa`. If

`kappa>=256/pi`,                                                   (4.6)

then this is at most one half of the modulus in (4.5), and hence

`|F_t(z)| >= (sqrt(pi)/2)(t epsilon)^(-1/2)`                       (4.7)

for every `|z|<=epsilon/4`.

Thus for finite `q`,

`||F_t||_q >= (sqrt(pi)/2)(epsilon/2)^(1/q)
              epsilon^(-1/2)t^(-1/2)`,                            (4.8)

with the evident endpoint interpretation for `q=infinity`.

### Proof: lower bound for the genuinely dependent residual fiber

If

`|z|<=1/(4sqrt(2))`,                                               (4.9)

then `a(z)>=3/(4sqrt(2))`. Compare the finite Fresnel integral in (3.3) with the complete integral. Its two omitted tails have total modulus at most

`2/[t a(z)] <= 8sqrt(2)/(3t)`.                                    (4.10)

Therefore, once

`t>=512/(9pi)`,                                                    (4.11)

we have

`|G_t(z)| >= (sqrt(pi)/2)t^(-1/2)`                                (4.12)

throughout the interval (4.9). Consequently for finite `p`,

`||G_t||_p >= (sqrt(pi)/2)(1/(2sqrt(2)))^(1/p)t^(-1/2)`,          (4.13)

again with the evident endpoint interpretation for `p=infinity`.

### Assembly

For

`t>=T(epsilon):=256/(pi epsilon)`,                                 (4.14)

condition (4.11) is automatic because `epsilon<=1/64`. Multiplying (4.8) and (4.13) gives

`||F_t||_q ||G_t||_p
 >= (pi/4) epsilon^(-1/2)
    (epsilon/2)^(1/q)(1/(2sqrt(2)))^(1/p) t^(-1)`.                (4.15)

The coefficient in (4.15) is positive for every fixed `epsilon` and every Holder-conjugate pair, including the endpoint pairs `(q,p)=(1,infinity)` and `(infinity,1)`. Hence its integral diverges logarithmically, proving (4.2). QED.

This strictly strengthens account03/B16 r43's `L2-L2` obstruction. The failure is not caused by pretending `(L,V)` are independent: they are genuinely dependent here, and their exact joint product-projection provenance was retained all the way to (3.3).

## 5. Required pinned result applied at a real inequality

The completed ruled one-sheet theorem from the required pinned `COUNTEREXAMPLE_SEARCH.md` applies directly to (2.2). Its signature is `(+,+,-)` and all three eigenvalue magnitudes are at least one. Therefore

`boxed: p_{Q_epsilon}(s)<=pi sqrt(2)` for a.e. `s>=0`.             (5.1)

Numerically `pi sqrt(2)=4.442882938158366...`.

This is the exact interface requested by the assignment: the theorem uses a two-dimensional marginal of an original product law only as a joint-density/line-integral bound inside the curved ruled geometry. It never upgrades the projected coordinates to independence. Equation (5.1) also proves that the divergence in (4.2) is a proof-interface obstruction, not positive-side output-density blowup.

## 6. The same dependent-projection family has a uniform global density bound

The family (2.2) is not a QFORM counterexample. In the original independent coordinates `(H,X_1,X_2)`, the physical principal pair `(H,X_1)` has matrix

`P_epsilon=[[epsilon,1/sqrt(2)],
            [1/sqrt(2),(1-epsilon)/2]]`.                           (6.1)

Its determinant is negative and

`D_epsilon=|det P_epsilon|=(1-epsilon+epsilon^2)/2
 >=4033/8192`.                                                     (6.2)

Moreover

`||P_epsilon||_F^2
 =5/4-epsilon/2+5epsilon^2/4
 <=5/4`.                                                          (6.3)

For a symmetric `2x2` matrix, `sigma_min=D/sigma_max`; hence

`sigma_min(P_epsilon)
 >=2D_epsilon/sqrt(5)
 > (8/9)(4033/8192)
 =4033/9216
 >7/16`.                                                          (6.4)

The whole matrix is exact rank three with all three nonzero eigenvalue magnitudes at least one. Therefore the completed physical-pair logarithmic theorem at

`math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

applies with `s=1`, `D>=4033/8192`, `kappa>7/16`, and gives

`||p_{Q_epsilon}||_infinity
 <=8 sqrt(5) [(4033/8192)(7/16)]^(-1/4)
 =26.25855995211... <26.259`.                                     (6.5)

Thus this genuinely dependent two-dimensional projection family simultaneously has

- every absolute Holder hub-fiber norm closure divergent by (4.2),
- one-sheet density at most `pi sqrt(2)` by the required pinned theorem,
- full-line essential density below `26.259` by a source-valid physical-pair mechanism.

The contrast isolates what is missing: not another choice of absolute function-space exponent, but a pre-absolute oscillatory or source-separated use of the third resource.

## 7. Consequence for the live account03/B16 endpoint

Partner r43 correctly keeps the hub-star identity

`phi(t)=int F_t(z)G_t(z)dz`                                       (7.1)

and refutes only the proposed closure

`int |t|^(-1/2)||G_t||_2 dt<infinity`.                            (7.2)

The present theorem shows that replacing Cauchy-Schwarz in (7.1) by any ordinary Holder pair does not repair the problem. Even a strict target whose residual `(L,V)` is an explicit dependent product projection has

`int ||F_t||_q||G_t||_p dt=infinity`                              (7.3)

for every conjugate `(q,p)`.

Therefore the live first unpaid implication is more specific than r43's `PAIR-PREABSOLUTE-THIRDRESOURCE`: one must obtain cancellation from the **relative phase in the `z` pairing itself**, or expose a disjoint third smoother before separating the two factors. Rearrangement, interpolation, or changing `L2` to `Lp` only after separate absoluteization cannot close the punctured hub.

## 8. Deterministic check

`VERIFY.py` and `CHECK_OUTPUT.txt` in this run directory check the endpoint carrier spectrum, the physical-pair determinant and singular-value lower bound, the pair-log constant `<26.259`, the ruled constant, and the two stationary-phase thresholds. The saved output ends `STATUS=PASS`.

## 9. Status

- `QFORM-DEPENDENT-PROJECTION-ALL-HOLDER-HUBFIBER-BARRIER-v1`: **PROVED source-valid intermediate-mechanism obstruction**.
- Strict target family (2.2): **not a QFORM counterexample**; globally `||p||_infinity<26.259`.
- Required pinned completed result: **applied at (5.1)**.
- Latest designated partner account03/B16 r43: **applied and strictly strengthened at the exact interface it left open**.
- Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuity: **OPEN**.
