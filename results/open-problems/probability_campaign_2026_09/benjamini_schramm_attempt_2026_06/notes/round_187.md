# Round 187

Round 187 audits the logarithmic scale hierarchy after the anchor-count
correction of Round 186.

There are now three distinct capped-branch thresholds, each attached to a
different object:

\[
\begin{array}{c|c|c}
\text{object} & \text{capped exponent} & \text{optimized scale range}\\
\hline
\Theta_p(I_{j,p}^{\rm gate})
&
1-6\theta-14\theta\alpha_\omega-4U\alpha_\omega
&
U<1/(4\alpha_\omega)
\\
\text{operator/support profile}
&
2-6\theta-15\theta\alpha_\omega-6U\alpha_\omega
&
U<1/(3\alpha_\omega)
\\
\text{anchor count}
&
1-2\theta-5\theta\alpha_\omega-2U\alpha_\omega
&
U<1/(2\alpha_\omega).
\end{array}
\]

The first two thresholds are diagnostics for two-replica or operator mass.  The
third is the strongest pure scale amplification currently available from the
volume-counting inputs.  Thus the old \(1/(3\alpha_\omega)\) wording should be
read as a support-profile/operator barrier, not as the best available bound on
how far the expanded gate-annulus data can be pushed.

This bookkeeping matters downstream: endpoint-anchor and buffered-tube scale
collapses use count-based contradictions, while normalized profile criteria
still need a sharper estimate on the support set \(Y\) or a stronger extracted
mass lower bound.
