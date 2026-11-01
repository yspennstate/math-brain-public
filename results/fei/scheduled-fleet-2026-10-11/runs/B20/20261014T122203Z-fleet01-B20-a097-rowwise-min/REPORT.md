# B20 / A097 — rowwise-minimum singleton cut

**Status:** a strictly smaller universal-GU obligation is proved. Universal GU and full FEI remain **OPEN**; independent review is pending.

## Frozen candidate and prior obstruction

The frozen pair is

\[
G(f)\le4I(f)+\frac34U(f)
\]

for every genuine Boolean function in every finite dimension. The preceding source-complete cut retained

\[
G\le D_{\ge2}+\frac12V_1+\frac2{\ln2}(I-Q_{\ge3}).
\]

The newest B11 one-point-surgery family proves that `V1/2` cannot be paid separately by any absolute multiple of `Q_ge3`, even under relevance, tensor-primality, and degree at least three.

## New assembled theorem

For each singleton index `j`, define

\[
r_j=\sum_{i\ne j}p(ij),\qquad
s_j=\sum_{|S|\ge3:j\in S}p(S),
\]

\[
V_j=\sum_{i\ne j}(p(j)+p(ij))
\log_2\frac{\pi(j)}{p(j)+p(ij)}.
\]

Two independent genuine-Boolean estimates apply to the **same row**:

\[
\sum_{i\ne j}K_{i,\{j\}}
\le \frac12V_j+\frac1{\ln2}r_j,
\]

and, using the ternary derivative `D_j f in {-1,0,1}`,

\[
\sum_{i\ne j}K_{i,\{j\}}
\le\frac9{\ln2}(2r_j+s_j).
\]

Taking the minimum **before** summing yields

\[
\boxed{
G\le D_{\ge2}+\frac2{\ln2}M_1+
\sum_j\min\left\{
\frac12V_j+\frac{r_j}{\ln2},
\frac9{\ln2}(2r_j+s_j)
\right\}.}
\]

This is stronger than either global singleton payment alone. It also retains the sharper global corollary

\[
K^{(1)}\le\frac1{\ln2}
\left(36W_2+9\sum_{d\ge3}dW_d\right),
\]

rather than the earlier coarser coefficient `36` on all higher levels.

## Strictly smaller unpaid leaf

It now suffices to prove, only for tensor-prime positive-residual genuine Boolean functions of Fourier degree at least three,

\[
\boxed{
D_{\ge2}+\frac2{\ln2}M_1+
\sum_j\min\left\{
\frac12V_j+\frac{r_j}{\ln2},
\frac9{\ln2}(2r_j+s_j)
\right\}
\le4I+\frac34U.}
\]

This removes the unbounded `V1/Q_ge3` obstruction: the second branch is dimension-free, dummy-invariant, and depends only on actual level-two and higher energy. The remaining difficulty begins with the signed term plus `|A|>=2` KL rows in `D_ge2`; those terms are not separated or declared paid.

For the exact B11 surgery spectrum, its proved lower bound on the old global singleton budget first exceeds the new ternary global budget at `d=50`:

\[
13.2213475204>12.9842553680.
\]

The old budget then grows linearly, while the new budget converges to `9/ln(2)`. Thus the improvement is strict on the family that refuted every separate `V1 <= C Q_ge3` payment.

If the displayed leaf is proved, then `G<=4I+3U/4` universally. The audited induction gives `U<=16I`, and `H<=2I+2U` gives `H<=34I`.

The conditional reduction was rederived from the source, not inferred from its headline: weighted averaging of `sum_i Delta_i U=G` against `sum_i Inf_i=I`, followed by induction on both physical children, gives `U<=aI/(1-b)`; then the source inequality `H<=2(I-Var(f))+2U` yields `H<=(2+2a/(1-b))I`. Constants are treated separately.

## Proof and verification

The proof reconstructs the ternary-derivative scalar lemma from the signed branch constraints `|a+-b|<=M+-2C`, keeps the signed posterior through the KL term, and combines it rowwise with the genuine-child singleton estimate. No arbitrary spectral law, finite maximum, or unsigned-correlation relaxation is used.

The checker exhausts every Boolean function modulo global output sign through four variables, adds seeded controls in dimensions five and six, checks both rowwise bounds and their minimum, checks the sharp root payment, and probes the one-point-surgery family. See `CHECK.out` for actual counts and extrema.

Model/effort metadata: `UNKNOWN`.

## Next action

Apply the same physical-derivative normalization to the `|A|=2` rows and keep the rowwise-minimum architecture. The next lemma must control the signed `D_ge2` aggregate on the minimal positive-residual class; a separate unsigned bound is not sufficient.
