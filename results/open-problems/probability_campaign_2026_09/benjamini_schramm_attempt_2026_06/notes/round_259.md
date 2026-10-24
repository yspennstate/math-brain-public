# Round 259

Round 259 splits the locally short staircase residual by successor gaps.

If a slab contains linearly many locally short staircase lower levels, then
the usual bounded-gap pigeonhole gives linearly many successor pairs with
gap at most
\[
  B_{\lambda,\sigma,\beta,K}
  =
  \left\lceil
    \frac{16K\beta}{\theta_{\lambda,\sigma,\beta}}
  \right\rceil+1.
\]
Pigeonholing again over the finite set of possible gaps gives a finite
fixed-gap staircase-pair family.

In the finite ladder, with
\[
  B_i=\left\lceil
    \frac{2048M_i\beta_i}{\theta_{\lambda_i,\sigma_i,\beta_i}}
  \right\rceil+1,
\]
the new gap cutoff is
\[
  C_i
  =
  \left\lceil
    \frac{4096M_iB_i\beta_i}{\theta_{\lambda_i,\sigma_i,\beta_i}}
  \right\rceil+1.
\]
The live residual is now
\[
  P^{\rm pre,stair,loc,gap,sh}_{i,j,h}\quad(1\le h\le C_i),
  \qquad
  P^{\rm pre,br,sh}_{i,j,h}\quad(2\le h\le B_i),
\]
plus the previous terminal far tail, long-run, enlarged spread-return,
ordinary exact-level return, finite-defect, and near-tail terms.

No external open-status search was refreshed in this round.
