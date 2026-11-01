# B14 — proxy-gauge activation drop and a global low-defect nonreuse bound

**Status:** PARTIAL / new proved structural lemmas. **Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; no authenticated brain retrieval/context was available or claimed.  
**Model self-report:** GPT-5.6 Sol. Configured/provider reasoning effort: UNKNOWN / NOT_EXPOSED.  
**Route:** FEI erasure/existential-selector, but with a mechanism change from the preceding gauge-lock/product-obstruction calculation: arbitrary branch-dependent character recentering is absorbed into the folded dimension-cooling activation potential, then composed with the newest all-row proxy-gauge stability theorem.  
**Novelty/publication priority:** UNVERIFIED; no novelty claim.

## 0. Fresh compatible inputs actually consumed

This run used the current joint FEI order and the following completed results on fresh `master`.

1. **fleet04/B13**, `proofnet24/P03-fei/fleet-2026-09-21/fleet04/B13/20260921T2225Z-proxy-gauge-closure/REPORT.md`, blob `1ec1555932e690e403f7d4320640040628697b96`. It proves a one-shot physical block `B` and an explicit branch-dependent character `T(z)` such that, with
   \[
   c_z=\chi_{T(z)}f_{B=z},
   \]
   the exact proxy-gauge identity gives
   \[
   \mathbb E_z I(c_z)=\sum_{r\in S}e_r
   \le \mathcal D(f),
   \qquad
   \mathcal D(f):=\sum_i j_i\Delta_i.
   \tag{0.1}
   \]
   Here `j_i` are centered/folded influences and `Delta_i` are the nonnegative derivative-row depth defects. This peer result is used substantively below: its **varying branch character**, previously listed as part of the unpaid interface, is fed directly into the activation potential.

2. **fleet01/B18**, `proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260921T2205Z-folded-cooling-compiler/REPORT.md`. It defines the character-invariant folded activation
   \[
   \mathcal A_z(f)=\min_T\sum_S\widehat f(S)^2\Phi_z(|S\triangle T|),
   \qquad
   \Phi_z(k)=1+z+\cdots+z^{k-1},
   \tag{0.2}
   \]
   proves `0<=A_z<=J`, permits fresh character minimization after every physical restriction, and proves the nonincreasing-scale adaptive telescope.

3. **fleet02/B14**, `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B14/20260921T220126Z-stationary-trigger-selector/REPORT.md`. It proves a complementary paid physical step whenever a nonempty closed `C12` trigger subsystem exists, and localizes the remaining obstruction to a stalled trigger state. I do not reprove that result; Section 5 explains how the new activation short circuit complements it.

No settled read-once certificate was rerun and no FEI audit was performed.

## 1. New elementary coercivity of the folded activation

Let `X` be the squared-Fourier spectral sample of a Boolean function on `d` currently unqueried coordinates. Define
\[
J(f)=\min_T\mathbb E|X\triangle T|
=\sum_i\min\{\Pr(i\in X),1-\Pr(i\in X)\}.
\tag{1.1}
\]
For `d>=2`, use the dimension-cooling scale
\[
z_d=1-\frac1d,
\qquad
a_d=z_d^{d-1}.
\tag{1.2}
\]
For `d=1`, interpret `a_1=1` and the statement below directly.

### Theorem 1.1 — gauge-free activation coercivity

For every Boolean function,
\[
\boxed{
 a_d J(f)\le \mathcal A_{z_d}(f)\le J(f).
}
\tag{1.3}
\]
In particular
\[
\boxed{e^{-1}J(f)\le\mathcal A_{z_d}(f)\le J(f).}
\tag{1.4}
\]

### Proof

For every integer `0<=k<=d`,
\[
\Phi_{z_d}(k)
=\sum_{r=0}^{k-1}z_d^r
\ge k z_d^{k-1}
\ge k z_d^{d-1}
=a_d k.
\tag{1.5}
\]
Therefore for every character gauge `T`,
\[
P_{z_d}^T(f)
:=\mathbb E\Phi_{z_d}(|X\triangle T|)
\ge a_d\mathbb E|X\triangle T|.
\]
Minimizing over `T` gives the lower bound in (1.3). The upper bound follows from `Phi_z(k)<=k` and the same minimization. Finally
\[
(d-1)\log(1-1/d)>-1
\]
(for instance from `log(1-x)>-x/(1-x)`), so `a_d>e^{-1}` for finite `d>=2`; `d=1` is trivial. QED.

This is stronger for the present purpose than the previous singleton hit-probability reserve: it says the **whole folded activation bank itself is uniformly comparable to folded influence without first proving that the minimizing character equals the median gauge**.

## 2. New arbitrary branch-character absorption theorem

Let `B` be any physical restriction block. For each branch `b`, let `f_b=f_{B=b}` and let `T(b)` be an **arbitrary** character on the surviving coordinates. Put
\[
c_b=\chi_{T(b)}f_b.
\tag{2.1}
\]
Let the child cooling scale `z_b` be no larger than the parent scale `z`; in particular this holds for dimension cooling after a physical restriction.

### Theorem 2.1 — branch-dependent gauge absorption

For every branch,
\[
\boxed{
\mathcal A_{z_b}(f_b)
\le I(c_b).
}
\tag{2.2}
\]
Consequently the true adaptive folded-activation drop
\[
T_B:=\mathcal A_z(f)-\mathbb E_b\mathcal A_{z_b}(f_b)
\tag{2.3}
\]
satisfies
\[
\boxed{
T_B\ge \mathcal A_z(f)-\mathbb E_b I(c_b).
}
\tag{2.4}
\]
At the dimension-cooling parent scale,
\[
\boxed{
T_B\ge a_dJ(f)-\mathbb E_b I(c_b).
}
\tag{2.5}
\]

### Proof

The folded activation is character invariant, so
\[
\mathcal A_{z_b}(f_b)=\mathcal A_{z_b}(c_b).
\]
Monotonicity in the scale gives
\[
\mathcal A_{z_b}(c_b)\le\mathcal A_z(c_b).
\]
The minimizing definition permits the empty gauge, and `Phi_z(k)<=k`, hence
\[
\mathcal A_z(c_b)
\le P_z^{\varnothing}(c_b)
\le\sum_S|S|\widehat c_b(S)^2
=I(c_b).
\]
This proves (2.2); average and subtract from the parent to obtain (2.4), then apply Theorem 1.1 for (2.5). QED.

The point is that **the character label may depend arbitrarily on the physical branch**. There is no label-leak term in this inequality. The branch label is swallowed by character invariance before the ordinary child influence is measured.

## 3. Consuming the fleet04/B13 proxy-gauge theorem

Apply Theorem 2.1 to the exact one-shot block and explicit branch characters supplied by fleet04/B13. Their theorem gives (0.1), therefore
\[
\boxed{
T_B\ge a_dJ(f)-\mathcal D(f).
}
\tag{3.1}
\]
This is the main new cross-account implication of the run.

### Corollary 3.1 — low-defect activation short circuit

If
\[
\mathcal D(f)\le\theta J(f)
\qquad\text{for some }\theta<a_d,
\tag{3.2}
\]
then the actual proxy-gauge physical block consumes at least
\[
\boxed{
T_B\ge(a_d-\theta)J(f).
}
\tag{3.3}
\]
Using `a_d>=e^{-1}`, the convenient universal threshold
\[
\mathcal D(f)\le\frac{J(f)}{2e}
\tag{3.4}
\]
implies
\[
\boxed{
T_B\ge\frac{J(f)}{2e}.
}
\tag{3.5}
\]

Thus the all-row stability theorem does more than make the residual child influence small. In the low-global-defect branch, its **same real physical reveal consumes a definite fraction of the globally bounded folded activation bank**.

## 4. New global nonreuse theorem for all low-defect activations

Consider any finite adaptive physical restriction tree. At node `v` use the dimension-cooling scale corresponding to its number of unqueried physical coordinates, and let `w_v` be the reach probability. Fleet01/B18's adaptive theorem gives nonnegative true activation drops and the exact one-use budget
\[
\sum_{v\text{ internal}}w_vT_v
\le\mathcal A_{z_{\rm root}}(f)
\le J(f).
\tag{4.1}
\]
Let `L` be **any** collection of nodes at which the fleet04/B13 proxy-gauge block is used and
\[
\mathcal D(f_v)\le\theta J(f_v),
\qquad\theta<e^{-1}.
\tag{4.2}
\]
Then (3.3) and `a_{d_v}>=e^{-1}` give
\[
T_v\ge(e^{-1}-\theta)J(f_v).
\]
Summing only over `L` and using nonnegativity at all other nodes proves:

### Theorem 4.1 — low-defect occupancy/nonreuse bound

\[
\boxed{
\sum_{v\in L}w_vJ(f_v)
\le
\frac{J(f)}{e^{-1}-\theta}.
}
\tag{4.3}
\]
At the threshold `theta=1/(2e)`,
\[
\boxed{
\sum_{v\in L}w_vJ(f_v)
\le2e\,J(f).
}
\tag{4.4}
\]

This is an actual global nonreuse statement. A recursive strategy may encounter arbitrarily many low-defect nodes on different branches, but their total **reach-weighted folded influence** is bounded by `2e` times the root folded influence when each is treated by the proxy-gauge block at threshold (3.4). The same activation currency cannot be spent twice.

No every-coordinate payment is asserted. The theorem is existential/adaptive and is compatible with the known counterexamples to fixed prescribed-coordinate payment.

## 5. A sharper two-branch interface for the remaining proof

The new result gives a clean dichotomy at every centered state:

1. **Low global row defect:**
   \[
   \mathcal D\le J/(2e).
   \]
   The fleet04/B13 one-shot proxy block has branch-gauged residual ordinary influence at most `mathcal D` and, by (3.5), consumes at least `J/(2e)` from a globally one-use activation bank. Repeated appearances of this branch obey the global bound (4.4).

2. **High global row defect:**
   \[
   \mathcal D>J/(2e).
   \]
   The derivative rows contain a definite amount of the exact physical erasure-information budget of fleet02/B12. This is now the only branch in which a large row-defect bank must be converted into a paid Shannon/restriction step.

The fleet02/B14 stationary-trigger theorem is complementary: whenever a closed `C12` trigger subsystem exists it already produces a genuine physical block with `Delta H<=12 I_block`; if that mechanism stalls, (3.1)--(4.4) remain available without asking for a closed trigger cycle.

What this **does not** prove is the missing source-exact upper bound for the raw spectral erasure/Shannon cost `B_B` of the fleet04/B13 one-shot reveal. The activation drop is globally paid, and the post-reveal branch-dependent character label no longer leaks from that bank, but an unbounded `B_B` cannot simply be renamed an activation cost. Likewise the high-defect branch still needs a realizable conversion from `mathcal D` into a dimension-free restriction payment/crossing refund. Those are the remaining universal arrows; full FEI is not closed.

A useful next target is therefore substantially narrower than before:
\[
\boxed{
B_B\le C_1\bigl[J(f)-\mathbb E J(f_B)\bigr]
+C_2\mathcal D(f)
-\text{already-counted crossing/information credits},
}
\tag{5.1}
\]
for the **actual proxy-gauge/source-frontier block**, with constants independent of dimension and no second-factorial-moment substitution. Together with (3.1) and the existing corrected-entropy potential this would provide a genuine recursive FEI step.

## 6. Decisive finite falsification check

`verify_proxy_gauge_activation.py` is a sanity check only; the proofs above are analytic. It exhausts Boolean functions modulo global output sign through `n<=3`, every nonempty proper physical block, and **every branch-dependent character map** on the surviving variables. It tests both
\[
\mathcal A_{z_d}\ge a_dJ
\]
and
\[
T_B\ge a_dJ-\mathbb E I(\chi_{T(b)}f_b).
\]
Recorded output:

```text
cases 12352
min_coercivity_slack 0
min_proxy_gauge_drop_slack 0
```

No negative violation was found. Checker source SHA-256:
`b5bdf759d2db817c1e3c7f82307705df7acce77511f8f4b4eff25e095180f9bc`.
Verification-output SHA-256:
`2728c304cd37dd1e3f0d8cd3b7b4b976ea2dfd36b05590f70fff8592cfa9da45`.

## 7. Joint handoff

**PROVED this run:**

- gauge-free coercivity `a_d J<=A_{z_d}<=J`, uniformly `A_{z_d}>=J/e`;
- arbitrary branch-dependent character absorption `A_child<=I(character-gauged child)`;
- composing with fleet04/B13 gives the exact useful drop `T_B>=a_dJ-mathcal D`;
- low defect `mathcal D<=J/(2e)` forces an actual activation drop at least `J/(2e)`;
- across an arbitrary adaptive tree, all such low-defect proxy-gauge uses satisfy the global nonreuse bound `sum w_v J_v<=2e J_root`.

**Consumed peer artifact:** fleet04/B13 `20260921T2225Z-proxy-gauge-closure/REPORT.md`, blob `1ec1555932e690e403f7d4320640040628697b96`, applied directly to (3.1); fleet01/B18 folded-cooling telescope supplies the global one-use budget.

**Mechanism change:** previous B14 work optimized scalar gauge-lock/crossing inequalities; this run instead quotients arbitrary branch labels and proves a global activation-occupancy theorem. It is not another unchanged universal implication.

**Remaining implication:** pay the raw Shannon/spectral-erasure cost of the source-frontier block, or convert the high-`mathcal D` branch into a paid physical selector, without charging uncontrolled second factorial depth. Full FEI remains OPEN.

**Suggested next recipients:** B18 synthesis workers for insertion into the activation-refunded compiler; B12/B13 physical-erasure workers for the raw reveal-cost inequality (5.1).
