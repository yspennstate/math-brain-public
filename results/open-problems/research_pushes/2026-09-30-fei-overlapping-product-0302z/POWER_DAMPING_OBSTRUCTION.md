# Signed Fourier powers need not preserve boundedness

30 September 2026. Full classical FEI remains OPEN. This short consequence of the already certified seven-variable witness blocks one proposed interpolation shortcut; it is not a new FEI bound.

For a Boolean sign `f`, define the coefficientwise signed-power transform

\[
P_t f(x)=\sum_S\operatorname{sgn}(\widehat f(S))|\widehat f(S)|^t\chi_S(x),\qquad t\ge1.
\]

At `t=1`, this is the actual Boolean function, of supremum norm one. For `t>=2`, Parseval and `|fhat(S)|<=1` give

\[
\|P_t f\|_\infty\le\sum_S|\widehat f(S)|^t\le\sum_S\widehat f(S)^2=1.
\]

It would be incorrect to interpolate these endpoint facts by assuming the same bound on `1<t<2`.

## Explicit certificate

Use the actual seven-bit function defined in `witness.json` and REPORT.md Section 1. Its signed integer Walsh histogram is `−6:48, −2:60, 26:16, 30:4`, with normalization 128. At the origin,

\[
P_{3/2}f(0)
=\frac{52\sqrt{13}+15\sqrt{15}-36\sqrt3-15}{128}
>1.314.
\tag{1}
\]

For an elementary rational certificate, use

\[
\sqrt{13}>36055/10000,\qquad \sqrt{15}>38729/10000,
\quad \sqrt3<17321/10000.
\]

Each comparison follows by squaring nonnegative rationals. Substitution gives a lower bound `1.31424921875`, already strictly above 1.314. The checker additionally gives finer rational root enclosures and an outward decimal summary.

The violation starts immediately to the right of one. The function `t -> P_t f(0)` is analytic and has

\[
\left.\frac{d}{dt}P_t f(0)\right|_{t=1}
=-6\ln2-\frac{21}{16}\ln3+\frac{13}{4}\ln13+\frac{15}{16}\ln5
>4.
\tag{2}
\]

This is checked with rational logarithm bounds. Since `P_1f(0)=1`, there is some positive interval `(1,1+epsilon)` on which its value exceeds one. No maximal interval or critical exponent is claimed.

## Tensor amplification and operator interpretation

For disjoint tensor products, signed coefficient powers factor exactly. Thus for the Boolean tensor `F_k=f^tensor k`,

\[
P_{3/2}F_k(0)=\bigl(P_{3/2}f(0)\bigr)^k>1.314^k.
\]

There is therefore no dimension-independent replacement bound `||P_(3/2) f||_infty<=C` for this map on all Boolean functions. This concerns coefficientwise signed powers, not ordinary powers of a Boolean function.

Equivalently, the real Boolean convolution matrix `A_(S,T)=fhat(S xor T)` is a symmetric orthogonal involution, while replacing each entry by `sgn(A_(S,T))|A_(S,T)|^(3/2)` can have operator norm greater than 1.314. Its eigenvalues are the inverse Walsh values in (1), and tensoring gives the exponential failure. Positive-semidefinite Schur-power results cannot be applied to this indefinite matrix without an additional argument.

## Provenance and verification

`python verify_power.py` uses the exact witness, integer Walsh transforms, integer-square-root rational enclosures and the corrected dual binary/decimal outward serialization helper from `verify.py`. Its output includes exact rational lower and upper strings as authoritative evidence, plus checked decimal summaries and executed-file hashes. A two-factor actual Boolean truth table independently verifies the tensor coefficient identity.

Before writing this note, bounded repository and primary-source searches covered fractional Fourier powers, entrywise/Schur powers, spectral-power damping, and Boolean amplitude damping. No directly matching P03 source was found in that bounded retrieval. This is not a novelty certificate. The source seven-variable witness is the earlier product-entropy package, and its history/attribution correction remains intact.

The failed hypothesis is boundedness of this particular coefficient deformation on the intermediate real exponents. No ordinary noise-semigroup inequality, classical FEI, or arbitrary alternative interpolation method is refuted.
