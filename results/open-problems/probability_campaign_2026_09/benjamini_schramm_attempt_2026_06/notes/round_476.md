# Round 476 one-ended product warning: \(T_d\square \mathbb Z\)

Round 476 identifies the next product calibration after finite fibers.

The finite-fiber transfer works because every exterior component has only
boundedly many boundary ports.  Even when \(u\) is small, the exceptional hub
has finite width, so a self-avoiding path can use it only boundedly many
times.  This is why the \(T_d\square K_2\) exponent is controlled by the
forward branching \(q=d-1\), not by repeated switching through the root.

This bounded-port picture fails for \(T_d\square\mathbb Z\).  With root
\((o,0)\),
\[
  d((o,0),(v,z))=d_T(o,v)+|z|.
\]
For the exterior
\[
  X_u=\{(v,z):d_T(o,v)+|z|\ge u\},
\]
all tree branches communicate through the high \(\mathbb Z\)-levels
\(|z|\ge u\).  Thus \(X_u\) is one-ended rather than a disjoint union of
bounded-port descendant cones.

A self-avoiding annular path can switch between different tree branches at
many distinct \(\mathbb Z\)-heights without revisiting a vertex.  Each height
acts as a new portal through which the path can move across the tree factor.
This creates a genuinely different transfer problem from the finite-fiber
case: the state must control an unbounded sequence of portal heights, not only
a finite bag state at one cone root.

Consequences:

1. The finite-fiber proof target \(\mathbf G=\Phi_F(z,\mathbf G;q)\) does not
   extend directly to \(T_d\square\mathbb Z\).
2. The lower bound \(\Gamma_{\rm ann}\ge\sqrt{d-1}\) from tree out-and-back
   paths remains valid but is probably not sharp.
3. The right one-ended product model is a half-plane transfer in the
   coordinates
   \[
     h=d_T(o,v),\qquad k=|z|,\qquad h+k\ge u,
   \]
   with additional self-avoidance memory preventing reuse of tree vertices at
   the same \(\mathbb Z\)-height.

This is the next serious annular-boundary test.  Finite fibers calibrate the
bounded-width case; \(T_d\square\mathbb Z\) tests whether the annular exponent
can still stay below \(1/\pc\) when the exterior of a ball has unbounded
one-ended bypass corridors.
