# Round 474 clique-fiber stress test for the strong \(<q\) target

Round 474 gives a concrete reason the finite-fiber target must be compared
with \(1/\pc(T_d\square F)\), not uniformly with \(q=d-1\).

Take \(F=K_m\), root \(0\in K_m\), and \(q=d-1\).  Here
\[
  d((o,0),(v,f))=d_T(o,v)+\mathbf 1_{\{f\ne0\}},
\]
so a component over a boundary tree vertex \(t\) has one descendant-side port
\((t,0)\) and \(m-1\) parent-side ports
\[
  (\operatorname{par}(t),f),\qquad f\ne0.
\]

Choose disjoint fiber sets
\[
  O,I\subseteq\{1,\ldots,m-1\},\qquad |O|=\alpha,\quad |I|=\beta,
\]
with \(\alpha,\beta\ge2\).  An annular return can:

1. enter from \((t,0)\) into a fiber in \(O\);
2. follow an outward tree ray of length \(r\), and in each visited bag
   traverse a self-avoiding \(K_m\)-path through the fibers of \(O\);
3. switch once at the deepest bag from \(O\) to \(I\);
4. return inward along the same tree ray, and in each visited bag traverse a
   self-avoiding \(K_m\)-path through the fibers of \(I\);
5. exit through a parent-side port in \(I\).

The sets \(O\) and \(I\) are disjoint, so the inward part does not revisit
vertices used by the outward part in any bag.  With fixed entry and exit
coordinates in \(O\) and \(I\), there are at least
\[
  ((\alpha-2)!(\beta-2)!)^r
\]
choices for the in-bag fiber paths, and \(q^r\) choices for the outward tree
ray.  The length is \(r(\alpha+\beta)+O(1)\).  Therefore
\[
  \Gamma_{\rm ann}(T_d\square K_m)
  \ge
  \max_{\substack{\alpha,\beta\ge2\\ \alpha+\beta\le m-1}}
  \bigl(q(\alpha-2)!(\beta-2)!\bigr)^{1/(\alpha+\beta)}.
\]

Taking \(\alpha\) and \(\beta\) of order \(m/2\), Stirling's formula gives a
lower bound of order \(m\) for fixed \(q\).  Hence the strong sufficient
condition
\[
  \Gamma_{\rm ann}(T_d\square K_m)<q
\]
cannot be expected uniformly in \(m\).

This does not threaten the desired annular gap.  The same clique fibers also
increase the finite-type percolation branching matrix from Round 473, so
\(1/\pc(T_d\square K_m)\) grows with \(m\) as well.  The right calibration is
the finite comparison
\[
  \Gamma_{\rm ann}(T_d\square K_m)<1/\pc(T_d\square K_m),
\]
not the embedded-tree comparison with \(q\).
