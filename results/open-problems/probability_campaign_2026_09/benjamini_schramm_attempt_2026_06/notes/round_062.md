# Round 062 log

## Goal

Clarify how much of the bridge criterion can be controlled by a global
nonbacktracking \(L^2\) estimate, and identify the loss from doing so.

## Result

Added Proposition `sphere-from-nb-growth` to the manuscript.  For an infinite
connected \(D\)-regular graph,
\[
  \rho_{\mathrm{sph},2}(G)
  \le (D-1)\sigma_{\mathrm{NB},2}(G),
\]
where \(\sigma_{\mathrm{NB},2}\) is the \(L^2\) spectral growth rate of the
nonbacktracking transition operator on directed edges.

The proof writes the length-\(n\) nonbacktracking count kernel as
\[
  N_n=B\bigl((D-1)\mathcal P_{\mathrm{NB}}\bigr)^{n-1}C
\]
with \(\|B\|,\|C\|\le\sqrt D\), and uses
\[
  S_n^G(x,y)\le N_n(x,y)
\]
because every distance-\(n\) pair is joined by at least one nonbacktracking
geodesic.

## Consequence

The directed-edge spectral bridge criterion follows from the stronger square
condition
\[
  p_c(G)\bigl((D-1)\sigma_{\mathrm{NB},2}(G)\bigr)^2<1.
\]
This is a guardrail, not the main proof route.  For regular trees it is at the
critical boundary, while the bridge-resolved certificate keeps a strict margin.
