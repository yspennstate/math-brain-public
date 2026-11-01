# Round 482 corrected repeated-bubble variational target

Round 482 corrects the repeated-bubble construction by including the cost of
returning from high root height to the fixed annular boundary.

Start at the outward neighbor \((o,u)\) of the boundary vertex \((o,u-1)\).
Run a bubble phase with total branch depth \(R\) and total upward height gain
\(S\).  A lower-bound count for this phase is
\[
  q^R\binom{R+S}{R},
\]
with length \(2R+S\), ending at \((o,u+S)\).  This aggregates the bubble
transfer from Round 481; polynomial ballot factors are ignored in the
exponential scale.

To end at the annular boundary, choose a terminal tree depth \(T\le u\) and
descend to a vertex \((w,u-T)\) of radius \(u\), where \(w\) lies in a
terminal branch.  The exit phase uses
\[
  T\text{ outward tree steps},\qquad S+T\text{ downward line steps}.
\]
The exterior condition is the ballot constraint
\[
  D_{\rm prefix}-O_{\rm prefix}\le S,
\]
which again costs only polynomial factors at the exponential scale.  The exit
interleavings contribute
\[
  \binom{S+2T}{T},
\]
and the terminal boundary set contributes the annular normalization factor
\[
  \frac{q^T}{\sqrt{q^T}}=q^{T/2}
\]
when \(V\) is chosen as the set of terminal boundary vertices at tree depth
\(T\).

Hence this corrected repeated-bubble family gives the variational lower
bound
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)
  \ge
  \exp\Bigg[
    \sup_{R,S,T\ge0}
    \frac{
      R\log q
      +(R+S)H\!\left(\frac{R}{R+S}\right)
      +\frac{T}{2}\log q
      +(S+2T)H\!\left(\frac{T}{S+2T}\right)
    }{
      2(R+S+T)
    }
  \Bigg],
\]
with homogeneous variables and \(q=d-1\).

This formula is the corrected object to optimize.  It may improve on the
symmetric portal bound \(2q^{1/4}\), but the high-root bubble rate
\[
  \frac{1+\sqrt{1+4q}}{2}
\]
cannot be imported directly without paying the final descent cost.
