# account04/B14 handoff — affine physical core and aligned rank drop

Run: 20260923T061428Z-account04-B14-affine-physical-core-r8  
Status: supporting target-level synthesis proved; full QFORM remains open.  
Execution: WITHOUT_VERIFIED_BRAIN. Continuity is separate.

## Source pins

- Active request blob: 165c570ecb4dcc6299c38fc3298771e4a8339dac.
- B14 assignment blob: 46b1d3db2ffb7759153a7209cd4cc34071e8c362.
- Correction inbox blob: c7000cf3822ae4935a2faf43b89ac92ea65ac0fe.
- Required Claude package baseline: math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837.
- Completed partner account01/B14 r30: math-open-problems@fe1b05ba7083f2da708eed681eb13b65236e9209.
- Prior account04/B14 r7: math-open-problems@2ac84e141e8e939506cbd5cd8314589141b714d5.

## New compiled theorem

If an actual original-coordinate \(3\times3\) principal block \(B\) satisfies \(s_{\min}(B)\ge\sigma\), then conditioning on every outside original coordinate preserves the active product law and gives

\[
\|p_{X^TAX}\|_\infty\le 6\sqrt\pi/\sigma,
\]

uniformly in all conditioning-generated affine terms, arbitrary outside spectrum/couplings, translations, and rough fragmented or unbounded laws.

For signature \((2,1)\), with

\[
\tau(z)=z^T(D-C^TB^{-1}C)z,
\]

the ruled estimate simultaneously gives

\[
\Pr\{Q\in I,\ Q\ge\tau(Z)\}\le C_+(B)|I|
\le \pi\sqrt2\,|I|/\sigma.
\]

The opposite moving side is obtained for signature \((1,2)\). Smooth cap-preserving approximation plus product-TV contraction supplies the rough-law trace justification; no density version is evaluated on a quadratic surface.

At exact rank two, if the kernel leakage factors through one coarsened disjoint bank \(W=a^TV\), account01/B14 r30 gives

\[
\|p_Q\|_\infty
\le
\frac{C_4}
{\min\{\nu,|\gamma|\|a\|_2/\sqrt2\}},
\qquad C_4=1000(8+\log4).
\]

For \(B=\operatorname{diag}(1,-1,0)\) and \(|\gamma|\|a\|_2\ge1\), the matrix is genuinely in the full target and

\[
\|p_Q\|_\infty\le\sqrt2 C_4<13274.3.
\]

## Remaining implication

The near-rank-two chamber and exact rank-two cores with overlapping, non-factorable leakage statistics remain open. A small matrix coefficient cannot be treated as a small random quadratic error for arbitrary unbounded laws. The next structural step must extract an actual physical-core gate, a disjoint aligned leakage bank, or a joint cross-volume/ridge certificate.

Canonical report: math-open-problems commit e0fd3e5ae1e84a7a7d1eec28949bd962e0ca5bf8, blob f0bc74c60cd6b793e46ddf2b58d48cc2b279194a.
