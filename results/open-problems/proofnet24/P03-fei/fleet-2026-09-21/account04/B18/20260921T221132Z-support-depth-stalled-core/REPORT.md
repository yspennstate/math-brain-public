# B18 FEI proof integration — activation-compatible stalled cores and support-depth localization

**Run:** `20260921T221132Z-b18-fei-r15`  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Scientific source snapshot:** `yspennstate/math-open-problems@fd176bb4507d29cbf30fd7ad27cad5291bb3fe59`  
**Status:** **PARTIAL. Full uniform-cube Fourier entropy--influence remains OPEN / NOT PROVED.**  
**Claim level:** source-exact universal auxiliary theorems and a sharper primitive-core reduction. No novelty or publication-priority claim.

## 0. What changed this run

The newest compatible account01/B18 result replaces the fixed-gauge activation bank by the character-invariant folded potential
\[
 \mathcal A_z(f)=\min_T\sum_S\widehat f(S)^2\Phi_z(|S\triangle T|),
\]
proves a globally nonreused physical-restriction telescope even when descendants re-center, and introduces
\[
 \mathcal G_\lambda(f)
 =\mathcal F(f)-\lambda\mathcal A_{z_d}(f),
 \qquad
 \mathcal F=H-\mathcal C .
\]
The fresh account02/B14 stationary-selector result, which landed during this invocation, proves that every nonempty **closed** family of sufficiently accurate near-subcube pivot rows contains a row whose control block satisfies the already proved coefficient-12 physical entropy payment. Its adaptive compiler therefore localizes any `H/J>12` obstruction to a stalled state with empty certified trigger kernel.

This report integrates those interface-A results with the account04/B18 mixed-curvature law and the newest account04/B12--B14 interface-B/A steps. The main new points are:

1. the pivotality-depth quantity `M` used by the posterior-variance selector is **exactly the unsigned-support part** of the B18 mixed-curvature/second-factorial bank:
   \[
   \boxed{\sum_i d_i=M+\sum_{i\ne k}o_{ik}};
   \]
2. consequently the physical near-subcube trigger load is paid by `M` itself, not merely by the larger raw depth bank:
   \[
   \boxed{\sum_{i\in R}j_i|F_i|
      \le \frac{2}{1-2\varepsilon}M};
   \]
3. the account01 folded activation potential is compatible with the coefficient-12 stationary physical compiler: any counterexample to
   \[
   \mathcal G_\lambda\le12J
   \]
   has a physical descendant that is simultaneously a `G_lambda/J` critical core and has **empty closed C12-certified trigger kernel**;
4. on that critical core the B14 Bernoulli posterior-variance selector gives a new activation-compatible product obstruction
   \[
   \boxed{(8M-2J)S_\rho\ge \rho J^2},
   \qquad
   S_\rho:=\sum_i[h_2(j_i)-\rho j_i].
   \]

This isolates the live obstruction more sharply. The opposite-sign overlap part of mixed curvature cannot masquerade as the B14 high-depth branch; the latter is exactly support disagreement. The remaining universal work is the stalled/kernel-free, fixed-relative error-discovery and exceptional-row sector. Full FEI is not closed.

## 1. Exact inputs consumed

All statements below use the current median-character normalization, so every active folded influence obeys
\[
 0<j_i=\operatorname{Inf}_i(f)\le\frac12,
 \qquad J=\sum_i j_i.
\]

The exact completed inputs used substantively are:

1. **account01/B18**,  
   `proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260921T2205Z-folded-cooling-compiler/REPORT.md`,  
   Git blob `9f2bb40584be20e5e440e7f3913873c34858bc91`.  
   Used for the folded activation potential, its descendant-recentering telescope, and the inequality
   \[
     \Delta_A\mathcal G_\lambda
     \le E_A-\lambda\Lambda_A
     \le E_A\le B_A .
     \tag{1.1}
   \]

2. **account04/B12**,  
   `.../account04/B12/20260921T212331Z-factorial-trigger-address/REPORT.md`,  
   Git blob `d21168c13eb0ba0a52a38691206b0d726727eb79`.  
   Used for the exact factorial Palm partition and the robust address payment
   \[
   \frac3{16}\sum_{i\in R_{\rm Palm}}
       j_i\log_2(|F_i|+1)
   \le \mathbb E\log_2(K!).
   \tag{1.2}
   \]

3. **account04/B13**,  
   `.../account04/B13/20260921T2122Z-source-frontier-one-shot/REPORT.md`,  
   Git blob `8cced1e67ed2181463caaf877946717e81e4e7c8`.  
   Used for the one-shot robust quotient-DAG reveal block, the residual estimate
   \[
   \mathbb E J(\text{child})
   \le J_E+\varepsilon J_R,
   \tag{1.3}
   \]
   and its previous representative-trigger load estimate through raw depth.

4. **account04/B14**,  
   `.../account04/B14/20260921T211337Z-posterior-variance-short-circuit/REPORT.md`,  
   Git blob `dd147272df8df45d1284474bf5a04eeaaf1b908e`.  
   Used for the pivotality-depth variable
   \[
   M=\frac14\sum_i\sum_{k\ne i}\operatorname{Inf}_k(\eta_i),
   \tag{1.4}
   \]
   the Bernoulli-reveal crossing curve, and the certified physical near-subcube block theorem.

5. **account02/B14**, newly completed during this invocation,  
   `.../account02/B14/20260921T220126Z-stationary-trigger-selector/REPORT.md`,  
   Git blob `46d1c34d488bb5d4e97f2cbfa897f626e3c55f6c`.  
   Used for the closed-trigger stationary selector and the physical coefficient-12 adaptive compiler. This avoids reproving its already completed selector.

6. **account04/B18**,  
   `.../account04/B18/20260921T191147Z-mixed-curvature-global-rigidity/REPORT.md`,  
   Git blob `0e8c2cc28da81af8843b565cb47285684b164480`.  
   Used for
   \[
    \kappa_{ik}=p_{ik}+4o_{ik}=\kappa_{ki},
    \qquad
    \sum_{i\ne k}(p_{ik}+4o_{ik})=4d_k,
    \tag{1.5}
   \]
   and the exact all-zero-depth classification.

The known false bridges remain excluded: `sum d_i=O(J)`, prescribed-coordinate payment, ambient-alphabet Fannes continuity, the fixed-relative full-block entropy claim, and the unconditional `R_pref=O(I)` claim.

## 2. PROVED: B14 pivotality depth is exactly the support part of B18 mixed curvature

For a derivative row
\[
 g_i=D_i f\in\{0,\pm1\},
 \qquad E_i=\{g_i\ne0\},
 \qquad \eta_i=1_{E_i},
\]
write
\[
 p_{ik}
 =\Pr[\eta_i(y)\ne\eta_i(y+e_k)]
 =\operatorname{Inf}_k(\eta_i),
\]
and
\[
 o_{ik}
 =\Pr[g_i(y)=-g_i(y+e_k)\ne0].
\]
The B18 mixed-curvature identity is
\[
 \kappa_{ik}=p_{ik}+4o_{ik}
\]
and, with
\[
 d_i=\sum_{k\ne i}\|D_k g_i\|_2^2,
\]
\[
 \sum_{k\ne i}\kappa_{ik}=4d_i.
\]

Define
\[
 M:=\frac14\sum_{i\ne k}p_{ik},
 \qquad
 O:=\sum_{i\ne k}o_{ik},
 \qquad
 D:=\sum_i d_i.
\]

### Theorem 2.1 — exact support/orientation split
\[
 \boxed{D=M+O.}
 \tag{2.1}
\]

### Proof
Sum `kappa_ik=p_ik+4o_ik` over all ordered pairs and divide by four:
\[
 \sum_i d_i
 =\frac14\sum_{i\ne k}\kappa_{ik}
 =\frac14\sum_{i\ne k}p_{ik}
  +\sum_{i\ne k}o_{ik}
 =M+O.
\]
QED.

The account04/B12 Palm identity gives, for the spectral sample `S`,
\[
 q_{ik}:=\Pr(i,k\in S)=\frac{\kappa_{ik}}4.
\]
Hence
\[
 \boxed{
 D=\sum_{i\ne k}q_{ik}
   =\mathbb E[K(K-1)]
   =M+O.
 }
 \tag{2.2}
\]

This is the exact interface-A/interface-B identification that was missing from the current ledgers:

* `M` is the **support-disagreement** share of the second-factorial spectral bank;
* `O` is the **opposite-sign/orientation** share;
* B14 posterior-variance crossing sees `M`, not `O`.

Therefore a state whose raw depth is large only because of sign flips is not a hidden "high-M" obstruction to the posterior-variance selector.

## 3. PROVED: physical robust trigger load is paid by M, not by total depth

Let `R` be any collection of physical near-subcube rows. For each `i in R`, suppose
\[
 Q_i=\{x_{F_i}=a_i\},
 \qquad
 s_i=\mu(Q_i)=2^{-|F_i|},
\]
and
\[
 e_i:=\mu(E_i\triangle Q_i)
 \le\varepsilon j_i,
 \qquad 0\le\varepsilon<\frac12.
 \tag{3.1}
\]
Put `r_i=|F_i|`.

For every `k in F_i`, the coordinate-subcube boundary perturbation estimate gives
\[
 p_{ik}\ge2(s_i-e_i).
\]
Because `|s_i-j_i|\le e_i`,
\[
 s_i-e_i
 \ge j_i-2e_i
 \ge(1-2\varepsilon)j_i.
\]
Thus
\[
 p_{ik}\ge2(1-2\varepsilon)j_i.
 \tag{3.2}
\]

### Theorem 3.1 — support-depth trigger-load bound
\[
 \boxed{
 \sum_{i\in R}j_i r_i
 \le \frac{2}{1-2\varepsilon}\,M.
 }
 \tag{3.3}
\]

### Proof
Sum (3.2) over the actual trigger incidences and then enlarge to all ordered row/direction pairs:
\[
 2(1-2\varepsilon)\sum_{i\in R}j_i r_i
 \le
 \sum_{i\in R}\sum_{k\in F_i}p_{ik}
 \le
 \sum_{i\ne k}p_{ik}
 =4M.
\]
Divide. QED.

At the live fixed-relative threshold `epsilon=1/16`,
\[
 \boxed{
 \sum_{i\in R}j_i|F_i|
 \le\frac{16}{7}M.
 }
 \tag{3.4}
\]

This strictly sharpens the current account04/B13 one-shot trigger-load recipient from
`(16/7) sum d_k` to `(16/7) M`, because `M<=sum d_k` with equality exactly when the opposite-sign overlap bank vanishes.

### Corollary 3.2 — robust marginal entropy localization
From `s_i<= (1+\varepsilon)j_i`,
\[
 \log_2\frac1{j_i}
 \le r_i+\log_2(1+\varepsilon).
\]
Also
\[
 h_2(x)
 \le x\left(\log_2\frac1x+\frac1{\ln2}\right)
 \qquad(0<x\le1/2).
\]
Therefore
\[
 \boxed{
 \sum_{i\in R}h_2(j_i)
 \le
 \frac{2}{1-2\varepsilon}M
 +
 \left[
   \log_2(1+\varepsilon)+\frac1{\ln2}
 \right]J_R.
 }
 \tag{3.5}
\]
At `epsilon=1/16`,
\[
 \sum_{i\in R}h_2(j_i)
 \le
 \frac{16}{7}M
 +1.530157883\,J_R.
 \tag{3.6}
\]

This is not an FEI proof: `M` is not declared `O(J)`. The gain is exact localization of the robust marginal cost to the support-curvature bank plus a linear term.

## 4. PROVED: the folded activation critical core inherits a posterior-depth product obstruction

Use the newest account01 potential
\[
 \mathcal G_\lambda
 =\mathcal F-\lambda\mathcal A_{z_d},
 \qquad\lambda\ge0.
\]
Let a nonconstant centered physical state maximize
\[
 \rho=\frac{\mathcal G_\lambda}{J}
\]
over its physical-restriction descendants. Then for every physical block `A`,
\[
 \Delta_A\mathcal G_\lambda
 \ge \rho D_A,
 \qquad
 D_A=I_A+C_A.
 \tag{4.1}
\]
By the account01 folded-cooling theorem,
\[
 \Delta_A\mathcal G_\lambda
 \le E_A-\lambda\Lambda_A
 \le B_A.
 \tag{4.2}
\]
Subadditivity of the spectral marginal entropy gives
\[
 B_A\le\sum_{i\in A}h_2(j_i).
\]
Hence
\[
 \rho C_A
 \le
 \sum_{i\in A}[h_2(j_i)-\rho j_i].
 \tag{4.3}
\]

In particular singleton blocks show each scalar bracket is nonnegative.

Let `A_t` include each physical coordinate independently with probability `t` and put `s=1-t`. Account04/B14 proves
\[
 \mathbb E C_{A_t}
 \ge
 s[J-2sM]_+.
 \tag{4.4}
\]
It also proves `M>=J/2`, so
\[
 s_*=\frac{J}{4M}\le\frac12
\]
is legal. At this value,
\[
 \mathbb E C_{A_{t_*}}\ge\frac{J^2}{8M}.
\]
Average (4.3):
\[
 \rho\frac{J^2}{8M}
 \le
 \left(1-\frac{J}{4M}\right)
 S_\rho,
 \qquad
 S_\rho:=\sum_i[h_2(j_i)-\rho j_i].
\]
Therefore:

### Theorem 4.1 — activation-compatible support-depth obstruction
\[
 \boxed{
 (8M-2J)S_\rho\ge\rho J^2.
 }
 \tag{4.5}
\]

This holds for every fixed `lambda>=0`. It is the B14 critical-core product obstruction transported to the **newest descendant-recentered activation potential**. No activation credit is double-counted: the proof discarded the nonnegative `lambda Lambda_A` refund.

Using Theorem 2.1, (4.5) can be written
\[
 \boxed{
 [8(D-O)-2J]S_\rho\ge\rho J^2.
 }
 \tag{4.6}
\]
Thus the high-depth branch in this critical-core argument is specifically `D-O=M`, not arbitrary mixed depth `D`.

A useful quantified form is: for any `L>1/2`,
\[
 M\le LJ
 \quad\Longrightarrow\quad
 S_\rho\ge\frac{\rho}{8L-2}\,J.
 \tag{4.7}
\]
If this scalar surplus is not available, the support-disagreement bank `M` must be large.

## 5. PROVED: C12-certified physical rows are completely paid at G_lambda level

Use the account04/account02 certified near-subcube hypothesis. For an active pivot `j`, let `Z` be a nonempty physical control block of size `r`, let
\[
 q=2^{-r},
\]
and suppose its pivotality event obeys
\[
 \delta:=\mu(E_j\triangle Q)\le\frac{q}{16r},
 \tag{5.1}
\]
while
\[
 I_Z:=\sum_{k\in Z}j_k\le rj_j.
 \tag{5.2}
\]
The inherited physical theorem gives
\[
 \Delta_ZH\le12I_Z.
 \tag{5.3}
\]

### Theorem 5.1 — direct critical-ratio cap
If the current state is `G_lambda/J`-critical with ratio `rho`, then
\[
 \boxed{\rho\le12.}
 \tag{5.4}
\]

### Proof
For this actual physical block,
\[
 \rho D_Z
 \le\Delta_Z\mathcal G_\lambda
 \le E_Z
 \le\Delta_ZH
 \le12I_Z
 \le12D_Z.
\]
The certified block is nontrivial, so `D_Z>0`; divide by it. QED.

This is stronger than routing the same row through the generic crossing compiler.

### Compatibility with the newest account01 certificate

The same row is nevertheless an explicit account01 certificate. The full control reveal has
\[
 c_j(Z)\ge j_j-\delta.
\]
Since `|j_j-q|\le\delta`,
\[
 \frac{\delta}{j_j}
 \le\frac1{16r-1}
 \le\frac1{15},
\]
hence
\[
 \boxed{c_j(Z)\ge\frac{14}{15}j_j.}
 \tag{5.5}
\]

Also `j_j<=q(1+1/(16r))`. For `j_j<=1/2`,
\[
 \frac{h_2(j_j)}{j_j}
 =
 \log_2\frac1{j_j}
 +
 \frac{1-j_j}{j_j}\log_2\frac1{1-j_j}.
\]
The first term is at least
\[
 r-\log_2(1+1/(16r)),
\]
while the second is at least `(1-j_j)/ln2 >=1/(2ln2)`, which is larger than
`log_2(1+1/(16r))`. Therefore
\[
 \boxed{rj_j\le h_2(j_j).}
 \tag{5.6}
\]
Consequently
\[
 E_Z-\lambda\Lambda_Z
 \le12I_Z
 \le12h_2(j_j),
\]
so `(Z,j)` is a `(gamma,K,lambda)` folded-cooling certificate with
\[
 \boxed{\gamma=14/15,\qquad K=12}
 \tag{5.7}
\]
for every `lambda>=0`. The generic account01 compiler would cap the critical ratio by `405/7`, but the direct physical argument (5.4) gives the stronger cap `12`.

## 6. PROVED: activation-compatible stalled-leaf compiler

The fresh account02/B14 stationary theorem says that every nonempty **closed** finite family of C12-certified rows contains a row satisfying (5.2). It then executes that physical block and recursively prunes until either a character or a state with empty closed certified kernel is reached.

At every successful node, Theorem 5.1's underlying estimate gives
\[
 \Delta\mathcal G_\lambda
 \le\Delta H
 \le12I_A
 \le12D_A.
 \tag{6.1}
\]
Therefore exactly the same physical tree telescopes at the activation-refunded level:

### Theorem 6.1 — folded stalled-leaf reduction
For the account02 stationary C12 policy,
\[
 \boxed{
 \mathcal G_\lambda(f)-12J(f)
 \le
 \mathbb E_{\ell}
 [\,\mathcal G_\lambda(f_\ell)-12J(f_\ell)\,].
 }
 \tag{6.2}
\]
Character leaves contribute zero, so only stalled leaves matter.

Equivalently, if there exists any function with
\[
 \frac{\mathcal G_\lambda}{J}>12,
\]
then there is a physical descendant with the same strict inequality and **empty nonempty closed C12-certified trigger subsystem**.

One can sharpen this to a critical primitive state: among all physical descendants with positive `G_lambda/J`, choose a maximizer. If its ratio exceeds `12`, Theorem 5.1 plus the stationary selector shows immediately that its closed C12 kernel is empty. Thus a single state can be assumed simultaneously:

* `G_lambda/J`-critical;
* ratio `rho>12`;
* stalled / empty closed C12-certified kernel;
* subject to the product obstruction (4.5).

This is the smallest honest universal core produced by the current A/B machinery.

Finally,
\[
 H
 =\mathcal G_\lambda+\lambda\mathcal A_{z_d}+\mathcal C
 \le
 \mathcal G_\lambda+
 \left(\lambda+\frac2{\ln2}\right)J.
\]
Therefore proving
\[
 \mathcal G_\lambda\le12J
\]
only on the stalled primitive class would yield full FEI with
\[
 H\le
 \left(12+\lambda+\frac2{\ln2}\right)I.
 \tag{6.3}
\]
This is **CONDITIONAL** because the stalled-class inequality is still open.

## 7. PROVED: fixed-relative robust mass in a high critical core must feed M or the exceptional sector

Now let `R` be the account04/B13 fixed-relative physical robust sector with `epsilon=1/16`, and let `E` be its complement. Put
\[
 J_R=\sum_{i\in R}j_i,\qquad J_E=J-J_R.
\]

At a `G_lambda/J` critical state of ratio `rho`, singleton criticality gives
\[
 \frac{h_2(j_i)}{j_i}\ge\rho
 \qquad(i\text{ active}).
 \tag{7.1}
\]
For a robust row, Corollary 3.2 gives
\[
 \frac{h_2(j_i)}{j_i}
 \le r_i+c_*,
 \qquad
 c_*=
 \log_2\frac{17}{16}+\frac1{\ln2}
 =1.530157882\ldots.
\]
Therefore
\[
 r_i\ge\rho-c_*.
\]
Combine with Theorem 3.1:
\[
 M
 \ge\frac7{16}\sum_{i\in R}j_i r_i
 \ge\frac7{16}(\rho-c_*)J_R.
 \tag{7.2}
\]

### Corollary 7.1 — robust/exceptional dichotomy
\[
 \boxed{
 \frac{J_R}{J}
 \le
 \frac{16}{7(\rho-c_*)}\frac{M}{J}.
 }
 \tag{7.3}
\]
In particular, if `rho>12`, then either
\[
 \boxed{J_E>\frac12J}
\]
or
\[
 \boxed{
 \frac MJ
 >
 \frac7{32}(12-c_*)
 =
 2.290277963\ldots.
 }
 \tag{7.4}
\]

This does not pay either branch. It makes the remaining obstruction explicit: a high-ratio critical stalled state cannot be simultaneously dominated by fixed-relative robust rows **and** have small support-disagreement depth.

For robust Palm rows, account04/B12 already pays the trigger-address term through (1.2). Thus in the overlapping robust physical/Palm sector:

* logarithmic trigger **address** is factorial-paid;
* linear trigger **codimension load** is support-depth-paid by `M`;
* closed C12 subfamilies are physically paid and removed;
* what remains is the fixed-relative error-discovery / stop-conditioned dependence and the exceptional endpoint sector.

## 8. Exact zero-defect branch and preserved refutations

The account04/B18 zero-depth theorem remains untouched:

> if every relevant derivative row has exact zero depth defect, the median-folded Boolean function is a character-twisted one-point defect (up to sign and irrelevant variables), and `H<4J`.

Since `G_lambda<=H`, such a state cannot be a `rho>12` primitive core. Thus every stalled primitive obstruction above 12 has genuine positive-defect content.

The following shortcuts remain explicitly **REFUTED / FORBIDDEN** in this chain:

1. `sum_i d_i=O(J)` — false/unproved and not used;
2. fixed-relative `q/16` **full-block** entropy payment — refuted;
3. prescribed-coordinate cheap restriction — addressing obstruction remains;
4. `R_pref=O(I)` for unconditional prefix total correlation — refuted by the bent family; only the stop-conditioned repair remains live;
5. TV/Fannes conversion over an ambient alphabet — not used;
6. treating finite enumeration as a proof — not done.

## 9. Decisive executed calculation

`check_support_depth_integration.py` was executed with exact rational arithmetic for the mixed-curvature identity on every Boolean truth table modulo global output sign through dimension four.

Results:

* Boolean functions: `32,906`;
* ordered derivative row/direction cases: `394,000`;
* violations of `D=M+O`: `0`;
* exact live robust-load constant at `epsilon=1/16`: `16/7`;
* exact C12 crossing fraction used above: `14/15`;
* direct critical-ratio cap: `12`;
* generic crossing-compiler cap from `(gamma,K)=(14/15,12)`: `405/7`;
* scalar diagnostic of `h_2(j)>=rj` at the largest allowed `j` for `1<=r<=40`: minimum ratio `1.0360119439063808` at `r=40`.

Checker SHA-256:
`a3e1d574cd5eea978d58d63b82e80ea82795d28ec2e398f3095fb0e0c79f0f00`.

Captured stdout SHA-256:
`1db7d8cdce7e956edba21589108377c822696fbc6e6e1103aaf3960e111ca294`.

The enumeration is falsification evidence only. The theorems above are analytic and all-dimensional.

## 10. Exact remaining universal implication

The current proof chain now reduces a putative violation of
\[
 H\le
 \left(12+\lambda+\frac2{\ln2}\right)I
\]
to a centered physical descendant which is simultaneously:

1. `G_lambda/J`-critical with `rho>12`;
2. C12-kernel-free under the stationary closed-trigger selector;
3. subject to
   \[
   (8M-2J)S_\rho\ge\rho J^2;
   \]
4. not in the exact zero-defect class;
5. either substantially exceptional or carrying substantial support-disagreement depth, quantitatively via (7.3)--(7.4).

The remaining arrow is **not** another selector audit. It is a genuine mathematical payment theorem on these stalled primitive states:

> extend the paid physical policy from the `q/(16r)` C12 class into the fixed-relative/error-discovery sector, or show that the support-depth `M`, the stop-conditioned prefix/factorial credits, and the exceptional-row defect banks together pay the stalled state without reuse.

The account03 fixed-relative example no longer refutes this adaptive target: its short-circuit ratio was computed to remain near four. But no universal arbitrary-error-set theorem is currently proved.

**Full uniform-cube FEI remains OPEN / NOT PROVED.**
