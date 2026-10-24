# account03/B12 — descendant refund retention and sequential robust-row nonreuse

**Run:** `account03-B12-20260922T104514Z`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`  
**Assignment:** account03/B12, Path C, *Descendant refund retention*  
**Classification:** `ESSENTIAL_STEP_APPLIED / PATHWISE_REFUND_IDENTITY / SEQUENTIAL_ROBUST_NONREUSE / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Exact target and source state

The target assigned to this worker is:

> prove a pathwise identity that retains curvature refunds when a chosen physical block creates new medium or small rows; track posterior crossings, phase potential and folded influence across successive real restrictions; prevent a parent's credit from being reused after recentering.

This report proves such an identity for an arbitrary adaptive physical restriction tree and then applies it to a new sequential robust-row compiler. The compiler closes the overlap defect left explicitly open by the newest compatible `account04/B12` result: a robust row can be charged to the *actual folded-influence decrement of the physical block that removes that row and its trigger coordinates*. Therefore trigger coordinates shared by many robust rows cannot be charged repeatedly across generations.

The main completed peer artifact consumed is:

* repository `yspennstate/math-open-problems`;
* commit `a1b2a93210fe7cc871cd10c5bbbf43b1b983a254`;
* path `proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260922T094436Z-robust-row-codimension-staircase/REPORT.md`;
* blob `06a4c1d51bb5d53d0783e567e6176511a68b1167`.

Its exact theorem used here is the pairwise trigger-transfer inequality. If a centered derivative row `i` is relative-`eta` close to a coordinate subcube with trigger set `F_i`, codimension `r_i=|F_i|`, then every trigger satisfies

\[
\boxed{q_k\ge (1-2\eta)q_i\qquad(k\in F_i).}
\tag{0.1}
\]

The exact restriction identities used below come from:

* `account01/B18/20260921T1856Z-curvature-refunded-crossing/REPORT.md`, source blob `ef9f471c019a7d81e9864fd457a0e4bae9da890d`;
* `account02/B13/20260922T075416Z-all-block-terminal-core/REPORT.md`, source blob `68e838a493671ed5c27a29468dfcce7bb621d860`;
* `account02/B12/20260922T091546Z-uniform-selector-debit-and-safe-lift/REPORT.md`, source blob `058e0b1d47e14a65d9055fdc29163752a2692fcf`.

No fixed `Gamma^dagger`, no raw `U_4=O(J)` statement, and no unweighted-L2 payment is assumed. Those routes are refuted at their recorded scopes in the current state.

## 1. One-step exact decomposition, including the slack discarded by the usual inequality

Let `g` be a centered Boolean function on a set `R` of currently surviving physical coordinates. Write

\[
q_j=\operatorname{Inf}_j(g)\le\frac12,
\qquad
\mathcal J(g)=\sum_{j\in R}q_j,
\]
\[
\mathfrak j(q)=1-h_2\!\left(\frac12+\sqrt{q(1-q)}\right),
\qquad
\mathcal P(g)=\sum_{j\in R}\mathfrak j(q_j),
\qquad
\mathcal F(g)=H(g)-\mathcal P(g).
\]

Query a nonempty physical block `A subset R`. For `j notin A`, let

\[
p_j(z)=\operatorname{Inf}_j(g_{A=z})
\]

be the raw child influence before child recentering. Then `E_z p_j(z)=q_j`. Put

\[
q_j(z)=\min\{p_j(z),1-p_j(z)\},
\]

and define the exact majority-crossing increment

\[
c_j(A):=\mathbb E_z(2p_j(z)-1)_+.
\tag{1.1}
\]

Because

\[
q_j(z)=p_j(z)-(2p_j(z)-1)_+,
\]
we have the exact survivor drift

\[
\boxed{q_j-\mathbb E_z q_j(z)=c_j(A).}
\tag{1.2}
\]

Hence, with

\[
I_A:=\sum_{i\in A}q_i,
\qquad
C_A:=\sum_{j\notin A}c_j(A),
\]

\[
\boxed{
D_A:=\mathcal J(g)-\mathbb E_z\mathcal J(g_{A=z})=I_A+C_A.
}
\tag{1.3}
\]

This is the exact folded-influence currency.

Now define the deleted phase

\[
L_A:=\sum_{i\in A}\mathfrak j(q_i),
\tag{1.4}
\]

the first-order crossing refund

\[
W_A:=\sum_{j\notin A}\mathfrak j'(q_j)c_j(A),
\tag{1.5}
\]

and the reflected-curvature remainder

\[
\boxed{
R_A:=\sum_{j\notin A}
\left[
\mathfrak j(q_j)-\mathbb E_z\mathfrak j(q_j(z))
-\mathfrak j'(q_j)c_j(A)
\right].
}
\tag{1.6}
\]

The reflected tangent inequality of account01/B18 gives

\[
\boxed{R_A\ge0.}
\tag{1.7}
\]

Because `j` is symmetric, child recentering does not change the child phase. Therefore (1.6) is not merely a lower bound: by definition,

\[
\boxed{
\Delta_A\mathcal P
:=\mathcal P(g)-\mathbb E_z\mathcal P(g_{A=z})
=L_A+W_A+R_A.
}
\tag{1.8}
\]

For entropy, the exact physical restriction identity is

\[
\Delta_AH=B_A+\operatorname{JS}_A,
\qquad
B_A=H(X_A\mid X_{A^c}),
\tag{1.9}
\]

and block recombination satisfies `JS_A<=L_A`. Define the *selector slack*

\[
\boxed{S_A:=L_A-\operatorname{JS}_A\ge0.}
\tag{1.10}
\]

Subtracting (1.8) from (1.9) gives the exact identity

\[
\boxed{
\Delta_A\mathcal F
=B_A-W_A-S_A-R_A.
}
\tag{1.11}
\]

The usual curvature-refunded inequality `Delta_A F<=B_A-W_A` is exactly (1.11) after discarding the two nonnegative credits `S_A` and `R_A`. These credits are real and, crucially for descendant work, they can be retained across an entire adaptive restriction tree.

## 2. Main theorem: pathwise refund retention under arbitrary adaptive recentering

Consider any finite adaptive physical restriction tree `T`. At each internal node `v`:

* the current Boolean descendant is `g_v`, recentered by a character;
* a nonempty physical block `A_v` is selected using the complete history up to `v`;
* children are the actual restrictions and are again recentered by characters.

Let `pi_v` be the reach probability of node `v`, and let `L` denote the random terminal leaf. At node `v`, use the quantities `D_v,L_v,W_v,R_v,S_v,B_v` from Section 1.

### Theorem 2.1 — exact pathwise nonreuse ledger

For every such tree,

\[
\boxed{
\mathcal J(g_\varnothing)-\mathbb E\mathcal J(g_L)
=
\sum_{v\in T^\circ}\pi_vD_v.
}
\tag{2.1}
\]

\[
\boxed{
\mathcal P(g_\varnothing)-\mathbb E\mathcal P(g_L)
=
\sum_{v\in T^\circ}\pi_v(L_v+W_v+R_v).
}
\tag{2.2}
\]

\[
\boxed{
\mathcal F(g_\varnothing)-\mathbb E\mathcal F(g_L)
=
\sum_{v\in T^\circ}\pi_v(B_v-W_v-S_v-R_v).
}
\tag{2.3}
\]

In particular,

\[
\boxed{
\sum_v\pi_vW_v\le \mathcal P(g_\varnothing),
\qquad
\sum_v\pi_vC_v\le \mathcal J(g_\varnothing).
}
\tag{2.4}
\]

and even

\[
\boxed{
\sum_v\pi_v(S_v+W_v+R_v)
=
\mathcal P(g_\varnothing)-\mathbb E\mathcal P(g_L)
-\sum_v\pi_v\operatorname{JS}_v
\le \mathcal P(g_\varnothing).
}
\tag{2.5}
\]

### Proof

Condition on an internal node `v`. Equations (1.3), (1.8), and (1.11) are exact one-step conditional identities. Multiply each by the reach probability `pi_v` and sum over internal nodes. Every child term cancels the corresponding parent term at the next generation; only the root and terminal leaves survive. This proves (2.1)-(2.3).

For (2.4), all deleted phase terms `L_v`, curvature remainders `R_v`, leaf phase, revealed-coordinate influence, and leaf folded influence are nonnegative. Drop them from (2.1)-(2.2). For (2.5), substitute `S_v=L_v-JS_v` into (2.2) and rearrange. `QED`.

### Interpretation

A child may be recentered and may contain completely new medium or small rows. Nothing is reset. A parent crossing refund remains in the already-summed `W_v`; the later child's `W_u` is computed only from its *new* posterior transition. Equations (2.1)-(2.3) therefore forbid the same influence or phase decrement from being spent twice merely because a later child is recentered.

This is stronger bookkeeping than a generation-by-generation application of `Delta F<=B-W`, because the exact nonnegative `S` and `R` banks are preserved instead of silently discarded at each generation.

## 3. Applying the peer theorem: replace the fixed-state overlap problem by a physical decrement

Take a current descendant `g_v` and a relative-`eta` robust derivative row `i`. Thus its derivative support `E_i` satisfies

\[
\mu(E_i\triangle Q_i)\le\eta q_i,
\qquad
Q_i=\{y_{F_i}=a_i\},
\qquad
r_i=|F_i|,
\qquad 0\le\eta<\frac12.
\tag{3.1}
\]

The consumed account04/B12 theorem gives (0.1). Instead of comparing the row to the *whole current* `J`, physically query the elimination block

\[
\boxed{A_i:=\{i\}\cup F_i.}
\tag{3.2}
\]

By the exact folded-influence decrement (1.3),

\[
D_{A_i}=I_{A_i}+C_{A_i}\ge I_{A_i}.
\]

Using (0.1),

\[
\begin{aligned}
D_{A_i}
&\ge q_i+\sum_{k\in F_i}q_k\\
&\ge \left[1+(1-2\eta)r_i\right]q_i.
\end{aligned}
\]

Hence:

### Theorem 3.1 — local robust address cost is paid by the *actual physical loss*

\[
\boxed{
\left[1+(1-2\eta)r_i\right]q_i
\le D_{\{i\}\cup F_i}.
}
\tag{3.3}
\]

This strictly sharpens the peer's fixed-state estimate

\[
[1+(1-2\eta)r_i]q_i\le J,
\]

because the right side is now the exact quantity that disappears when the block is really queried. The difference is what makes nonreuse possible.

## 4. Sequential compiler: trigger overlap is no longer an aggregate obstruction

Run the following adaptive procedure.

1. At a current descendant, if a relative-`eta` robust row exists, select any one of them.
2. Query its physical elimination block `A_i={i} union F_i`.
3. Recenter every child by a character.
4. Repeat on each child, including rows that did not exist or were not robust at earlier generations.
5. Stop when no selected robust row remains, or the descendant is constant.

Let `i_v,r_v,q_v` denote the selected row, codimension and folded influence at node `v`.

### Theorem 4.1 — sequential robust-row address nonreuse

\[
\boxed{
\sum_{v\in T^\circ}
\pi_v\,[1+(1-2\eta)r_v]q_v
\le
\mathcal J(g_\varnothing)-\mathbb E\mathcal J(g_L)
\le
\mathcal J(g_\varnothing).
}
\tag{4.1}
\]

Consequently,

\[
\boxed{
\sum_v\pi_v r_vq_v
\le
\frac{\mathcal J(g_\varnothing)}{1-2\eta}.
}
\tag{4.2}
\]

At the live threshold `eta=1/16`,

\[
\boxed{
\sum_v\pi_v r_vq_v\le\frac87\mathcal J(g_\varnothing).
}
\tag{4.3}
\]

### Proof

Apply (3.3) at each internal node, multiply by the reach probability, and sum. Equation (2.1) telescopes the right side exactly. `QED`.

The theorem does **not** require the trigger sets of different rows to be disjoint at a fixed state. If the same physical trigger would serve many rows, the first selected block that queries it removes it from all later descendants. Overlap is resolved by the physical tree rather than by a false simultaneous incidence sum.

This is precisely the descendant-refund mechanism requested by the assignment: if the first restriction creates a new medium or small robust row in a child, its address is charged to the *remaining* descendant `J`, while all ancestor `D,W,S,R` entries are already frozen in the pathwise ledger.

## 5. A quantitative entropy consequence for all selected robust descendants

The robust-row geometry itself converts codimension into the logarithmic entropy scale. From (3.1), with `s_i=2^{-r_i}`,

\[
s_i\le(1+\eta)q_i,
\]
so

\[
\log_2\frac1{q_i}\le r_i+\log_2(1+\eta).
\tag{5.1}
\]

Also

\[
(1-q)\log_2\frac1{1-q}\le\frac q{\ln2}.
\tag{5.2}
\]

Therefore

\[
\boxed{
h_2(q_i)
\le q_i\left[r_i+b_\eta\right],
\qquad
b_\eta:=\log_2(1+\eta)+\frac1{\ln2}.
}
\tag{5.3}
\]

For `eta<1`, a centered robust row cannot have `r_i=0`: otherwise `Q_i` is the whole cube and `1-q_i<=eta q_i`, forcing `q_i>=1/(1+eta)>1/2`. Thus `r_i>=1`.

Put `a=1-2eta`. Since

\[
\frac{r+b_\eta}{1+ar}
\]

is fractional-linear in `r`, its maximum for real `r>=1` is attained either at `r=1` or in the limit `r to infinity`. Define

\[
\boxed{
C_\eta:=
\max\left\{
\frac{1+b_\eta}{1+a},\frac1a
\right\}.
}
\tag{5.4}
\]

Combining (5.3) with (4.1) gives:

### Corollary 5.1 — all-generation robust-row entropy payment

\[
\boxed{
\sum_v\pi_v h_2(q_v)
\le C_\eta\,\mathcal J(g_\varnothing).
}
\tag{5.5}
\]

At `eta=1/16`,

\[
C_{1/16}
=
\frac8{15}
\left(
1+\log_2\frac{17}{16}+\frac1{\ln2}
\right)
=1.3494175371409616\ldots<1.35.
\tag{5.6}
\]

Thus the binary address entropy of **every robust row selected anywhere in the descendant tree**, including newly created small rows with large codimension, is bounded by `1.35 J(root)`. No ambient dimension, row count, raw depth, or trigger-overlap multiplicity appears.

Moreover `r_v>=1` in (4.1) yields

\[
\boxed{
\sum_v\pi_v q_v
\le
\frac{1}{2(1-\eta)}\,\mathcal J(g_\varnothing).
}
\tag{5.7}
\]

At `eta=1/16`, the coefficient is exactly `8/15`.

## 6. Application to the source's unresolved selector entropy debit

The consumed selector-debit theorem states that for a physical selector of bias `s`, with disagreement probability `d`,

\[
Q_s(d):=\Delta_i\widetilde H-dh_2(V_s)
\le h_2(d)+\frac2{\ln2}\min\{d,1-d\}.
\tag{6.1}
\]

On the uniform cube, after character centering the selected physical coordinate has `d=q_v<=1/2`, so

\[
Q_{1/2}(q_v)
\le h_2(q_v)+\frac2{\ln2}q_v.
\tag{6.2}
\]

Within each macro-step `A_v={i_v} union F_v`, query `i_v` first and then the triggers. This is the same final physical restriction, so the folded-influence decrement still telescopes exactly. Equations (5.5) and (5.7) give

\[
\boxed{
\sum_v\pi_vQ_{1/2}(q_v)
\le
\left[
C_\eta+
\frac{1}{(1-\eta)\ln2}
\right]
\mathcal J(g_\varnothing).
}
\tag{6.3}
\]

At `eta=1/16`,

\[
\boxed{
\sum_v\pi_vQ_{1/2}(q_v)
\le
2.8882922474225223\ldots\,\mathcal J(g_\varnothing).
}
\tag{6.4}
\]

This pays the previously logarithmic `h_2(d)` selector term on the entire sequential **robust-row branch** with one dimension-free bank. It does not pay nonrobust rows; therefore this is not full FEI closure.

## 7. Refutation stress test: why simultaneous fixed-state summation is false

A stronger-looking statement would try to sum the peer's single-row bound over all robust rows at one fixed state:

\[
\sum_i[1+(1-2\eta)r_i]q_i\stackrel{?}{\le}J.
\tag{7.1}
\]

This is false even for exact-subcube rows (`eta=0`). Take the `n`-input AND function in the usual centered gauge. For every coordinate,

\[
q_i=2^{-(n-1)},
\qquad
r_i=n-1,
\]

and each derivative support is exactly the subcube where all other `n-1` inputs are `1`. Therefore

\[
J=n2^{-(n-1)},
\]
while the left side of (7.1) is

\[
\sum_i(1+r_i)q_i
=n^2 2^{-(n-1)}
=nJ.
\]

Thus simultaneous incidence summation loses an unbounded factor `n`. The sequential physical theorem (4.1) passes this test perfectly: selecting one row queries `A_i={i} union F_i=[n]`, so the actual decrement is `D_{A_i}=J` and the compiler terminates immediately. No trigger is reused.

This exact Boolean obstruction explains why the peer report correctly left fixed-state overlap open and why the physical descendant tree, rather than another incidence inequality, is the appropriate repair.

## 8. Relation to the K=4 terminal critical-core route

At a true `F/J` critical core of ratio `rho>4`, the existing all-block theorem gives

\[
U_A\ge \rho D_A
\quad\text{for every nonempty physical block }A.
\]

The present work does **not** contradict or close that terminal inequality. Instead it strengthens the usable structure on the robust branch:

* one robust row's address cost is paid by the exact `D_{\{i\} union F_i}`, not merely by the whole-state `J`;
* the payment telescopes over descendants, so new robust medium/small rows cannot force repeated trigger charges;
* all phase crossing refunds and the discarded selector/curvature slacks are retained exactly by (2.2)-(2.5);
* the entire selected robust-row Shannon debit is `O(J)` by (5.5) and (6.3), without `U_4=O(J)` or a raw depth bound.

The remaining Path-C obligation is therefore sharper: control **nonrobust** positive-defect rows, or prove that every terminal critical core can be driven into the robust sequential compiler with enough total entropy decrement. Hidden orientation curvature may still be needed for that conversion, but it is no longer needed merely to pay address overlap among rows already in the robust regime.

## 9. Status and next attack

### PROVED IN THIS SOURCE

1. **PATHWISE-REFUND-RETENTION-v1:** equations (2.1)-(2.5), exact for every adaptive physical restriction tree.
2. **ROBUST-PHYSICAL-DECREMENT-v1:** equation (3.3), applying the account04/B12 trigger-transfer theorem to the actual elimination block.
3. **SEQUENTIAL-ROBUST-NONREUSE-v1:** equations (4.1)-(4.3), resolving trigger overlap by physical elimination.
4. **ROBUST-DESCENDANT-ENTROPY-v1:** equations (5.5)-(5.7), with explicit constant `<1.35` at `eta=1/16`.
5. **ROBUST-SELECTOR-DEBIT-v1:** equation (6.3), conditional only on the cited source selector-debit theorem and the cited peer trigger-transfer theorem.

### REFUTED

`SIMULTANEOUS-ROBUST-ADDRESS-SUM-v0`, equation (7.1), is false by the exact AND_n family.

### OPEN

Full FEI remains **OPEN / NOT PROVED**. Nonrobust rows and the implication from terminal criticality to a globally sufficient robust/nonrobust decomposition remain unpaid.

### Next attack

Use the exact pathwise bank (2.3) to define a first-entry stopping time into the nonrobust set and prove one of two alternatives:

* before first nonrobust entry, the robust compiler already spends a definite fraction of `J` while paying every selector debit; or
* at first nonrobust entry, the exact retained `R_v+S_v` credit or a signed co-pair/orientation statistic is quantitatively large enough to pay that row without reverting to raw `U_4=O(J)`.

The primary recipient should be `account01/B19`, as required by the assignment card. The result is also directly relevant to `account04/B12`, because it closes the trigger-overlap issue explicitly left open in that peer report.
