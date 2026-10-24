Model actually run: **GPT-5.6 Sol** (system model metadata). Reasoning-effort setting: **UNVERIFIED**.

# NM13-08 / T07 — commuting two-tail spider algebra and a new independent-terminal mixed-spider theorem

Status: **PARTIAL on the parent Grimmett–Winkler conjecture / CANDIDATE_FULL for the restricted theorem below, pending independent review.** Novelty/priority: **UNVERIFIED**. The arbitrary-finite-graph uniform-all-forests conjecture remains OPEN.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-08/progress-forest-structure/`  
Companion: NM13-04, `proofnet24/NM13-04/progress-forest/`

## 0. Compact handoff and substantive move

The preceding NM13-08 run proved a 15-state nilpotent tail for right stars `K_{1,m}` under three independent terminals and obtained an arbitrary-star-forest theorem. Its recorded next attack was branching depth two rather than another path/cycle component-size cutoff.

This run executes that attack. A right **mixed spider** has one center, `p` direct legs of length one, and `q` subdivided legs of length two. The direct-leg and subdivided-leg extension operators act on the same 15 frontier partitions. Exact partition DP shows that both are scalar-plus-nilpotent, that their nilpotent parts commute, and, more strongly, that they generate a seven-dimensional algebra with explicit cubic relations. This produces closed two-parameter marked transfers.

The sign application proves p-NC for three independent terminals joined to one arbitrary mixed spider plus an arbitrary number of isolated right vertices. In particular the once-subdivided stars with arbitrarily many arms are now covered; for three or more arms their right component is genuinely branching, not a path, cycle, or star.

The current LIVE20 mapping, `POSTED.md`, the latest own report, and the latest NM13-04 report were read. NM13-04 now has the complementary **triangle-seeded** arbitrary-star-forest theorem; the theorem below keeps an **independent** terminal triple and introduces branching depth two. No historical or peer artifact is overwritten. No email, Drive, public posting, paid compute, workflow execution, access/permission change, or schedule change is performed.

## 1. Parent theorem before/after, separately from mechanism gain

For a finite graph `G=(V,E)`, put

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\qquad
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is exactly pairwise negative correlation of the two edge indicators under the uniform law on **all** spanning forests.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-simple-graph order in repository continuity:** `9 -> 9`.  
**Source-valid lower bound on a counterexample order:** `>=10 -> >=10`.

No complete-order metric moves in this run.

**Mechanism before:** one nilpotent leaf operator for arbitrary right stars, plus finite path/cycle response-strip libraries.

**Mechanism after:** a **commuting two-operator branching algebra** for direct and subdivided spider legs, with an explicit seven-dimensional nilpotent quotient and an all-`p,q` marked sign theorem. This is a structural branching-depth gain, not another finite component-order extension.

## 2. Exact P14 / source scope recovered

Only essential dependencies were reread.

1. **Grimmett–Winkler, arXiv:math/0302185 / Random Structures & Algorithms 24 (2004).** Their conjecture is the unit-weight uniform law on **all forests**. They verified every graph with at most eight vertices and every nine-vertex graph with at most eighteen edges. They explicitly separate the already-known uniform-spanning-tree theorem.
2. **P14/HARD10 repository complement.** The exact dense-nine computation covers the complementary 19--36-edge sector. Repository continuity therefore covers all `274,668` unlabeled simple nine-vertex graphs; the dense sector contains `120,314` graphs and `25,304,635` exact present-edge-pair checks.
3. **Structural P14 reduction.** Block/direct-sum factorization reduces a vertex-minimal counterexample to 2-connected. P14's two-separator transfer, together with the fixed-graph unit-to-positive-weight implication recorded from Cocks/Semple--Welsh, reduces it further to a **3-connected** graph. This is a reduction, not closure of the conjecture.
4. **Erickson, arXiv:1008.3660.** Erickson proves the stronger all-positive-weight independent-set-Rayleigh / sum-of-squares theorem for **series-parallel** graphs. The class below contains `K_{3,3}` as soon as the right side has at least three vertices, so this theorem does not cover the branching members below.
5. **Later work.** Huang `arXiv:2311.00965` still presents general arboreal-gas negative correlation as open while proving restricted graph cases. Bado proves strict unit p-NC for wheel graphs (Statistics and Probability Letters 241, article 110960; DOI `10.1016/j.spl.2026.110960`). Tang--Zhang `arXiv:2603.10738`, submitted 11 March 2026, treats specified complete-graph ensembles including forests with exactly `k` components for fixed `k`; that is not the arbitrary-graph law mixing all forest component counts.

A bounded 20 September 2026 search did not locate the exact independent-terminal mixed-spider family below. That is negative evidence only; novelty/priority remains **UNVERIFIED**.

## 3. The mixed-spider class

Let `D_{p,q}` be the tree with center `c`,

- direct leaves `d_1,...,d_p` and edges `cd_i`, and
- subdivided legs `c-b_j-x_j`, `1<=j<=q`, with edges `cb_j,b_jx_j`.

Thus `D_{p,0}=K_{1,p}` and `D_{0,q}` is the once-subdivided `q`-arm star. By convention `D_{0,0}=K_1` (the center alone).

Let

\[
H_{p,q,r}=D_{p,q}\sqcup rK_1,
\qquad
G_{p,q,r}=\overline{K_3}\vee H_{p,q,r},
\qquad p,q,r\ge0.
\]

The three vertices of `bar(K3)` are **independent** terminals; each is joined to every vertex of `H_{p,q,r}`.

The basic size formulas are

\[
|V(G_{p,q,r})|=4+p+2q+r,
\]

and

\[
|E(G_{p,q,r})|=3(1+p+2q+r)+(p+2q)=3+4p+8q+3r.
\]

For `q>=3`, the right component `D_{0,q}` has a degree-`q` branch vertex and diameter four. It is not a path, cycle, or star.

## 4. Retained five-state terminal algebra

The three terminals have five connectivity states

\[
0|1|2,\quad0|12,\quad01|2,\quad02|1,\quad012.
\]

For one isolated right vertex adjacent to all terminals,

\[
S=4I+N,
\qquad N^3=0.
\]

Every terminal-symmetric unmarked atom considered here has transfer

\[
T=A I+B N+C N^2.
\]

After factoring `A>0`, write

\[
\widehat T=I+aN+cN^2,
\qquad
\rho(T)=\frac{a^2/2-c}{a}.
\]

For any product of normalized atoms,

\[
\prod_i(I+a_iN+c_iN^2)=I+uN+vN^2,
\]

and exact multiplication using `N^3=0` gives

\[
\frac{u^2}{2}-v=\sum_i \rho_i a_i.
\]

Hence, for `u>0`,

\[
v=\frac{u^2}{2}-hu,
\qquad
h=\frac{\sum_i\rho_i a_i}{\sum_i a_i}.
\]

This response-strip identity is retained from the preceding runs.

## 5. New decomposition lemma: a commuting two-tail branching algebra

Retain the frontier `(0,1,2,c)`, where `c` is the spider center. There are `B_4=15` partitions.

A **direct-leg step** introduces a fresh vertex `d`, considers the four edges

\[
cd,\ d0,\ d1,\ d2,
\]

rejects cyclic choices and forgets `d`. Let the resulting exact `15 x 15` operator be `L`.

A **subdivided-leg step** introduces fresh vertices `b,x`, considers the eight edges

\[
cb,\ b0,\ b1,\ b2,\ bx,\ x0,\ x1,\ x2,
\]

rejects cyclic choices and forgets `x,b`. Let the resulting operator be `B`.

### Lemma `T07-MIXED-SPIDER-TWO-TAIL-ALGEBRA-25`

Set

\[
J=L-5I,
\qquad
K=B-28I.
\]

Then exact partition DP gives

\[
J^4=K^4=0,
\]

with

\[
(\operatorname{rank}J,\operatorname{rank}J^2,\operatorname{rank}J^3,\operatorname{rank}J^4)
=(8,2,1,0),
\]

and the same rank tuple for `K`. Moreover

\[
\boxed{JK=KJ},
\]

and the mixed products satisfy

\[
\boxed{JK^2=\frac{31}{270}K^3},
\qquad
\boxed{J^2K=\frac{76}{6075}K^3},
\qquad
\boxed{J^3=\frac{8}{6075}K^3}.
\tag{5.1}
\]

The algebra generated by `J,K` has dimension exactly seven, with basis

\[
I,\ K,\ K^2,\ K^3,\ J,\ JK,\ J^2.
\]

### Proof

The checker constructs all 15 frontier partitions and all admissible edge subsets for each of the two local steps. Every displayed matrix identity is then checked over the integers/rationals, as are the ranks and the rank-seven span assertion. No floating-point sign decision is used.

Because `J^4=K^4=0`,

\[
5^{-p}L^p
=I+\frac p5J+\frac{\binom p2}{25}J^2+\frac{\binom p3}{125}J^3,
\]

and

\[
28^{-q}B^q
=I+\frac q{28}K+\frac{\binom q2}{28^2}K^2+\frac{\binom q3}{28^3}K^3.
\]

The commutation and relations (5.1) collapse their product into the seven-dimensional algebra. A marked edge pair distinguishes at most two direct/subdivided legs. By permuting equal-type legs, place those distinguished legs first; all remaining legs contribute the displayed powers. Therefore every unmarked, one-marked and two-marked mixed-spider transfer, after removal of the positive scalar `5^p 28^q`, is polynomial in `(p,q)` of bounded degree. This is the required all-parameter transfer, not finite interpolation in the graph size. QED.

## 6. Closed unmarked transfer and a common response strip

Let `T_{p,q}` be the unmarked three-terminal transfer of `D_{p,q}` after removal of `5^p28^q`. Exact multiplication gives

\[
\boxed{T_{p,q}=A_{p,q}I+B_{p,q}N+C_{p,q}N^2},
\]

where

\[
A_{p,q}=\frac{42p+45q+280}{70},
\tag{6.1}
\]

\[
B_{p,q}=\frac{1568p^2+4830pq+12152p+3375q^2+22875q+9800}{9800},
\tag{6.2}
\]

and

\[
C_{p,q}=\frac{1}{8232000}\Bigl(
175616p^3+893760p^2q+1393952p^2+1464750pq^2
\]

\[
\qquad\qquad +5403090pq+1174432p+759375q^3+5229375q^2+2341250q
\Bigr).
\tag{6.3}
\]

Put `a=B/A`, `c=C/A`. The response is

\[
\rho_{p,q}=\frac{a^2/2-c}{a}
\]

and simplifies to

\[
\rho_{p,q}=\frac{R(p,q)}{840(42p+45q+280)(1568p^2+4830pq+12152p+3375q^2+22875q+9800)},
\]

where

\[
\begin{aligned}
R(p,q)={}&6607552p^3+27462540p^2q+95579008p^2+36092700pq^2\\
&+287818860pq+385696640p+15271875q^3+198665625q^2\\
&+689500000q+288120000.
\end{aligned}
\]

Two exact factorizations give a size-independent interval:

\[
\boxed{
\rho_{p,q}-\frac{43}{360}
=
\frac{8820p^2q+96040p^2+18900pq^2+259959pq+902776p+10125q^3+171000q^2+785400q+3841600}
{252(42p+45q+280)(1568p^2+4830pq+12152p+3375q^2+22875q+9800)}>0,
}
\tag{6.4}
\]

and

\[
\boxed{
\frac18-\rho_{p,q}
=
\frac{153664p^3+623280p^2q+2055256p^2+806400pq^2+6240045pq+7395080p+337500q^3+4321875q^2+14665000q}
{420(42p+45q+280)(1568p^2+4830pq+12152p+3375q^2+22875q+9800)}\ge0.
}
\tag{6.5}
\]

Thus

\[
\boxed{\frac{43}{360}<\rho_{p,q}\le\frac18},
\]

with the upper equality only at `p=q=0`, when the atom is one isolated right vertex.

Consequently any unmarked product formed from this atom and isolated right vertices lies in the same continuous strip

\[
\boxed{u\ge0,\qquad v=\frac{u^2}{2}-hu,\qquad \frac{43}{360}\le h\le\frac18.}
\tag{6.6}
\]

## 7. New sign certificate

Fix a present pair `e,f`. After exposing every right component containing a marked edge, the remaining unmarked product is `U(u,v)=I+uN+vN^2`. Each of the four counts `I,I_e,I_f,I_ef` is affine in `(u,v)`, so the normalized Rayleigh numerator is an exact quadratic

\[
Q(u,v;p,q).
\]

Substitute (6.6):

\[
R(u,h)=Q\left(u,\frac{u^2}{2}-hu;p,q\right)=\sum_{j=0}^4 c_j(h;p,q)u^j.
\]

Each `c_j` is quadratic in `h`.

### 7.1 Both marked edges in the mixed spider

Terminal permutations, direct-leg permutations, subdivided-leg permutations, and interchange of `e,f` reduce all pairs to exactly

\[
\boxed{48\text{ symbolic orbit schemes}.}
\]

For each scheme, shift `p=p_0+x`, `q=q_0+y` to the minimum physical leg counts. For **41** schemes, every degree-two Bernstein coefficient of every `c_j` on `[43/360,1/8]` is a polynomial in `x,y` with nonnegative monomial coefficients.

Exactly **seven** schemes leave that cone. They are repaired by the retained strip-discriminant identity. If

\[
Q=q_{00}+q_{10}u+q_{01}v+q_{20}u^2+q_{11}uv+q_{02}v^2,
\]

then after the strip substitution

\[
4c_4c_2-c_3^2
=
q_{02}\left(q_{20}+\frac{q_{01}}2\right)-\frac{q_{11}^2}{4},
\tag{7.1}
\]

which is independent of `h`.

For the seven exceptions the exact invariant `K=4c_4c_2-c_3^2` is respectively:

\[
\frac{5625}{2314037239808}(1591716p^2+3422580pq+22140104p+2115450q^2+21735945q+83839430),
\]

\[
\frac{9}{470596000}(258132p^2+567840pq+3567368p+367200q^2+3511005q+13630965),
\]

\[
\frac{9}{578509309952}(27440196p^2+57947820pq+376315240p+30862350q^2+395067225q+1310290950),
\]

\[
\frac{9}{94119200}(54096p^2+118860pq+672196p+76275q^2+640650q+2818425),
\]

\[
\frac{27}{478515625}(112308p^2+254380pq+1535072p+173025q^2+1519840q+5908224),
\]

\[
\frac{27}{29412250000}(586236p^2+1237600pq+8080828p+660375q^2+8469400q+28364486),
\]

and

\[
\frac{27}{3615683187200}(5244372p^2+11197760pq+70443408p+5980950q^2+75168275q+237045650).
\]

Every coefficient shown is positive. In all seven cases the checker also verifies `c_4>0`, `c_0>0`, nonnegative Bernstein coefficients for `c_1`, and the exact identity (7.1). Therefore the quadratic core `c_4u^2+c_3u+c_2` has negative discriminant and is positive for every real `u`, so `R(u,h)>0` for all physical parameters.

Among all 48 same-spider schemes, the only zero constant term at a physical minimum is the pair of two center-to-terminal spokes with `p=q=0`. There the strip polynomial begins

\[
R(u,h)=4u+4(9h^2-12h+5)u^2-12(3h-2)u^3+9u^4,
\]

which is positive whenever an unmarked component remains.

### 7.2 One mixed-spider edge and one singleton edge

There are exactly **11** symbolic schemes. Every one is Bernstein-positive on the full strip after the physical `(p,q)` shift. Their constant terms at the physical minima are strictly positive.

### 7.3 Pairs using only singleton components

There are three schemes: two spokes in one singleton, and spokes in two distinct singletons with equal or unequal terminal labels. All three are Bernstein-positive on the same strip. The same-singleton scheme has zero constant term but begins with positive `4u`; in the present graph an unmarked mixed-spider atom remains whenever that scheme occurs, so `u>0`.

Thus the complete certificate consists of

\[
\boxed{55\text{ regular Bernstein schemes}+7\text{ discriminant schemes}=62\text{ schemes},\quad 0\text{ failures}.}
\]

The exact staged execution ends `ALL_EXACT_CHECKS_PASS`.

## 8. New all-parameter theorem

### Theorem `T07-INDEPENDENT-MIXED-SPIDER-PNC-25`

For every integers `p,q,r>=0`, let

\[
G_{p,q,r}=\overline{K_3}\vee(D_{p,q}\sqcup rK_1).
\]

Then for every two distinct present edges `e,f`,

\[
\boxed{\Delta_{G_{p,q,r}}(e,f)\ge0.}
\]

Equality occurs only for the degenerate graph

\[
G_{0,0,0}=K_{3,1},
\]

which is a tree. Every other physical edge pair is strict.

### Proof

Take a marked pair. If both edges lie in `D_{p,q}`, expose that component; the remaining `r` singleton atoms give an unmarked response lying in the strip (indeed at `h=1/8` when nonempty). Section 7.1 proves the corresponding normalized gap nonnegative, and strict except when `p=q=r=0` and the marked edges are two center spokes.

If exactly one marked edge lies in `D_{p,q}`, expose that component and the marked singleton. The remaining singletons again lie in the strip, and Section 7.2 gives strict positivity.

If both marked edges use singleton components, expose the required one or two singleton atoms. The unmarked product contains `D_{p,q}` plus any remaining singletons and lies in the strip by Section 6. Section 7.3 gives strict positivity. Restoring every removed factor `5^p28^q` and every positive unmarked identity coefficient multiplies the Rayleigh numerator by a positive factor, so the sign is unchanged. QED.

The case `G_{0,0,0}=K_{3,1}` has no cycles, so every edge subset is a forest and distinct edge indicators are independent; its Rayleigh differences are zero.

## 9. Genuine uncovered branching subfamily and exact check

The cleanest new tail is

\[
\boxed{G_q=\overline{K_3}\vee D_{0,q}},\qquad q\ge3,
\]

where `D_{0,q}` is the once-subdivided `q`-arm star. This right component has a genuine branching vertex of degree `q` and is neither a path nor a star.

The first member beyond the complete-nine baseline is `q=3`:

\[
|V(G_3)|=10,\qquad |E(G_3)|=27.
\]

Exact transfer evaluation gives

\[
I_{G_3}(\mathbf1)=2,298,452,
\]

and the minimum Rayleigh numerator over its physical pair orbits is

\[
\boxed{573,003,024},
\]

attained by internal second-leg edges on two distinct subdivided arms.

This family is complementary to NM13-04 in several independent senses.

- The three left terminals are independent; NM13-04's current theorem has a left `K_3` seed.
- For every nontrivial member here the clique number is at most three, whereas every nonempty `K_3\vee H` contains a `K_4`.
- Deleting the three seed-triangle edges from a merely unit-weight p-NC theorem is not a valid inheritance principle.
- For `q>=3`, the right induced component has branching depth two and is outside NM13-08's previous path/cycle library and its arbitrary-star-forest theorem.
- Since the right side has at least three vertices, the whole graph contains `K_{3,3}` and is not series-parallel.

The theorem is therefore a genuine new all-parameter branching class, not finite enumeration and not a corollary of a spanning-tree or fixed-component result.

## 10. Exact execution and sanity checks

The staged exact computation used only integer/rational arithmetic in the 15-state partition DP and SymPy polynomial algebra. It established:

- direct-leg and subdivided-leg scalar-plus-nilpotent operators;
- exact commutation and the three mixed algebra relations;
- seven-dimensional algebra rank;
- the closed `A_{p,q},B_{p,q},C_{p,q}` formulas;
- both response-strip factorizations;
- all 48 same-spider orbit response quadratics;
- `41` Bernstein certificates and `7` exact discriminant certificates;
- all `11` mixed-spider/singleton schemes;
- all `3` singleton-only schemes;
- exact `q=3` forest count and minimum Rayleigh numerator.

The archived monolithic checker is a reproducer of the same exact routines; the runtime computation was executed in stages to stay within single-call limits. The archived output records the actual staged results and ends `ALL_EXACT_CHECKS_PASS`.

Independent small-graph brute-force sanity checks were also run for `(p,q,r)=(1,1,0),(0,2,0),(2,0,1),(1,1,1)`, with respectively

- `Z=5776`, minimum gap `27300`;
- `Z=44340`, minimum gap `340560`;
- `Z=3986`, minimum gap `19884`;
- `Z=30720`, minimum gap `715536`.

These finite checks are sanity checks only; the proof is the symbolic transfer above.

## 11. Honest boundary and next attack

The parent conjecture is not closed. The new theorem allows **one** arbitrary mixed spider plus arbitrary singleton atoms. The same-spider marked sign theorem is already uniform over the whole star response strip, but a pair of marked edges lying in **two different mixed-spider components** would require a four-parameter cross-component certificate in `(p,q,p',q')`. A first exact attempt at that full cross certificate generated the required response polynomials but was too expensive for the single-process execution cap in this run, so it is **not claimed**.

This identifies the next substantive attack precisely: derive a cone/factorization for cross-component one-edge response vectors that proves their Rayleigh determinant nonnegative abstractly, avoiding four-parameter orbit expansion. If that succeeds, the present theorem should lift from one mixed spider to an **arbitrary forest of mixed spiders**, strictly extending both independent-terminal star forests and the current branching-depth-two class.

No theorem beyond the stated class is promoted.
