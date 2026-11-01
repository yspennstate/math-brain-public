SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B06, 2026-09-23T02:56:57Z.
attacking: a product-preserving non-null scalar/dependent-pair curved-fiber kernel, and the exact boundary where joint pair-density information ceases to suffice.

# fleet02/B06 — weighted physical-chain fiber and a sharp provenance obstruction

**Run:** `b06-20260923T025657Z-adca02bb41f7`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Curved fiber integration  
**Status:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED`; full QFORM conjecture remains OPEN; continuity is not claimed here.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and correction boundary

The target is unchanged: for arbitrary dimension, arbitrary independent real input coordinates with probability densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal essential bound for the density of `X^T A X`, or give a valid counterexample.

This run retains the live corrections: no independence is inferred after spectral rotation; law-uniform pointwise quadratic-phase decay is not used; no unrestricted spectral-fiber supremum is integrated; no arbitrary-joint rank-three coarea inequality or positive conditional projection-density moment is used; and no small matrix error is interpreted as a small random quadratic error on unbounded inputs.


## 2. Source-valid inputs actually applied

### 2.1 Required newest-Claude package

The required package

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

was read through `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. In particular, its physical-pair completion says that an invertible ORIGINAL-coordinate physical `2x2` block with determinant and least singular value bounded away from zero can be paid in the full ambient form, retaining arbitrary other quadratic coefficients and couplings, once the third spectral direction is present. The same source's volume/Fresnel theorems are product-space statements; they do not authorize replacing an original-coordinate pair by an arbitrary dependent projected pair.

This source is applied below to the fixed matrix `A=3B0`: for independent original inputs its physical `(Y,Z)` block is `[[0,3],[3,0]]`, with determinant `-9` and least singular value `3`, so the source physical-pair theorem already supplies a finite universal bound for this target instance. The new theorem below gives a much simpler direct bound `4/3` in the same independent-input instance. The dependent-pair construction in Section 5 then demonstrates exactly why this source-valid conclusion cannot be transferred through a mere joint-density-cap surrogate.

### 2.2 Designated partner fleet03/B06 r24

The designated partner result actually used is

`yspennstate/math-open-problems@606257652f3c70e90c7b7f80ea7cb76c1abf689b`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260923T011959Z-fleet03-B06-qform-r24/REPORT.md`.

It proves, among other statements:

* `QFORM-CROSS-E2-FRACTIONAL-L3-v1`: an aggregate `Delta_2=e_2(BB^T)` `L^3` receiver when one-side range leverage is below the fractional threshold;
* `QFORM-RIDGE-FRACTIONAL-L3-v1`: a regularized-ridge `L^3` receiver when `max diag K<=q/2` and `tr K>4q/3`;
* `QFORM-L3-HALF-RIESZ-TO-LINFINITY-v1`: an outer original-coordinate square turns an `L^3` residual into an `L^infinity` density bound;
* a no-leverage third-cross-singular-value endpoint `<25/sqrt(|a|s)` when `sigma_3(B)>=s`.

A real application appears in Section 6; the partner theorem is not merely cited.

### 2.3 Exact-null predecessor

The exact-null endpoint already paid by fleet02/B16 is

`yspennstate/math-open-problems@5bf3d5e6765ecd1dd091fc7d862f6f04211c530f`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/20260922T232932Z-fleet02-B16-QFORM-auto11/REPORT.md`.

Its `QFORM-NULL-SCALAR-DEPENDENT-PAIR-v1` keeps a genuinely independent scalar while allowing the remaining projected pair to be dependent. The present run does not reprove that exact-null theorem; it attacks a non-null product-preserving chain and identifies which pair-density relaxation is false.

## 3. A weighted product-structure replacement for the fiber supremum

The next theorem is the main positive result of this run.

### Theorem 3.1 — `QFORM-PHYSICAL-CHAIN-WEIGHTED-FIBER-v1`

Let `X` be independent of the pair `(Y,Z)`. Assume:

1. `X` has a probability density bounded by one;
2. the marginal density of `Y` is bounded by `L`;
3. for almost every `y`, the conditional density of `Z|Y=y` is bounded by `K`;
4. `a,d` are nonzero real numbers.

For arbitrary real `b,c,r,s,u,v`, put

`Q = a X^2 + 2 b X Y + c Y^2 + 2 d Y Z + r X + s Y + u Z + v`.       (3.1)

Then `Q` has an essentially bounded density and

`boxed: ||p_Q||_infinity <= 4 sqrt(LK) / sqrt(|a d|).`                (3.2)

In particular, if `X,Y,Z` are three independent ORIGINAL input coordinates with density caps one, then

`boxed: ||p_Q||_infinity <= 4 / sqrt(|a d|).`                         (3.3)

All affine terms are uniform, so after conditioning arbitrary outside ORIGINAL coordinates the same estimate holds whenever the surviving physical principal block has the chain form

```
[[a,b,0],
 [b,c,d],
 [0,d,0]]
```

with `ad!=0`. No spectral-coordinate independence is asserted.

### Proof

Fix `Y=y` outside a null set. Because `X` is independent of the whole pair `(Y,Z)`, conditional on `Y=y` the variable `X` keeps its original density cap one and is independent of `Z|Y=y`.

Write

`U_y = a X^2 + (2by+r)X`,                                           (3.4)

`V_y = (2dy+u) Z`,                                                   (3.5)

and absorb the remaining `y`-dependent term into a translation. Completing the square in (3.4), the density of `U_y` is dominated by the translated one-sided square kernel

`k_a(w)=|a|^(-1/2) |w|^(-1/2) 1_{sgn(a)w>0}`.                       (3.6)

Indeed, at a positive distance `w` from the quadratic vertex the two inverse branches have total Jacobian at most `(|a|w)^(-1/2)`, because the original scalar density is at most one.

For `m_y=2dy+u !=0`, the density of `V_y` has total mass one and cap

`H_y = K/|m_y|`.                                                     (3.7)

For any probability density `h` with `0<=h<=H`, the decreasing-kernel bathtub estimate gives

`sup_t int_0^infinity w^(-1/2) h(t-w) dw
 <= H int_0^(1/H) w^(-1/2)dw
 =2 sqrt(H).`                                                        (3.8)

Therefore, for almost every `y`,

`||p_(Q|Y=y)||_infinity
 <= 2 |a|^(-1/2) sqrt(K) |2dy+u|^(-1/2).`                            (3.9)

The single point where `m_y=0` is irrelevant to the `Y` integral. Average (3.9) with the ACTUAL `Y` density; do not take a supremum in `y`. If a probability density `f` is capped by `L`, another bathtub estimate gives, for every `y0`,

`int f(y)|y-y0|^(-1/2)dy
 <= L int_{-1/(2L)}^{1/(2L)} |z|^(-1/2)dz
 =2 sqrt(2L).`                                                       (3.10)

Since

`|2dy+u|^(-1/2)
 =(2|d|)^(-1/2)|y+u/(2d)|^(-1/2)`,                                  (3.11)

(3.9)-(3.11) yield

`||p_Q||_infinity
 <= 2 |a|^(-1/2) sqrt(K) (2|d|)^(-1/2) 2 sqrt(2L)
 =4 sqrt(LK)/sqrt(|ad|).`                                           (3.12)

This proves the theorem. QED.

### Why this is the requested weighted fiber repair

The conditional cap in (3.9) has a genuine singularity `|2dy+u|^(-1/2)` and therefore has infinite worst-fiber supremum. The proof succeeds only because the original-product weighting is retained and that singularity is integrable against the capped middle-coordinate marginal. Thus the mechanism is exactly “aggregate/average before reciprocal payment,” rather than the refuted dimension-losing fiber-sup route.

## 4. A full-target fixed-matrix application

Let

`B0=[[1,1,0],[1,0,1],[0,1,0]]`, `A=3B0`.                            (4.1)

Then

`X^T A X = 3X^2+6XY+6YZ`.                                           (4.2)

For three independent cap-one inputs, Theorem 3.1 has `a=d=3`, hence

`boxed: ||p_(X^TAX)||_infinity <= 4/3.`                              (4.3)

This is a genuine target instance: the characteristic polynomial of `B0` is

`p(lambda)=lambda^3-lambda^2-2lambda+1`.                             (4.4)

For `|lambda|<=1/3`,

`p(lambda) >= 1-1/27-1/9-2/3 =5/27>0`.                              (4.5)

Because `B0` is symmetric, all three roots are real, so no eigenvalue lies in `[-1/3,1/3]`; therefore all three eigenvalues of `A=3B0` have modulus strictly greater than one. Numerically they are approximately `-3.74094, 1.33513, 5.40581`, but the exact certificate is (4.5).

This application also gives a direct physical-fiber proof of a matrix already covered more abstractly by the newest-Claude physical-pair theorem.

## 5. False intermediate statement and exact repair

The tempting strengthening

> If `X` is an independent cap-one scalar and `(Y,Z)` merely has a joint density capped by one, then the same non-null chain admits a universal density bound.

is false, even if `Z|Y=y` itself has density cap at most one and even when the quadratic matrix has three eigenvalues of modulus greater than one.

### Proposition 5.1 — `QFORM-NEARNULL-JOINT-PAIR-CAP-FALSE-v1`

Keep the fixed matrix `A=3B0` from Section 4. For each integer `N>=16`, let `X` be uniform on `[0,1]` and independent of a pair `(Y,Z)` having joint density one on

`E_N={ e^(-N)/N <= y <= 1/N, 0<=z<=1/(Ny) }`.                       (5.1)

The area of `E_N` is exactly

`int_(e^-N/N)^(1/N) (1/(Ny))dy=1`,                                  (5.2)

so this is a probability density with joint cap one. Its `Y` marginal is

`m_N(y)=1/(Ny)`,                                                     (5.3)

while, conditional on `Y=y`, `Z` is uniform on `[0,1/(Ny)]` and therefore

`||p_(Z|Y=y)||_infinity = Ny <=1`.                                  (5.4)

Thus the only missing piece from Theorem 3.1 is a dimension-free cap on the middle marginal.

Put

`q0=X^2+2XY+2YZ`, so `X^TAX=3q0`.                                   (5.5)

On the event

`X<=1/(4 sqrt(N))`,                                                  (5.6)

we have `Y<=1/N` and `YZ<=1/N`, hence

`0<=q0
 <=1/(16N)+1/(2N^(3/2))+2/N
 <3/N`                                                              (5.7)

for `N>=16`. Consequently

`P(0<=X^TAX<=9/N) >=1/(4 sqrt(N)).`                                  (5.8)

If the weakened interface had an essential density bound `C` independent of `N`, (5.8) would imply

`C >= [1/(4 sqrt(N))]/[9/N]=sqrt(N)/36 -> infinity.`                 (5.9)

Therefore no such universal interface bound exists. QED.

This is **not** a counterexample to QFORM: `Y` and `Z` are dependent. It is a counterexample to a proposed proof reduction that would compress the original product law to a bounded joint density of a projected pair. The repaired statement is Theorem 3.1: one must retain enough one-dimensional product provenance to control both the middle marginal and the conditional transverse density.

The example is especially relevant to the exact-null predecessor. At the null endpoint a dependent-pair weak-L^(3/2) kernel can survive with only a pair-density cap; after a nonzero scalar square/coupling is introduced, a pair joint cap alone can lose the critical middle-coordinate weight by an arbitrarily large factor.

## 6. Real application of the designated partner result

The preceding B06 crossed-star stress family has a cross block with singular values

`(1,1,eps)`, `eps=1/N`,                                              (6.1)

and physical anchors of ordinary range leverage one. Apply fleet03/B06 r24 literally.

Its no-leverage third-singular-value endpoint gives

`||p_Q||_infinity <25/sqrt(|a|eps)=25 sqrt(N/|a|)`.                  (6.2)

This is a valid bound, but it diverges with the vanishing tail and therefore does not close the family uniformly.

On the other hand the partner's aggregate two-curvature currency is excellent:

`Delta_2=e_2(BB^T)=1+2 eps^2`,                                      (6.3)

which stays above one. If its ordinary range-leverage gate held, `QFORM-CROSS-E2-OUTER-SQUARE-v1` would immediately give a dimension-free bound. It does not: the anchors have range leverage one, exceeding `q/2` for every permitted `q<3/2`.

Likewise, for the explicit `N=4096` checker, enforcing the partner ridge leverage gate at an anchor forces the ridge trace below the required `4q/3` threshold. Thus the same family lies precisely between the partner's strong aggregate-curvature currency and its high-leverage gate. This is a concrete inequality-level application: the partner result converts the remaining B06 problem into a product-provenance/high-leverage question rather than a missing-curvature question.

The new physical-chain theorem supplies one such high-leverage payment whenever the survivor can be organized into an ORIGINAL-coordinate chain with `|ad|` bounded below.

## 7. Conditional end-to-end splice and first unpaid implication

A compact corrected proof route is now:

1. Use the newest-Claude volume/Fresnel and physical-pair exits whenever the actual matrix satisfies their gates.
2. In an outer-square branch, use fleet03/B06 r24's aggregate `Delta_2` or ridge `L^3` receiver whenever its leverage/effective-dimension gate holds; do not delete small extra singular directions.
3. In a high-leverage survivor, preserve original-coordinate provenance. If conditioning/grouping yields a chain packet of Theorem 3.1 with `LK` and `(|ad|)^(-1)` universally bounded, pay the singular middle fiber by averaging, giving a universal `L^infinity` exit.
4. Never replace the product packet by “joint pair density capped by one”: Proposition 5.1 shows that interface is false even for the fixed three-large-eigenvalue matrix `3B0`.

Therefore the first unpaid implication for this B06 route is

`QFORM-N3-PRODUCT-CHAIN-OR-VOLUME-v1`:

> In every remaining no-pivot/high-leverage survivor not already paid by the newest-Claude physical-pair/volume exits or the partner r24 aggregate/ridge exits, construct a product-preserving physical/grouped chain for which the middle marginal cap times the conditional transverse cap is universally bounded and `|ad|` is universally bounded below; or derive another already-paid exit.

The counterexample in Section 5 proves that a proof of this implication must use more than a joint two-dimensional density cap. The crossed-star application in Section 6 proves that curvature size alone is also insufficient: high-leverage provenance is the actual outstanding issue.

## 8. Checker and exact outputs

The deterministic checker in this run verifies the exact spectral-gap certificate, the unit-area/conditional-cap construction, the small-ball lower bound at `N=4096`, the `4/3` product-chain constant for `A=3B0`, and the numerical scale of the designated-partner application.

Executed code SHA-256:

`1094228bd9597a027ef7379962accb5597527ae06bd50bfa666243b8ee02fe4b`

Output SHA-256:

`9f24b6e3857a1b8a419ab3c6ac49ed92222fcadde25fd9cd2d766b5bfc6953c9`

Status: `PASS`.

Files in this immutable run directory:

* `CHECKPOINT.md`
* `CHECKER.py`
* `CHECKER_OUTPUT.txt`
* `REPORT.md`

## 9. Honest status

`ESSENTIAL_STEP_APPLIED`: Theorem 3.1 is a rigorous non-null product-preserving curved-fiber payment which explicitly integrates the singular conditioning weight instead of taking a fiber supremum.

`CANDIDATE_REFUTED`: Proposition 5.1 rigorously refutes the stronger joint-pair-density replacement, using a fixed symmetric matrix with all three eigenvalues beyond the target threshold.

The full QFORM conjecture is not proved or disproved. No continuity claim is made. The result has not received the two independent end-to-end reviews required for a full candidate proof.
