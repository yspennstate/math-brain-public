SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B19, 2026-09-22T19:13:59.911403Z.
attacking: the first surviving O0 aligned/near-singular splice, by paying the exact-rank-two Schur endpoint with a weighted Fourier half-Riesz estimate that allows arbitrary self blocks.

# fleet01/B19 — exact-rank-two cross-bank half-Riesz endpoint

**Run:** `20260922T191359Z-b19-qform-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh owner control:** revision `2026-09-22.14` at the final control refresh; later source-backed corrections override refuted mathematical suggestions in the owner message.  
**Assignment:** Universal proof assembly  
**Outcome:** `ESSENTIAL_STEP_APPLIED / TARGET-LEVEL SUBBRANCH CLOSED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and correction discipline

The target is unchanged: for arbitrary independent real coordinates `X_i` with densities `0<=f_i<=1`, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite bound for the density of `Q=X^TAX`. Continuity is tracked separately.

The full theorem remains **OPEN**. This run does not use the refuted arbitrary-joint rank-three coarea bound, positive conditional projection-density moments, worst scalar-conditioned density supremum, post-rotation independence, law-uniform pointwise quadratic-phase decay, a single-good-minor exhaustion, or the false inference of a rank-two physical cut from high off-diagonal spectral mass.

The new point is that the existing exact cross-bank `L^2` argument, which was previously used only for density when the exact cross rank is at least three, has a useful **rank-two weighted endpoint**: rank two is critical for `L^1` Fourier inversion, but it is already strictly sufficient for the half-Riesz kernel needed behind one genuine scalar square. This endpoint keeps arbitrary within-bank quadratic terms and therefore removes the arbitrary-self-block issue whenever an honest exact-rank-two Schur cross bank has been structurally produced.

## 2. Completed inputs actually used

### 2.1 Current designated partner: fleet02/B19 r16

Canonical source:

`yspennstate/math-open-problems@89a0197f2e9ed58383cdd516eedcc2ecd2145407`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B19/20260922T190733Z-fleet02-B19-qform-r16/REPORT.md`.

The partner proves the exact raw O0 alternatives `R0/R1/R2`, and in particular the Schur-projection inheritance identity. In the `R1` branch, for a physical scalar pivot `a=A_ii!=0`, if `b_i` is its cross row and `N` is the honest physical Schur cross bank, then

`||b_i||^2 e_2(NN^T) >= 1/1536`.                              (2.1)

The partner pays (2.1) when `||b_i||^2<=M` and the selected-side range leverage of `N` is at most `1/2`, obtaining `<19.201 M^(1/8)|a|^(-1/2)`. It leaves the high-leverage / aligned-near-singular regime open.

### 2.2 Exact cross-bank `L^2` factorization

Canonical source: fleet03/B19 r16,

`yspennstate/math-open-problems@9d55d9ca5a7beaed6f693a57bd32b5fc9949b981`.

For disjoint original-coordinate banks `I,J`, after conditioning outside them the residual has

`R_w(U,V)=F_w(U)+2U^T C V+G_w(V)+c_w`,                        (2.2)

with arbitrary quadratic-affine `F_w,G_w`. If `C` has exact rank `r`, the proof gives before the final `L^1` step

`|eta_w(t)| <= min(1, pi^(r/2) e^(r/2) |t|^(-r/2) Pi_r(C)^(-1/2))`  (2.3)

for general banks. If one active bank consists of exactly `r` original physical coordinates, `e^(r/2)` improves to `e^(r/4)`; if both do, it improves to `1`. These pointwise inequalities are valid also at `r=2`; only the density conclusion in that report required `r>2`.

### 2.3 Half-Riesz Fourier identity and scalar-pivot transducer

Canonical source: fleet03/B03 r17,

`yspennstate/math-open-problems@924b3c4c70f86a64402863fe228f641bf3db60b2`.

For any real random variable `R` with characteristic function `eta`,

`H_(1/2)(R):=sup_y E|R-y|^(-1/2)
 <= sqrt(2/pi) int_0^infinity t^(-1/2)|eta(t)|dt`.             (2.4)

And if a genuine original coordinate gives

`Q=a(X_0+h(Z))^2+R(Z)`, `a!=0`,                               (2.5)

then

`||p_Q||_infinity <= |a|^(-1/2) H_(1/2)(R)`.                  (2.6)

No independence after a spectral rotation is used in (2.4)-(2.6).

## 3. New theorem: the rank-two cross-bank weighted endpoint

Let (2.2) hold and assume

`rank(C)=2`, `s_1(C),s_2(C)>0`, `Pi=s_1(C)s_2(C)`.             (3.1)

### Theorem 3.1 — `QFORM-EXACT-RANK2-CROSS-HALF-RIESZ-v1`

For completely arbitrary within-bank quadratic-affine terms, arbitrary signs, arbitrary outside conditioning, and arbitrary independent cap-one marginal laws,

`boxed(H_(1/2)(R) <= 4 sqrt(2e) Pi^(-1/4).)`                  (3.2)

If one active bank consists of exactly two original physical coordinates, the sharper bound is

`boxed(H_(1/2)(R) <= 4 sqrt(2) e^(1/4) Pi^(-1/4).)`           (3.3)

If both active banks consist of exactly two original physical coordinates,

`boxed(H_(1/2)(R) <= 4 sqrt(2) Pi^(-1/4).)`                    (3.4)

Numerically the three coefficients are respectively

`9.326575926388497`, `7.263544634846275`, `5.656854249492381`.

#### Proof

Set `r=2` in the exact cross-bank factorization (2.3). In the general-bank case,

`|eta_w(t)| <= min(1, A/|t|)`,

`A=pi e Pi^(-1/2)`.                                          (3.5)

The outside mixture obeys the same majorant. Insert (3.5) into (2.4). The weighted integral is exact:

`int_0^infinity t^(-1/2) min(1,A/t) dt
 =int_0^A t^(-1/2)dt + A int_A^infinity t^(-3/2)dt
 =4 sqrt(A)`.                                                 (3.6)

Therefore

`H_(1/2)(R)
 <=4 sqrt(2/pi) sqrt(pi e Pi^(-1/2))
 =4 sqrt(2e) Pi^(-1/4)`,                                     (3.7)

which proves (3.2).

If one bank consists of exactly two original coordinates, (2.3) has `A=pi sqrt(e) Pi^(-1/2)`, giving (3.3). If both do, `A=pi Pi^(-1/2)`, giving (3.4). QED.

### Why rank two is enough here but not for direct density inversion

At exact cross rank two the characteristic majorant is `O(|t|^-1)`, so `int |eta(t)|dt` is critical and may diverge logarithmically. The half-Riesz transform inserts `|t|^-1/2`; the tail becomes `t^-3/2`, which is integrable. Thus no third mixed direction is being silently invented: the genuine third smoothing resource is the **outer physical square** in (2.5).

## 4. New scalar-pivot theorem with arbitrary self blocks

Combine Theorem 3.1 with (2.6).

### Theorem 4.1 — `QFORM-SCALAR-PIVOT-EXACT-RANK2-CROSS-v1`

Let `a=A_00!=0` be an original-coordinate scalar pivot and let `S` be its exact Schur complement. Suppose that after conditioning any irrelevant outside coordinates, `S` contains disjoint original-coordinate banks with exact-rank-two cross block `C`. Then

`boxed(||p_Q||_infinity
 <=4 sqrt(2e)|a|^(-1/2)[e_2(CC^T)]^(-1/8).)`                 (4.1)

Here `e_2(CC^T)=(s_1s_2)^2` because `rank C=2`. All self blocks on both banks are arbitrary.

If the selected side of `C` is exactly a physical two-row bank, then

`boxed(||p_Q||_infinity
 <=4 sqrt(2)e^(1/4)|a|^(-1/2)[det(CC^T)]^(-1/8).)`           (4.2)

The theorem proves essential boundedness; continuity is not claimed from this half-Riesz splice alone.

This is the desired analytic removal of the **arbitrary two-row self block** at the exact-rank-two endpoint. No zero-self hypothesis, sign assumption on that self block, or reciprocal single column minor appears.

## 5. Actual application of the designated partner r16 inequality

Use the partner's honest physical Schur bank (2.1). Assume its stated moderate-row subbranch

`||b_i||^2<=M`,                                               (5.1)

but **do not** assume its selected-side range leverage is at most `1/2`. If instead

`rank(N)=2`,                                                  (5.2)

then (2.1) gives

`e_2(NN^T)>=1/(1536M)`.                                      (5.3)

Apply Theorem 4.1 to the actual Schur residual:

`||p_Q||_infinity
 <=4sqrt(2e) 1536^(1/8) M^(1/8)|a|^(-1/2)`

`boxed( ||p_Q||_infinity
 <23.336 M^(1/8)|a|^(-1/2). )`                               (5.4)

The numerical coefficient is `23.335716073732943`.

Thus the current partner's `R1` branch is now paid in two complementary regimes:

- selected-side range leverage `<=1/2`: partner/fleet03-B03 payment `<19.201 M^(1/8)|a|^(-1/2)`;
- **exact Schur cross rank two, with arbitrary leverage:** new payment (5.4).

The same calculation applies to the partner's `ALIGNED2` obstruction whenever its honest Schur cross bank has exact rank two and `||B_Cu||^2<=M`: the aligned factor gives `e_2>=1/(1536M)`, and (5.4) follows. This is an actual use of the partner's new Schur-projection inheritance; no projected raw bank is renamed physical without that identity.

## 6. Application to the current near-coloop pair currency: fixed-packet endpoint

The newest fleet03/B08 near-coloop theorem gives, at its fine-scale residual,

`sum_(k!=j) det(H[{j,k}]H[{j,k}]^T)
 > delta_0 gamma^4`,                                         (6.1)

where

`delta_0=4191/281804800`.                                    (6.2)

Equation (6.1) is an aggregate over `k`; it does **not** by itself give one dimension-free fixed pair, and I do not make that invalid inference.

However, if structural work produces a fixed physical pair `P={j,k}` behind the same outer pivot with

`det(H_P H_P^T)>=delta gamma^4`,                              (6.3)

then (4.2) immediately pays that endpoint with arbitrary pair self block:

`||p_Q||_infinity
 <=4sqrt(2)e^(1/4) delta^(-1/8) / sqrt(|a|gamma)`.            (6.4)

At `delta=delta_0`, the coefficient is

`29.147576466060368`.                                        (6.5)

Thus **self curvature is no longer the analytic obstruction once a fixed two-row packet exists**. The surviving issue is genuinely the dimension-free conversion of aggregate `sum_k` pair currency into an admissible grouped/ridge payment, not removal of the two-row self block.

## 7. Compact conditional proof assembly after this run

A correction-safe full-proof tree can now be written as follows.

1. **Low off-diagonal branch.** The current B19 low-offdiagonal theorem pays `s_2(A-diag A)<=499/1000` with a universal bound `<84`.
2. **High off-diagonal branch.** Use the source-backed third-compound overlap reduction into O0/O1/O2/O3; do not infer a rank-two cut merely from large `s_2`.
3. **O0 diffuse and three-heavy states.** The completed ridge results pay the diffuse states; fleet03/B19 r17 pays every state with at least three `3/4`-heavy rows by `12sqrt(e)<19.785`.
4. **O0 one/two-heavy raw states.** Apply designated partner fleet02/B19 r16. It gives `R0/R1/R2`, exact Schur-projection inheritance, pays `R0-GOOD3`, pays the diffuse `R1` E2 branch, and pays every definite two-coordinate self pair.
5. **New exact-rank-two endpoint.** Whenever the partner's honest Schur E2 bank has exact rank two, Theorem 4.1 pays it with no leverage or self-block condition. In particular (5.4) closes the exact-rank-two part of `R1` and the bounded-aligned-vector part of `ALIGNED2`.
6. **Remaining O0 debt.** The surviving E2 bank therefore has rank at least three *and* lies outside the already-paid diffuse-leverage gate, or it is the partner's R2 near-singular/indefinite state with only one-direction honest Schur currency. The B08 near-coloop theorem supplies aggregate pair-volume currency but not one fixed pair.
7. **O1/O2/O3.** Their aggregate overlap packets still require their already-identified product-preserving analytic splices; nothing here claims them paid.

Conditional on one structural lemma that converts the remaining high-leverage E2 / near-coloop aggregate into either (i) a fractional-ridge half-Riesz certificate, (ii) an exact-rank-two fixed/grouped bank of dimension-free strength, or (iii) an unconditional E3 bank, the O0 branch closes. The rest of the full theorem then reduces to the corresponding O1/O2/O3 aggregate splices already tracked by the fleet.

## 8. First essential missing implication

The first missing inequality is now sharper than “arbitrary self-block splice”:

### `QFORM-O0-HIGHRANK-E2-NEARCOLOOP-GROUPING-v1`

For the honest physical Schur cross bank `N` furnished by fleet02/B19 r16, in the surviving regime

`rank(N)>=3`, selected-side leverage `>1/2`, and an E2/near-coloop aggregate lower bound, prove a product-preserving half-Riesz estimate of the scale

`H_(1/2)(R) <= C [e_2(NN^T)]^(-1/8)`                         (8.1)

or prove an exhaustive alternative that sends the state to a fixed two-row packet, a fractional-ridge state, or an E3 bank with universal constants.

Equation (8.1) is already proved by fleet03/B03 under leverage `<=1/2`, and this run proves the exact-rank-two endpoint with **no** leverage hypothesis. What remains is specifically the **rank-at-least-three, high-leverage, near-coloop interpolation**. The source-backed B08 aggregate

`sum_(k!=j)sum_(r<s) det H[{j,k},{r,s}]^2 > delta_0 gamma^4`

is the concrete currency that must be consumed without selecting one reciprocal tiny pair.

This is the next derivation target. The full QFORM theorem is not yet proved or disproved.

## 9. Continuity

The new weighted endpoint establishes essential boundedness after the scalar-pivot transducer. It does **not** by itself prove a continuous representative. Continuity remains available on the already-completed exact-rank `r>=3`, zero-self grouped, diffuse ridge, and other branches whose source theorems explicitly state `C_0`; it remains separate on this new half-Riesz endpoint.
