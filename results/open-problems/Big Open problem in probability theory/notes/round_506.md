# Round 506 two-state scalar trace skeleton is subcritical

With the corrected child-atom inventory from Round 505, the simplest
compressed-trace skeleton is already subcritical.

Ignore, for the moment, distinct portal heights, hard-core adjacent gaps, and
the killed excess walk.  Keep only:

1. the corrected row-summed inventory for a child-cone atom,
   \[
     A_q(z)=qz^2w_*(z)^2\frac{2z}{1-z},
     \qquad
     w_*(z)=\frac{2z}{1+z^2};
   \]
2. the row-summed inventory for a nonempty vertical run,
   \[
     U(z)=\frac{2z}{1-z};
   \]
3. the maximal-compression rule that two vertical runs cannot be consecutive.

This gives a two-state transfer matrix for the atom sequence:
\[
  R_q(z)=
  \begin{pmatrix}
    A_q(z) & U(z)\\
    A_q(z) & 0
  \end{pmatrix},
\]
where the states record whether the previous atom was non-vertical or
vertical.  Its positive eigenvalue is
\[
  \rho_q(z)
  =
  \frac{A_q(z)+\sqrt{A_q(z)^2+4A_q(z)U(z)}}{2}.
\]
Equivalently,
\[
  \rho_q(z)<1
  \quad\Longleftrightarrow\quad
  A_q(z)(1+U(z))<1.
\]

At the target radius \(z=M_q^{-1}\), this condition holds with a large
margin for every integer \(q\ge2\).  If \(q=s^2\ge4\), then \(M_q=s+1\), and
\[
  A_q(M_q^{-1})(1+U(M_q^{-1}))
  =
  \frac{8(s+2)}{(s^2+2s+2)^2}
  \le
  0.32.
\]
For the fresh-column-dominated cases,
\[
\begin{array}{c|c|c|c}
q & A_q(M_q^{-1}) & U(M_q^{-1}) & \rho_q(M_q^{-1})\\
\hline
2 & 0.172718\ldots & 1.265752\ldots & 0.561834\ldots\\
3 & 0.165820\ldots & 1.101500\ldots & 0.518255\ldots
\end{array}
\]
The maximum over integer \(q\ge2\) occurs at \(q=2\) in this diagnostic.

This is a significant correction to the direction after Round 504.  Even a
very crude scalar trace skeleton, once the two crossing edges are charged and
the no-consecutive-vertical rule is kept, does not obstruct the target
\(M_q\).  The remaining proof task is to lift this one-trace skeleton to the
packet-level transform of Round 503 while preserving the endpoint packet
weights and the annular exterior constraint.
