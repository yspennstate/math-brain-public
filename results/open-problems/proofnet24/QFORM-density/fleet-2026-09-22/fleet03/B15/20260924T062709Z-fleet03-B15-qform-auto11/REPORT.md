SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B15, 2026-09-24T06:27:09Z.
attacking: repair the localized physical-triple regime with a product-preserving proof and an explicit universal constant, then apply same-constant C0 closure.

# fleet03/B15 — product-preserving localized triple theorem

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T062709Z-fleet03-B15-qform-auto11`  
Status: `LOCALIZED_PHYSICAL_TRIPLE_UNIVERSAL_BOUND_PROVED / PARTNER_APPLIED / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Main theorem

Let `X_1,...,X_n` be independent real random variables with probability densities bounded by one, and let `A` be real symmetric. Suppose that for some set `I` of **three original coordinates**, the physical principal block

\[
B=A_{I,I}\in\mathbb R^{3\times3}
\]

has all three eigenvalues of absolute value at least `s>0`.

Then the full ambient quadratic form, with arbitrary coefficients outside `I` and arbitrary cross-couplings between `I` and `I^c`, has an essentially bounded density and

\[
\boxed{
\|p_{X^TAX}\|_\infty
\le {128\,2^{1/4}\over s}
< {153\over s}.
}
\tag{1.1}
\]

Moreover, because the physical block has rank three, the full matrix has rank at least three. Applying the completed fleet04/B15 same-constant regularity compiler gives the canonical representative

\[
\boxed{
p_{X^TAX}\in C_0(\mathbb R),\qquad
\|p_{X^TAX}\|_\infty
\le {128\,2^{1/4}\over s}.}
\tag{1.2}
\]

In particular, if `s>=1`, this proves the complete localized target branch with a universal constant `<153` and the desired continuity conclusion.

This is a replacement for the old localized-three-coordinate argument that went through the refuted arbitrary-joint coarea height lemma. The proof below never replaces the three original independent coordinates by an arbitrary joint density and never rotates them into independent spectral coordinates.

## 2. Source-pinned inputs

Two completed supporting analytic arguments are used.

### 2.1 Scalar-pivot / rank-two half-Riesz theorem

Source:

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`

For an original-coordinate principal block of exact rank three,

\[
B=VMV^T,\qquad V^TV=I_3,
\]

if one physical diagonal entry `a=B_ii` is nonzero, the full ambient quadratic form satisfies

\[
\|p_Q\|_\infty
\le 128\,[c_i|a||\det M|]^{-1/4},
\tag{2.1}
\]

where `c_i` is the squared norm of row `i` of `V`. For a physical `3x3` block, `V` is square orthogonal, hence `c_i=1`, and `|det M|=|det B|`. Arbitrary outside coefficients, cross-couplings, and the induced affine terms are allowed by the source theorem.

### 2.2 Indefinite physical-pair logarithmic theorem

Source:

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`

If the same exact-rank-three physical block has nonzero eigenvalue magnitudes at least `s`, and an original-coordinate `2x2` principal pair `D` is invertible indefinite, writing

\[
\Delta=|\det D|,\qquad \kappa=\sigma_{\min}(D),
\]

the full ambient quadratic form satisfies

\[
\|p_Q\|_\infty
\le 8\sqrt5\,(\Delta\kappa s)^{-1/4}.
\tag{2.2}
\]

Again all outside coefficients/couplings and induced affine terms are retained. The proof keeps the logarithmic pair singularity and averages it against a product-preserving rank-one Schur remainder; it does not assert a false bounded density for an indefinite quadratic pair.

## 3. Algebraic dichotomy inside a well-conditioned physical triple

Let the eigenvalues of `B` be `mu_1,mu_2,mu_3`, so

\[
|\mu_j|\ge s\quad(j=1,2,3).
\tag{3.1}
\]

Consequently

\[
|\det B|\ge s^3,
\qquad
\operatorname{tr}(B^2)=\sum_{j=1}^3\mu_j^2\ge3s^2.
\tag{3.2}
\]

We split according to the physical diagonal size.

### Case A: one diagonal is at least `s/2`

Suppose `|B_ii|>=s/2`. Apply (2.1) with `a=B_ii`. Since the spectral frame of the `3x3` physical block is square orthogonal, `c_i=1`; using (3.2),

\[
\|p_Q\|_\infty
\le128\,(|B_{ii}|\,|\det B|)^{-1/4}
\le128\,[(s/2)s^3]^{-1/4}.
\]

Hence

\[
\boxed{
\|p_Q\|_\infty\le {128\,2^{1/4}\over s}.
}
\tag{3.3}
\]

This branch uses only an original-coordinate scalar pivot; the remaining two-dimensional Schur quadratic is paid by the orientation-free affine half-Riesz theorem from the cited source.

### Case B: every physical diagonal is smaller than `s/2`

Assume instead

\[
|B_{11}|,|B_{22}|,|B_{33}|<s/2.
\tag{3.4}
\]

Write the off-diagonal entries as `b_12,b_13,b_23`. From (3.2),

\[
3s^2
\le \sum_i B_{ii}^2+2\sum_{i<j}b_{ij}^2
< {3s^2\over4}+2\sum_{i<j}b_{ij}^2.
\]

Therefore

\[
\sum_{i<j}b_{ij}^2>{9s^2\over8},
\]

so for at least one pair, after relabelling `(1,2)`,

\[
|b_{12}|>s\sqrt{3/8}.
\tag{3.5}
\]

Consider its physical pair

\[
D=\begin{pmatrix}B_{11}&b_{12}\\b_{12}&B_{22}\end{pmatrix}.
\]

Because `|B_11 B_22|<s^2/4` while `b_12^2>3s^2/8`,

\[
\det D=B_{11}B_{22}-b_{12}^2<-{s^2\over8}.
\]

Thus `D` is invertible indefinite and

\[
\Delta=|\det D|>{s^2\over8}.
\tag{3.6}
\]

For its smallest singular value, write

\[
D=\begin{pmatrix}0&b_{12}\\b_{12}&0\end{pmatrix}
 +\operatorname{diag}(B_{11},B_{22}).
\]

The first summand has both singular values `|b_12|`. Weyl's singular-value perturbation inequality and (3.4)-(3.5) give

\[
\kappa=\sigma_{\min}(D)
\ge |b_{12}|-\max(|B_{11}|,|B_{22}|)
>s\left(\sqrt{3/8}-{1\over2}\right)
={s(\sqrt6-2)\over4}.
\tag{3.7}
\]

Insert (3.6)-(3.7) into the product-preserving pair-log theorem (2.2):

\[
\begin{aligned}
\|p_Q\|_\infty
&\le8\sqrt5\,(\Delta\kappa s)^{-1/4}\\
&< {8\sqrt5\over s}
\left({32\over\sqrt6-2}\right)^{1/4}\\
&= {51.9616026228\ldots\over s}.
\end{aligned}
\tag{3.8}
\]

In particular this is strictly below the Case-A constant `128*2^(1/4)/s`.

Combining (3.3) and (3.8) proves (1.1).

## 4. Why outside coordinates do not break the proof

Conditioning on every original coordinate outside `I` preserves independence and the density caps of the three coordinates in `I`. The outside block and all cross-couplings contribute only a conditioning-dependent constant and affine terms in those three variables.

Both source theorems (2.1) and (2.2) were proved with precisely those arbitrary affine terms and arbitrary outside couplings retained. Hence their constants are uniform in the outside conditioning. Averaging the conditional laws therefore keeps the same interval-density bound.

No diagonalization of the product law is performed.

## 5. Designated partner fleet04/B15 applied at an actual inequality

The completed fleet04/B15 theorem at

`yspennstate/math-open-problems@7b2b0f54db9acbd23a5f69f715178ab666e22d8e`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260923T221909Z-fleet04-B15-ruled-trace-c0-r8/REPORT.md`

states: for a fixed rank-at-least-three target/product instance, once a separate argument proves

\[
\Pr\{Q\in J\}\le M|J|
\tag{5.1}
\]

for every interval `J`, the same law has a canonical representative

\[
p_Q\in C_0(\mathbb R),\qquad \|p_Q\|_\infty\le M
\tag{5.2}
\]

with no height loss.

Apply this theorem to the actual interval inequality supplied by Sections 3-4 with

\[
M={128\,2^{1/4}\over s}.
\]

Because `B` has rank three, the full matrix has rank at least three. Therefore (5.2) gives exactly (1.2). This separates continuity from the hard height estimate: continuity is not inferred from essential boundedness alone.

## 6. Consequence for the owner target

If a target matrix contains a physical `3x3` principal block whose three eigenvalues all have absolute value at least one, then

\[
\boxed{
p_Q\in C_0(\mathbb R),\qquad \|p_Q\|_\infty<153.}
\tag{6.1}
\]

By Cauchy interlacing/inertia monotonicity, such a principal block itself guarantees that the ambient matrix has at least three eigenvalues of absolute value at least one (counting the positive and negative sides separately).

This is a genuine product-preserving proof of the **localized physical-triple regime**.

## 7. Relation to live corrections

The proof uses none of the refuted interfaces:

- no law-uniform pointwise van-der-Corput decay;
- no post-rotation independence;
- no arbitrary-joint rank-three coarea `L^infinity` theorem;
- no conditional projection-density positive moment;
- no dimension-free fiber supremum;
- no fixed support diameter or fragment count.

The earlier arbitrary-joint coarea claim cannot prove the localized branch because it is false even for smooth compactly supported joint densities. Here the gain comes specifically from the original-coordinate product law through the rank-two affine half-Riesz and physical-pair logarithmic theorems.

## 8. What remains open

The unrestricted owner theorem is **not** proved. The bare spectral hypothesis `s_3(A)>=1` does not force any physical `3x3` principal block to have its smallest eigenvalue bounded below. The live correction family

\[
[1]\oplus J_m/m\oplus(-J_m/m)
\]

has nonzero spectrum `{1,1,-1}` while every nonsingular physical `3x3` principal block can have smallest singular value of order `1/m`.

Therefore the remaining full-target step is still an aggregate-before-inversion theorem: diffuse large spectral directions must be paid by grouped original-coordinate mechanisms rather than by selecting a single well-conditioned physical triple.

This run closes only the localized physical-triple branch, but it closes it under the exact rough-law quantifiers and with the stronger `C_0` conclusion.

## 9. Status and source integrity

- Main new synthesis: proved in Sections 3-4 from source-pinned supporting theorems.
- Essential boundedness: proved in the stated localized scope.
- Continuous density: obtained separately by the designated partner same-constant compiler.
- Full universal QFORM theorem: OPEN.
- Counterexample to QFORM: none produced.
- Native mathematical receiver ingestion: not verified; repository retrieval/write is not treated as native brain ingestion.
