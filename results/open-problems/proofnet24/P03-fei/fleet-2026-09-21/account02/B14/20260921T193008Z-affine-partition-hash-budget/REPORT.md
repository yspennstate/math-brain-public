TASK: B14 ACCOUNT: account02 RUN: 2026-09-21T19:30:08.890200Z — affine partition-hash restriction with a spendable centered budget

**Status:** PARTIAL / PROVED universal auxiliary theorems. **Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.**

**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated mathematical-brain or cognitive-memory retrieval/context was used.

**Model self-report:** GPT-5.6 Sol. **Reasoning requested:** maximum actually supported. Configured reasoning level, current reasoning-level self-report, provider reasoning-token usage, and provider thinking time are UNKNOWN / not exposed.

**FULL-PROBLEM CHANGE:** **NO FULL-BOUND MOVEMENT.** This report does not prove a finite universal FEI constant.

**MECHANISM CHANGE:** **YES.** The preceding B14 affine-pair report produced a large *sum* of available pair drops in shell-poor critical cores but explicitly could not spend that sum at one tree node. This run replaces one-pair selection by a random affine **coalescence partition** of all current coordinates. It proves (i) a genuine affine restriction whose centered influence drop is nonnegative and telescopes globally, (ii) an exact corrected-entropy upper charge for every such partition, and (iii) a random-colouring theorem converting high spectral mass above the first shell into a **single actually spendable affine drop**. At the inherited current lower-bound calibration, the previous `>0.6843938676 J` aggregate pair supply becomes a guaranteed one-step affine drop `>0.3421969338 J`.

No novelty or publication-priority claim is made.

## 0. Fresh frontier and last-three substantive comparison

Fresh scientific `master` was recovered before this work. The three preceding account02/B14 substantive reports were:

1. `20260921T170108Z-centered-refunded-selector`: median-character centering made the mass-weighted singleton selector parity-padding invariant and localized a hypothetical high-ratio physical restriction-critical descendant to centered first-shell fraction
   \[
   r_c:=\Pr(|X|=1)/J<0.3156061323581677
   \]
   at the current certified lower-bound scale.
2. `20260921T175746Z-block-js-critical-han`: coherent restriction information tensorized over physical blocks, giving all-block critical erasure floors and a fractional-Han hierarchy, but the proper-block upper envelope could not beat the singleton envelope.
3. `20260921T190143Z-affine-pair-global-budget`: pair-parity affine restriction was made globally safe. For a centered spectral law it supplied exact nonnegative centered drop at least `2 p_ij`; shell-poor spectra obeyed
   \[
   \sum_{i<j}2p_{ij}\ge (1-r_c)J.
   \]
   The report correctly warned that this was only an **availability statistic**: a node may select one pair, so the whole sum was not spendable.

The same universal implication was still unpaid: find a physical/affine restriction strategy whose entropy charge is globally payable by a nonreused `O(I)` budget. The present run attacks the precise nonspendability obstruction rather than further optimizing the scalar singleton threshold.

A compatible fresh account01/B14 result supplies the folded Jensen--Shannon potential
\[
\Phi(f)=\sum_i\eta(p_i),\qquad
\eta(p)=1-h_2\!\left(\frac12+\sqrt{s(1-s)}\right),\quad s=\min(p,1-p),
\]
with `0<=Phi<=(2/ln 2)I`, and shows that `H-Phi` is the natural corrected entropy for physical erasure. I use that potential below but change the restriction geometry.

## 1. Normalization

Work on `F_2^n` with Boolean
\[
f:F_2^n\to\{-1,+1\}.
\]
Let
\[
a_S=\widehat f(S),\qquad \mu(S)=a_S^2,\qquad X\sim\mu.
\]
Then
\[
H(f)=H(X),\qquad p_i=\Pr(i\in X)=\operatorname{Inf}_i(f).
\]

At every tree node multiply by the coordinatewise median character, so
\[
0\le p_i\le\frac12.
\]
This translation of the spectrum preserves entropy and the folded quantities
\[
J(f):=\sum_i\min(p_i,1-p_i)=\sum_i p_i=I(f),
\]
and
\[
\Phi(f):=\sum_i\eta(p_i).
\]
After every restriction, recenter the child in the same way. Character multiplication does not alter the spectral entropy of a physical or affine restriction child.

Put
\[
\mathcal E(f):=H(f)-\Phi(f).
\]

## 2. A genuine affine coalescence restriction

Let
\[
\mathcal P=\{B_1,\ldots,B_m\}
\]
be any partition of the current coordinate set into nonempty buckets. Choose one anchor `a_b in B_b` for each bucket. Perform the invertible linear change of variables
\[
y_{a_b}=x_{a_b},\qquad
y_i=x_i+x_{a_b}\quad(i\in B_b\setminus\{a_b\}),
\]
with addition in `F_2`.

Now uniformly restrict all nonanchor coordinates `y_i`. Each child `g_z` is a genuine Boolean function on the `m` surviving quotient variables `y_{a_b}`. This is a restriction to affine subspaces, not a basis-only relabelling.

On the Fourier side the surviving quotient spectral bit is
\[
Y_b=\bigoplus_{i\in B_b} X_i.
\]
Indeed, writing an original character in the new variables gives
\[
\sum_{i\in B_b}X_i x_i
=
\left(\bigoplus_{i\in B_b}X_i\right)y_{a_b}
+\sum_{i\in B_b\setminus\{a_b\}}X_i y_i.
\]
Thus the quotient spectral label is
\[
Y=(Y_1,\ldots,Y_m).
\]

Let
\[
r_b=\Pr(Y_b=1),\qquad q_b=\min(r_b,1-r_b),\qquad
Q_{\mathcal P}=\sum_b q_b.
\]

### Theorem 2.1 -- exact affine entropy decomposition

For every Boolean `f`, every partition `P`, and every choice of anchors,
\[
\boxed{
\Delta_{\mathcal P}H
:=H(f)-\mathbb E_z H(g_z)
=
H(X\mid Y)+JS_{\mathcal P},
}
\]
where
\[
JS_{\mathcal P}
:=
H(Y)-\mathbb E_z H(g_z)\ge0.
\]

**Proof.** Walsh orthogonality in the uniformly fixed nonanchor variables says that the average child spectral law on the surviving quotient label is exactly the pushforward law of `Y`. Therefore `JS_P` is the Jensen--Shannon mutual information between the restriction label and the final quotient spectral label. Since `H(X)=H(Y)+H(X|Y)`, the displayed identity follows. QED.

## 3. PROVED: nonnegative centered influence drop for every affine partition

Define the actual centered budget drop
\[
D_{\mathcal P}(f)
:=
J(f)-\mathbb E_zJ(g_z),
\]
where every child is recentered before evaluating `J`.

### Theorem 3.1 -- folded quotient lower bound

For every median-centered Boolean parent,
\[
\boxed{
D_{\mathcal P}\ge J-Q_{\mathcal P}\ge0.
}
\]

**Proof.**
In the transformed parent, the influence of quotient coordinate `y_{a_b}` is exactly `r_b`. Influence is a martingale under uniform restrictions of the other transformed coordinates, so if `r_{z,b}` is its influence in child `z`,
\[
\mathbb E_zr_{z,b}=r_b.
\]
The map `u -> min(u,1-u)` is concave, hence
\[
\mathbb E_z\min(r_{z,b},1-r_{z,b})
\le
\min(r_b,1-r_b)=q_b.
\]
Summing over buckets gives
\[
\mathbb E_zJ(g_z)\le Q_{\mathcal P},
\]
and therefore the first inequality.

For the second, since the parent is centered,
\[
q_b\le r_b
=\Pr\!\left(\bigoplus_{i\in B_b}X_i=1\right)
\le\Pr(X\cap B_b\ne\varnothing)
\le\sum_{i\in B_b}p_i.
\]
Summing over disjoint buckets yields `Q_P<=J`. QED.

This theorem is important operationally: an affine change of variables can make ordinary influence behave badly, but the **actual quotient child cost**, after folding/recentering, is still bounded by the original-coordinate root budget. No transformed-coordinate cost is silently discarded.

## 4. PROVED: corrected-entropy affine partition rebate

For each bucket choose the anchor maximizing `eta(p_i)` and write
\[
M_{\mathcal P}:=
\sum_b\max_{i\in B_b}\eta(p_i).
\]

Define the quotient-potential Jensen gap
\[
G_{\mathcal P}
:=
\sum_b\left[
\eta(q_b)
-
\mathbb E_z\eta\!\left(\min(r_{z,b},1-r_{z,b})\right)
\right]\ge0.
\]
Nonnegativity follows because
`u -> eta(min(u,1-u))` is concave on `[0,1]`.

### Theorem 4.1 -- affine corrected-entropy charge

For every median-centered Boolean parent and every affine coalescence partition,
\[
\boxed{
\Delta_{\mathcal P}\mathcal E
\le
H(X\mid Y)
+\sum_b\eta(q_b)
-M_{\mathcal P}
-G_{\mathcal P}.
}
\tag{4.1}
\]

**Proof.**
In the transformed parent, each restricted nonanchor coordinate `y_i` flips exactly the original coordinate `x_i`, so its transformed influence is the original `p_i`. Apply the already proved physical block-Jensen--Shannon tensorization to the entire nonanchor block:
\[
JS_{\mathcal P}
\le
\sum_b\sum_{i\in B_b\setminus\{a_b\}}\eta(p_i)
=
\Phi(f)-M_{\mathcal P}.
\tag{4.2}
\]

By definition of `G_P`,
\[
\mathbb E_z\Phi(g_z)
=
\sum_b\eta(q_b)-G_{\mathcal P}.
\tag{4.3}
\]
Subtract (4.3) from the parent potential, combine with Theorem 2.1 and (4.2):
\[
\begin{aligned}
\Delta_{\mathcal P}\mathcal E
&=
H(X\mid Y)+JS_{\mathcal P}
-\Phi(f)+\mathbb E_z\Phi(g_z)\\
&\le
H(X\mid Y)
+\sum_b\eta(q_b)
-M_{\mathcal P}
-G_{\mathcal P}.
\end{aligned}
\]
QED.

The point is not merely another nonnegative potential. Equation (4.1) identifies the exact new unpaid term under this affine geometry: **parity-hash erasure** `H(X|Y)`, offset by the anchor and quotient-potential rebates.

## 5. PROVED: a globally summable hybrid physical/affine tree

At each node:
1. median-character center;
2. choose a nontrivial affine coalescence partition as above, or a previously justified physical split;
3. uniformly branch over its restriction labels;
4. recenter every child.

Every nontrivial affine partition reduces dimension. Continue to one-bit characters/constants.

Let `pi_v` be the probability of reaching internal node `v`, `D_v` its actual centered drop, and `Delta_v E` its corrected-entropy decrement.

### Theorem 5.1 -- exact global telescope

Every complete adaptive tree of these operations satisfies
\[
\boxed{\sum_v\pi_vD_v=J(f)}
\]
and
\[
\boxed{\sum_v\pi_v\Delta_v\mathcal E=\mathcal E(f)}.
\]

**Proof.**
At each node, by definition,
\[
J(\text{parent})=D_v+\mathbb E J(\text{child}),
\]
and
\[
\mathcal E(\text{parent})
=\Delta_v\mathcal E+\mathbb E\mathcal E(\text{child}).
\]
Multiply by reach probabilities and telescope. Centered character/constant leaves have `H=Phi=J=0`. QED.

Hence if an adaptive strategy can ensure at every selected node
\[
\Delta_v\mathcal E\le C D_v
\]
for one universal `C`, then
\[
\mathcal E(f)\le CJ(f)
\]
and therefore
\[
\boxed{
H(f)\le\left(C+\frac2{\ln2}\right)I(f).
}
\tag{5.1}
\]
This is a genuine global compiler with no budget reuse.

## 6. PROVED NEW IMPLICATION: shell-poor mass gives one spendable affine drop

This section resolves the specific nonspendability gap left by the previous pair-affine report.

For a centered spectral sample put
\[
K=|X|,\qquad
W_1=\Pr(K=1),\qquad
r_c=W_1/J
\quad(J>0).
\]

Fix an integer `m>=2`. Independently color every physical coordinate with one of `m` labels, uniformly. The nonempty color classes form a random affine coalescence partition. Empty labels are discarded.

For a fixed spectral set of size `k`, let `N_{\rm odd}` be the number of color classes hit an odd number of times. Its expectation is
\[
u_m(k)
=
\frac m2\left[1-\left(1-\frac2m\right)^k\right].
\tag{6.1}
\]
Indeed, for any fixed color the parity of `k` independent Bernoulli-`1/m` hits is odd with probability
\[
\frac12\left[1-\left(1-\frac2m\right)^k\right].
\]

For the random coloring `h`, let `Q_h` be the sum of folded quotient parity influences. Since `min(r,1-r)<=r`,
\[
Q_h
\le
\sum_b\Pr(Y_b=1).
\]
Averaging first in the coloring and then in `X` gives
\[
\boxed{
\mathbb E_h[J-Q_h]
\ge
\mathbb E\,[K-u_m(K)].
}
\tag{6.2}
\]

The right side is already a useful exact level-profile lower bound. It has a simple first-shell corollary.

Write
\[
a=1-\frac2m.
\]
Because
\[
u_m(k)=1+a+\cdots+a^{k-1},
\]
for every `k>=2`,
\[
u_m(k)\le k\left(1-\frac1m\right).
\tag{6.3}
\]
For `k=2` this is equality. For `k>2`, the average of the first two terms is exactly `1-1/m`, while every later term is at most `a<=1-1/m`.

Thus
\[
K-u_m(K)\ge\frac Km\,1_{\{K\ge2\}},
\]
and therefore
\[
\boxed{
\mathbb E_h[J-Q_h]
\ge
\frac{J-W_1}{m}
=
\frac{1-r_c}{m}J.
}
\tag{6.4}
\]

By Theorem 3.1 the actual centered drop satisfies `D_h>=J-Q_h`. Hence:

### Theorem 6.1 -- spendable random-coalescence selector

For every noncharacter median-centered Boolean function and every integer `m>=2`, there exists a genuine affine coalescence restriction with at most `m` quotient variables such that
\[
\boxed{
D_h
\ge
\mathbb E[K-u_m(K)]
\ge
\frac{1-r_c}{m}J.
}
\tag{6.5}
\]

This is an **existential affine restriction**. It is not an every-coordinate or every-partition payment statement.

For `m=2`,
\[
u_2(0)=0,\qquad u_2(k)=1\ (k\ge1),
\]
so the sharper exact profile guarantee is
\[
\boxed{
D_h\ge\mathbb E[(K-1)_+].
}
\tag{6.6}
\]

### Quantified before/after at the inherited hard-core scale

The earlier centered physical selector proved that a hypothetical counterexample above
\[
C_0=6.521845710923046575
\]
has a physical restriction-critical descendant with
\[
r_c<0.3156061323581677.
\]
Apply Theorem 6.1 with `m=2` to that same centered descendant. There is one valid affine quotient step with
\[
\boxed{
D_h>
\frac{1-0.3156061323581677}{2}J
=
0.34219693382091615\,J.
}
\tag{6.7}
\]

**Before:** the pair theorem guaranteed total available pair base mass
`>0.6843938676418323 J`, but warned that this sum could not be spent at one node.

**After:** one actual affine restriction spends
`>0.34219693382091615 J` in a single tree step. The denominator in the sought local payment is therefore no longer allowed to vanish in this shell-poor hard regime.

This is the main universal-facing change of the run.

## 7. Affine corrected-critical cores and the exact remaining tube

Consider all noncharacter descendants reachable by the affine coalescence operations above (and recentering). Choose one maximizing
\[
\rho=\frac{\mathcal E}{J},
\]
and among maximizers choose minimum dimension.

For every nontrivial affine partition first step, every positive-`J` child has corrected ratio strictly below `rho`. Therefore
\[
\Delta_{\mathcal P}\mathcal E\ge \rho D_{\mathcal P}.
\]
Combining Theorems 3.1 and 4.1 yields the all-partition necessary condition
\[
\boxed{
\rho\,(J-Q_{\mathcal P})
\le
H(X\mid Y)
+\sum_b\eta(q_b)
-M_{\mathcal P}
-G_{\mathcal P}.
}
\tag{7.1}
\]

This is an **affine parity-hash critical tube** on a genuine Boolean minimal descendant. It is stronger than a statement about every weak ratio-critical function: tensor replication can remain weakly critical while changing shell statistics, whereas the minimum-dimension maximizer here is selected from the actual affine descendant family.

Equation (7.1) also states the remaining universal obligation exactly. To close FEI by this route it would suffice to show that every sufficiently high corrected-ratio Boolean state has some affine coalescence partition for which
\[
H(X\mid Y)
+\sum_b\eta(q_b)
-M_{\mathcal P}
-G_{\mathcal P}
\le C\,
D_{\mathcal P}
\tag{7.2}
\]
with a dimension-independent `C`.

Theorem 6.1 now guarantees a constant-fraction **actual** denominator for a two-color quotient in the previously hard shell-poor regime. What is still unpaid is the parity-hash erasure `H(X|Y)`. Sign-free parity profiles cannot pay it universally: the current interactive handoff already contains an all-dimensional non-Boolean family satisfying extensive scalar parity tests with unbounded entropy/influence ratio. A future closure must therefore use genuine Boolean signed/convolution structure, not merely optimize the distribution of `K` or parity marginals.

## 8. Preserved failures and quantifiers

Nothing here revives the known-false prescribed-coordinate payment. A partition is selected existentially; no claim is made for every pair, every coordinate, or every affine partition.

The older weak-critical shell claim remains false by tensor replication. The shell fraction is used only on the specially selected physical restriction-critical descendant where the earlier theorem proved it.

The previous pair supply is not retrospectively treated as simultaneously spendable. The new spendability result comes from a single randomized coalescence operation and the exact telescoping drop `D_P`.

No pointwise inequality `H<=B+cI` is inferred from a comparison of universal suprema. The known erasure-constant-four proposal remains false.

The fresh global phase/rank/l1 and sign-free parity-profile relaxations remain refuted at their recorded scopes and are not reopened.

## 9. Finite regression and execution scope

A standard-library checker independently implements:
- median-character centering;
- the genuine affine partition children;
- the quotient parity pushforward;
- `D_P >= J-Q_P`;
- the exact entropy decomposition;
- the block-JS anchor bound;
- the corrected-entropy rebate (4.1); and
- the random-colouring lower bound (6.4).

The captured run
`python -S verify_affine_partition_budget.py`
exited `0`. It exhausts Boolean functions modulo global output sign for dimensions `1,2,3` and uses a deterministic broad sample of `3,963` dimension-four functions. It checked:
- `4,101` functions,
- `56,002` affine partitions, and
- `8,170` random-colouring budget instances.

Maximum observed violations of the entropy identity, JS bound, corrected bound, and minimum slacks in the nonnegative inequalities were all `0` at the recorded floating precision. This is regression evidence only; the analytic theorems above do not depend on finite enumeration.

An attempted full dimension-four expansion was abandoned after exceeding the current single-call execution envelope before producing a completed result. No partial output from that attempt is used or described as exhaustive.

## 10. Literature/status boundary

Current primary literature still treats unrestricted FEI as open. González--MacManus--Pereyra (2026) develop a restriction-decrement/stopping-tree framework in which local paid decrements compile to FEI. Potapov (2026) proves the conjecture for plateaued and partially bent functions, not universally. The present affine coalescence theorem is therefore recorded only as an internal partial mechanism; search failure is not novelty evidence.

## 11. Full-problem and mechanism ledger

**FULL-PROBLEM CHANGE:** NO FULL-BOUND MOVEMENT. Full FEI remains OPEN / NOT PROVED.

**MECHANISM CHANGE:** YES.
- Before: shell-poor criticality forced `>0.6843938676 J` aggregate pair-affine drop supply, explicitly nonspendable at one node.
- After: a random affine coalescence theorem proves existence of one real restriction spending `>0.3421969338 J` at the inherited hard-core calibration.
- New exact corrected affine charge: (4.1).
- New global tree compiler: (5.1).
- Remaining quantified residual: prove one partition satisfying (7.2), i.e. pay the genuine parity-hash erasure `H(X|Y)` by the same nonreused centered drop using Boolean signed structure.

That residual, rather than another scalar threshold evaluation, is the next B14 target.
