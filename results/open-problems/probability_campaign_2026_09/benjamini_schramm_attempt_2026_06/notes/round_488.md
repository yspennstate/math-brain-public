# Round 488 stack-charge lemma for the tree-line split

Round 488 isolates the combinatorial lemma needed for the upper target in
Round 487.

Fix an annular exterior self-avoiding path in \(T_d\square\mathbb Z\), and
let
\[
  a=\#\{\text{tree-coordinate steps}\},\qquad
  b=\#\{\mathbb Z\text{-steps}\},\qquad n=a+b.
\]
Project the path to the tree.  The projected tree walk has length \(a\).
After reducing immediate cancellations, suppose its endpoint displacement in
the tree is \(D\).  Then the tree walk has
\[
  P=\frac{a+D}{2}
\]
forward stack pushes and
\[
  R=\frac{a-D}{2}
\]
stack pops.

A raw stack count would pay roughly \(q^P\), too large.  In the annular cut
norm, however, endpoint averaging over boundary sets supplies exactly the
Haagerup gain \(q^{D/2}\), leaving
\[
  q^{P-D/2}=q^{a/2}.
\]
This is the desired tree factor in Round 487.  The remaining issue is not the
branching weight but the number of possible push-pop schedules: arbitrary
tree walks carry Catalan entropy that would normally produce a \(2^a\)-type
loss.

The needed stack-charge lemma is:

> For annular exterior SAWs in \(T_d\square\mathbb Z\) with \(a\) tree steps
> and \(b\) line steps, the push-pop schedule of the tree projection can be
> encoded, up to \(e^{o(n)}\) choices, by the interleaving pattern of the
> \(a\) tree steps among the \(n\) total steps together with the line-height
> trace.

Equivalently, self-avoidance should force every nontrivial tree pop to be
paid by a line-height separation: crossing back over a tree edge at the same
height would revisit a vertex.  Thus Catalan tree-stack entropy is not free;
it is coupled to the \(\mathbb Z\)-motion already counted by the binomial
\(\binom na\).

If this lemma holds, then for each \(a\)
\[
  \frac{\langle \nu_U,C_{n,a}^{X_u}\nu_V\rangle}{\sqrt{|U||V|}}
  \le
  e^{o(n)}\binom na q^{a/2},
\]
which gives
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)\le \sqrt q+1.
\]

The portal constructions clarify why the lemma must use line-height memory.
In a root-portal bubble, many stack pops occur, but each pop is separated
from its matching push by upward line motion; the corrected generating
function in Round 484 is exactly a counted example of this charge mechanism.
