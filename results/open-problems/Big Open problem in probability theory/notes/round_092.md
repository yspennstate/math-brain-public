# Round 092 log

## Goal

Clarify the exact normalization of the two-replica profile needed for
finite-set escape.

## Result

Added `prop:fe-iff-sublinear-two-replica`.

For any positive symmetric kernel \(Q\) with row sums at most one, define
\[
  \eta(Q)=\sup_K |K|^{-1}\langle 1_K,Q1_K\rangle
\]
and
\[
  \rho(Q)=\sup_K |K|^{-1}\|Q1_K\|_2^2 .
\]
Then
\[
  \eta(Q)^2\le \rho(Q)\le \sqrt{6\eta(Q)}.
\]

Applied to \(Q_p=T_p/\bar\chi_p\), this gives
\[
  \eta(Q_p)\to0
  \quad\Longleftrightarrow\quad
  \mathcal R_p^*/\bar\chi_p\to0.
\]

Also added `cor:sublinear-two-replica-criterion`, which restates the
Hutchcroft finite-set criterion in this normalization: mean-field
susceptibility plus \(\mathcal R_p^*/\bar\chi_p\to0\) implies
\(p_c<p_{2\to2}\).

The proof is constructive.  If \(\|Q1_K\|_2^2/|K|=a\), then the level set
\[
  H=\{Q1_K\ge a/2\}
\]
has \(|H|\le 2|K|/a\), and \(U=K\cup H\) has normalized \(Q\)-mass at least
\(a^2/6\).

## Interpretation

Finite-set escape is exactly the sublinear two-replica condition
\(\mathcal R_p^*=o(\bar\chi_p)\).  The bounded two-replica profile used in
the intermediate theorem is therefore a stronger target, while Round 091 shows
that the desired strict \(L^2\) gap would force the even stronger conclusion
\(\mathcal R_p^*\to0\).
