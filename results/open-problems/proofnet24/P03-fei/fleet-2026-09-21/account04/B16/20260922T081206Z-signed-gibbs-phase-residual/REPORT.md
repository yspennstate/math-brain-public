# account04/B16 — signed Gibbs phase residual from Boolean convolution parity

**Classification:** `ESSENTIAL_STEP_APPLIED / SIGNED_BOOLEAN_SHAPE_CREDIT / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full unrestricted FEI:** **OPEN / NOT PROVED**.

## 0. Control and scope


Fresh scientific master used for the derivation was `2d89b7d5bec088d163aa3986e9f83d7499193fd5`.

The exact required inherited interface-C inputs were re-read at that revision:

1. account02/B16 actual parent weights:
   `proofnet24/P03-fei/fleet-2026-09-21/account02/B16/20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`.
   After same-syndrome signed aggregation its genuine central parent weights are
   \[
   \mu_j=\sum_{R:j\text{ doubled}}\frac{\varepsilon_{q_R,k_R}}{r_R}b_R^2,
   \qquad \sum_j\mu_j=E_{\rm cen},
   \]
   and the original-coordinate incidence bank is at most `11/192 W`. No R32 sign is discarded before the signed aggregate `b_R` is squared; terminal and R16/moment ledgers are not spent.
2. account03/B18 signed flag curvature:
   `proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260921T185340Z-signed-flag-curvature/REPORT.md`.
   Its exact physical sink is
   \[
   \kappa_i(w)=p_i(w)+4o_i(w),
   \]
   retaining the opposite-orientation overlap, with ordered-flag payments `sum E kappa <= 2J`, `sum E kappa^2 <= 4J`, and `sum E o <= J/2` in the minimizing-character gauge.

Those ledgers, including dual-code multiplicity, negative credits, live-window/R16 compensation and terminal terms, are left untouched below. The new theorem uses the same methodological rule at the live all-gate endpoint: preserve Fourier signs until the legitimate Boolean cancellation has been extracted, and only then pass to a positive KL/Hellinger quantity.

I also consumed the fresh all-gate sources at the same scientific revision:

- account03/B18 `20260922T075546Z-gibbs-price-bellman/REPORT.md`, which proves the exact Gibbs/Bellman decomposition for the live candidate;
- account02/B16 `20260922T074443Z-first-cell-weighted-curvature/REPORT.md`, which reduces the authenticated n=18 coherent-bias test to one positive weighted local slope curvature.

## 1. Exact live Gibbs residual

On the balanced uniform slice let `G:{-1,+1}^k -> {-1,+1}` be balanced and nonconstant. Write its ordinary Walsh coefficients as `a_S` and

\[
w(S)=a_S^2,\qquad a_\varnothing=0,\qquad \sum_{S\ne\varnothing}w(S)=1.
\]

For the live lifted candidate

\[
C^\dagger=6.521851214,
\qquad a^\dagger=0.268204856,
\qquad x=2^{-C^\dagger},
\]

account03/B18 proves, for every real `lambda`,

\[
R_B(G)=D_{\rm KL,2}(w\|\rho_{\lambda})
+\lambda C^\dagger I(G)-\log_2\frac{A_\lambda}{x},
\tag{1.1}
\]

where

\[
y=x^{1-\lambda},\qquad
A_\lambda=(1+y)^k-1,
\qquad
\rho_\lambda(S)=\frac{y^{|S|}}{A_\lambda}\quad(S\ne\varnothing).
\tag{1.2}
\]

The preceding B18 theorem solved the best lower bound using only the scalar mean price. Its stated missing term is exactly the residual shape information `D(w||rho_lambda)`. The purpose of this run is to extract a strictly positive part of that residual from **signed Boolean realizability**.

## 2. Boolean convolution must cancel before squaring

Because `G^2=1`, the signed Walsh coefficients obey, for every nonempty `T subset [k]`,

\[
\boxed{\sum_S a_Sa_{S\triangle T}=0.}
\tag{2.1}
\]

This is an oriented cancellation. Replacing `a_S` by `|a_S|` destroys it.

Fix `T` with `|T|=t>=2`. Pair subsets under the involution `S <-> S triangle T`. The pair `{empty,T}` contributes zero because `a_empty=0`. For the target Gibbs magnitudes, attach the **actual signs** of `a_S` (arbitrarily on zero coefficients) and define

\[
b_S=\operatorname{sgn}(a_S)\sqrt{\rho_\lambda(S)},\qquad b_\varnothing=0.
\]

Decompose `S=R union U`, with `R subset T^c` and `U subset T`. For `R=empty`, there are

\[
2^{t-1}-1
\]

remaining unordered pairs after deleting `{empty,T}`. This number is odd, and every such Gibbs pair product has the identical magnitude

\[
\frac{y^{t/2}}{A_\lambda}.
\]

Therefore their signed sum has magnitude at least one copy of that number. For each nonempty outside set `R`, there are `2^{t-1}` pairs and every pair product has magnitude

\[
\frac{y^{|R|+t/2}}{A_\lambda}.
\]

Even if all of those later blocks are oriented adversarially against the odd `R=empty` block, reverse triangle gives

\[
\boxed{
\left|\sum_{\{S,S\triangle T\}} b_Sb_{S\triangle T}\right|
\ge L_{k,t}(y)
}
\tag{2.2}
\]

with

\[
\boxed{
L_{k,t}(y)
=
\frac{y^{t/2}}{(1+y)^k-1}
\left[1-2^{t-1}\bigl((1+y)^{k-t}-1\bigr)\right]_+.
}
\tag{2.3}
\]

For `t=k` there are no outside blocks, so this simplifies universally to

\[
\boxed{L_{k,k}(y)=\frac{y^{k/2}}{(1+y)^k-1}>0.}
\tag{2.4}
\]

Thus the Gibbs I-projection itself is never a balanced Boolean squared spectrum: its equal-magnitude complement pairs have an odd signed-parity obstruction.

## 3. PROVED — explicit signed Boolean lower bound for the residual KL

Let

\[
h^2(w,\rho)=\sum_{S\ne\varnothing}
(\sqrt{w(S)}-\sqrt{\rho(S)})^2.
\]

Use the actual signs of `a_S` on both amplitude systems. Since unordered `T`-pairs are disjoint,

\[
\sum_{\{S,S\triangle T\}}
\left|
\sqrt{w(S)w(S\triangle T)}-
\sqrt{\rho(S)\rho(S\triangle T)}
\right|
\le 2h(w,\rho)
\tag{3.1}
\]

by two Cauchy-Schwarz applications. The actual signed pair sum is zero by (2.1), while the Gibbs signed pair sum has magnitude at least (2.3). Hence

\[
h(w,\rho_\lambda)\ge \frac{L_{k,t}(y)}2.
\tag{3.2}
\]

Rényi monotonicity (or the elementary affinity bound) gives in base two

\[
D_{\rm KL,2}(w\|\rho)
\ge \frac{h^2(w,\rho)}{\ln2}.
\]

Therefore:

### Theorem B16-SIGNED-GIBBS-PHASE-RESIDUAL

For every balanced Boolean `k`-input gate, every real `lambda`, and every `2<=t<=k`,

\[
\boxed{
D_{\rm KL,2}(w\|\rho_\lambda)
\ge
P_{k,t}(y)
:=
\frac{y^t}{4\ln2\,((1+y)^k-1)^2}
\left[1-2^{t-1}\bigl((1+y)^{k-t}-1\bigr)\right]_+^2.
}
\tag{3.3}
\]

In particular the unconditional complement-pair credit is

\[
\boxed{
D_{\rm KL,2}(w\|\rho_\lambda)
\ge
\frac{y^k}{4\ln2\,((1+y)^k-1)^2}.
}
\tag{3.4}
\]

This is a genuine positive lower bound for the residual shape term that the scalar Gibbs/Bellman relaxation necessarily discards. It comes from signed Boolean realizability, not from an unsigned support relaxation.

## 4. Exact strengthened Bellman inequality and comparable gate margin

Combining (1.1) and (3.3), for every balanced Boolean gate,

\[
\boxed{
R_B(G)
\ge
\lambda C^\dagger I(G)
-\log_2\frac{(1+y)^k-1}{x}
+\max_{2\le t\le k}P_{k,t}(y),
\qquad y=x^{1-\lambda}.
}
\tag{4.1}
\]

This is strict mechanism movement over the scalar-only B18 envelope: the extra term is source-valid and positive for every `lambda` through `t=k`.

In the owner-requested gate-margin units, if `D_0` denotes the defect of the underlying unlifted candidate `Gamma_0`, then on the balanced uniform slice

\[
D_{\Gamma^\dagger}=D_0+a^\dagger\frac{I(G)-1}{4},
\]

so for `I(G)>1`

\[
\boxed{
c_G=-\frac{D_0}{(I-1)/4}
\le a^\dagger-
\frac{4}{I-1}
\left[
\lambda C^\dagger I-
\log_2\frac{A_\lambda}{x}
+\max_tP_{k,t}(y)
\right].}
\tag{4.2}
\]

No raw defect is being compared across arities without the Poincare-currency denominator.

## 5. Concrete exact slice and diagnostic size

For `k=3`, choose the exact rational tilt `lambda=5/6` and `t=3`. Then

\[
y=x^{1/6},\quad A=(1+y)^3-1,
\]

and (4.1) proves safety whenever

\[
I(G)\ge
\boxed{
\frac{\log_2(A/x)-y^3/(4\ln2\,A^2)}{(5/6)C^\dagger}.
}
\tag{5.1}
\]

A deterministic floating evaluation, used only as a diagnostic, is

\[
1.4055847175768663\ldots
\]

versus `1.4070396062353996...` from the same `lambda=5/6` after deleting the signed phase credit. The gain is `0.00145488865853327...` in the influence threshold. This does not replace the stronger finite low-arity certificates already in the fleet; it validates that the missing B18 residual has an analytic Boolean payment rather than being merely a formal nonnegative term.

The checker exhausts all 70 balanced three-input truth tables at `lambda=5/6,t=3` and all 12,870 balanced four-input truth tables at `lambda=4/5,t=4`. The minimum observed slack `D_KL-P` is respectively `0.7477902534237776` and `0.4892820648099886`; these finite checks are sanity tests, not the proof.

## 6. What remains open

The new phase credit does **not** close unrestricted FEI. At large arity the universal `t=k` credit can be exponentially small at the scalar-optimal Gibbs tilt. To finish the all-gate route one still needs either:

1. a sum/packet version of the signed convolution constraints that accumulates dimension-independently rather than spending only one `T`; or
2. a genuine composition-prime gate/bias falsifying the live lifted candidate.

The natural next signed step is to keep a whole family of low-cardinality `T` convolution equations simultaneously and derive a PSD/relative-entropy packet inequality before taking absolute values. That is directly analogous to the historical interface-C rule: preserve orientation and opposite-sign overlap until the legitimate cancellation has happened, then contract to a positive sink.

No historical R16/R32 negative credit, dual-code multiplicity, terminal term, finite-window remainder, Ward bank, or signed flag-curvature payment is reused in (3.3)--(4.2).