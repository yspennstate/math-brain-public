# fleet04/B18 — surplus-weighted hidden-curvature reduction on K=4 critical cores

**Run:** `20260922T091529Z-b18-fei-r11-auto`  
**Classification:** `ESSENTIAL_STEP_APPLIED / A-B_INTERFACE_INTEGRATION / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Publication priority:** unverified; no novelty claim.

## 0. Scope and source correction

This run continues the candidate-independent A/B route.  The fixed all-gate potential
`Gamma^dagger` used in several MUX collars is source-exactly refuted as a universal candidate by a biased composition-prime 18-input gate, so no fixed-`Gamma^dagger` collar is used as universal FEI currency here.

The newest fleet01/B18 completed report is

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260922T080302Z-mux-newborn-cancellation-121/REPORT.md`, commit `7bbd5fa7324a849f77394a9fa38e5888c57f92d0`, blob `c08efa20ebf01b207ed3bb8ada31e8f258681084`.

It is retained exactly at its family-specific fixed-candidate scope.  The universal fleet01/B18 curvature-refunded result actually consumed below is

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260921T1856Z-curvature-refunded-crossing/REPORT.md`, blob `ef9f471c019a7d81e9864fd457a0e4bae9da890d`.

The newest compatible fleet04 inputs are:

* B12 `20260922T081051Z-terminal-trigger-surplus/REPORT.md`, commit `fdbfbcc1beed0db4cb6d13c8d61fd92db53a8113`, blob `d283c7b495316959312155f8ba68fb83569d9633`;
* B13 `20260922T074113Z-han-crossing-collapse/REPORT.md`, commit `3a241a0defa5a65ce6a6f14939684dfb4622e009`, blob `49065f1706a3cc5c0b9038273ffe9b1163187918`;
* B14 `20260922T071120Z-criticality-matched-stopping/REPORT.md`, blob `79cf35fd1ddb48ccb9948081cc5ae6f3b13ce5b2`.

The still-newer B14 MUX denominator-20 theorem, commit `329e454a013a71a0d90a4cee68a3921134b327e2`, remains a valid family-specific statement but is not promoted into this universal chain.

Finally this report consumes fleet04/B18's own preceding exact visible/hidden decomposition,

`proofnet24/P03-fei/fleet-2026-09-22/fleet04/B18/20260922T081002Z-visible-hidden-curvature-split/REPORT.md`, commit `40d53b2d7f2c8b388a95d4abd82221321f6fcfcf`, blob `b22432baafae5b44e2ca3f73d63fc4dcf95d96b9`.

No prescribed-coordinate entropy payment, fixed-relative near-subcube theorem, raw `sum d_i=O(J)` estimate, or unsigned-curvature shortcut is assumed.

## 1. Critical-core setup

Median-center a Boolean function and write

\[
q_i=\operatorname{Inf}_i(f)\le\frac12,
\qquad
\mathcal J=\sum_i q_i,
\]
\[
\mathfrak j(q)=1-h_2\!\left(\frac12+\sqrt{q(1-q)}\right),
\qquad
\mathcal P=\sum_i\mathfrak j(q_i),
\qquad
\mathcal F=H-\mathcal P.
\]

Assume toward the `K=4` terminal contradiction that a centered physical-restriction descendant is an actual `F/J`-critical core of ratio

\[
\rho=\mathcal F/\mathcal J>4.
\tag{1.1}
\]

For every physical block `A`, fleet01/B18 proves

\[
\sum_{i\in A}h_2(q_i)-W_A
\ge
\rho(I_A+C_A),
\tag{1.2}
\]

where

\[
W_A=\sum_{j\notin A}\mathfrak j'(q_j)c_j(A).
\]

Hence the same state is automatically **all-block terminal at K=4**:

\[
\boxed{
\sum_{i\in A}h_2(q_i)-W_A\ge4(I_A+C_A)
\quad\text{for every nonempty physical block }A.
}
\tag{1.3}
\]

This is exactly the hypothesis under which the fresh fleet04/B12 robust-row theorem applies.  B14 supplies the matching realizable adaptive interpretation: an `F/J`-critical core is terminal for the curvature-aware physical stopping rule, and proving `F<=4J` on that terminal class would yield `H<=(4+2/ln2)J` globally.

## 2. Exact visible/hidden row law

For distinct `i,k`, let

* `c_{k<-i}=c_k({i})` be the physical singleton posterior crossing into row `k`;
* `p_{ki}` be derivative-support disagreement;
* `o_{ki}` be opposite-sign overlap;
* `kappa_{ki}=p_{ki}+4o_{ki}` be mixed curvature.

The preceding B18 theorem gives

\[
2c_{k<-i}\le p_{ki}\le\kappa_{ki}
\]

and defines

\[
\omega_{ki}:=p_{ki}-2c_{k<-i}+4o_{ki}\ge0,
\]

so that

\[
\boxed{\kappa_{ki}=2c_{k<-i}+\omega_{ki}.}
\tag{2.1}
\]

Put

\[
R_k:=\sum_{i\ne k}c_{k<-i},
\qquad
\Omega_k:=\sum_{i\ne k}\omega_{ki}.
\]

Mixed-derivative conservation is therefore the exact row identity

\[
\boxed{4d_k=2R_k+\Omega_k.}
\tag{2.2}
\]

Define the already-used hidden bank

\[
\boxed{
U_4:=\sum_k(4+\mathfrak j'(q_k))\Omega_k.
}
\tag{2.3}
\]

The opposite-sign `4o` mode is inside `Omega_k`; it is not discarded.

## 3. New scalar lemma: terminal surplus is a small curvature weight

Define the K=4 terminal surplus

\[
\sigma_k:=h_2(q_k)-4q_k\ge0.
\tag{3.1}
\]

### Lemma 3.1

Every coordinate of a ratio-`rho>4` critical core satisfies

\[
\boxed{
\sigma_k\le\lambda_4\,[4+\mathfrak j'(q_k)],
\qquad
\lambda_4:=\frac7{44}\log_2\frac{17}{16}
=0.0139145429261903\ldots .
}
\tag{3.2}
\]

### Proof

From the singleton case of (1.2), `h_2(q_k)>=rho q_k>4q_k` for every positive `q_k`.  Since `h_2(q)/q` is decreasing, it is enough to note

\[
h_2(1/6)<2/3,
\]

which is exactly equivalent to

\[
6^6<16\,5^5,
\]

i.e. `46656<50000`.  Hence every positive `q_k<1/6`.

Set

\[
x=\sqrt{\frac q{1-q}}.
\]

Rewriting fleet01/B18's exact derivative formula using
`artanh(2x/(1+x^2))=2 artanh(x)` gives

\[
\mathfrak j'(q)
=\frac{1-x^2}{x\ln2}
\ln\frac{1+x}{1-x}.
\tag{3.3}
\]

Since

\[
\ln\frac{1+x}{1-x}\ge2x
\]

for `0<=x<1`, and `q<1/6` implies `x^2<1/5`,

\[
\mathfrak j'(q)>rac8{5\ln2}.
\tag{3.4}
\]

The elementary exponential-series certificate

\[
1+\frac7{10}+\frac{(7/10)^2}{2}
+\frac{(7/10)^3}{6}
=2.002166\ldots>2
\]

proves `ln2<7/10`.  Therefore

\[
\boxed{\mathfrak j'(q)>16/7,\qquad 4+\mathfrak j'(q)>44/7.}
\tag{3.5}
\]

Finally `sigma(q)=h_2(q)-4q` is concave and is maximized where
`h_2'(q)=4`, namely `q=1/17`.  Thus

\[
\max_{0\le q\le1/2}\sigma(q)
=h_2(1/17)-4/17
=\log_2(17/16).
\tag{3.6}
\]

Equations (3.5)-(3.6) prove (3.2). QED.

## 4. New theorem: the surplus-weighted depth bank reduces to the same hidden bank U4

Fleet01/B18's fixed-cardinality curvature theorem gives on this critical core

\[
\boxed{
\sum_k(\rho+\mathfrak j'(q_k))R_k
\le\mathcal P-\operatorname{DTC}(X).
}
\tag{4.1}
\]

Since `rho>4`, Lemma 3.1 implies

\[
\sum_k\sigma_kR_k
\le
\lambda_4\,[\mathcal P-\operatorname{DTC}(X)].
\tag{4.2}
\]

Likewise, by definition of `U_4`,

\[
\sum_k\sigma_k\Omega_k\le\lambda_4U_4.
\tag{4.3}
\]

Multiply the exact row identity (2.2) by `sigma_k` and sum.  The result is the new exact reduction

\[
\boxed{
\sum_k\sigma_k d_k
\le
\frac{\lambda_4}{2}
[\mathcal P-\operatorname{DTC}(X)]
+\frac{\lambda_4}{4}U_4.
}
\tag{4.4}
\]

This is strictly more targeted than the older raw-depth reduction: B12's terminal theorem asks for exactly the surplus-weighted bank on the left, and (4.4) shows that its crossing-visible part is already paid by the same `P-DTC` bank used by interface A.  Only the explicitly hidden mixed-curvature component survives.

No `sum d_k=O(J)` statement is used or obtained.

## 5. New robust-row consequence

Let `R_{1/16}` be the relative-`1/16` near-subcube derivative rows at the critical state.  Fresh fleet04/B12 proves

\[
\boxed{
\sum_{i\in R_{1/16}}q_i^2[4+\mathfrak j'(q_i)]
\le
\frac{256}{105}\sum_k\sigma_kd_k.
}
\tag{5.1}
\]

Combining (5.1) with (4.4) yields:

### Theorem 5.1 — robust load versus hidden curvature

\[
\boxed{
\sum_{i\in R_{1/16}}q_i^2[4+\mathfrak j'(q_i)]
\le
\frac{128\lambda_4}{105}
[\mathcal P-\operatorname{DTC}(X)]
+
\frac{64\lambda_4}{105}U_4.
}
\tag{5.2}
\]

Numerically,

\[
\frac{128\lambda_4}{105}=0.0169624904243082\ldots,
\qquad
\frac{64\lambda_4}{105}=0.00848124521215412\ldots.
\]

Using `P-DTC<=P<=(2/ln2)J` gives the simpler universal form

\[
\boxed{
\sum_{i\in R_{1/16}}q_i^2[4+\mathfrak j'(q_i)]
<0.048944\,\mathcal J+0.008482\,U_4.
}
\tag{5.3}
\]

For exact-subcube rows, B12's coefficient `2` instead of `256/105` gives the sharper corollary

\[
\boxed{
\sum_{i\in R_0}q_i^2[4+\mathfrak j'(q_i)]
\le
\lambda_4[\mathcal P-\operatorname{DTC}(X)]
+\frac{\lambda_4}{2}U_4.
}
\tag{5.4}
\]

## 6. Medium/heavy robust rows are now quantitatively eliminated unless U4 is large

For `tau>0`, let

\[
M_\tau:=\sum_{\substack{i\in R_{1/16}\\q_i\ge\tau}}q_i.
\]

Because `4+j'(q_i)>=4` and `q_i^2>=tau q_i`, (5.2) gives

\[
\boxed{
M_\tau
\le
\frac{32\lambda_4}{105\tau}
[\mathcal P-\operatorname{DTC}(X)]
+
\frac{16\lambda_4}{105\tau}U_4.
}
\tag{6.1}
\]

and therefore

\[
\boxed{
M_\tau
<
\frac{0.012235851}{\tau}\,\mathcal J
+
\frac{0.002120312}{\tau}\,U_4.
}
\tag{6.2}
\]

At the concrete scale `tau=1/16`,

\[
\boxed{
M_{1/16}
<0.195774\,\mathcal J+0.033925\,U_4.
}
\tag{6.3}
\]

Thus the B12 medium/heavy robust branch no longer requires a separate payment currency: unless the already-isolated hidden bank `U_4` is large, it carries only a controlled fraction of the total folded influence.

This is an influence-mass statement, not an entropy-decrement theorem, and is not substituted for the separate inherited entropy estimate.

## 7. Smallest honest universal chain after this run

1. Run B14's genuine curvature-aware physical selector.  If the terminal class obeys `F<=4J`, then `H<=(4+2/ln2)J` globally.
2. Otherwise choose an actual centered `F/J`-critical physical descendant with `rho>4`; fleet01/B18 makes it all-block terminal at `K=4`.
3. The exact zero-depth branch is already classified by mixed-derivative integrability as a character-twisted one-point defect, with `H<4J`; therefore a genuine obstruction lies in the positive-defect branch.
4. Split every mixed curvature exactly as `kappa=2c+omega`.  Fleet01/B18's `P-DTC` budget pays the entire visible singleton-crossing component.
5. The fresh B12 robust-row obstruction asks for the weighted bank `sum sigma_k d_k`, not raw depth.  The new theorem (4.4) reduces that bank to the already-paid phase term plus `U_4` with coefficient only `lambda_4/4` on the hidden component.
6. Consequently medium/heavy robust rows are quantitatively small unless `U_4` itself is large, by (6.1)-(6.3).

### Unpaid arrows — explicit

**U1 — hidden curvature.** Prove a dimension-free payment or realizable elimination for

\[
U_4=\sum_{i\ne k}(4+\mathfrak j'(q_k))
[p_{ki}-2c_k(\{i\})+4o_{ki}]
\]

on positive-defect `K=4` terminal critical cores.  The opposite-sign mode is part of this bank and cannot be dropped.

**U2 — small/nonrobust positive-defect rows.** Equation (5.2) covers the inherited relative-`1/16` near-subcube class.  Rows outside that stability regime, and robust rows below a chosen influence scale, still require a source-valid nonreusing payment or a reduction to U1.

No other arrow is silently paid.  In particular, the fixed `Gamma^dagger` MUX collars and the refuted decomposable-gate extremality conjecture are not used as universal closure inputs.

## 8. Exact zero-defect endpoint and preserved refutations

The earlier fleet04/B18 equality theorem is unchanged: if every normalized row-depth defect is zero, Boolean integrability forces a character times a signed one-point defect (irrelevant variables allowed), and `H<4J`.  This branch is closed at exactly that scope.

Preserved refutations/corrections:

* prescribed-coordinate Shannon payment is false;
* the fixed-relative near-subcube tolerance is false;
* raw `sum d_k=O(J)` is not assumed;
* unsigned support curvature alone misses opposite-sign overlap;
* blind arity induction is false;
* the old AND/decomposable extremality shortcut is refuted by the later prime-gate witness state;
* fixed `Gamma^dagger` is not a universal all-gate potential;
* no family-specific or conditional theorem is promoted to unconditional FEI closure.

**Status:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`.
