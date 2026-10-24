# Round 478 portal-staircase lower bound in \(T_d\square\mathbb Z\)

Round 478 gives a concrete lower bound showing that the unbounded portal
heights in \(T_d\square\mathbb Z\) create real annular entropy.

Let \(q=d-1\), root at \(x=(o,0)\), and take \(u\) large.  Choose a tree
vertex \(v\) at depth \(u\), and let \(U=\{(\operatorname{par}(v),0)\}\subset
S_{u-1}(x)\).  The outward neighbor \((v,0)\) lies in \(X_u\).

First move from \((v,0)\) to \((o,u)\) using:

* \(u\) inward tree steps toward \(o\);
* \(u\) upward \(\mathbb Z\)-steps.

The path stays in \(X_u\) exactly when every prefix has at least as many
upward \(\mathbb Z\)-steps as inward tree steps.  The number of such
interleavings is the Catalan number
\[
  C_u\asymp 4^u u^{-3/2}.
\]

Then choose a terminal tree vertex \(w\) at depth \(u\) in a principal branch
different from that of \(v\), and move from \((o,u)\) to \((w,0)\) using:

* \(u\) outward tree steps along the geodesic to \(w\);
* \(u\) downward \(\mathbb Z\)-steps.

The exterior condition is now that every prefix has at least as many outward
tree steps as downward \(\mathbb Z\)-steps, again giving \(C_u\) Catalan
interleavings.  The two principal branches are different, so the second
staircase does not revisit vertices of the first except at the joining point
\((o,u)\).

Let \(V\subset S_{u-1}(x)\) be the set of parents \((\operatorname{par}(w),0)\)
for these terminal vertices \(w\).  Then \(|V|\asymp q^u\), and the length
inside \(X_u\) is \(4u\).  The contribution to the annular cut norm is at
least
\[
  \frac{C_u^2 |V|}{\sqrt{|U||V|}}
  \asymp
  \frac{16^u q^{u/2}}{\operatorname{poly}(u)}.
\]
Therefore
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)
  \ge
  2\,q^{1/8}.
\]
Together with the tree out-and-back lower bound from Round 462, this
singleton-start calibration is
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)
  \ge
  \max\{\sqrt q,\ 2q^{1/8}\}.
\]
Round 479 improves the portal term by using large starting and terminal
boundary sets.

This lower bound is not expected to be sharp.  It does not settle the
product-shuffle fork from Round 477, but it proves that the one-ended
high-\(\mathbb Z\) portals add entropy beyond the bounded-cone picture.  In
particular, the \(T_d\square\mathbb Z\) annular transfer cannot be modeled as
a finite-fiber return recursion with only boundedly many ports.
