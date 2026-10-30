# B15 — every five-input gate is safe in an explicit full bias neighborhood of the uniform point

**Classification:** `ESSENTIAL_STEP_APPLIED / ARITY5_FULL-CENTER-TUBE-CLOSED`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Version/change summary

The current live owner order asks every FEI worker to converge on the all-gate formulation.  Accordingly this run does not reopen the older arithmetic-packet residual.  It binds to the current fixed all-gate candidate from

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260922T0325Z-addressing-star-cdagger/REPORT.md`

with

\[
C^\dagger=6.521851214,\qquad C_0=6.4548,
\qquad a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(u)=\Gamma_0(u)+a^\dagger u(1-u).
\tag{0.1}
\]

The universal missing implication remains

\[
D_{\Gamma^\dagger}(P;p)\ge0
\quad\text{for every finite composition-prime Boolean gate }P
\text{ and every interior product bias }p.
\tag{0.2}
\]

This run proves a new open neighborhood of that statement: **every** Boolean gate on five inputs, prime or decomposable, satisfies (0.2) whenever every input bias is within `10^-7` of `1/2`.

The principal other-account theorem consumed is fleet01/B17,

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B17/20260922T043923Z-arity5-uniform-c001/REPORT.md`

(observed report blob `daca0767157595c2c2ac7d9da4a58fe86132ffe4`).  It proves for **all** five-input Boolean gates at the exact uniform bias vector

\[
D_{\Gamma_{.01}}(G;1/2^5)\ge0,
\qquad
\Gamma_{.01}(u)=\Gamma_0(u)+0.01u(1-u).
\tag{0.3}
\]

A second compatible peer input is fleet01/B18,

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260922T050337Z-complementary-mux-address-tube/REPORT.md`

(observed report blob `ce379eac385c9f388d2a72f5c10f3a0f6611fca9`).  It extracts from the h96 source diagnostics the deliberately weakened global transformed-slope fact

\[
|G'(x)|<31,
\tag{0.4}
\]

for the source function `Gamma_0(2^-x)=2^-x G(x)`.  The original source output also records

\[
G(x)-4.9096x\le 8.62812,
\tag{0.5}
\]

and `Gamma_0>=0`; because the source interpolates `G` linearly in `x` and uses the same tail slope, (0.5) holds between nodes as well.

## 1. Gate defect and the exact center reserve

For a Boolean gate `G` at product bias `p`, write

\[
D_\Gamma(G;p)=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
       \bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\tag{1.1}
\]

At the uniform vector `u=(1/2,...,1/2)` define

\[
W_G(u)={I(G)\over4}-p_{\rm out}(1-p_{\rm out}).
\tag{1.2}
\]

If `m` is the number of negative truth-table values and `B` is the undirected edge boundary of that set in `Q_5`, then

\[
I(G)={B\over16},\qquad p_{\rm out}={m\over32},
\]
so

\[
\boxed{
W_G(u)={16B-m(32-m)\over1024}.
}
\tag{1.3}
\]

Poincare gives `W_G(u)>=0`.  The numerator in (1.3) is an integer.  Moreover

\[
4W_G(u)=I(G)-4p_{\rm out}(1-p_{\rm out})
=\sum_{|S|\ge2}(|S|-1)\widehat G(S)^2.
\tag{1.4}
\]

Hence `W_G(u)=0` iff the uniform Fourier degree is at most one.  A Boolean function of Fourier degree at most one is a constant or a signed dictator: from `G^2=1`, the coefficient of `chi_i chi_j` gives `a_i a_j=0`, so at most one linear coefficient is nonzero, and then the coefficient of `chi_i` gives `a_0a_i=0`.  Therefore every five-input Boolean gate that is neither constant nor signed dictator obeys the discrete gap

\[
\boxed{W_G(u)\ge{1\over1024}.}
\tag{1.5}
\]

Changing a scalar quadratic lift by `delta c` changes the gate defect by exactly `delta c W_G`.  Combining the peer theorem (0.3) with (1.5), for every nonconstant nondictator,

\[
\begin{aligned}
D_{\Gamma^\dagger}(G;u)
&=D_{\Gamma_{.01}}(G;u)
 +(a^\dagger-0.01)W_G(u)\\
&\ge {0.268204856-0.01\over1024}\\
&=\boxed{0.0002521531796875}.
\end{aligned}
\tag{1.6}
\]

Thus the exact central finite theorem has a uniform strictly positive reserve after moving to the live `Gamma^dagger` candidate.  Constants and signed dictators are exact all-bias base cases and will be separated below.

## 2. A source-valid Lipschitz bound for `Gamma^dagger` on every relevant output interval

Fix

\[
\varepsilon=10^{-7},
\qquad \|p-u\|_\infty\le\varepsilon.
\tag{2.1}
\]

For a nonconstant five-bit gate the uniform output mass is `m/32` with `1<=m<=31`.  Product-measure total variation gives

\[
|p_{\rm out}(p)-p_{\rm out}(u)|\le5\varepsilon.
\tag{2.2}
\]

Therefore the smaller representative

\[
r=\min(p_{\rm out},1-p_{\rm out})
\]

satisfies

\[
r>{1\over32}-5\cdot10^{-7}>{1\over64}.
\tag{2.3}
\]

Write `r=2^-x`.  Then `1<=x<6`.  From (0.5),

\[
0\le G(x)\le4.9096\cdot6+8.62812<38.086.
\tag{2.4}
\]

For the lifted potential write

\[
\Gamma^\dagger(r)=rG^\dagger(x),
\qquad
G^\dagger(x)=G(x)+a^\dagger(1-r).
\]

Using (0.4), `a^dagger<0.269`, `ln2<0.7`, and `r<=1/2`,

\[
|G^\dagger(x)|<38.355,
\qquad
|(G^\dagger)'(x)|
<31+{0.269\cdot0.7\over2}<31.095.
\tag{2.5}
\]

Since `1/ln2<3/2`,

\[
\left|{d\over dr}\Gamma^\dagger(r)\right|
=\left|G^\dagger(x)-{(G^\dagger)'(x)\over\ln2}\right|
<38.355+{3\over2}(31.095)<85.
\tag{2.6}
\]

By symmetry the same bound holds on the large side.  Thus every output value appearing in (2.2), and every input bias in (2.1), lies in a region where

\[
\boxed{|(\Gamma^\dagger)'|<85.}
\tag{2.7}
\]

This is the only potential regularity used below.

## 3. Influence-price variation

Set

\[
\alpha_i(p)={\operatorname{It}_i(G;p)\over V_{p_i}}.
\]

For a Boolean gate `alpha_i(p)` is exactly the pivotal probability of coordinate `i` under the product law on the other four inputs, hence

\[
0\le\alpha_i\le1,
\qquad
|\alpha_i(p)-\alpha_i(u)|\le4\varepsilon.
\tag{3.1}
\]

Put

\[
A(t)=\Gamma^\dagger(t)+h_2(V_t).
\]

Inside the input tube, (2.7) and `h_2<=1` give `A(t)<8`.  Also, with `delta=t-1/2`,

\[
V_t=1-4\delta^2,
\qquad
h_2(V_t)=h_2(4\delta^2).
\]

For `0<z<=1/2`, `h_2(z)<=z log_2(e/z)`, so at `|delta|<=10^-7`,

\[
h_2(4\delta^2)<2\times10^{-12}.
\tag{3.2}
\]

Since `A(1/2)=C^dagger`, equations (2.7), (3.1), and (3.2) yield

\[
\begin{aligned}
&\left|
\sum_{i=1}^5\alpha_i(p)A(p_i)
-
\sum_{i=1}^5\alpha_i(u)A(1/2)
\right|\\
&\qquad\le
5\left[4\varepsilon\cdot8+85\varepsilon+2\times10^{-12}\right]\\
&\qquad<\boxed{5.850001\times10^{-5}}.
\end{aligned}
\tag{3.3}
\]

The output-potential variation is independently

\[
|\Gamma^\dagger(p_{\rm out}(p))
-
\Gamma^\dagger(p_{\rm out}(u))|
\le85\cdot5\varepsilon
=\boxed{4.25\times10^{-5}}.
\tag{3.4}
\]

## 4. Uniform continuity of the actual biased spectral entropy

The remaining issue is not an arbitrary probability law: it is the **actual biased Fourier spectrum** of the same Boolean truth table.  For one biased bit define the orthogonal matrix

\[
B(t)=
\begin{pmatrix}
\sqrt{1-t}&-\sqrt t\\
\sqrt t&\sqrt{1-t}
\end{pmatrix}.
\tag{4.1}
\]

Let

\[
U(p)=\bigotimes_{i=1}^5 B(p_i),
\]

and let `F` be the diagonal matrix of the `+-1` truth table.  The vector of biased Fourier coefficients is exactly

\[
a(p)=U(p)^T F U(p)e_\varnothing.
\tag{4.2}
\]

If `theta(t)=arcsin sqrt(t)`, then `B(t)` is a planar rotation and

\[
|\theta'(t)|={1\over2\sqrt{t(1-t)}}\le{2\over\sqrt3}
\]

on `[1/4,3/4]`.  Hence, using tensor telescoping,

\[
\|U(p)-U(u)\|_{op}
\le {10\over\sqrt3}\varepsilon.
\tag{4.3}
\]

Since `F` and both `U`'s are orthogonal/isometric,

\[
\|a(p)-a(u)\|_2
\le2\|U(p)-U(u)\|_{op}
\le{20\over\sqrt3}\varepsilon.
\tag{4.4}
\]

The spectral mass vectors are `w_S=a_S^2`, so Parseval and Cauchy--Schwarz give

\[
\|w(p)-w(u)\|_1
\le\|a(p)-a(u)\|_2\|a(p)+a(u)\|_2
\le{40\over\sqrt3}\varepsilon.
\tag{4.5}
\]

Thus their total variation distance obeys

\[
\tau\le{20\over\sqrt3}\varepsilon<12\varepsilon=1.2\times10^{-6}.
\tag{4.6}
\]

Fannes--Audenaert on the 32 Fourier atoms gives

\[
|\widetilde H_G(p)-H(G)|
\le h_2(\tau)+\tau\log_2 31.
\]

Using again `h_2(z)<=z log_2(e/z)` and `log_2 31<5`, the right side is less than

\[
\boxed{3.2\times10^{-5}}.
\tag{4.7}
\]

This step keeps the genuine Boolean biased spectrum throughout; no non-Boolean relaxation or automatic packet-integrality assumption enters.

## 5. The arity-five full-center tube theorem

Combining (3.3), (3.4), and (4.7), the total possible decrease of the live gate defect from its uniform value is less than

\[
0.00005850001+0.0000425+0.000032
<0.000133001.
\tag{5.1}
\]

The adjacent checker uses the slightly sharper displayed entropy arithmetic and obtains

\[
\text{total cost}<0.000132333484235193.
\tag{5.2}
\]

Subtracting from the exact center reserve (1.6) yields

\[
D_{\Gamma^\dagger}(G;p)
>
0.000119819695452307
>0
\tag{5.3}
\]

for every five-input Boolean gate that is neither constant nor signed dictator and every bias vector satisfying (2.1).  Constants and signed dictators satisfy the all-gate identity exactly for every bias (dummy coordinates contribute zero), so they are already covered.

Therefore:

### Theorem 5.1 — all five-input gates in a full product-bias tube

For every Boolean gate

\[
G:\{0,1\}^5\to\{-1,+1\}
\]

and every interior product-bias vector `p` satisfying

\[
\boxed{
\max_i|p_i-1/2|\le10^{-7},
}
\tag{5.4}
\]

the current candidate obeys

\[
\boxed{D_{\Gamma^\dagger}(G;p)\ge0.}
\tag{5.5}
\]

For every gate with positive Poincare denominator

\[
W_G(p)={1\over4}\sum_i\operatorname{It}_i(G;p)
-p_{\rm out}(1-p_{\rm out})>0,
\]
this can be expressed in the owner-requested comparable margin as

\[
c_G(p)=-{D_{\Gamma_0}(G;p)\over W_G(p)}
=a^\dagger-{D_{\Gamma^\dagger}(G;p)\over W_G(p)}.
\]

Since `sum_i It_i<=5`, `W_G<=5/4`.  Using (5.3), every nontrivial gate in the tube obeys the quantitative bound

\[
\boxed{c_G(p)<0.26811.}
\tag{5.6}
\]

The radius `10^-7` is deliberately conservative; no optimization is claimed.

## 6. Exact status relative to full FEI

**Exact candidate version.** `Gamma^dagger` at `C^dagger=6.521851214` from fleet01/B18 `20260922T0325Z-addressing-star-cdagger`.

**Prior missing implication.** Prove `D_{Gamma^dagger}(P;p)>=0` for every finite composition-prime Boolean gate and every interior product bias.

**Consumed peer artifact.** Primary: fleet01/B17 `20260922T043923Z-arity5-uniform-c001`, which closes all five-input gates at the exact center for the smaller `0.01` lift.  Regularity input: fleet01/B18 `20260922T050337Z-complementary-mux-address-tube`, which source-binds `|G'|<31` for the same h96 base potential.

**New proved inference.** The exact center slice expands to the full five-dimensional box `||p-1/2||_inf<=10^-7`, uniformly over all `2^32` five-input truth tables, with a strict defect reserve for every nonconstant nondictator.

**Replacement obligation.** Enlarge this tube toward the genuinely off-center region, or find a source-valid five-input gate/bias outside it with margin above the candidate.  The universal all-arity/all-bias implication remains unpaid.

**Next recipient.** `fleet03/B18`, the Campaign-B/all-gate integration lead; the useful next line is to combine this uniform tube with the already-certified dyadic/off-center slices and attack the remaining compact five-input bias region rather than repeat the center.

**Implication to full FEI.** Direct but partial: one open neighborhood in the decisive universal gate inequality is now closed.  Full FEI remains **OPEN / NOT PROVED** because no argument covers every product bias and every finite arity.

## 7. Verification scope

`check_arity5_bias_tube.py` checks the conservative scalar constants in Sections 1--5.  Its source SHA-256 is

`5dc6e47203b071330304d1d43277464beebed168a851db1ff550681515b57f40`.

The captured output SHA-256 is

`23097f59eed665360356db1d65fd33c11641161b06df6f2a8b7912b7201b724d`.

It prints `PASS`, with the checked defect lower bound `0.0001198196954523071` and margin upper bound `0.2681090002436382`.  The checker verifies arithmetic, not the inherited peer theorem; that theorem is consumed at its exact source-bound scope rather than copied as a local finite rerun.

Scoped privacy review: only FEI mathematics, repository-relative source identifiers, nonsecret hashes, and sanitized verification metadata are included.  No credentials, scheduler identifiers, machine paths, unrelated private material, email/Drive action, public-posting action, paid/remote compute, workflow dispatch, permission changes, or benchmark material are present.
