# account03/B16 — zero-pair product–square bank closure

**Run:** `20260922T164017Z-account03-B16-QFORM-r13`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Classification:** `TARGET_SUPPORTING_THEOREM / EXACT_RANK3_DIFFUSE_BANK_BRANCH_CLOSED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction discipline

The full owner target remains open: for independent real coordinates `X_i` with probability densities bounded by one and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal dimension-, law-, and matrix-independent bound on the essential supremum of the density of `Q=X^T A X`, or give a valid counterexample. Continuity is a separate desired conclusion.

This report does **not** rotate the independent physical coordinates, does not use the refuted law-uniform pointwise quadratic-phase decay, does not infer an indefinite quadratic trace bound from a projected-density cap alone, and does not average reciprocal local-minor estimates. The product aggregation occurs before the final curved trace.

The completed assigned partner result actually applied is account04/B16 run `20260922T161909Z-account04-B16-QFORM-r2`, source:

- full proof: `yspennstate/math-open-problems@58c23c624db350cf44f0c836daa3582eb7e2d266`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260922T161909Z-account04-B16-QFORM-r2/REPORT.md`.

It proves in the exact-rank-three nested-heavy geometry that if physical row `i` has leverage `c_0>1/2` and row `j` has residual leverage `h>1/2`, then

`G_ij = c_0 h > 1/4`,

where `G_ij=|r_i|^2|r_j|^2-<r_i,r_j>^2`. Combined with the fixed-pair Cauchy–Binet identity, the total determinant-bank mass is

`P_ij := |det Lambda| G_ij = sum_{k != i,j} |det A_{ {i,j,k} }|`.

Thus, when the three nonzero eigenvalues all have modulus at least one, `P_ij>1/4`. The partner left the diffuse normalized determinant-bank aggregation as the first unpaid implication.

The fixed-pair projection-product theorem used below is account01/B16 run `20260922T154258Z-account01-B16-QFORM-r12`, source `yspennstate/math-open-problems@47fe1ce92881fa4b6df0fa8a12b706d6a4eb14c5`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/20260922T154258Z-account01-B16-QFORM-r12/REPORT.md`. It proves that the normalized fixed-pair determinant weights are squares of coefficients of an original-coordinate normalized linear bank and, by the product-projection theorem, that such a bank has density at most `2`.

## 2. First implication attacked

The partner's remaining debt was to exploit the whole normalized physical-coordinate bank before paying reciprocal local determinant costs. This report closes that debt in the important **zero-diagonal physical-pair** branch, without requiring a heavy third atom or a zero diagonal on the third coordinate.

The mechanism has two independent ingredients:

1. a translation-uniform density envelope for the product of two independent cap-one variables;
2. a sharp-enough logarithmic trace estimate for a square of a capped one-dimensional projection bank.

The common conditional envelope is what permits the two ingredients to be composed despite dependence between the product shifts and the bank.

## 3. Translation-uniform product envelope

### Lemma 3.1 — `QFORM-TRANSLATED-PRODUCT-ENVELOPE-v1`

Let `U,V` be independent real random variables with probability densities bounded by one. Let `c != 0`, and let `k_c` be the density of `cUV`. Then for every `w != 0` and every `r>0`,

`k_c(w) <= 1/(|c| r) + (2/|c|) log(1 + |c| r/(2|w|)).`  (3.1)

The same bound, with the same constants, holds after arbitrary deterministic translations of `U` and `V`.

### Proof

Put `z=w/c`. The standard product-density formula gives

`k_c(w) = (1/|c|) integral f(u) g(z/u) du/|u|`.

Split at `|u|=r`. On `|u|>=r`, probability normalization gives

`(1/|c|) integral_{|u|>=r} f(u)g(z/u)du/|u| <= 1/(|c|r)`.

On `|u|<r`, use `f<=1` and substitute `v=z/u`; then `du/|u|=dv/|v|`, and the image is `|v|>|z|/r`. Hence this part is at most

`(1/|c|) integral_{|v|>|z|/r} g(v) dv/|v|`.

Among all probability densities `0<=g<=1`, the last integral is maximized by placing the unit mass on the points of largest weight `1/|v|` outside the forbidden interval. The bathtub optimizer consists of the two intervals adjacent to `+/- |z|/r`, each of length `1/2`. Therefore

`integral_{|v|>|z|/r} g(v) dv/|v|
 <= 2 log(1 + r/(2|z|))
 = 2 log(1 + |c|r/(2|w|))`,

which proves (3.1). Translation preserves independence, normalization and the density caps. QED.

This lemma is deliberately not a pointwise oscillatory estimate; fragmented supports cause no difficulty because the proof is a direct product-density rearrangement.

## 4. Logarithmic trace of a squared capped bank

### Lemma 4.1 — `QFORM-LOG-SQUARE-TRACE-v1`

Let `L` have a probability density bounded by `M`, let `sigma !=0`, and set

`D=|q-sigma L^2|`.

Then for every `B>0`, uniformly in `q in R`,

`E log(1+B/D) <= 2 sqrt(2) pi M sqrt(B/|sigma|).`  (4.1)

### Proof

For every `delta>0`, the one-dimensional set

`E_delta={ell: |q-sigma ell^2|<delta}`

has Lebesgue measure at most

`|E_delta| <= 2 sqrt(2 delta/|sigma|)`.  (4.2)

Indeed, after dividing by `sigma`, either the interval around the target does not meet `[0,infinity)`, or it begins at zero, in which case the total two-sided length is at most `2 sqrt(2 delta/|sigma|)`, or it is an annulus in `ell^2`, whose two-sided length is maximized at the endpoint where the lower radius vanishes and has the same bound.

Thus

`F_D(delta)=P(D<delta) <= K sqrt(delta)`,

with `K=2 sqrt(2) M / sqrt(|sigma|)`. Because `L` is absolutely continuous, `P(D=0)=0`. Integration by parts gives for `s>0`

`E[1/(D+s)]
 = integral_0^infinity F_D(t)/(t+s)^2 dt
 <= K integral_0^infinity sqrt(t)/(t+s)^2 dt
 = K pi/(2 sqrt(s))
 = sqrt(2) pi M /(sqrt(|sigma|) sqrt(s)).`  (4.3)

Finally use

`log(1+B/D)=integral_0^B ds/(D+s)`

and integrate (4.3) from `0` to `B`. This yields (4.1). QED.

The estimate is translation-uniform in the output level `q` and pays the square-root singularity exactly at the integrable exponent needed below.

## 5. Exact zero-pair rank-three theorem

### Theorem 5.1 — `QFORM-ZEROPAIR-CUBIC-BANK-CLOSURE-v1`

Let `A` be a real symmetric matrix of **exact rank three**, written

`A=R Lambda R^T`, `R^T R=I_3`,

with all three nonzero eigenvalues nonzero. Let the independent physical coordinates `X_1,...,X_n` have probability densities bounded by one. Suppose distinct physical indices `i,j` satisfy

`A_ii=A_jj=0`  and  `G_ij>0`.

Define

`P_ij := |det Lambda| G_ij
       = sum_{k != i,j}|det A_{ {i,j,k} }| >0`.

Then the law of `Q=X^TAX` has an essentially bounded density satisfying

`boxed( ||p_Q||_infinity <= 3 (2 pi)^(2/3) P_ij^(-1/3). )`  (5.1)

No diagonal condition is imposed on any third coordinate, no heavy determinant atom is required, and arbitrary diffuse determinant weights are allowed.

### Proof

Let `I={i,j}`, `K=I^c`, and block-decompose

`A = [[B,C],[C^T,D]]`.

Because `A_ii=A_jj=0`,

`B=[[0,a],[a,0]]`, where `a=A_ij`.

The assumptions force `a !=0`: if `a=0`, every principal triple through `i,j` has determinant zero, contradicting `P_ij>0`. Hence `B` is invertible.

Since `rank(A)=3` and `rank(B)=2`, the Schur complement

`S=D-C^T B^(-1) C`

has rank one. Write

`S=sigma d d^T`, `||d||_2=1`, `sigma !=0`,

and define the original-coordinate bank

`L=d^T X_K`.

Completing the square only in the **physical** coordinates `X_i,X_j` yields the exact identity

`Q = 2a U_Z V_Z + sigma L^2`,  (5.2)

where, conditional on `Z=X_K`, `U_Z` and `V_Z` are deterministic translations of `X_i` and `X_j`. Thus, conditional on `Z`, they remain independent and each has density cap one. They need not be independent of `L` unconditionally; the next step does not require this.

For every `k in K`, the principal `3x3` determinant through the pair satisfies the Schur identity

`det A_{ {i,j,k} }
 = det(B) S_kk
 = -a^2 sigma d_k^2`.  (5.3)

Taking absolute values and summing gives

`a^2 |sigma| = sum_k |det A_{ {i,j,k} }| = P_ij`.  (5.4)

Thus `d_k^2` are exactly the normalized determinant-bank weights. Equivalently, this is the same normalized physical-coordinate bank identified by the fixed-pair projection-product theorem. That theorem gives

`||p_L||_infinity <= M`, with `M=2`.  (5.5)

Now set `c=2a`. Conditional on `Z`, Lemma 3.1 applied to the product term in (5.2) gives, for every `r>0`,

`p_{Q|Z}(q)
 <= 1/(|c|r)
  + (2/|c|) log(1 + |c|r/[2 |q-sigma L^2|])`.

The right side depends on `Z` only through `L`. Average over `Z` and apply Lemma 4.1 with `B=|c|r/2`:

`p_Q(q)
 <= 1/(|c|r)
  + 4 pi M sqrt(r)/sqrt(|c sigma|).`  (5.6)

This is the critical common-envelope step: no conditional density of `L` is invoked, and no cancellation credit is reused.

Optimizing (5.6) over `r>0` gives

`p_Q(q)
 <= 3 * 2^(2/3) (pi M)^(2/3)
    (|c|^2 |sigma|)^(-1/3).`  (5.7)

Since `c=2a`, (5.4) turns (5.7) into

`p_Q(q) <= 3 (pi M)^(2/3) P_ij^(-1/3)`.

With `M=2`, this is exactly (5.1), uniformly in `q`. QED.

Numerically,

`3(2 pi)^(2/3) = 10.215065764430264...`.

## 6. Direct application of the assigned account04/B16 partner theorem

Assume now the account04/B16 nested-heavy exact-rank-three geometry: row `i` has leverage `c_0>1/2`, and row `j` has residual leverage `h>1/2`. Its proved identity is

`G_ij=c_0 h>1/4`.

If the three nonzero eigenvalues satisfy the target normalization `|lambda_1|,|lambda_2|,|lambda_3|>=1`, then `|det Lambda|>=1`, so

`P_ij=|det Lambda|G_ij>1/4`.  (6.1)

Therefore, whenever the selected nested-heavy pair also satisfies `A_ii=A_jj=0`, Theorem 5.1 gives the explicit universal estimate

`boxed( ||p_Q||_infinity
        < 3(2 pi)^(2/3) 4^(1/3)
        = 16.21540614038094... . )`  (6.2)

This **closes the partner's diffuse cubic-bank debt for the zero-diagonal-pair branch**. In contrast with the previous heavy-atom theorem, (6.2) needs neither `max w_k>=1/8` nor `A_kk=0` for any `k`; the entire normalized bank is paid once through `L`.

## 7. What was actually gained

The live correction set contains examples where every individual physical triple is tiny, so selecting one triple incurs a divergent reciprocal-minor cost. Equations (5.2)–(5.6) show a different mechanism: the determinant weights are first aggregated into one capped original-coordinate bank, and only then is the rank-one square traced against a translation-uniform product envelope. The resulting cost depends on the **total** fixed-pair invariant `P_ij`, at the homogeneous scale `P_ij^(-1/3)`, exactly as the cubic determinant ledger suggested.

This is stronger than the earlier zero-diagonal-atom branch in two ways:

1. no individual bank weight needs to be large;
2. no diagonal hypothesis is imposed on the third coordinates.

The result is still a scoped theorem, not the full QFORM conjecture.

## 8. Remaining full-target implication

The first assignment-relevant debt is now:

**`QFORM-INDEFINITE-PAIR-PRODUCT-SCHUR-v1`.** Extend the common-envelope Schur argument from the zero-diagonal physical pair

`[[0,a],[a,0]]`

to an arbitrary invertible indefinite physical `2x2` block, while preserving the original two-coordinate product geometry rather than diagonalizing that block. A determinant-homogeneous estimate would attack the owner's zero/near-isotropic physical-pivot branch directly.

A second, logically separate debt remains even after exact-rank-three closure: arbitrary additional spectral components cannot be convolved away as independent noise. A full theorem must make the product-preserving reduction stable under those correlated extra components.

The current correction `QFORM-HEAVY-ROW-FORCES-GOOD-SCHUR-PAIR-FALSE-v1` is compatible with this result: the theorem here assumes a suitable zero-diagonal pair and never claims that a heavy row forces such a pair or a uniformly good local Schur cross-volume.

## 9. Status and regularity

**Proved here:**

- the translation-uniform product envelope (3.1);
- the uniform logarithmic square-trace estimate (4.1);
- the exact-rank-three zero-diagonal-pair density theorem (5.1);
- the explicit nested-heavy target-normalized consequence (6.2), by direct application of the completed account04/B16 partner geometry.

**Not proved:** existence of a suitable zero-diagonal pair in every target matrix, the arbitrary indefinite-pair extension, stability under arbitrary additional spectral components, or the full universal conjecture.

The argument proves absolute continuity with an essentially bounded density in its stated scope. **Continuity is not separately proved.**

**Full QFORM conjecture: OPEN / NOT PROVED.**

## 10. Reproducibility and privacy note

The displayed constants were checked by direct scalar evaluation; all theorem steps above are analytic. The changed-file allowlist for this delivery consists only of this mathematical report. A manual fallback privacy review found only authorized mathematical/source metadata and no credentials, scheduler identifiers, machine paths, unrelated private transcripts, or public-release material. No installation or external paid computation was used.
