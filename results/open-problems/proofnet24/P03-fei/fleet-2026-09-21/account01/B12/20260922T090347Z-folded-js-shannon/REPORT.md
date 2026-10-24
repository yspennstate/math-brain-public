# account01/B12 — folded all-bias JS payment and a closed conditional-Shannon increment bound

**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Source correction and exact inputs

The current all-gate objective is still the exact gate inequality `(G)`, but the fixed potential

\[
\Gamma^\dagger=\Gamma_0+0.268204856\,p(1-p),\qquad \Gamma^\dagger(1/2)=6.521851214,
\]

is **not** a live universal candidate: account03/B12's source-exact composition-prime 18-input witness at `(3/8,1/2,...,1/2)` has

\[
D_{\Gamma^\dagger}=-0.0176114199558017537894958865691\ldots<0,
\]

and account04/B18 records the resulting repair-shape constraint. I therefore do not use local positive results for `Gamma^dagger` as evidence of universal closure.

The completed other-account theorem consumed and applied here is account03/B15

`proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T082654Z-js-packet-payment/REPORT.md`

at strengthened commit `8793c7e49e1de7921bc76c7724c92fae03024e26`, blob `b42a78fd9e6621661954fdc0b44eaa1ba0261179`. It proves the exact genuine-restriction packet decomposition and, for selector bias `s`,

\[
\operatorname{JS}_s(U,V)\le \kappa(s)\operatorname{It}_i(G;p),
\]

where

\[
\kappa(s)=\frac{\ln((1-s)/s)}{(1-2s)\ln 2},\qquad
\kappa(1/2)=\frac{2}{\ln2}.
\]

The new step below applies that theorem to a second **genuine Boolean sign-twist of the same gate**, not to a relaxed packet law.

## 1. Exact conditional Shannon increment

Fix an actual selector coordinate `i` of bias `s in (0,1)`. Let `G_0,G_1` be the two Boolean restrictions and write their biased Fourier coefficients on the remaining coordinates as `u_T,v_T`. Put

\[
e_T=(1-s)u_T^2+s v_T^2,
\]

\[
q_T=\frac{s(1-s)(u_T-v_T)^2}{e_T}
\]

on nonzero packets. Let

\[
p:=\sum_T e_Tq_T=\operatorname{It}_i(G;p).
\]

If `U_T=u_T^2`, `V_T=v_T^2`, then the exact entropy chain rule for the parent Fourier pair gives

\[
\boxed{
\Delta_i\widetilde H
:=\widetilde H_G-(1-s)\widetilde H_{G_0}-s\widetilde H_{G_1}
=B_i+\operatorname{JS}_s(U,V),
}
\tag{1.1}
\]

where

\[
B_i=\sum_Te_T h_2(q_T).
\tag{1.2}
\]

This is the actual conditional Shannon increment. No coordinate label, sign, or conditional-information term is omitted.

By Jensen,

\[
\boxed{B_i\le h_2(p).}
\tag{1.3}
\]

The known obstruction `B_i/p -> infinity` for sparse defects is therefore preserved rather than hidden.

## 2. New theorem: fold the JS charge by a genuine selector sign-twist

Define the Boolean sign function on the selector coordinate

\[
\sigma_i(0)=1,\qquad \sigma_i(1)=-1,
\]

and the genuine Boolean gate

\[
G^\sharp=\sigma_i G.
\]

Its two restrictions are `G_0` and `-G_1`, so their **squared** Fourier laws are still exactly `U,V`. Hence the weighted Jensen--Shannon term is unchanged:

\[
\operatorname{JS}_s(U,V)\quad\text{is the same for }G\text{ and }G^\sharp.
\]

The selector influence of the sign-twisted gate is

\[
p^\sharp
=s(1-s)\sum_T(u_T+v_T)^2.
\]

Parseval for the two Boolean children gives `sum_T u_T^2=sum_Tv_T^2=1`, and therefore

\[
\begin{aligned}
p+p^\sharp
&=s(1-s)\sum_T\big[(u_T-v_T)^2+(u_T+v_T)^2\big]\\
&=2s(1-s)\sum_T(u_T^2+v_T^2)\\
&=4s(1-s)=:V_s.
\end{aligned}
\tag{2.1}
\]

Apply the account03/B15 all-bias theorem once to `G` and once to the genuine Boolean gate `G^sharp`. Since both applications have the same child spectral laws,

\[
\operatorname{JS}_s(U,V)\le\kappa(s)p,
\qquad
\operatorname{JS}_s(U,V)\le\kappa(s)p^\sharp.
\]

Using (2.1) proves the new folded payment

\[
\boxed{
\operatorname{JS}_s(U,V)
\le
\kappa(s)\min\{p,V_s-p\}.
}
\tag{2.2}
\]

This is dimension-free, sign-safe, valid at every interior selector bias, and uses only genuine Boolean gates. It is strictly stronger than the one-sided peer estimate whenever `p>V_s/2`.

There is also a physical form. If

\[
d=\Pr[G_0\ne G_1]
\]

under the actual product law on the remaining inputs, then because the outputs are `+-1`,

\[
p=s(1-s)\mathbb E(G_1-G_0)^2=4s(1-s)d=V_s d.
\tag{2.3}
\]

The sign twist exchanges disagreement and agreement, so `p^sharp=V_s(1-d)`. Thus (2.2) is exactly

\[
\boxed{
\operatorname{JS}_s(U,V)
\le\kappa(s)V_s\min\{d,1-d\}.
}
\tag{2.4}
\]

At a selector-like split `d -> 1`, the JS mixing charge therefore goes to zero, as it should; the earlier one-sided estimate did not see this endpoint cancellation.

## 3. Closed bound for the entire missing conditional-Shannon term

Combining the exact identity (1.1), Jensen (1.3), and the folded JS theorem (2.2) gives

\[
\boxed{
\Delta_i\widetilde H
\le
h_2(p)+\kappa(s)\min\{p,V_s-p\},
\qquad 0\le p\le V_s.
}
\tag{3.1}
\]

Equivalently, in physical disagreement coordinates,

\[
\boxed{
\Delta_i\widetilde H
\le
h_2(V_s d)+\kappa(s)V_s\min\{d,1-d\}.
}
\tag{3.2}
\]

This is the requested explicit bound on the missing conditional Shannon increment. It contains no free `B_i` term and no uncharged label entropy.

For example, at `s=3/8`,

\[
V_s=15/16,\qquad \kappa(3/8)=2.947862376664825\ldots.
\]

At a hypothetical physical disagreement `d=0.9`, the old one-sided JS budget is about `2.48726`, while (2.4) gives about `0.276362`, a factor-nine improvement. This decimal is only an illustration; (2.2)--(3.2) are analytic.

At the symmetric selector `s=1/2`, (3.1) becomes

\[
\Delta_i\widetilde H
\le
h_2(p)+\frac{2}{\ln2}\min\{p,1-p\}.
\tag{3.3}
\]

The previously proved exact uniform scalar frontier `Psi(p)=h_2(p)+j(p)` is sharper on that special slice, so (3.3) is not presented as a replacement for the older symmetric theorem. The advance here is the **all-bias folded endpoint correction**.

## 4. Insertion into an arbitrary replacement all-gate potential

For any symmetric potential `Gamma` for which the gate defect is defined, account03/B15's exact recursion is

\[
D_\Gamma(G;p)
=(1-s)D_0+sD_1
+(1-s)\Gamma(q_0)+s\Gamma(q_1)-\Gamma(q)
+a_i p-B_i-\operatorname{JS}_s(U,V),
\]

where

\[
a_i=\frac{\Gamma(s)+h_2(V_s)}{V_s}.
\]

The new theorem gives the candidate-independent lower bound

\[
\boxed{
\begin{aligned}
D_\Gamma(G;p)\ge{}&(1-s)D_0+sD_1\\
&+(1-s)\Gamma(q_0)+s\Gamma(q_1)-\Gamma(q)\\
&+a_i p-h_2(p)-\kappa(s)\min\{p,V_s-p\}.
\end{aligned}}
\tag{4.1}
\]

Thus a future repaired universal potential does not need to budget the full one-sided `kappa(s)p` JS loss near selector-like splits. The remaining local obstruction is now the explicit scalar entropy overhead `h_2(p)` together with the actual child defects and the potential Jensen term.

## 5. Obstruction checks before promotion

This theorem does **not** evade the known hard families.

1. **Sparse defects / bent-plus-flip.** When `p -> 0`, `h_2(p)/p -> infinity`. Equation (3.1) therefore does not imply a false universal linear erasure bound.
2. **Addressing, tribes, majority.** Their hard coordinates can remain in the small-`p` regime; (3.1) does not declare them solved.
3. **Tensor products.** The theorem is one physical restriction identity. No tensor-subadditivity or product closure is inferred from it.
4. **Biased limits.** `kappa(s)` diverges as `s -> 0,1`, so no false bias-uniform pointwise coefficient is claimed. The absolute factor `V_s kappa(s)` nevertheless tends to zero, consistently with the vanishing selector mass.
5. **Refuted fixed potential.** Equations (2.2)--(4.1) do not resurrect `Gamma^dagger`; the exact 18-input prime witness still has negative defect for that fixed potential.

## 6. Exact old/new missing implication

**Old live mathematical obstruction:** after the source-exact packet recursion, the conditional increment retained an unpaid `B_i` and a one-sided JS estimate `JS_s<=kappa(s)p`; the fixed `Gamma^dagger` to which some recent B handoffs attached this recursion has separately been refuted.

**New proved inference:** the same physical JS term is simultaneously controlled by the selector influence of the genuine Boolean sign-twist, giving `JS_s<=kappa(s)min(p,V_s-p)`, and consequently the whole conditional Shannon increment obeys the closed scalar estimate (3.1)/(3.2).

**Remaining implication to full FEI:** construct a symmetric nonnegative finite-cap replacement potential satisfying every gate inequality, or prove a candidate-independent stopping/critical-core argument. In recursion form, one must still pay the explicit small-`p` entropy overhead in (4.1) using retained child slack / shape information; `h_2(p)/p` shows why a credit-free per-coordinate argument cannot finish the conjecture.

**Classification:** `ESSENTIAL_STEP_APPLIED`; full FEI remains **OPEN / NOT PROVED**.
