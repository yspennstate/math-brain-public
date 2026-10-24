# Round 426 monotonicity obstruction to naive scale decay

Round 426 corrects the scale-decay target stated in Round 425.  The
coefficient-scale ratio
\[
  D_{m+1}/K_{m+1}=D_m/(8K_m)
\]
is a real bookkeeping identity, but it does not by itself give a usable
logarithmic-exponent proof mechanism for the retained spread-return profiles.

The reason is monotonicity in the spread parameter.  The spread-return event
is
\[
  \mathcal X^{\rm spr}_{j,K,p}
  =
  \left\{
    \#\{u\in A_{j,p}\cap\mathbb N:u\ge1,\mathcal X_{u,0}\}
    >
    \frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H
  \right\}.
\]
If \(K_1\le K_2\), then
\[
  \frac{\theta_{\lambda,\sigma,\beta}}{4K_1}L_H
  \ge
  \frac{\theta_{\lambda,\sigma,\beta}}{4K_2}L_H,
\]
so
\[
  \mathcal X^{\rm spr}_{j,K_1,p}
  \subseteq
  \mathcal X^{\rm spr}_{j,K_2,p}
\]
and hence
\[
  \mathfrak X^{G\to H,{\rm rad,ret,spr}}_{Q,\lambda,\sigma,\beta,j,K_1}
  \le
  \mathfrak X^{G\to H,{\rm rad,ret,spr}}_{Q,\lambda,\sigma,\beta,j,K_2}.
\]
Thus larger \(K\) makes the retained spread-return event easier, not harder.
The naive target
\[
  \mathfrak X^{\rm rad,ret,spr}_{j,K}=O(K^{-1})
\]
cannot be a consequence of the definitions and is false as a general
monotonicity heuristic.

This also affects the interpretation of the bridge-record cycle.  A new
bridge-return term produced at source scale \(K_m\) has return-spread
parameter
\[
  2K_m\max\{h-1,1\},
  \qquad 1\le h\le B_m,
\]
which can be as large as a constant multiple of \(K_mB_m\), i.e. comparable
to the next fixed-gap scale.  Since the event is monotone increasing in this
parameter, the cycle pushes part of the obstruction into lower-density
spread-return events.

The correct formulation should use the density
\[
  \delta=\frac{\theta_{\lambda,\sigma,\beta}}{4K}
\]
rather than the scale \(K\).  A plausible usable hypothesis is not
polynomial decay in \(K\), but a density-rate estimate of the form
\[
  \mathfrak X^{\rm rad,ret,spr}_{j,K}(s,p)
  \le
  D_H^{-(\psi(\delta)+o(1))L_H},
  \qquad \delta=\theta/(4K),
\]
for some positive rate \(\psi(\delta)\) when \(\delta>0\), together with a
compatible long-run estimate.  Such a statement may have \(\psi(\delta)\to0\)
as \(\delta\downarrow0\).

Consequently, an infinite bridge-record descent is not justified unless one
also proves a uniform summability statement coupling the coefficient growth
and the decay of \(\psi(1/K_m)\).  In the existing finite-exponent framework,
where all \(K_m\) and coefficients are fixed before \(p\uparrow p_c\), finite
coefficients do not affect the logarithmic exponent; the live obligation is
still to prove positive fixed-density exponent bounds for every retained
spread-return and long-run family that appears in the finite ladder.

The next target is therefore revised:

1. prove or disprove a fixed-density spread-return exponent lemma for
   \(\mathcal X^{\rm spr}_{j,K,p}\) with \(K<\infty\) fixed;
2. track how its exponent depends on \(\delta=\theta/(4K)\);
3. only then decide whether the bridge-record coefficient-scale identity can
   be promoted to a summable infinite-depth argument.
