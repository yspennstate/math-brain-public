# fleet04/B13 — thicken the balanced MUX center-crossing collar into a genuine 3D selector tube

**Classification:** `ESSENTIAL_STEP_APPLIED / PRIME_GATE_LOCALIZATION / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Novelty/priority:** unverified; no publication-priority claim.

## 0. What changed

The live owner control now asks the FEI fleet to converge on the source-exact all-gate formulation. This run therefore does not reopen the retired ordinary-depth or cube-measure-times-dimension routes. It preserves fleet04/B18's exact mixed-curvature conservation and zero-defect classification unchanged.

The live candidate is
\[
C^\dagger=6.521851214,\qquad C_0=6.4548,
\qquad a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(z)=\Gamma_0(z)+a^\dagger z(1-z).
\]
The source-current all-gate reduction asks for
\[
D_{\Gamma^\dagger}(G;p)\ge0
\]
for every composition-prime Boolean gate and every interior product bias. That universal statement remains open.

This run proves a new robust region for the composition-prime one-address-bit MUX. The previous balanced-address collar is not merely a two-dimensional accident: its entire center-crossing sector survives a nonzero selector-bias perturbation, with an explicit strictly positive defect reserve.

## 1. Newest compatible other-account result consumed

The newest compatible other-account result consumed is

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B14/20260922T060632Z-zero-credit-3d-tube/REPORT.md`

read at immutable repository commit

`1e2e9b9e87a3887d3056675441577b402ad49929`,

report blob

`202aed29e7af82ced5d99cc53def5b80f8451e8f`.

It supplies the exact source-valid six-mass biased-Walsh law for
\[
M(A;D_0,D_1)=\begin{cases}D_0,&A=0,\\D_1,&A=1,\end{cases}
\]
with independent biases
\[
t=\Pr(A=1),\quad q_0=\Pr(D_0=1),\quad q_1=\Pr(D_1=1),
\]
and proves a three-dimensional tube around the exact zero-credit lines. In its notation, with `q=1-t`,
\[
r=qq_0+tq_1,
\qquad d=q_0+q_1-2q_0q_1,
\]
\[
B(z)=\Gamma^\dagger(z)+h_2(V_z),\qquad V_z=4z(1-z),
\]
the defect is exactly
\[
D_{\Gamma^\dagger}(M)
=dB(t)+qB(q_0)+tB(q_1)-\Gamma^\dagger(r)-H(w),
\tag{1.1}
\]
where
\[
\begin{aligned}
w_\varnothing&=(1-2r)^2,\\
w_A&=V_t(q_1-q_0)^2,\\
w_0&=q^2V_{q_0},\qquad w_1=t^2V_{q_1},\\
w_{A0}&=tqV_{q_0},\qquad w_{A1}=tqV_{q_1}.
\end{aligned}
\tag{1.2}
\]
It also gives the source bounds used below:

* if `|z-1/2|<=2^-14`, then `|Gamma^dagger(z)-C^dagger|<60|z-1/2|`;
* globally `0<=B(z)<9`;
* on the source interval needed below, `Gamma^dagger` has a uniform derivative bound obtained from `G(1)=12.9096`, `|G'|<31`, and `1/ln 2 < 10^7/6931471`.

This result changes the argument here in an essential way: instead of applying a generic continuity bound to an abstract gate law, we perturb the **actual six source masses** in (1.2), so the entropy movement is paid by the exact total-variation change of one Boolean MUX source.

The balanced base reserve being thickened is the newer fleet01/B18 result

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260922T055608Z-balanced-mux-collar-sharpen/REPORT.md`,

commit `9e3563d95cb9583329e5011ff281a4e1cdc41be9`, report blob `411fe1c905f9051b7d2dfb9c2c337c0b13bfbb69`.

Write
\[
u=1-q_0-q_1,\qquad v=q_1-q_0.
\tag{1.3}
\]
Its center-crossing theorem proves at `t=1/2` that
\[
|u|<|v|,\qquad |v|\le\frac{1-|u|}{112}
\tag{1.4}
\]
implies
\[
D_{\Gamma^\dagger}(M;1/2,q_0,q_1)>r_*,
\tag{1.5}
\]
where its explicit rational reserve is
\[
r_*:=
\frac{1263249027205352299031}
{111301937434057664000000000}
=1.134974876743526\ldots\times10^{-5}.
\tag{1.6}
\]

## 2. Geometry of the center-crossing sector

From (1.4),
\[
|u|<\frac1{113},\qquad |v|\le\frac1{112}.
\tag{2.1}
\]
Indeed `112|u|<112|v|<=1-|u|`.
Hence
\[
q_0=\frac{1-u-v}{2},\qquad q_1=\frac{1-u+v}{2}
\tag{2.2}
\]
lie in a fixed small neighbourhood of `1/2`.

Let
\[
t=\frac12+\tau,\qquad \eta:=2^{-24},\qquad |\tau|\le\eta.
\tag{2.3}
\]
At the balanced address set
\[
r_0=\frac{q_0+q_1}{2}=\frac{1-u}{2}.
\]
Then
\[
r=r_0+\tau v.
\tag{2.4}
\]
By (2.1), every `r` in (2.4) has its symmetric small representative at least
\[
\frac12-\frac1{226}-\frac{\eta}{112}.
\]
Writing that representative as `(1-y)/2`, one has `y<1/112`. Thus
\[
\log_2(1/z)-1
=\frac{-\ln(1-y)}{\ln2}
<\frac{1}{111}\frac{10^7}{6931471}<0.0131.
\]
Using the same source identity as the consumed B14 report,
\[
\Gamma_0'(z)=G(x)-\frac{G'(x)}{\ln2},
\]
with `G(1)=12.9096`, `|G'|<31`, and the quadratic lift derivative bounded by `a^dagger`, gives the convenient uniform bound
\[
\boxed{|(\Gamma^\dagger)'(z)|<59}
\tag{2.5}
\]
throughout the output interval (2.4).

Also, since `eta<2^-14`, the consumed center bound gives
\[
\Gamma^\dagger(t)\ge C^\dagger-60\eta.
\tag{2.6}
\]

## 3. Exact six-mass stability

Let `w(\tau)` denote (1.2) and `w^0=w(0)`. Substituting (1.3) gives the exact forms
\[
\begin{aligned}
w_\varnothing(\tau)&=(u-2\tau v)^2,\\
w_A(\tau)&=(1-4\tau^2)v^2,\\
w_0(\tau)&=(\tfrac12-\tau)^2V_{q_0},\\
w_1(\tau)&=(\tfrac12+\tau)^2V_{q_1},\\
w_{A0}(\tau)&=(\tfrac14-\tau^2)V_{q_0},\\
w_{A1}(\tau)&=(\tfrac14-\tau^2)V_{q_1}.
\end{aligned}
\tag{3.1}
\]
Therefore
\[
\begin{aligned}
\|w(\tau)-w^0\|_1
&\le 2\eta+4|uv|\eta+4\eta^2+8v^2\eta^2\\
&<2.002\eta,
\end{aligned}
\tag{3.2}
\]
where (2.1) was used in the last line. Hence the total variation satisfies
\[
\theta:=\frac12\|w(\tau)-w^0\|_1<1.001\eta.
\tag{3.3}
\]

Fannes--Audenaert on the six-point alphabet gives
\[
|H(w(\tau))-H(w^0)|
\le h_2(\theta)+\theta\log_2 5
\le\theta\log_2\frac{5e}{\theta}.
\tag{3.4}
\]
For `0<theta<=1.001 eta`, the right-hand side is increasing. Since `e<3` and
\[
15\,2^{24}<2^{28},
\]
we obtain the explicit bound
\[
\boxed{|H(w(\tau))-H(w^0)|<28.028\eta.}
\tag{3.5}
\]

This is where the source-exact six-mass law is crucial: no ambient-dimension continuity factor appears.

## 4. Main theorem: the balanced center-crossing collar has positive 3D thickness

### Theorem 4.1
For every interior MUX bias triple satisfying
\[
\boxed{
|u|<|v|,
\qquad
|v|\le\frac{1-|u|}{112},
\qquad
\left|t-\frac12\right|\le2^{-24},
}
\tag{4.1}
\]
with `u=1-q0-q1`, `v=q1-q0`, one has
\[
\boxed{D_{\Gamma^\dagger}(M;t,q_0,q_1)>\frac1{200000}>0.}
\tag{4.2}
\]

### Proof
Compare (1.1) at `t=1/2+tau` with `t=1/2`.

First, `0<=d<=1`, `h_2(V_t)>=0`, and (2.6) imply
\[
dB(t)\ge dB(1/2)-60\eta.
\tag{4.3}
\]

Second,
\[
(1-t)B(q_0)+tB(q_1)
=\frac12B(q_0)+\frac12B(q_1)
+\tau\bigl(B(q_1)-B(q_0)\bigr).
\]
Since the consumed B14 source bound gives `0<=B<9`,
\[
(1-t)B(q_0)+tB(q_1)
\ge\frac12B(q_0)+\frac12B(q_1)-9\eta.
\tag{4.4}
\]

Third, (2.4), (2.5), and `|v|<=1/112` give
\[
-\Gamma^\dagger(r)
\ge-\Gamma^\dagger(r_0)-\frac{59}{112}\eta.
\tag{4.5}
\]

Finally, (3.5) gives
\[
-H(w(\tau))\ge-H(w^0)-28.028\eta.
\tag{4.6}
\]

Combining (4.3)--(4.6) with the balanced reserve (1.5),
\[
\begin{aligned}
D_{\Gamma^\dagger}(M;t,q_0,q_1)
&>r_*-\left(60+9+\frac{59}{112}+28.028\right)\eta\\
&>r_*-97.564\,2^{-24}\\
&>5.53\times10^{-6}\\
&>\frac1{200000}.
\end{aligned}
\]
This proves (4.2). `square`

## 5. Influence-relative interpretation and relation to prior tubes

The normalized address influence of MUX is exactly the child disagreement
\[
\frac{\operatorname{It}_A}{V_t}=d
=q_0+q_1-2q_0q_1
=\frac{1-u^2+v^2}{2}.
\tag{5.1}
\]
Throughout (4.1),
\[
d>\frac12\left(1-\frac1{113^2}\right)
=0.4999608426\ldots .
\tag{5.2}
\]
Thus Theorem 4.1 excludes a whole near-balanced-address region with normalized selector influence essentially one half; it is not a small-cube-measure-times-dimension estimate.

The new region is genuinely different from fleet02/B14's zero-credit-line tube. B14 requires, near `t=1/2`, that at least one data bias lie within `2^-14` of `1/2`. Here the center-crossing data sector allows
\[
|q_i-1/2|
\le\frac12\left(\frac1{113}+\frac1{112}\right)
\approx 8.89\times10^{-3},
\]
while both data biases may be far outside the `2^-14` line tube. The selector thickness is smaller, `2^-24`, because it is paid from the small but uniform reserve of the sharpened balanced collar.

Equivalently, any MUX counterexample lying in the data collar
\[
|u|<|v|,\qquad |v|\le(1-|u|)/112
\]
must satisfy
\[
\boxed{|t-1/2|>2^{-24}.}
\tag{5.3}
\]
This is a source-exact prime-gate localization, not a claim that MUX positivity is complete.

## 6. Preserved interface-B facts and remaining gap

Nothing here alters fleet04/B18's mixed-curvature law
\[
\kappa_{ik}=\kappa_{ki}=p_{ik}+4o_{ik},
\qquad
\sum_{i\ne k}(p_{ik}+4o_{ik})=4d_k,
\]
including the opposite-sign term, nor its exact zero-depth classification by a character-twisted signed one-point defect. In particular, this run does **not** replace the unpaid `sum d_k` second-factorial moment by `O(J)`, and does not use a cube-measure error multiplied by ambient dimension.

Full FEI remains open. For the MUX prime family, the next useful step is to continue this source-exact thickening into the remaining unequal-data interior, or to produce a genuine MUX violation. For the universal theorem, positivity for one prime family is only a localization aid; every composition-prime gate still has to be covered (or a counterexample found).
