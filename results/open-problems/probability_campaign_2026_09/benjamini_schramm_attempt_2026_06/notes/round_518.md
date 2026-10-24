# Round 518 excess reservoir replaces the geometric bubble sum

Round 517 shows that unconstrained span-only reversal sums are too large.
The missing geometric fact is that reversal bubbles below a record height do
not have an infinite reservoir: the annular exterior constraint and
root-column self-avoidance give a finite reserve.

Work in the one-sided high-root regime.  At tree depth \(r\), outside the
ball of radius \(u\), a root-column height \(h\) has annular excess
\[
  e_r(h)=r+h-u.
\]
If a trace is at a record height \(R\), then a downward reversal of depth
\(d\) is legal only if
\[
  d\le e_r(R).
\]
Moreover, portal heights are distinct.  Thus all reversal bubbles below the
same record level draw from the finite interval
\[
  \{R-e_r(R),\ldots,R-1\}.
\]
In a compressed trace, the primitive bubbles extracted by the record-envelope
algorithm have disjoint first new lower levels.  Therefore a crude but
useful replacement for the unconstrained geometric sum is
\[
  \frac{1}{1-D}
  \quad\leadsto\quad
  (1+D)^{e_r(R)}.
\]
This is weaker than a precise hard-core gas on the lower levels, but it uses
the finite excess reservoir.

The calibrated excess multiplier has enough room to absorb this factor.  At
\(z=M_q^{-1}\), \(C=2\), and \(D=D_q(z)\) from Round 511,
\[
\begin{array}{c|c|c|c}
q & w_*(z) & D_q(z) & w_*(z)(1+D_q(z))\\
\hline
2 & 0.673929\ldots & 0.248450\ldots & 0.841367\ldots\\
3 & 0.630744\ldots & 0.210147\ldots & 0.763293\ldots\\
4 & 0.6 & 0.1856 & 0.71136\\
5 & 0.564161\ldots & 0.140046\ldots & 0.643170\ldots\\
6 & 0.534847\ldots & 0.110034\ldots & 0.593698\ldots
\end{array}
\]
All values are \(<1\).  Thus the same excess weight that calibrates the
fresh-column excursion also has slack to pay for a reservoir of reversal
bubbles.

This suggests replacing the span-only packet norm by a record-reserve norm.
For a trace family \(\mathfrak W\), let
\[
  R_*(\mathfrak W)
\]
be the sum, over record levels of the root-column traces, of the available
downward excess reserve at that record.  Add the factor
\[
  (1+D_q(z))^{R_*(\mathfrak W)}
\]
to the trace majorant and charge it against the existing \(w_*^{E}\)-type
excess weight.  Since \(w_*(1+D_q)<1\), record levels with large reserve are
still summable.

The next rigorous lemma should therefore be:

> In a valid compressed packet trace, the record-envelope bubbles below each
> record height can be assigned injectively to distinct lower excess levels
> in that record's annular reserve.

If true, the low-branching nonmonotone obstruction is no longer an infinite
neutral-loop problem; it becomes a finite hard-core gas controlled by the
annular excess multiplier.
