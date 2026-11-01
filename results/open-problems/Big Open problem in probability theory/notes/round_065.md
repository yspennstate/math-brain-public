# Round 065 log

## Goal

Clarify exactly what the existing nonbacktracking polynomial bound gives if
one uses only the adjacency spectral radius.

## Criterion

Let \(G\) be \(D\)-regular, let \(\rho_A=\|A\|_{2\to2}\), and let
\[
  \beta(D,\rho_A)
  =
  \begin{cases}
    \sqrt{D-1}, & \rho_A\le2\sqrt{D-1},\\
    \dfrac{\rho_A+\sqrt{\rho_A^2-4(D-1)}}2, & \rho_A>2\sqrt{D-1}.
  \end{cases}
\]
Added Corollary `adjacency-spectrum-square`: if
\[
  p_c(G)\beta(D,\rho_A)^2<1,
\]
then \(p_c(G)<p_{2\to2}(G)\).

The proof uses the nonbacktracking count-kernel estimate
\[
  \|N_m\|_{2\to2}\le C_\theta\theta^m
\]
with \(\theta>\beta(D,\rho_A)\).  This gives both
\[
  \alpha_c^{\max}(G)\le p_c(G)\theta
  \qquad\text{and}\qquad
  \rho_{\mathrm{sph},2}(G)\le\theta,
\]
then applies the critical shell exponent criterion.

## Limitation

For the \(D\)-regular tree, the criterion gives
\[
  p_c(T_D)\beta(D,2\sqrt{D-1})^2=1.
\]
So adjacency-spectrum control alone reaches the critical boundary in the
model case.  This reinforces that the main route must keep bridge-resolved
information rather than collapsing everything to the global adjacency norm.
