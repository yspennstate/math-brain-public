# Round 461 annular product stress is weaker than global SAW stress

Round 461 compares the product lower bound from Round 460 with the old global
SAW operator stress test.

For the global route, Round 009 gave
\[
  \gamma_{\rm SAW,2}(T_d\square H)
  \ge
  \sqrt{d-1}+\mu(H),
\]
so the global SAW operator gap can only work if
\[
  p_c(T_d\square H)
  <
  \frac{1}{\sqrt{d-1}+\mu(H)}.
\]
This is often too strong for low-branching products.

The annular boundary exponent sees a different mechanism.  The first
staircase construction from Round 460 gives
\[
  \Gamma_{\rm ann}(T_d\square H)\ge\sqrt{g_{\rm geo}(H)}.
\]
That particular lower bound has no tree-branching term because it trades
inward tree movement directly against factor geodesic motion.  Round 462
records a stronger out-and-back construction showing that tree branching can
also contribute as \(\sqrt{d-1}\).

Thus, after the correction in Round 462, the annular gap
\[
  \Gamma_{\rm ann}(G)<1/\pc(G)
\]
is not refuted by the standard product obstruction to the global SAW operator
route.  It remains a genuinely weaker target, at least under these basic
diagnostics.

This does not prove the annular gap on products.  There may be more elaborate
exterior returns that combine tree branching and factor motion more
efficiently than the simple staircase.  But the first product calibration is
encouraging: the annular exponent is focused on return geometry rather than
all forward SAW propagation.

The next product-specific task is to bound \(\Gamma_{\rm ann}\) from above on
\(T_d\square\mathbb Z\) or \(T_d\square\mathbb Z^r\) using a transfer matrix
for the distance pair
\[
  (d_T(o,\cdot), d_H(h_0,\cdot)).
\]
That would test whether the annular gap is a plausible general replacement
for the global SAW operator gap.
