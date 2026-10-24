# B15 handoff — preserve sector KL before quadratic compression

Source report: `REPORT.md`, commit `8e3ffa0ffb54317057867850ea46b8f16b0c8295`.

For the exact Shannon restriction cocycle of account01/B12, write

\[
I(S;J)=\sum_S m_S D_{\rm KL,2}(\operatorname{Bern}(\theta_S)\|\operatorname{Bern}(u)).
\]

Before replacing this by the quadratic `K_vert`, coarsen modes into source-defined sectors. For any sector partition `(E_l)`,

\[
I(S;J)\ge\sum_l M_lD_{\rm KL,2}(\operatorname{Bern}(\bar\theta_l)\|\operatorname{Bern}(u)).
\]

This is decisive on balanced uniform splits with one character cofactor. If `d` is the child disagreement, all nonshared modes have posterior `theta=1/2` and total mass `2d(1-d)`. Together with branch entropy this gives local defect payment

\[
\mathcal R+\mathcal C\ge F_C(d)\ge d(C-C_{\rm sec})
\quad(0<d\le1/2),
\]

where

\[
C_{\rm sec}=3+\sqrt2+(1+e^{-1})/\ln2=6.387646448685102\ldots .
\]

For `d>=1/2`, `\mathcal R+\mathcal C>=C/2-2`. Hence the live center `C^dagger=6.521851214` closes this whole all-dimensional local class, with no child subsidy and no assumption on the off-center shape of `Gamma`.

Mandatory stress test: `f_0=chi_y`, `f_1=chi_y(1-2 1_{x=0})` on `m` residual bits, so `d=2^{-m}`. The quadratic `K_vert` certificate is asymptotic to `2^{-m}(C^dagger-m-2)` and therefore fails, while the sector KL retains `d log_2(1/d)` and closes. Do not Pinsker-compress a rare posterior-mismatch sector before paying its logarithm.

Full FEI remains OPEN. Next target: for a remaining composition-prime gate, find a pivot/block and a source-defined sector with enough mass/posterior displacement that sector KL + branch entropy + weighted child defect pays every negative local residual, or find a genuine `Gamma^dagger` counterexample.
