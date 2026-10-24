# account04/B15 — source-bound FEI handoff: logarithmic all-shift tariff

**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Full unrestricted FEI:** **OPEN / NOT PROVED**.  
**Scientific source:** `yspennstate/math-open-problems`, report commit `94f7fa8b85819fd242f7c019ef080162d11deb8c`, checker commit `4ff52f51a9cf41c2782c5fec1ad74dc7774d8537`, output commit `e0fe26e054a3e7395ec93e80378341ba3800185d`.

The consumed account02/B15 I-projection remainder is source-exact:

\[
R_\Gamma=B_{\rm inf}^{\Gamma}+K_{\rm occ},
\qquad
K_{\rm occ}=D_{\rm KL,2}(P\Vert Q_r)=H_{\max}(r)-H(P),
\]

so the actual unpaid Shannon obligation is `K_occ >= [-B_inf^Gamma]_+`.  No valuation term is substituted for this KL, and no packet integrality or credit-free interpolation is used.  Account02/B15's newer suspension no-loss theorem shows that a fixed fractional loss of `K_occ` cannot be repaired by an `O(J)` valuation bank.

On the genuine sparse one-point-defect suspensions, put `p=2^(1-m)`, `g_m=1-2 1_{x=0}`, `F_m=y g_m`, and sign-align the square roots of the influence I-projection with the actual Walsh signs.  For every nonzero XOR shift `U`, with `r=|U|`, the exact convolution defect is

\[
C_m(U)=(2\sqrt{p(1-p)})^r-4(1-p)^{m-r/2}p^{r/2}.
\]

Define the nonlinear full-shift statistic

\[
\mathcal L_m=\sum_{U\ne0}C_m(U)^2\log_2\frac1{C_m(U)^2}.
\]

The new theorem proves

\[
\frac{\mathcal L_m}{4I(g_m)}=m-3+o(1),
\qquad
\frac{K_{\rm occ}(F_m)}{I(g_m)}=m-5+\frac1{\ln2}+o(1),
\]

hence

\[
\boxed{
K_{\rm occ}(F_m)
=\frac14\mathcal L_m
-\left(2-\frac1{\ln2}\right)I(g_m)+o(I(g_m)).
}
\]

Thus `1/4` is the unique coefficient compatible with an additive `O(I)` transfer `K_occ >= theta L - O(I)` on this actual Boolean family.  If `theta<1/4`, the payment is short by `Theta(mI)`; if `theta>1/4`, the proposed lower bound overclaims the true KL by `Theta(mI)`; at `theta=1/4` the mismatch is only `(2-1/ln 2)I+o(I)`, about `0.557304959 I`.

This materially changes the failed all-shifts quadratic method: the raw `L^2` energy is only `O(I)`, but the logarithmic tariff recovers the exact rare-event `Theta(mI)` scale.  The support-KL refund is zero on this calibration family, so the recovered quantity is genuine shape/dependence KL.

**Replacement obligation:** first spend the exact support refund, then construct or refute on physical signed sources—preferably the balanced composition-prime `c<1` corridor—a support-conditioned inequality of the form

\[
D(P\Vert Q_r(\cdot\mid\operatorname{supp}P))
\ge \frac14\mathcal L_{\rm phys}-\kappa I
\]

with finite `kappa`, retaining every remaining KL and valuation credit separately.  A prime-only theorem may exploit stronger structure, but any full-source transfer that composes without KL loss must respect the `1/4` suspension calibration.
