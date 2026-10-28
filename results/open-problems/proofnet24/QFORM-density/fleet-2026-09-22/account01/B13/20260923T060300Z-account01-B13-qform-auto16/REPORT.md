SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B13, 2026-09-23T06:03:00Z.
attacking: recursive tri-hub compression: turn the partner's scalar-Schur E2 slab dichotomy into a quantitative low-rank normal form for any high-ratio product witness.

# account01/B13 auto16 — recursive extremal E2 compression of high-ratio slab witnesses

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Extremal product laws  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED TARGET-RELEVANT SUPPORTING STRUCTURAL THEOREMS / FULL QFORM OPEN / CONTINUITY SEPARATE**

The full arbitrary-dimensional conjecture is not proved here. The result below preserves arbitrary independent original-coordinate laws with density caps one, arbitrary translations and fragmented supports, arbitrary extra spectrum and arbitrary same-side quadratic curvature. No rotation of the random coordinates is used. A low-rank matrix approximation obtained below is a structural certificate only; it is not perturbatively deleted from the quadratic random variable.

## 1. Source boundary and designated-partner theorem actually applied


The designated partner source used at the decisive inequality is

`yspennstate/math-open-problems@892bfe36756e09cbaff3f05070f7a3e20fea0fd1`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260923T040105Z-account02-B13-extremal-r23/REPORT.md`.

Its theorem `QFORM-SCALAR-E2-LINF-OR-TRIHUB-v1` states the following at the scope used here. Choose a nonzero ORIGINAL-coordinate scalar pivot `i`, write

`d=A_ii != 0`,

and let

`S=A_{-i,-i}-A_{-i,i}A_{i,-i}/d`

be the scalar Schur complement. For any disjoint physical banks `I,J` avoiding `i`, put

`M=S[I,J]`,
`E=E_2(M):=e_2(M^T M)=sum_{|P|=|T|=2} det(M[P,T])^2`.

With

`C_* = 29.922421174319`,

one has either

`||p_Q||_infinity <= C_* |d|^(-1/2) E^(-1/8)`,                 (1.1)

or there are physical hub sets `H subset I`, `C subset J`, each of cardinality at most three, such that the squared two-minor mass whose row pair avoids `H` is `<E/4`, and the squared two-minor mass whose column pair avoids `C` is `<E/4`.

I apply that result recursively below to the *same actual slab inequality*. This is not a citation-only use.

The exact extremal-product reduction from my preceding B13 run remains available: for every bounded nonnegative slab kernel, the supremum over cap-one product densities equals the supremum over arbitrary unit-measure product indicators. No interval, centered-uniform, bounded-diameter or fixed-fragment conclusion is used.

## 2. One-step tri-hub compression

Assume the tri-hub branch of the partner theorem. Set

`N=M[I\H,J\C]`.

Every `2x2` minor of `N` avoids `H` on the row side and avoids `C` on the column side. Hence, directly from the two partner mass inequalities,

`boxed: E_2(N) < E/4.`                                          (2.1)

Let the singular values of `N` be `s_1>=s_2>=...`. Then

`E_2(N)=sum_{a<b}s_a^2 s_b^2 >= s_1^2 s_2^2 >= s_2^4`,        (2.2)

so

`s_2(N) < (E/4)^(1/4)=E^(1/4)/sqrt(2).`                        (2.3)

By Eckart--Young there is a rank-one matrix `N_1` for which

`||N-N_1||_op=s_2(N)`.                                         (2.4)

Embed `N_1` back into the original row/column locations and write

`L=P_H M+(I-P_H)M P_C+N_1`.                                    (2.5)

The first term has rank at most `|H|`, the second at most `|C|`, and `N_1` rank at most one. Therefore

`boxed: rank(L)<=7,   ||M-L||_op < E^(1/4)/sqrt(2).}`           (2.6)

This is a deterministic consequence of the partner's tri-hub alternative. No random-coordinate rotation is involved.

## 3. Main theorem: a high slab ratio forces recursive low-rank compression

Fix an interval `J_0` of positive length and let its actual slab ratio be

`R = P{Q in J_0}/|J_0|`.                                       (3.1)

Keep the nonzero scalar pivot `d` and an initial Schur cross block

`M_0=S[I_0,J_0']`, `E_0=E_2(M_0)`.

Define the witness-dependent E2 threshold

`T_d(R) = (C_*/(R sqrt(|d|)))^8`                               (3.2)

and the corresponding operator scale

`tau_d(R)=T_d(R)^(1/4)=C_*^2/(R^2 |d|)`
`          < 895.352/(R^2 |d|).`                               (3.3)

### Theorem 3.1 — `QFORM-SCALAR-E2-WITNESS-RANK-COMPRESSION-v1`

If `E_0=0`, then `M_0` has rank at most one and the original pre-Schur block `A[I_0,J_0']` has rank at most two.

If `E_0>0`, put

`k_max = max(0, ceil(log_4(E_0/T_d(R))))`.                      (3.4)

Then there are cumulative physical hub sets

`H subset I_0`, `C subset J_0'`,

with

`|H|<=3 k_max`, `|C|<=3 k_max`,                                (3.5)

such that the residual Schur block

`N=S[I_0\H,J_0'\C]`

satisfies

`boxed: E_2(N)<=T_d(R),   s_2(N)<=tau_d(R).}`                  (3.6)

Consequently there exists a matrix `L_S` with

`boxed: rank(L_S)<=6 k_max+1,`
`       `||S[I_0,J_0']-L_S||_op<=tau_d(R).`                     (3.7)

Since

`A[I_0,J_0']=S[I_0,J_0'] + A[I_0,i]A[i,J_0']/d`                (3.8)

and the correction in (3.8) has rank at most one,

`boxed: dist_op(A[I_0,J_0'], {rank<=6k_max+2})`
`       `<= C_*^2/(R^2|d|).`                                   (3.9)

#### Proof

Start with the current subblock `M_t` and let `E_t=E_2(M_t)`. If

`E_t > T_d(R)`,                                                 (3.10)

then by definition of `T_d(R)`,

`C_* |d|^(-1/2) E_t^(-1/8) < R`.                               (3.11)

The density branch (1.1) is therefore impossible: it would imply every interval slab ratio, in particular the actual ratio `R`, is at most the left-hand side of (3.11). Thus the designated partner theorem must be in its tri-hub branch. Remove the resulting at-most-three row hubs and at-most-three column hubs. By (2.1),

`E_{t+1}<E_t/4`.                                                (3.12)

Iterate only while (3.10) holds. The process stops after at most `k_max` steps because after `k` tri-hub steps,

`E_k < E_0/4^k`.                                                (3.13)

At stopping, `E_k<=T_d(R)`, which proves the first part of (3.6); (2.2) gives the second. The cumulative hub sets have the size bound (3.5).

As in (2.5), the entries touching cumulative row hubs contribute rank at most `|H|`, those touching cumulative column hubs outside those rows contribute rank at most `|C|`, and a best rank-one approximation to `N` contributes one additional rank. This proves (3.7). Adding the exact rank-one scalar-Schur correction (3.8) proves (3.9). QED.

The cancellation in (3.3) is useful: after recursive extremal compression, the final operator error no longer contains the starting exterior volume `E_0`; it depends only on the observed slab ratio and the physical pivot.

## 4. Actual geometric product-set consequence

Let every input density be an indicator `1_{E_j}` of an arbitrary measurable set of measure one. Then

`R = |{x in product E_j : x^T A x in J_0}|/|J_0|`.             (4.1)

Theorem 3.1 applies verbatim. Conversely, by the exact product-bathtub theorem from the preceding B13 run, any strict violation by arbitrary cap-one product densities can be approximated with zero asymptotic slab-constant loss by such product-indicator witnesses. Thus (3.6)-(3.9) are genuine geometric consequences for the extremal product-set problem, without a single-interval or bounded-fragment assumption.

This is the requested inequality-level application of the designated `account02/B13` result: a large geometric slab ratio forces a quantitative low-rank physical-cross normal form.

## 5. Pair-pivot analogue, including the exact zero-diagonal pair

The preceding B13 run proved the pair version

`||p_Q||_infinity <= C_pair kappa^(-1/2) E^(-1/8)`,
`C_pair=75.41281`,                                              (5.1)

unless the actual pair-Schur `E_2` mass is two-sided tri-hub, where `kappa` is the least singular value of an invertible indefinite ORIGINAL-coordinate principal pair.

Exactly the same stopping argument yields

`T_kappa(R)=(C_pair/(R sqrt(kappa)))^8`,                        (5.2)

and

`tau_kappa(R)=C_pair^2/(R^2 kappa)
              <5687.092/(R^2 kappa).`                          (5.3)

After at most

`k_pair=max(0,ceil(log_4(E_0/T_kappa(R))))`                     (5.4)

tri-hub removals, the pair-Schur cross block is within operator distance `tau_kappa(R)` of rank at most `6k_pair+1`. The exact pair-Schur correction has rank at most two, so the original cross block is within the same distance of rank at most

`boxed: 6k_pair+3.`                                             (5.5)

For the important null-diagonal pair

`B=[[0,b],[b,0]]`,                                              (5.6)

one has `kappa=|b|`, so

`boxed: dist_op(original cross block, rank<=6k_pair+3)`
`       `<=5687.092/(R^2 |b|).`                                (5.7)

This does not close the null-pair branch, but it replaces the abstract repeated tri-hub obstruction by a quantitative high-ratio low-rank normal form.

## 6. What this does and does not solve

The proved gain is structural: repeated failure of the diffuse E2 payment is not an indefinitely complicated product geometry. At slab ratio `R`, every chosen nonzero scalar-pivot Schur cross block can be compressed, after finitely many physical hub removals, to a rank-one tail at operator scale `O((R^2|d|)^(-1))`; an indefinite physical pair gives the analogous `O((R^2 kappa)^(-1))` statement even when both scalar diagonals are zero.

Three limitations remain explicit.

1. The rank count still contains `log_4(E_0/T)`; no universal bound on the starting `E_0` follows from the bare spectral hypothesis in this report.
2. When every usable scalar pivot or indefinite-pair conditioning scale is extremely small, the operator-error bound is weak. This is the genuine near-null physical-pivot chamber.
3. Most importantly, the small operator residual may not be deleted from the random quadratic form on arbitrarily translated fragmented product supports. The live correction against raw slab continuity remains in force.

The first unpaid implication is therefore

`QFORM-HIGHRATIO-COMPRESSED-CROSSBLOCK-CLOSURE-v1`:

combine the witness-dependent rank-compression theorem with the existing all-cut low-cross-rank / finite-grid skeleton, and either convert the resulting finite physical core plus rank-one tails into an already-paid grouped-bank or pair-log mechanism, or construct a genuine product-indicator counterexample. The full conjecture remains OPEN.
