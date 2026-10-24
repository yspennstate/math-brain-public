# account01/B04 QFORM checkpoint — six-row complement-Hellinger volume compiler

Run `20260923T104329Z-account01-B04-QFORM-auto11`.

Fresh target/control: QFORM-DENSITY-3EIG-20260922, OWNER CONTROL revision `2026-09-22.15`; full conjecture remains open. Corrections retained: no law-uniform pointwise quadratic-phase decay, no independence after spectral rotation, no arbitrary-joint rank-three coarea, no universal good single physical minor/cross cut.

## First substantive calculation

For an original-coordinate cross block `M` and a six-row set `R`, define for each row triple `S subset R`

`a_S = sum_{|T|=3} det(M[S,T])^2 = det(M[S,:] M[S,:]^T)`

and write `Sbar=R\S`. Define

`C_R(M)=sum_{|S|=3} sqrt(a_S a_Sbar)`.

If `C_R(M)>0`, set the row-triple law

`mu(S)=sqrt(a_S a_Sbar)/C_R(M)`.

Then `mu(S)=mu(Sbar)`, so every physical row of `R` has inclusion marginal exactly `1/2`; rows outside `R` have marginal zero. Given `S`, choose a column triple with probability `det(M[S,T])^2/a_S`. The resulting full minor weight is therefore admissible for the q=1 sharp weighted-three-volume theorem.

The exact determinant/entropy currency is

`G(w)=C_R(M)`.

Indeed conditional column entropy plus the conditional mean of `log det^2` equals `log a_S`, while complement symmetry gives

`H(mu)+sum_S mu(S)log a_S = log C_R(M)`.

Equivalently, if `p_R(S)=a_S/Z_R` with `Z_R=sum_S a_S`, then

`C_R/Z_R = sum_S sqrt(p_R(S)p_R(Sbar))`

is the Hellinger/Bhattacharyya affinity of the canonical row-volume law with its complement image, and

`D_KL(mu||p_R)=log(Z_R/C_R)`.

Thus the sharp product-Fourier theorem at q=1 gives the candidate supporting bound

`||p_Q||_inf <= 3e C_R(M)^(-1/6)`

with a continuous density vanishing at infinity, in the full theorem's stated scope with arbitrary same-bank measurable phases and outside conditioning.

This quantitatively refines account02/B04's completed `QFORM-THIRDVOLUME-Q1-BASEPACKING-v1`: `C_R>0` exactly means that `R` contains two disjoint rank-three row bases. The remaining work in this run is to write the proof carefully, verify an explicit genuinely rotated indefinite target matrix, apply the partner result at an actual inequality, and state the unresolved global routing step.
