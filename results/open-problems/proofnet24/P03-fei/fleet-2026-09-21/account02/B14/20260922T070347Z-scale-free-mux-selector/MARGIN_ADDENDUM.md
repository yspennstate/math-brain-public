# B14 margin addendum

The final owner-control reread requires comparison through the normalized gate margin rather than raw defect. A completed other-account result, `account01/B14/20260922T0044Z-balanced-gate-margin-refutation/REPORT.md` (blob `776ade5c2e2017844785b09ab7af50c7eaf54c03`), already refutes the literal base-potential AND/decomposable extremality claim: for the h96 base potential `Gamma_0`, its certified balanced 18-input seed has `c_G >= 0.2681828436921863026...`, versus the quoted AND margin `0.0043974201`. Full FEI remains open. This run therefore works on the compatible lifted Campaign-A candidate `Gamma^dagger=Gamma_0+a^dagger z(1-z)`, `a^dagger=0.268204856`, and does not reopen the refuted base-potential claim.

For any gate let
\[
P_G=I(G;p)/4-p_{out}(1-p_{out})\ge0.
\]
The quadratic lift gives exactly
\[
D_{\Gamma^\dagger}=D_{\Gamma_0}+a^\dagger P_G
=P_G(a^\dagger-c_G^{\Gamma_0})
\]
when `P_G>0`. For the MUX, the exact biased total influence is
\[
I=V_t d+(1-t)V_0+tV_1.
\]
Under the main report's normalization `q_0+q_1=m<=1`, `d<=m` and `V_0+V_1<=4m`, hence `I<=5m` and `P_M<=5m/4`.

The main theorem proves
\[
D_{\Gamma^\dagger}(M)>m/400
\]
throughout
\[
|q_1-q_0|\le m/224,\qquad |t-1/2|\le1/464.
\]
Therefore throughout the whole fixed-width tube
\[
\boxed{c_M^{\Gamma_0}<a^\dagger-1/500=0.266204856.}
\]
If `P_M=0`, the positive lifted defect already makes the point non-dangerous and no division is needed. Thus the new region has a uniform normalized-margin gap of at least `0.002` below the lifted budget, which is the cross-arity quantity requested by the owner message.

**FULL-PROBLEM CHANGE:** none; FEI remains open. **MECHANISM CHANGE:** yes; exact source-scale cancellations turn the previous boundary-dependent selector radius `m/1024` into the fixed radius `1/464`, and the resulting statement is now expressed in the normalized gate-margin currency. The remaining successor obligation is `c_G^{Gamma_0}(p)<=a^dagger` for every Boolean gate and interior bias, or a genuine gate/bias counterexample.
