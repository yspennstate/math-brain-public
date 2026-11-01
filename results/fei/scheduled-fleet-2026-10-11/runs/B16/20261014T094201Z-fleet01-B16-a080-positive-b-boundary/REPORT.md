# B16 / A080 — positive `U` tax absorbs the OR-family GU boundary layer

**Status:** PROVED all-parameter family theorem, pending independent review. **Universal GU and full FEI remain OPEN.**

## Frozen candidate

- Primary packet: **A080**.
- Attempt: `A080-POSITIVE-B-BOUNDARY-1`.
- Stable gap: `GU-UNIVERSAL-PAIR-BOUNDARY`.
- Claim version: `B16-A080-POSITIVE-B-BOUNDARY-v1`.
- Frozen pair: `(a,b)=(3/4,1/4)`.

The exact candidate tested is the GU residual

\[
R_{3/4,1/4}(f)=G(f)-\frac34I(f)-\frac14U(f)
\]

on the genuine Boolean family given by the OR of `k_r=floor(lambda 2^r)` disjoint `r`-bit point defects, for every fixed `lambda>0` as `r` tends to infinity.

## Result

Complete Fourier and unequal-child upper-set accounting proves

\[
I=2\lambda e^{-\lambda}r+O_\lambda(r2^{-r}),\quad
H=8\lambda e^{-\lambda}r+O_\lambda(1),
\]
\[
U=2\lambda e^{-\lambda}r+O_\lambda(1),\quad
G=2\lambda e^{-\lambda}r+O_\lambda(r^2 2^{-r}).
\]

The sharper terminal and signed-boundary limits are

\[
U-I\to\Psi(\lambda)
=c((2e^{-\lambda}-1)^2)
+\frac{4\lambda e^{-\lambda}(1-e^{-\lambda})}{\ln2}>0,
\qquad G-I\to0.
\]

Therefore, for every fixed `b in (0,1)`,

\[
\boxed{G-(1-b)I-bU\to-b\Psi(\lambda)<0.}
\]

In particular,

\[
\boxed{R_{3/4,1/4}(f_{k_r,r})\to-\Psi(\lambda)/4<0.}
\]

The proof treats the rare balanced intensity `lambda=ln 2` separately. There the constant Fourier atom is nonsmooth and supplies a term cancelling the apparent `2r2^{-r}` surcharge; suppressing this atom in a Taylor remainder would be invalid.

## Interpretation

The earlier first-order ratios only forced `a+b>=1`. The refined family does falsify the endpoint `G<=I`: for every fixed `lambda != ln 2`,

\[
G-I=4\lambda e^{-\lambda}r^2 2^{-r}+O_\lambda(r2^{-r})>0
\]

eventually. But this defect vanishes, whereas `U-I` tends to the strictly positive reserve `Psi(lambda)`. Hence every fixed positive `U` coefficient on the boundary absorbs the defect on this family. The threshold is not claimed uniform as `b` tends to zero or `lambda` tends to `0` or infinity.

This removes this family as an obstruction to the frozen pair `(3/4,1/4)`; it does not prove that pair universally. No ratio diverges: `G/I->1`, `U/I->1`, and `H/I->4`.

## Verification

The 140-digit Decimal reconstruction retained the two unequal children and evaluated five intensities through `r=50`. All frozen residuals were negative at `r=50`; their errors relative to `-Psi(lambda)/4` ranged from `6.58e-13` to `3.29e-12`. The program is diagnostic only; the proof is analytic for every fixed `lambda>0`.

## Remaining obligation

Convert a fixed positive fraction of the terminal reserve into a global payment for arbitrary genuine Boolean functions while preserving signed overlap and single-use influence. The natural next stress test is a growing-rank overlapping, rather than disjoint-block, family.

Requested reviewers: A090, A092, A094. Model/effort metadata: `UNKNOWN`.
