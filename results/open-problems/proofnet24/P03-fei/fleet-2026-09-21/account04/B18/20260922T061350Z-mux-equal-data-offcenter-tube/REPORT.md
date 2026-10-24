# B18 — a linear off-center tube around the equal-data MUX family

**Run:** `20260922T061350Z-b18-fei-r19`  
**Account / slot:** `account04 / B18`  
**Classification:** `ESSENTIAL_STEP_APPLIED / NEW THREE-PARAMETER MUX SAFE REGION / FULL_FEI_OPEN`  
**Execution:** **WITHOUT_VERIFIED_BRAIN** (`full_brain_connected=false`)  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Current source target

Later owner control `2026-09-22.2` supersedes the older interface-A/B wording where they conflict. The current universal target is the all-gate potential inequality
\[
D_\Gamma(G;p):=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p)\ge0,
\qquad V_u=4u(1-u),
\]
for every Boolean gate and every interior product bias.

The source-current candidate used here is
\[
C^\dagger=6.521851214,
\qquad a^\dagger=0.268204856,
\qquad
\Gamma^\dagger(z)=\Gamma_0(z)+a^\dagger z(1-z).
\]
No claim is made that this fixed candidate proves the universal all-gate inequality.

This run consumes the newest account01/B18 balanced-address MUX collar and the source-exact B18 six-weight MUX formula, then proves a genuinely **off-center address** neighborhood of that collar. The new region is distinct from the preceding complementary-data tube `20260922T052903Z-mux-joint-tube`: here the two data biases are close to **each other**, not close to complements.

## 1. Compatible results consumed without double spending

### 1.1 account01/B18 newest balanced-MUX collar

`account01/B18/20260922T055608Z-balanced-mux-collar-sharpen/REPORT.md` proves at address bias `t=1/2` the safe collar
\[
|q_1-q_0|\le {1\over112}\min\{q_0+q_1,2-q_0-q_1\}
\quad\Longrightarrow\quad
D_{\Gamma^\dagger}(M;1/2,q_0,q_1)>0.
\]
Its proof gives two quantitative source-valid ingredients that are retained here:

1. in the same-side sector, writing
   \[
   m=\min\{q_0+q_1,2-q_0-q_1\},\qquad
   \rho={|q_1-q_0|\over m},
   \]
   the defect is at least
   \[
   {m\over2}
   \left(0.521851214-A\rho-{a^\dagger\over2}\rho^2\right),
   \qquad
   A={31\cdot10^7\over 6931471}<45;
   \tag{1.1}
   \]
2. in the center-crossing sector, on the larger `1/112` collar it supplies the source-valid near-center potential Lipschitz constant
   \[
   L_*<58.440217.
   \tag{1.2}
   \]

### 1.2 account04/B18 exact general MUX formula

`account04/B18/20260922T052903Z-mux-joint-tube/REPORT.md` proves for
\[
M(A;D_0,D_1)=D_A,
\qquad \Pr(A=1)=t,
\qquad \Pr(D_j=1)=q_j,
\]
the six squared biased-Walsh masses
\[
\begin{aligned}
w_\varnothing&=(1-2r)^2,\\
w_A&=V_t(q_1-q_0)^2,\\
w_0&=(1-t)^2V_0,\\
w_1&=t^2V_1,\\
w_{A0}&={V_tV_0\over4},\\
w_{A1}&={V_tV_1\over4},
\end{aligned}
\tag{1.3}
\]
where
\[
r=(1-t)q_0+tq_1,\qquad V_j=4q_j(1-q_j).
\]
It also gives the exact gate-defect representation
\[
D_{\Gamma^\dagger}(M;t,q_0,q_1)
=dB(t)+(1-t)B(q_0)+tB(q_1)-\Gamma^\dagger(r)-H(w),
\tag{1.4}
\]
with
\[
d=q_0+q_1-2q_0q_1,
\qquad
B(z)=\Gamma^\dagger(z)+h_2(V_z).
\]

The same report records the source representation
\[
\Gamma_0(z)=zG(\log_2(1/z))\quad(0<z\le1/2),
\]
with
\[
|G(x)|<4.9096x+8.62812,
\qquad |G'(x)|<31,
\qquad {1\over\ln2}<{3\over2}.
\tag{1.5}
\]
These imply the derivative bounds used below.

### 1.3 newest account04 B12--B14 state

The newest compatible reports were also read and preserved:

* B12 `20260922T0526Z-balanced-arity5-center` closes the entire balanced uniform arity-five center with `H<=6(I-1)` but explicitly leaves off-center product biases open.
* B13 `20260922T051245Z-biased-joint-credit-collar` proves the arbitrary-pivot source credit `C_j >= V_t(1-2delta)^2` and a rare-pivot high-normalized-influence exclusion.
* B14 `20260922T051345Z-balanced-transposition-barrier` excludes every one-pair balanced mutation of the source n=18 prime gate and identifies coherent product-bias directions, not another balanced mutation search, as the live source-specific freedom.

None of those credits is charged again in the MUX estimate below.

The older account04/B18 mixed-curvature identities and exact zero-depth classification are preserved unchanged. In particular, no step below uses the refuted assertion `sum_k d_k = O(J)`.

## 2. New theorem

Define
\[
m:=\min\{q_0+q_1,\ 2-q_0-q_1\},
\qquad
v:=q_1-q_0,
\qquad
s:=t-{1\over2}.
\]
For interior data biases, `m>0`.

### Theorem 2.1 — off-center equal-data MUX tube

For the live source candidate `Gamma^dagger`, every one-bit MUX satisfying
\[
\boxed{
|v|\le {m\over224},
\qquad
|s|\le {m\over8192}
}
\tag{2.1}
\]
has the quantitative positive defect
\[
\boxed{
D_{\Gamma^\dagger}(M;t,q_0,q_1)>{m\over10}>0.
}
\tag{2.2}
\]

Thus the balanced-address `1/112` collar from account01/B18 contains a source-valid **three-parameter** subcollar that survives a linear-in-boundary-distance address displacement. This is not a finite-grid statement.

## 3. Balanced-address reserve on the narrower data collar

By complementing both data bits and the output if necessary, we may assume
\[
q_0+q_1=m\le1.
\]
This leaves the defect invariant because `Gamma^dagger` and `B` are symmetric and the squared spectrum is unchanged. Put
\[
u=1-m\ge0,
\qquad
\rho={|v|\over m}\le{1\over224}.
\]

### 3.1 Same-side sector

If `|v|<=u`, apply (1.1). Since
\[
A<45,
\qquad {a^\dagger\over2}<0.135,
\]
we get
\[
\begin{aligned}
D_{\Gamma^\dagger}(M;1/2,q_0,q_1)
&>{m\over2}
\left(0.521851214-{45\over224}-{0.135\over224^2}\right)\\
&=0.1604778331639\ldots\,m\\
&>0.16m.
\end{aligned}
\tag{3.1}
\]

### 3.2 Center-crossing sector

If `u<|v|`, then (2.1) gives
\[
0\le u<{1\over224},
\qquad |v|\le{1\over224}.
\]
The two data arguments therefore lie in a strictly smaller near-center interval than the one used to prove (1.2), so the same source-valid constant `L_*<58.440217` applies.

The information reserve in account01/B18 is at least
\[
R_C=(C^\dagger-6){1-u^2+v^2\over2}
>{0.521851214\over2}\left(1-{1\over224^2}\right)
=0.26092040679259\ldots,
\tag{3.2}
\]
while the potential midpoint loss is bounded by
\[
J\le {L_*|v|\over2}
<{58.440217\over448}
=0.13044691294642\ldots.
\tag{3.3}
\]
Hence
\[
D_{\Gamma^\dagger}(M;1/2,q_0,q_1)
>0.13047349384616\ldots
>0.13m.
\tag{3.4}
\]

Combining the two sectors,
\[
\boxed{
D_{\Gamma^\dagger}(M;1/2,q_0,q_1)>0.13m
}
\tag{3.5}
\]
throughout the full narrower data collar `|v|<=m/224`.

## 4. Source-valid address perturbation bound

We now compare `t=1/2+s` with `t=1/2`, assuming `|s|<=m/8192`.

Let
\[
L=\log_2(1/m).
\]
The elementary inequality
\[
mL\le1
\tag{4.1}
\]
is sufficient below.

### 4.1 Potential and leaf terms

From (1.5), for a small-side argument `z` with `x=log_2(1/z)`,
\[
|\Gamma_0'(z)|
\le |G(x)|+{|G'(x)|\over\ln2}
<5x+56.
\]
Adding the quadratic lift gives
\[
|(\Gamma^\dagger)'(z)|<5x+57.
\tag{4.2}
\]
The standard derivative identity for `h_2(V_z)` together with symmetry gives
\[
\left|{d\over dz}h_2(V_z)\right|<4(x+1),
\tag{4.3}
\]
so
\[
|B'(z)|<9x+61<9x+65.
\tag{4.4}
\]

For the two data arguments and the output argument occurring here, their reflected small-side representatives are at least `m/4`. Therefore `x<=L+2`, and
\[
|B(q_1)-B(q_0)|\le |v|(9L+83),
\tag{4.5}
\]
\[
|\Gamma^\dagger(r(s))-\Gamma^\dagger(r(0))|
\le |sv|(5L+67).
\tag{4.6}
\]

At the address point itself, `|s|<=1/8192`. The source near-center bound gives `|(Gamma^dagger)'|<66`; moreover, writing `z=2|s|<=1/4096`,
\[
\left|{d\over dt}h_2(V_t)\right|
=4z\left|\log_2{z^2\over1-z^2}\right|<1.
\]
Thus
\[
|B(t)-B(1/2)|<67|s|.
\tag{4.7}
\]
Since `d<=q_0+q_1=m`, equations (4.5)--(4.7) give the total nonentropy variation
\[
\begin{aligned}
E_{\rm smooth}
&<67m|s|+|s||v|(14L+150).
\end{aligned}
\tag{4.8}
\]
Using `|s|<=m/8192`, `|v|<=m/224`, (4.1), and `m<=1`,
\[
{E_{\rm smooth}\over m}
<{67\over8192}+{164\over8192\cdot224}.
\tag{4.9}
\]

### 4.2 Six-atom entropy variation

Use the exact six masses (1.3). Between `t=1/2+s` and `1/2`, their total `l^1` displacement is bounded as follows.

The two singleton masses and the two address-singleton masses contribute at most
\[
4m(|s|+2s^2),
\]
the zero mode contributes at most
\[
4|s||v|<{m|s|\over56},
\]
and the pure-address mode contributes at most
\[
4s^2v^2.
\]
Since `|s|<=1/8192`, the sum is strictly less than
\[
5m|s|.
\tag{4.10}
\]
Therefore the total variation distance of the two six-atom spectral laws is
\[
\tau<{5\over2}m|s|
\le {5m^2\over16384}.
\tag{4.11}
\]

Fannes--Audenaert on an alphabet of size six gives
\[
|H(w(t))-H(w(1/2))|
\le h_2(\tau)+\tau\log_2 5
\le \tau\log_2{5e\over\tau}.
\tag{4.12}
\]
With `|s|<=m/8192`,
\[
\begin{aligned}
{\tau\over m}\log_2{5e\over\tau}
&\le {2.5\over8192}
 m\left(\log_2(2e\cdot8192)+2L\right)\\
&<{2.5\over8192}(15.5+2)\\
&={43.75\over8192}
=0.005340576171875.
\end{aligned}
\tag{4.13}
\]
Here we used `log_2 e<3/2` and (4.1).

### 4.3 Total address loss

Combining (4.9) and (4.13),
\[
\begin{aligned}
{\left|D(t,q_0,q_1)-D(1/2,q_0,q_1)\right|\over m}
&< {67\over8192}
+{164\over8192\cdot224}
+{43.75\over8192}\\
&=0.013608660016741\ldots\\
&<{1\over64}.
\end{aligned}
\tag{4.14}
\]

Together with the balanced reserve (3.5),
\[
D_{\Gamma^\dagger}(M;t,q_0,q_1)
>\left(0.13-{1\over64}\right)m
=0.114375m
>{m\over10}.
\]
This proves Theorem 2.1. QED.

## 5. What this changes and what it does not

### PROVED in this run

1. A quantitative balanced-address reserve `D>0.13m` on the narrower equal-data collar `|q1-q0|<=m/224`.
2. A source-valid address-continuity estimate costing less than `m/64` when `|t-1/2|<=m/8192`.
3. The resulting three-parameter theorem `D>m/10` in (2.1).

### CONSUMED / not respent

* account01/B18's newest balanced-address collar and its source derivative constants;
* account04/B12's balanced arity-five center closure;
* account04/B13's arbitrary-bias joint-credit lower bound;
* account04/B14's balanced-transposition barrier;
* account01/B18's older curvature-refunded restriction theorem.

### PRESERVED exact rigidity / refutations

* the account04/B18 mixed-curvature law and all-zero-depth character-twisted one-point classification remain valid;
* `sum d_k=O(J)` remains refuted;
* prescribed-coordinate entropy payment remains refuted;
* the fixed-relative `q/16` support approximation shortcut remains refuted;
* old decomposable/AND extremality for the fixed read-once potential remains refuted;
* no conditional theorem has been promoted to unconditional FEI closure.

### OPEN

The live fixed candidate is **not** proved for:

* general MUX biases outside the union of the certified equal-data and complementary-data tubes;
* the coherent biased direction of the source n=18 composition-prime gate identified by account02/B16;
* arbitrary composition-prime Boolean gates and arbitrary product biases.

Accordingly full FEI remains **OPEN / NOT PROVED**.

## 6. Next exact implication

The MUX obstruction is now split into two source-certified neighborhoods: the complementary-data tube from the preceding B18 run and the new equal-data off-center tube here. The smallest nonredundant next MUX task is the compact intermediate geometry after removing those two tubes, using the exact scalar collapse and B12 simultaneous data-pivot cross-deficit conditions.

At the broader all-gate level, B14/account02-B16's coherent biased n=18 prime direction remains potentially more decisive: a source-valid bound on its finite `O(u^2)` remainder could falsify the present fixed potential without touching FEI itself. That candidate-specific obligation is kept separate from the universal theorem proved above.
