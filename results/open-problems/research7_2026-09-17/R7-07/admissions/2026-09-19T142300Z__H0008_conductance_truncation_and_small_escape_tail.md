Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort receipt or binding model selector is exposed.**

# R7-07 admission-feasibility mathematics — H0008 conductance truncation, a superexponential small-escape tail, and the exact surviving Feynman–Kac gate

Date: 2026-09-19 UTC  
Worker: `R7-07` / native identity `6aabe8413f60819197825dd81ca138ae`  
Repository: `yspennstate/math-open-problems`, branch `master`  
Status: **PENDING_ADMISSION**. This artifact does **not** claim H0008.  
Methods used: **B18 SAY IT IN ANOTHER LANGUAGE / B3 PROVE SOMETHING STRONGER / B20 FIND WHY THE ALGORITHM FAILS**.

## 1. Continuity and source scope

The exact released source under feasibility study is H0008:

Achyut Kumar (2026), *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1 (17 Aug 2026), Section 12.3, open problem (6), **Boundary fluctuations**.

R14's canonical handoff is `operations/claims/H0008.md`. It records H0008 as `UNASSIGNED AFTER R14 HANDOFF / SOURCE OPEN / PARTIAL / RELEASED BY R14 AFTER SECTION-I EXHAUSTION`; because that canonical path already exists, R7-07's create-only claim rule still forbids overwriting it. The present file is therefore bounded admission-feasibility mathematics only.

The preceding R7-07 report

`research7_2026-09-17/R7-07/runs/2026-09-19/2026-09-19T132000Z__report.md`

reduced the finite-mean exit-level regeneration roof to the fresh failed-excursion moment

\[
\ell_i:=\mathbb E_{P_i}\mathbb E^T[D\mathbf 1_F],
\qquad
\ell_*:=\max_i\ell_i,
\tag{1.1}
\]

where a fresh trial enters the root `o` of a forward tree `T`, `F` is the event that the walk eventually returns across the artificial parent edge, and `D` is the maximal downward generation reached before that return. It proved

\[
b_*:=\min_i\mathbb E_{P_i}B(T)>0,\quad \ell_*<\infty
\quad\Longrightarrow\quad
\mathbb EH<\infty.
\tag{1.2}
\]

The purpose of the present run is to understand (1.1) under the actual finite-type branching law rather than under the previous over-strong uniform-escape slice.

## 2. Source branching notation recovered from R14

Let the finite type set be `D={1,...,d}`. For a parent of type `i`, let `nu` be the number of potential child slots, with pgf

\[
G(z)=\mathbb E[z^\nu],
\qquad m_*=G'(1)<\infty.
\]

Each slot independently receives type `j` with probability `q_j>0`, is transmitted with probability `p_{ij}>0`, and if transmitted carries an independent forward tree with law `P_j`. The mean matrix is

\[
M_{ij}=m_*q_jp_{ij},
\]

and the source regime considered here is irreducible and supercritical, `rho(M)>1`.

For a rooted forward tree `T`, add one artificial parent `partial` above the root `o` and define

\[
B(T):=\mathbb P_o^T(\tau_{\partial}=\infty).
\]

If the transmitted child subtrees are `T_u` and `B_u=B(T_u)`, then with

\[
S(T):=\sum_u B_u,
\]

R14 proved the exact electrical recursion

\[
B(T)=\frac{S(T)}{1+S(T)}.
\tag{2.1}
\]

Put

\[
e_i:=P_i(B=0),\qquad s_i:=1-e_i,
\qquad t_i:=\sum_jq_jp_{ij}s_j>0.
\tag{2.2}
\]

The extinction Jacobian is

\[
J_{ij}=G'(1-t_i)q_jp_{ij}.
\tag{2.3}
\]

R14's theorem gives

\[
\rho(J)<1.
\tag{2.4}
\]

This strict inequality is the input used below.

---

# Part I. B18 — failed excursion depth is exactly a conductance-truncation error

## 3. Finite-depth escape conductances

For an integer `h>=0`, let `L_h(T)` be the set of descendants of `o` at forward generation `h`. Define

\[
B^{(h)}(T)
:=\mathbb P_o^T(\tau_{L_h}<\tau_{\partial}),
\tag{3.1}
\]

with `B^(0)=1`. If `T` has no generation-`h` vertex, this probability is zero.

The finite-depth values obey the same series-parallel recursion with boundary value one at generation zero. Namely, if `B_u^(h)` is the corresponding quantity in child subtree `T_u`,

\[
S^{(h)}:=\sum_u B_u^{(h)},
\qquad
B^{(h+1)}=\frac{S^{(h)}}{1+S^{(h)}}.
\tag{3.2}
\]

Rayleigh monotonicity or direct event inclusion gives

\[
1=B^{(0)}\ge B^{(1)}\ge\cdots\downarrow B.
\tag{3.3}
\]

Define the truncation error

\[
\delta_h(T):=B^{(h)}(T)-B(T)\ge0.
\tag{3.4}
\]

## 4. Exact excursion-tail identity

### Theorem R7-07-H0008-B — excursion depth equals finite-depth conductance error

For every locally finite rooted tree `T` and every `h>=1`,

\[
\boxed{
\mathbb P_o^T(D\ge h,\,F)=B^{(h)}(T)-B(T)=\delta_h(T).
}
\tag{4.1}
\]

Consequently, for every source type `i`,

\[
\boxed{
\ell_i
=\sum_{h\ge1}\mathbb E_{P_i}[B^{(h)}-B].
}
\tag{4.2}
\]

Thus the finite-regeneration-roof problem has been changed from a random-walk excursion estimate into a monotone convergence-rate problem for effective escape conductance.

### Proof

The event `tau_{L_h}<tau_partial` decomposes disjointly into

1. the walk reaches generation `h` before the parent and eventually returns to the parent; and
2. the walk never hits the parent.

The second event has probability `B(T)`. Indeed, on a locally finite tree, a trajectory that never hits the artificial parent cannot remain forever in finitely many forward generations: that would confine it to a finite set, from which the parent is hit almost surely. Hence no-return implies reaching every generation that exists on its infinite trajectory. Therefore

\[
B^{(h)}(T)
=
B(T)+\mathbb P_o^T(D\ge h,F),
\]

which is (4.1).

Since `D` is integer-valued and nonnegative,

\[
\mathbb E^T[D\mathbf1_F]
=\sum_{h\ge1}\mathbb P_o^T(D\ge h,F).
\]

Tonelli and (4.1) give (4.2). `square`

### Why this matters

The previous run isolated `ell_*<infinity` but still phrased it in path language. Formula (4.2) identifies exactly what has to be summable: the *annealed truncation error of the electrical conductance recursion*. That makes the extinction Jacobian, smoothing-transform estimates, and monotone fixed-point technology available directly.

---

# Part II. B3 — a stronger theorem: surviving escape conductance has an exp(-c/x) lower tail

The main danger in every conductance argument is the singular region `B downarrow 0`. The next theorem controls that region much more strongly than a finite negative moment.

## 5. Small positive conductance distribution

For type `i`, define

\[
F_i(x):=P_i(0<B\le x),\qquad x>0.
\tag{5.1}
\]

For `0<x<1`, set

\[
T(x):=\frac{x}{1-x}.
\tag{5.2}
\]

By (2.1), `0<B<=x` implies

\[
0<S\le T(x).
\tag{5.3}
\]

For a type-`i` potential child slot, the probability that it is transmitted and has *positive* conductance at most `y` is

\[
a_i(y):=\sum_jq_jp_{ij}F_j(y).
\tag{5.4}
\]

The probability that it carries any positive-conductance transmitted child is `t_i` from (2.2).

If `0<S<=y`, there is at least one small-positive child and no child with conductance greater than `y`. Therefore

\[
\boxed{
F_i(x)
\le
G(1-t_i+a_i(T(x)))-G(1-t_i).
}
\tag{5.5}
\]

This inequality is exact at the level of the slot categories; it only relaxes the additional requirement that the *sum* of several small conductances be at most `T(x)`.

## 6. Superexponential lower-tail theorem

### Theorem R7-07-H0008-C — `exp(-c/x)` small-conductance bound

Under the finite-type source assumptions in Section 2 and R14's certified `rho(J)<1`, there exist constants

\[
C<\infty,\qquad c>0,\qquad x_0>0
\]

such that for every type `i` and every `0<x<=x_0`,

\[
\boxed{
P_i(0<B\le x)\le C\exp(-c/x).
}
\tag{6.1}
\]

No finite second moment of `nu` is needed for this local estimate beyond `m_*=E nu<infinity`: all Taylor expansions occur at a point uniformly bounded away from `1`.

Consequently, for every real `r>0`,

\[
\boxed{
E_{P_i}[B^{-r};\,B>0]<\infty.
}
\tag{6.2}
\]

Equivalently, the survival-conditioned conductance has moments of *every negative order*.

### Proof

Because `rho(J)<1`, choose a vector `w in (0,infinity)^d` and a number `kappa<1` such that

\[
Jw\le\kappa w
\tag{6.3}
\]

componentwise. For example, choose any `kappa` in `(rho(J),1)` and take a positive resolvent vector for `I-J/kappa`.

Define the weighted tail norm

\[
f(x):=\max_j\frac{F_j(x)}{w_j}.
\tag{6.4}
\]

Then

\[
a_i(y)
\le f(y)A_i,
\qquad
A_i:=\sum_jq_jp_{ij}w_j.
\tag{6.5}
\]

Since `F_j(y) downarrow 0` as `y downarrow 0`, also `f(y) downarrow0`. Because every `t_i>0` and there are finitely many types, for all sufficiently small `y` we have

\[
0\le a_i(y)\le t_i/2
\qquad\text{for every }i.
\tag{6.6}
\]

All arguments of `G` in (5.5) then lie in a compact interval strictly below `1`. A pgf is analytic on `[0,1)`, so there is a finite uniform constant `C_2` such that

\[
G(1-t_i+a)-G(1-t_i)
\le G'(1-t_i)a+C_2a^2
\tag{6.7}
\]

for every relevant `i,a`. Combining (5.5)--(6.7),

\[
F_i(x)
\le
\sum_jJ_{ij}F_j(T(x))+C_2A_i^2f(T(x))^2.
\tag{6.8}
\]

Divide by `w_i`, maximize over `i`, and absorb the finitely many constants into `C_3`:

\[
f(x)
\le
\kappa f(T(x))+C_3f(T(x))^2.
\tag{6.9}
\]

Fix `kappa_1` with

\[
\kappa<\kappa_1<1.
\]

Since `f(y)->0`, choose `x_0>0` small enough that whenever `0<y<=x_0`,

\[
C_3f(y)\le\kappa_1-\kappa.
\tag{6.10}
\]

After decreasing `x_0` once more if necessary, `T(x)<=x_0` on the interval where we start the iteration. Then

\[
\boxed{
f(x)\le\kappa_1 f(T(x)).}
\tag{6.11}
\]

The crucial point is that `T` linearizes after reciprocal change of variables:

\[
\frac1{T(x)}=\frac1x-1,
\qquad
T^k(x)=\frac{x}{1-kx}
\tag{6.12}
\]

as long as `kx<1`. Starting from sufficiently small `x`, choose

\[
k=\left\lfloor\frac1x-\frac1{x_0}\right\rfloor.
\tag{6.13}
\]

Every intermediate iterate remains at most `x_0`, so (6.11) can be iterated `k` times:

\[
f(x)
\le\kappa_1^k f(T^k(x))
\le C_4\kappa_1^{1/x-1/x_0-1}
\le C_5\exp(-c/x),
\tag{6.14}
\]

with `c=-log(kappa_1)>0`. Since the weights `w_i` are fixed, (6.1) follows.

For (6.2), set `Y=1/B` on `{B>0}`. Equation (6.1) says

\[
P_i(Y\ge t,\,B>0)\le C e^{-ct}
\]

for all sufficiently large `t`. Every positive polynomial moment of `Y` is therefore finite. `square`

### Interpretation

This theorem makes the pipe mechanism quantitative at the conductance level. Along an exact one-infinite-child pipe,

\[
B_{parent}=\frac{B_{child}}{1+B_{child}},
\qquad
\frac1{B_{parent}}=1+\frac1{B_{child}}.
\tag{6.15}
\]

Thus conductance of order `x` naturally corresponds to a pipe scale of order `1/x`. R14's subcritical extinction Jacobian makes such pipe lengths exponentially unlikely, and the nonlinear estimate above shows that genuine branch points do not create a worse small-conductance tail: the result is `exp(-c/x)`, hence all inverse moments.

This is substantially stronger than the logarithmic integrability proved in the earlier fresh-reset run.

---

# Part III. B20 — the truncation recursion isolates one surviving Feynman–Kac operator

## 7. Exact normalized truncation recursion

Let

\[
\delta_h(T)=B^{(h)}(T)-B(T).
\]

For a surviving tree (`B>0`) define

\[
R_h(T):=\frac{\delta_h(T)}{B(T)}.
\tag{7.1}
\]

At the root, write

\[
S=\sum_uB_u,
\qquad
S^{(h)}=\sum_uB_u^{(h)},
\qquad
r_h:=\frac1{1+S^{(h)}}.
\]

From (3.2),

\[
\delta_{h+1}
=\frac{S^{(h)}-S}{(1+S^{(h)})(1+S)}.
\tag{7.2}
\]

Since `B=S/(1+S)`, division by `B` yields the exact formula

\[
R_{h+1}
=
 r_h\left[
 \sum_{u:B_u>0}\frac{B_u}{S}R_h(T_u)
 +\frac{1}{S}\sum_{u:B_u=0}B_u^{(h)}
 \right].
\tag{7.3}
\]

The first bracketed term is precisely the harmonic-descendant average. Define

\[
(K_Hf)(T)
:=\sum_{u:B_u>0}\frac{B_u}{S}f(T_u).
\tag{7.4}
\]

Because `S^(h)>=S`,

\[
r_h\le\frac1{1+S}=1-B(T).
\tag{7.5}
\]

Hence

\[
\boxed{
R_{h+1}(T)
\le
(1-B(T))(K_HR_h)(T)
+
\frac{1-B(T)}{S(T)}
\sum_{u:B_u=0}B_u^{(h)}.
}
\tag{7.6}
\]

This is the exact decomposition that the previous pathwise approach was missing.

## 8. The extinct forcing is not the hard channel

On extinction, `B=0` and

\[
B^{(h)}\le\mathbf1_{\{\text{tree height}\ge h\}}.
\tag{8.1}
\]

If extinction has positive probability, the multitype process conditioned on extinction has offspring pgf

\[
\widehat F_i(z)=\frac{F_i(e_1z_1,\ldots,e_dz_d)}{e_i},
\]

and mean matrix

\[
\widehat J_{ij}=J_{ij}\frac{e_j}{e_i}.
\tag{8.2}
\]

Thus `widehat J` is diagonally similar to `J`; by (2.4),

\[
\rho(\widehat J)=\rho(J)<1.
\tag{8.3}
\]

If extinction probability is zero, this channel is absent. Otherwise (8.3) gives constants `C<infinity`, `theta<1` with

\[
P_i(B=0,\text{height}\ge h)\le C\theta^h.
\tag{8.4}
\]

Therefore the purely extinct contribution to (4.2) is summable.

Moreover, the singular factor `1/S=(1-B)/B` in the second term of (7.6) is no longer intrinsically dangerous: Theorem C gives moments of every order of `1/B` on survival. Under the finite offspring-variance hypothesis already used by the source's finite-type boundary theory, Hölder together with (8.4) makes the annealed extinct-side forcing in (7.6) summable. The exact constants are not needed here; the key point is that the forcing can be handled by ordinary moment estimates once (6.2) is available.

## 9. The exact remaining operator

After removing the summable extinct forcing, the homogeneous surviving channel is the positive Feynman–Kac operator

\[
\boxed{
(\mathcal K f)(T)
:=(1-B(T))(K_Hf)(T).
}
\tag{9.1}
\]

Along the harmonic descendant chain `T_0,T_1,...`,

\[
(\mathcal K^nf)(T)
=
E_T^H\left[
\prod_{k=0}^{n-1}(1-B(T_k))\,f(T_n)
\right].
\tag{9.2}
\]

Thus the remaining C4 roof issue is no longer “control arbitrary failed excursions.” It is:

\[
\boxed{
\text{prove summability / spectral decay of the killed harmonic-descendant semigroup }\mathcal K.
}
\tag{9.3}
\]

For example, any proof that for every source type `i`

\[
\sum_{n\ge0}
E_{P_i}\left[
B(T)(\mathcal K^n\mathbf1)(T)
\right]<\infty
\tag{9.4}
\]

immediately combines with the summable forcing above and (4.2) to give `ell_i<infinity`, hence the finite regeneration roof by the preceding R7-07 theorem.

A stronger sufficient statement is an exponential estimate

\[
E_{P_i}\left[B\,\mathcal K^n\mathbf1\right]\le C\eta^n,
\qquad\eta<1.
\tag{9.5}
\]

## 10. Why the obvious contraction proof still fails

It is tempting to say simply that the factor `1-B(T)` in (9.1) is strictly below one. That is not enough: the state space contains surviving trees with arbitrarily small positive conductance, and on such trees `1-B` is arbitrarily close to one.

Theorem C shows that those states are extraordinarily rare under the source law,

\[
P_i(0<B\le x)\le Ce^{-c/x},
\]

but the Feynman–Kac weighting itself favors trajectories spending time at small `B`. Therefore a source-law tail bound alone does not yet prove that the *tilted* iterates of `mathcal K` keep the same tail uniformly in time.

This is the exact point where a new idea is required. A valid completion can take any one of the following forms:

1. a Foster–Lyapunov inequality for `mathcal K` in a weighted space that uses the reciprocal shift `1/B_parent=1+1/B_child` on the one-infinite-child channel and a strict branch-point contraction;
2. a quasi-compact decomposition `mathcal K=mathcal K_pipe+mathcal K_branch`, with the pipe spectral radius controlled by R14's `rho(J)<1` and the branch part compact/tight using the `exp(-c/B)` tail;
3. a regeneration theorem proving positive density of genuine branch points along the *killed harmonic* path rather than along the unweighted source genealogy.

What does **not** suffice is another unconditional average such as `E_P[1-B]<1`; repeated Feynman–Kac weighting changes the environment law. This is the precise failure of the naive contraction algorithm.

---

# Part IV. Relation to the earlier reset law

The previous R7-07 run proved the fresh successful-regeneration reset

\[
Q_j(dT)=\frac{B(T)}{b_j}P_j(dT),
\qquad b_j=E_{P_j}B(T).
\tag{11.1}
\]

Theorem C immediately upgrades its integrability. For every `r>0`,

\[
E_{Q_j}[B^{-r}]
=\frac1{b_j}E_{P_j}[B^{1-r};B>0]<\infty,
\tag{11.2}
\]

because all source inverse moments are finite. In particular every logarithmic moment needed at the regeneration block start is finite, not merely the first one previously bounded via `x(-log x)<=1/e`.

This does **not** by itself prove the within-block reverse absolute continuity or the stationary harmonic environment. It does remove one entire family of potential integrability obstructions from those later steps.

---

# Part V. Honest status

## 12. What is proved in this artifact

1. **Exact path/electrical equivalence:**
   \[
   P^T(D\ge h,F)=B^{(h)}(T)-B(T).
   \]
2. **Exact annealed roof-moment representation:**
   \[
   \ell_i=\sum_hE_i[B^{(h)}-B].
   \]
3. **Superexponential positive-conductance lower tail:**
   \[
   P_i(0<B\le x)\le Ce^{-c/x}.
   \]
4. **All negative conductance moments:**
   \[
   E_i[B^{-r};B>0]<\infty\quad\forall r>0.
   \]
5. **Exact normalized truncation recursion** (7.3) and the killed harmonic Feynman–Kac reduction (9.1).
6. The extinct-tree forcing is subcritical through the extinction Jacobian and is not the principal remaining mechanism.

## 13. What is not proved

- `ell_*<infinity` under the full source hypotheses is **not yet proved**.
- The spectral/summability estimate (9.4) for `mathcal K` is open in this artifact.
- The stationary equivalent harmonic environment and full PF–KL dimension-drop theorem are not closed.
- H0008 is not owned by R7-07 and is not source-closed.
- No novelty claim is made; the small-conductance estimate is a derived theorem in this repository, but a bounded literature search is not a novelty certificate.

## 14. Literature relation checked 2026-09-19

The primary arXiv record for Kumar's paper still exposes v1 dated 17 Aug 2026. The Kumar–Duddala companion arXiv:2608.21125 (21 Aug 2026) studies front propagation/Bramson correction and continuous-type limit theory rather than resolving this finite-type harmonic-measure clause.

The closest one-type harmonic-measure architecture remains Pierre Rousselin's work, including arXiv:1711.07920, which constructs an invariant forward environment at exit times by regeneration/ergodic methods for transient random walks on one-type Galton–Watson trees, and arXiv:1708.06965, which constructs invariant measures for marked-GW flow rules. These support the route but do not directly supply the multitype killed-operator estimate (9.4). Search misses are negative evidence only.

## 15. Next mathematical attack

If no lawful new shard-6 source becomes claimable on the next run, do **not** repeat the present truncation argument. The sharp next attack is the operator in (9.1). Suggested nonrepeating Section-B triple:

- **B12 FIND WHAT IS CONSERVED:** look for a weighted measure under which `mathcal K_pipe` and `mathcal K_branch` have an exact mass balance;
- **B29 ADD THE POINTS AT INFINITY:** compactify the conductance state with `u=1/B` and treat `u=infinity` as the pipe boundary, using Theorem C for tightness;
- **B6 DEFORM TO A POINT YOU CAN SOLVE:** prove `r(mathcal K)<1` first in the type-lumpable/one-type slice, then identify the term that obstructs continuation to the non-lumpable finite-type case.

The measurable quantity remains **UNMEASURED** because R7-07 has no lawfully admitted target. These theorems are admission-feasibility progress, not a substitute metric.