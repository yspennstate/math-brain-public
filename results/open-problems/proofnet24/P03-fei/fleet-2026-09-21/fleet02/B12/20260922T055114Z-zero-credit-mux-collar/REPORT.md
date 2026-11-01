# B12 FEI — a uniform joint collar around both exact zero-credit MUX lines

**Status:** `ESSENTIAL_STEP_APPLIED / ZERO_CREDIT_MUX_COLLAR / FULL_FEI_OPEN`.

Full unrestricted uniform-cube Fourier entropy-influence remains **OPEN / NOT PROVED**. This report proves the live fixed gate candidate on a new two-parameter collar around each of the two exact zero-selector-credit lines of the one-bit unequal-data MUX. It does not prove the full MUX cube, all composition-prime gates, or FEI.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Fresh authenticated repository controls and mathematical source files were read directly; no native authenticated mathematical-brain receiver/context was used.

## 0. Live target, source version, and last-three comparison

Fresh owner control revision `2026-09-22.2` supersedes the older native B12 harmonic-row wording for substantive work and directs the FEI fleet to the all-gate inequality

\[
D_\Gamma(G;p):=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p)\ge0,
\qquad V_u=4u(1-u).
\tag{0.1}
\]

The gate-reformulation continuation proves that a finite symmetric nonnegative `Gamma` satisfying (0.1) for every Boolean gate and every product bias implies full FEI, because an arbitrary Boolean function is itself one gate on fresh variables.

The fixed candidate is
\[
C^\dagger=6.521851214,
\qquad C_0=6.4548,
\qquad a^\dagger=0.268204856,
\tag{0.2}
\]
\[
\Gamma^\dagger(u)=\Gamma_0(u)+a^\dagger u(1-u),
\tag{0.3}
\]
where `Gamma_0` is the committed h96 read-once candidate.

The last three completed own B12 mechanisms are, newest first:

1. `fleet02/B12/20260922T045519Z-complementary-mux-fourstep/REPORT.md` (report commit `59f5dee19fdaa8409b73d562588ba098168399c6`): a four-generation descendant AND bootstrap proved the entire balanced-address complementary-data MUX line.
2. `fleet02/B12/20260922T035404Z-balanced-bent-local-obstruction/REPORT.md` (blob recorded by the preceding report as `606cbb7078cb2fc76d8e749a84f2dcab4a4061ab`): a genuine bent/two-point selector refuted every finite **pointwise-local** restriction payment.
3. `fleet02/B12/20260922T025438Z-gate-margin-falsification/REPORT.md` (blob `bf37b4fd5ceae2c40e2b59266e2701fed8ff2780`): genuine Boolean gates refuted the old AND/read-once extremality mechanism.

Thus this run does not reopen pointwise-local restriction payment, global phase/rank/l1, sign-free profiles, ordinary-depth payment, or old AND extremality. It uses a different mechanism on the same live candidate: an exact MUX information identity plus a **uniform continuity budget around the rigorously identified zero-credit locus**.

## 1. Completed other-account results consumed and applied

### 1.1 fleet01/B18: exact zero-credit line with a uniform positive reserve

This run consumes substantively

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260922T052537Z-zero-credit-mux-line/REPORT.md`,
commit `c9794c46ea6b09c45e042290c99e53bec364dcdc`.

For the one-bit MUX
\[
M(a,x_0,x_1)=(1-a)x_0+a x_1,
\]
that report combines the exact selector-credit collapse with the live h96 source and proves, for
\[
Z(s):=C^\dagger-2+\frac12\Gamma^\dagger(s)
-\Gamma^\dagger\!\left(\frac14+\frac{s}{2}\right),
\tag{1.1}
\]
that
\[
Z(s)>0\qquad(0\le s\le1).
\]
More importantly for the present quantitative collar, its proof has a **uniform source-bound reserve**. On `0<=s<=1/50`, the certified lower comparison is increasing from
\[
Z(0)=0.0167628035\ldots,
\]
while the next two branches have displayed lower bounds `>0.0479544` and `>0.26545`; symmetry covers `s>=1/2`. Hence the completed theorem implies the deliberately weakened rational floor
\[
\boxed{Z(s)>{1\over64}\qquad(0\le s\le1).}
\tag{1.2}
\]
This is not inferred from a grid; it is a direct weakening of that report's analytic/source-segment proof.

### 1.2 fleet04/B18 and fleet01/B15: exact Boolean six-mass / negative-credit formulas

I also use the completed actual-Boolean MUX identities in

`fleet04/B18/20260922T045533Z-mux-joint-credit-collapse/REPORT.md`

and the compatible exact negative-posterior-credit derivation in

`fleet01/B15/20260922T050419Z-mux-negative-posterior-credit/REPORT.md`,
commit `9ff5ab66db321bb07f8c0667f702b2c15f97fe67`.

For independent biases
\[
\Pr(a=1)=t,
\qquad \Pr(x_0=1)=q_0,
\qquad \Pr(x_1=1)=q_1,
\qquad r=(1-t)q_0+tq_1,
\]
the six exact squared biased-Walsh masses are
\[
\boxed{
\begin{aligned}
w_\varnothing&=(1-2r)^2,\\
w_a&=V_t(q_1-q_0)^2,\\
w_0&=(1-t)^2V_{q_0},\\
w_1&=t^2V_{q_1},\\
w_{a0}&=t(1-t)V_{q_0},\\
w_{a1}&=t(1-t)V_{q_1}.
\end{aligned}}
\tag{1.3}
\]
They are the actual Boolean spectrum; no arbitrary spectral-law relaxation is introduced. The normalized influence prices are
\[
{\operatorname{It}_a\over V_t}=d:=q_0+q_1-2q_0q_1,
\qquad
{\operatorname{It}_0\over V_{q_0}}=1-t,
\qquad
{\operatorname{It}_1\over V_{q_1}}=t.
\tag{1.4}
\]
Writing
\[
B(u):=\Gamma^\dagger(u)+h_2(V_u),
\]
we therefore have the exact source-valid slack formula
\[
\boxed{
D_{\Gamma^\dagger}(M;t,q_0,q_1)
=dB(t)+(1-t)B(q_0)+tB(q_1)
-\Gamma^\dagger(r)-H(w).}
\tag{1.5}
\]
The fleet01/B15 report independently derives the same formula through the exact negative posterior-entropy credit. Thus the continuity argument below does not discard the negative information term: it perturbs the **whole actual six-point Shannon law**.

## 2. Source bounds used in the collar

For `v=min(u,1-u)<=1/2`, the completed h96 source envelope used by the peer reports is
\[
\Gamma^\dagger(u)
\le v\left(4.9096\log_2{1\over v}+8.629\right)
+a^\dagger v(1-v).
\tag{2.1}
\]
Since
\[
\max_{0<v\le1/2}v\log_2(1/v)={1\over e\ln2}<0.531,
\]
(2.1), `h_2(V_u)<=1`, and `a^dagger/4<0.068` give the convenient global bound
\[
\boxed{B(u)<8\qquad(0\le u\le1).}
\tag{2.2}
\]
Indeed the right side for `Gamma^dagger` is below
\[
4.9096(0.531)+{8.629\over2}+{0.268204856\over4}
=6.988548814<7.
\]

The same source records `|G'(x)|<31` for `Gamma_0(u)=uG(log_2(1/u))`. Hence, using `1/ln2<3/2`,
\[
|({\Gamma^\dagger})'(u)|
<4.9096x+8.629+{93\over2}+0.269.
\tag{2.3}
\]
Throughout the center collar below, `x<1.001`; throughout the perturbed output interval, whose symmetric representative stays above `1/4-2^-15-2^-30`, `x<2.001`. Thus
\[
\boxed{|({\Gamma^\dagger})'(u)|<66}
\tag{2.4}
\]
for every potential evaluation that moves in the proof.

## 3. New theorem: a uniform two-parameter collar around a zero-credit line

Put
\[
\eta:=2^{-15}={1\over32768}.
\tag{3.1}
\]
Fix arbitrary `s in [0,1]` and perturb the first zero-credit line by
\[
t={1\over2}+\tau,
\qquad
q_0={1\over2}+\varepsilon,
\qquad
q_1=s,
\qquad
|\tau|,|\varepsilon|\le\eta.
\tag{3.2}
\]
Let `D` be the slack (1.5), and let `D_0=Z(s)` be its value at `tau=epsilon=0`. We prove
\[
|D-D_0|<{1\over128}.
\tag{3.3}
\]
Together with (1.2), this will leave another `1/128` of reserve.

Write
\[
E=|\varepsilon|,
\qquad T=|\tau|.
\]
At the base point, `d_0=1/2` and `r_0=1/4+s/2`. The elementary variations are
\[
|d-d_0|\le E,
\tag{3.4}
\]
\[
|r-r_0|\le {E\over2}+{T\over2}+ET.
\tag{3.5}
\]
Also
\[
h_2(V_{1/2+x})=h_2(4x^2).
\tag{3.6}
\]
From (2.2)-(2.4), the four non-Shannon terms in (1.5) obey the following deliberately coarse bounds:
\[
\left|dB(t)-{C^\dagger\over2}\right|
\le 8E+33T+{1\over2}h_2(4T^2),
\tag{3.7}
\]
\[
\left|(1-t)B(q_0)-{C^\dagger\over2}\right|
\le36E+7T+h_2(4E^2),
\tag{3.8}
\]
where `(1/2+T)<17/32` and `C^dagger<7` were used,
\[
\left|tB(s)-{B(s)\over2}\right|<8T,
\tag{3.9}
\]
and, by (3.5),
\[
|\Gamma^\dagger(r)-\Gamma^\dagger(r_0)|
<34(E+T).
\tag{3.10}
\]
(The tiny `66ET` term is absorbed because `E,T<=2^-15`.) Summing (3.7)-(3.10) gives
\[
\boxed{
\text{non-Shannon change}
<78E+82T+{3\over2}h_2(4\eta^2)
\le160\eta+{3\over2}h_2(2^{-28}).}
\tag{3.11}
\]

## 4. Exact six-mass perturbation and Fannes payment

It remains to perturb `H(w)` without dropping any selector information credit. For the six weights in (1.3), direct algebra gives
\[
\begin{aligned}
|\Delta w_\varnothing|&\le2E+2T+4ET,\\
|\Delta w_a|&\le E+E^2+{17\over16}T^2,\\
|\Delta w_0|&\le T+T^2+{17\over16}E^2,\\
|\Delta w_1|&\le T+T^2,\\
|\Delta w_{a0}|&\le E^2+T^2,\\
|\Delta w_{a1}|&\le T^2.
\end{aligned}
\tag{4.1}
\]
Here only `|s-1/2|<=1/2` and `E,T<=1/64` are used. Therefore
\[
\|w-w^0\|_1
\le3E+4T+4ET+{49\over16}E^2+{81\over16}T^2.
\tag{4.2}
\]
For `E,T<=1/64`,
\[
4ET\le{E+T\over32},
\qquad
{49\over16}E^2\le{49\over1024}E,
\qquad
{81\over16}T^2\le{81\over1024}T,
\]
so
\[
\boxed{\|w-w^0\|_1<5(E+T).}
\tag{4.3}
\]
Thus the total-variation distance is
\[
\delta_{\rm TV}<{5\over2}(E+T)\le5\eta={5\over32768}.
\tag{4.4}
\]

Fannes--Audenaert on a six-point alphabet gives
\[
|H(w)-H(w^0)|
\le h_2(\delta_{\rm TV})+\delta_{\rm TV}\log_2 5.
\tag{4.5}
\]
Using `h_2(x)<=x log_2(e/x)` and monotonicity of `x log(K/x)` in this range,
\[
\begin{aligned}
|H(w)-H(w^0)|
&<{5\over32768}
\log_2\!\left({5e\over5/32768}\right)\\
&={5\over32768}(15+\log_2e)\\
&<{165\over65536}.
\end{aligned}
\tag{4.6}
\]
The cancellation of the factor five in the logarithm is why the collar can be kept at a transparent dyadic width.

Finally, since `4 eta^2=2^-28`,
\[
h_2(2^{-28})
\le2^{-28}(28+\log_2e)
<{59\over2^{29}},
\]
so
\[
{3\over2}h_2(2^{-28})<2^{-22}.
\tag{4.7}
\]
Combining (3.11), (4.6), and (4.7),
\[
\boxed{
|D-D_0|
<{160\over32768}+{165\over65536}+2^{-22}
={31041\over4194304}
=0.0074007511\ldots<{1\over128}.}
\tag{4.8}
\]

### Theorem 4.1 — uniform joint zero-credit collar

For the fixed live source candidate `Gamma^dagger`, every one-bit MUX satisfying
\[
\boxed{
\left|t-{1\over2}\right|\le2^{-15},
\qquad
\left|q_0-{1\over2}\right|\le2^{-15},
\qquad
0\le q_1\le1}
\tag{4.9}
\]
has
\[
\boxed{
D_{\Gamma^\dagger}(M;t,q_0,q_1)>{1\over128}>0.}
\tag{4.10}
\]
Indeed (1.2) and (4.8) give
\[
D>{1\over64}-{31041\over4194304}
={34495\over4194304}
>{1\over128}.
\]
By exchanging the two data labels and replacing `t` by `1-t`, the symmetric collar also holds whenever
\[
\boxed{
\left|t-{1\over2}\right|\le2^{-15},
\qquad
\left|q_1-{1\over2}\right|\le2^{-15},
\qquad
0\le q_0\le1.}
\tag{4.11}
\]
Boundary values follow by continuity.

This is a genuinely two-parameter neighborhood of the **entire** exact zero-credit locus, not a sampled finite grid and not a collar whose width shrinks with the remaining data bias.

## 5. Integration and remaining implication

The newest fleet01/B18 report explicitly left the next task: extend positivity from the exact zero-selector-credit lines to a quantitative collar, then attack the compact region separated from those lines. Theorem 4.1 completes that first task for the live candidate with the uniform dyadic width `2^-15` and reserve `1/128`.

It is complementary to fleet04/B18's newer tube around the **complementary-data** locus, which permits a small simultaneous address/data perturbation. Neither theorem contains the other: the present collar allows the other data bias to be completely arbitrary, while requiring one data bias and the address bias to stay close to `1/2`.

The first unproved MUX implication is now the compact remainder after removing:

* both zero-credit collars (4.9), (4.11);
* the already-proved complementary-data balanced-address line and its current joint tube;
* the previously proved common-data addressing family.

A full MUX closure still needs either a positive lower bound on the exact selector information credit strong enough to dominate the potential midpoint deficit on that compact remainder, or an exact Boolean counterexample to `Gamma^dagger` there. Even full MUX closure would still leave arbitrary composition-prime gates.

## 6. FULL-PROBLEM CHANGE / MECHANISM CHANGE

**FULL-PROBLEM CHANGE:** **none.** No universal FEI upper bound has been proved. The live all-gate candidate is established on one additional infinite three-parameter region only.

**MECHANISM CHANGE:** **yes.** The preceding own B12 run paid the complementary MUX midline by a four-generation descendant AND bootstrap. This run instead imports the exact zero-credit rigidity and its uniform line reserve, keeps the full six-atom Boolean Shannon law intact, and pays a simultaneous two-parameter perturbation by a nonreusing total-variation/price budget. The exact old missing implication “prove a collar around the zero-credit lines” is now proved at width `2^-15`; the quantified new implication is positivity on the compact MUX remainder described above.

## 7. Verification and source scope

The adjacent `check_zero_credit_mux_collar.py` verifies the new rational budget, the six-mass `l1` coefficient bounds, the derivative-envelope diagnostics, and the final strict reserve. It intentionally does **not** regenerate the binary h96 candidate. The source-dependent premises are exactly the completed peer theorem (1.2), the committed h96 envelope/slope bounds (2.1)-(2.4), and the exact Boolean MUX identities (1.3)-(1.5).

All changed scientific files for this run were reviewed for scope/privacy: they contain only FEI mathematics, public-style constants already present in the private research repository, source paths/commits, and deterministic verification output; no credentials, scheduler identifiers, machine paths, raw transcripts, benchmark gold, email, Drive data, or unrelated private material are included.
