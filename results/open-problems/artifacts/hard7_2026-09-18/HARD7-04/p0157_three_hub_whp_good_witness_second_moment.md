# P0157 — three-hub components occur whp in the explicit barely-subcritical stress family

**Scope.** This is a self-contained HARD7-04 route theorem for the explicit finite-third-moment configuration-model family already introduced in `p0157_multihub_route_refutation.md` and used in `p0157_four_hub_exclusion_and_three_hub_witness.md`. It does **not** solve van der Hofstad's full barely-subcritical crossover problem. It upgrades the preceding exact first moment for three-hub V-witnesses to a high-probability statement. Combined with the already proved four-hub exclusion, it determines the maximal number of designated hubs in one component for this stress family: it is exactly three with high probability.

## 1. Family, notation, and prior input

Let `m` tend to infinity through even positive integers and put

\[
n=8m^{12},\qquad M=m^5,\qquad d=m^2,
\]

\[
x=3m^{11}+\frac{m^5}{4}(m^2-1)^2,
\]

\[
N_d=M,\qquad N_3=2m^{12}-x,\qquad N_1=6m^{12}+x-M.
\]

The `M` vertices of degree `d` are the designated **hubs**. The total half-edge count and subcriticality parameter satisfy

\[
\ell
=\frac{m^5}{2}\left(24m^7-12m^6-m^4+4m^2-3\right)
\sim12m^{12},
\]

\[
\delta
=1-\frac{\sum_vd_v(d_v-1)}\ell
=\frac{12m^{11}}\ell
\sim m^{-1}.
\]

Write

\[
D_k:=(\ell-1)(\ell-3)\cdots(\ell-(2k-1)).
\]

For distinct ordered hubs `(a,b,c)` and integers `m<=r,s<=2m`, a **V-witness** is a pair of internally vertex-disjoint simple paths, one of length `r` from `a` to `b` and one of length `s` from `a` to `c`, whose internal vertices are all distinct degree-three vertices. The half-edge embedding is part of the witness. Let `Z_m` be the total number of ordered V-witnesses.

The preceding HARD7-04 theorem proved exactly

\[
\mathbb EZ_m
=(M)_3d^3(d-1)
\sum_{r=m}^{2m}\sum_{s=m}^{2m}
\frac{(N_3)_{r+s-2}6^{r+s-2}}{D_{r+s}},
\tag{1.1}
\]

and

\[
\mathbb EZ_m\sim c_*m,
\qquad
c_*:=\frac{(e^{-1}-e^{-2})^2}{144}>0.
\tag{1.2}
\]

It also proved

\[
\mathbb P\{\text{some component contains at least four hubs}\}=O(m^{-1}).
\tag{1.3}
\]

The missing implication was that the diverging first moment in (1.2) is not carried by rare highly dependent configurations.

## 2. Main theorem

### Theorem 2.1 — exact three-hub boundary in the stress family

Let `H_max` be the maximum number of designated hubs contained in a connected component of the configuration model above. Then

\[
\boxed{\mathbb P(H_{\max}=3)\longrightarrow1.}
\tag{2.1}
\]

More precisely, with high probability there exists an acyclic component containing exactly three hubs whose minimal three-hub subtree is a V with both arm lengths in `[m,2m]`.

The proof has two ingredients. First, conditioning on one witness, the probability that its host component either acquires a fourth hub or a cycle is `O(m^{-2})`. Second, ordered pairs of vertex-disjoint witness skeletons have factorial moment asymptotic to `(E Z_m)^2`. On the resulting good event, each host component contributes exactly two ordered witnesses, so the second moment closes without a full overlap taxonomy.

## 3. Conditional cleanup: almost every witness lives in a three-hub tree

Let `w` be any fixed V-witness skeleton with arm lengths `r,s in [m,2m]`, and write

\[
R=r+s\in[2m,4m].
\]

Condition on all `R` prescribed matching pairs of `w` being present. The remaining matching is uniform on the remaining `ell-2R` half-edges.

The skeleton uses two hub half-edges at its center, one at each leaf hub, and two half-edges at each of its `R-2` internal degree-three vertices. Therefore the number of still-unpaired half-edges incident to the skeleton is

\[
A_0=(3d-4)+(R-2)=3d+R-6\le4m^2
\tag{3.1}
\]

for all sufficiently large `m`.

Explore the rest of the host component from these `A_0` active half-edges. Let `A_t` be the active queue after `t` additional pairings and `tau` its extinction time. Set

\[
T=\left\lfloor\frac{\ell\delta}{64}\right\rfloor.
\tag{3.2}
\]

The full degree sequence obeys

\[
\sum_v d_v(d_v-2)=-\ell\delta.
\tag{3.3}
\]

Conditioning on the skeleton removes three degree-`d` vertices and `R-2` degree-three vertices from the unseen set; all of these have nonnegative `d_v(d_v-2)`, so this only makes the unseen drift numerator more negative. Each subsequently discovered ordinary vertex can increase that numerator by at most one, because `d_v(d_v-2)>=-1` for integer degrees. Hence, for `t<=T` and before extinction,

\[
\mathbb E[A_{t+1}-A_t\mid\mathcal F_t]\le-\frac\delta2
\tag{3.4}
\]

for all sufficiently large `m`. Exactly as in the standard active-half-edge calculation,

\[
\mathbb E(\tau\wedge T)\le\frac{2A_0}{\delta}=O(m^3),
\tag{3.5}
\]

and therefore

\[
\mathbb P(\tau>T)\le\frac{2A_0}{\delta T}
=O(m^{-8}).
\tag{3.6}
\]

### 3.1 Hitting a fourth hub

Until a fourth hub is hit, at most `Md=m^7` half-edges belong to as-yet-unseen extra hubs. For `t<=T`, the residual denominator is at least `ell/2`, so the conditional hazard of discovering an extra hub at one pairing is at most

\[
\frac{2Md}{\ell}=O(m^{-5}).
\]

Combining this with (3.5), and adding the long-exploration probability (3.6), gives uniformly in the witness `w`

\[
\mathbb P\{\text{host component of }w\text{ contains a fourth hub}\mid w\}
=O(m^{-2}).
\tag{3.7}
\]

### 3.2 Creating a cycle

The family has bounded normalized third moment:

\[
\sum_vd_v^3=O(m^{12})=O(\ell).
\]

Thus there is an absolute constant `B` such that, throughout the truncated exploration,

\[
\mathbb E[(A_{t+1}-A_t)^2\mid\mathcal F_t]\le B.
\tag{3.8}
\]

From (3.4) and (3.8),

\[
\delta\,
\mathbb E\!\left[\sum_{t<\tau\wedge T}A_t\right]
\le A_0^2+B\mathbb E(\tau\wedge T)
=O(m^4),
\]

so

\[
\mathbb E\!\left[\sum_{t<\tau\wedge T}A_t\right]=O(m^5).
\tag{3.9}
\]

At a truncated pairing step, the probability that the partner half-edge is already active is at most `2A_t/ell`. Hence (3.9) and (3.6) imply

\[
\mathbb P\{\text{host component of }w\text{ contains a cycle}\mid w\}
=O(m^{-7}).
\tag{3.10}
\]

Define a witness to be **good** when its host component is acyclic and contains no hub other than its three witness hubs. Let `Z_m^g` count good ordered witnesses. By (3.7)--(3.10), uniformly over all witness skeletons,

\[
\mathbb P(w\text{ is not good}\mid w\text{ occurs})=O(m^{-2}).
\tag{3.11}
\]

Summing (3.11) with the same weights as in (1.1),

\[
\mathbb E(Z_m-Z_m^g)=O(m^{-2})\mathbb EZ_m=O(m^{-1}),
\tag{3.12}
\]

and therefore

\[
\boxed{\mathbb EZ_m^g=(1+o(1))\mathbb EZ_m\sim c_*m.}
\tag{3.13}
\]

This already rules out the most dangerous negation: the linear first moment is not concentrated on the rare four-hub or cyclic configurations.

## 4. Count the same object twice: disjoint witness pairs

Let `D_m^0` count ordered pairs of V-witness skeletons whose six hubs are all distinct and whose internal degree-three vertices are all distinct. No condition is imposed on whether the two skeletons later become connected by extra edges. Direct pairing enumeration gives

\[
\mathbb ED_m^0
=(M)_6d^6(d-1)^2
\sum_{r,s,u,v=m}^{2m}
\frac{(N_3)_{r+s+u+v-4}6^{r+s+u+v-4}}
{D_{r+s+u+v}}.
\tag{4.1}
\]

For a fixed quadruple `(r,s,u,v)`, put `R=r+s` and `R'=u+v`. The ratio of the corresponding summand in (4.1) to the product of the two corresponding first-moment summands in (1.1) is

\[
\frac{(M)_6}{(M)_3^2}
\frac{(N_3)_{R+R'-4}}{(N_3)_{R-2}(N_3)_{R'-2}}
\frac{D_RD_{R'}}{D_{R+R'}}.
\tag{4.2}
\]

Uniformly for `2m<=R,R'<=4m`,

\[
\frac{(M)_6}{(M)_3^2}=1+O(M^{-1})=1+O(m^{-5}),
\tag{4.3}
\]

\[
\frac{(N_3)_{R+R'-4}}{(N_3)_{R-2}(N_3)_{R'-2}}
=1+O\!\left(\frac{m^2}{N_3}\right)
=1+O(m^{-10}),
\tag{4.4}
\]

and

\[
\frac{D_RD_{R'}}{D_{R+R'}}
=1+O\!\left(\frac{m^2}{\ell}\right)
=1+O(m^{-10}).
\tag{4.5}
\]

All summands are positive, so the uniform comparison yields

\[
\boxed{\mathbb ED_m^0=(1+O(m^{-5}))(\mathbb EZ_m)^2.}
\tag{4.6}
\]

This is the useful factorial-moment statement: finite-population depletion and matching-without-replacement dependence are both much smaller than the hub-label exclusion correction.

## 5. The tree identity that eliminates all same-component overlap classes

A good witness lies in a tree component with exactly three hubs. In a tree there is a unique simple path between any pair of vertices. For a V-witness centered at hub `a`, the two witness arms to hubs `b,c` therefore determine the unique minimal three-hub subtree. The only other ordered V-witness in that same component is obtained by swapping the leaf order `(b,c)` to `(c,b)`.

Indeed, neither leaf hub can become the center of another V-witness: the two paths from that leaf to the other two hubs would share the path segment leading back to `a`, hence would not be internally vertex-disjoint. Extra non-hub branches do not create alternate paths because the component is acyclic.

Consequently **every good host component contributes either zero or exactly two ordered good witnesses**.

Let `D_m^g` count ordered pairs of good witnesses lying in distinct connected components. Then pointwise

\[
(Z_m^g)^2=2Z_m^g+D_m^g.
\tag{5.1}
\]

Witnesses in distinct components have vertex-disjoint skeletons, hence

\[
D_m^g\le D_m^0.
\tag{5.2}
\]

Taking expectations and applying (4.6) and (3.13),

\[
\mathbb E[(Z_m^g)^2]
\le2\mathbb EZ_m^g+(1+o(1))(\mathbb EZ_m)^2
=(1+o(1))(\mathbb EZ_m^g)^2,
\tag{5.3}
\]

because `E Z_m^g ~ c_* m -> infinity`.

The second-moment inequality now gives

\[
\mathbb P(Z_m^g>0)
\ge
\frac{(\mathbb EZ_m^g)^2}{\mathbb E[(Z_m^g)^2]}
\longrightarrow1.
\tag{5.4}
\]

Thus with high probability there exists a tree component containing exactly three hubs.

Combining (5.4) with the previously proved four-hub exclusion (1.3) proves Theorem 2.1. `QED`

## 6. What this changes in the P0157 route

The preceding rank-one heuristic predicted the hierarchy

\[
M^kp_m^{k-1}\asymp m^{7-2k},
\]

so that two-hub contacts are abundant, three-hub trees still occur, and four-hub trees disappear. The present theorem makes the `k=3/k=4` boundary rigorous in the **actual configuration model** for the explicit stress family:

\[
\boxed{H_{\max}\xrightarrow{\mathbb P}3.}
\]

This is stronger than the previous first-moment checkpoint and shows that the global upper-tail interaction structure is real rather than an artifact of an independent rank-one surrogate.

It still does not determine the largest-component size for every finite-third-moment degree sequence, nor identify the full transition between `d_max/delta` and `delta^{-2} log(n delta^3)`. The source problem remains OPEN. The frozen HARD7-04 metric `Q_m=m^{-1}+O(m^{-2})->0` is unchanged by this theorem.

## 7. Prior-art and verification status

A bounded literature refresh on 2026-09-19 rechecked van der Hofstad's 4 August 2026 monograph and Coulson--Perarnau, *Largest component of subcritical random graphs with given degree sequence* (EJP 28 (2023), arXiv:2111.11780). The current monograph still presents the finite-third-moment subcritical crossover as an open phase-transition question. The search also checked 2025--2026 adjacent subcritical growing/inhomogeneous random-graph work; no located source was found stating this exact three-hub stress-family theorem. This is **not** a novelty certificate.

No finite exhaustive assertion is introduced here, so no checker-only artifact is manufactured. The proof is an asymptotic theorem written on the page. It depends on the preceding HARD7-04 four-hub exclusion and exact first-moment formula, both already archived with their own verification status. This note is a **self-check / PARTIAL route result**, not an independent audit and not source closure.