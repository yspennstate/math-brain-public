SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B12, 2026-09-22T22:54:40Z.
attacking: rank-reserve stability for arbitrary added eigenvalues: spend one extra singular direction per arbitrary low-rank spectral change, while charging only the perturbation seen by a protected physical two-bank pair.

# QFORM B12: rank-reserve / pair-compression stability under arbitrary spectral changes

## Status and first unpaid implication

**Status:** PROVED SUPPORTING STABILITY THEOREM. The full conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

This run proves a complementary additional-eigenvalue theorem to the completed fleet03/B12 finite-small-tail result. The new point is that an added rank-`r` symmetric perturbation may have **arbitrarily large operator norm and arbitrary signs**. Instead of paying its full spectral leakage, we spend `r` pre-existing singular directions and charge only what the perturbation does to one protected physical two-bank pair.

**First unpaid implication:** the bare hypothesis `s_3(A)>=1` still does not force a quantitatively nonsingular two-bank pair together with the required reserve. A full proof must extract such a protected pair/reserve, or switch to one of the already-paid diffuse/ridge/grouped-bank/physical-triple branches, before reciprocal pair conditioning is paid.


## Source-valid completed partner theorem actually applied

The designated partner fleet03/B12 has the completed theorem

`QFORM-TWO-BANK-THIRD-SOURCE-ARBITRARY-COMPLETION-v1`

at

`yspennstate/math-open-problems@e71ed8023266f157a6f5c7a04ea6f9c53acc59c5`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260922T214833Z-qform-eigenvalue-r18/REPORT.md`.

For two disjoint normalized original-coordinate scalar banks `Y_1,Y_2`, an arbitrary additional original-coordinate core `Z`, and arbitrary outside completion, write the reduced core matrix as `H` and its leading bank pair as `B`. If

`s_3(H)>=s>0`

and `B` is invertible indefinite, with

`D=|det B|`, `kappa=sigma_min(B)`,

then

`||p_Q||_infinity <= 6*400^(1/3) (D^2 kappa s)^(-1/6)`.        (P)

If `B` is definite, then

`||p_Q||_infinity <= 2*pi/sqrt(|det B|)`.                       (P-def)

The theorem already absorbs arbitrary outside spectrum and cross coupling by the fleet04/B12 mixed-norm shear compiler; no independence of the outside quadratic remainder is used.

I also read the newer fleet03/B12 result

`QFORM-FINITE-SMALL-SPECTRAL-TAIL-ARBITRARY-COMPLETION-v1`

at `yspennstate/math-open-problems@a069e66a087a471e0a4b0a23b909c0d8ba6a1e1f`, path
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260922T225241Z-qform-eigenvalue-r19/REPORT.md`. It controls a fixed finite physical packet when the fourth and later in-packet singular values are small. The theorem below is complementary: it allows an arbitrarily large rank-`r` change by paying `r` extra singular-value reserve directions.

## 1. Rank-`r` singular-value reserve

### Lemma 1 — low-rank perturbations remove at most their rank in the singular-value list

Let `H_0,E` be real matrices of the same size with

`rank(E)<=r`.

Then for every `k` for which the right side is defined,

`s_k(H_0+E) >= s_(k+r)(H_0)`.                                  (1.1)

In particular,

`boxed(s_3(H_0+E) >= s_(3+r)(H_0)).`                            (1.2)

### Proof

The standard singular-value Weyl inequality says

`s_(k+r)(H_0) <= s_k(H_0+E) + s_(r+1)(-E)`.

Because `rank(E)<=r`, `s_(r+1)(E)=0`. Hence (1.1). QED.

This is the key additional-eigenvalue payment: the perturbation norm never appears. A rank-`r` change can destroy at most `r` singular directions, no matter how large its nonzero eigenvalues are.

## 2. Pair-compression stability

Let `B_0` be a real symmetric invertible `2 x 2` matrix and put

`beta_0=sigma_min(B_0)>0`.

Let `F` be any symmetric `2 x 2` perturbation with

`delta=||F||_op < beta_0`.                                      (2.1)

Then

`sigma_min(B_0+F) >= beta_0-delta`.                             (2.2)

Moreover `B_0+tF` is nonsingular for every `0<=t<=1`, because

`sigma_min(B_0+tF)>=beta_0-t delta>0`.

Therefore `B_0+F` has the same inertia as `B_0`.

If `B_0` is indefinite, then `B=B_0+F` is indefinite and

`|det B| >= (beta_0-delta)^2`,
`kappa=sigma_min(B) >= beta_0-delta`.                           (2.3)

If `B_0` is definite, it remains definite and

`|det B| >= (beta_0-delta)^2`.                                 (2.4)

No bound on the perturbation outside the two-bank compression is imposed.

## 3. Main theorem — rank reserve plus protected pair

### Theorem — `QFORM-RANK-RESERVE-PAIR-COMPRESSION-STABILITY-v1`

Use the partner's original-coordinate two-bank setup. Thus `T_1,T_2,K,R` are pairwise disjoint sets of ORIGINAL coordinates, `Y_j=u_j^T X_(T_j)` are normalized scalar banks, `Z=X_K`, `W=(Y_1,Y_2,Z)`, and the full quadratic form has the factorization

`Q = W^T H W + 2 W^T C R + psi(R)`,                             (3.1)

with arbitrary `C` and arbitrary measurable `psi` (in particular an arbitrary outside quadratic form).

Suppose a protected base reduced core `H_0` satisfies

`s_(3+r)(H_0) >= s_0 > 0`                                      (3.2)

for some integer `r>=0`. Let its leading bank pair be `B_0` and put

`beta_0=sigma_min(B_0)>0`.

Now add **any symmetric reduced-core perturbation** `E` satisfying

`rank(E)<=r`,                                                   (3.3)

with arbitrary sign pattern and arbitrary operator norm. Let

`F=E_[1,2;1,2]`,
`delta=||F||_op < beta_0`.                                      (3.4)

Set `H=H_0+E` and allow the outside matrix `C` and outside remainder `psi` in (3.1) to be completely arbitrary.

Then `Q` has an essentially bounded density. More precisely:

### Indefinite protected pair

If `B_0` is indefinite, then

`boxed(||p_Q||_infinity
 <= 6*400^(1/3) [ (beta_0-delta)^5 s_0 ]^(-1/6).)`              (3.5)

### Definite protected pair

If `B_0` is positive or negative definite, then

`boxed(||p_Q||_infinity <= 2*pi/(beta_0-delta).)`               (3.6)

### Proof

By Lemma 1 and (3.2)-(3.3),

`s_3(H)=s_3(H_0+E) >= s_(3+r)(H_0) >= s_0`.                    (3.7)

This uses only the rank of `E`, not its size.

By Section 2, the final bank pair `B=B_0+F` keeps the inertia of `B_0` and has smallest singular value at least `beta_0-delta`.

If `B_0` is indefinite, then (2.3) gives

`D=|det B| >= (beta_0-delta)^2`,
`kappa>=beta_0-delta`.

Apply the completed partner estimate (P) to the **actual final core** `H` and the actual arbitrary completion. We obtain

`||p_Q||_infinity`
` <=6*400^(1/3)[D^2 kappa s_3(H)]^(-1/6)`
` <=6*400^(1/3)[(beta_0-delta)^5 s_0]^(-1/6)`,

which is (3.5).

If `B_0` is definite, (2.4) and (P-def) give

`||p_Q||_infinity <=2*pi/sqrt(|det B|)`
` <=2*pi/(beta_0-delta)`,

which is (3.6). QED.

### What is different from small-leakage stability

The earlier fleet03/B12 spectral-leakage theorem assumes a bound on the **entire core perturbation norm** in order to preserve `s_3(H)`. Here the perturbation may be enormous on the rest of the reduced core. Its size is paid by the reserve count `r`; only the `2 x 2` bank compression must stay below the pair gap.

For a signed spectral sum

`E = sum_(j=1)^r tau_j v_j v_j^T`,                              (3.8)

with arbitrary real `tau_j`, one has `rank(E)<=r` and the pair price obeys

`delta <= sum_j |tau_j| ||(v_j)_[1,2]||_2^2`.                  (3.9)

Thus each `tau_j` may be arbitrarily large when its physical bank leverage is correspondingly small. Large overlap with the rest of the reduced core is free once the reserve (3.2) is available.

## 4. Exact commuting eigenvalue-replacement corollary

The preceding theorem gives a literal arbitrary-eigenvalue statement, not merely a generic low-rank perturbation statement.

Assume `H_0` has `s_(3+r)(H_0)>=s_0`, and let `u_1,...,u_r` be orthonormal eigenvectors of `H_0` whose first two bank coordinates vanish. Suppose

`H_0 u_j = lambda_j u_j`.

Choose **arbitrary real numbers** `mu_1,...,mu_r` (smaller, larger, zero, either sign, and with no magnitude restriction) and replace those eigenvalues by defining

`H = H_0 + sum_(j=1)^r (mu_j-lambda_j) u_j u_j^T`.              (4.1)

The perturbation has rank at most `r` and zero bank-pair compression, so `delta=0`. The vectors `u_j` remain eigenvectors and their eigenvalues are exactly `mu_j`. Therefore:

- if the protected pair is indefinite,

`boxed(||p_Q||_infinity
 <=6*400^(1/3)(beta_0^5 s_0)^(-1/6));`                          (4.2)

- if it is definite,

`boxed(||p_Q||_infinity <=2*pi/beta_0.)`                        (4.3)

The constants are completely independent of the replacement eigenvalues `mu_j`, their signs, and their magnitudes.

This is the requested source-valid stability theorem for adding/replacing arbitrary smaller or larger eigenvalues without treating any rotated quadratic remainder as an independent convolution.

## 5. Explicit target-class family with arbitrarily many arbitrary eigenvalue changes

Fix any `r>=1` and take the reduced core

`H_0 = diag(1,-1,1,1,...,1)`                                   (5.1)

of size `r+3`, with the first two coordinates as the two banks. Thus every singular value of `H_0` equals one, so

`s_(3+r)(H_0)=1`,

and the bank pair is

`B_0=diag(1,-1)`,
`beta_0=1`, `D=1`, `kappa=1`.

Now replace any `r` of the final `r+1` unit eigenvalues by completely arbitrary numbers `mu_1,...,mu_r`. Equivalently,

`H_mu = diag(1,-1,1,mu_1,...,mu_r)`.                            (5.2)

For every choice of the `mu_j`, the final matrix still has at least the three eigenvalues `1,-1,1` of magnitude one. The theorem gives

`boxed(||p_Q||_infinity <= 6*400^(1/3)
 =44.2083779836846...).`                                       (5.3)

The estimate remains valid with arbitrary outside quadratic spectrum and arbitrary cross coupling allowed by the partner factorization (3.1).

This family separates the present theorem from small-operator-tail results: if `|mu_j-1|` is huge, the full perturbation norm is huge, but the uniform density constant remains unchanged.

## 6. Why the reserve count is the correct low-rank currency

Without an a priori final `s_3` hypothesis, `r` arbitrary rank directions can erase `r` singular directions. For example,

`diag(1,-1,I_r) + diag(0,0,-I_r) = diag(1,-1,0,...,0)`.

Thus `s_(3+r)`-type reserve is the natural norm-free hypothesis for a rank-`r` perturbation if one wants to guarantee a third surviving singular source by rank alone. This observation is only about the reduction mechanism; it is not a QFORM counterexample, because the final matrix in this example falls outside the three-large-eigenvalue target.

## 7. Relation to the newer fleet03/B12 finite-tail theorem

The two theorems pay genuinely different regimes.

- `QFORM-FINITE-SMALL-SPECTRAL-TAIL-ARBITRARY-COMPLETION-v1` starts with exactly three dominant directions in a fixed finite physical packet and requires the remaining in-packet spectral tail to be small in operator norm.
- `QFORM-RANK-RESERVE-PAIR-COMPRESSION-STABILITY-v1` allows the added perturbation to have arbitrarily large eigenvalues of either sign, but spends one additional pre-existing singular direction per perturbation rank and requires only the protected bank-pair compression to stay below its gap.

Neither theorem implies the bare `s_3(A)>=1` conjecture. Together they clarify a useful dichotomy for additional eigenvalues: **small magnitude can be paid by operator norm; arbitrary magnitude can be paid by rank reserve plus a protected product-coordinate pair.**

## 8. Integrity and regularity

All statistical independence is kept in original coordinate blocks. No rotated spectral coordinates are declared independent. The arbitrary outside quadratic remainder is handled only through the completed mixed-norm shear theorem already built into the fleet03/B12 partner result.

No moments, Gaussianity, log-concavity, compact support, connected support, pointwise oscillatory decay, arbitrary-joint coarea, normalized worst conditional-fiber bound, or numerical evidence is used in the proof.

The result establishes an essentially bounded density in its stated scope. Continuity is not claimed.

Claim ID: `QFORM-RANK-RESERVE-PAIR-COMPRESSION-STABILITY-v1`.
