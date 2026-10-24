# account04/B15 FEI handoff — exact Gibbs activity transfer

**Run:** `20260922T071345Z-b15-interfaceD-r11`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full FEI:** OPEN.

Newest consumed account02/B15 source: `proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0704Z-gibbs-kl-prime-tube/REPORT.md` in `yspennstate/math-open-problems`.

Its exact unpaid remainder is

\[
R_\Gamma(f)=\log_2\frac{Z-1}{x_q}-D_{KL,2}(w^+\|\nu^+),\qquad D_\Gamma(f)=-V_qR_\Gamma(f).
\]

For a disjoint composition `F=G(f_1,...,f_m)`, if `beta_i=Pr_{w_G}(i active)` and `v_i=V_{q_i}`, the physical Gibbs reference induces a block-activity law `eta` and the exact KL chain is

\[
D(w_F\|\nu_F)=D(w_G\|\eta)+\sum_i\beta_iD(w_i^+\|\nu_i^+).
\]

`eta` is the exact exponential tilt of the canonical outer Gibbs law by the child partition demands, yielding with no dropped KL

\[
D_\Gamma(F)=D_\Gamma(G;q)+\sum_i\frac{\beta_i}{v_i}D_\Gamma(f_i).
\]

For the tensor/product specialization `F=prod_j f_j`, conditioning on a nonempty parent spectrum creates a nonnegative block-activity KL.  If `P_A,Q_A` are the source/reference activity laws conditioned on at least one active block, then

\[
v_FK_F=\sum_jv_jK_j+v_FD(P_A\|Q_A)
\]

and the exact unpaid-remainder transfer is

\[
\boxed{
v_FR_\Gamma(F)=\sum_jv_jR_\Gamma(f_j)-\left[\sum_j\Gamma(q_j)-\Gamma(q_F)\right].
}
\]

For identical balanced tensor powers with child Gibbs partition `Z`,

\[
K_{f^{\otimes m}}=mK_f+\log_2\frac{Z^m-1}{(Z-1)^m},
\]

so dropping the activity KL loses `Theta(m)` genuine relative entropy.  This is a source-exact no-go for credit-free conditional-KL tensor interpolation.  The decomposition step itself introduces no hidden arithmetic debt; the remaining target is composition-prime outer gates.

Canonical science report: `proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260922T071345Z-gibbs-activity-tensor-transfer/REPORT.md`, creation commit `2384ded61f0015e1c14e5921436c1ef6ec9c98f4`, report blob `3d830c3b92fd50c0b62b9c64cb7effaa66a19414`.  Checker creation commit `b177b4a447b83655db86f6656518510baa49b2f2`; verification creation commit `d6460d8e431350d8ba56a3cdfc0b26e71ddc20fc`.
