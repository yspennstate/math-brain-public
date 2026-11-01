# Round 427 entropy cost in fixed-density spread-return estimates

Round 427 sharpens the corrected Round 426 target by identifying the
combinatorial entropy that any fixed-density spread-return proof must beat.

In the slab localization,
\[
  W_{\beta,p}=\max\{1,\lfloor \beta L_H\rfloor\},
\]
so a slab \(A_{j,p}\) contains \(W_{\beta,p}+O(1)\) possible return levels.
For
\[
  \delta=\frac{\theta_{\lambda,\sigma,\beta}}{4K},
\]
the spread-return event requires more than \(\delta L_H\) return levels in a
slab of length about \(\beta L_H\).  A proof that first selects the set of
return levels pays, at the logarithmic scale, the entropy
\[
  \log \binom{\beta L_H}{\delta L_H}
  =
  \beta H(\delta/\beta)L_H+o(L_H),
\]
where
\[
  H(t)=-t\log t-(1-t)\log(1-t).
\]
In base \(D_H\), this is
\[
  \frac{\beta H(\delta/\beta)}{\log D_H}L_H+o(L_H).
\]

Thus a density-rate lemma cannot merely show a per-return saving of the form
\(\exp[-c\delta L_H]\) unless
\[
  c\delta>\beta H(\delta/\beta).
\]
For small \(\delta\),
\[
  \beta H(\delta/\beta)
  =
  \delta\log(\beta/\delta)+O(\delta),
\]
so a purely linear-in-\(\delta\) saving with fixed \(c\) is not enough as
\(\delta\downarrow0\).  This is exactly the regime created by repeated
bridge-record cycles, since the retained bridge-return spread terms can have
parameters comparable to the next scale and hence density threshold
\(\delta_m\simeq 1/K_{m+1}\).

The corrected quantitative target is therefore:

* prove a return-level cost function \(a(\delta)\) for the property
  \(\mathcal X^{\rm spr}_{j,K,p}\);
* verify
  \[
    a(\delta)>\frac{\beta H(\delta/\beta)}{\log D_H}
  \]
  on the density range actually produced by the finite ladder;
* avoid sending \(\delta\) to zero through an infinite bridge-record descent
  unless the cost function has superlinear small-density strength sufficient
  to beat \(\delta\log(1/\delta)\).

This explains why the bridge-record coefficient identity from Round 425 is
not enough: coefficients fixed before \(p\uparrow p_c\) disappear from the
logarithmic exponent, while the level-choice entropy remains at order
\(L_H\).  The next useful attack is to look for a structural reason that
exterior returns at many levels are not independently placeable, which would
lower the entropy below the raw binomial bound.
