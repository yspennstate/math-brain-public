# Round 277

Round 277 pushes the residual-width successor cutoff through the existing
one-step chain-amplification machinery.

The new one-step corollary is

```tex
\begin{corollary}[Residual-width one-step amplification]
\label{cor:residual-width-one-step-staircase-chain-amplification}
```

Starting from the residual-width cutoff
\[
  B^{\rm res}_{K,\ell,p}
  =
  \left\lceil
    \frac{16K R_{\ell,p}}{\theta_{\lambda,\sigma,\beta}L_H}
  \right\rceil+1,
\]
the bounded-gap chain-pair profile has parameters
\((2K,L,\ell,B^{\rm res}_{K,\ell,p})\).  Applying the fixed-gap pigeonhole
then changes the depth parameter to
\[
  K^{\rm res}_{K,\ell,p}=2K B^{\rm res}_{K,\ell,p}.
\]
Finally, the fixed-gap chain-pair split gives:

- gaps \(1\le h\le\ell\) glue into longer chains of length \(\ell+h\);
- gaps \(h\ge\ell+1\) become confined staircase-chain bridges.

This is the residual-width analogue of the old one-step amplification, but
with \(B_{\lambda,\sigma,\beta,K}\) replaced by the smaller p-dependent
residual cutoff.

The near-top version is

```tex
\begin{corollary}[Near-top one-step amplification has bounded cost]
\label{cor:near-top-one-step-amplification-has-bounded-cost}
```

If \(R_{\ell,p}\le C L_H/K\), then the whole one-step reduction uses the
p-independent cutoff
\[
  B_C=
  \left\lceil
    \frac{16C}{\theta_{\lambda,\sigma,\beta}}
  \right\rceil+1
\]
and the p-independent depth cost \(K_C=2K B_C\).  Thus near slab exhaustion
the chain step is genuinely bounded-cost.

This still does not solve the main problem.  The unresolved mechanism is how
to move from fixed initial chain lengths to the near-top residual-width
regime without paying the original rapidly growing \(K\)-loss.

No external literature refresh was performed in this round; the Round 276
source check remains the latest external status.
