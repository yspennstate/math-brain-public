# Round 288

Round 288 refines the large-window branch after counting saturation.

The new definition is

```tex
\begin{definition}[Few-start chain profiles]
\label{def:few-start-locally-short-staircase-chain-profiles}
```

It records a finite-start version of the locally short staircase-chain
profile: instead of requiring more than
\[
  \frac{\theta_{\lambda,\sigma,\beta}}{4K}L_H
\]
admissible chain starts, the profile requires at least a fixed integer
\(q\) admissible starts.

The new corollary is

```tex
\begin{corollary}[Large-window children reduce to few-start chains]
\label{cor:large-window-children-reduce-to-few-start-chains}
```

In the last valid large-window branch, the child parameter satisfies
\[
  K_{r+1}\ge \frac{\theta_{\lambda,\sigma,\beta}}{16}L_H.
\]
Thus the ordinary chain start threshold at each child is at most \(4\).  With
\[
  q_{r,p}
  =
  \left\lfloor
    \frac{\theta_{\lambda,\sigma,\beta}}{4K_{r+1}}L_H
  \right\rfloor+1,
\]
one has \(1\le q_{r,p}\le5\), and every large-window child chain profile is
bounded by the corresponding few-start profile.  Consequently the parent is
bounded by at most \(5W_{\beta,p}\) few-start child profiles, preserving the
same logarithmic exponent implication.

The remaining large-window target is now sharper: prove uniform exponent
bounds for bounded finite-start chain profiles, with \(1\le q\le5\), across
the subexponential child family.

No external literature refresh was performed in this round; the Round 285
source check remains the latest external status.
