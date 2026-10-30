SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B12, 2026-09-22T19:34:21Z.
attacking: additional-eigenvalue control by composing lossless physical Schur peeling with the new isotropic-crossbank half-Riesz terminal theorem.

# fleet01/B12 — lossless heavy-pivot peeling into a half-Riesz terminal packet

Run: `20260922T193421Z-fleet01-B12-QFORM-r16`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Additional eigenvalue control  
Status: `PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh source state and exact target


The target remains: for every dimension, independent real coordinates with densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal finite essential density bound for `X^T A X`, or give a genuine counterexample. Continuity is an additional desired conclusion and is tracked separately.

The live corrections were re-read before this write. In particular this report does not use the false arbitrary-joint rank-three coarea lemma, the false positive conditional-projection moment gate, the false normalized scalar-`Qrest` worst-fiber gate, post-rotation independence, a fixed-good-minor dichotomy, or law-uniform pointwise quadratic-phase decay.

## 2. Exact completed inputs actually consumed

### 2.1 Named partner fleet02/B12: lossless Schur inheritance and no-blowup square recurrence

The designated partner result was consumed in full from

`yspennstate/math-open-problems@4b8eb43e9d001d41de6190b587fefe8fdea2006b`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260922T185427Z-fleet02-B12-QFORM-r11/REPORT.md`.

Its exact block theorem is: for an ORIGINAL-coordinate decomposition

`A=[[B,E],[E^T,C]]`, with invertible physical `r x r` block `B`, and Schur complement

`S=C-E^T B^(-1)E`,

one has

` s_j(S) >= s_(j+r)(A) `                                                    (2.1)

for every admissible `j`. The proof is the exact rank-`r` decomposition

`A=diag(0_r,S)+U B^(-1)U^T`, `U=[B;E^T]`,

followed by rank-`r` singular-value interlacing. Thus large eigenvalues counted by absolute value survive physical Schur elimination at the SAME spectral scale.

The same report applies the completed dependent-square smoothing theorem: if the Schur residual has density cap `B/ell` and the physical pivot has `|a|>=delta ell`, then the normalized density constant obeys

`T_delta(B)=2 sqrt(B/delta)`.                                                (2.2)

Writing `F_delta=4/delta`,

`T_delta^k(B)=F_delta^(1-2^(-k)) B^(2^(-k)) <= max(F_delta,B)`.              (2.3)

This is valid without declaring the completed square independent of its residual; original-coordinate independence supplies the conditional translate density cap.

### 2.2 Isotropic crossbank half-Riesz terminal theorem

I also consumed the complete current theorem from

`yspennstate/math-open-problems@1c4f1eba5940275a1e0454581a1a870707944137`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260922T190034Z-fleet03-B03-QFORM-r18/REPORT.md`.

Partition independent ORIGINAL coordinates into disjoint blocks `(U,V,W)`. If `T` has rank `r>=1`, positive singular values `sigma_1,...,sigma_r`,

`Delta_r=prod_m sigma_m`,

and

`R=2 U^T T V+b(W)^T U+c(V,W)`,                                             (2.4)

then

`sup_s E |R-s|^(-1/2) <= C_r Delta_r^(-1/(2r))`,                            (2.5)

where

`C_r=[4r/(2r-1)] sqrt(e) v_r^(1/(2r))`,
`v_r=pi^(r/2)/Gamma(r/2+1)`.                                                (2.6)

In particular `C_1=4 sqrt(2e)=9.326575926388497...`.

Consequently, for another independent original coordinate `Z`,

`Q=a(Z+h(U,V,W))^2+R`, `a!=0`,

has an essentially bounded density with

`||p_Q||_infinity <= C_r |a|^(-1/2) Delta_r^(-1/(2r))`.                    (2.7)

The theorem permits completely arbitrary measurable `c(V,W)` and arbitrary `b(W)`: the active `U` bank only has to be isotropic in the Schur residual (`U-U` block zero). Continuity is not claimed by that theorem.

## 3. New composition theorem: extra large eigenvalues cost neither scale nor depth

### Theorem 3.1 — `QFORM-HEAVY-PEEL-TO-ISOTROPIC-BANK-v1`

Fix `ell>0`. Suppose `A=A^(0)` has at least `k+3` eigenvalues of modulus at least `ell`. Assume there is a chain of `k` ORIGINAL-coordinate scalar Schur eliminations

`A^(0),A^(1),...,A^(k)`

with nonzero physical pivots `a_0,...,a_(k-1)` satisfying

`|a_j| >= delta ell` for every `j`,                                      (3.1)

where `delta>0` is independent of `j` and `k`.

Assume the terminal matrix `A^(k)` has another physical scalar pivot `a_*` satisfying

`|a_*| >= alpha ell`,                                                     (3.2)

and, after this pivot, its Schur residual can be partitioned into disjoint ORIGINAL-coordinate blocks `(U,V,W)` such that

`B_UU=0`,
`T:=B_UV` has rank `r>=1`,                                                (3.3)

and its positive singular values obey the geometric-mean lower bound

`Delta_r^(1/r) >= beta ell`, `beta>0`.                                   (3.4)

Then `X^T A X` has an essentially bounded density and

`boxed:
 ||p_(X^T A X)||_infinity
 <= ell^(-1) max{ C_r/sqrt(alpha beta), 4/delta }.
`                                                                              (3.5)

The bound is independent of `k`, the ambient dimension, all pivot signs, and every coefficient outside the protected terminal packet.

### Proof

By (2.1), after one scalar Schur elimination

`s_j(A^(1)) >= s_(j+1)(A^(0))`.

Inductively,

`s_j(A^(m)) >= s_(j+m)(A)`                                                (3.6)

for every admissible `j,m`. Hence the initial `k+3` singular values at least `ell` imply that `A^(k)` still has at least three such directions at exactly the original scale `ell`. No condition-number or shear factor accumulates.

At the terminal pivot, (2.7), (3.2), and (3.4) give

`||p_(A^(k))||_infinity
 <= C_r (alpha ell)^(-1/2) (beta^r ell^r)^(-1/(2r))`
` = [C_r/sqrt(alpha beta)] ell^(-1).`                                    (3.7)

Put `B_k=ell ||p_(A^(k))||_infinity`. Lifting one earlier physical square by the partner's dependence-safe recurrence gives

`B_(j-1) <= T_delta(B_j)=2 sqrt(B_j/delta)`.                              (3.8)

Iterating and using (2.3),

`B_0 <= max{B_k,4/delta}`.                                                (3.9)

Insert (3.7) into (3.9). This is (3.5). QED.

### Concrete rank-one packet

Take `r=1`, `delta=1/4`, `alpha=beta=1/2`. Then

`C_1/sqrt(alpha beta)=2C_1=8 sqrt(2e)=18.653151852776993...`,
`4/delta=16`.

Thus an arbitrarily long heavy-pivot chain terminating in a rank-one isotropic cross bank at the stated half-scale satisfies

`||p_Q||_infinity <= [8 sqrt(2e)]/ell < 18.654/ell`.                       (3.10)

This illustrates the substantive point: extra large eigenvalues do not multiply density constants and do not shrink the spectral scale while they are peeled through physical heavy pivots.

## 4. Arbitrary additional spectral cloud that is literally free at the terminal packet

The half-Riesz theorem has a stronger stability feature that is useful for the B12 assignment.

### Corollary 4.1 — `QFORM-ISOTROPIC-BANK-FREE-CLOUD-v1`

At the terminal Schur residual in Theorem 3.1, let `H` be any symmetric perturbation, of arbitrary rank, sign and operator norm, satisfying only

`H_UU=0`, `H_UV=0`.                                                       (4.1)

Then the same density bound (3.5) holds with exactly the same constants.

Indeed, after adding `H`, the protected cross block remains `T`. The `U-W` part of `H` merely changes the arbitrary coefficient `b(W)` in (2.4), while the `V-V`, `V-W`, and `W-W` parts merely change the arbitrary measurable term `c(V,W)`. The terminal half-Riesz estimate therefore does not see their size, rank, sign, or spectral decomposition.

At the pre-Schur matrix level, it is enough that an added perturbation has zero row and column at the terminal pivot and induces a residual perturbation satisfying (4.1). This is a direct matrix stability theorem; no added term is treated as an independent convolution.

### Literal additional-eigenvalue example

For independent cap-one scalar coordinates `Z,U,V` and an independent vector `W`, consider

`Q=a(Z+h(U,V,W))^2 + 2 sigma U V + 2 U g^T W + c(V,W)`.                    (4.2)

Here `c(V,W)` may be any quadratic form in `(V,W)`, with arbitrarily many eigenvalues, of either sign and arbitrary magnitude. The theorem gives

`boxed:
 ||p_Q||_infinity <= 4 sqrt(2e) |a sigma|^(-1/2).
`                                                                              (4.3)

When `h=g=0` and `c(V,W)` contains a direct diagonal block `sum_j tau_j W_j^2`, the base three-coordinate core `Z^2+2UV` has eigenvalues `{1,1,-1}` and the `tau_j` are literally arbitrary additional eigenvalues. Formula (4.3) is unchanged for every choice of the `tau_j`. Allowing the displayed `U-W` coupling and arbitrary `V-W`/`W-W` terms makes the ambient matrix genuinely nonseparable while retaining the same certificate.

This is a substantial additional-eigenvalue control statement: a whole arbitrary-rank spectral cloud is harmless once it lies in the free blocks of a source-valid original-coordinate half-Riesz packet.

## 5. Exact use of the named partner result

The partner theorem is not merely cited. It enters twice at actual inequalities:

1. Equation (3.6) is the fleet02/B12 lossless singular-value inheritance, preserving all `ell`-scale directions through each physical elimination.
2. Equation (3.8) is the partner's dependence-safe normalized density recurrence. Its fixed point gives the `4/delta` term in (3.5), proving that arbitrarily many additional large eigenvalues cause no depth-dependent blow-up on this branch.

Thus this run converts the partner reduction into a terminal theorem with an explicit, nontrivial cross-dominated payment rather than leaving `B_terminal` abstract.

## 6. What this does and does not settle

This is not a proof of the full conjecture. The bare hypothesis `s_3(A)>=1` does not yet force a heavy-pivot chain ending in a uniformly strong isotropic original-coordinate cross bank. Existing source-backed counterexamples already rule out replacing this missing implication by a fixed-good-minor or universal rank-three-cross-cut dichotomy.

The new unpaid structural implication is therefore narrower:

> after the already-proved ridge/principal/pair branches fail, convert the remaining high-leverage/cross-dominated geometry into either (i) a terminal packet satisfying (3.2)--(3.4), or (ii) a translation-uniform half-Riesz payment that tolerates a nonzero self block on the active `U` bank.

The second option is especially natural because the only rigid hypothesis in the terminal theorem is `B_UU=0`; all coefficients on the opposite side of the bank are already free. A useful next step is to handle a low-rank or quantitatively small nonzero `B_UU` without normalizing rare fibers or rotating the product law.

The theorem establishes essential boundedness in its stated branch. It does **not** prove continuity, so the owner's continuity goal remains separately open here.

## 7. Integrity and scope review

No Gaussianity, moments, log-concavity, compact support, connected support, post-rotation independence, unrestricted coarea, normalized worst-fiber cap, or pointwise law-uniform oscillatory decay is used. The only conditioning is on blocks of ORIGINAL independent coordinates, exactly within the scopes of the two consumed theorems.

A manual changed-file review found only mathematical/source metadata in this report; no credentials, signed URLs, machine paths, unrelated private data, scheduler identifiers, public release, paid/remote computation, email or permission changes are involved. No repository-wide scanner was available through the connector, so this is recorded as a narrow manual scope review rather than a full automated privacy scan.
