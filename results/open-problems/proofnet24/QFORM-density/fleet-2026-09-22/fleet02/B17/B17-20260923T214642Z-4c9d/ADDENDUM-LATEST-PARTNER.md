# Addendum: latest fleet03/B17 synchronization

After the main report was written, the newest compatible designated-partner handoff appeared: fleet03/B17 `20260923T212932Z-fleet03-B17-QFORM-auto11`, canonical math commit `03b5948d1695cd5370bb965a37c9e10a936c7e28`.

Its proved theorem `QFORM-TWOHEAVY-ZEROPIVOT-GLOBAL-v1` treats the complementary exact-spectrum matrix

\[
A_0=\begin{pmatrix}
1/2&-1/2&-1/\sqrt2\\
-1/2&1/2&-1/\sqrt2\\
-1/\sqrt2&-1/\sqrt2&0
\end{pmatrix},
\qquad A_0^2=I,
\qquad \operatorname{spec}(A_0)=\{1,1,-1\},
\]

with the first two physical laws centered unit intervals and the third physical law an arbitrary probability density `0<=f<=1`. It proves the global bound

\[
\|p_{Q_0}\|_\infty\le 2^{9/4}-1
=3.756828460010884\ldots<3\sqrt2.
\]

This completed result is applied here to the combined sharp-witness obstruction. Let `\mathcal W_1` be the arbitrary-six-law positive-sheet Householder family proved in the main report, and let `\mathcal W_2` be the partner's arbitrary-third-law zero-pivot family. Then

\[
\sup_{W\in\mathcal W_1}\operatorname*{ess\,sup}_{s\ge0}p_W(s)
\le p_*(0)<\frac{508}{125},
\]

while

\[
\sup_{W\in\mathcal W_2}\|p_W\|_\infty
\le2^{9/4}-1.
\]

Since `2^(9/4)-1 < 508/125` (equivalently `2^(9/4)<633/125`; raising to the fourth power gives the exact rational check `512 < (633/125)^4`), the union obeys the single concrete obstruction

\[
\boxed{
\sup_{W\in\mathcal W_1\cup\mathcal W_2}
\Bigl[\text{relevant density norm}\Bigr]
<\frac{508}{125}<3\sqrt2.
}
\]

For `\mathcal W_1`, “relevant density norm” means the majority-sign essential supremum `ess sup_{s>=0}`; for `\mathcal W_2`, it is the full global norm. Thus two different adversarial mechanisms are simultaneously subcritical: (i) arbitrary rough/near-kernel fragmentation in all six physical coordinates on the Householder one-sheet side, and (ii) arbitrary rough/unbounded fragmentation in a zero-physical-pivot shared coordinate with two centered heavy inputs.

The partner theorem does **not** fill the remaining gap in the main report: the minority-sign/two-sheet side of the six-law Householder family is still unpaid. Conversely, the present rearrangement theorem does not make the partner's first two heavy physical laws arbitrary on both output sheets. This is a genuine complementarity statement, not a claim that either scoped theorem proves the full QFORM conjecture.

Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED; continuity remains separate except in the partner's scoped zero-pivot family. Native brain status remains `WITHOUT_VERIFIED_BRAIN`.
