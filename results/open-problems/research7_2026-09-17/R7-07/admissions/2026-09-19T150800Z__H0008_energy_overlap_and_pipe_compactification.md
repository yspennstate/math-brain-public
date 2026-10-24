Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort receipt or binding scheduler selector is exposed.**

# H0008 admission-feasibility mathematics: electrical energy, harmonic-ray overlap, and the `u=1/B` pipe compactification

Date: 2026-09-19 UTC  
Worker: R7-07  
Native ID: `6aabe8413f60819197825dd81ca138ae`  
Status: **PENDING_ADMISSION / H0008 feasibility work only**. This document does not create or overwrite the canonical H0008 claim history.

## 1. Continuity and purpose

The preceding R7-07 report reduced the finite exit-generation regeneration-roof problem to conductance truncation and then to a killed harmonic-descendant operator

\[
 (\mathcal K f)(T)
 =(1-B(T))(K_H f)(T),
\]

where `B(T)` is the escape probability across the artificial parent edge and

\[
 (K_Hf)(T)=\sum_{u}\frac{B(T_u)}{S(T)}f(T_u),
 \qquad
 S(T)=\sum_u B(T_u),
 \qquad
 B(T)=\frac{S(T)}{1+S(T)}.
\]

That report also proved the small-positive-conductance estimate

\[
 P_i(0<B\le x)\le C e^{-c/x}
 \tag{1.1}
\]

uniformly over the finite source type set for sufficiently small `x`, and hence all negative moments of `B` on survival.

The remaining homogeneous obstruction was the long-time behavior of `\mathcal K`. This note carries out Section-B methods **B12 (find what is conserved)**, **B29 (add the points at infinity)**, and **B6 (deform to a solvable point)**.

The main gain is an exact deterministic identity: the quantity `B \mathcal K^n 1` is the tail electrical energy of the harmonic unit flow, and its sum over `n` is exactly a weighted second moment of the common-prefix length of two independent harmonic rays. This changes the remaining operator question into a concrete two-ray collision problem.

## 2. Setup on one fixed transient rooted tree

Let `T` be a locally finite rooted tree with root `o` and an artificial parent `partial` joined to `o` by a unit-resistance edge. For every vertex `v`, let `T_v` denote the forward subtree rooted at `v`, and define

\[
 B_v:=P_v^{T_v\cup\{\operatorname{par}(v)\}}
       (\tau_{\operatorname{par}(v)}=\infty).
\]

On the surviving/transient channel `B_v>0`. If the children of `v` are `u`, write

\[
 S_v:=\sum_{u\succ v} B_u.
\]

The elementary series/parallel recursion is

\[
 B_v=\frac{S_v}{1+S_v},
 \qquad
 S_v=\frac{B_v}{1-B_v}.
 \tag{2.1}
\]

The harmonic exit ray chooses child `u` at `v` with probability

\[
 p_v(u):=\frac{B_u}{S_v}.
 \tag{2.2}
\]

Let `theta(v)` be the harmonic mass of the cylinder through `v`, normalized by `theta(o)=1`:

\[
 \theta(v)=\prod_{r=0}^{n-1}p_{v_r}(v_{r+1})
 \quad\text{for }o=v_0\prec v_1\prec\cdots\prec v_n=v.
 \tag{2.3}
\]

Finally define

\[
 (\mathcal Kf)(v)
 =(1-B_v)\sum_{u\succ v}p_v(u)f(u).
 \tag{2.4}
\]

All identities below are quenched/deterministic identities on this one tree.

## 3. B12 — exact Doob/linearization identity

Define the positive linearized conductance operator

\[
 (\mathscr L g)(v)
 :=(1-B_v)^2\sum_{u\succ v}g(u).
 \tag{3.1}
\]

This is exactly the derivative of the recursion `S/(1+S)` in all child coordinates at the fixed conductance profile.

### Proposition 3.1 (Doob relation)

For every nonnegative `f`,

\[
 \boxed{
 B_v(\mathcal K f)(v)=\mathscr L(Bf)(v).
 }
 \tag{3.2}
\]

Consequently, for every integer `n>=0`,

\[
 \boxed{
 B_o\,\mathcal K^n1(o)=\mathscr L^nB(o).
 }
 \tag{3.3}
\]

#### Proof

Using (2.1)-(2.4),

\[
\begin{aligned}
 B_v(\mathcal Kf)(v)
 &=B_v(1-B_v)\sum_u\frac{B_u}{S_v}f(u)\\
 &=(1-B_v)^2\sum_u B_u f(u),
\end{aligned}
\]

because `B_v/S_v=1-B_v`. The right-hand side is `\mathscr L(Bf)(v)`. Iteration gives (3.3). `square`

This identifies the killed harmonic operator as the `B`-Doob transform of the exact conductance linearization.

## 4. B12 — conserved electrical energy and a two-ray collision identity

Set

\[
 A_n(T):=B_o\mathcal K^n1(o).
 \tag{4.1}
\]

The harmonic cylinder weights telescope against the conductances. From

\[
 p_v(u)=\frac{B_u(1-B_v)}{B_v},
\]

we get, for `|v|=n`,

\[
 \boxed{
 \theta(v)
 =\frac{B_v}{B_o}
   \prod_{r=0}^{n-1}(1-B_{v_r}).
 }
 \tag{4.2}
\]

Expanding `\mathcal K^n` and using (4.2) yields two equivalent exact forms:

\[
 \boxed{
 A_n
 =\sum_{|v|=n}
 B_v\prod_{r=0}^{n-1}(1-B_{v_r})^2
 =B_o^2\sum_{|v|=n}\frac{\theta(v)^2}{B_v}.
 }
 \tag{4.3}
\]

Define the level-`n` harmonic collision mass

\[
 C_n(T):=\sum_{|v|=n}\theta(v)^2.
 \tag{4.4}
\]

### Theorem 4.1 (energy-layer conservation law)

For every `n>=0`,

\[
 \boxed{
 A_n-A_{n+1}=B_o^2 C_n.
 }
 \tag{4.5}
\]

Moreover

\[
 \boxed{
 \sum_{n\ge0}C_n=\frac1{B_o},
 }
 \tag{4.6}
\]

and hence

\[
 \boxed{
 A_n=B_o^2\sum_{m\ge n}C_m.
 }
 \tag{4.7}
\]

#### Proof of (4.5)

Fix a level-`n` vertex `v`. Let

\[
 P_v:=\prod_{r=0}^{n-1}(1-B_{v_r})^2.
\]

Its contribution to `A_n` is `P_vB_v`. The total contribution of its children to `A_{n+1}` is

\[
 P_v(1-B_v)^2\sum_{u\succ v}B_u
 =P_v(1-B_v)^2S_v
 =P_vB_v(1-B_v),
\]

using `S_v=B_v/(1-B_v)`. The difference is therefore `P_vB_v^2`. By (4.2),

\[
 P_vB_v^2=B_o^2\theta(v)^2.
\]

Summing over `|v|=n` proves (4.5). `square`

#### Proof of (4.6)

The numbers `theta(v)` are the unit electrical current through the unit-resistance edge entering `v` when one unit of current is sent from the artificial parent to infinity. On a tree, the harmonic flow is the unit current flow. Its energy is therefore

\[
 \sum_{v\in T}\theta(v)^2
 =\sum_{n\ge0}C_n.
\]

The effective conductance of the complete branch from the artificial parent through `o` to infinity is `B_o`; hence its effective resistance is `1/B_o`. Thomson's principle/Ohm's law therefore gives total unit-current energy `1/B_o`, proving (4.6). `square`

Equation (4.7) follows by summing (4.5) and using (4.6), equivalently `A_n\downarrow0`.

### Corollary 4.2 (the proposed killed-semigroup gate is exactly a two-ray second moment)

Let `xi,eta` be two conditionally independent harmonic rays in `T`, and let

\[
 L:=\sup\{m\ge0:\xi_m=\eta_m\}
\]

be their common-prefix generation (the root is generation zero). Then

\[
 P(L\ge m\mid T)=C_m(T).
 \tag{4.8}
\]

Therefore

\[
 \boxed{
 \sum_{n\ge0}B_o\mathcal K^n1(o)
 =\frac{B_o^2}{2}
 E\big[(L+1)(L+2)\mid T\big].
 }
 \tag{4.9}
\]

Indeed, Tonelli and (4.7) give

\[
\begin{aligned}
 \sum_{n\ge0}A_n
 &=B_o^2\sum_{n\ge0}\sum_{m\ge n}C_m\\
 &=B_o^2\sum_{m\ge0}(m+1)C_m\\
 &=\frac{B_o^2}{2}E[(L+1)(L+2)\mid T].
\end{aligned}
\]

Thus the particular summability gate isolated in the preceding R7-07 report is not an abstract spectral condition: it is exactly a **`B_o^2`-weighted second moment of the overlap length of two independent harmonic rays**.

This is the main new reduction of the run.

## 5. What this does and does not solve

Equation (4.9) does **not** by itself prove that the moment is finite under the full H0008 source law. It replaces the opaque long-time Feynman-Kac problem by a concrete collision problem:

> show that two independent harmonic rays split quickly enough, in an annealed `B_o^2`-weighted second-moment sense.

The exact obstruction is now visible. Sole-positive-child pipes have no pair-splitting at all, while genuine branch points split the pair with probability

\[
 1-\sum_up_v(u)^2.
 \tag{5.1}
\]

This quantity can be arbitrarily small at a highly unbalanced branch point, so merely counting branch points is insufficient. The next proof must combine control of exact/near pipes with control of conductance imbalance at genuine branches.

## 6. B29 — compactification at `u=1/B`: exact pipe dynamics

Put

\[
 U_v:=\frac1{B_v}\in[1,\infty).
 \tag{6.1}
\]

The boundary `B=0` becomes the point `U=\infty`.

Suppose `v` has exactly one child `u` with positive escape conductance; all other forward children have `B=0`. Then `S_v=B_u`, and (2.1) gives

\[
 \boxed{U_v=U_u+1.}
 \tag{6.2}
\]

The harmonic child is then deterministically `u`, and the killed factor is

\[
 1-B_v=\frac{U_v-1}{U_v}=\frac{U_u}{U_v}.
 \tag{6.3}
\]

### Proposition 6.1 (exact telescoping on sole-positive-child pipes)

Along `ell` consecutive sole-positive-child vertices

\[
 v_0\prec v_1\prec\cdots\prec v_\ell,
\]

we have

\[
 \boxed{U_{v_r}=U_{v_0}-r}
 \tag{6.4}
\]

and the killed-semigroup weight of traversing the whole pipe is exactly

\[
 \boxed{
 \prod_{r=0}^{\ell-1}(1-B_{v_r})
 =\frac{U_{v_\ell}}{U_{v_0}}.
 }
 \tag{6.5}
\]

In particular `U_{v_0}\ge \ell+1`, hence

\[
 \boxed{B_{v_0}\le\frac1{\ell+1}.}
 \tag{6.6}
\]

#### Proof

Equation (6.2) iterates to (6.4). Equation (6.3) then telescopes:

\[
 \prod_{r=0}^{\ell-1}\frac{U_{v_{r+1}}}{U_{v_r}}
 =\frac{U_{v_\ell}}{U_{v_0}}.
\]

Since `B_{v_\ell}\le1`, `U_{v_\ell}\ge1`, giving (6.6). `square`

### Corollary 6.2 (all exact sole-positive-child pipe lengths have exponential source tails)

Let `L_pipe` be the initial length of the sole-positive-child pipe on a surviving source tree. The previously proved estimate (1.1) and (6.6) give

\[
 \boxed{
 P_i(L_{\rm pipe}\ge\ell,\ B>0)
 \le C e^{-c(\ell+1)}.
 }
 \tag{6.7}
\]

Hence `L_pipe` has finite moments of every order and finite exponential moments for every exponent strictly below the constant supplied by (1.1).

This gives an independent and very concrete explanation of why the point `U=\infty` is not itself the unresolved obstruction. Long exact pipes force `B` to be of order at most `1/ell`, and the source law suppresses that event exponentially in `ell`.

The genuinely new difficulty is therefore **near-pipe genuine branch points**: at least two positive child conductances are present, but one carries almost all harmonic mass, so the two-ray split probability (5.1) is very small.

## 7. B6 — solvable deterministic finite-type deformation

The preceding obstruction disappears completely if the forward escape conductance is deterministic within each type.

Assume a finite type set `D`, numbers

\[
 b_i\in(0,1],\qquad i\in D,
\]

and a row-stochastic harmonic child-type matrix `H=(H_{ij})` such that every surviving type-`i` environment has `B=b_i` and harmonic child type law `H_{ij}`. On type functions, the killed operator is then the finite matrix

\[
 K=\operatorname{diag}(1-b_i)H.
 \tag{7.1}
\]

Let `b_*:=\min_i b_i>0`. Then

\[
 \|K\|_{\infty\to\infty}\le1-b_*<1,
\]

so

\[
 \boxed{
 K^n1\le(1-b_*)^n1,
 \qquad
 \sum_{n\ge0}b_i(K^n1)_i\le\frac{b_i}{b_*}<\infty.
 }
 \tag{7.2}
\]

Thus the killed-semigroup gate and the two-ray second-moment gate are automatic in this deterministic finite-type deformation. Finite type variation alone is not the difficulty; the difficulty is random conductance approaching the compactification boundary `B=0` together with highly unbalanced genuine branches.

### Exact one-type regular tree

For the regular forward `k`-ary tree (`k>=2`),

\[
 b=\frac{k-1}{k},
 \qquad
 \mathcal K=\frac1k,
\]

and therefore

\[
 \boxed{
 A_n=bk^{-n},
 \qquad
 \sum_{n\ge0}A_n=1.
 }
 \tag{7.3}
\]

The finite-depth escape probabilities satisfy

\[
 B^{(h)}=\frac{k-1}{k-k^{-h}}
 \tag{7.4}
\]

(`B^{(0)}=1`), so

\[
 B^{(h)}-b
 =\frac{(k-1)k^{-h}}{k(k-k^{-h})}
 \le k^{-(h+1)}.
 \tag{7.5}
\]

Hence the failed-excursion depth moment is finite explicitly in this slice.

## 8. Combined conclusion

The three methods produce a sharper hierarchy than the preceding report:

1. **B12:** `B\mathcal K^n1` is exactly tail electrical energy, and the full proposed summability gate is exactly a `B^2`-weighted second moment of two-harmonic-ray common-prefix length.
2. **B29:** exact sole-positive-child pipes linearize under `U=1/B`, with `U` dropping by one per level; the established `exp(-c/B)` source tail therefore gives exponential pipe-length tails. The boundary `B=0` itself is not the unresolved mechanism.
3. **B6:** deterministic finite-type conductances have an immediate finite-state spectral gap; the regular tree is explicit. Thus random, highly unbalanced **genuine branch points** are the only remaining channel in this route.

A useful next state variable is therefore the pair-splitting deficit

\[
 \Delta(T):=1-\sum_up_T(u)^2.
 \tag{8.1}
\]

The next attack should separate exact pipes (`Delta=0`) from near-pipe branches (`0<Delta<<1`) and ordinary branches (`Delta` bounded below), then use the already proved small-conductance tail to show that near-pipe genuine branches cannot dominate the pair-overlap Green function.

No source-level closure is claimed here. H0008 remains **SOURCE OPEN / PARTIAL** in its canonical history and R7-07 remains **PENDING_ADMISSION** under its create-only acquisition rule.
