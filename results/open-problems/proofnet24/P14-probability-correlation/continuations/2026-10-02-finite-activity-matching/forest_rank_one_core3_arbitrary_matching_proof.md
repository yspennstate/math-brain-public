# Rank-one spokes over a three-vertex core: all matching-edge pairs

## Exact theorem

Let a graph have three core vertices `1,2,3` and any number of terminal vertices. The core-edge activities are arbitrary `p12,p13,p23≥0`. Fix positive column weights `b1,b2,b3`. Terminal `j` joins core vertex `i` with spoke activity

\[
z_{ji}=a_j b_i,\qquad a_j\ge0.
\]

The only edges between terminals form an arbitrary matching, with arbitrary nonnegative activities. Choose any two distinct matching edges `e,f`; their four endpoints are automatically distinct. If the four endpoint row weights are positive, then

\[
R_{ef}=Z_eZ_f-ZZ_{ef}>0,
\qquad Z=\sum_{F\text{ acyclic}}\prod_{h\in F}z_h.
\]

Other terminal row weights may be zero. Missing core or matching edges are allowed by zero activity. The activities of `e,f` themselves do not enter `R`; if both are positive, the corresponding strict negative correlation is

\[
\Pr(e\in F)\Pr(f\in F)-\Pr(e,f\in F)
=\frac{z_ez_f}{Z^2}R_{ef}>0.
\]

If an endpoint row weight is allowed to vanish, the nonnegative conclusion follows by continuity. Parallel core edges can be aggregated by adding their activities. This theorem concerns pairs of matching edges only; it makes no claim for pairs involving spokes or core edges, or for terminal-terminal edges that do not form a matching.

The number of terminals and matching edges is unbounded. The proof below holds at every stated activity, rather than only asymptotically. No historical novelty claim is made.

## Five-state weighted terminal transfer

Record only the connectivity partition of the three core vertices. There are five states. Define

\[
B=b_1+b_2+b_3,\qquad J=b_1b_2b_3,\qquad d(x)=1+Bx.
\]

Adding one terminal of row weight `x` chooses a subset of its three spokes. Choosing zero or one spoke does not change core connectivity and has total weight `d(x)`. Define `P` to merge a pair of distinct core components, counting the pair `i,j` with weight `b_i b_j`. Define `Q` to merge all three components, with weight `J`; this transition is allowed only from the three-component state. Then the exact transfer is

\[
T(x)=d(x)I+x^2P+x^3Q.
\]

The nilpotent multiplication rules are

\[
P^2=2B Q,\qquad PQ=QP=Q^2=0.
\]

For example, two successive pair merges have total weight

\[
\sum_{\{i,j\}} b_i b_j b_k(b_i+b_j)=2BJ,
\]

where `k` is the remaining core vertex. This equals `2B` times the weight of `Q`. Every other displayed product attempts a further merge after all components have already been merged.

Put

\[
\alpha(x)=\frac{x^2}{d(x)},\qquad
\gamma(x)=\frac{x^3}{d(x)^2}.
\]

Using `P²=2BQ` and `Q` times either nilpotent operator equal to zero gives the exact identity

\[
\boxed{T(x)=d(x)\exp\{\alpha(x)P+\gamma(x)Q\}.}
\]

Indeed, the exponential has `Q` coefficient `γ+Bα²=x³/d`. All these operators commute.

## Core coefficients

Let `r` be the initial row vector of core-forest weights, and let `1` be the column vector of ones. Write

\[
X=p_{12}+p_{13}+p_{23},\qquad
t=p_{12}p_{13}+p_{12}p_{23}+p_{13}p_{23},\qquad
S=1+X+t.
\]

The initial scalar products are

\[
r1=S,\qquad rQ1=J,\qquad rP1=L,
\]

where

\[
L=b_1b_2+b_1b_3+b_2b_3
+p_{12}b_3(b_1+b_2)
+p_{13}b_2(b_1+b_3)
+p_{23}b_1(b_2+b_3).
\]

This follows directly from the zero-edge, one-edge, and two-edge core forests. The empty core permits all three weighted pair merges. A core forest containing edge `i,j` permits only merges to the remaining vertex `k`, of total weight `b_k(b_i+b_j)`. Only the empty core permits a triple merge.

For any product of transfer groups of the form

\[
D\exp\{UP+\Gamma Q\},
\]

the exact resulting forest sum is

\[
DF,\qquad
F=S+LU+J\Gamma+BJ U^2.
\]

## Including every other matching edge

Remove the two selected matching edges `e,f` for the moment, leaving their four endpoint terminals unmerged. All other terminals form disjoint groups: singletons, or the endpoint pair of another matching edge.

A singleton of row weight `x` contributes `T(x)`. A matching pair with row weights `a,b` and matching-edge activity `w≥0` contributes the exact deletion/contraction sum

\[
H=T(a)T(b)+wT(a+b).
\]

Contraction aggregates each pair of parallel spokes to activity `(a+b)b_i`. Since the matching edges are vertex-disjoint, these group contributions multiply without interactions between their terminal vertices.

Write `s=a+b` and

\[
k_0=d(a)d(b),\quad k_1=d(s),\quad
K=k_0+wk_1,\quad \theta=\frac{wk_1}{K}\in[0,1].
\]

Also put

\[
u_0=\alpha(a)+\alpha(b),\quad u_1=\alpha(s),\quad
g_0=\gamma(a)+\gamma(b),\quad g_1=\gamma(s),\quad
\delta=u_1-u_0.
\]

Expanding the nilpotent exponential and averaging the two branches shows exactly that

\[
H=K\exp\{U_H P+\Gamma_H Q\},
\]

\[
U_H=(1-\theta)u_0+\theta u_1,
\]

\[
\Gamma_H=(1-\theta)g_0+\theta g_1
+B\theta(1-\theta)\delta^2.
\]

The variance term has been retained; dropping it would give an incorrect transfer.

## A bound preserved by every matching group

For a singleton,

\[
\frac{\alpha(x)}B-\gamma(x)
=\frac{x^2}{B d(x)^2}\ge0.
\]

The same inequality survives the matching-pair mixture. To see this, direct algebra gives

\[
\delta=\frac{ab(2+Bs)}{d(a)d(b)d(s)}\ge0,
\qquad
\delta\le\frac{a}{B d(a)},\quad
\delta\le\frac{b}{B d(b)}.
\]

For the first bound, cancellation reduces it to

\[
Bb(2+Bs)\le d(b)d(s),
\]

whose right side minus left side is `1+Ba>0`. The other bound is symmetric. The function `x/d(x)` is increasing, so `s/d(s)≥a/d(a)`.

It follows that both branches have margin at least `Bδ²`:

\[
\frac{u_0}B-g_0
=\frac{a^2}{B d(a)^2}+\frac{b^2}{B d(b)^2}
\ge B\delta^2,
\]

\[
\frac{u_1}B-g_1
=\frac{s^2}{B d(s)^2}\ge B\delta^2.
\]

Consequently,

\[
\frac{U_H}B-\Gamma_H
\ge B\delta^2\,[1-\theta(1-\theta)]\ge0.
\]

Multiplying all singleton and matching-pair groups adds their exponential coefficients and multiplies their positive scalar factors. Thus, for the base graph in which `e,f` are absent,

\[
D>0,\qquad U\ge0,\qquad 0\le\Gamma\le U/B.
\]

## Exact two-edge Rayleigh formula

For either selected matching pair of positive row weights `a,b`, define

\[
\delta=\alpha(a+b)-\alpha(a)-\alpha(b),\qquad
\epsilon=\gamma(a+b)-\gamma(a)-\gamma(b),\qquad
c=\frac{d(a+b)}{d(a)d(b)}.
\]

Both `δ` and `ε` are strictly positive. The explicit formula above proves this for `δ`. For `ε`, observe that

\[
\gamma(0)=0,\qquad \gamma''(x)=\frac{6x}{(1+Bx)^4}>0\quad(x>0).
\]

Strictly increasing derivative and `γ(0)=0` give strict superadditivity for positive arguments.

Contracting the selected pair changes `D` to `Dc`, `U` to `U+δ`, and `Γ` to `Γ+ε`. The corresponding increment of `F` is

\[
X_{\mathrm{pair}}
=\delta(L+2BJ U)+J\epsilon+BJ\delta^2.
\]

Use subscripts `e,f` for the two pairs. Writing

\[
Z=A+z_e B_e+z_f B_f+z_ez_f C
\]

gives exactly

\[
A=DF,\quad B_e=Dc_e(F+X_e),\quad B_f=Dc_f(F+X_f),
\]

\[
C=Dc_ec_f(F+X_e+X_f+2BJ\delta_e\delta_f).
\]

Therefore

\[
\boxed{R_{ef}=D^2c_ec_f
\,[X_eX_f-2BJ\delta_e\delta_f F].}
\]

All scalar factors outside the brackets are positive.

## Positivity of the bracket

First, the core expression is strictly positive. Expanding it in the arbitrary core activities yields

\[
\begin{aligned}
L^2-2BJ S={}&\sum_{i<j}b_i^2b_j^2\\
&+2\sum_{\{i,j\}}p_{ij}b_k^2(b_i^2+b_ib_j+b_j^2)\\
&+\sum_{\{i,j\}}p_{ij}^2b_k^2(b_i+b_j)^2\\
&+2p_{12}p_{13}b_2^2b_3^2
+2p_{12}p_{23}b_1^2b_3^2
+2p_{13}p_{23}b_1^2b_2^2,
\end{aligned}
\]

where `k` is the remaining core vertex in each sum. Every coefficient is nonnegative, and the constant sum is positive. Also `BL>J`, because `L≥b1b2+b1b3+b2b3` and multiplication by `B` includes `3J` plus positive terms.

Put `K0=L+2BJ U`. The preserved bound `Γ≤U/B` gives

\[
\begin{aligned}
K_0^2-2BJ F
&=L^2-2BJ S+2BJ LU+2B^2J^2U^2-2BJ^2\Gamma\\
&\ge L^2-2BJ S+2J(BL-J)U+2B^2J^2U^2>0.
\end{aligned}
\]

Since `X_e≥δ_e K0` and `X_f≥δ_f K0`, with positive `δ_e,δ_f`,

\[
X_eX_f-2BJ\delta_e\delta_f F
\ge\delta_e\delta_f(K_0^2-2BJ F)>0.
\]

This proves the theorem for every pair of matching edges, with every other matching activity already incorporated.

## Independent exact verification

The companion `forest_rank_one_core3_arbitrary_matching_exact.py` checks this proof by three separate calculations:

1. Original, uncontracted graph edge-subset enumeration for small examples, calculating all four coefficients `A,B_e,B_f,C` directly by acyclicity.
2. Explicit five-state connectivity transitions that enumerate all eight spoke subsets. Other matching edges are summed by their two direct deletion/contraction branches. This routine uses none of `α,γ,U,Γ` or the claimed positive bound.
3. The exponential formula and boxed Rayleigh identity.

All three methods agree for the original-graph cases. The explicit connectivity transfer also agrees with the formula for three or more matching edges, for a zero row away from the selected pair, for missing core edges, and for exact rational examples through 100 terminals. The symbolic argument, not these finite checks, establishes the unbounded theorem. See the companion results JSON for exact values.
