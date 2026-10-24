# Round 078 log

## Goal

Audit the remaining low-branching finite-cycle stress test
\[
  T_3\square C_m,\qquad m\ge3.
\]
This family is not a new open case: since \(T_3\square C_m\) is quasi-isometric
to a regular tree, it is Gromov hyperbolic and is covered by Hutchcroft's
hyperbolic theorem.  The question here is narrower: can the elementary
finite-fibre branching plus finite-length SAW certificate route close it?

## Branching side

The scalar cycle-cluster criterion for \(d=3\) requires
\[
  2\varphi_{C_m}(p)>1.
\]
Its threshold is too high, tending to \(p\approx0.3276217564\), so it asks the
operator side to prove a root below about \(3.0523\).

Added `scripts/cycle_subset_branching_scan.py`, a floating-point diagnostic for
the exact reached-subset branching process on \(C_m\).  For a parent reached
subset \(S\), the child fibre receives independent horizontal seeds from \(S\),
then expands through vertical percolation on \(C_m\).  Multiplication by the
two forward tree children gives the mean matrix.  The resulting threshold
diagnostics are:
\[
\begin{array}{c|c|c}
m & p_{\rm subset} & 1/p_{\rm subset}\\
\hline
3&0.317132230751&3.153258808\\
4&0.305160759915&3.276961298\\
5&0.300234054466&3.330734756\\
6&0.298002864821&3.355672438\\
7&0.296940367281&3.367679542\\
8&0.296420873959&3.373581579
\end{array}
\]
These are not rational certificates yet, but they are reproducible and show
that retaining arbitrary finite cycle subsets substantially improves the
percolation-side bound.

## Operator side

Using the existing quotient SAW enumeration with \(T_3\) sphere norms, the
length-\(11\) operator roots are:
\[
\begin{array}{c|c}
m & \|C_{11}\|_{2\to2}^{1/11}\\
\hline
3&3.510460092\\
4&3.630232944\\
5&3.674388421\\
6&3.691848908\\
7&3.697288328\\
8&3.699063401
\end{array}
\]
For \(C_3\), a length-\(13\) exact enumeration gives
\[
  \|C_{13}\|_{2\to2}^{1/13}=3.462720635,
\]
still far above the subset-branching target \(3.153258808\).  The generic
length-\(15\) \(C_3\) enumeration timed out in the current implementation.

## Conclusion

The \(T_3\square C_m\) finite-SAW certificate route is not currently promising:
the percolation-side thresholds are much better than the scalar cluster bound
but still do not meet the available finite-length operator roots.  Closing this
family by elementary methods would need a new \(p_{2\to2}\)-side argument, not
just exact rationalization of the current finite-SAW data.

For the manuscript's mathematical coverage, the correct way to include
\(T_3\square C_m\) is to cite the known hyperbolic-graph theorem.  For the
project's search program, this diagnostic says not to spend the next round
trying to certify the current SAW inequalities for finite cycles.
