# Round 034 log

## Goal

After correcting the depth-two block regeneration in Round 033, test whether
either valid block conventions or larger one-step finite-subset retention can
still improve the \(T_3\square\mathbb Z\) percolation-side certificate.

## Valid depth-two block scaling

The valid factorized and regenerative block scans were probed at larger width.
For type width \(7\), margin \(2\):

\[
\begin{array}{c|cc}
p & \text{factorized ratio} & \text{regenerative ratio}\\
\hline
0.296 & 0.955948146115 & 0.954221772699\\
0.302 & 1.008236280010 & 1.006719233170\\
0.305 & 1.034961006190 & 1.033571834260
\end{array}
\]

Thus the valid depth-two block thresholds at this width are near \(0.301\),
well above the current decorated-strip certificate \(0.29545\).

## Larger one-step finite-subset process

The one-step finite-subset process from Round 031 remains the strongest
non-oriented lower process tested.  Larger width probes give:

\[
\begin{array}{c|c|c}
W & p & \rho_{\rm lower}\\
\hline
9 & 0.29545 & 0.997311302109\\
9 & 0.29580 & 0.998952678348\\
9 & 0.29600 & 0.999890906372\\
9 & 0.29605 & 1.000125497220\\
10 & 0.29545 & 0.997581067940
\end{array}
\]

Width \(9\) brackets its threshold very close to \(0.2960\), and width \(10\)
still fails at \(0.29545\).  The improvement from \(W=8\) to \(W=10\) is too
small to suggest that this retention rule will beat the decorated-strip bound
soon.

## Consequence

The current best rigorous \(p_c\)-side certificate remains
\[
  p_c(T_3\square\mathbb Z)<5909/20000=0.29545.
\]
The finite-subset lower process is close but still weaker, and the valid
depth-two block variants are weaker still.  Further progress likely needs a
new retention rule that keeps reusable boundary vertical information without
double-exposing it, or a sharper operator-side estimate.
