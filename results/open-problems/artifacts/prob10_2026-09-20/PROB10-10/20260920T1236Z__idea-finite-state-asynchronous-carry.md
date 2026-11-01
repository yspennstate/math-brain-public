Model: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.

# PROB10-10 idea before code: conservative finite-state asynchronous carry

## Frozen source target
Nearest-neighbor **undirected** first-passage percolation on `Z^2` with iid `Exp(1)` edge weights.  The source target remains strict convexity of the deterministic limit shape.  The first source-facing checkpoint is

\[
\Delta_{12}=2\mu(e_1)-\mu(1,1)>0.
\]

The retained rigorous axis lower bound is
\[
b=0.3002823,
\]
so it is enough for this checkpoint to prove
\[
\mu(1,1)<2b=0.6005646.
\]
This is only a restricted-direction PARTIAL result even if achieved.

The incomplete idea note `20260920T1148Z__idea-asynchronous-boundary-carry.md` proposed carrying the whole antidiagonal arrival profile instead of synchronizing at every block.  The present route makes that proposal into a rigorous finite-state certificate architecture; it is not another local-SAW/reflected-cone iteration.

## Exact strip decomposition
Use rotated coordinates
\[
s=x+y,\qquad d=x-y.
\]
Fix integers `L,W>=1`.  Let the `j`th band contain the lattice vertices
\[
B_j=\{(s,d):2jL\le s\le2(j+1)L,\ |d|\le W,\ s\equiv d\pmod2\}.
\]
Assign to `B_j` precisely the nearest-neighbor edges whose lower `s`-coordinate lies in
`[2jL,2(j+1)L-1]`.  Hence different bands have disjoint physical edge sets and their environments are iid.  Adjacent bands share only their boundary vertices.

Write
\[
D_W=\{d:|d|\le W,\ d\equiv0\pmod2\}
\]
for the offsets on the even antidiagonals.  For a normalized arrival-offset vector
`y in [0,infty]^{D_W}` with `min y=0`, and one reference-band environment `omega`, define
\[
F_\omega(y)(d')=
\min_{d\in D_W}\{y(d)+T_{B_0,\omega}((0,d),(2L,d'))\},
\]
where the minimum ignores `+infty` labels.  Put
\[
g(y,\omega)=\min_{d'}F_\omega(y)(d'),\qquad
\Phi(y,\omega)=F_\omega(y)-g(y,\omega){\bf1}.
\]
The min-plus map `F_omega` is coordinatewise monotone and additively homogeneous.

Without any projection, if `M_j` is the accumulated minimum boundary label and `Y_j` its normalized vector, then
\[
M_{j+1}=M_j+g(Y_j,\omega_j),\qquad
Y_{j+1}=\Phi(Y_j,\omega_j).
\]
This keeps all asynchronous boundary information and introduces no independence fiction: `omega_j` is fresh because the band edge sets are disjoint.

## New conservative projection theorem
Let `P` be any map on normalized boundary vectors satisfying

1. `P(y)>=y` coordinatewise (with `+infty` allowed), and
2. `min P(y)=0` whenever `min y=0`.

Run the projected recursion
\[
M_{j+1}=M_j+g(Y_j,\omega_j),\qquad
Y_{j+1}=P(\Phi(Y_j,\omega_j)).
\tag{1}
\]
Start from `Y_0(0)=0` and `Y_0(d)=+infty` for `d!=0`.

**Claim (path-dominance).**  For every realization and every `j`, every finite absolute label `M_j+Y_j(d)` dominates the weight of an actual lattice path from the origin to the corresponding boundary vertex, using only the first `j` bands.  In particular the minimum label `M_j` dominates the weight of some such path.

**Proof.**  At `j=0` this is immediate.  Assume it holds at boundary `j`.  For every finite source label and every terminal `d'`, concatenate its witnessing prefix path with a shortest path inside the fresh band.  Therefore `M_j+F_{omega_j}(Y_j)(d')` dominates an actual concatenated path weight.  Subtracting the minimum merely writes these absolute labels as `M_{j+1}+Phi`.  Applying `P` only raises or deletes (`+infty`) normalized labels and preserves at least one zero label, so each surviving absolute label still dominates a witness path.  Induct.  QED.

This point is the reason upward rounding is safe.  It deliberately makes the auxiliary process slower; it never treats a rounded process as an equality for true FPP.

## Bellman certificate with explicit finite-to-infinite error
Let
\[
\Psi(y,\omega)=P(\Phi(y,\omega)).
\]
Suppose a real-valued potential `h` bounded below on the reachable projected states and a number `lambda` satisfy
\[
\mathbb E\big[g(y,\omega)+h(\Psi(y,\omega))\big]-h(y)\le\lambda
\tag{2}
\]
for every reachable state `y`.  Conditioning on the past in (1) and summing (2) gives
\[
\mathbb E M_N\le N\lambda+h(Y_0)-\inf h.
\tag{3}
\]
At antidiagonal `s=2NL`, let `d_*` be a minimizing offset.  Append a fresh zig-zag from `d_*` to `0` on the *future* side of that antidiagonal:
\[
(s,d)\to(s+1,d-\operatorname{sgn}d)\to(s,d-2\operatorname{sgn}d).
\]
It uses exactly `|d_*|<=W` new edges, all having lower `s`-coordinate `2NL`, hence none were used by the bands.  Conditional on the past its expected cost is `|d_*|<=W`.  Consequently
\[
\frac{\mathbb E T(0,(NL,NL))}{NL}
\le
\frac{\lambda}{L}
+
\frac{h(Y_0)-\inf h+W}{LN}.
\tag{4}
\]
Taking `N->infty` yields the unconditional source-valid implication
\[
\boxed{\mu(1,1)\le\lambda/L.}
\tag{5}
\]
Thus any certified `lambda/L<0.6005646` proves `Delta_12>0`.

Compared with the first-hit/synchronization compiler, (4) has no per-block boundary reset and its stitching term is explicitly `O(N^{-1})`; all dependence is carried in `Y_j`.

## A genuinely finite state space
For mesh `eps>0` and cutoff `H=K eps`, define
\[
P_{eps,H}(y)_d=
\begin{cases}
0,&y_d=0,\\
 eps\lceil y_d/eps\rceil,&0<y_d\le H\text{ and the rounded value is }\le H,\\
+\infty,&y_d>H\text{ (or rounding exceeds }H).
\end{cases}
\tag{6}
\]
Then `P_{eps,H}(y)>=y`, `min P=0`, and every state coordinate lies in
\[
\{0,eps,2eps,\ldots,Keps,+\infty\}.
\]
If `m=|D_W|`, the number of normalized states is at most
\[
(K+2)^m-(K+1)^m,
\tag{7}
\]
because at least one coordinate is zero.  Therefore (2) becomes a finite-state average-reward/Bellman inequality once its one-band transition expectations are rigorously enclosed.  This removes the previous continuous boundary-state obstruction without paying an uncontrolled approximation error: projection is one-sided by construction.

For a fixed finite state set, writing
\[
c(y)=\mathbb E g(y,\omega),\qquad
p(y,y')=\mathbb P(\Psi(y,\omega)=y'),
\]
turns (2) into the finite linear inequalities
\[
c(y)+\sum_{y'}p(y,y')h(y')-h(y)\le\lambda.
\tag{8}
\]
The remaining rigor obligation is numerical integration / interval enclosure of `c,p`, not another FPP dependence lemma.

## Tail-safe route to interval certification
A future implementation must not truncate an `Exp(1)` edge to a finite value downward.  A safe scheme is:

- on the good event that all band edges are at most `R`, round each edge **upward** to a mesh;
- on the complement, use a fixed canonical crossing path from a zero-labelled source.

For even `W`, one band has `m_e=4LW` edges.  A canonical zig-zag crossing has `2L` iid exponential edges, so if its cost is `S`,
\[
\mathbb E S^2=(2L)^2+2L.
\]
The bad event `A_R` satisfies
\[
\mathbb P(A_R)\le m_e e^{-R},
\]
and Cauchy-Schwarz gives the explicit tail cost
\[
\mathbb E[S\mathbf1_{A_R}]
\le
\sqrt{(4L^2+2L)m_e e^{-R}}.
\tag{9}
\]
Thus a finite rounded good-event calculation can be augmented by a rigorous analytic tail term.  Equation (9) is the planned way to turn the finite-state screen into a proof rather than silently treating a truncated exponential as bounded.

## Negation-first test planned before certification
Before spending effort on interval transition kernels, test whether carrying the whole boundary profile has enough quantitative room at all.  The falsification screen will compare widths around the threshold and will also apply the conservative projection (6).  Failure of width 30--50 after carry would kill this route.  Passing is only evidence; it does not change `c_*`.

## Three materially different approaches compared
1. **Asynchronous carry + conservative finite projection (pursue now).**  It directly repairs the synchronization/dependence loss and has the exact compiler (4)--(8).
2. **P20 actual-geodesic/Busemann residual disagreement.**  The newest neighboring report proves linear U-backtracking patterns and sublinear total diagonal residual under flatness, but still lacks a path-unavoidable positive residual per pattern.  The pattern occurrence is selected by the axis geodesic, so cheap local bypasses are biased away; no source defect follows yet.
3. **Jacquet directed comparison + a directed diagonal upper bound.**  Jacquet gives strict `mu<mu_dir`, but not the numerical inequality `mu(1,1)<0.6005646` needed here.  Preliminary directed-strip screens remain too close/above the threshold, and no primary-source explicit constant found in the fresh search supplies the missing quantitative bound.

This run therefore changes method within the same source problem rather than extending the retired reflected-cone/local-SAW chain.