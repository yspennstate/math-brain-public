# Round 439 endpoint weights block scalar annular averages

Round 439 records a second correction to the annular-return program.  Even
after replacing the percolation kernel by the \(Q\)-weighted SAW transfer
kernel \(A_{Q,u}^x\), a scalar averaged bound is not enough by itself.

For a marked disjoint return interval through level \(u\), deleting the
interval leaves a prefix/suffix skeleton.  When the deleted interval is
reinserted, the relevant contribution has the form
\[
  \langle \alpha, A_{Q,u}^x \beta\rangle
  =
  \sum_{a,b\in S_{u-1}(x)}
    \alpha(a)A_{Q,u}^x(a,b)\beta(b),
\]
where \(\alpha,\beta\) are endpoint weights produced by the surrounding
skeleton count.

The scalar average
\[
  \frac{1}{|S_{u-1}(x)|}
  \sum_{a,b\in S_{u-1}(x)} A_{Q,u}^x(a,b)
\]
only controls the special case where the endpoint weights are diffuse and
roughly uniform.  A self-avoiding skeleton can instead concentrate many
weighted prefixes and suffixes on a small subset of \(S_{u-1}(x)\).  In that
case the scalar average does not control
\(\langle \alpha,A_{Q,u}^x\beta\rangle\).

Thus the product/BK intuition must be replaced by one of the following
stronger inputs.

1. A Schur-type transfer bound, for example a useful estimate on
   \(\sup_a\sum_b A_{Q,u}^x(a,b)\) and its transpose.
2. An \(L^2\)-type transfer bound
   \[
     \|A_{Q,u}^x\|_{2\to2}\le \rho_u,
   \]
   plus a separate bound on the \(L^2\) size of the endpoint weights generated
   by the skeleton.
3. A new endpoint-spread dichotomy: either the endpoint weights are diffuse
   enough for an averaged annular estimate, or their concentration creates a
   separate exact-level congestion/support profile that can be charged
   elsewhere in the ladder.

This is the same obstruction already seen in the finite-set boundary-energy
program.  Boundary averages are easy to state, but the actual witness
generates weighted boundary data.  The correct estimate must control the
energy of those weights, not only the total mass of the annular kernel.

The revised disjoint-return target is therefore a weighted transfer estimate:
for every family of endpoint weights \(\alpha_i,\beta_i\) arising from
deleting \(m\) disjoint exterior-return intervals,
\[
  \prod_{i=1}^m
  \langle \alpha_i,A_{Q,u_i}^x\beta_i\rangle
\]
must gain enough over the unmarked skeleton count to beat the level-selection
entropy from Round 427.  Proving this will require either endpoint
diffuseness or a genuinely operator-norm annular bound.
