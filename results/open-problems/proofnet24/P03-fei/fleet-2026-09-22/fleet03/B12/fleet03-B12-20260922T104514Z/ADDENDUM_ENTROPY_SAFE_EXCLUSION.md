# Addendum — coefficient-12 critical-core exclusion and the max-row residual dichotomy

A compatible Path-C result completed after the main B12 report and directly consumed the B12 pathwise-refund theorem. This addendum applies it back to the ratio-critical core and sharpens the remaining obstruction.

## 0. New compatible source consumed

Repository `yspennstate/math-open-problems`, commit

`208a82a980bf13f67181e961815dcee4206dddd6`,

path

`proofnet24/P03-fei/fleet-2026-09-22/fleet02/B11/20260922T104712Z-b11-fei-r18/REPORT.md`,

blob `6c09d3b6643bcd9f5e5f12bb3206ccb611bca20b`.

Its Theorem 4.2 is analytic in arbitrary dimension. For a centered physical pivot `x` with derivative support `E`, a codimension-`r` coordinate subcube

\[
Q=\{y_Z=a\},\qquad q=2^{-r},
\]

if

\[
I_Z:=\sum_{k\in Z}q_k\le rp
\quad\text{and}\quad
\mu(E\triangle Q)\le\frac{q}{8r},
\qquad p=q_x,
\tag{0.1}
\]

then the genuine physical block `A=Z union {x}` satisfies

\[
\boxed{\Delta_AH\le12I_A.}
\tag{0.2}
\]

The same source applies the B12 refund identity and records the stronger

\[
\boxed{
\Delta_A\mathcal F
\le12D_A-
\bigl(12C_A+L_A+W_A+R_A\bigr)
\le12D_A.
}
\tag{0.3}
\]

When `x` is a maximum-influence coordinate, `I_Z<=rp` is automatic.

A second fresh compatible source is repository `yspennstate/math-open-problems`, commit

`32e98f96b54e9c0e8bdee8f7ac49cba9aca0fe46`,

path

`proofnet24/P03-fei/fleet-2026-09-22/fleet03/B11/20260922T105133Z-fleet03-B11-fei/REPORT.md`,

blob `3e67992b1cb850a06a543835e286486596fcd665`.

For every derivative row `i` it proves the exact edge-isoperimetric dichotomy

\[
V_i\ge q_i\log_2\frac1{q_i}
\quad\text{or}\quad
Z_i\ge q_i\log_2\frac1{q_i},
\tag{0.4}
\]

where `V_i` is the sum of genuine physical singleton posterior crossings incident to row `i`, while

\[
Z_i=\sum_{j\ne i}
\bigl[p_{ij}-c_{i\leftarrow j}-c_{j\leftarrow i}\bigr]\ge0
\tag{0.5}
\]

is the symmetric common-source support residual. Unlike the old raw orientation bank, `Z_i` has zero cross-factor contribution on an exact tensor.

## 1. New target-level exclusion at ratio 12

### Theorem B.1 — a ratio-critical core above 12 cannot have an entropy-safe maximum row

Let `g` be a centered minimum-essential-dimension maximizer of

\[
\rho=\mathcal F(g)/\mathcal J(g).
\]

Assume `rho>12`, and let `x` be any maximum-influence coordinate. Then for **every** coordinate subcube `Q={y_Z=a}` of codimension `r>=1`,

\[
\boxed{
\mu(E_x\triangle Q)>\frac{2^{-r}}{8r}.
}
\tag{1.1}
\]

### Proof

Because `x` has maximum folded influence `p=q_x`, every `k in Z` has `q_k<=p`, so `I_Z<=rp`. If (1.1) failed, source Theorem 4.2 would apply to `A=Z union {x}` and give

\[
\Delta_A\mathcal F\le12D_A.
\tag{1.2}
\]

But the ratio-critical extremal property gives for every physical block

\[
\Delta_A\mathcal F\ge\rho D_A.
\tag{1.3}
\]

The pivot is essential, hence `D_A>=q_x>0`. Since `rho>12`, (1.2)-(1.3) contradict one another. `QED`.

This is a genuine reduction of the full terminal-class problem. Any counterexample to `F<=12J` has a ratio-critical descendant whose maximum derivative row lies **outside every entropy-safe coordinate-subcube tube at the exact `2^{-r}/(8r)` frontier**.

Consequently, if this residual class can be eliminated with any finite additional payment that is already present in the exact pathwise ledger, then the original FEI follows with a finite constant after adding the established phase cap `2/ln2`.

## 2. The maximum row must expose either visible physical crossing or tensor-centered support residue

The singleton critical-core inequality gives

\[
h_2(q_x)\ge\rho q_x.
\tag{2.1}
\]

For `0<q<=1/2`,

\[
h_2(q)
=q\log_2\frac1q+(1-q)\log_2\frac1{1-q}
\le
q\log_2\frac1q+\frac q{\ln2}.
\tag{2.2}
\]

Hence

\[
\boxed{
q_x\log_2\frac1{q_x}
\ge
\left(\rho-\frac1{\ln2}\right)q_x.
}
\tag{2.3}
\]

Apply the fresh B11 dichotomy (0.4):

### Theorem B.2 — quantitative max-row residual dichotomy

Every ratio-critical core with `rho>12` has a maximum-influence coordinate `x` satisfying one of

\[
\boxed{
V_x\ge
\left(\rho-\frac1{\ln2}\right)q_x
}
\tag{2.4}
\]

or

\[
\boxed{
Z_x\ge
\left(\rho-\frac1{\ln2}\right)q_x.
}
\tag{2.5}
\]

Together with Theorem B.1, this means the maximum row is simultaneously outside every entropy-safe subcube tube and carries a rare-event logarithm in one of two **source-valid** currencies.

## 3. The visible branch forces the maximum influence to be a tiny fraction of total influence

At a ratio-critical core, the fixed-cardinality crossing budget gives

\[
\sum_{i\ne j}
(\rho+\mathfrak j'(q_i))c_{i\leftarrow j}
\le
\mathcal P-\operatorname{DTC}(X).
\tag{3.1}
\]

Since `j'>=0`, with

\[
T:=\sum_{i\ne j}c_{i\leftarrow j},
\]

\[
T\le\frac{\mathcal P-\operatorname{DTC}(X)}\rho
\le\frac{2}{\rho\ln2}\,\mathcal J.
\tag{3.2}
\]

All terms making up `V_x` are distinct ordered terms of `T`, so `V_x<=T`. If the visible alternative (2.4) holds, then

\[
\boxed{
\frac{q_x}{\mathcal J}
\le
\frac{2}{\rho\ln2\,\left(\rho-1/\ln2\right)}.
}
\tag{3.3}
\]

At `rho=12`, the right side is

\[
0.022778\ldots .
\tag{3.4}
\]

Thus, above the coefficient-12 threshold, either

1. the maximum influence is already below roughly `2.28%` of total folded influence (and the physical crossing bank pays its rare-event logarithm), or
2. the maximum row carries the tensor-centered common-source residual (2.5).

The second branch is the genuinely new obstruction. It is more precise than raw `U_4`: the support residual `Z_x` vanishes on exact cross-factor tensor pairs and therefore does not contain the quadratic tensor-orientation baseline that invalidated `U_4=O(J)`.

## 4. Pathwise compatibility

The conclusion is compatible with the exact `K`-shifted ledger in `ADDENDUM_K_LEDGER.md`. If a later physical block is used to convert either branch, the available terminal surplus, block-dependence slack, selector slack and reflected curvature satisfy

\[
\Delta_A\mathcal G_\rho
=T_A(\rho)-E_A-S_A-R_A,
\]

and therefore cannot be spent again after descendant recentering.

In particular, the coefficient-12 elimination branch has already been fully compiled by the consumed fleet02/B11 theorem using exactly this B12 ledger. The remaining task is not another near-subcube audit: it is to convert the `Z_x` branch, or the many-small-coordinate visible branch allowed by (3.3), into a nonreusing physical entropy decrement.

## 5. Status

**PROVED IN THIS SOURCE:** `RHO12-ENTROPY-SAFE-MAXROW-EXCLUSION-v1`, `RHO12-MAXROW-RESIDUAL-DICHOTOMY-v1`, and the visible-branch bound (3.3), conditional only on the two cited source theorems and the established critical-core/crossing identities.

**FULL FEI:** still **OPEN / NOT PROVED**.

**Next attack:** use the co-pair identity `kappa_ij=4 Pr(i,j in X)` on the `Z_x` branch, but subtract the exact tensor baseline before any aggregate estimate. The target is a physical block whose exact `E_A+S_A+R_A` credit is bounded below by a fixed fraction of `Z_x`, or a genuine Boolean counterfamily showing that this conversion is false.
