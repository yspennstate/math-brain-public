# Round 477 product-shuffle fork for \(T_d\square\mathbb Z\)

Round 477 isolates the next question raised by the one-ended product warning.

For the global SAW \(L^2\) operator on a Cartesian product, the shuffle
construction gives a lower bound of the form
\[
  \gamma_{\rm SAW,2}(T_d\square H)
  \ge
  \sqrt{d-1}+\mu(H).
\]
For \(H=\mathbb Z\), this is \(\sqrt q+1\), where \(q=d-1\).

The finite-fiber annular calculations do not realize this additive lower
bound.  In \(T_d\square K_2\), tree branching must be paid in out-and-back
pairs inside bounded-port cones, giving only \(\sqrt q\).  In
\(T_d\square K_m\), the finite-fiber entropy is also tied to using disjoint
fiber sets on the outward and inward legs.

For \(T_d\square\mathbb Z\), the situation is unclear.  The exterior of a
ball has unbounded portal heights, so a path may be able to combine:

1. tree out-and-back entropy, contributing \(\sqrt q\);
2. monotone or near-monotone \(\mathbb Z\)-motion, contributing the line
   connective constant \(1\);
3. binomial shuffle entropy from interleaving the two motions.

If the sphere constraint can be satisfied while preserving self-avoidance and
the exterior condition, this would give an annular lower bound of the
global-product type
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)\ge \sqrt q+1.
\]
If not, then the annular exponent remains genuinely weaker than the global
SAW operator even in the first one-ended product.

This is now a concrete fork:

* Construct an annular product-shuffle family in \(T_d\square\mathbb Z\), or
* prove that every exterior return must couple \(\mathbb Z\)-motion to tree
  return depth strongly enough to lose the additive shuffle entropy.

Resolving this fork is necessary before using \(T_d\square\mathbb Z\) as
evidence for or against the universal annular gap
\[
  \Gamma_{\rm ann}(G)<1/\pc(G).
\]
