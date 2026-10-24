# B12 — exact B0 conditional Shannon increment and certified branch reserve

**Classification:** `AUXILIARY_ONLY`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Candidate attacked:** `LIMIT-PRIME-GATE-LIFT-v1`, stable scalar lift at center `C_*=6.5218512`.  
**Execution label:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact inherited target and peer results applied

The current all-gate defect is

\[
D_\Gamma(G;p)=\sum_i\frac{\operatorname{It}_i(G;p)}{V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\]

The stable candidate is

\[
\Gamma_*(u)=\Gamma_{\rm RO}(u)+a_*u(1-u),\qquad
C_*:=\Gamma_*(1/2)=6.5218512,
\]
with `Gamma_RO(1/2)=6.4548` and
\[
a_*=4(C_*-6.4548)=0.2682048.
\]
The remaining proposed universal implication is `D_{Gamma_*}(P;p)>=0` for every composition-prime finite Boolean gate and every interior product bias. This implication is not proved.

This run substantively applies two compatible other-account results.

1. `account03/B14/20260922T030222Z-quarter-equality-factorization/REPORT.md` classifies the five-input quarter-output equality cases and reduces all 1,920 essential cases through one literal and the same four-bit composition-prime gate
\[
B_0^{-1}(1)=\{0,1,2,3,4,5,8,10\}\subset Q_4.
\]
Thus the all-bias analysis of this actual prime gate is a genuine outstanding piece of that exact family, not a new unrelated subclass.

2. `account04/B17/20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md` proves the exact one-coordinate biased entropy/defect cocycle retaining the branch/KL and vertical-overlap credits. This run uses that cocycle, not the false credit-free restriction inequality.

The already certified read-once theorem gives `H<=6.4573 I` for every AND/OR/NOT read-once formula. Its certified potential is `Gamma_cert=Gamma_RO+0.01 u(1-u)`. Hence
\[
\Gamma_*=\Gamma_{\rm cert}+0.2582048\,u(1-u).
\]

## 2. Boolean structure of the prime gate

Use coordinates `x_1,x_2,x_3,x_4` corresponding to truth-table bits `0,1,2,3`, with independent biases
\[
p=\Pr[x_1=1],\quad q=\Pr[x_2=1],\quad t=\Pr[x_3=1],\quad r=\Pr[x_4=1].
\]
Directly from the eight true points,
\[
\boxed{B_0=1\iff \neg(x_2x_3)\wedge\neg(x_3x_4)\wedge\neg(x_4x_1).}
\tag{2.1}
\]
Thus `B0` is the independent-set indicator of the three-edge path `x_2-x_3-x_4-x_1`.

Condition on the selector `x_3`. The two restrictions are
\[
B_{0,0}=\operatorname{NAND}(x_1,x_4),\qquad
B_{0,1}=(1-x_2)(1-x_4).
\tag{2.2}
\]
The unused coordinate in each branch is dummy. Therefore both children are certified two-input read-once gates, and they share only `x_4`.

## 3. Exact four-scalar conditional Shannon increment

Take the sign representative `g=2B_0-1`; global sign is irrelevant to squared Fourier masses. On the remaining coordinates `{x_1,x_2,x_4}`, choose the biased-Walsh basis signs so the shared `x_4` coefficients are positive. The branch coefficients are
\[
\begin{aligned}
a_\varnothing&=1-2pr,&
|a_{1}|&=2r\sqrt{p(1-p)},&
a_4&=2p\sqrt{r(1-r)},&
|a_{14}|&=2\sqrt{p(1-p)r(1-r)},\\
b_\varnothing&=2(1-q)(1-r)-1,&
|b_{2}|&=2(1-r)\sqrt{q(1-q)},&
b_4&=2(1-q)\sqrt{r(1-r)},&
|b_{24}|&=2\sqrt{q(1-q)r(1-r)}.
\end{aligned}
\tag{3.1}
\]
All other coefficients vanish. Hence the two branch spectra overlap on exactly two supports: `emptyset` and `{x_4}`.

Put `phi(z)=-z log_2 z` with `phi(0)=0`, and define the exact entropy gain of one coefficient pair under selector bias `t` by
\[
F_t(a,b)=
\phi(((1-t)a+tb)^2)
+\phi(t(1-t)(a-b)^2)
-(1-t)\phi(a^2)-t\phi(b^2).
\tag{3.2}
\]
It is exactly two-homogeneous: `F_t(lambda a,lambda b)=lambda^2 F_t(a,b)`. Define the one-sided functions
\[
\begin{aligned}
A_0(t):=F_t(1,0)
&=-(1-t)(2-t)\log_2(1-t)-t(1-t)\log_2 t,\\
A_1(t):=F_t(0,1)
&=-t(1+t)\log_2 t-t(1-t)\log_2(1-t).
\end{aligned}
\tag{3.3}
\]
Then the complete conditional spectral-Shannon increment is
\[
\boxed{
\begin{aligned}
\Delta_H(p,q,t,r)
={}&F_t\!\left(1-2pr,\,2(1-q)(1-r)-1\right)\\
&+4r(1-r)F_t(p,1-q)\\
&+4p(1-p)r\,A_0(t)\\
&+4q(1-q)(1-r)\,A_1(t).
\end{aligned}}
\tag{3.4}
\]
There is no omitted coordinate-label term. The first two lines are the two overlap modes. The last two lines are the entire one-sided support: indeed
\[
|a_1|^2+|a_{14}|^2=4p(1-p)r,
\quad
|b_2|^2+|b_{24}|^2=4q(1-q)(1-r).
\]

The branch output probabilities and physical disagreement probability are
\[
\rho_0=1-pr,\qquad
\rho_1=(1-q)(1-r),\qquad
\rho=(1-t)\rho_0+t\rho_1,
\tag{3.5}
\]
\[
\boxed{\delta=(1-r)q+r(1-p).}
\tag{3.6}
\]
For (3.6), condition on `x_4`: at `x_4=0` the branches differ iff `x_2=1`, and at `x_4=1` they differ iff `x_1=0`.

Therefore the exact root increment in the defect cocycle is
\[
\boxed{
L_\Gamma(p,q,t,r)=
(1-t)\Gamma(\rho_0)+t\Gamma(\rho_1)-\Gamma(\rho)
+\delta\,[\Gamma(t)+h_2(V_t)]-\Delta_H(p,q,t,r).
}
\tag{3.7}
\]
The account04/B17 exact cocycle becomes
\[
\boxed{
D_\Gamma(B_0)=
(1-t)D_\Gamma(\operatorname{NAND}_{p,r})
+tD_\Gamma(\operatorname{AND}_{1-q,1-r})
+L_\Gamma.
}
\tag{3.8}
\]
Thus all branch conditional-information credits have been retained inside the exact `Delta_H`; no credit-free relaxation was used.

## 4. The missing term is reduced to one explicit scalar inequality

For a two-input AND with true-input probabilities `alpha,beta`, its quadratic Poincare currency is exactly
\[
W_{\rm AND}=I/4-p_{\rm out}(1-p_{\rm out})
=\alpha\beta(1-\alpha)(1-\beta).
\tag{4.1}
\]
Because `Gamma_cert` certifies every binary AND/NAND at every bias and `Gamma_*` adds `0.2582048 u(1-u)`, we get the rigorous child reserves
\[
D_{\Gamma_*}(\operatorname{NAND}_{p,r})
\ge0.2582048\,pr(1-p)(1-r),
\tag{4.2}
\]
\[
D_{\Gamma_*}(\operatorname{AND}_{1-q,1-r})
\ge0.2582048\,qr(1-q)(1-r).
\tag{4.3}
\]
Substituting into (3.8) yields
\[
\boxed{
\begin{aligned}
D_{\Gamma_*}(B_0;p,q,t,r)
\ge{}&L_{\Gamma_*}(p,q,t,r)\\
&+0.2582048\,r(1-r)
\big[(1-t)p(1-p)+tq(1-q)\big].
\end{aligned}}
\tag{4.4}
\]
This is the precise new missing implication. To certify the whole account03/B14 quarter-equality prime core, it is now enough to prove that the explicit right side of (4.4) is nonnegative for every `(p,q,t,r) in (0,1)^4`. It is also a direct falsification target: any negative point is a genuine Boolean product-bias obstruction to the stable candidate.

## 5. Biased-limit obstruction applied: every boundary facet is already read-once

Every codimension-one bias boundary of B0 reduces to an AND/OR/NOT read-once formula:

- `p=0`: `not x_3 OR (not x_2 AND not x_4)`;
- `p=1`: `not x_4 AND (not x_2 OR not x_3)`;
- `q=0`: `not x_4 OR (not x_3 AND not x_1)`;
- `q=1`: `not x_3 AND (not x_4 OR not x_1)`;
- `t=0`: `NAND(x_1,x_4)`;
- `t=1`: `not x_2 AND not x_4`;
- `r=0`: `NAND(x_2,x_3)`;
- `r=1`: `not x_1 AND not x_3`.

Hence `D_{Gamma_*}>=0` on the entire product-bias boundary by the certified read-once theorem plus the nonnegative additional quadratic lift. Away from character/constant degeneracies, the additional `0.2582048 W` gives strict reserve whenever the Poincare currency is positive. Therefore any counterexample in this B0 family must be genuinely interior (or approach a character boundary through a singular limiting regime); there is no exact boundary counterexample.

This is a real use of the biased-limit obstruction requested by the execution order, and it narrows the search/proof domain rather than introducing a second residual.

## 6. Status

**Old missing implication.** Prove `D_{Gamma_*}(B_0;p)>=0` for every product bias, because account03/B14 reduces the 1,920 quarter-output equality cases to one literal composition with this same composition-prime B0.

**New missing implication.** Prove the explicit four-scalar inequality (4.4) for the interior cube. Its boundary is certified, its two read-once child defects are already paid, and the only unresolved root entropy is the two-overlap formula (3.4) plus the displayed one-sided terms.

This is materially narrower and source-valid, but it is still an unproved universal inequality. Therefore this run is `AUXILIARY_ONLY`, not `ESSENTIAL_STEP_APPLIED` and not a full FEI candidate. Full FEI remains open.
