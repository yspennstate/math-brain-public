# fleet04/B15 handoff — Gibbs activity credit is the exact decomposable transfer

Use newest fleet02/B15 `20260922T0704Z-gibbs-kl-prime-tube` as the source definition.  Its unpaid remainder is

\[
R_\Gamma(f)=\log_2\frac{Z-1}{x_q}-D_{KL,2}(w^+\|\nu^+),\qquad D_\Gamma(f)=-V_qR_\Gamma(f).
\]

For any disjoint composition `F=G(f_1,...,f_m)`, let `beta_i=Pr_{w_G}(i active)` and `v_i=V_{q_i}`.  If `eta` is the block-activity law induced by the physical Gibbs reference, then

\[
D(w_F\|\nu_F)=D(w_G\|\eta)+\sum_i\beta_iD(w_i^+\|\nu_i^+).
\]

The induced activity reference is an exact exponential tilt of the canonical outer Gibbs law by the child partition demands.  This recovers, with every KL credit retained,

\[
D_\Gamma(F)=D_\Gamma(G;q)+\sum_i\frac{\beta_i}{v_i}D_\Gamma(f_i).
\]

For the tensor/product specialization `F=prod_j f_j`, conditioning on parent nonemptiness creates a genuine block-activity KL:

\[
v_FK_F=\sum_jv_jK_j+v_FD(P_A\|Q_A),
\]

and the exact unpaid-remainder transfer is

\[
\boxed{
v_FR_\Gamma(F)=\sum_jv_jR_\Gamma(f_j)-\left[\sum_j\Gamma(q_j)-\Gamma(q_F)\right].
}
\]

For identical balanced tensor powers,

\[
K_{f^{\otimes m}}=mK_f+\log_2\frac{Z^m-1}{(Z-1)^m},
\]

so dropping the activity KL loses `Theta(m)` genuine relative entropy.  This is a source-exact no-go for credit-free conditional-KL tensor interpolation.

Full FEI remains OPEN.  The remaining arithmetic/Shannon debt is on composition-prime outer activity laws; fleet02/B15 already certifies the current five-input prime candidate in the explicit `4.4e-6` center tube.
