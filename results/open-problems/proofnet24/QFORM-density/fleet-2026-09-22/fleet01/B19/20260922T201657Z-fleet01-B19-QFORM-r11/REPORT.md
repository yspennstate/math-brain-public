SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B19, 2026-09-22T20:16:57Z.
attacking: the normalized Schur half-Riesz core — aggregate a whole zero-self physical cross bank before inversion, then splice the resulting Frobenius bound into the partner's scalar-Schur route.

# fleet01/B19 — Frobenius zero-self half-Riesz transducer

**Run:** `20260922T201657Z-fleet01-B19-QFORM-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15` at the prepublication refresh  
**Assignment:** Universal proof assembly  
**Outcome:** `ESSENTIAL_STEP_APPLIED / TARGET-LEVEL SUBBRANCH CLOSED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and correction discipline

The unrestricted target remains open: for arbitrary independent real coordinates with one-dimensional densities at most one and arbitrary real symmetric `A` having at least three eigenvalues of absolute value at least one, prove one universal finite essential bound for the density of `X^T A X`. Continuity is tracked separately.

This report uses no post-rotation independence, no arbitrary-joint rank-three coarea bound, no positive conditional projection-density moment, no law-uniform pointwise quadratic-phase decay, no worst conditional projection-density supremum, and no inference of one fixed coordinate minor from an aggregate exterior packet. Every conditioning is on disjoint original-coordinate banks.

The new theorem is deliberately a **half-Riesz** estimate rather than a direct density theorem. It pays a whole physical cross bank through its Frobenius norm when the active source bank has exactly zero quadratic self block. Unlike the existing grouped zero-self density theorem, it does not require rank at least two or a product of nonzero singular values; rank one and arbitrarily diffuse high rank are included. This is useful precisely behind the genuine scalar-square transducer in the live Schur route.

## 2. Completed inputs actually used

### 2.1 Designated partner fleet02/B19 r18

Canonical source:

`yspennstate/math-open-problems@a8d94490f91131df5f18a3fe9e58087077458835`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B19/20260922T195812Z-fleet02-B19-qform-r18/REPORT.md`.

The partner proves `QFORM-SCHUR-HALFRIESZ-NORMAL-FORM-v1`: the universal affine/singular Schur statement with `s_2(S)>=1` has exactly the same best constant as the homogeneous invertible normal form `S` invertible, `s_2(S)=1`, `ell=0`, `c=0`. It also records the dependence-safe scalar-square transducer

`||p_Q||_infinity <= |a|^(-1/2) H_(1/2)(R)`                    (2.1)

for a genuine original-coordinate pivot

`Q=a(X_i+g)^2+R`.

Thus any product-preserving half-Riesz estimate for an exact Schur residual becomes an actual density estimate for the parent.

### 2.2 Partner r17 scalar-Schur inheritance

Canonical source:

`yspennstate/math-open-problems@b8afb539ea7217d2c8d2336e31f53614fb2241ee`.

For every nonzero original-coordinate scalar pivot `a=A_ii`, its exact Schur complement `S` satisfies

`s_2(S)>=s_3(A)>=1`.                                           (2.2)

The same run gives the S0/S1/S2 physical-overlap trichotomy and identifies, in S1, the exact identity

`det S[{k,i},{k,j}] = S_kk S_ij - S_ki S_kj`.                 (2.3)

At a zero-self row `S_kk=0`, the shared minor is therefore the genuine star product `-S_ki S_kj`; hidden curvature is not discarded.

### 2.3 fleet03/B07 colored exterior matching

Canonical source:

`yspennstate/math-open-problems@4ee3cfb2d6682d5be670819cf5de173ad859f6cf`.

Applied to the partner S0 resource `e_2(BB^T)>=1/48`, it gives four disjoint original-coordinate banks and two matching cross blocks `B_1,B_2` satisfying

`||B_1||_F^2 ||B_2||_F^2 >= 1/768`,                           (2.4)

plus rainbow second-minor mass at least `1/192`. No single local minor is inferred from (2.4).

### 2.4 One-dimensional product-projection cap

The source-pinned product-projection theorem used by fleet02/B19 gives: if `u` is a unit vector and `Z` has independent cap-one coordinates, then `u^T Z` has a density bounded by

`C_lin = sqrt(e)`.                                             (2.5)

All constants below are written first in terms of `C_lin`, then specialized to (2.5). A sharper classical `sqrt(2)` scalar cap would improve constants only; it is not needed.

## 3. A scalar capped-density half-Riesz lemma

### Lemma 3.1

If a real random variable `Y` has a density bounded by `M`, then

`sup_t E |Y-t|^(-1/2) <= 2 sqrt(2M)`.                          (3.1)

#### Proof

For every `r>0`,

`P(|Y-t|<r) <= min(1,2Mr)`.                                   (3.2)

Layer cake with `s=|Y-t|^(-1/2)` gives

`E|Y-t|^(-1/2)
 <= integral_0^infinity min(1,2M s^(-2)) ds`.

Splitting at `s_0=sqrt(2M)` gives

`s_0 + 2M/s_0 = 2 sqrt(2M)`.                                  (3.3)

No regularity beyond the density cap is used. QED.

## 4. New aggregate inverse-radius inequality

Let `B` be a nonzero real `m x n` matrix, let `Z in R^n` have independent cap-one coordinates, and let `h in R^m` be arbitrary.

### Theorem 4.1 — `QFORM-FROBENIUS-INVERSE-RADIUS-v1`

`boxed(
 E ||BZ+h||_2^(-1/2)
 <= 2 sqrt(2) C_lin^(1/2) ||B||_F^(-1/2).
)`                                                            (4.1)

With `C_lin=sqrt(e)`,

`E ||BZ+h||^(-1/2)
 <= 2 sqrt(2) e^(1/4) ||B||_F^(-1/2).`                        (4.2)

This estimate is dimension-free, translation-uniform, and uses the whole Frobenius bank before any reciprocal is taken.

#### Proof

Let `Theta` be uniform on the Euclidean sphere `S^(m-1)` and put

`c_m = E |Theta_1|^(-1/2) < infinity`.                         (4.3)

Rotational invariance gives, for every nonzero `y in R^m`,

`||y||^(-1/2)
 = c_m^(-1) E_Theta |Theta^T y|^(-1/2).`                       (4.4)

For fixed `theta`, put `w=B^T theta`. If `w!=0`, the scalar random variable

`theta^T(BZ+h)=w^T Z+theta^T h`

has density cap at most `C_lin/||w||`. Lemma 3.1 therefore gives

`E_Z |theta^T(BZ+h)|^(-1/2)
 <=2 sqrt(2) C_lin^(1/2) ||B^T theta||^(-1/2).`                (4.5)

The set of `theta` with `B^T theta=0` has sphere measure zero unless `B=0`, which is excluded. Tonelli and (4.4) reduce the theorem to

`E_Theta ||B^T Theta||^(-1/2)
 <= c_m ||B||_F^(-1/2).`                                      (4.6)

To prove (4.6), let `s_1,...,s_r` be the singular values of `B` and append zeros to length `m`. Set `a_j=s_j^2`, so

`sum_j a_j = ||B||_F^2 =: A`.

By sphere invariance,

`E_Theta ||B^T Theta||^(-1/2)
 = F(a_1,...,a_m)`

with

`F(a)=E_Theta (sum_j a_j Theta_j^2)^(-1/4).`                   (4.7)

For every fixed `Theta`, the map `a -> (sum a_j Theta_j^2)^(-1/4)` is convex on the positive cone. Averaging preserves convexity, and exchangeability of the sphere makes `F` symmetric. Hence `F` is Schur-convex. Among nonnegative vectors with sum `A`, the vector `(A,0,...,0)` majorizes every other vector, so

`F(a) <= F(A,0,...,0)
 = A^(-1/4) E|Theta_1|^(-1/2)
 = c_m ||B||_F^(-1/2).`                                      (4.8)

This is (4.6), and (4.1) follows. QED.

### Structural meaning

The worst singular-value arrangement for this negative inverse-radius moment is rank one. Diffusing the same Frobenius mass over many singular directions can only improve the estimate. This is exactly the direction needed for the fleet's matching-bank packets, where selecting one singular direction can lose dimension-dependent factors.

## 5. New zero-self Frobenius half-Riesz theorem

Let `X in R^m`, `Z in R^n`, and `W` be disjoint original-coordinate banks. Their coordinates are mutually independent and have density caps one. Let `B` be a nonzero `m x n` matrix, let `h(W) in R^m` be arbitrary measurable, and let `G(Z,W)` be an arbitrary real measurable function. Consider

`R = 2 X^T(BZ+h(W)) + G(Z,W).`                                (5.1)

Thus the physical self quadratic block on the active source bank `X` is exactly zero. All tail self curvature, target shifts, outside couplings entering `h(W)`, and all signs are retained.

### Theorem 5.1 — `QFORM-ZERO-SELF-FROBENIUS-HALFRIESZ-v1`

`boxed(
 H_(1/2)(R):=sup_t E|R-t|^(-1/2)
 <= 4 sqrt(2) C_lin ||B||_F^(-1/2).
)`                                                            (5.2)

Using the completed cap `C_lin=sqrt(e)`,

`boxed(
 H_(1/2)(R)
 <=4 sqrt(2e) ||B||_F^(-1/2)
 =9.3265759263... ||B||_F^(-1/2).
)`                                                            (5.3)

The bound holds for rank one, arbitrary finite rank, and arbitrary dimension.

#### Proof

Fix `z,w`. Put

`c=Bz+h(w)`.

Conditioned on `z,w`, the random variable in (5.1) is the scalar linear form

`2 c^T X + constant`.

Its density is bounded by `C_lin/(2||c||)`. Applying Lemma 3.1 gives, uniformly in the constant and in `t`,

`E_X |R-t|^(-1/2)
 <= 2 sqrt(2) [C_lin/(2||c||)]^(1/2)
 = 2 C_lin^(1/2) ||c||^(-1/2).`                               (5.4)

Now condition on `W=w` and average over `Z`. Theorem 4.1, uniformly in the translation `h(w)`, gives

`E_Z ||BZ+h(w)||^(-1/2)
 <=2 sqrt(2) C_lin^(1/2)||B||_F^(-1/2).`                       (5.5)

Multiplying (5.4) and (5.5), then averaging over `W`, yields

`H_(1/2)(R)
 <=4 sqrt(2) C_lin ||B||_F^(-1/2)`.                           (5.6)

QED.

### Corollary 5.2 — a fixed zero-self Schur star

If a symmetric Schur residual `S` has a physical coordinate `k` with

`S_kk=0`, `beta=||S_{k,-k}||_2>0`,                            (5.7)

then, with arbitrary affine terms allowed,

`H_(1/2)(Z^T S Z+affine)
 <=4sqrt(2e) beta^(-1/2).`                                    (5.8)

If a genuine outer original-coordinate square pivot has coefficient `a!=0`, partner equation (2.1) therefore yields the actual density inequality

`boxed(
 ||p_Q||_infinity
 <=4sqrt(2e) |a|^(-1/2) beta^(-1/2).
)`                                                            (5.9)

This pays the exact-zero row endpoint without selecting a single incident edge.

### Corollary 5.3 — a fixed S1 zero-self aggregate packet

For a fixed zero-self row `k`,

`sum_(i,j != k) [det S[{k,i},{k,j}]]^2
 = sum_(i,j != k) S_ki^2 S_kj^2
 = beta^4.`                                                    (5.10)

Thus if a source-valid structural step gives a fixed `k` with the left side at least `eta`, then

`H_(1/2)(S) <=4sqrt(2e) eta^(-1/8)`,                           (5.11)

and a parent scalar pivot `a` gives

`||p_Q||_infinity <=4sqrt(2e)|a|^(-1/2)eta^(-1/8)`.           (5.12)

The aggregate at one star is paid before choosing `i,j`.

## 6. Actual application of completed peer mathematics: high-leverage S0 zero-self matching endpoint

Apply fleet03/B07's completed colored-exterior extraction to the partner's exact S0 resource. It gives disjoint matching cross blocks `B_1,B_2` with (2.4). Write

`F_r=||B_r||_F`.

Then

`F_1 F_2 >= 768^(-1/2)`,

hence

`max(F_1,F_2) >= 768^(-1/4).`                                 (6.1)

Suppose the source bank of a block realizing the maximum in (6.1) has zero Schur self block. (In particular, this holds if both matching source banks have zero self blocks.) Theorem 5.1 gives directly, without a rank or leverage hypothesis,

`H_(1/2)(Z^T S Z+affine)
 <=4sqrt(2e) 768^(1/8)
 =21.3989459907... .`                                         (6.2)

Now apply the designated partner fleet02/B19 scalar-square transducer (2.1). For the genuine parent pivot,

`boxed(
 ||p_Q||_infinity
 <=21.399 |a|^(-1/2).
)`                                                            (6.3)

In the source-valid subbranch `|a|>=1/4`, this is

`boxed(||p_Q||_infinity <42.798.)`                            (6.4)

This is an actual target-level payment of a portion of the previously unpaid high-leverage S0 matching-bank branch. It is complementary to the existing rank-two exact-cross theorem: (6.2) remains valid if the strong matching block has rank one, and its cost depends on the aggregate Frobenius norm rather than a reciprocal local determinant.

## 7. Compact conditional end-to-end proof map

The live correction-safe proof tree can now be assembled as follows.

1. Use the completed low-offdiagonal, ridge, and third-compound reductions at their exact scopes. Do not infer a rank-two physical cut merely from spectral offdiagonal mass.
2. In O0, use the completed three-heavy-row theorem; only the at-most-two-heavy states enter the scalar-Schur machinery.
3. Whenever a genuine nonzero original-coordinate pivot is structurally available, form the exact Schur complement. Partner r17 gives `s_2(S)>=1` and the S0/S1/S2 overlap trichotomy.
4. Partner r18 removes affine terms, nullspaces, and scale as separate half-Riesz debts: it is enough to solve the homogeneous invertible `s_2=1` core.
5. Diffuse S0 is already paid. Exact-rank-two cross banks with arbitrary self blocks are already paid. The present theorem additionally pays the S0 matching-bank endpoint whenever a sufficiently strong matching source block is exactly zero-self, even at rank one, through (6.2)-(6.4).
6. In S1, every fixed zero-self star carrying dimension-free aggregate overlap mass is paid by (5.10)-(5.12); no incident edge need be selected.
7. Partner r18 pays every exposed pair of disjoint aggregate square channels, including the source-valid S2 block adversary.
8. Conditional on a remaining **arbitrary-self matching-bank transducer** for high-leverage S0 / curved S1 / genuinely coupled S2, plus the already-tracked no-usable-scalar-pivot parent descent, the normalized Schur half-Riesz theorem closes; the genuine outer square then gives a universal parent density bound.

The new theorem removes one possible source of dimension loss: a zero-self cross bank no longer needs a fixed singular direction, fixed minor, or rank-two determinant. The unresolved content is exactly how to exploit the same Frobenius/matching currency when the active source bank carries nonzero quadratic self curvature.

## 8. First essential missing inequality after this run

The first missing analytic implication is now the following sharpened form of the partner/fleet debt.

### `QFORM-ARBITRARY-SELF-FROBENIUS-MATCHING-HALFRIESZ-v1` — OPEN

In the normalized invertible Schur core `s_2(S)=1`, suppose the completed exterior extraction gives disjoint original-coordinate matching banks with

`||B_1||_F^2 ||B_2||_F^2 >= 1/768`.                           (8.1)

Prove a dimension-free `H_(1/2)` estimate while retaining the two active source self blocks, **or** prove a product-preserving exhaustive alternative sending the state to one of the already-paid branches: a genuine scalar-Schur descent with bounded pivot, an exact-rank-two cross bank, a ridge/diffuse certificate, two disjoint square channels, or a zero-self source bank paid by Theorem 5.1.

A naive deletion of the self blocks is invalid: they can shift the critical set of each active linear channel and may contain the very curvature that prevents a rank-one singularity. What is now proved is the exact endpoint at self block zero, with a bound depending only on Frobenius currency and no rank assumption.

A second still-open structural issue is that the S1 global overlap sum may be spread over many zero-self stars. Equation (5.10) pays a **fixed** star aggregate exactly, but the fleet still needs a source-valid grouping/charging argument if no single star carries universal mass.

The full QFORM theorem is therefore **not** proved or disproved by this run.

## 9. Continuity

The new result is a half-Riesz bound. After the partner scalar-square transducer it gives an essential `L^infinity` density bound for the parent branch, but this report does not prove a continuous representative there. Continuity remains a separate tracked obligation, exactly as required by the programme.
