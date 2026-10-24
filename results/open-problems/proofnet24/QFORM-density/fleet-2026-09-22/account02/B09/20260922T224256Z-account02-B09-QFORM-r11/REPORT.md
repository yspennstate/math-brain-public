SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-22T22:42:56Z.
attacking: indefinite Schur-lightcone external smoother via a disjoint-bank bilinear split that preserves the third spectral direction instead of conditioning it away.

# account02/B09 QFORM r11 — diffuse external square bank pays a rank-two lightcone core

Programme: `QFORM-DENSITY-3EIG-20260922`, programme revision `2026-09-22.5`.
Owner control at start: `yspennstate/math-research-brain@8f4fc3081c4197ab549d4aa2b3bde859a10de324`, revision `2026-09-22.15`.
Prewrite control refresh: `yspennstate/math-research-brain@fc7d770c6dede6b96ed629920b388b47be831cb4`, same revision.
Worker: `account02/B09` (`Bilinear block mechanism`).
Status: **ESSENTIAL_STEP_APPLIED / LOCAL STRENGTHENING REFUTED / FULL QFORM OPEN**.
Execution label: **WITHOUT_VERIFIED_BRAIN**.

The full conjecture remains open. This run closes one precise form of the first debt left by r10: a rank-two indefinite/lightcone core becomes uniformly bounded when the third curvature direction is retained as a genuinely independent scalar projection of a disjoint original-coordinate bank, even when that scalar projection is completely diffuse across the bank. The proof is a direct `O(interval length)` argument and does not use square-root decoupling.

## 1. Source-pinned premises actually used

### 1.1 Orientation-free rank-two half-Riesz estimate

Complete source:

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

Its theorem `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` says: if `V^T V=I_2`, `Lambda` is invertible symmetric `2x2`, and `b` is arbitrary in the original independent coordinate space, then

`sup_t E |(V^T X)^T Lambda(V^T X)+b^T X-t|^(-1/2) <=128 |det Lambda|^(-1/4)`.      (1.1)

If the affine term lies in `range(V)`, including zero affine term, the constant improves to `16 sqrt(30)`.

### 1.2 Scalar projection density cap

The same source records the Rogozin--Ball/Livshyts--Paouris--Pivovarov scalar projection bound used throughout this programme: for a nonzero vector `z` on a product bank of cap-one independent coordinates,

`||p_<z,X>||_infinity <= sqrt(2)/||z||_2`.                            (1.2)

### 1.3 Completed designated-partner theorem

The newest completed designated-partner result available at the fresh control snapshot is account03/B09 r18:

`QFORM-TWO-BANK-DEFINITE-TRANSVERSE-RANK2-v1`, complete source

`yspennstate/math-open-problems@9404859d9039d9eb76286588dc6d38a0fc3393ed:proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260922T214906Z-account03-B09-QFORM-r18/REPORT.md`.

It proves

`||p_F||_infinity <= 2^(5/4) sqrt(pi) e^(3/4) Gamma^(-1/4) < 8.925 Gamma^(-1/4)`   (1.3)

for one scalar cross direction plus a definite transverse two-curvature bank, preserving an `O(|L|)` interval bound.

Corrections enforced in this run include: no independence after spectral rotation; no arbitrary-joint rank-three coarea; no positive conditional projection-density moment; no pointwise law-uniform Fresnel decay; no local-minor-only extraction; no replacement of product provenance by a mere projected joint-density cap; and the r10 lightcone obstruction showing that a rank-two indefinite core can genuinely have logarithmically unbounded density.

## 2. New theorem: `QFORM-DIFFUSE-EXTERNAL-SQUARE-SCHUR-v1`

Let `I,J` be disjoint sets of original independent coordinates. Let `V` be an `|I| x 2` matrix with orthonormal columns and put

`Y=V^T X_I`.

Let `z in R^J` be nonzero and

`Z=<z,X_J>`.

Assume the active dependence on the `J`-bank factors through this single scalar `Z`. After any conditioning on further disjoint original coordinates, suppose the active conditional quadratic-plus-linear form has the shape

`F=Y^T H Y + 2 Z r^T Y + d Z^2 + b^T X_I + alpha Z + c`,             (2.1)

where `H` is symmetric `2x2`, `r in R^2`, `d !=0`, and `b` is arbitrary in the original `I`-coordinates. Define the scalar-Schur residual

`Lambda = H - r r^T / d`.                                            (2.2)

Assume `Lambda` is invertible. Then `F` has an essentially bounded density and

`boxed: ||p_F||_infinity <= 128 sqrt(2) [d^2 ||z||_2^4 |det Lambda|]^(-1/4).`      (2.3)

Equivalently every interval `L` satisfies

`P{F in L} <= 128 sqrt(2) [d^2 ||z||_2^4 |det Lambda|]^(-1/4) |L|`.  (2.4)

If the residual affine term after completing the scalar square lies in `range(V)` (in particular when `b=0` and `alpha=0`), the constant `128 sqrt(2)` improves to

`16 sqrt(60)=123.9354670786...`.                                     (2.5)

The scale certificate

`Gamma_ext = d^2 ||z||_2^4 |det Lambda|`                             (2.6)

is invariant under rescaling the scalar bank coordinate `z -> c z`, accompanied by the corresponding coefficient rescaling in (2.1).

### Proof

Complete the scalar square:

`d Z^2 +2Z r^T Y + alpha Z
 = d [ Z + (r^T Y+alpha/2)/d ]^2
   -(r^T Y+alpha/2)^2/d`.                                            (2.7)

Hence

`F = d[Z+m(X_I)]^2 + R(X_I)`,                                        (2.8)

where

`m(X_I)=(r^T Y+alpha/2)/d`,

and

`R(X_I)=Y^T Lambda Y + b_tilde^T X_I + c_tilde`                      (2.9)

for an arbitrary original-coordinate affine coefficient `b_tilde`.

Because the banks `I,J` are disjoint, conditioning on `X_I=x` leaves the law of `Z` unchanged except for the deterministic translation by `m(x)`. By (1.2), its density cap is

`M <= sqrt(2)/||z||_2`.                                               (2.10)

For any scalar random variable `W` of density cap `M`, any shift `s`, and `d !=0`, the variable `d(W+s)^2` has conditional density bounded by

`M / sqrt(|d| |u|)`                                                   (2.11)

on the half-line of the appropriate sign. This is the elementary two-preimage Jacobian bound; the factor two from the two roots cancels the derivative factor two.

Therefore, for almost every `t`, conditioning on `X_I` gives

`p_F(t | X_I)
 <= M |d|^(-1/2) |t-R(X_I)|^(-1/2)`.                                (2.12)

Average and apply the source-pinned half-Riesz theorem (1.1):

`p_F(t)
 <= M |d|^(-1/2) E|t-R|^(-1/2)
 <=128 M |d|^(-1/2) |det Lambda|^(-1/4)`                             (2.13)

and then (2.10) gives (2.3). The improved constant follows from the improved affine-in-range half-Riesz constant.

This proof remains linear in interval length because it proves an actual `L^infinity` density bound. It uses no resampling and no square-root small-ball conversion. `QED`

## 3. Why this is a genuine aggregate-before-inversion gain

For every `m`, take three disjoint original-coordinate banks `I_1,I_2,J`, each of size `m`. Let `u,v,z` be unit flat vectors on their respective banks and set

`U=<u,X_{I_1}>`, `V0=<v,X_{I_2}>`, `Z=<z,X_J>`.

Put

`F_m = 2 U V0 + Z^2`.                                                 (3.1)

On the orthonormal compressed basis `(u,v,z)`, the coefficient matrix is

`[[0,1,0],[1,0,0],[0,0,1]]`,                                        (3.2)

with spectrum exactly

`{-1,1,1}`.                                                           (3.3)

Thus every `F_m` is a genuine target matrix with exactly three eigenvalues of magnitude one. Every nonzero physical coefficient is `O(1/m)`; in particular every physical diagonal pivot supplied by the `Z^2` bank equals `1/m`.

Apply Theorem 2 with core frame `(u,v)`,

`H=[[0,1],[1,0]]`, `r=0`, `d=1`, `||z||=1`, `|det Lambda|=1`.

Because there is no residual affine term, the sharp scoped constant from (2.5) yields

`boxed: ||p_(F_m)||_infinity <=16 sqrt(60) <123.936`                 (3.4)

uniformly in `m` and in every admissible collection of independent cap-one input laws.

By contrast, the source rank-three physical-pivot consequence applied to any physical coordinate in the `J` bank only yields a bound of order `128 sqrt(m)`. The new theorem pays the whole diffuse third direction before any reciprocal physical-pivot cost.

This does not prove a universal routing from `s_3(A)>=1` to the structural factorization (2.1). It proves that once the third direction is exposed as a rank-one scalar bank, diffuseness of that direction is not itself an obstruction.

## 4. Designated partner result applied to an actual inequality

Use the completed account03/B09 theorem (1.3) on two disjoint original-coordinate banks. Let `u` be a unit scalar projection on the first bank and let `v,w1,w2` be orthonormal projections on the second. Define

`G = 2 U V + 2 W1^2 + W2^2`.                                        (4.1)

The compressed spectrum is

`{-1,1,2,1}`,                                                        (4.2)

so this is target-valid. In the partner notation,

`a=1`, `||u||=1`, `Omega=||v wedge w1 wedge w2||=1`, `D=diag(2,1)`,

hence `Gamma=2`. Therefore the partner theorem gives the concrete direct estimate

`boxed: ||p_G||_infinity <= 2 sqrt(pi) e^(3/4) = 7.5045696636...`.   (4.3)

This is a real application of the named partner theorem, not a citation-only dependency.

## 5. Local strengthening refuted: overlapping curvature is not an external smoother

The disjoint-bank hypothesis in Theorem 2 cannot simply be deleted. Let `U,W1,W2` be iid `Uniform[-1/2,1/2]`. The r10 lightcone core was

`Q0=2U(W1+W2)+W1^2-W2^2`.

Add the apparently positive rank-one curvature `(W1+W2)^2` on the *same* variables. Then

`Q0+(W1+W2)^2
 =2(W1+W2)(U+W1)`.                                                   (5.1)

Thus the added square does not supply an independent third smoother; the form remains rank at most two and factors into two linear forms.

Write

`S=W1+W2`, `T=U+W1`.

The joint density of `(S,T)` is at least `1/2` on `[-1/4,1/4]^2`: for fixed `(s,t)` in this square, the fiber parameter `w1` may range over

`[-1/2,1/2] intersect [t-1/2,t+1/2] intersect [s-1/2,s+1/2]`,

whose length is at least `1/2`. Therefore for `0<|q|<1/8`, the density of `2ST` satisfies

`p(q)
 >= (1/2) log(1/(8|q|))`,                                            (5.2)

by integrating the product Jacobian `1/(2|s|)` over both signs and `2|q|<=|s|<=1/4`.

Hence the density is logarithmically unbounded. This is **not** a counterexample to the full conjecture because the coefficient matrix still has rank at most two. It refutes only the tempting strengthening “any nonzero added square curvature smooths an indefinite rank-two core.” What matters is a genuinely external product-compatible third direction (or another already-paid higher-rank mechanism), not the formal presence of a square term in overlapping variables.

## 6. First unpaid implication after this run

`QFORM-EXTERNAL-SCALARBANK-OR-OVERLAPPING-CURVATURE-ROUTING-v1`:

Starting only from `s_3(A)>=1`, after the paid ridge/zero-internal/definite-transverse/pair-log branches, force either

1. a disjoint scalar bank whose Schur residual is an invertible rank-two quadratic at universal aggregate scale, so Theorem 2 applies;
2. an already-paid definite-transverse or multi-cross branch; or
3. a genuinely overlapping higher-rank curvature configuration and prove a product-provenance-sensitive estimate there.

The counterexample in Section 5 is a regression test: a routing lemma may not count a square as an “external third direction” when it lies inside the same rank-two lightcone span and merely refactorizes the product singularity.

The full QFORM conjecture remains **OPEN**; continuity is not proved here.

## 7. Integrity / provenance

No benchmark material, credentials, unrelated private data, paid model/API call, public release, permission change, remote workflow, scheduler mutation, email, or notification change was used. Mathematical dependencies are source-pinned above. No numerical computation is needed for the proof; the displayed decimals are evaluations of explicit constants only. The result is an auxiliary theorem plus a source-valid falsifier of a stronger intermediate mechanism, not a full proof candidate.