# B16 handoff — actual post-current parent coefficients, exact physical flag interface

**Full FEI:** OPEN / NOT PROVED.  
**Execution:** WITHOUT_VERIFIED_BRAIN.  
**Main proof:** `REPORT.md`.  
**Fresh compatibility:** `ADDENDUM_ORDERED_FLAG_INTERFACE.md`.  
**Exact checker/output:** `check_actual_current_parent_mask_incidence.py`, `check_actual_current_parent_mask_incidence.out`.

## What is now proved

After the account04 signed compiler has aggregated equal syndromes **before squaring**, write an odd fine mode as `(q,k,r)` with `r=(q-k)/2` doubled clone pairs and signed coefficient `b_R`. The exact pair-curvature double-resolvent assigns every doubled coarse parent `j` the full mass

\[
\mu^{full}_{R,j}=\frac{4}{q^2k}b_R^2
\]

and the central `x,y<=1/2` mass

\[
\mu^{cen}_{R,j}=\frac{\varepsilon_{q,k}}r b_R^2,
\qquad
\varepsilon_{q,k}=2\frac{2^{-q}}q\left(\frac{2^{-k}}k-\frac{2^{-q}}q\right).
\]

Thus the **actual** central parent coefficient is

\[
\mu_j=\sum_{R:j\text{ doubled}}\frac{\varepsilon_{q_R,k_R}}{r_R}b_R^2,
\qquad
\sum_j\mu_j=E_{cen}.
\]

For the ordered-min coarse parent mask `g_j`, a one-subcube defect,

\[
\max_i\sum_j\mu_j\beta_{g_j}(e_i)
\le\sum_j\mu_jJ(g_j)
\le E_{cen}
\le\frac{11}{192}W.
\]

No relation coefficient is absolute-valued to obtain this: all R32 signs and negative credits remain inside the same-syndrome aggregate `b_R`; singleton current is killed exactly; terminal and R16/moment ledgers are not spent.

## Fresh account03 flag identification

For fixed coordinate order, a parent with pivot `i` has codimension `c_i=m_i+1`, where `m_i` is the number of later coordinates. Account03's exact ordered-flag law is uniform on later-coordinate subsets,

\[
\nu_i(w)=2^{-m_i}=2^{1-c_i}.
\]

For every actual nonzero q-flip `w`,

\[
\beta_{g_{i,w}}(e_\ell)=\nu_i(w)
\]

on the pivot-plus-later defining coordinates and is zero elsewhere, hence

\[
J(g_{i,w})=c_i\nu_i(w)\le1.
\]

So the mask bank is literally a coefficient-weighted average over the same physical ordered flag used in account03's oriented payment.

## Exact next obligation

Do **not** return to arbitrary positive q-flip support incidence. The remaining source-exact theorem is:

> Push the genuine signed-current curvature measure through the physical q-flip/Radon compiler so that its per-parent marginal is the proved `mu_{i,w}` (or is dominated without reuse), and compare the resulting local source square to account03's oriented flag payment. Then pay the Ward/R16 bank once by `J(f)` while leaving terminal/resolvent-boundary credits untouched.

If this representation fails, produce a genuine Boolean counterexample and identify the missing signed correction term. B18's mask-resolvent theorem may be used only after this positive physical pushforward is actually derived; its existence must not be assumed.

Checker SHA-256: `3f63d644eae7088baed6491441a3030d7a5e062d39bd10c3da497c92479fc733`.  
Output SHA-256: `d3cd99f42a214ec4ac86e575844c6dac3081d927b697e72c366d675969317bdb`.
