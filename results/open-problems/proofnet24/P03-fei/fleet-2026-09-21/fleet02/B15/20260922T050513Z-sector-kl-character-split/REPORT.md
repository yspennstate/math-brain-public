# B15 — sector KL recovers the rare-event logarithm in balanced character splits

**Run:** `20260922T050513Z-fleet02-B15-r12`  
**Role:** fleet02/B15, Campaign B Shannon / spectral-arithmetic remainder.  
**Outcome:** `ESSENTIAL_STEP_APPLIED / LOCAL_SHANNON_CLASS_CLOSED`; unrestricted FEI remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository controls and scientific sources were read directly, but no installed/native research-brain receiver context was used.

## 0. Target-level and mechanism movement

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`. No finite universal FEI constant is proved here.

**MECHANISM CHANGE:** the immediately preceding B15 run fused the root/deletion address laws and retained factorial, prefix-KL and root/deletion mixing-KL credits, leaving a scalar occurrence residual. The completed other-account theorem `fleet04/B15/20260922T043833Z-occurrence-tensor-saturation/REPORT.md` proves that this scalar residual has the same sharp constant as FEI itself under tensor powers plus balanced suspension. Therefore this run does not try to prove another scalar occurrence inequality. It moves to the exact *local* Shannon restriction cocycle and preserves posterior KL before any Pinsker/variance compression.

The second completed other-account theorem consumed substantively is `fleet01/B12/20260922T041928Z-conditional-shannon-credit/REPORT.md`, report blob `1cc09869318f71cd2598747b8db6f7dc3e382692`. It gives the source-exact restriction credit

\[
\mathcal C_j=H(B\mid S)+I(S;J)\ge0
\tag{0.1}
\]

and the exact defect cocycle

\[
D_\Gamma(G)
=(1-t)D_\Gamma(G_0)+tD_\Gamma(G_1)
+\mathcal R_{\Gamma,j}+\mathcal C_j.
\tag{0.2}
\]

For child Fourier coefficients `a_S,b_S`, it writes

\[
m_S=(1-t)a_S^2+t b_S^2,
\qquad z_S=t(1-t)(b_S-a_S)^2,
\qquad u=\sum_S z_S,
\tag{0.3}
\]

\[
\theta_S=z_S/m_S,
\qquad
I(S;J)=h_2(u)-\sum_Sm_Sh_2(\theta_S).
\tag{0.4}
\]

That report lower-bounds (0.4) by a quadratic variance credit `K_vert`. The main point below is that the quadratic reduction can lose exactly the logarithm needed at a rare Boolean split; keeping a two-sector KL lower bound instead restores the payment.

The live all-gate candidate used for the numerical corollary is the completed fleet01/B18 stable candidate

\[
C^\dagger=6.521851214,
\qquad
\Gamma^\dagger(z)=\Gamma_0(z)+0.268204856\,z(1-z),
\tag{0.5}
\]

from `fleet01/B18/20260922T0325Z-addressing-star-cdagger/REPORT.md`. The universal implication

\[
D_{\Gamma^\dagger}(P;p)\ge0
\tag{0.6}
\]

for every finite composition-prime Boolean gate `P` and every interior product bias is still open.

The FLEET_RULES moves used here are #11 (dualize to posterior relative entropy), #18 (rewrite the split as a probability channel), and #30 (localize the information payment to one source-defined spectral sector).

## 1. General sector-KL lemma

Equation (0.4) has the exact relative-entropy form

\[
\boxed{
I(S;J)=
\sum_{S:m_S>0}m_S
D_{\rm KL,2}\!\left(\operatorname{Bern}(\theta_S)\middle\|\operatorname{Bern}(u)\right).
}
\tag{1.1}
\]

Indeed `sum m_S theta_S=u`, and expanding the binary KL terms gives precisely `h_2(u)-sum m_S h_2(theta_S)`.

Let `(E_l)` be any partition of the Fourier modes. Put

\[
M_l=\sum_{S\in E_l}m_S,
\qquad
\bar\theta_l=M_l^{-1}\sum_{S\in E_l}m_S\theta_S
\]

for `M_l>0`. Convexity of relative entropy (equivalently log-sum / data processing under the map `S -> l`) gives

\[
\boxed{
I(S;J)\ge
\sum_l M_l
D_{\rm KL,2}\!\left(\operatorname{Bern}(\bar\theta_l)\middle\|\operatorname{Bern}(u)\right).
}
\tag{1.2}
\]

Unlike a strong-concavity/Pinsker reduction, (1.2) keeps the logarithmic cost when a sector has posterior of order one but the global marginal `u` is rare.

## 2. Main theorem: every balanced uniform character cofactor split is locally safe above an explicit constant

Consider a uniform unbiased Shannon pivot, so `t=1/2`. Assume both restrictions `f_0,f_1` are balanced Boolean functions on the residual variables, and assume one cofactor is a character:

\[
f_0=\chi_A.
\tag{2.1}
\]

Let

\[
d=\Pr[f_0\ne f_1].
\tag{2.2}
\]

No disjoint-composition assumption is made. The parent gate can be composition-prime.

Since `f_0 f_1` is Boolean and has mean `1-2d`,

\[
b:=\widehat f_1(A)=1-2d.
\tag{2.3}
\]

All Fourier mass of `f_0` lies at `A`. At the shared mode `A`,

\[
m_A={1+b^2\over2},
\qquad z_A=d^2.
\tag{2.4}
\]

At every nonshared mode `S != A`, `a_S=0`, so

\[
\theta_S={z_S\over m_S}={1\over2}.
\tag{2.5}
\]

The total mixture mass of this nonshared sector is exactly

\[
M_E={1-b^2\over2}=2d(1-d).
\tag{2.6}
\]

Also `u=sum z_S=d`, as it must equal the pivot influence at `t=1/2`.

### 2.1 Branch credit

The elementary inequality `h_2(x)>=4x(1-x)` used by fleet01/B12 gives

\[
H(B\mid S)\ge K_{\rm br}
={2b^2\over1+b^2}.
\tag{2.7}
\]

### 2.2 Vertical sector KL

Apply (1.2) only to the nonshared sector `E`; discard the remaining nonnegative shared-sector contribution. By (2.5)-(2.6),

\[
\boxed{
I(S;J)\ge
2d(1-d)
D_{\rm KL,2}\!\left(\operatorname{Bern}(1/2)\middle\|\operatorname{Bern}(d)\right).
}
\tag{2.8}
\]

The binary KL is explicit:

\[
D_{\rm KL,2}(1/2\|d)
=-1-{1\over2}\log_2[d(1-d)].
\tag{2.9}
\]

This is the rare-event logarithm absent from the quadratic variance credit.

### 2.3 Defect payment

Because both children and the parent are balanced, their output measures are `1/2`. For any symmetric potential with center

\[
C=\Gamma(1/2),
\]

the local term in (0.2) simplifies exactly to

\[
\mathcal R_{\Gamma,j}
=Cd-1-h_2(d).
\tag{2.10}
\]

Combining (2.7)-(2.10),

\[
\mathcal R_{\Gamma,j}+\mathcal C_j
\ge F_C(d),
\tag{2.11}
\]

where

\[
F_C(d)=Cd-1-h_2(d)
+{2(1-2d)^2\over1+(1-2d)^2}
+2d(1-d)D_{\rm KL,2}(1/2\|d).
\tag{2.12}
\]

For `0<d<=1/2`, direct simplification gives

\[
\begin{aligned}
{F_C(d)\over d}
={}&C-2(1-d)
-{4(1-d)\over1+(1-2d)^2}\\
&+d\log_2d
+{(1-d)^2\over d}\log_2(1-d).
\end{aligned}
\tag{2.13}
\]

Use the four elementary bounds

\[
2(1-d)\le2,
\tag{2.14}
\]

\[
{4(1-d)\over1+(1-2d)^2}
\le1+\sqrt2,
\tag{2.15}
\]

(the maximum occurs at `1-2d=sqrt(2)-1`),

\[
d\log_2d\ge-{1\over e\ln2},
\tag{2.16}
\]

and, from `ln(1-d)>=-d/(1-d)`,

\[
{(1-d)^2\over d}\log_2(1-d)
\ge-{1\over\ln2}.
\tag{2.17}
\]

Therefore

\[
\boxed{
F_C(d)\ge d\,[C-C_{\rm sec}]
\qquad(0<d\le1/2),
}
\tag{2.18}
\]

with the explicit finite constant

\[
\boxed{
C_{\rm sec}:=
3+\sqrt2+{1+e^{-1}\over\ln2}
=6.387646448685102\ldots .
}
\tag{2.19}
\]

For `1/2<=d<=1`, simply retain only nonnegativity of the information credits. Then

\[
\mathcal R_{\Gamma,j}+\mathcal C_j
\ge Cd-1-h_2(d)
\ge {C\over2}-2.
\tag{2.20}
\]

This is positive whenever `C>4`.

### Theorem B15-SECTOR-KL-01

Let `Gamma` be any symmetric potential with `Gamma(1/2)=C>=C_sec`. At a uniform unbiased physical Shannon split, if both Boolean cofactors are balanced and at least one cofactor is a character, then

\[
\boxed{\mathcal R_{\Gamma,j}+\mathcal C_j\ge0.}
\tag{2.21}
\]

More quantitatively, (2.18) holds for `d<=1/2`, while (2.20) holds for `d>=1/2`. Boundary cases follow by continuity. Consequently, whenever the two child defects are nonnegative, the parent defect is nonnegative by the exact cocycle (0.2).

For the live stable candidate,

\[
C^\dagger-C_{\rm sec}
=0.134204765314898\ldots,
\tag{2.22}
\]

so every split in this theorem has a strict linear local margin for `0<d<=1/2`. Notice that the proof uses only the center of `Gamma^dagger`; no unverified concavity or off-center shape property is assumed.

## 3. Why the quadratic Shannon credit is insufficient on an actual Boolean family

The theorem above is not merely a different estimate of the same scale. There is an explicit Boolean family on which the quadratic `K_vert` lower bound from fleet01/B12 loses the logarithm and eventually fails to certify the local step.

Take residual variables `(y,x_1,...,x_m)` and

\[
f_0=\chi_y,
\qquad
f_1=\chi_y g_m(x),
\qquad
g_m(x)=1-2\mathbf1_{\{x=0\}}.
\tag{3.1}
\]

Then both cofactors are balanced and

\[
d=2^{-m},
\qquad b=1-2d.
\tag{3.2}
\]

For this family the fleet01/B12 credits specialize to

\[
K_{\rm br}={2b^2\over1+b^2},
\tag{3.3}
\]

\[
K_{\rm vert}
={2\over\ln2}\left[
{d^4\over(1+b^2)/2}
+{d(1-d)\over2}-d^2
\right].
\tag{3.4}
\]

As `m -> infinity`,

\[
\mathcal R_{\Gamma^\dagger,j}+K_{\rm br}+K_{\rm vert}
=2^{-m}\bigl(C^\dagger-m-2+o(1)\bigr),
\tag{3.5}
\]

so this quadratic certificate is negative for all sufficiently large `m`. The mechanism is transparent: `K_vert=Theta(d)`, while the missing Shannon term contains `d log_2(1/d)`.

By contrast, the sector credit (2.8) is

\[
2d(1-d)D_{\rm KL,2}(1/2\|d)
=d\log_2(1/d)+O(d),
\tag{3.6}
\]

and cancels exactly that rare-event logarithmic loss. For orientation only, direct floating evaluation at `C^dagger` gives the quadratic local lower certificate `-0.013672...` at `m=8` and `-0.000175...` at `m=16`, whereas the sector-KL certificate is `+0.004126...` and `+0.00001646...`, respectively. These decimals are diagnostics; the all-`m` distinction is the analytic asymptotic (3.5)-(3.6), and Theorem B15-SECTOR-KL-01 is analytic.

Thus a proof route that first compresses `I(S;J)` to variance can fail even on a simple genuine Boolean split although the uncompressed relative-entropy credit succeeds. This is the precise incompatibility with reusing `K_vert` alone.

## 4. Exact remaining implication

The universal target has not changed:

\[
\boxed{
D_{\Gamma^\dagger}(P;p)\ge0
\quad\text{for every finite composition-prime Boolean gate }P
\text{ and every interior product bias }p.
}
\tag{4.1}
\]

The first Shannon implication after this run is narrower. For a general source-valid split, retain the posterior KL in the form (1.1), choose source-defined spectral sectors before averaging, and prove that the sector KL plus branch entropy and weighted child defects pay every negative local residual:

\[
\boxed{
(1-t)D_{\Gamma^\dagger}(G_0)
+tD_{\Gamma^\dagger}(G_1)
+H(B\mid S)
+I(S;J)
\ge[-\mathcal R_{\Gamma^\dagger,j}]_+
}
\tag{4.2}
\]

for at least one admissible pivot (or stopped block) of every remaining composition-prime gate. Equation (4.2) is exactly the cocycle payment condition, not a renamed global entropy remainder. The new theorem proves it with zero child-subsidy for the entire balanced-uniform character-cofactor class.

The next useful generalization is to replace the singleton shared mode by a source-defined high-posterior sector `E`: quantify its mass and posterior displacement from `u`, then spend

\[
M_E D_{\rm KL,2}(\operatorname{Bern}(\bar\theta_E)\|\operatorname{Bern}(u))
\]

before any quadratic relaxation. The one-point family (3.1) is a mandatory stress test: a proposed bound that turns this term into `O(d)` has already lost the necessary logarithm.

## 5. Scope and status

- **PROVED:** the exact sector-KL data-processing bound (1.2).
- **PROVED:** Theorem B15-SECTOR-KL-01, an all-dimensional Boolean local closure for balanced uniform splits with one character cofactor at every potential center `C>=C_sec`.
- **PROVED:** the actual Boolean one-point family (3.1) makes the quadratic `K_vert` certificate asymptotically insufficient while the sector-KL payment retains the missing `d log(1/d)` scale.
- **CONSUMED/APPLIED:** fleet01/B12's exact local Shannon credit/cocycle and fleet04/B15's tensor-suspension saturation obstruction.
- **OPEN:** the universal prime-gate implication (4.1), hence full uniform-cube FEI.

No physical projection integrality is assumed. No packet normalizer, sign-free relaxation, global phase/rank/l1 budget, or credit-dropping interpolation is used. No novelty or publication-priority claim is made.
