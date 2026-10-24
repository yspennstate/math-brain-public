# QFORM B03 — translation-uniform indefinite binary small-ball and physical-pivot closure

Run: `20260922T161346Z-account02-B03-QFORM-r12`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Initial owner revision: `2026-09-22.5`; later fresh owner revision consumed before publication: `2026-09-22.6`  
Initial control head: `9c3cf770bb02e1759f285f6bf895bab4cf0cd05f`; pre-publication control head: `63029d74af9bc20db417cfe539d637f3b55b3632`  
Assignment: `Decoupled time integral`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Outcome: `PROVED_SUPPORTING_THEOREM / ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`.

## 1. Exact target and source corrections retained

The sole target is the full arbitrary-dimensional conjecture: for independent real original-coordinate variables with densities bounded by one and real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal finite essential-density bound for `X^T A X`, or construct a valid target counterexample.

No moment, support, sign, diagonal-basis, or post-rotation-independence assumption is used here. I do not use the refuted law-uniform pointwise Fresnel bound, the false conditional density-cap claim for conjugate sum/difference variables, a fixed-good-minor dichotomy, or receiver-only projected density as a substitute for original product provenance.

The named partner result actually applied is account03/B03 `QFORM-FRACTIONAL-PAIRCOLLISION-v1`, canonical source `yspennstate/math-open-problems@57e920edebdcf1da2a046bcf4152dd459925bb8c`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B03/20260922T155848Z-account03-B03-QFORM-r15/REPORT.md`. I use its exact physical-pivot square transducer

`p_Q(y) <= |d|^(-1/2) E |y-R|^(-1/2)`

for `Q=d(Z+h(W))^2+R(W)`, where `Z` is an original coordinate independent of `W` and has density cap one. That theorem explicitly does not require independence between the shift `h(W)` and the residual `R(W)`.

A second source-pinned peer dependency is account03/B16, canonical `yspennstate/math-open-problems@aee79a848b8d1a5ee1187ce01056b31de32f9505`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260922T150329Z-account03-B16-qform-r12/REPORT.md`. It closed the exact light-cone Schur case `S=[[0,s],[s,c]]` and explicitly left the arbitrary nondegenerate indefinite binary Schur polynomial (both physical diagonals nonzero) as its next unpaid implication. The theorem below closes that local implication by a direct small-ball estimate rather than by the hoped-for strong `L^3` endpoint.

## 2. Main new theorem: arbitrary indefinite binary quadratic polynomial

### Theorem 2.1 — `QFORM-INDEFINITE-BINARY-2/3-SMALLBALL-v1`

Let `X,Y` be independent real random variables with probability densities bounded by one. Let

`q(x,y)=a x^2+2bxy+c y^2+l x+m y+r`,

and assume

`Delta=b^2-ac=|det [[a,b],[b,c]]|>0`.

Thus the quadratic part is nondegenerate and indefinite. Then for every interval `I` of length `ell>0`,

`P(q(X,Y) in I) <= min(1, 3*2^(2/3) * ell^(2/3) * Delta^(-1/3)).`   (2.1)

The bound is uniform over all linear terms and translations.

### Proof

Because the quadratic matrix is invertible, translate `(X,Y)` by the unique critical point to remove `l,m`. Coordinate translations preserve independence and the density caps. Constants only translate the target interval. It therefore suffices to take

`q(x,y)=a x^2+2bxy+c y^2`.

Write

`q_x=2ax+2by`.

Fix parameters `tau,s>0` and split the event `{q in I}` into

`E1={q in I, |q_x|>tau}`,
`E2={|Y|<=s}`,
`E3={q in I, |q_x|<=tau, |Y|>s}`.

For fixed `y`, the one-variable quadratic `x -> q(x,y)` has at most two monotonicity branches. On the part where `|q_x|>tau`, change of variables on each branch gives total preimage length at most `2 ell/tau`. Since the density of `X` is at most one,

`P(E1) <= 2 ell/tau`.                                      (2.2)

Also

`P(E2) <= 2s`.                                               (2.3)

For `E3`, use the polynomial map

`F(x,y)=(q(x,y),q_x(x,y))`.

Its Jacobian is exactly

`det DF = 4(b^2-ac)y = 4 Delta y`.                           (2.4)

The multiplicity of `F` is at most two. Indeed, if `a!=0`, then from `v=q_x` one has `x=(v-2by)/(2a)` and substitution gives

`u=q=v^2/(4a) - (Delta/a)y^2`,

so there are at most two possible values of `y`, and then `x` is fixed. If `a=0`, necessarily `b!=0`; on `y!=0`, `v=2by` fixes `y` and then `u=2bxy+cy^2` fixes `x`, so the multiplicity is one.

The joint density of `(X,Y)` is at most one. By the area formula, because `F(E3)` is contained in `I x [-tau,tau]` and `|y|>s`,

`4 Delta s |E3| <= integral_E3 |det DF| <= 2 * |I x [-tau,tau]| = 4 ell tau`.

Hence

`P(E3) <= |E3| <= ell tau/(Delta s)`.                        (2.5)

Combining (2.2)--(2.5),

`P(q in I) <= 2ell/tau + 2s + ell tau/(Delta s)`.           (2.6)

Choose

`tau=2^(1/3)(ell Delta)^(1/3)`,
`s=2^(-1/3) ell^(2/3) Delta^(-1/3)`.

All three terms in (2.6) equal `2^(2/3) ell^(2/3) Delta^(-1/3)`, proving (2.1). The trivial probability bound gives the displayed minimum with one. QED.

This proof uses only the original two-coordinate product density and an exact two-dimensional Jacobian. It never rotates the variables.

## 3. Half-Riesz upgrade: the arbitrary indefinite physical-Schur branch

The exponent `2/3` in (2.1) is already strictly above the `1/2` threshold needed by the partner's physical square transducer.

Let `R=q(X,Y)` be as in Theorem 2.1. For any `z` and `rho>0`, applying (2.1) to `[z-rho,z+rho]` gives

`P(|R-z|<=rho) <= K rho^(2/3)`,

where

`K=3*2^(4/3) Delta^(-1/3)`.                                (3.1)

For `H>0`, Stieltjes integration by parts gives

`E[|z-R|^(-1/2); |z-R|<=H]
 <= H^(-1/2) P(|z-R|<=H)
    +(1/2) integral_0^H rho^(-3/2) P(|z-R|<=rho) d rho
 <= 4 K H^(1/6)`.                                           (3.2)

The complementary part is at most `H^(-1/2)`. Thus

`E|z-R|^(-1/2) <= 4 K H^(1/6)+H^(-1/2)`.                  (3.3)

Taking

`H=Delta^(1/2)/32`

and substituting the exact value of `K` yields the clean uniform bound

`sup_z E|z-R|^(-1/2) <= 16 sqrt(2) Delta^(-1/4)`.          (3.4)

Now let three selected original coordinates have physical principal block

`B=[[d,r^T],[r,C]]`, `d!=0`,

and Schur complement

`S=C-rr^T/d`.

Assume `det S<0`. Condition on all coordinates outside this triple. Completing the square only in the pivot coordinate gives

`Q_w=d(Z+h_w(X,Y))^2+R_w(X,Y)`,

where the quadratic part of `R_w` is exactly `S`; outside coordinates only change its linear and constant terms. The variables `X,Y,Z` remain independent original coordinates with density caps one under this conditioning.

Apply (3.4) uniformly to `R_w`, then the named partner account03/B03 square transducer. Since `Delta=|det S|`,

`||p_{Q_w}||_infinity <= 16 sqrt(2) |d|^(-1/2)|det S|^(-1/4).`  (3.5)

Because `det B=d det S`, (3.5) is

`boxed( ||p_Q||_infinity <= 16 sqrt(2) (|d det B|)^(-1/4) )`  (3.6)

for the full ambient quadratic form, with arbitrary outside couplings. Averaging the uniformly bounded conditional densities over the outside coordinates proves the ambient result. Equivalently, (3.6) applies whenever the chosen physical pivot satisfies `d det B<0`.

### Scope gained

Account03/B16 previously proved (with the sharper constant 8) the exact physical light-cone Schur form `[[0,s],[s,c]]`. Formula (3.6) removes the zero-diagonal restriction completely: both residual physical diagonal entries may be arbitrary and nonzero, as long as the binary Schur form is nondegenerate indefinite. Thus its stated local unpaid implication is closed without post-rotation independence.

This does **not** solve the full conjecture. The three-large-eigenvalue hypothesis does not force a dimension-free physical triple with bounded reciprocal `( |d det B| )^(-1/4)`; the live singleton-plus-two-banks and local-cross-rank-three obstruction families prevent replacing the remaining global reduction by a uniformly good fixed minor.

## 4. Decoupled-time / independent-copy corollary

Although the proof above deliberately changes mechanism to a product-preserving real-space Jacobian after several Fourier attempts, it also yields an exact integrated independent-copy estimate on the paid branch.

Let `phi_Q(t)=E exp(itQ)` and `Q'` be an independent copy. Then

`|phi_Q(t)|^2=E exp(it(Q-Q'))`                                  (4.1)

with no claim that coordinatewise sums and differences inside a copy pair are independent. From (3.6), `p_Q` is a probability density with

`||p_Q||_2^2 <= ||p_Q||_infinity`.

Plancherel therefore gives

`integral_R |phi_Q(t)|^2 dt
 <= 32 pi sqrt(2) (|d det B|)^(-1/4)`.                         (4.2)

Thus this whole indefinite physical-Schur branch has a dimension-free total pair-collision time integral and, more importantly, the direct linear small-ball bound

`P(Q in I) <= 16 sqrt(2) (|d det B|)^(-1/4) |I|`.             (4.3)

The total-collision estimate (4.2) is downstream of the stronger density theorem; it is not being misused as a sufficient endpoint condition, consistent with the named partner's explicit rank-two endpoint obstruction.

## 5. Exact checker

`check.py` symbolically verifies:

- `det d(q,q_x)/d(x,y) = -4 y(ac-b^2)`;
- the optimized small-ball constant `3*2^(2/3)`;
- the radius-ball constant `3*2^(4/3)=6*2^(1/3)`;
- the optimized half-Riesz constant `16*sqrt(2)`.

Checker source creation commit: `6a4b2e513e1db85135d07323a7866cdd3dbe33db`.  
Saved exact output commit: `cfec10550c508078e25dc82da5deded935a5b6b8`, ending `STATUS=PASS`.

The checker is arithmetic regression evidence only; Sections 2--4 are the all-parameter proof.

## 6. Conditional end-to-end proof and first unpaid implication

A current product-preserving end-to-end skeleton is:

1. If a completed diffuse/ridge certificate applies, use the existing regularized-determinant/ridge theorem.
2. Otherwise seek grouped-coordinate or heavy-coordinate structure in original coordinates.
3. If this produces one physical triple with a nonzero pivot and indefinite nondegenerate Schur complement at dimension-free determinant scale, Theorem 2.1 plus the account03/B03 square transducer gives (3.6), hence linear small-ball.
4. Other already-paid grouped-bank and cross-volume branches cover several complementary geometries.

The first genuinely unpaid target-level implication is therefore **global and structural**, not the local arbitrary-indefinite-binary trace anymore:

> From only three eigenvalues of modulus at least one, give an exhaustive quantitative original-coordinate reduction to the completed ridge/diffuse, grouped-bank/cross-volume, or a physical-pivot branch with dimension-free determinant payment, while retaining all additional spectral components.

The new theorem removes one local analytic obstruction from that synthesis, but the full arbitrary-matrix conjecture remains OPEN.

## 7. Provenance / integrity

Corrections consumed before publication include `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1`, and the later live correction inbox through fresh main `63029d74af9bc20db417cfe539d637f3b55b3632`. The later owner proof-first continuation `QFORM-PROOF-FIRST-20260922T161801Z` was also consumed; it preserves the same full target and explicitly prioritizes translation-uniform fractional-trace synthesis / physical-pivot closure.

No benchmark material, credentials, scheduler identifiers, machine paths, emails, Drive data, public release, paid API, remote workflow, permission change, or unrelated private data were used. A narrow changed-file review found only mathematical text/code and source hashes. Repository retrieval/write is not native learned-memory ingestion, so execution remains `WITHOUT_VERIFIED_BRAIN`.
