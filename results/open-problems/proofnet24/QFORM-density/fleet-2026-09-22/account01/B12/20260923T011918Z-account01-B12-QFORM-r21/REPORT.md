SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-23T01:19:18Z.
attacking: sign-sensitive negative-part compression stability for arbitrary added eigenvalues, with an exact one-hostile-mode-free refinement.

# account01/B12 r21 — sign-sensitive additional-eigenvalue stability

Status: **PROVED_SUPPORTING_THEOREMS / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN**.

Target: for independent real inputs with densities bounded by one and symmetric A with at least three eigenvalues of modulus at least one, prove a universal density bound for X^TAX, or give a valid counterexample. This report does not claim the full target.

Fresh control observed before publication: math-research-brain main `bf4025022951fec4ada13e008f431c30cc292f11`, OWNER CONTROL revision `2026-09-22.15`, programme revision `2026-09-22.5`. Live corrections consumed include the failures of pointwise quadratic-phase decay, arbitrary-joint coarea, normalized conditional-fiber bounds, post-rotation independence, one-good-minor extraction, and raw operator-norm stability of a collective cross-tail certificate.

## 1. Sources actually applied

### 1.1 Completed partner result: account02/B12 localized physical core

From account02/B12 run `20260922T235544Z-account02-B12-qform`, canonical proof

`yspennstate/math-open-problems@3afc8473206ce82f5f6b19b9e88f8c9fa32ff058:proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260922T235544Z-account02-B12-qform/REPORT.md`,

if a physical original-coordinate triple S has `sigma_min(B)>=kappa` and the actual perturbation on that triple has operator norm at most Delta<kappa, then after conditioning all outside original coordinates the affine 3D theorem gives a **continuous** density with

`||p||_infinity <= 6 sqrt(pi)/(kappa-Delta)`.

The outside quadratic form and cross couplings are arbitrary. This is an original-coordinate conditioning theorem, not a convolution after spectral rotation.

### 1.2 Two-same-sign physical-three-block theorem

From

`yspennstate/math-open-problems@b3c543b40dfaef13468466fa82625303a7719af8:proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260922T141530Z-two-samesign-threeblock/REPORT.md`,

if a physical 3x3 block has at least two eigenvalues >=L, or at least two <=-L, with its third eigenvalue arbitrary, then the full ambient form has an essentially bounded density with

`||p||_infinity <= C_*/L`,

where

`C_*=24.183038289961516...`.

Continuity is not imported from this source.

## 2. Matrix notation: favorable and hostile spectral parts

Fix a sign `sigma in {+1,-1}`. For an arbitrary symmetric perturbation E define

`G_sigma(E)=(sigma E)_+`,
`H_sigma(E)=(sigma E)_-`.

Thus both are positive semidefinite and

`sigma E = G_sigma(E)-H_sigma(E)`.

If

`E=sum_r tau_r v_r v_r^T`

is an orthonormal spectral decomposition, then

`H_sigma(E)=sum_{sigma tau_r<0} |tau_r| v_r v_r^T`.

For a physical triple S, write

`H_S = P_S H_sigma(E) P_S^T`,

and let its eigenvalues be

`beta_1(S)>=beta_2(S)>=beta_3(S)>=0`.

Only the hostile spectral part appears below. Every favorable eigenvalue is free, regardless of its size, sign in the original convention, rank, or orientation.

## 3. Continuous stability: pay only the hostile compression

### Theorem 3.1 — QFORM-SIGNED-NEGATIVE-PART-COMPRESSION-v1

Assume a baseline symmetric matrix A0 has a physical triple S satisfying

`sigma A0[S,S] >= kappa I_3`

in Loewner order, with `kappa>0`. Let E be an arbitrary symmetric matrix of arbitrary rank and arbitrary spectrum. If

`beta_1(S)<kappa`,

then for every independent cap-one input vector X, and also after any affine tilt, the full ambient form associated with A=A0+E has a continuous density satisfying

`||p_(X^T A X)||_infinity <= 6 sqrt(pi)/(kappa-beta_1(S))`.      (3.1)

#### Proof

Multiply the form by sigma; this only reflects its output law and does not change the density supremum. Put

`B0 = sigma A0 + G_sigma(E)`.

Since `G_sigma(E)>=0`,

`B0[S,S] >= kappa I_3`.                                         (3.2)

The remaining perturbation is exactly `-H_sigma(E)`. On S its operator norm is

`||H_S||op=beta_1(S)`.                                          (3.3)

Apply the completed account02/B12 localized physical-core theorem to the baseline B0 with perturbation `-H_sigma(E)` and `Delta=beta_1(S)`. This gives (3.1), uniformly after conditioning all outside original coordinates. No random-variable independence is asserted for the spectral remainder; the only independence used is the original product structure when conditioning outside S. QED.

### Spectral reading

Equation (3.3) is exactly

`beta_1(S)=|| sum_{sigma tau_r<0} |tau_r| (v_r)_S (v_r)_S^T ||op`. (3.4)

Hence every favorable eigenvalue is omitted from the cost. Hostile eigenvalues are charged only through their **collective compressed spectral energy**, not through `||E||op`, not through their absolute sum, and not through a convolution estimate.

The crude but sometimes useful comparison is

`beta_1(S) <= sum_{sigma tau_r<0}|tau_r| ||(v_r)_S||_2^2`.       (3.5)

The exact operator quantity in (3.4) can be much smaller than this trace bound.

## 4. Exact one-hostile-mode-free peeling

The preceding continuous theorem pays the largest hostile compressed direction. For essential boundedness it can be removed completely.

### Lemma 4.1 — exact rank-one peel of a PSD compression

Let H be any positive semidefinite n x n matrix and S any three-coordinate set. Put

`B=P_S H P_S^T`

with eigenvalues `beta_1>=beta_2>=beta_3>=0`. Then there exists a positive semidefinite rank-one matrix R such that

`0<=R<=H`,

`P_S R P_S^T = beta_1 y y^T`

for a unit top eigenvector y of B, and therefore

`||P_S(H-R)P_S^T||op = beta_2`.                                 (4.1)

#### Proof

If beta_1=0 take R=0. Otherwise let

`V=H^(1/2) P_S^T`,

so `B=V^T V`. Let y be a unit top eigenvector of B and define

`z=Vy/sqrt(beta_1)`.

Then `||z||=1`. Set

`R=H^(1/2) z z^T H^(1/2)`.

Because `zz^T<=I`, one has `0<=R<=H`. Moreover

`P_S R P_S^T = V^T z z^T V = beta_1 y y^T`.

Thus the compressed residual equals `B-beta_1 y y^T` and has operator norm beta_2. QED.

### Theorem 4.2 — QFORM-ONE-HOSTILE-COMPRESSED-MODE-FREE-v1

Under the same baseline assumption

`sigma A0[S,S]>=kappa I_3`,

let E be arbitrary and let `beta_2(S)` be the second eigenvalue of the hostile compression `H_S`. If

`beta_2(S)<kappa`,

then the full ambient quadratic form has an essentially bounded density satisfying

`||p_(X^T(A0+E)X)||_infinity <= C_*/(kappa-beta_2(S))`.         (4.2)

The largest hostile compressed direction is completely unrestricted.

#### Proof

Write, as before,

`sigma E=G-H`,

with `G,H>=0`, and apply Lemma 4.1 to H and S. Thus

`H=R+H_tail`,

where `R>=0` has rank at most one and

`||P_S H_tail P_S^T||op=beta_2(S)`.                              (4.3)

Define

`C = sigma A0 + G - H_tail`.

On S,

`C[S,S] >= (kappa-beta_2(S)) I_3`.                              (4.4)

The final signed block is

`sigma(A0+E)[S,S]=C[S,S]-R[S,S]`.                               (4.5)

A negative semidefinite rank-one update of a 3x3 matrix obeys rank-one interlacing. If the eigenvalues are listed decreasingly, then

`lambda_2(C[S,S]-R[S,S]) >= lambda_3(C[S,S])`.                 (4.6)

By (4.4), the right side is at least `kappa-beta_2(S)`. Hence the final physical triple has at least two eigenvalues of sign sigma and magnitude at least `kappa-beta_2(S)`, while the third eigenvalue may be anything. The completed two-same-sign physical-three-block theorem therefore gives (4.2). QED.

### Why this is strictly stronger than a global second-hostile-eigenvalue bound

If the hostile eigenvalues of H are `h_1>=h_2>=...`, Cauchy interlacing for the physical compression gives

`beta_2(S)<=h_2`.                                                (4.7)

But beta_2 can be arbitrarily smaller than h_2 because hostile eigenvectors may have low or nearly rank-one footprint on S. Thus (4.2) is a genuinely local spectral-addition theorem, not merely the previous global `h_2` criterion rewritten.

## 5. Concrete arbitrary-large-eigenvalue family

Take a positive physical core

`A0[S,S]=I_3`, `kappa=1`,

and let E have the signed decomposition

`E=G-H`, `G>=0`, `H>=0`.

No restriction is imposed on G: it may have arbitrary rank and arbitrarily large eigenvalues. Suppose only that the hostile compression H_S has

`beta_2(H_S)<=1/2`.

Then Theorem 4.2 gives

`||p||_infinity <= 2 C_* = 48.36607657992303...`.              (5.1)

The top hostile compressed eigenvalue beta_1 can be arbitrarily large. For example, for arbitrary unit vectors u,w and arbitrary M>0,

`H=M u u^T + H_tail`,

with `||H_tail[S,S]||op<=1/2`, is covered uniformly in M, regardless of the orientation or S-leverage of u. Additional hostile eigenvalues outside S can have arbitrary magnitudes because they contribute zero to H_S. Thus the branch allows simultaneously:

1. arbitrarily many favorable added eigenvalues of arbitrary magnitude and orientation;
2. one completely arbitrary hostile effective direction;
3. arbitrarily many further hostile eigenvalues, charged only by the second compressed hostile eigenvalue.

Reflection (`sigma=-1`) gives the symmetric statement with all signs reversed.

For comparison, if the stronger condition `beta_1(S)<=1/2` holds, Theorem 3.1 yields a **continuous** density and

`||p||_infinity <= 12 sqrt(pi) = 21.26944621086619...`.         (5.2)

## 6. Weighted-family corollary

Suppose a probability distribution mu is supported on physical triples S satisfying

`sigma A0[S,S]>=kappa I_3`,

and let

`alpha=max_i P_mu(i in S)`.

For the hostile matrix H, write `H=R+H_tail` using any rank-one PSD peel `0<=R<=H`. Since

`E_mu tr(P_S H_tail P_S^T)=sum_i P_mu(i in S) (H_tail)_{ii}`
`<=alpha tr(H_tail)`,

there exists at least one S in the family with

`||P_S H_tail P_S^T||op <= alpha tr(H_tail)`.                  (6.1)

Applying Theorem 4.2 after optimizing the rank-one peel gives the valid selection inequality

`||p||_infinity <= C_*/(kappa-alpha tr(H_tail))`                (6.2)

whenever the denominator is positive. In particular, taking R to be the largest hostile spectral mode recovers the earlier tail-trace dilution but the local theorem (4.2) is stronger because it optimizes after compression.

## 7. Exact scope and remaining implication

These theorems are **stability/reduction results**, not a proof of the full conjecture. The bare global hypothesis `s_3(A)>=1` does not currently force a sign-definite physical triple with a useful kappa, nor one for which beta_2 of the hostile remainder is small. The known singleton-plus-two-bank and Hadamard stress families rule out replacing that missing structural step by one uniformly good local triple or one universal rank-three cross cut.

What is now proved on this branch is precise:

- favorable added spectral directions cost exactly zero;
- for continuity, the hostile spectrum costs only `beta_1` of its physical compression;
- for essential boundedness, one hostile compressed direction is exactly free and only `beta_2` is paid;
- all arguments stay in original coordinates and use conditioning only on original independent variables.

The next structural task is to combine this beta_2 certificate with the current no-pivot/grouped-bank alternatives: either extract a signed physical triple for which the hostile compression is effectively rank one, or route to the aggregate cross/bank certificates before any inverse local curvature is paid.

Full target status: **OPEN**. Continuity: proved only under Theorem 3.1's stronger `beta_1<kappa` condition; not claimed from Theorem 4.2.
