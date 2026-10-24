# B14 — adaptive pivotality determination and a sharper folded-J information compiler

**Status:** PARTIAL. Full Friedgut--Kalai Fourier entropy--influence remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; no authenticated brain retrieval/context is claimed.  
**Route:** materially different continuation of APPROACH 5/6: replace a single static crossing block by an adaptive physical decision tree that determines one folded pivotality event.  
**Publication priority:** UNVERIFIED; no novelty claim.

## 0. Fresh compatible inputs actually used

This run used the current joint A-interface and, in particular, the complete other-account result

`account02/B14/20260921T210915Z-crossing-information-selector/REPORT.md`, blob `673dbf5d2bc162fc43b7931e88a5449fce2a219a`.

That report proves, for a centered survivor `j`, the KL lower bound

\[
I(\eta_j;Z_A)\ge \log_2\frac{1-p_j}{p_j}\,c_j(A),
\]

the Boolean-square estimate `Inf_i(eta_j)<=2 Inf_i(f)`, and the static `(gamma,K)` compiler requiring one block with both substantial crossing and small corrected erasure. I use those objects, but replace its upper information estimate by a sharper **folded-J drift** estimate and then pass from static blocks to adaptive determination trees.

I also use the exact folded restriction drift and corrected entropy from account04/B14,

\[
D_A=\Delta_A J,
\qquad
\Delta_A\mathcal F=B_A-Q_A,
\]

and account01/B13's proved fact that rare pivotality events cannot cross majority under too few revealed coordinates. Thus no singleton-crossing hypothesis is reintroduced.

Throughout, physical input bits are denoted `Z`; the Fourier spectral sample is not conflated with them.

## 1. Folded pivotality events

For a Boolean function `f` and coordinate `j`, let

\[
\eta_j(z_{-j})=1_{\{f(z)\ne f(z\oplus e_j)\}},
\qquad p_j=\Pr(\eta_j=1),
\]

and put

\[
q_j:=\min(p_j,1-p_j),\qquad J(f)=\sum_j q_j.
\]

Define the **folded pivotality event**

\[
Y_j=
\begin{cases}
\eta_j,&p_j\le1/2,\\
1-\eta_j,&p_j>1/2.
\end{cases}
\]

Thus `Pr(Y_j=1)=q_j<=1/2`. Under a restriction not querying `j`, if the posterior of this event is `U`, the child's folded `j`-influence is `min(U,1-U)`. Hence the loss in the folded `j`-influence is exactly

\[
q_j-\mathbb E\min(U,1-U)=\mathbb E(2U-1)_+.
\tag{1.1}
\]

This remains true if the locally preferred orientation flips later; complementing a Bernoulli event does not change mutual information.

## 2. A sharp scalar Jensen--Shannon inequality

Set

\[
\boxed{\beta:=4h_2(1/4)-2=1.2451124978365313\ldots.}
\tag{2.1}
\]

### Lemma 2.1

Let `0<=u<=v<=1` and `(u+v)/2<=1/2`. Put

\[
m={u+v\over2},\quad d={v-u\over2},\quad c=(v-1/2)_+.
\]

Then the equal-weight Bernoulli Jensen--Shannon information satisfies

\[
\boxed{
h_2(m)-{h_2(u)+h_2(v)\over2}\le \beta d+c.}
\tag{2.2}
\]

The coefficient `beta` is sharp for the part without majority crossing: equality occurs at `(u,v)=(0,1/2)`.

### Proof

First assume `v<=1/2`. Write `v=u+2d`. Since

\[
-h_2''(x)={1\over \ln2\,x(1-x)}=:k(x)
\]

is decreasing on `(0,1/2]`, the normalized midpoint Jensen gap at fixed `d` is largest when the interval is shifted all the way left, i.e. `u=0`. One convenient integral form is

\[
{1\over d}\left[h_2(u+d)-{h_2(u)+h_2(u+2d)\over2}\right]
={1\over2d}\int_0^d\int_{u+s}^{u+s+d}k(t)\,dt\,ds.
\tag{2.3}
\]

At `u=0`, scale `t=dr`. The factor

\[
dk(dr)={1\over\ln2\,r(1-dr)}
\]

is increasing in `d`; here `0<d<=1/4`. Therefore the largest normalized gap occurs at `d=1/4`, and equals

\[
4\left[h_2(1/4)-{h_2(0)+h_2(1/2)\over2}\right]
=4h_2(1/4)-2=\beta.
\]

Now assume `v>1/2`. Put `b=1-v`, so `0<=u<=b<=1/2`, and define

\[
e={b-u\over2},\qquad c={1\over2}-b.
\]

Then `d=e+c`. By symmetry `h_2(v)=h_2(b)`, and with `x=(u+b)/2`,

\[
\begin{aligned}
JS(u,v)
&=\left[h_2(x)-{h_2(u)+h_2(b)\over2}\right]
 +\left[h_2(x+c)-h_2(x)\right]\\
&\le \beta e+2c.
\end{aligned}
\tag{2.4}
\]

The first term uses the first case. For the second, `x>=(1/2-c)/2`. Since `h_2'` is decreasing, the increment is largest at `x=1/4-c/2`. The average of the convex function `h_2'` over the symmetric interval `[1/4-c/2,1/4+c/2]` increases with its radius, and at the largest radius `c=1/2` it equals

\[
{h_2(1/2)-h_2(0)\over1/2}=2.
\]

Thus the second term is at most `2c`. Since `beta>1`,

\[
\beta e+2c\le \beta(e+c)+c=\beta d+c.
\]

This proves (2.2). QED.

## 3. The Boolean square gives a folded boundary estimate

### Lemma 3.1

For distinct coordinates `i,j`, let `Y_j` be either the `j`-pivotality event or its complement. Then

\[
\boxed{
\operatorname{Inf}_i(Y_j)
\le 2\min\{\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)\}
=2q_i.
}
\tag{3.1}
\]

### Proof

Freeze every coordinate except `i,j`. If the `j`-pivotality status differs between the two values of `i`, exactly one of the two `j`-edges of this Boolean square is bichromatic. In that situation exactly one of the two `i`-edges is bichromatic. Hence on every square counted by `Inf_i(Y_j)`, the conditional `i`-influence of `f` is exactly `1/2`.

On every other square the conditional `i`-influence lies in `[0,1]`. Therefore, if `r=Inf_i(Y_j)`, both the global `i`-influence and its complement are at least `r/2`. Taking their minimum proves (3.1). Complementing `Y_j` does not change its boundary. QED.

This is the folded strengthening of the centered estimate used by account02/B14.

## 4. One revealed physical bit: information is paid by the actual folded-J drift

At a current restriction node, fix a surviving target `j` and query `i!=j`. Orient the current target event so its prior `p<=1/2`, and write its two posteriors as `u,v`. Let

\[
c_{j\leftarrow i}=p-\frac12\left[\min(u,1-u)+\min(v,1-v)\right]
\]

be the target coordinate's contribution to the folded-J decrease.

The coupling using the same remaining input coordinates gives

\[
|u-v|\le \operatorname{Inf}_i(Y_j).
\]

By Lemma 3.1,

\[
d={|u-v|\over2}\le q_i.
\]

Lemma 2.1 therefore yields

\[
\boxed{
I(Y_j;Z_i)\le \beta q_i+c_{j\leftarrow i}.
}
\tag{4.1}
\]

The exact one-step folded drift is

\[
D_i:=J(f)-\frac{J(f_{i=0})+J(f_{i=1})}{2}
=q_i+\sum_{k\ne i}c_{k\leftarrow i}.
\tag{4.2}
\]

Consequently

\[
\boxed{I(Y_j;Z_i)\le\beta D_i.}
\tag{4.3}
\]

This is strictly sharper in mechanism than `I(Y_j;Z_i)<=2 q_i`: it spends the actual folded restriction drift, and it gives coefficient `beta<1.246` rather than `2`.

## 5. Fixed blocks: sharpening the other-account crossing estimate

Let `A` be any physical block not containing `j`. Reveal its bits in any order. Chain rule, (4.1), and telescoping give

\[
\boxed{
I(Y_j;Z_A)
\le \beta D_A-(\beta-1)c_j(A),
}
\tag{5.1}
\]

where

\[
D_A=J(f)-\mathbb E_zJ(f_{A=z})
\]

and `c_j(A)` is the total folded `j`-crossing in (1.1).

Indeed, the sum of target crossing contributions along the reveal is exactly `c_j(A)`, while every other crossing contribution is nonnegative and belongs to `D_A`.

Combining (5.1) with account02/B14's proved KL threshold lower bound gives the new block inequality

\[
\boxed{
\left[\log_2{1-p\over p}+\beta-1\right]c_j(A)
\le \beta D_A,
}
\tag{5.2}
\]

for the folded target density `p=q_j<1/2`.

Thus the earlier logarithmic crossing payment can be charged to **total folded influence actually destroyed by the same restriction**, not merely to twice the root block influence.

If `p<=1/4` and `c_j(A)>=\gamma p`, account02/B14's scalar inequality `h_2(p)<=(9/4)p log_2((1-p)/p)` and (5.2) imply, in particular,

\[
\boxed{
h_2(p)\le {9\beta\over4\gamma}D_A< {2.802\over\gamma}D_A.}
\tag{5.3}
\]

The exact factor can be slightly improved by retaining the `beta-1` term in (5.2). The previous static conversion had coefficient `9/(2 gamma)=4.5/gamma` against the unreimbursed physical block influence.

## 6. Adaptive determination: no crossing fraction is needed

A **`j`-determining physical tree** is a finite decision tree which never queries `j` and whose transcript determines the folded pivotality event `Y_j`. Such a tree always exists by revealing all coordinates other than `j`.

At each leaf, the `j`-edge status is constant on all remaining completions. Hence `j` is either irrelevant, or it is always pivotal. In the latter case the leaf function factors as `chi_j` times a Boolean function not depending on `j`. Thus `j` can be removed at the leaf without changing spectral entropy, folded influence, or the corrected entropy used below.

Let

\[
D_T=J(f)-\sum_\ell\pi_\ell J(f_\ell)
\]

be the total expected folded-J drop. Applying (4.1) at every internal node and using the mutual-information chain rule gives

\[
I(Y_j;\text{transcript})
\le \beta\sum_v\pi_v q_{i(v)}
+\sum_v\pi_v c_{j\leftarrow i(v)}.
\]

Because the tree determines `Y_j`, the left side is `h_2(q_j)`. The total target folded drop is exactly `q_j`, and all other crossing refunds are nonnegative. Therefore

\[
\boxed{
h_2(q_j)\le \beta D_T-(\beta-1)q_j<\beta D_T.}
\tag{6.1}
\]

This is the principal new selector lemma of the run. It is adaptive, uses only actual physical restrictions, has no prescribed-coordinate payment hypothesis, and automatically preserves all known counterexamples to every-coordinate or singleton crossing statements.

## 7. A new adaptive compiler for full FEI

Use the current bounded potential

\[
\Phi(f)=\sum_i\mathfrak j(p_i),
\qquad
\mathcal F(f)=H(f)-\Phi(f),
\qquad
0\le\Phi(f)\le{2\over\ln2}J(f).
\tag{7.1}
\]

Choose a centered physical-restriction descendant maximizing

\[
\rho={\mathcal F\over J}.
\]

For a `j`-determining tree `T`, define its corrected entropy decrement

\[
E_T=\mathcal F(f)-\sum_\ell\pi_\ell\mathcal F(f_\ell).
\tag{7.2}
\]

Every nonconstant leaf is a proper physical restriction descendant (and `j` is freely removable there), so criticality gives

\[
E_T\ge\rho D_T.
\tag{7.3}
\]

### Theorem 7.1 — adaptive pivotality-certificate compiler

Suppose there is a universal finite `K` such that every nontrivial corrected-ratio-critical core has **some** active coordinate `j` and **some** `j`-determining physical tree with

\[
\boxed{E_T\le K h_2(q_j).}
\tag{7.4}
\]

Then

\[
\boxed{\rho\le\beta K}
\tag{7.5}
\]

for every critical core, and hence full FEI follows with

\[
\boxed{
H(f)\le\left(\beta K+{2\over\ln2}\right)I(f)
}
\tag{7.6}
\]

for every Boolean `f`.

### Proof

By (7.3), (7.4), and (6.1),

\[
\rho D_T\le E_T\le K h_2(q_j)<K\beta D_T.
\]

The target is active, so `h_2(q_j)>0`, and (6.1) forces `D_T>0`. Divide by `D_T` to get (7.5). Finally use (7.1), character-centering to make ordinary influence equal to folded influence, and the invariance of spectral entropy under a character shift. QED.

This is a different universal missing arrow from the static `(gamma,K)` certificate: **no fixed crossing fraction and no one-shot block are required**. The tree is allowed to reveal different coordinates on different branches and stop early after the target pivotality has become deterministic.

Full FEI is not proved because (7.4) is not yet proved universally.

## 8. The missing potential becomes an exact Bellman value

For a fixed active target `j`, define

\[
V_j(f)=\inf_T\left[\mathcal F(f)-\sum_\ell\pi_\ell\mathcal F(f_\ell)\right],
\tag{8.1}
\]

where the infimum is over all `j`-determining physical trees. This is finite because revealing all other coordinates determines the event.

It obeys the exact dynamic-programming recursion

\[
\boxed{
V_j(f)=
\min_{i\ne j}
\left\{
\Delta_i\mathcal F
+{V_j(f_{i=0})+V_j(f_{i=1})\over2}
\right\},
}
\tag{8.2}
\]

with terminal value `V_j=0` once `q_j=0` (coordinate labels are naturally relabelled after a restriction).

Therefore the adaptive FEI selector problem has a precise potential-free form:

\[
\boxed{
\text{prove on every corrected critical core that}
\quad
\min_{j:q_j>0}{V_j(f)\over h_2(q_j)}\le K
\quad\text{for one universal }K.
}
\tag{8.3}
\]

Equation (8.2) is a genuine candidate for the missing potential in APPROACH 6: it is not a guessed scalar statistic, but the value function of the realizable physical restriction problem itself. It also makes the next obstruction test explicit: if the ratio in (8.3) is unbounded, retain that Boolean family and abandon this compiler rather than returning to a static threshold scan.

## 9. Executed diagnostic calculation

`check_adaptive_pivotality_selector.py` was executed in this run. Local SHA-256 values before delivery were

- script: `7b0c584b5f33279c0579c37541a1f7376f913772ec07a352df15ffae3c825fcf`;
- captured output: `5c02bcade4e0d4e1f33f3ea134dc8b5394405a701070fa8c8b0087d33df9e462`.

The scalar grid (`801 x 801` triangular domain) found minimum slack `0.0` in (2.2), at a trivial equality point; no negative grid slack occurred.

For the Bellman diagnostic, global sign was quotiented by fixing one truth-table value. All nonzero-folded-influence classes were scanned through four variables:

- `n=2`: 4 classes, maximum `min_j V_j/h_2(q_j)=0`;
- `n=3`: 120 classes, maximum `0.3459404194728127`;
- `n=4`: 32,752 classes, maximum `0.5987662209366419`.

The corresponding largest corrected ratios `F/J` in those scans were `0`, `0.3742051929126789`, and `0.6509360549803045`. These finite floating diagnostics do **not** prove a universal Bellman bound and are not a substitute for the analytic lemmas above.

## 10. Exact remaining obligation

This run changes the selector interface from

> find one static block with a fixed positive posterior crossing fraction and separately prove its erasure is small

to

> find one target coordinate whose **optimal adaptive pivotality-determination tree** has corrected entropy cost at most `K h_2(q_j)`.

The information side of that adaptive statement is now completely paid:

\[
h_2(q_j)\le\beta D_T-(\beta-1)q_j.
\]

The only universal gap is the **upper** corrected-entropy cost (8.3). The next attack should combine the Bellman recursion with the current near-subcube branch: when a derivative row is close to a coordinate subcube, query its defining bits in a short-circuit order (stop on the first mismatch), rather than paying the entire static block on every branch. Large row defect should be handed to the mixed-derivative/depth branch instead of being charged again.

**Full-problem change:** NONE; full FEI remains OPEN.  
**Mechanism change:** YES — static block crossing has been replaced by adaptive pivotality determination, with a sharp scalar constant `beta<1.246` and an exact Bellman selector potential.
