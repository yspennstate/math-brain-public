SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B06, 2026-09-23T18:30:23Z.
attacking: convert partner r40's anchored cofactor bank into the exact projected-crossing currency seen by a physical one-hub weighted receiver, without dropping the cross tail.

# Early substantive calculation

Write partner r40's ORIGINAL-coordinate cross block after choosing its heavy anchors as

\[
N=\begin{pmatrix}b&r^T\\ c&D\end{pmatrix},\qquad
Z_{ia}=\|bD-cr^T\|_F^2.
\]

Use physical hub `i`.  In the light variables split `I=J\setminus\{i\}` and `J'=\{a\}\cup(K\setminus\{a\})`.  The restriction of the hub partner to `J'` is

\[
w=(b,r),
\]

and the remainder crossing block from `I` to `J'` is

\[
A_0=[c\;D].
\]

Let `Pi_w` be orthogonal projection onto `span(w)` and set `C=A_0(I-Pi_w)`, `F=\|C\|_F`.  Rowwise Lagrange identity gives the exact formula

\[
\|w\|^2F^2
 =\sum_{j\in I}\sum_{u<v}(w_u(A_0)_{jv}-w_v(A_0)_{ju})^2
 \ge \sum_{j,\beta}(bD_{j\beta}-c_jr_\beta)^2
 = Z_{ia}.
\]

Therefore

\[
\boxed{\ \|w\|F\ge \sqrt{Z_{ia}}\ }.
\]

The same identity holds in the opposite orientation with `w'=(b,c)` and crossing block `[r\;D^T]`.  This is the exact bridge from partner r40's cofactor currency to the projected-crossing currency of the current Claude one-hub Proposition 6.6; no individual minor is selected and every cross-tail entry remains present.

On partner r40's live packet,
\[
Z_{ia}>4395076119/2748779069440=0.0015989193776476895\ldots,
\]
so in either orientation
\[
\|w\|F>0.03998648993907429\ldots.
\]

Next step: impose/check the Proposition 6.6 row-share gate.  If it holds, the displayed identity immediately produces a dimension-free logarithmic small-ball bound.  If it fails, the heavy projected row itself has wedge currency exceeding `sqrt(Z_ia/2)`, giving a new literal physical hub rather than an invalid fiber supremum.
