Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.

# NM13-11 / T09 — weakened triangle-fibre criterion and new S-arithmetic higher-rank Cayley class

Status: **PARTIAL / CANDIDATE_FULL for the restricted theorem below; full T09 remains OPEN.** The percolation argument below is complete as written, with exact arithmetic for its finite core. The external group-theoretic inputs are cited and were checked in this run; the candidate still awaits later independent review.

## 1. Original problem: before/after scope and gap

The frozen parent is the Benjamini–Schramm Cayley-graph conjecture for iid bond percolation:

> For every locally finite Cayley graph `G` of every finitely generated nonamenable group, prove `p_c(G)<p_u(G)`.

**Before this run.** The universal parent was OPEN. NM13-11 had a complete restricted candidate for specially constructed degree-9 Cayley graphs of `SL_n(Z)`, `n>=5`, with

\[
 p_c<\frac{19}{125}<\frac4{25}<p_u,
 \qquad p_u-p_c>\frac1{125}=0.008.
\]

That theorem assumed a `(2,3)` generating pair `Gamma=<s,t>` with `s^2=t^3=1`, plus a ping-pong partner `g` for `<t>`.

**After this run.** The universal parent remains OPEN, but both the theorem hypothesis and the certified gap improve.

> **Theorem A (one-involution extension of a `C_3*Z` core).** Let `Gamma` contain
> \[
> H=\langle t,g\rangle\cong C_3*\mathbb Z,\qquad t^3=1,
> \]
> and let `s` be an involution such that
> \[
> \Gamma=\langle H,s\rangle.
> \]
> Define `a_j=t^jgt^{-j}` for `j=0,1,2` and
> \[
> S=\{a_0^{\pm1},a_1^{\pm1},a_2^{\pm1},t,t^{-1},s\}.
> \]
> Then `G=Cay(Gamma,S)` is a simple 9-regular Cayley graph and
> \[
> \boxed{p_c(G)<\frac{473}{3125}=0.15136}
> \]
> while
> \[
> \boxed{p_u(G)>\frac{16189}{100000}=0.16189}.
> \]
> Consequently
> \[
> \boxed{p_u(G)-p_c(G)>\frac{1053}{100000}=0.01053.}
> \]

The hypothesis `Gamma=<H,s>` is strictly weaker than the predecessor's `Gamma=<s,t>`: the ping-pong partner `g` is now allowed to be needed to generate the ambient group.

The theorem gives a genuinely new uncovered arithmetic class:

> **Corollary B.** For every prime `ell` and every `n>=40`, the S-arithmetic group
> \[
> \Gamma_{n,\ell}=SL_n(\mathbb Z[1/\ell])
> \]
> has a simple degree-9 Cayley graph satisfying
> \[
> p_u-p_c>1053/100000.
> \]

These groups were not in NM13-11's preceding `SL_n(Z)` scope. They are not Gromov-hyperbolic (they contain `Z^2`), and the higher-rank hyperbolic-action theorem also places these S-arithmetic lattices outside the acylindrically-hyperbolic all-Cayley scope. Thus this is not a relabeling of the already-covered hyperbolic or acylindrically-hyperbolic families.

## 2. Compact handoff: what was preserved and what changed

The controlling policy is `operations/PROGRESS20_2026-09-20.md`; LIVE20 assigns NM11 to T09 under `proofnet24/NM13-11/progress-percolation/`. I read the latest own substantive report and the essential June Benjamini–Schramm history, rather than restarting the repository.

Preserved failed/conditional routes include normalized finite-set escape, BK boundary/finite-volume dichotomies, killed-SAW growth, boundary-energy bounds, global `l^2` SAW estimates, scalar nonbacktracking criteria, quotient/fibre-shell conditions, bridge criteria, and tree/product stress tests. Several never obtained the needed percolation transfer. Product examples later overlapped known product theorems and are not counted as new qualitative classes.

The immediate NM13-11 line is preserved:

1. free-subgroup/nonbacktracking gap on one degree-34 `SL_3(Z)` Cayley graph;
2. a general free-core/complement criterion and degree-14 family;
3. rank-4 plus three-complement degree-11 graphs;
4. triangle-fibre `C_3*Z` construction giving degree-9 graphs on `SL_n(Z)`, `n>=5`, with gap `>1/125`.

This run does not revisit those proofs. It sharpens the exact fibre and nonbacktracking constants, weakens the ambient generation hypothesis, and transfers the construction to a new S-arithmetic higher-rank family.

## 3. Algebraic core and the weakened structural hypothesis

Let

\[
 H=\langle t,g\rangle\cong C_3*\mathbb Z.
\]

Map `H -> C_3` by `t -> t` and `g -> 1`. Reidemeister–Schreier with transversal `1,t,t^2` gives the kernel

\[
 K=\langle a_0,a_1,a_2\rangle\cong F_3,
 \qquad a_j=t^jgt^{-j}.
\]

Conjugation by `t` cyclically permutes this free basis, so

\[
 H=K\rtimes C_3.
\]

With

\[
 A=\{a_0^{\pm1},a_1^{\pm1},a_2^{\pm1},t,t^{-1}\},
\]

the Cayley graph `Cay(H,A)` is exactly

\[
 T_6\square C_3.
\tag{3.1}
\]

Indeed every element of `H` is uniquely `k t^r`, `r=0,1,2`; right multiplication by `t^{\pm1}` moves in the cycle coordinate, while right multiplication by a free-basis generator remains in a fixed `r`-layer after cyclic relabelling of the basis.

Now assume only `Gamma=<H,s>` with `s^2=1`. Since `C_3*Z` has no element of order 2 (every finite-order element is conjugate into the `C_3` factor), `s` is not in `H`. Therefore

\[
 S=A\cup\{s\}
\]

contains nine distinct nonidentity elements and generates `Gamma`, proving that `Cay(Gamma,S)` is simple and 9-regular. No assumption that `s,t` alone generate `Gamma` is used below.

## 4. Sharpened exact `p_c` bound on the triangle fibre

By (3.1), the ambient graph contains a copy of `T_6 square C_3`, so it suffices to upper-bound the latter's bond threshold.

Root the `T_6` factor. Each nonroot tree vertex has five forward child fibres. After exposing internal edges of a triangle fibre, let its type `k in {1,2,3}` be the number of triangle vertices connected to the parent side.

For a fixed forward child and a type-`k` parent, the number of horizontal seeds is `j~Bin(k,p)`. If `C_{j,l}` is the probability that `j` prescribed seeds generate exactly `l` vertices after internal triangle percolation, then

\[
 C_{1,1}=(1-p)^2,
 \quad C_{1,2}=2p(1-p)^2,
 \quad C_{1,3}=3p^2-2p^3,
\]
\[
 C_{2,2}=(1-p)^2,
 \quad C_{2,3}=2p-p^2,
 \quad C_{3,3}=1.
\]

Thus

\[
 P_{k\ell}(p)=
 \sum_{j=1}^k {k\choose j}p^j(1-p)^{k-j}C_{j,\ell}(p),
\qquad
 M(p)=5P(p).
\tag{4.1}
\]

Different forward child fibres use disjoint horizontal and internal edges, and the base is a tree, so this is an exact three-type Galton–Watson exploration.

Take

\[
 p_0=\frac{473}{3125}=0.15136,
 \qquad
 v=(10000000,19495060,28521640)^T.
\]

The executed exact checker gives

\[
 (M(p_0)v-v)_1
 =\frac{3102085989781288}{3814697265625}>0,
\]
\[
 (M(p_0)v-v)_2
 =\frac{18894712975083214052}{11920928955078125}>0,
\]
\[
 (M(p_0)v-v)_3
 =\frac{86395467784932374973856}{37252902984619140625}>0.
\tag{4.2}
\]

Since `M(p_0)` is positive, Collatz–Wielandt yields `rho(M(p_0))>1`. The multitype Galton–Watson process therefore survives with positive probability and produces an infinite open cluster in `T_6 square C_3`. Because every entry of `M(p)` is polynomial in `p` and the inequalities (4.2) are strict, the same componentwise inequalities persist for all `p<p_0` sufficiently close to `p_0`. Hence

\[
 \boxed{p_c(T_6\square C_3)<473/3125}
\]

and therefore

\[
 \boxed{p_c(G)<473/3125}.
\tag{4.3}
\]

This improves the predecessor's certified `19/125=0.152` without changing the source model.

## 5. Sharpened degree-9 nonbacktracking `p_u` floor

Write the ambient adjacency operator as

\[
 A_G=A_K+(R_t+R_{t^{-1}})+R_s.
\]

The six `K`-generators act on left cosets of `K` as the 6-regular tree, so

\[
 \|A_K\|=2\sqrt5.
\]

The order-three pair has operator norm at most `2`, and the involution has norm `1`. Thus

\[
 \|A_G\|\le a:=2\sqrt5+3.
\tag{5.1}
\]

For a simple `D`-regular graph let `N_m` be the endpoint kernel for length-`m` nonbacktracking walks. Then

\[
 N_m=A_GN_{m-1}-(D-1)N_{m-2}
\]

for `m>=3`. Spectral calculus gives exponential `l^2` growth at most the larger root `beta_D(a)` of

\[
 z^2-az+(D-1)=0
\]

when `a>2sqrt(D-1)`. Every open connection has a self-avoiding, hence nonbacktracking, witness, so entrywise

\[
 T_p\le\sum_{m\ge0}p^mN_m.
\]

Consequently `T_p` is `l^2`-bounded for `p beta_D(a)<1`, which gives

\[
 p_{2\to2}(G)\ge \beta_D(a)^{-1}.
\tag{5.2}
\]

If `p>p_u`, uniqueness plus FKG gives `T_p(x,y)>=theta(p)^2>0`, impossible for a bounded operator on `l^2` of an infinite Cayley graph. Hence

\[
 p_{2\to2}(G)\le p_u(G).
\tag{5.3}
\]

Here `D=9`. Use the exact rational upper bound

\[
 \sqrt5<\frac{559017}{250000}=2.236068,
\]

whose squared slack is

\[
 \left(\frac{559017}{250000}\right)^2-5
 =\frac{6289}{62500000000}>0.
\]

Set

\[
 z_0=\frac{100000}{16189}.
\]

The checker gives `z_0^2>8` and exactly

\[
 z_0+\frac8{z_0}
 -\left(3+2\frac{559017}{250000}\right)
 =\frac{35997}{2023625000}>0.
\tag{5.4}
\]

The function `z+8/z` is strictly increasing for `z>sqrt8`. Since the larger characteristic root satisfies `beta_9(a)>sqrt8` and `beta_9(a)+8/beta_9(a)=a`, (5.1) and (5.4) imply

\[
 \beta_9(a)<z_0.
\]

Combining with (5.2)-(5.3),

\[
 \boxed{p_u(G)>\frac{16189}{100000}=0.16189}.
\tag{5.5}
\]

Subtracting (4.3) gives the exact source-level certificate

\[
 \boxed{
 p_u(G)-p_c(G)
 >\frac{16189}{100000}-\frac{473}{3125}
 =\frac{1053}{100000}=0.01053.
 }
\tag{5.6}
\]

## 6. New application: `SL_n(Z[1/ell])`, every prime `ell`, `n>=40`

Fix a prime `ell` and write

\[
 R=\mathbb Z[1/\ell].
\]

### 6.1 `R` is Euclidean, self-contained check

Every nonzero `x in R` has a unique form `u m`, where `u=+-ell^k` is a unit and `m` is a positive integer coprime to `ell`. Define `nu(x)=m`.

Given `a,b in R`, `b!=0`, multiply both by a unit so that `b=n` is a positive integer coprime to `ell`; write `a=m/ell^k`. Choose `c in Z` nearest to `m/n` and put `q=c/ell^k`. Then

\[
 r=a-bq=\frac{m-nc}{\ell^k}.
\]

If `r!=0`, removing any `ell`-power from its numerator can only reduce absolute value, so

\[
 \nu(r)\le |m-nc|\le n/2<n=\nu(b).
\]

Thus `R` is Euclidean.

### 6.2 `(2,3)` generation at `n>=40`

Tamburini–Wilson–Gavioli, *On the (2,3)-generation of some classical groups* (J. Algebra 168 (1994), DOI `10.1006/jabr.1994.1234`) prove: if a finitely generated commutative ring is generated by `d` elements `t_1,...,t_d` with `t_1` a finite-order unit, then `E_n(R)` is `(2,3)`-generated for `n>=12d+16`; for Euclidean domains `E_n(R)=SL_n(R)`.

For `R=Z[1/ell]` use the two ring generators

\[
 t_1=1,\qquad t_2=1/\ell.
\]

Hence `d=2` and

\[
 n\ge12\cdot2+16=40
\]

implies

\[
 SL_n(R)=\langle s,t\rangle,
 \qquad s^2=t^3=1.
\tag{6.1}
\]

### 6.3 Produce the `C_3*Z` partner inside the same group

The group `SL_n(R)` contains `SL_n(Z)` and is therefore Zariski-dense in the split real algebraic group `SL_n`. The finite subgroup `<t>cong C_3` intersects the real center trivially, because the center of `SL_n(R)` has no element of order 3.

Janssens–Temmerman–Thilmany, arXiv:2510.23957v1, Theorem 3.23, proves abundance of ping-pong partners in a Zariski-dense subgroup of a product of inner real forms of `SL_n`/`GL_n` whenever the finite subgroup embeds in an adjoint simple factor. Applied here, it supplies an infinite-order

\[
 g\in SL_n(R)
\]

such that

\[
 \langle t,g\rangle\cong C_3*\mathbb Z.
\tag{6.2}
\]

Now (6.1) implies `Gamma=<s,t>`, hence certainly `Gamma=<H,s>` for `H=<t,g>`. Theorem A applies and proves Corollary B.

### 6.4 Why this is genuinely outside the major already-covered classes

The group contains commuting infinite-order elementary matrices, for example `I+E_{12}` and `I+E_{13}`, so it contains `Z^2`; consequently it is not Gromov-hyperbolic and is outside Hutchcroft's arXiv:1804.10191 theorem.

Moreover `SL_n(Z[1/ell])` is the standard irreducible S-arithmetic lattice in

\[
 SL_n(\mathbb R)\times SL_n(\mathbb Q_\ell),
\]

whose two simple factors both have rank `n-1>=2`. Bader–Caprace–Furman–Sisto, arXiv:2206.06431 / ETDS, show that non-elementary hyperbolic actions of higher-rank lattices come from rank-one factors. There is no rank-one factor here, so this family is not acylindrically hyperbolic. Therefore the later Choi–Seo theorem arXiv:2508.08932, which proves `p_c<p_u` for every Cayley graph of every acylindrically hyperbolic group, does not absorb Corollary B.

A bounded current search for `SL_n(Z[1/p])` / S-arithmetic percolation did not locate a source already proving this exact degree-9 fixed-graph certificate. This is only bounded negative novelty evidence, not a worldwide priority claim.

## 7. Exact current scopes requested in the directive

Fresh checks on 20 September 2026 give:

1. **Hutchcroft, arXiv:1804.10191v3**, last revised **26 March 2019**. Theorem 1.3 proves `p_c<p_u` for connected, locally finite, nonamenable, **Gromov-hyperbolic quasi-transitive** graphs. It does not cover the higher-rank S-arithmetic groups above.
2. **Hutchcroft–Pan, arXiv:2409.12283v1**, submitted **18 September 2024**. It proves **nonuniqueness at `p_u`** for groups containing an amenable `wq`-normal subgroup of exponential growth, together with a co-heredity theorem for a strong endpoint property. Its subject is behavior at the uniqueness threshold, not a general quantitative fixed-Cayley `p_c<p_u` bound of the form proved here.
3. **Terlov–Timar, arXiv:2502.02560v2**, revised **14 September 2025**. It proves weighted/level-amenability characterizations and a relaxed Pak–Smirnova-Nagnibeda-style version of a `p_h<p_u` conjecture in the weighted/nonunimodular framework. It is not the ordinary unimodular fixed-Cayley `p_c<p_u` target.

The 2019 Hutchcroft introduction also records the older perturbative fact of Pak–Smirnova-Nagnibeda: every nonamenable finitely generated group has *some* Cayley graph with `p_c<p_u`. Therefore this report does **not** claim group-level existence as new in that broad sense. The new candidate contribution is the explicit structural degree-9 theorem, the sharpened uniform gap, and its concrete S-arithmetic realization.

## 8. Essential exact code/output and one correction

Load-bearing checker/output for this report:

- `proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T06-52-14+0300__t09-s-arithmetic-d2-check.py`
- `proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T06-52-14+0300__t09-s-arithmetic-d2-check.out`

The executed output ends `ALL_EXACT_CHECKS_PASS` and certifies the three strict `Mv>v` inequalities, the rational `sqrt(5)` bound, the nonbacktracking characteristic-root margin, the exact gap `1053/100000`, and the Tamburini ring-generator count `d=2`, threshold `40`.

An earlier exploratory checker written in this same invocation, `...__t09-s-arithmetic-triangle-check.py`, printed `12*1+16=28`. That arithmetic line is **not valid for `Z[1/ell]` under the Tamburini theorem's generator convention**, because the first listed ring generator must be a finite-order unit; one must use `1,1/ell`, hence `d=2`. I did not overwrite the exploratory artifact. It is superseded for the arithmetic application by the corrected `d2` checker above. Its percolation arithmetic coincides with the corrected checker, but its `n_threshold` line is not used in any theorem claim.

## 9. Remaining obstruction and next attack

The full T09 obstruction is unchanged: these are specially constructed generating sets, not arbitrary Cayley graphs of the same groups. The current mechanism still needs a visible `C_3*Z` fibre core and only tolerates one extra involution without a sharper ambient operator argument.

The next materially useful weakening is therefore not another decimal optimization. It is to replace the singleton involution complement by a larger fixed complement whose adjacency contribution is controlled **relative to the `T_6 square C_3` core**, rather than by the triangle inequality. A successful relative/colored operator bound that tolerates an inverse pair would move from `Gamma=<H,s>` to groups generated by `H` plus one arbitrary generator and would be a genuine step toward fixed natural Cayley sets.

## ledger_delta

```yaml
worker: NM13-11
target: T09
status: PARTIAL
candidate_label: CANDIDATE_FULL_RESTRICTED
parent_statement: pc(G) < pu(G) for every locally finite Cayley graph of every finitely generated nonamenable group
original_problem_before:
  universal_status: OPEN
  best_own_scope: specially constructed degree-9 Cayley graphs of SL_n(Z), n>=5
  certified_gap: "> 1/125 = 0.008"
original_problem_after:
  universal_status: OPEN
  abstract_scope: Gamma generated by H ~= C3*Z plus one involution
  new_group_family: SL_n(Z[1/ell]) for every prime ell, n>=40
  degree: 9
  pc_upper: "< 473/3125 = 0.15136"
  pu_lower: "> 16189/100000 = 0.16189"
  certified_gap: "> 1053/100000 = 0.01053"
mechanism_progress:
  - weakened ambient generation from Gamma=<s,t> to Gamma=<H,s>, H~=C3*Z
  - exact 3-type triangle-fibre Galton-Watson certificate at p=473/3125
  - sharpened degree-9 nonbacktracking root certificate to pu>16189/100000
  - Tamburini-Wilson-Gavioli + JTT transfer to S-arithmetic SL_n(Z[1/ell])
continuity:
  preserved_failed_routes: [finite-set-escape, killed-SAW, boundary-energy, SAW-l2, scalar-NB, quotient-fibre-shell, bridge, covered-products]
  unchanged_substantive_runs: 0
  failed_recoveries: 0
artifacts:
  checker: proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T06-52-14+0300__t09-s-arithmetic-d2-check.py
  output: proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T06-52-14+0300__t09-s-arithmetic-d2-check.out
residual_obstruction: arbitrary generating sets; need relative operator control for complements larger than one involution
next_attack: colored/relative nonbacktracking or adjacency estimate for H plus an inverse-pair complement
```

## References checked in this run

- T. Hutchcroft, *Percolation on hyperbolic graphs*, arXiv:1804.10191v3, 26 Mar 2019.
- T. Hutchcroft and M. Pan, *Percolation at the uniqueness threshold via subgroup relativization*, arXiv:2409.12283v1, 18 Sep 2024.
- G. Terlov and A. Timar, *Weighted-amenability and percolation*, arXiv:2502.02560v2, 14 Sep 2025.
- I. Choi and D. Seo, *Percolation in acylindrically hyperbolic groups*, arXiv:2508.08932.
- U. Bader, P.-E. Caprace, A. Furman, A. Sisto, *Hyperbolic actions of higher-rank lattices come from rank-one factors*, arXiv:2206.06431.
- M. C. Tamburini, J. S. Wilson, N. Gavioli, *On the (2,3)-generation of some classical groups*, J. Algebra 168 (1994), 353–370, DOI 10.1006/jabr.1994.1234.
- G. Janssens, D. Temmerman, F. Thilmany, *Simultaneous ping-pong for finite subgroups of reductive groups*, arXiv:2510.23957v1, Theorem 3.23.
