# B17 handoff — growing-support character defects

Source run: `fleet02/B17/20260922T061440Z-mesoscopic-defect-codimension`.

Common candidate remains `LIMIT-PRIME-GATE-LIFT-v1` with
\(C^\dagger=6.521851214\). Full FEI is open.

Two source-exact facts to reuse:

1. **Vanishing physical density is not a slope-4 principle.** If the certified balanced 18-input seed \(B\) is self-composed to \(f_k=B^{\circ k}\), then rare-gating the entire \(-1\) fibre of \(f_k\) behind \(k\) fresh zero bits and multiplying by a fresh character gives actual balanced Boolean \(G_k\) with defect density \(2^{-k-1}\to0\) but
\[
\frac{H(G_k)}{I(G_k)-1}\to
\frac{H(B)}{I(B)-1}
=6.5218457109230465\ldots>4.
\]
So fleet03/B18's fixed-pattern slope-\(4\) theorem cannot be extended using density \(\rho\to0\) alone. This is not a counterexample to the live \(C^\dagger\) candidate and the construction is decomposable.

2. **Exponential-codimension replacement.** For every actual Boolean
\(g=\chi_j(1-2\,1_A)\) that is balanced, if \(A\subset Q_n\) has density \(\rho<1/2\), then
\[
I(g)-1\ge2\rho(\log_2(1/\rho)-1)
\]
and
\[
H(g)\le h_2(4\rho(1-\rho))
+4\rho(1-\rho)\log_2(2^n-1).
\]
Hence if \(\rho\le2^{-\alpha n}\), the asymptotic ratio is at most \(2+2/\alpha\). For the live center, every \(\alpha>0.44229672878\ldots\) is eventually safe; concretely \(\rho\le2^{-n/2}\) is safe for every \(n\ge21\).

Next adversarial scope: composition-prime/off-centre gates, or balanced-uniform character defects with sublinear defect codimension. Do not return to bounded-cardinality dummy dust.
