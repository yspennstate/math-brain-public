# Round 181

Round 181 adds a weighted-profile audit for the Round 180 square-profile
branch.

For a finitely supported non-zero weight \(w:V\to[0,\infty)\), layer-cake over
the level sets \(K_t=\{x:w(x)>t\}\) gives
\[
  \sum_z
  \left(
    \sum_{\substack{x\\d(x,z)\in I}}w(x)\tau_p(x,z)
  \right)^2
  \le
  \bar\chi_p^2\|w\|_1\|w\|_\infty\Theta_p(I).
\]
Thus weighted annular square profiles are not a stronger object than the
existing unweighted \(\Theta_p(I)\); the unweighted level-set supremum already
dominates them.

The same lemma gives a reusable lower bound.  If \(A,Y\) are finite,
\(w:A\to[0,1]\), \(S=\sum_A w>0\), and every \(a\) with \(w(a)>0\) has
\[
  \sum_{\substack{y\in Y\\d(y,a)\in I}}\tau_p(y,a)\ge m,
\]
then
\[
  \Theta_p(I)\ge \frac{m^2S}{\bar\chi_p^2|Y|}.
\]

Applied to the expanded gate-annulus data with \(w=\mathbf 1_A\), this is the
Round 180 lower bound.  Applying it with root weights
\(w(a_z)=\tau_p(x,a_z)\) does not improve the exponent, because the current
input only proves
\[
  \sum_z\tau_p(x,a_z)\ge\kappa_j^{\rm vol}(p),
\]
the same lower size available from \(|A|\ge\kappa_j^{\rm vol}(p)\).  Therefore
reweighting the gate set is lossless but not stronger.  To improve the
square-profile threshold one needs genuinely new information: either a larger
selected gate count, a larger total selected root weight, or a smaller support
set \(Y\).
