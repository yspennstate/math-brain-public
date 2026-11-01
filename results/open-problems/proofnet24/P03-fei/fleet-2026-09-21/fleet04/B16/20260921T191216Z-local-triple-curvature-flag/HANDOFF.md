# B16 handoff — local triple-curvature / ordered-parent flag bridge

**Full unrestricted FEI remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Main proof:** `REPORT.md`.  
**Checker:** `check_local_triple_curvature_flag.py`; archived output `verification.txt`.

## New exact compiler identity

Let `Psi_s` be the retained `C_0-D_d` Borel potential and `g_{j,0},g_{j,1}` the two disjoint slice-clones of coarse ordered-min parent `j`. If `F_s(S)=Psi_s(g_S)` and `F_s^odd=(I-T_f)F_s/2`, then

\[
\boxed{
D_jF_s^{odd}(S)=\frac12\Delta_{g_{j,0}}\Delta_{g_{j,1}}\Delta_f\Psi_s(g_S).
}
\]

Thus the actual doubled-parent current is a **three-phase mixed difference**: two clone phases plus the actual Boolean phase. No unsigned support replacement is needed.

## New local distance-four cancellation

For one dual word, disjoint clone halves give

\[
\Delta_{g_{j,0}}\Delta_{g_{j,1}}\cos(s(A+B+C))
=-4\cos(sA)\sin(sB)\sin(sC).
\]

After splitting by `f=+/-`, the apparent quadratic term of the triple difference is proportional to

\[
B_+C_-+B_-C_+.
\]

Each product pairs disjoint truth-table cells. Because every retained relation code is a subcode of `RM(1,n)^perp`, which has no weight-two word, both dual-code averages vanish exactly. Hence every genuine current parent begins at four-point order **after the signed retained average**.

## Dimension-free ordered-parent square bank

In the minimizing-character gauge, let `u_j^+`, `u_j^-` be the sign masses of `f` inside the genuine coarse parent cell `C_j`, density `delta_j`. Keeping the terminal subtraction signed yields the pointwise bound

\[
|\Delta_{g_{j,0}}\Delta_{g_{j,1}}\Delta_f\Psi_s|
\le16(1-\rho_d)s^4
\left[\frac43\sqrt{u_j^+u_j^-}+p_+p_-\delta_j\right].
\]

For the complete ordered-min parent family,

\[
\sum_j u_j^+u_j^-\le J(f)/4,
\qquad
\sum_j\delta_j^2<1/2,
\qquad
(p_+p_-)^2\sum_j\delta_j^2\le J(f)/32.
\]

Therefore

\[
\boxed{
\sum_j\|D_jF_s^{odd}\|_2^2
\le64\left(\frac23+\frac1{4\sqrt2}\right)^2
(1-\rho_d)^2s^8J(f).
}
\]

Using the exact central mode ratio `epsilon_{q,k}/(16r)<=11/4608`,

\[
\boxed{
E_{cen}(s)
\le\frac{11}{72}
\left(\frac23+\frac1{4\sqrt2}\right)^2
(1-\rho_d)^2s^8J(f).
}
\]

The coefficient is `0.108685607684...`. This is not numerically better than the previous global small-`s` phase-switch bound; its gain is **physical localization to the actual ordered parent cells with orientation preserved**.

## Exact next target

Do not return to unsigned support disagreement: genuine parity refutes that source interface. Instead insert the **random ordered-flag Hardy kernel** into the exact local sine/cosine triple difference before absolute values, and try to PSD-contract the large-`s` remainder into fleet03/B18's signed derivative Hardy bank

\[
E_{Pi,W}\kappa_i(W)^2
=4\sum_{U,V\ne0}b_i(U)b_i(V)
\left[1-\frac1{|U|+1}-\frac1{|V|+1}+\frac1{|U\triangle V|+1}\right].
\]

If the contraction fails, preserve an authentic R32 packet showing which component is orthogonal to the signed derivative rows. Leave R16/moment refunds, negative entropy credits, dual multiplicity, resolvent boundary and terminal band untouched.

Checker SHA-256: `1633f6240d609886db6c5183db105abd667fba940eadcda396b524cf3c50e097`.  
Verification SHA-256: `17c8ab18f814f9ec47ce7e7eadd443043e50608523c7e48204d6b69c56b76608`.
