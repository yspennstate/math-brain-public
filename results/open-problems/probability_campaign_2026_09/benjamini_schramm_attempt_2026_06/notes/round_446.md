# Round 446 coverage-root profile reduction

Round 446 packages the coverage split from Rounds 444--445 as a
property-restricted profile reduction.

In a slab \(A_{j,p}\), put
\[
  \delta=\frac{\theta_{\lambda,\sigma,\beta}}{4K},
  \qquad N=\delta L_H.
\]
For an exterior-return interval \(I\) through level \(u(I)\), define its slab
coverage block
\[
  C_{j,p}(I)
  =
  [u(I),M(I)]\cap A_{j,p}\cap\mathbb N,
\]
where \(M(I)\) is the maximum radius reached by \(I\).

For \(\kappa>0\), define two properties of rooted paths.

The many-root property \(\mathcal X^{\rm rootdisj}_{j,\kappa,p}\) is that
the path contains at least
\[
  \lceil \kappa L_H\rceil
\]
pairwise time-disjoint exterior-return intervals through levels in
\(A_{j,p}\).

The few-root-cover property \(\mathcal X^{\rm cov}_{j,K,\kappa,p}\) is that
there are fewer than \(\lceil\kappa L_H\rceil\) pairwise time-disjoint
exterior-return intervals \(I_1,\ldots,I_m\) such that
\[
  \left|\bigcup_{r=1}^m C_{j,p}(I_r)\right|
  >
  \delta L_H.
\]

Then the spread-return property satisfies the deterministic inclusion
\[
  \mathcal X^{\rm spr}_{j,K,p}
  \subseteq
  \mathcal X^{\rm rootdisj}_{j,\kappa,p}
  \cup
  \mathcal X^{\rm cov}_{j,K,\kappa,p}.
\]

Proof: choose one exterior-return interval for every return level counted by
\(\mathcal X^{\rm spr}_{j,K,p}\).  The chosen intervals form a laminar
forest.  If the number of root intervals is at least \(\lceil\kappa L_H\rceil\),
those roots are pairwise time-disjoint, giving
\(\mathcal X^{\rm rootdisj}_{j,\kappa,p}\).  Otherwise the root intervals are
fewer than \(\lceil\kappa L_H\rceil\), and by Round 444 their slab coverage
blocks cover all selected return levels, hence more than \(\delta L_H\)
levels.  This gives \(\mathcal X^{\rm cov}_{j,K,\kappa,p}\).

Consequently the spread-return radial profile obeys
\[
  \mathfrak X^{\rm rad,ret,spr}_{Q,\lambda,\sigma,\beta,j,K}
  \le
  \mathfrak X^{\rm rootdisj}_{Q,\lambda,\sigma,\beta,j,\kappa}
  +
  \mathfrak X^{\rm cov}_{Q,\lambda,\sigma,\beta,j,K,\kappa},
\]
with the two right-hand profiles defined by replacing
\(\mathcal X^{\rm spr}_{j,K,p}\) by the corresponding property in the usual
property-restricted radial profile.

This reduction is coefficient-free and keeps positive density in the
many-root branch.  The few-root branch has low coverage entropy, while the
many-root branch is the corrected target for annular transfer/cut estimates.
