# Round 481 high-root bubble transfer and the missing exit cost

Round 481 isolates a useful high-root transfer, but also records why it does
not by itself give an annular lower bound.

After paying a finite entrance cost to reach \((o,u)\), concatenate many
``bubbles'' from \((o,H)\) to \((o,H+s)\), with \(H\ge u\).  A bubble is:

1. choose a tree branch and move outward from \(o\) to depth \(r\) at fixed
   line height \(H\);
2. take one upward line step at the leaf;
3. return inward to \(o\), interleaving the remaining \(s-1\) upward line
   steps with the \(r\) inward tree steps.

The first upward step ensures that the inward traversal does not revisit the
outward vertices, since it occurs at line height \(>H\).  Consecutive bubbles
use increasing root heights; choosing the first tree edge different from the
previous bubble avoids revisiting vertices at the shared root height.  This
costs only a bounded factor.  The exterior condition is automatic because
all bubble vertices have line height at least \(u\).

For one bubble, the number of choices is at least
\[
  c\,q^r\binom{r+s-1}{r},
\]
and the length is \(2r+s\).  Put \(s=ar\).  The exponential rate per step is
\[
  \exp\left\{
    \frac{\log q+(1+a)H(1/(1+a))}{2+a}
  \right\}.
\]
Optimizing in \(a>0\), the derivative condition is
\[
  \frac{1+a}{a^2}=q.
\]
At this optimum the rate is
\[
  \lambda_q=\frac{1+\sqrt{1+4q}}{2},
\]
equivalently \(\lambda_q^2-\lambda_q-q=0\).

This is a valid transfer rate from \((o,H)\) to \((o,H+s)\) at high line
height.  However, it is not yet a valid lower bound on
\(\Gamma_{\rm ann}(T_d\square\mathbb Z)\).  After many bubbles the path ends
at a root vertex with line height far above the annular boundary.  Returning
to an outward neighbor of \(S_{u-1}((o,0))\) costs a comparable number of
downward line steps, so the exit cost cannot be discarded.

Thus the claimed annular lower bound
\[
  \Gamma_{\rm ann}(T_d\square\mathbb Z)\ge \lambda_q
\]
is not justified by the bubble transfer alone.  The correct use of this
component is the variational annular construction recorded in Round 482,
where the bubble phase and the final descent back to the boundary are counted
together.
