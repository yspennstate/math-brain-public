Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# G0008 — spectral obstruction, punctured-star normal form, and a rigorous critical-point first-step certificate

Target: Campos--de Lima / canonical intake `G0008`, Bernoulli bond percolation on the square lattice.  Write

\[
\tau_n(p)=\mathbb P_p(0\leftrightarrow n e_1).
\]

The source-level square-lattice question asks whether `tau_{n+1}(p) <= tau_n(p)` for every `0<p<1` and every `n>=1`.  This artifact is **PARTIAL**: it proves a new source-valid special point, namely the strict first-step inequality at the self-dual point `p=1/2`, and gives two exact reformulations for future work.  It does not settle all `p`, does not set the frozen metric `M_axis` to 1, and makes no publication-novelty claim.

The previous R7-06 run established, for `x=0`, `y=e_1`, `z=2e_1` and the slit graph

\[
H=\mathbb Z^2\setminus\{xy,yz\},
\]

the exact identity

\[
\tau_1-\tau_2
=(1-p)\,[\Delta_H+pD_H]
=(1-p)\,[a_H-(1-p)b_H+p s_H],
\tag{1}
\]

where `a_H` is the terminal partition mass `xy|z`, `b_H` the mass `xz|y`, and `s_H` the all-separate mass.  The present run continues from (1), rather than restarting.

## B11 — dualize: the axial connectivity sequence is a Fourier transform of a positive measure

### Proposition 1 (Herglotz representation of percolation connectivity)

For every fixed `p`, the bi-infinite sequence

\[
 n\longmapsto \tau_{|n|}(p)
\]

is positive definite.  Consequently there is a symmetric probability measure `mu_p` on the unit circle such that

\[
\boxed{\tau_n(p)=\int_{-\pi}^{\pi}\cos(n\theta)\,d\mu_p(\theta),\qquad n\ge0.}
\tag{2}
\]

#### Proof

Fix one percolation configuration `omega` and put `v_j=j e_1`.  On finitely many axial vertices define

\[
K_\omega(i,j)=\mathbf 1_{\{v_i\leftrightarrow v_j\}}.
\]

Open connectivity is an equivalence relation.  Hence for every finite scalar family `(c_i)`,

\[
\sum_{i,j}c_i\overline{c_j}K_\omega(i,j)
=
\sum_{C}\left|\sum_{i:v_i\in C}c_i\right|^2\ge0,
\]

where the sum on the right runs over open clusters meeting the selected vertices.  Thus `K_omega` is positive semidefinite.  Taking expectations preserves positive semidefiniteness, and translation invariance makes the expected kernel Toeplitz:

\[
\mathbb E K_\omega(i,j)=\tau_{|i-j|}(p).
\]

Herglotz's theorem gives a finite positive measure whose Fourier coefficients are this sequence.  Since `tau_0=1`, the measure has total mass one; since the coefficients are real and even, it may be chosen symmetric.  This proves (2).  QED.

The first comparison is therefore exactly

\[
\boxed{
\tau_1-\tau_2
=
\int(\cos\theta-\cos2\theta)\,d\mu_p(\theta)
=
\int 2\sin(3\theta/2)\sin(\theta/2)\,d\mu_p(\theta).
}
\tag{3}
\]

The integrand is nonnegative on `|theta|<=2pi/3` and negative on the complementary high-frequency arc.  Any first-step counterexample must therefore satisfy the exact spectral imbalance

\[
\int_{|\theta|>2\pi/3}(\cos2\theta-\cos\theta)\,d\mu_p
>
\int_{|\theta|<2\pi/3}(\cos\theta-\cos2\theta)\,d\mu_p.
\tag{4}
\]

This is a useful dual obstruction, but positive definiteness alone cannot prove the conjecture.  For `0<r<=1/2`, the abstract probability measure

\[
\mu=(1-r)\delta_0+r\delta_\pi
\]

has nonnegative Fourier coefficients

\[
\widehat\mu(n)=(1-r)+r(-1)^n,
\]

yet `hat mu(2)=1 > 1-2r=hat mu(1)`.  Hence a proof must use specifically planar/percolative structure, not merely the PSD property of cluster-equivalence kernels.

### B11 outcome

The problem has a clean dual language: rule out excessive spectral mass beyond `2pi/3` using planarity/FKG/finite-energy structure.  The construction above is also an exact no-go example for a purely Toeplitz-PSD proof.

---

## B30 — localize, then identify the gluing obstruction

### 2.1 Exact finite-volume boundary-state identity

Let `Lambda` be any finite box containing `x,y,z`.  Condition on every edge outside `Lambda`.  The outside open clusters induce a random wiring partition `Pi` on the boundary vertices of `Lambda`; conditional on `Pi`, all interior edges remain independent Bernoulli(`p`).  If

\[
F_\Lambda^\pi(p)
=
\mathbb P_{\Lambda,p}^{\pi}(x\leftrightarrow y)
-
\mathbb P_{\Lambda,p}^{\pi}(x\leftrightarrow z),
\]

then the tower property gives the exact identity

\[
\boxed{\tau_1(p)-\tau_2(p)=\mathbb E[F_\Lambda^{\Pi}(p)].}
\tag{5}
\]

For fixed `Lambda,pi`, `F_Lambda^pi` is a finite exact polynomial in `p` and `1-p`.  Therefore a certificate `F_Lambda^pi>=0` for every realizable boundary wiring `pi` would settle the first comparison.  Conversely, free-boundary positivity alone does **not** glue: the exterior may choose a wiring that strongly favors `x<->z`.  Equation (5) isolates the exact boundary-state obstruction rather than hiding it in a truncation error.

A softer sufficient version is also immediate.  Split boundary states into good and bad sets `G,B`, and suppose

\[
F_\Lambda^\pi\ge m_+\ge0\quad(\pi\in G),
\qquad
F_\Lambda^\pi\ge -m_-\quad(\pi\in B).
\]

Then

\[
\tau_1-\tau_2\ge m_+\mathbb P(\Pi\in G)-m_-\mathbb P(\Pi\in B).
\tag{6}
\]

Thus a finite exact polynomial calculation plus a rigorous probability bound for a small family of bad wirings is enough; one need not solve every boundary state uniformly.

### 2.2 Delete the whole central star: only six D4 orbit masses remain

Now refine (1).  Besides the two horizontal slit edges `xy,yz`, delete the two vertical edges incident to `y`.  Call the resulting punctured graph `K`.  Around the hole, in cyclic order, write the neighbours of `y` as

\[
x,\ u,\ z,\ d.
\]

Under Bernoulli(`p`) percolation on `K`, their cluster partition is planar.  The crossing partition `xz|ud` with two distinct opposite-pair clusters is impossible, so there are 14 noncrossing partitions.  By the full dihedral symmetry around the puncture, they collapse to six orbit probabilities, where each symbol denotes the probability of **one specified partition** in the orbit:

- `sigma`: all four singletons (orbit size 1);
- `alpha`: one adjacent pair plus two singletons (size 4);
- `beta`: one opposite pair plus two singletons (size 2);
- `gamma`: two noncrossing adjacent pairs (size 2);
- `delta`: a triple plus a singleton (size 4);
- `epsilon`: all four connected (size 1).

Hence

\[
\boxed{\sigma+4\alpha+2\beta+2\gamma+4\delta+\epsilon=1.}
\tag{7}
\]

Restore only `yu,yd`, independently with probability `p`, to recover the slit graph `H`.  Put `q=1-p` and

\[
B_H:=a_H-qb_H+p s_H,
\]

so that (1) is `tau_1-tau_2=q B_H`.  Conditioning on each of the 14 noncrossing partitions and then summing within its D4 orbit gives

\[
\boxed{
\begin{aligned}
B_H={}&p\sigma
+2p(1+2q)\alpha
+(p-q)\beta\\
&+2pq(1+q)\gamma
+(1-q^2-2q^3)\delta
-q^3\epsilon.
\end{aligned}}
\tag{8}
\]

This is an exact six-variable finite normal form for the first source milestone.  The finite orbit enumeration and all coefficients in (8) were independently checked symbolically; the checker and output accompany this artifact.

At `p=q=1/2`, (8) becomes

\[
\boxed{
B_H
=\frac12\sigma+2\alpha+\frac34\gamma+\frac12\delta-\frac18\epsilon.
}
\tag{9}
\]

The opposite-pair-only orbit `beta` disappears completely at self-duality; the only negative coefficient is the all-four-connected orbit `epsilon`.

### 2.3 Critical self-duality supplies one exact linear relation

Condition the original horizontal edge `xy` to be closed in critical square-lattice percolation.  Standard planar self-duality of the deleted-edge geometry gives

\[
\mathbb P_{1/2}(x\leftrightarrow y\mid xy\text{ closed})=\frac12.
\tag{10}
\]

This is the local self-dual statement underlying the source's observation that its nearest-neighbour detour threshold equals `p_c(Z^2)=1/2`.

Given the punctured configuration on `K`, let `m_x` be the number of vertices among `{u,z,d}` that lie in the `K`-cluster of `x`.  After restoring the other three edges incident to `y`, each with probability `1/2`, the vertex `y` fails to connect to `x` exactly when all `m_x` corresponding star edges are closed.  Hence (10) is equivalent to

\[
\mathbb E[2^{-m_x}]=\frac12.
\tag{11}
\]

Summing `2^{-m_x}` over each D4 orbit gives respectively

\[
1,\quad 3,\quad \frac32,\quad 1,\quad \frac74,\quad \frac18.
\]

Thus (11), together with (7), yields the exact relation

\[
\boxed{4\sigma+8\alpha+4\beta-2\delta-3\epsilon=0.}
\tag{12}
\]

Substituting (12) into (9) gives the equivalent form

\[
B_H
=\frac13\sigma+\frac53\alpha-\frac16\beta
+\frac34\gamma+\frac7{12}\delta.
\tag{13}
\]

So the critical problem is reduced to controlling exactly one potentially adverse orbit, the opposite-pair-only mass `beta`.

### 2.4 FKG plus planarity closes the critical first comparison

Define the increasing events on `K`

\[
A=\{x\leftrightarrow z\},\qquad C=\{u\leftrightarrow d\}.
\]

By D4 symmetry,

\[
\mathbb P(A)=\mathbb P(C)=T:=\beta+2\delta+\epsilon.
\tag{14}
\]

If both opposite connections occur, planarity forces the two open clusters to intersect, so all four terminals are in one cluster.  Therefore

\[
A\cap C=\{x,u,z,d\text{ all connected}\},
\qquad \mathbb P(A\cap C)=\epsilon.
\]

FKG now gives the exact nonlinear constraint

\[
\boxed{\epsilon\ge T^2.}
\tag{15}
\]

Use (7), (12), and (14) to solve for three orbit variables:

\[
\begin{aligned}
\sigma&=5\delta+\frac52\epsilon+2\gamma-1,\\
\alpha&=\frac12-\frac38\epsilon-\frac12T-\frac54\delta-\gamma,\\
\beta&=T-2\delta-\epsilon.
\end{aligned}
\tag{16}
\]

Since `alpha>=0`, dropping the nonnegative `delta,gamma` terms gives

\[
T\le1-\frac34\epsilon.
\]

Together with (15),

\[
T\le1-\frac34T^2,
\]

and hence

\[
\boxed{0\le T\le\frac23.}
\tag{17}
\]

Using (16), the critical bracket (9) can also be written

\[
8B_H=4+3\epsilon-8T+4\delta-2\gamma.
\tag{18}
\]

Again `alpha>=0` implies

\[
\gamma\le\frac12-\frac38\epsilon-\frac12T-\frac54\delta.
\]

Substitution into (18) yields

\[
8B_H
\ge
3+\frac{15}{4}\epsilon-7T+\frac{13}{2}\delta
\ge
3+\frac{15}{4}T^2-7T+\frac{13}{2}\delta.
\tag{19}
\]

The quadratic term factors as

\[
3+\frac{15}{4}T^2-7T
=\frac14(3T-2)(5T-6).
\tag{20}
\]

By (17), both factors on the right of (20) are nonpositive, so their product is nonnegative.  Therefore

\[
B_H\ge \frac{13}{16}\delta\ge0.
\tag{21}
\]

There is in fact a strict quantitative gap.  Force the three-terminal partition `{x,u,z}|{d}` by opening the four edges

\[
x\!-\!(-1,1),\quad (-1,1)\!-\!u,\quad u\!-\!(1,1),\quad (1,1)\!-\!z,
\]

and closing the three remaining `K`-edges incident to `d`.  This seven-edge cylinder event has probability `2^{-7}` at `p=1/2` and guarantees precisely that specified triple-plus-singleton partition.  Hence

\[
\delta\ge 2^{-7}.
\tag{22}
\]

Combining (1), (21), (22), and `q=1/2` proves the source-valid restricted theorem

\[
\boxed{
\tau_1(1/2)-\tau_2(1/2)
\ge \frac{13}{4096}>0.
}
\tag{23}
\]

This is a complete written proof.  It uses only planarity, self-duality at `p=1/2`, D4 symmetry, product-measure FKG, and a seven-edge finite-energy event.  The symbolic checker verifies the finite partition algebra but is not being substituted for the proof.

### B30 outcome

The previous middle-parameter gap now has a rigorous interior anchor: **the first monotonicity inequality is strictly true at the critical point with an explicit gap `13/4096`**.  More structurally, the entire first-step sign has been compressed to six punctured-star orbit masses, and at criticality FKG plus duality closes their only dangerous direction.

This still does not move `M_axis`, because that frozen metric requires the first inequality simultaneously for every `p in (0,1)`.

---

## B21 — import the finite-state layered-graph method, but target the first step rather than eventual monotonicity

König--Richthammer's layered-graph method encodes percolation on `G x Z`, for finite transverse `G`, by a finite Markov chain of infection/connectivity patterns built layer by layer.  Applied to the nested free strips

\[
S_W=P_{2W+1}\times\mathbb Z,
\]

with source and target on the central transverse vertex, the same construction gives a finite state space `M_W`, a transition matrix `K_W(p)`, an initial row vector `a_W(p)`, and a terminal indicator `h_W` such that, after the standard augmentation that records whether the current layer remains source-connected,

\[
\tau_n^{(W)}(p)=a_W(p)K_W(p)^n h_W.
\tag{24}
\]

Consequently the first-step inequality on the width-`W` strip is the exact finite-state sign

\[
\boxed{
\tau_1^{(W)}-\tau_2^{(W)}
=a_WK_W(I-K_W)h_W\ge0.
}
\tag{25}
\]

For each fixed `W`, every matrix entry is a finite polynomial in `p` and `1-p`; thus (25) is in principle an exact algebraic certificate problem rather than an infinite-volume connectivity problem.

The strips `S_W` are nested subgraphs of `Z^2`.  For each fixed terminal separation and fixed `p`, their connection probabilities increase to the full-plane probability.  Hence, if one could prove (25) for every width `W` and every `p`, then taking `W->infinity` would prove `tau_1>=tau_2` in the plane.

This explains exactly what the existing layered-graph theorem does and does not provide.  König--Richthammer prove eventual monotonicity for every **fixed finite** transverse graph, with an onset `N(G)` obtained from finite-state/quasi-stationary analysis.  Their result supplies no `N=1` theorem and no width-uniform onset that survives `W->infinity`.  Therefore simply citing eventual layered monotonicity does not address G0008.  The useful imported object is instead the finite matrix sign (25).

A sharper next finite-state goal suggested by B30 is to quotient the strip pattern chain by the four-neighbour puncture orbits `sigma,alpha,beta,gamma,delta,epsilon`, and seek an invariant cone forcing the signed functional in (8) nonnegative.  The critical proof above shows what such a cone looks like at `p=1/2`: normalization + the dual relation + FKG constrain the dangerous opposite-pair direction strongly enough to force positivity.

### B21 outcome

The imported layered method becomes a concrete finite certificate program rather than a vague analogy: prove `a_W K_W(I-K_W)h_W>=0` for all `W,p`, or find the smallest `(W,p)` where it fails.  No such all-width certificate is claimed in this run.

---

## Exact finite check

The 14-partition orbit calculation, formula (8), critical coefficients, relation (12), elimination formulas (16)--(20), and final polynomial factorization were executed symbolically with exact rational arithmetic.

Checker:

`research7_2026-09-17/R7-06/artifacts/2026-09-18/2026-09-18T040600Z__G0008_punctured_orbit_checker.py`

Archived output:

`research7_2026-09-17/R7-06/artifacts/2026-09-18/2026-09-18T040600Z__G0008_punctured_orbit_checker.out`

Terminal line: `ALL_EXACT_CHECKS_PASS`.

## What remains open

1. `M_axis` remains `UNKNOWN/UNMEASURED`: equation (23) is only `p=1/2`, whereas `M_axis>=1` requires all `p`.
2. The current self-contained parameter coverage for `n=1` is: the previous explicit low-density interval, the single critical point proved here, and the previous explicit high-density interval.  The two large middle subintervals remain unresolved.
3. The punctured-star formula (8) is exact for all `p`, but away from self-duality relation (12) is replaced by a detour statistic that is not explicitly known.  An abstract orbit relaxation permits negative brackets, so more percolative structure is genuinely required.
4. The finite-strip transfer representation (25) is a route, not a uniform proof.  The missing ingredient is a width-uniform invariant cone or another sign-preserving comparison that survives `W->infinity`.
5. The source asks all `n` (and discusses `Z^d` more broadly); even a future `M_axis=1` result remains only a first milestone.

## Next nonrepeating methods

Do not repeat B11/B30/B21 immediately.  If the next run is ordinary research, useful candidates are:

- **B5:** introduce a parameter interpolating the four central star-edge probabilities and differentiate the six-orbit bracket, looking for a monotone route away from `p=1/2`;
- **B25:** double-count pivotal configurations for `tau_1-tau_2` and seek an injection from the adverse opposite-pair orbit to one of the positive puncture orbits;
- **B6:** deform from the now-solved `p=1/2` point and identify the first exact derivative/continuation obstruction.

The fixed metric remains unchanged, so G0008 ordinary stagnation count advances from 1 to 2, not to zero.
