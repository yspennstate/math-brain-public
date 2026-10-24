SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B13, 2026-09-23T20:30:16Z.
attacking: convert account02/B13's single-bi-star obstruction into a quantitative relative rank-three collapse of the actual scalar-Schur cross block, while preserving the exact extremal-product reduction.

# account01/B13 — bi-star concentration forces relative rank-three collapse

Programme: `QFORM-DENSITY-3EIG-20260922`. OWNER CONTROL revision `2026-09-22.15`. Assignment: extremal product laws. Execution status: `WITHOUT_VERIFIED_BRAIN`.

**Status.** New proved deterministic exterior-volume lemma plus a target-level slab inequality obtained by applying the latest completed designated partner theorem. Full unrestricted QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Continuity remains separately open.

## 1. Fresh scope and dependencies

Fresh `math-research-brain` main at run start was `f5b1fb16df62f83d216afcdd918156d44ea30d37`. I re-read the current owner control, MANIFEST, CURRENT_RESEARCH, CLAIMS, live CORRECTION_INBOX, MEMORY_PROTOCOL, `scheduled_tasks/PROTOCOL.md`, and the account01/B13 assignment. In particular, none of the following is used: uniform pointwise quadratic oscillatory decay, independence after rotation, arbitrary-joint coarea, projection-density-only pushforward, bounded support diameter, bounded fragment count, or centered/single-interval extremality.

The completed designated partner result used here is account02/B13, source-pinned at

`yspennstate/math-open-problems@e499a26f35ec939d0fae47bbc5ccf8c0b7683516`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/account02-B13-20260923T200130Z/REPORT.md`.

Its Theorem 3.1 (`QFORM-SCALAR-D2-SINGLE-BISTAR-v1`) is the only probabilistic input needed below. For a genuine original-coordinate scalar pivot `d=A_ii != 0`, exact Schur remainder `S`, disjoint original-coordinate banks `I,L`, and

`M=S[I,L]`, `Z_2=e_2(M^T M)>0`,

put

`T_i = rho |d|^(1/2) Z_2^(1/8)`,

where `rho=P{X^T A X in J_0}/|J_0|` is an actual slab ratio. If

`T_i >= C_* := 16 e^(1/4)`,

then under the natural squared-2-minor law of `M` there are a physical row `r in I` and physical column `c in L` satisfying

`P(r in R and c in C) > 1 - C_*/T_i`.                       (1.1)

The partner theorem retains arbitrary self blocks, outside couplings, affine terms, and arbitrary cap-one independent input laws.

## 2. Deterministic theorem: a bi-star in squared 2-minor volume forces rank-three collapse

Let `M` be any real `p x q` matrix with

`Z_2 := e_2(M^T M)
    = sum_{|R|=|C|=2} det(M[R,C])^2 > 0`.                    (2.1)

Define the natural probability law

`mu(R,C) := det(M[R,C])^2/Z_2`.                              (2.2)

For a physical row `r` and column `c`, write

`theta_{r,c} := mu(r in R and c in C)`.                      (2.3)

Let `R_3` denote the set of real matrices of rank at most three, and set the normalized relative rank-three defect

`eta_3(M) := dist_op(M,R_3)/Z_2^(1/4)`.                     (2.4)

### Theorem 2.1 — `QFORM-BISTAR-RELATIVE-RANK3-COLLAPSE-v1`

For every physical row-column pair `(r,c)`,

`boxed: eta_3(M)^4 <= 1-theta_{r,c}.`                        (2.5)

In particular `0<=eta_3(M)<=1`, and

`boxed: theta_{r,c} <= 1-eta_3(M)^4.`                        (2.6)

#### Proof

Let `N=N_{r,c}` be obtained from `M` by zeroing the entire row `r` and the entire column `c`. Then every `2 x 2` minor of `N` meeting row `r` or column `c` vanishes, while every minor avoiding both is unchanged. Therefore Cauchy--Binet gives the exact identity

`e_2(N^T N)
 = sum_{R not containing r, C not containing c} det(M[R,C])^2`.

The event `{r notin R, c notin C}` is contained in the complement of `{r in R, c in C}`, hence

`e_2(N^T N) <= (1-theta_{r,c}) Z_2`.                        (2.7)

Now `H:=M-N` is supported on one row plus one column, so

`rank(H)<=2`.                                                (2.8)

Let `N_1` be a best rank-one approximation to `N` in operator norm. Then `H+N_1` has rank at most three and, by Eckart--Young,

`dist_op(M,R_3) <= ||N-N_1||_op = s_2(N)`.                  (2.9)

If `s_1(N)>=s_2(N)>=...` are the singular values, then

`e_2(N^T N)=sum_{a<b}s_a(N)^2 s_b(N)^2
            >=s_1(N)^2s_2(N)^2
            >=s_2(N)^4`.                                    (2.10)

Combining (2.7)--(2.10),

`dist_op(M,R_3)^4 <= (1-theta_{r,c})Z_2`,                    (2.11)

which is exactly (2.5). QED.

### Exact anchored identity

After permuting the selected row and column first, write

`M = [[m, u^T], [v, N_0]]`.                                 (2.12)

The numerator of `theta_{r,c}` is exactly

`J_{r,c}:=sum_{a,b}(m(N_0)_{ab}-v_a u_b)^2
        = ||mN_0-vu^T||_F^2`.                               (2.13)

Hence, if `m!=0`,

`boxed: J_{r,c}=m^2 ||N_0-vu^T/m||_F^2`,                    (2.14)

where the matrix inside is a **cross-matrix** Schur residual, not automatically a principal Schur complement of the full symmetric coefficient matrix. If `m=0`,

`boxed: J_{r,c}=||u||_2^2 ||v||_2^2`.                       (2.15)

Thus a high joint anchored mass has an exact scalar-anchor-versus-star-star interpretation, without selecting rotated random variables.

## 3. Application of the partner theorem: an actual slab inequality

Keep the target-level scalar-pivot setting of Section 1. Let

`eta := eta_3(M)
       = dist_op(M,R_3)/Z_2^(1/4)`.                          (3.1)

### Theorem 3.1 — `QFORM-SCALAR-SCHUR-RANK3-DEFECT-INEQUALITY-v1`

Every actual slab ratio satisfies

`boxed:
 rho |d|^(1/2) Z_2^(1/8) eta^4 <= 16 e^(1/4).`              (3.2)

Equivalently, whenever `eta>0`,

`boxed:
 rho <= 16 e^(1/4)
        / [ |d|^(1/2) Z_2^(1/8) eta^4 ].`                   (3.3)

Or, in unnormalized form,

`boxed:
 rho |d|^(1/2) dist_op(M,R_3)^4 Z_2^(-7/8)
 <=16 e^(1/4).`                                             (3.4)

#### Proof

Set

`T_i=rho |d|^(1/2)Z_2^(1/8)`.                              (3.5)

If `T_i<C_*`, then Theorem 2.1 gives `eta<=1`, so immediately

`T_i eta^4<C_*`.                                            (3.6)

If `T_i>=C_*`, apply the completed account02/B13 theorem. It supplies physical `r,c` with

`theta_{r,c}>1-C_*/T_i`.                                    (3.7)

The deterministic Theorem 2.1 simultaneously gives

`theta_{r,c}<=1-eta^4`.                                     (3.8)

Thus

`eta^4<C_*/T_i`,                                             (3.9)

and again `T_i eta^4<C_*`. Replacing strict inequalities by `<=` gives the stable statement (3.2). QED.

### Interpretation

A substantial scalar-Schur pair-volume can no longer evade the pair-volume receiver merely by concentrating on a single row-column bi-star. If

`|d|^(1/2) Z_2^(1/8)`

is bounded below while `rho` grows, then the **actual original-coordinate Schur cross block** must satisfy the relative collapse

`boxed:
 eta_3(M)
 <= [16e^(1/4)/(rho |d|^(1/2)Z_2^(1/8))]^(1/4).`            (3.10)

Thus the unpaid high-bi-star chamber becomes a rank-at-most-three cross carrier plus a quantitatively small operator tail *relative to the exterior 2-volume scale*. No coefficient tail is discarded probabilistically.

Moreover, in the partner high-`T_i` branch, (1.1) and the exact identities (2.14)--(2.15) imply, with `delta=C_*/T_i`, either

`|m| ||N_0-vu^T/m||_F > sqrt(1-delta) Z_2^(1/2)`             (3.11)

when `m!=0`, or

`||u||_2 ||v||_2 > sqrt(1-delta) Z_2^(1/2)`                  (3.12)

when `m=0`. This records the residual currency still present at the selected physical anchor; it is not a claim that a principal pivot has already been paid.

## 4. Exact extremal-product transfer

The previously completed B13/product-purification result remains the correct extremal-law reduction: for every nonnegative measurable kernel `K`,

`sup_{0<=f_i<=1, int f_i=1} int K(x) prod_i f_i(x_i) dx
 = sup_{|E_i|=1} int_{prod E_i} K(x) dx`.                    (4.1)

For a fixed slab indicator, every strict witness can be approximated with arbitrarily small loss by bounded finite unions `E_i` of total measure one. There is no optimizer claim, no single-interval or centered-uniform claim, no common diameter bound, and no uniform fragment-count bound.

Consequently Theorem 3.1 is already an explicit geometric product-set sublevel inequality: for arbitrary measurable `|E_j|=1`, if

`rho_E := |{x in prod E_j : x^T A x in J_0}|/|J_0|`,         (4.2)

then the same coefficient-side inequality holds:

`rho_E |d|^(1/2) Z_2^(1/8) eta_3(M)^4 <=16e^(1/4).`          (4.3)

Conversely, any strict arbitrary-density violation of a proposed universal constant transfers, with arbitrarily small ratio loss, to bounded finite-union product indicators before applying the same structural inequality.

## 5. What remains open

This does **not** prove QFORM. The new theorem pays the scalar-pivot pair-volume branch unless the exact Schur cross block becomes relatively rank at most three. A rank-three cross carrier is not itself a density bound under arbitrary same-side curvature and shared original inputs.

The first unpaid implication is therefore

`QFORM-SCALAR-SCHUR-RELATIVE-RANK3-RECEIVER-v1`:

> starting from the rank-three approximation forced by (3.10), retain the operator tail inside a product-preserving estimate and use the third large spectral direction (or an existing grouped-coordinate / rank-two affine half-Riesz receiver) to obtain the missing density smoothing, without rotating the independent coordinates or deleting the tail.

A useful bifurcation is already exact: the selected bi-star anchor has either a nonzero scalar entry and the cross-Schur residual (2.14), or a zero anchor with star-star currency (2.15). These are the next two original-coordinate receivers to test.

No valid counterexample was produced in this run.
