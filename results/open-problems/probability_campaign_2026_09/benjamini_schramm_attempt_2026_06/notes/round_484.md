# Round 484 generating function for the corrected bubble variational problem

Round 484 optimizes the corrected repeated-bubble family from Round 482.

Use \(t\) to mark half-length \(R+S+T\).  The corrected family has weights
\[
  q^R\binom{R+S}{R}\,q^{T/2}\binom{S+2T}{T}
\]
and length \(2(R+S+T)\).  Hence its half-length generating function is
\[
  F_q(t)=
  \sum_{R,S,T\ge0}
  q^R\binom{R+S}{R}
  q^{T/2}\binom{S+2T}{T}
  t^{R+S+T}.
\]
Allowing \(T=0\) is an algebraic shorthand for the \(T=o(R)\) exit regime;
using a fixed fresh terminal column, say \(T=1\), changes only polynomial
factors and gives the same exponential radius.
Summing first over \(R\) gives
\[
  \sum_{R\ge0}\binom{R+S}{R}(qt)^R=(1-qt)^{-S-1}.
\]
For the \(T\)-sum, use
\[
  \sum_{T\ge0}\binom{S+2T}{T}x^T
  =
  \frac{A(x)^S}{\sqrt{1-4x}},
  \qquad
  A(x)=\frac{1-\sqrt{1-4x}}{2x}.
\]
With \(x=\sqrt q\,t\), this gives
\[
  F_q(t)=
  \frac{1}{(1-qt)\sqrt{1-4\sqrt q\,t}}
  \cdot
  \frac{1}{
    1-\dfrac{tA(\sqrt q\,t)}{1-qt}
  }.
\]

Since all coefficients are nonnegative, the optimized exponential rate of
the corrected repeated-bubble family is
\[
  \Lambda_q=t_q^{-1/2},
\]
where \(t_q\) is the smallest positive singularity of \(F_q\).  Equivalently,
\[
  t_q=
  \min\left\{
    \frac1q,\,
    \frac1{4\sqrt q},\,
    t_{\rm int}
  \right\},
\]
where \(t_{\rm int}\) is included only if it lies before the first two
singularities and solves
\[
  \frac{tA(\sqrt q\,t)}{1-qt}=1.
\]

Thus the corrected repeated-bubble construction gives the rigorous lower
bound
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)\ge \Lambda_{d-1}.
\]
It contains the symmetric portal term \(2q^{1/4}\) as the singularity
\(t=1/(4\sqrt q)\), and it contains the paid-exit subfamily
\(\sqrt{q+1}\) from Round 483 as a non-sharp explicit subcase.  For large
\(q\), the interior singularity gives
\[
  \Lambda_q=\sqrt q+o(\sqrt q),
\]
still below the global product-shuffle scale \(\sqrt q+1\).
