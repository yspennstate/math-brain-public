# FOREST / account03 B03 — exact activity residual identity and complete-graph boundary saturation

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Assignment: compute exact forest-pair counts for structured/asymptotic adversaries to the shared candidate and turn failures into a structural constraint.  
Outcome: **AUXILIARY_ONLY / STRUCTURAL_CONSTRAINT_PROVED**. The Grimmett–Winkler uniform-forest pairwise negative-correlation conjecture remains **OPEN**.  
Execution context: **WITHOUT_VERIFIED_BRAIN**.

The current owner control supersedes this slot's historical brain-population role and stops new installation/benchmark work. Existing brain/state artifacts were preserved unchanged. This report contains only source-bound FOREST mathematics.

## 1. Source target and exact peer consumed

For a finite simple graph `G`, let `F` be uniformly distributed over every acyclic edge subset, including the empty and disconnected forests. For distinct edges `e,f`, write

`Z = #forests`, `Z_e = #forests containing e`, `Z_f = #forests containing f`, and `Z_ef = #forests containing both`.

The target is

\[
\Delta_G(e,f):=Z_e Z_f-Z Z_{ef}\ge 0.
\]

The exact assigned other-account partner consumed here is account04/B01:

`proofnet24/P14-probability-correlation/collective-2026-09-22/account04/B01/b01-20260922T001208Z-forest-r11/report.md`, blob `d5faa9e572e9fa67b736693a7f1a9d5205764b3c`.

That report proves the all-parameter multi-bridge 2-separator gluing formulas and rigorously localizes a lexicographically minimal counterexample to the 3-connected obstruction. In particular, this run does not reopen separator bookkeeping.

The second exact input is account03/B01's activity/unrooting representation (scientific commit `f9f56b1817456c462e1b0c9708099eeb00b997d8`). Put the marked pair first in the edge order, `e<f<others`. For a spanning tree `T`, weight it by

\[
w(T)=2^{i(T)},
\]

where `i(T)` is its internal activity. The actual uniform unrooted forest law is the disjoint union of these activity cubes, so `sum_T w(T)=Z`. If

\[
\mathcal A_f(e)=\{T:f\in T,e\notin T,T-f+e\text{ is a tree}\},
\]

then the overlap reservoir `q` from the exact reconnection identity satisfies

\[
q=\sum_{T\in\mathcal A_f(e)}w(T),
\]

and the reverse exchange `T-f+e` has exactly twice the activity weight. This is an exact unrooting identity, not a spanning-tree surrogate.

## 2. New exact four-cell activity identity

Partition the activity-weighted spanning trees by membership of `e,f`:

- `A`: weight of trees containing neither edge;
- `B`: weight of trees containing `e` but not `f`;
- `C`: weight of trees containing `f` but not `e`;
- `D`: weight of trees containing both.

The activity representation gives

\[
A+B+C+D=Z,
\quad B+D=2Z_e,
\quad D=4Z_{ef},
\quad C+D+q=2Z_f.
\tag{2.1}
\]

Inside the `C` cell, the forward exchange class has weight `q`; its image inside the `B` cell has weight `2q`. Define the genuine nonexchange residual masses

\[
B_0:=B-2q\ge0,
\qquad
C_0:=C-q\ge0.
\tag{2.2}
\]

Substituting (2.1) into `4 Delta` and then (2.2) gives the exact identity

\[
\boxed{
4\Delta_G(e,f)
=(B_0+2q)(C_0+2q)-D(A-q).
}
\tag{2.3}
\]

Proof by direct algebra:

\[
\begin{aligned}
4\Delta
&=(B+D)(C+D+q)-(A+B+C+D)D\\
&=BC+Bq+Dq-AD\\
&=(B_0+2q)(C_0+2q)-D(A-q).
\end{aligned}
\]

Thus the source conjecture for this ordered pair is *equivalent* to

\[
D(A-q)\le (B_0+2q)(C_0+2q).
\tag{2.4}
\]

This is a graph-global compatibility coordinate absent from the already-refuted local three-edge cone. It also shows exactly why `q` alone cannot be treated as the whole compensation mechanism: the two nonexchange residual masses enter multiplicatively.

A source violation would necessarily have `A>q` and the strict reverse of (2.4).

## 3. Structured adversary: two disjoint marked edges in `K_n`

Take `G=K_n`, with disjoint marked edges `e={1,2}` and `f={3,4}` and order `e<f<others`. Symmetry gives `Z_e=Z_f`. Equations (2.1)-(2.2) reduce to

\[
D=4Z_{ef},
\qquad
B_0+2q=C_0+2q=2Z_e-4Z_{ef},
\qquad
A-q=Z-4Z_e+4Z_{ef}.
\tag{3.1}
\]

Define the activity residual ratio

\[
R_n:=\frac{D(A-q)}{(B_0+2q)(C_0+2q)}.
\]

Then exactly

\[
\boxed{
R_n=\frac{Z_{ef}(Z-4Z_e+4Z_{ef})}{(Z_e-2Z_{ef})^2},
\qquad
1-R_n=\frac{\Delta_G(e,f)}{(Z_e-2Z_{ef})^2}.
}
\tag{3.2}
\]

Hence the complete-graph source correlation asymptotics directly measure how close the new exact activity inequality is to equality.

## 4. Rigorous asymptotic saturation

Dudley Stark, *The Edge Correlation of Random Forests*, Annals of Combinatorics 15 (2011), 529-539, DOI `10.1007/s00026-011-0104-7`, Theorem 3, gives for a uniformly random forest of `K_n`

\[
P(e)^2=4n^{-2}-4n^{-3}-23n^{-4}+O(n^{-5}),
\]

and for nonadjacent (therefore disjoint) `e,f`,

\[
P(e,f)=4n^{-2}-4n^{-3}-27n^{-4}+O(n^{-5}).
\]

Consequently

\[
\frac{\Delta}{Z^2}=P(e)^2-P(e,f)=4n^{-4}+O(n^{-5}),
\]

while `P(e)=2n^{-1}+O(n^{-2})` and `P(e,f)=4n^{-2}+O(n^{-3})`, so

\[
\left(\frac{Z_e}{Z}-2\frac{Z_{ef}}{Z}\right)^2
=4n^{-2}+O(n^{-3}).
\]

Using the exact identity (3.2),

\[
\boxed{
1-R_n=n^{-2}+O(n^{-3}),
\qquad
R_n=1-n^{-2}+O(n^{-3}).
}
\tag{4.1}
\]

Therefore no universal multiplicative strengthening `R_n <= 1-epsilon` with fixed `epsilon>0` can prove the source conjecture through this coordinate system. The exact boundary is approached already by the source-valid, highly symmetric, 3-connected complete graphs. Any all-graphs argument based on (2.4) must preserve sign information at a scale fine enough to survive this `Theta(n^-2)` relative slack; a coarse constant-factor loss is fatal.

This is distinct from the earlier split-graph no-fixed-margin obstruction: here the almost-tight object is the exact *activity residual inequality equivalent to the source Rayleigh gap*, and the rate follows from source-level forest correlation asymptotics.

## 5. Exact integer regression, `n=4..100`

The accompanying standard-library checker derives the counts from labelled-tree component recurrences, not floating-point sampling. It computes exactly:

- the total forest count `Z`;
- `Z_e` for one specified edge;
- `Z_ef` for two specified disjoint edges, split into same-tree and separate-tree components;
- the exact overlap `q`, by the two cross-pair component patterns `(1~3,2~4)` and `(1~4,2~3)`;
- the activity cells `A,B,C,D` and residuals `B0,C0`.

For every `4<=n<=100` it checks

\[
4\Delta=(B_0+2q)(C_0+2q)-D(A-q),
\]

all residual counts are nonnegative, `Delta>0`, and

\[
1-R_n=\frac{\Delta}{(Z_e-2Z_{ef})^2}.
\]

The executed output ends in:

`IDENTITY_CHECKS_N4_TO_N100=PASS`  
`DELTA_POSITIVE_N4_TO_N100=PASS`  
`ACTIVITY_RESIDUAL_RATIO_APPROACHES_ONE_NUMERICALLY=YES`.

Selected scaled gaps `n^2(1-R_n)` are `2.161860458...` at `n=10`, `1.485350620...` at `n=20`, `1.173106489...` at `n=50`, and `1.083226803...` at `n=100`, matching (4.1).

Executed checker-source SHA-256: `cdc80c93275cb92d6617f630e3e84029e5658dcc4248573b192a7f9a764b69f7`.  
Captured output SHA-256: `f2b28a7db79b111d936bb02282baebabdea9b4c53fe78f3f4c7150d084eaf813`.

## 6. Structural consequence and next exact obligation

The current collective state has already shown that:

1. separator bookkeeping can be eliminated exactly (account04/B01);
2. a minimal obstruction is 3-connected;
3. local three-edge graphic-matroid constraints plus sign coherence do not suffice (account04/B03);
4. a violating pair in a minimal counterexample has tightly constrained global covariance signs and small positive correlation (account01/B01);
5. the source inequality can now be written exactly as the activity residual inequality (2.4).

This run adds that (2.4) is asymptotically tight with relative gap `n^-2+O(n^-3)` on complete graphs. The next mechanism therefore should not seek another universal fixed margin. It should prove the **sign-exact activity residual inequality** by a weight-preserving exchange/conservation argument coupling `A-q` to the two residual one-sided classes, or derive an equally sharp global conservation law from the simultaneous constraints across all third edges.

A promising exact target is a mass transport that starts from `D x (A\mathcal A)` and lands in the product of the two one-sided activity classes with their `q` exchange images, with multiplicities controlled exactly rather than by a constant factor. Any proposed transport must reproduce the complete-graph `1/n^2` boundary slack and the earlier `K_{3,m}` overlap-leading-order regression.

## 7. Status

- Parent Grimmett–Winkler conjecture: **OPEN**.
- New exact identity: (2.3), equivalent to the source pair inequality.
- New structured obstruction: complete graphs force asymptotic equality in (2.4) at relative rate `1-n^-2+O(n^-3)`.
- Outcome: **AUXILIARY_ONLY / STRUCTURAL_CONSTRAINT_PROVED**.
- Novelty/priority of the activity residual identity and saturation observation: **UNVERIFIED**; no priority claim is made.
- Next recipients: FOREST lead `account01/B01`, exact partner `account04/B01`, and switching/activity workers.
