# P0072 — the first chorded double-subdivision losange is still geodesic-selecting

Status: **restricted theorem / PROVED CANDIDATE after an exact finite spanning-tree certificate and a complete stochastic argument; full canonical P0072 remains OPEN; publication novelty UNVERIFIED.**

This note continues the R7-02 loop-erased branch.  It settles the smallest graph singled out in the preceding run as the first place where scalar series suppression fails.  It does **not** settle arbitrary finite graphs and does not address the source's separate uniform-geodesic reinforcement rule.

## 1. Graph, paths, and exact path-count state

Start with the five-edge losange on `s,a,b,t`.  Subdivide `s-a` once by a new vertex `x`, subdivide `a-t` once by a new vertex `y`, and add the chord `x-y`.  The eight edges are

` sx, xa, ay, yt, xy, sb, bt, ab `.

All initial weights are one.  The unique shortest `s-t` path is

`R = s-b-t`.

There are exactly seven simple `s-t` paths.  Let their reinforcement counts after `n` ants be `P0,...,P6`, with `P4=R`:

- `P0 : s-x-a-y-t`;
- `P1 : s-x-a-b-t`;
- `P2 : s-x-y-a-b-t`;
- `P3 : s-x-y-t`;
- `P4 : s-b-t`;
- `P5 : s-b-a-x-y-t`;
- `P6 : s-b-a-y-t`.

Thus `sum_i P_i=n`.  The edge weights are exactly

\[
\begin{aligned}
w_{sx}&=1+P_0+P_1+P_2+P_3,\\
w_{xa}&=1+P_0+P_1+P_5,\\
w_{ay}&=1+P_0+P_2+P_6,\\
w_{yt}&=1+P_0+P_3+P_5+P_6,\\
w_{xy}&=1+P_2+P_3+P_5,\\
w_{sb}&=1+R+P_5+P_6,\\
w_{bt}&=1+P_1+P_2+R,\\
w_{ab}&=1+P_1+P_2+P_5+P_6.
\end{aligned}
\tag{1.1}
\]

For the loop-erased rule, the next reinforced path has the same law as the `s-t` path in a weighted uniform spanning tree.  Let `Z` be the weighted spanning-tree partition function and `N_i` the sum of tree weights over trees whose `s-t` path is `P_i`.  Then

\[
q_i=\frac{N_i}{Z},\qquad \sum_iN_i=Z.
\tag{1.2}
\]

The exact checker enumerates all 35 spanning trees of this eight-edge graph and constructs these polynomials over the integers.

## 2. B11 — dualize the path-incidence system

The chord destroyed the two scalar series states, but the seven path-incidence vectors have a different exact dual certificate.  Give edge costs

\[
c_{sx}=c_{yt}=c_{ab}=\frac12,
\qquad c_e=0\text{ on the other five edges}.
\tag{2.1}
\]

Every non-geodesic path `P0,P1,P2,P3,P5,P6` contains exactly two of the three sentinel edges `{sx,yt,ab}`, whereas `R` contains none.  Therefore

\[
\sum_{e\in P_i}c_e=1\quad(i\ne4),
\qquad
\sum_{e\in R}c_e=0.
\tag{2.2}
\]

Equivalently, if

\[
S_n:=\frac{w_{sx}+w_{yt}+w_{ab}}2,
\]

then

\[
S_n=\frac32+(n-R_n).
\tag{2.3}
\]

This is the replacement for the lost series-equality invariant: a non-geodesic ant increments `S` by exactly one and a geodesic ant increments it by zero.

Set

\[
t_n=n+\frac32,
\qquad
Y_n:=\frac{R_n+1/2}{t_n}.
\tag{2.4}
\]

Then `0<Y_n<1` and, if `I_{n+1}` is the indicator that the next reinforced path is `R`,

\[
Y_{n+1}-Y_n
=\frac{I_{n+1}-Y_n}{t_n+1}.
\tag{2.5}
\]

## 3. B16 — exact finite UST drift certificate

Substitute (1.1) into the 35-tree polynomials.  The exact integer polynomial

\[
D(P):=t_nN_R-(R+1/2)Z
\tag{3.1}
\]

has **1397 nonzero monomials and every coefficient is strictly positive**; the minimum coefficient is 2 and the maximum is 812.  Hence, at every finite state,

\[
\boxed{
q_R=\frac{N_R}{Z}>\frac{R+1/2}{n+3/2}=Y_n.
}
\tag{3.2}
\]

This is an exact finite statement, not a numerical fit.  The accompanying checker derives `Z,N_R` from the graph, expands (3.1) over `QQ[P0,...,P6]`, and checks coefficient positivity.

By (2.5), `Y_n` is a bounded strict submartingale.  Its predictable drift is

\[
\mathbb E[Y_{n+1}-Y_n\mid\mathcal F_n]
=\frac{q_R-Y_n}{t_n+1}>0.
\tag{3.3}
\]

Therefore `Y_n` converges almost surely and

\[
\sum_n\frac{q_R(n)-Y_n}{t_n+1}<\infty
\quad\text{a.s.}
\tag{3.4}
\]

The latter follows from the Doob decomposition: the nonnegative predictable compensator has bounded expectation because `0<=Y_n<=1`.

Also (3.2) implies

\[
q_R\ge \frac1{2t_n},
\]

so conditional Borel--Cantelli gives

\[
\boxed{R_n\to\infty\quad\text{a.s.}}
\tag{3.5}
\]

### Interior projective limits are impossible

For a support `A` of path-count coordinates containing `R` and at least one non-geodesic path, restrict `D` and `Z` to the variables in `A` and retain their highest homogeneous degrees.  The exact checker exhausts all

\[
2^6-1=63
\]

such supports and verifies in every case that

\[
\deg D_A=\deg Z_A+1
\tag{3.6}
\]

and that the leading polynomial of `D_A` has strictly positive coefficients (minimum coefficient 2).

Suppose `Y_n->y` with `0<y<1`.  Then `R_n/n->y` and the total non-geodesic path count has positive limiting density `1-y`.  Passing to a subsequence, the normalized seven path counts converge to some simplex point whose support contains `R` and at least one bad path.  By (3.6), in a conic neighborhood of that point the quantity `q_R-Y_n` is bounded below by a fixed positive constant for all sufficiently large `n`.

Normalized path counts move by at most `O(1/n)` per step.  Hence each sufficiently close visit to that neighborhood lasts `Theta(n)` steps before the process can leave a slightly larger neighborhood, forcing a fixed positive contribution to the sum in (3.4).  Infinitely many visits would make that sum diverge.  Therefore

\[
\boxed{Y_\infty\in\{0,1\}.}
\tag{3.7}
\]

It remains to rule out zero.

## 4. B24 — the extremal blown-up bad boundary has invasion exponent 3/2

Assume for contradiction that `Y_n->0`, equivalently `R_n/n->0`.  By (3.5), still `R_n->infinity`.  We prove

\[
\boxed{
\liminf_{n\to\infty}\frac{nq_R(n)}{R_n}\ge\frac32.
}
\tag{4.1}
\]

The six non-geodesic counts have total `n-R_n~n`; pass to a subsequence on which their normalized vector converges.

The geodesic edge `sb` is reinforced by the bad paths `P5,P6`, while `bt` is reinforced by the bad paths `P1,P2`.  If both groups have positive macroscopic mass, then both geodesic edges have order-`n` weight and the exact tree formula gives `q_R->q_*>0`; since `R/n->0`, the ratio in (4.1) then tends to infinity.  Thus only the boundary faces on which one or both of these groups vanish macroscopically need analysis.

### 4.1 One geodesic edge is lower scale

By reflection it suffices to take `P5+P6=o(n)` while `P0,...,P3` have macroscopic coefficients `a0,...,a3`, with

\[
S=a_0+a_1+a_2+a_3>0,
\qquad a_1+a_2>0.
\]

Write `u=P5+P6`.  Keeping `R,u` at an arbitrary common lower scale and sending the macroscopic scale `T` to infinity, exact spanning-tree expansion gives

\[
q_R
=\frac1T\frac{2(R+u+1)N(a)}{D(a)}(1+o(1)),
\tag{4.2}
\]

uniformly whenever `R+u=o(T)`, where

\[
\begin{aligned}
N={}&2a_0^2+3a_0a_1+5a_0a_2+3a_0a_3+3a_1a_2+3a_1a_3+2a_2^2+3a_2a_3,
\end{aligned}
\tag{4.3}
\]

and

\[
\begin{aligned}
D={}&2a_0^3+4a_0^2a_1+8a_0^2a_2+6a_0^2a_3+2a_0a_1^2+10a_0a_1a_2+8a_0a_1a_3\\
&+6a_0a_2^2+12a_0a_2a_3+4a_0a_3^2+2a_1^2a_2+2a_1^2a_3+3a_1a_2^2\\
&+8a_1a_2a_3+3a_1a_3^2+a_2^3+4a_2^2a_3+3a_2a_3^2.
\end{aligned}
\tag{4.4}
\]

The key extremal inequality is

\[
4NS-3D\ge0.
\tag{4.5}
\]

Indeed the left side is exactly

\[
\begin{aligned}
&2a_0^3+8a_0^2a_1+4a_0^2a_2+2a_0^2a_3+6a_0a_1^2+14a_0a_1a_2+12a_0a_1a_3\\
&+10a_0a_2^2+8a_0a_2a_3+6a_1^2a_2+6a_1^2a_3+11a_1a_2^2+12a_1a_2a_3\\
&+3a_1a_3^2+5a_2^3+8a_2^2a_3+3a_2a_3^2,
\end{aligned}
\tag{4.6}
\]

which has strictly positive coefficients.  Since `n~ST`, dividing (4.2) by `R/n` yields, along any further subsequence for which `u/R` has an extended limit `U in [0,infinity]`,

\[
\liminf\frac{nq_R}{R}
\ge 2S(1+U)\frac ND
\ge\frac32.
\tag{4.7}
\]

If `U=infinity`, the left side diverges.  Reflection gives the same conclusion when `P1+P2=o(n)` but `P5+P6` has positive macroscopic mass.

### 4.2 Both geodesic side groups are lower scale

The remaining macroscopic support is contained in `{P0,P3}`.  Put

\[
u=P_1+P_2,
\qquad v=P_5+P_6,
\]

and let `P0~a0 T`, `P3~a3 T`, with `a0+a3>0`, while `u+v+R=o(T)`.  The exact two-scale tree expansion is

\[
q_R
=\frac1T
\frac{2(2a_0+3a_3)(R+u+1)(R+v+1)}
{(a_0+a_3)(a_0+2a_3)(2R+2u+2v+3)}
(1+o(1)).
\tag{4.8}
\]

Because `R->infinity`, pass to extended limits

\[
A=u/R,\qquad B=v/R.
\]

Using `n~(a0+a3)T`, (4.8) gives

\[
\liminf\frac{nq_R}{R}
\ge
\frac{2a_0+3a_3}{a_0+2a_3}
\frac{(A+1)(B+1)}{A+B+1}.
\tag{4.9}
\]

The first factor lies in `[3/2,2]`, and

\[
\frac{(A+1)(B+1)}{A+B+1}
=1+\frac{AB}{A+B+1}\ge1,
\]

with the same inequality under the natural extended limits.  Thus (4.1) follows in every boundary chart.

The asymptotic expansions (4.2) and (4.8) are uniform over lower scales `o(T)`: `Z` and `N_R` are fixed finite polynomials, and after the displayed leading powers of `T` are removed every omitted term is smaller by a factor `O((R+u+v+1)/T)`.

## 5. Supercritical-birth exclusion

Use the already-proved R7-02 harmonic-number lemma: if an integer nondecreasing process `M_n` with Bernoulli increments satisfies

\[
M_n\to\infty,\qquad M_n/n\to0,
\]

then it cannot eventually have increment probability at least `cM_n/n` for any fixed `c>1`.  Its proof writes `H_{M_n}` as a convergent martingale plus its predictable drift; the assumed lower drift gives `H_{M_n}>=c' log n+O(1)` for some `c'>1`, contradicting `H_{M_n}<=log n+O(1)`.

On the event `Y_n->0`, (3.5) and (4.1) imply that for every fixed `1<c<3/2`, eventually

\[
q_R(n)\ge c\frac{R_n}{n}.
\]

Applying the lemma to `M_n=R_n` is a contradiction.  Therefore

\[
\boxed{Y_n\to1\quad\text{a.s.}}
\tag{5.1}
\]

and hence

\[
\boxed{\frac{R_n}{n}\to1\quad\text{a.s.}}
\tag{5.2}
\]

## 6. Restricted theorem

Every non-geodesic edge is used only by non-geodesic simple paths, so from (1.1)

\[
W_e(n)\le 1+n-R_n
\qquad(e\notin\{sb,bt\}).
\]

Equation (5.2) therefore gives

\[
\boxed{
\frac{W_e(n)}n\to0
\quad\text{for all six non-geodesic edges.}
}
\tag{6.1}
\]

For the two geodesic edges,

\[
R_n+1\le W_{sb}(n),W_{bt}(n)\le n+1,
\]

so

\[
\boxed{
\frac{W_{sb}(n)}n\to1,
\qquad
\frac{W_{bt}(n)}n\to1.
}
\tag{6.2}
\]

### Theorem
For the source loop-erased reinforcement rule with unit initial weights on the once-subdivided-on-both-sides losange with the additional chord `x-y`, the unique geodesic `s-b-t` captures asymptotically all linear edge weight: its two edges have normalized weight tending to one and every other edge has sublinear weight, almost surely.

This is the first R7-02 family member in which one legal path immediately destroys equality of the two edges inside each subdivided branch, so the theorem genuinely goes beyond the scalar series-suppression architecture of the preceding run.

## 7. Exact certificate and source scope

Executed checker:

`research7_2026-09-17/R7-02/artifacts/2026-09-18/2026-09-18T113000Z__P0072_one_chord_exact_checker.py`

Archived output:

`research7_2026-09-17/R7-02/artifacts/2026-09-18/2026-09-18T113000Z__P0072_one_chord_exact_checker.out`

The output ends `ALL_EXACT_CHECKS_PASS`.  It certifies the 35-tree enumeration, the seven path costs, the 1397-term strict drift polynomial, all 63 positive-R/positive-bad projective supports, the 17-term coefficientwise proof of (4.5), and the exact leading factorizations behind (4.2) and (4.8).

The canonical 2025 outside source asks for every finite graph and for both stated reinforcement rules.  This theorem covers one additional non-series-parallel finite graph for the loop-erased rule only.  Therefore canonical P0072 remains **PARTIAL / SOURCE OPEN**, and the frozen full-source metric remains `C_P0072=0`.
