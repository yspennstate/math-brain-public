# B17 — exact biased restriction margin cocycle with mandatory KL credits

**Classification:** `ESSENTIAL_STEP_APPLIED / NEW_REPLACEMENT_MECHANISM`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Live target and peer results consumed

The current owner-level FEI target is the all-gate inequality

\[
D_\Gamma(G;p):=
\sum_i \frac{\operatorname{It}_i(G;p)}{V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p)\ge0,
\qquad V_u=4u(1-u),
\tag{1.1}
\]

for every Boolean gate and every product bias. The stable scalar-lift target in the current chain is
`LIMIT-PRIME-GATE-LIFT-v1`, with centre `6.5218512`; proving its gate inequality universally would imply FEI with that constant, but this remains open.

This run substantively consumes the newest compatible other-account B15 result

`account03/B15/20260922T022636Z-depth-locked-shared-core/REPORT.md`.

That report proves that, at the present shared-core state, depth four is the unique immediately improving integer self-composition depth and that a substantive next adversary must change the host/core geometry or product bias rather than repeat the depth-four tail. The preceding B17 semigroup ceiling already controls arbitrary interleavings of the same fixed shared-core transform with balanced disjoint composition, so this run changes mechanism completely.

Two still newer compatible handoffs are also used:

* `account03/B17/20260922T0304Z-biased-eq-boundary/REPORT.md` reduces the equal-bias antipodal two-defect family to exact one-variable formulas and proves that a positive linear-log potential repels that family at extreme bias. This run therefore does not repeat the EQ family.
* `account03/B14/20260922T030222Z-quarter-equality-factorization/REPORT.md` proves that all 1,920 five-input quarter-output equality cases factor through one literal and the same four-input composition-prime class
  \[
  B_0:\quad A=\{0,1,2,3,4,5,8,10\}\subset Q_4,
  \tag{1.2}
  \]
  and explicitly hands the all-bias analysis of this four-bit prime class to account04/B17.

The result below gives a new exact replacement interface for that all-bias problem. It also retains, rather than discards, the KL/information credits emphasized by earlier B15 restriction work.

## 2. Exact biased Fourier splitting at one physical coordinate

Let `G:{0,1}^n->{0,1}` and put `f=(-1)^G`. Inputs are independent with `Pr[X_i=1]=p_i`. Fix a pivot coordinate `j`, write

\[
t=p_j,\qquad q=1-t,
\]

and let `f_0,f_1` be the two restrictions at `X_j=0,1`. Expand the restrictions in the biased orthonormal basis on the remaining coordinates:

\[
a_S=\widehat {f_0}(S),\qquad b_S=\widehat {f_1}(S).
\]

Then the parent coefficients occur in exact orthogonal pairs

\[
\widehat f(S)=q a_S+t b_S,
\qquad
\widehat f(S\cup\{j\})=\sqrt{tq}\,(b_S-a_S).
\tag{2.1}
\]

Consequently, with

\[
P_0(S)=a_S^2,\qquad P_1(S)=b_S^2,
\]

\[
T_S=qP_0(S)+tP_1(S),
\qquad
d_S^2=tq(b_S-a_S)^2,
\tag{2.2}
\]

we have the pointwise identity

\[
\widehat f(S)^2+\widehat f(S\cup\{j\})^2=T_S.
\tag{2.3}
\]

Thus `P_0`, `P_1`, and `T` are probability laws. If

\[
\theta_S=d_S^2/T_S
\]

(with `theta_S=0` when `T_S=0`), then summing the binary split entropy inside each pair gives

\[
\widetilde H_G
=H(T)+\sum_ST_Sh_2(\theta_S).
\tag{2.4}
\]

The mixture entropy has the exact Jensen-Shannon decomposition

\[
H(T)=q\widetilde H_{G_0}+t\widetilde H_{G_1}
+\operatorname{JS}_t(P_0,P_1).
\tag{2.5}
\]

Let `B` be a latent restriction branch with `Pr[B=1]=t` and conditional spectral law `P_B`. Then

\[
\operatorname{JS}_t(P_0,P_1)=I(B;S)
=h_2(t)-H(B\mid S).
\tag{2.6}
\]

Next let `J` be the within-pair Fourier-layer bit with

\[
\Pr[J=1\mid S]=\theta_S.
\]

Its marginal mass is exactly the pivot spectral influence

\[
\Pr[J=1]=\sum_Sd_S^2=\operatorname{It}_j(G;p).
\tag{2.7}
\]

Therefore

\[
\sum_ST_Sh_2(\theta_S)
=H(J\mid S)
=h_2(\operatorname{It}_j)-I(S;J).
\tag{2.8}
\]

Combining (2.4)--(2.8) gives the first main identity.

### Theorem 1 — exact biased restriction entropy cocycle

For every Boolean gate, every interior product bias and every pivot coordinate,

\[
\boxed{
\widetilde H_G
=q\widetilde H_{G_0}+t\widetilde H_{G_1}
+h_2(t)+h_2(\operatorname{It}_j)-\mathcal C_j,
}
\tag{2.9}
\]

where the exact nonnegative credit is

\[
\boxed{
\mathcal C_j=H(B\mid S)+I(S;J)\ge0.
}
\tag{2.10}
\]

Both credits are source-exact. The first is the unspent branch uncertainty left after the Jensen-Shannon/KL mixture cost. The second is the mutual-information refund left after the within-pair split is upper-bounded by the binary entropy of its total mass.

No arbitrary probability-law relaxation has been introduced: `P_0`, `P_1`, `T`, `B`, and `J` all arise from actual Boolean restrictions and the exact biased Walsh transform.

## 3. Influence and output identities

Let

\[
r_b=\Pr[G_b=1],\qquad r=qr_0+tr_1,
\]

and let

\[
\delta_j=\Pr[G_0(X_{-j})\ne G_1(X_{-j})].
\]

Parseval applied to `f_1-f_0` gives

\[
\boxed{
\operatorname{It}_j=4tq\,\delta_j=V_t\delta_j.
}
\tag{3.1}
\]

For every other coordinate `i!=j`, physical sensitivity or, equivalently, the paired Fourier identity gives

\[
\boxed{
\operatorname{It}_i(G)=q\operatorname{It}_i(G_0)+t\operatorname{It}_i(G_1).
}
\tag{3.2}
\]

These identities use the same normalization as (1.1).

## 4. Exact all-gate defect cocycle

Substitute (2.9), (3.1), and (3.2) into the all-gate functional. Define

\[
\begin{aligned}
\mathcal R_{\Gamma,j}:={}&
q\Gamma(r_0)+t\Gamma(r_1)-\Gamma(r)\\
&+\delta_j\bigl(\Gamma(t)+h_2(V_t)\bigr)
-h_2(t)-h_2(\operatorname{It}_j).
\end{aligned}
\tag{4.1}
\]

Then:

### Theorem 2 — exact all-gate restriction cocycle

\[
\boxed{
D_\Gamma(G;p)
=qD_\Gamma(G_0;p_{-j})
+tD_\Gamma(G_1;p_{-j})
+\mathcal R_{\Gamma,j}+\mathcal C_j.
}
\tag{4.2}
\]

This is a replacement for a credit-free one-coordinate remainder estimate. It is an identity, not an inequality. In particular, the KL/branch credit and the vertical-overlap credit survive all the way into the all-gate normalization.

Iterating (4.2) down any fixed or adaptive restriction tree yields an exact telescoping representation of the parent defect as the product-measure weighted sum of the local quantities `R+C`, plus the defects of the terminal restrictions. For a boundary-normalized potential `Gamma(0)=Gamma(1)=0`, terminal constants have zero defect.

## 5. Quadratic lift: a second exact cocycle and a local margin max principle

Let

\[
\Gamma_c(u)=\Gamma_0(u)+c\,u(1-u),
\tag{5.1}
\]

where `Gamma_0` is any symmetric boundary-normalized base potential. The global change in defect is

\[
D_{\Gamma_c}(G)=D_{\Gamma_0}(G)+cW_G,
\qquad
W_G=\frac{I(G;p)}4-r(1-r).
\tag{5.2}
\]

At a restriction node, the quadratic part of (4.1) simplifies by the law of total variance:

\[
q r_0(1-r_0)+t r_1(1-r_1)-r(1-r)
=-tq(r_1-r_0)^2.
\]

Hence the local quadratic currency is exactly

\[
\boxed{
\mathcal W_j=tq\bigl(\delta_j-(r_1-r_0)^2\bigr)\ge0.
}
\tag{5.3}
\]

The inequality follows from `|r_1-r_0|<=delta_j<=1`. More strongly,

\[
\boxed{
W_G=qW_{G_0}+tW_{G_1}+\mathcal W_j.
}
\tag{5.4}
\]

Thus defect and quadratic currency telescope on the **same restriction tree**.

If `0<t<1`, then `W_j=0` can occur only in two degenerate cases:

* `delta_j=0`, so the pivot is dummy and `G_0=G_1`; or
* `delta_j=1` and `|r_1-r_0|=1`, so the node is exactly a literal/negated literal.

In both cases the exact local contribution `R_{Gamma_0,j}+C_j` is also zero. Therefore, for any complete restriction tree and any nonconstant gate with `W_G>0`, define at every positive-currency node

\[
c_v^{\rm loc}
=-\frac{\mathcal R_{\Gamma_0,v}+\mathcal C_v}{\mathcal W_v}.
\tag{5.5}
\]

Then:

### Theorem 3 — restriction-tree weighted-average margin theorem

\[
\boxed{
-\frac{D_{\Gamma_0}(G)}{W_G}
=
\sum_{v:\mathcal W_v>0}
\frac{\mu_v\mathcal W_v}{W_G}\,c_v^{\rm loc},
}
\tag{5.6}
\]

where `mu_v` is the product probability of reaching node `v`. The weights in (5.6) are nonnegative and sum to one.

Thus the required quadratic correction of an arbitrary Boolean gate is an exact weighted average of **local restriction-gluing margins**, in complete analogy with the previously proved disjoint-composition margin cocycle but along a different axis. Any gate exceeding a proposed scalar lift must contain a positive-currency restriction node whose exact local margin exceeds the same lift.

This is a genuinely different replacement mechanism: it converts the all-gate extremal problem into a local two-restriction gluing problem while retaining Boolean realizability and both information credits.

## 6. Exact adversary: dropping the KL credit fails already on a literal

The credit in (4.2) cannot be discarded. Take the unary identity `G(y)=y` at any `t in (0,1)`. Its restrictions are the two constants, so

\[
P_0=P_1=\delta_{\emptyset},\qquad
\operatorname{JS}_t(P_0,P_1)=0,
\qquad
\operatorname{It}_y=V_t.
\]

The within-pair entropy is exactly `h_2(V_t)`, hence

\[
\mathcal C_y=H(B\mid S)=h_2(t),
\qquad I(S;J)=0.
\tag{6.1}
\]

For **every** symmetric boundary-normalized potential,

\[
\boxed{
\mathcal R_{\Gamma,y}=-h_2(t)<0,
\qquad
\mathcal R_{\Gamma,y}+\mathcal C_y=0.
}
\tag{6.2}
\]

So any proposed local proof rule that throws away the branch/KL credit and demands `R>=0` is false on an actual Boolean gate at every interior bias. This is not a numerical counterexample and not a non-Boolean relaxation. The replacement (4.2) is exact and restores equality.

This adversary is compatible with the older B15 warning that local restriction payments can fail even after some refunds: the present theorem does not resurrect a credit-free selector. It changes to the all-gate normalization and keeps both exact product-bias credits.

## 7. Application to the fresh four-bit prime handoff B0

For the exact prime class

\[
A=\{0,1,2,3,4,5,8,10\}\subset Q_4,
\]

at uniform input the squared Walsh law is

\[
(1/4)^{\times2},\qquad(1/16)^{\times8},\qquad0^{\times6},
\]

so `H=3`, `I=3/2` as in the B14 handoff. The four pivots split into two exact orbits.

### Pivots 2 and 3

The two restriction spectral laws are each uniform on four atoms. Their mixture and vertical split give exactly

\[
\operatorname{It}_j=\frac12,
\qquad
\operatorname{JS}=\frac12,
\qquad
H(J\mid S)=\frac12,
\qquad
\boxed{\mathcal C_j=1}.
\tag{7.1}
\]

The restriction output biases are `3/4` and `1/4`, so the local quadratic currency is

\[
\boxed{\mathcal W_j=\frac1{16}}.
\tag{7.2}
\]

Writing `C_0=Gamma_0(1/2)`, the exact credit-retaining local base contribution is

\[
\boxed{
\mathcal R_{\Gamma_0,j}+\mathcal C_j
=\Gamma_0(1/4)-\frac12C_0-1.
}
\tag{7.3}
\]

### Pivots 0 and 1

Each restriction spectrum has masses

\[
9/16,\quad(1/16)^{\times7},
\]

while the mixture law has

\[
(5/16)^{\times2},\quad(1/16)^{\times6}.
\]

Therefore

\[
\operatorname{JS}
=\frac98\log_2 3-\frac58\log_2 5,
\tag{7.4}
\]

and the vertical conditional entropy is

\[
H(J\mid S)=\frac58 h_2(1/5)
=\frac58\log_2 5-1.
\tag{7.5}
\]

Since `It_j=1/4`, the exact total credit simplifies to

\[
\boxed{
\mathcal C_j=4-\frac{15}{8}\log_2 3
=1.028195311147832\ldots
}
\tag{7.6}
\]

The restriction output biases are `5/8` and `3/8`, and

\[
\boxed{\mathcal W_j=\frac3{64}}.
\tag{7.7}
\]

The exact local base contribution is

\[
\boxed{
\mathcal R_{\Gamma_0,j}+\mathcal C_j
=\Gamma_0(3/8)-\frac34C_0+1-\frac98\log_2 3.
}
\tag{7.8}
\]

Equations (7.3) and (7.8) are a strict normalization sharpening of the B14 handoff: the uniform root of the four-bit prime class now depends on only `Gamma_0(1/4)`, `Gamma_0(3/8)`, the centre, and explicitly preserved KL/overlap credits. The remaining all-bias problem is not claimed solved here.

## 8. Verification

`CHECK_BIASED_RESTRICTION_COCYCLE.py` is standard-library only. It uses exact `Fraction` arithmetic at square-odds product biases, so all biased basis values are rational. It:

* exhausts all 256 three-bit Boolean truth tables at three nontrivial exact product-bias vectors (768 gate/bias cases, with every pivot checked);
* verifies the coefficient-pair identities (2.1)--(2.3) exactly;
* verifies `It_j=V_t delta_j` and every nonpivot influence-mixture identity exactly;
* verifies the all-gate defect recursion for an independent symmetric boundary-normalized test potential;
* verifies the Poincare-currency recursion (5.4) exactly;
* recursively telescopes complete restriction trees and matches both the parent defect and parent currency;
* reconstructs the B0 uniform spectra and the two exact pivot orbits;
* verifies the unary-identity adversary.

The entropy/KL numerical layer is evaluated only after the exact rational mass identities have been established; no floating sign decides a theorem. Executed checker SHA-256:

`29f359e870885539e81ea914d46ff518180de6c12597a759dc7947a394af5994`.

Captured clean stdout SHA-256:

`27153359ded724be4a9d52fc19740590c6f3dc28600d2fa84fbd20fa4963af80`.

## 9. Exact movement of the proof gap

**Refuted route:** a credit-free one-coordinate all-gate remainder condition. It fails identically on every biased literal by (6.2).

**Replacement:** the exact restriction cocycle (4.2), carrying both `H(B|S)` and `I(S;J)`, together with the local Poincare currency (5.3).

**New structural reduction:** the global required scalar lift is an exact restriction-tree weighted average of local positive-currency gluing margins, equation (5.6).

**Fresh concrete target:** evaluate or interval-certify the local margin

\[
\mathcal R_{\Gamma_0,j}+\mathcal C_j+c_*\mathcal W_j
\tag{9.1}
\]

for the live successor potential on the two B0 pivot orbits and then on their lower-arity restrictions, preserving the credits rather than upper-bounding them away. More generally, a proof that (9.1) is nonnegative for every Boolean restriction pair and every interior product bias would prove the all-gate scalar-lift statement by (5.6). Conversely, any violation is an exact Boolean local adversary and identifies the two restrictions that generate it.

No publication-priority claim is made. No benchmark gold, mock data, paid/remote compute, workflow dispatch, email/Drive action, notification enabling, or unrelated private source was used.