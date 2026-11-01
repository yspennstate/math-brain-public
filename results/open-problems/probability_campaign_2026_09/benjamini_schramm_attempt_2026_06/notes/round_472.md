# Round 472 finite-fiber correction: ports and threshold comparison

Round 472 records two corrections to the finite-fiber roadmap.

First, the boundary ports of a component in \(T_d\square F\) are not only
the descendant-side vertices with
\[
  d_T(a,w)+d_F(f_0,f)=R-1.
\]
There are also parent-side ports
\[
  (\operatorname{par}(a),f),\qquad d_F(f_0,f)=R,
\]
adjacent to the top layer \((a,f)\) of the decorated cone.  In the exact
\(K_2\) calibration, this parent-side port is precisely
\((\operatorname{par}(t),1)\).  Omitting these ports would erase one side of
the two-port transfer.

Second, the natural finite-fiber inequality is not uniformly
\[
  \rho_F(d-1)<d-1.
\]
That estimate is a strong sufficient condition because \(T_d\square F\)
contains \(T_d\), but high-entropy finite fibers may increase both the
annular transfer exponent and the inverse percolation threshold.  The right
comparison for the finite-state transfer is therefore
\[
  \rho_F(d-1)<1/\pc(T_d\square F).
\]

The \(K_2\) computation remains a low-width calibration where the stronger
bound holds:
\[
  \rho_{K_2}(d-1)=\sqrt{d-1}<d-1\le 1/\pc(T_d\square K_2).
\]
For larger finite fibers, the transfer system from Round 471 should be
paired with a finite-width percolation-threshold comparison, not only with
the embedded-tree lower bound on \(1/\pc\).
