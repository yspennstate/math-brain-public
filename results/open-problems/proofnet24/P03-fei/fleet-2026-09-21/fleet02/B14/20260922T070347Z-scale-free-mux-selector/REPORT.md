# fleet02/B14 — scale-free off-center MUX selector tube

**Run:** `20260922T070347Z-fei-mux-offplane`  
**Classification:** `ESSENTIAL_STEP_APPLIED / MUX_SELECTOR_SCALE_CANCELLATION / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (authenticated repositories were read, but no native mathematical-brain receiver context was used).  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Publication priority:** unverified; no novelty claim is made.

## 0. Compact conditional universal argument and first missing implication

The source-current all-gate reformulation is the following.  For a symmetric nonnegative potential `Gamma`, define

\[
D_\Gamma(G;p)=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_z=4z(1-z).
\]

If `D_Gamma(G;p)>=0` for every finite Boolean gate and every interior product bias, the composition identity gives FEI with constant `Gamma(1/2)`.  The current Campaign-A candidate is

\[
C^\dagger=6.521851214,\qquad
C_0=6.4548,\qquad
a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(z)=\Gamma_0(z)+a^\dagger z(1-z),
\]
where `Gamma_0` is the committed h96 read-once potential.  The universal prime-gate inequality remains open.

The first explicit unpaid prime family is the one-bit MUX.  The exact missing implication is still to prove

\[
D_{\Gamma^\dagger}(M;t,q_0,q_1)\ge0
\]
for every interior `t,q0,q1`, or to exhibit a genuine negative point.  This report proves a new source-valid region of that exact inequality.  It does **not** replace the universal prime-gate obligation by a MUX theorem.

## 1. Named completed other-account inputs actually consumed

The principal input is fleet03/B13

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B13/20260922T063425Z-mux-selector-tube-x8/REPORT.md`.

It consumes the exact six-mass formula and proves

\[
|q_1-q_0|\le {m\over224},\qquad
\left|t-{1\over2}\right|\le {m\over1024}
\Longrightarrow
D_{\Gamma^\dagger}(M)>{7m\over250},
\]
where
\[
m=\min\{q_0+q_1,2-q_0-q_1\}.
\]
More importantly, it records from fleet04/B18 the stronger balanced-selector reserve

\[
\boxed{
|q_1-q_0|\le {m\over224}
\Longrightarrow
D_{\Gamma^\dagger}(M;1/2,q_0,q_1)>0.13m.
}
\tag{1.1}
\]

The exact arbitrary-bias MUX representation used below is fleet04/B18

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B18/20260922T061350Z-mux-equal-data-offcenter-tube/REPORT.md`,

which in turn uses the source-exact six-weight formula from its `20260922T045533Z-mux-joint-credit-collapse` report.  Fleet01/B18

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260922T055608Z-balanced-mux-collar-sharpen/REPORT.md`

supplies the h96 source representation and the near-center derivative window.  In particular, on `0<z<=1/2`,

\[
\Gamma_0(z)=zG(\log_2(1/z)),\qquad
G(1)=12.9096,\qquad |G'|<31,
\tag{1.2}
\]

and
\[
{1\over\ln2}<{10^7\over6931471}.
\tag{1.3}
\]
Its center-crossing calculation gives `|(Gamma^dagger)'|<58.440217` on a neighborhood wider than the one used below.

## 2. Before/after and the new mechanism

The preceding selector perturbation used Fannes--Audenaert directly on the six spectral masses.  Near the boundary `m->0`, that loses the exact `m log(1/m)` cancellation and therefore forces the selector displacement to shrink as

\[
|t-1/2|\le m/1024.
\]

The new observation is that the full defect, not the entropy term in isolation, has an exact scale cancellation.  Grouping the two Fourier masses belonging to each data input cancels every `V_j log V_j` term against the leaf entropy price, while grouping the source potential terms cancels the common `G(log_2(2/m))` value.  Only bounded local increments survive.

This yields a **fixed-width** selector tube, independent of `m`.

## 3. Theorem — fixed-width physical selector tube

Let

\[
M(A;D_0,D_1)=D_A,\qquad
\Pr(A=1)=t,\qquad \Pr(D_j=1)=q_j,
\]
and set
\[
m=\min\{q_0+q_1,2-q_0-q_1\},\qquad v=q_1-q_0,\qquad s=t-\frac12.
\]

### Theorem 3.1
For the live source candidate `Gamma^dagger`, every interior MUX satisfying

\[
\boxed{
|v|\le {m\over224},
\qquad
|s|\le {1\over464}
}
\tag{3.1}
\]
has

\[
\boxed{
D_{\Gamma^\dagger}(M;t,q_0,q_1)>{m\over400}>0.
}
\tag{3.2}
\]

The operation is the genuine physical reveal of the address bit; its children are literal gates and hence have exactly zero terminal gate defect.

Since `m<=1`, (3.1) strictly contains the previous `|s|<=m/1024` tube.  The selector radius improves by at least

\[
{1024\over464}=2.2068965\ldots,
\]
and by the factor `1024/(464m)` as `m->0`.  In particular the certified address radius no longer collapses at the data-boundary scale.

## 4. Exact MUX formula and normalization

Complement both data bits and the output if necessary.  This preserves the defect and lets us assume

\[
q_0+q_1=m\le1.
\tag{4.1}
\]
Put
\[
p={m\over2},\qquad u=1-m,\qquad
q_0={m-v\over2},\quad q_1={m+v\over2},\quad
t={1\over2}+s,\quad a=1-t,
\]
\[
V_j=4q_j(1-q_j),\qquad V_t=4t(1-t)=1-4s^2,
\]
\[
d=q_0+q_1-2q_0q_1\le m,\qquad
r=(1-t)q_0+tq_1=p+sv.
\]

The exact squared biased-Walsh masses are

\[
\begin{aligned}
w_\varnothing&=(1-2r)^2,\\
w_A&=V_t v^2,\\
w_0&=a^2V_0,\\
w_1&=t^2V_1,\\
w_{A0}&=taV_0,\\
w_{A1}&=taV_1.
\end{aligned}
\tag{4.2}
\]

Writing `B(z)=Gamma^dagger(z)+h_2(V_z)`, the exact defect is

\[
D(t)=dB(t)+aB(q_0)+tB(q_1)-\Gamma^\dagger(r)-H(w).
\tag{4.3}
\]

We compare (4.3) with `D(1/2)` and use the balanced reserve (1.1).

## 5. Source-potential difference: the scale logarithm cancels

The potential-only change is

\[
\Delta_\Gamma
=d[\Gamma^\dagger(t)-\Gamma^\dagger(1/2)]
+s[\Gamma^\dagger(q_1)-\Gamma^\dagger(q_0)]
-[\Gamma^\dagger(p+sv)-\Gamma^\dagger(p)].
\tag{5.1}
\]

### 5.1 Address term

For `|s|<=1/464`, reflect the address argument to

\[
z\in[231/464,1/2].
\]
Then, with `x=log_2(1/z)`,

\[
x-1\le\log_2{232\over231}
<{1\over231}{10^7\over6931471}.
\]
By (1.2)-(1.3), on every h96 source segment

\[
|\Gamma_0'(z)|
\le |G(x)|+{|G'(x)|\over\ln2}
<12.9096+31(x-1)+31{10^7\over6931471}.
\]
Adding the quadratic derivative `a^dagger|1-2z|<=a^dagger/232` gives the exact rational upper envelope

\[
12.9096
+{31\over231}{10^7\over6931471}
+31{10^7\over6931471}
+{0.268204856\over232}
<58.
\tag{5.2}
\]
Therefore

\[
d[\Gamma^\dagger(t)-\Gamma^\dagger(1/2)]
\ge-58m|s|.
\tag{5.3}
\]

### 5.2 Data/output cancellation

Define

\[
T=s[\Gamma^\dagger(q_1)-\Gamma^\dagger(q_0)]
-[\Gamma^\dagger(p+sv)-\Gamma^\dagger(p)].
\tag{5.4}
\]

If `m<=224/225`, then `q_0,q_1,p,p+sv<=1/2`.  Put

\[
\rho={v\over m},\qquad x=\log_2(1/p),
\qquad \delta_y=G(x-\log_2 y)-G(x).
\]
After swapping the two data inputs if necessary we may take `rho>=0`.  The common `G(x)` term cancels **exactly**:

\[
{T_0\over p}
=s[(1+\rho)\delta_{1+\rho}-(1-\rho)\delta_{1-\rho}]
-(1+2s\rho)\delta_{1+2s\rho}.
\tag{5.5}
\]

Using `|G'|<31`, `rho<=1/224`, `|s|<=1/464`,
`ln(1+x)<=x`, `-ln(1-x)<=x/(1-x)`, and (1.3), (5.5) gives the conservative bound

\[
|T_0|<94|s||v|.
\tag{5.6}
\]

For the quadratic lift the same combination is exact and favorable:

\[
T_{a^\dagger z(1-z)}=a^\dagger s^2v^2\ge0.
\tag{5.7}
\]

If `m>224/225`, all four arguments in (5.4), after symmetry reflection, lie in the fleet01/B18 near-center interval where `|(Gamma^dagger)'|<58.440217<59`.  Hence directly

\[
|T|<118|s||v|.
\tag{5.8}
\]

We retain the single loose bound

\[
\boxed{T\ge-160|s||v|.}
\tag{5.9}
\]

Combining (5.3), (5.9), and `|v|<=m/224`,

\[
\boxed{
\Delta_\Gamma
\ge-m|s|\left(58+{160\over224}\right).
}
\tag{5.10}
\]

The important point is structural: no `log(1/m)` remains.

## 6. Shannon part: exact pair grouping removes every `V log V` scale term

Let
\[
\phi(x)=x\log_2(1/x),\quad \phi(0)=0,
\qquad X(x)=\phi(x^2).
\]
The entropy-only part of (4.3) is

\[
E(t)=d h_2(V_t)+a h_2(V_0)+t h_2(V_1)-H(w).
\tag{6.1}
\]

Grouping `(w_0,w_{A0})` and `(w_1,w_{A1})` before subtracting the leaf entropy prices gives the exact identity

\[
\boxed{
E(t)=d h_2(V_t)+aX(u+v)+tX(u-v)
-V_0R_0(t)-V_1R_1(t)
-X(u-2sv)-\phi(V_t v^2),
}
\tag{6.2}
\]
where
\[
R_0(t)=a[(2-t)\log_2(1/a)+t\log_2(1/t)],
\]
\[
R_1(t)=t[(1+t)\log_2(1/t)+a\log_2(1/a)].
\tag{6.3}
\]

Every `V_j log V_j` term has disappeared from (6.2).  This is the cancellation that direct Fannes continuity misses.

Set
\[
R_{\rm av}={R_0+R_1\over2},\qquad
R_{\rm dif}={R_1-R_0\over2},
\]
\[
S=V_0+V_1,\qquad \Delta=V_1-V_0=4uv.
\]
Direct simplification gives

\[
R_{\rm av}(t)=h_2(t),
\qquad
V_0R_0+V_1R_1=S R_{\rm av}+\Delta R_{\rm dif}.
\tag{6.4}
\]
Moreover
\[
R_{\rm dif}(1/2)=0,
\qquad
R_{\rm dif}''(t)=2\log_2{1-t\over t}.
\]
On `[231/464,233/464]`, elementary differentiation gives

\[
|R_{\rm dif}'(t)|<1.
\tag{6.5}
\]
Also `S<=4m`, `|Delta|<=4|v|`, and the elementary binary-entropy estimate

\[
1-h_2(1/2+s)\le4s^2
\tag{6.6}
\]
holds for `|s|<=1/2`.

Finally, for `|x|<=1`,

\[
|X'(x)|
\le 4|x|\log_2(1/|x|)+{2|x|\over\ln2}
<{21\over4}.
\tag{6.7}
\]

Using (6.2)-(6.7), term by term,

* `d h_2(V_t)=d h_2(4s^2)<=m h_2(4s^2)`;
* the change of `aX(u+v)+tX(u-v)` is at most `11|s||v|`;
* the `R_0,R_1` change is at most `16ms^2+4|s||v|`;
* the `X(u-2sv)` change is at most `11|s||v|`.

For the last atom, `V_t=1-4s^2>=1/2` and `v^2<=m^2/224^2`.  The mean-value theorem for `phi` gives

\[
|\phi(V_t v^2)-\phi(v^2)|
\le4s^2v^2\log_2{1\over V_tv^2}.
\]
Since `log_2 224<8` and `m log_2(1/m)<=1`,

\[
4v^2\log_2{1\over V_tv^2}
< {76\over224^2}m<0.01m.
\tag{6.8}
\]

Therefore

\[
\boxed{
|E(t)-E(1/2)|
\le m h_2(4s^2)+26|s||v|+16.01ms^2.
}
\tag{6.9}
\]

Again, there is no `m log(1/m)` loss.

## 7. Numerical finish with exact rational slack

For `|s|<=1/464`,

\[
4s^2\le {1\over53824}.
\]
The standard bound `h_2(x)<=x log_2(e/x)` together with `log_2 e<3/2` and `53824<2^16` gives

\[
h_2(4s^2)< {35\over107648}.
\tag{7.1}
\]

By (6.9) and `|v|<=m/224`,

\[
{|E(t)-E(1/2)|\over m}
< {35\over107648}
+{26\over224\cdot464}
+{1601\over100\cdot464^2}.
\tag{7.2}
\]

By (5.10),

\[
{\Delta_\Gamma\over m}
\ge -{58\over464}-{160\over224\cdot464}.
\tag{7.3}
\]

Insert the balanced reserve (1.1).  The remaining exact rational margin is

\[
\begin{aligned}
{D(t)\over m}
&>
{13\over100}
-{58\over464}
-{160\over224\cdot464}
-{35\over107648}
-{26\over224\cdot464}
-{1601\over100\cdot464^2}\\
&={423629\over150707200}\\
&=0.0028109406849838627\ldots\\
&>{1\over400}.
\end{aligned}
\tag{7.4}
\]

This proves Theorem 3.1.  Boundary values follow by continuity; the all-gate formulation itself only needs interior biases.

## 8. What changed, and what remains

### FULL-PROBLEM CHANGE

**NONE.**  Full FEI remains open.  No universal all-prime-gate inequality is proved.

### MECHANISM CHANGE

**YES.**  The previous three substantive B14 reports moved through: (i) reachable shared-core exclusion by an invariant interval, (ii) a balanced-address signed-posterior MUX collar, and (iii) a small three-dimensional continuity tube whose entropy control was generic finite-alphabet continuity.  The present run changes the perturbation mechanism itself: it performs the leaf-price/spectral-pair cancellation **before** bounding entropy and performs the common-source `G(x)` cancellation **before** bounding the potential.  This removes the boundary-scale logarithm and produces a selector radius independent of `m`.

### Exact before/after

Old source-valid off-center region on the `|v|<=m/224` data collar:

\[
|s|\le {m\over1024}.
\]

New region:

\[
\boxed{|s|\le {1\over464}.}
\]

Thus any negative MUX point with `|v|<=m/224` must satisfy

\[
\boxed{|t-1/2|>1/464,}
\]
not merely a boundary-dependent exclusion.

### Remaining obligation

The exact MUX remainder is the compact region outside the accumulated equal-data, complementary-data, zero-credit, and fixed selector tubes.  Closing that MUX remainder would still not close FEI: the universal obligation is `D_{Gamma^dagger}(G;p)>=0` for every composition-prime Boolean gate and every interior product bias, or a source-valid replacement potential/policy that yields the same universal induction.

No prescribed-coordinate payment, every-critical-core shell claim, sign-free/global phase/rank/l1 bound, ordinary-depth budget, or fixed-relative near-subcube shortcut is used here.
