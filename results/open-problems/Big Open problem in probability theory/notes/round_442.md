# Round 442 subset boundary energy for annular cuts

Round 442 rewrites the annular cut profile from Round 441 as a subset
boundary-energy estimate.

Fix \(x,u,L\) and put \(X_u=V\setminus B_{u-1}(x)\).  For
\(U,V\subseteq S_{u-1}(x)\), define pushed boundary vectors on \(S_u(x)\) by
\[
  \nu_U(y)=\#\{a\in U:a\sim y\},
  \qquad
  \nu_V(y)=\#\{b\in V:b\sim y\}.
\]
Then the truncated \(Q\)-weighted annular cut mass satisfies
\[
  A_{Q,u,\le L}^x(U,V)
  \le
  Q^2
  \langle \nu_U,C_{Q,\le L-2}^{X_u}\nu_V\rangle.
\]
This is the subset version of Round 440.

The scalar whole-sphere diagnostic uses \(U=V=S_{u-1}(x)\).  The endpoint
problem requires much more: control for arbitrary or at least
skeleton-generated subsets \(U,V\).  Thus the live analytic target becomes a
family of estimates of the form
\[
  Q^2
  \langle \nu_U,C_{Q,\le L}^{X_u}\nu_V\rangle
  \le
  \Phi_Q(L,|U|,|V|,|S_{u-1}(x)|),
\]
with a rate function \(\Phi_Q\) strong enough to survive the dyadic endpoint
decomposition from Round 441.

Several benchmark bounds clarify the scale.

* A Schur bound would give
  \[
    A(U,V)\le \rho\,\min\{|U|,|V|\}.
  \]
  This is strong enough for arbitrary endpoint weights but is likely too
  optimistic near the target range \(Q>\pc(G)\).
* An \(L^2\) bound would give
  \[
    A(U,V)\le \rho\,\sqrt{|U||V|}.
  \]
  This matches operator methods but risks being close to the desired
  \(p_c<p_{2\to2}\) conclusion.
* A pure whole-sphere average gives only
  \[
    A(S_{u-1},S_{u-1}),
  \]
  and leaves concentrated endpoint weights uncontrolled.

The subset-energy formulation is therefore the right middle target.  It is
stronger than the scalar annular average but weaker than demanding a global
operator bound on the entire killed exterior SAW kernel.  It also gives a
clear inverse problem: if spread-return estimates fail, extract boundary
subsets \(U,V\) in many annuli with anomalously large truncated exterior SAW
energy.
