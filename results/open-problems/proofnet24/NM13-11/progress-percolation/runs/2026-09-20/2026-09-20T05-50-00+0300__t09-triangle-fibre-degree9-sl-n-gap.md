Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.

# NM13-11 / T09 — triangle-fibre subgroup transfer gives degree-9 higher-rank-lattice Cayley graphs

Status: **PARTIAL / CANDIDATE_FULL for the restricted theorem below; full T09 remains OPEN.** External novelty of the exact degree-9 family is **UNVERIFIED** after bounded current searching. The mathematics below is a complete candidate argument, not an independently reviewed final certification.

## 1. Original problem: source-level before/after, separately from mechanism progress

The frozen parent target is the Benjamini–Schramm bond-percolation conjecture in Cayley form:

> For every locally finite Cayley graph `G` of every finitely generated nonamenable group, prove `p_c(G)<p_u(G)` for iid bond percolation.

**Before this run.** The full parent was OPEN. The newest NM13-11 report proved that if a group contains `F_2` and has a symmetric 3-element generating set, then one can adjoin four free generators to obtain a simple degree-11 Cayley graph with

\[
 p_u-p_c>\frac1{287}.
\]

In particular this gave such degree-11 graphs on `SL_n(Z)` for every `n>=5`.

**After this run.** The parent remains OPEN, but the certified fixed-graph scope improves to degree **9** on the same genuinely non-hyperbolic higher-rank groups:

> **Theorem A.** Let `Gamma=<s,t>` with `s^2=1`, `t^3=1`, and suppose there is an infinite-order `g in Gamma` such that
> \[
> \langle t,g\rangle\cong C_3*\mathbb Z.
> \]
> Put `a_j=t^j g t^{-j}` for `j=0,1,2` and
> \[
> S=\{s,t,t^{-1},a_0^{\pm1},a_1^{\pm1},a_2^{\pm1}\}.
> \]
> Then `G=Cay(Gamma,S)` is simple and 9-regular and satisfies
> \[
> \boxed{p_c(G)<\frac{19}{125}<\frac4{25}<p_u(G)},
> \qquad
> \boxed{p_u(G)-p_c(G)>\frac1{125}=0.008.}
> \]

Using `(2,3)`-generation of `SL_n(Z)` for every `n>=5` and the 2025 simultaneous-ping-pong theorem of Janssens–Temmerman–Thilmany, Theorem A applies to every `SL_n(Z)`, `n>=5`. Thus every such group has a degree-9 Cayley graph with the displayed uniform gap.

This is a source-level advance: both `p_c` and `p_u` are transferred to the actual ambient Cayley graph. It is not an auxiliary inequality and it does not assert the conjecture for every Cayley graph of these groups.

**Mechanism progress, separately.** The new point is not another scalar free-core estimate. The preceding degree-11 result stalled at a rank-3 free core plus three complements. Here the order-three generator is used *inside the percolating comparison subgraph*: the subgroup `C_3*Z` contains an index-three free kernel `F_3`, and with the natural generators its Cayley graph is exactly `T_6 square C_3`. A three-type exact Galton–Watson comparison on triangle fibres gives `p_c<19/125`, while the ambient degree-9 nonbacktracking operator estimate gives `p_u>4/25`. The fibre enhancement is what crosses the old rank-three obstruction.

## 2. Compact continuity handoff

The controlling owner policy is `operations/PROGRESS20_2026-09-20.md`; LIVE20 assigns NM11 to T09 under `proofnet24/NM13-11/progress-percolation/`. I read the latest own report and only the essential historical T09 dependencies.

Preserved June Benjamini–Schramm routes from `probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/open_status.md` and `proof_strategy.md` include normalized finite-set escape, the BK finite-volume/boundary dichotomy, killed-SAW growth, boundary-energy estimates, global `l^2` SAW growth, nonbacktracking polynomial estimates, tree/product stress tests, quotient/fibre-shell criteria and bridge criteria. Several remained conditional because the required finite-set or shell transfer was not proved. Product/tree families were later recognized as overlapping known product results; they are not relabelled as new qualitative progress.

The immediate NM13-11 sequence was:

- degree-34 `SL_3(Z)` free-subgroup/nonbacktracking certificate, gap `>1/420`;
- a general free-core/complement criterion and degree-14 `SL_3(Z)` family, gap `>4/585`;
- degree-11 graphs for groups containing `F_2` with a symmetric 3-element generating set, including `SL_n(Z), n>=5`, gap `>1/287`.

The separate PROB10-09 surface-product work is also preserved. Its current quantitative certificates do not count here as a new qualitative source class because product nonuniqueness is already covered in the literature (in particular Peres 2000).

No historical or peer file was overwritten.

## 3. Algebraic core: `C_3*Z` contains a canonical `F_3` kernel

Let

\[
 H=\langle t,g\rangle\cong C_3*\mathbb Z,
 \qquad t^3=1,
\]

and map `H -> C_3` by `t -> t`, `g -> 1`. Let `K` be its kernel. Using Schreier transversal `1,t,t^2`, Reidemeister–Schreier gives

\[
 K=\langle a_0,a_1,a_2\rangle\cong F_3,
 \qquad a_j=t^jgt^{-j},\quad j=0,1,2.
\]

Moreover conjugation by `t` cyclically permutes the free basis, so

\[
 H=K\rtimes C_3.
\tag{3.1}
\]

With the symmetric generating set

\[
 A=\{a_0^{\pm1},a_1^{\pm1},a_2^{\pm1},t,t^{-1}\},
\]

the Cayley graph `Cay(H,A)` is exactly

\[
 T_6\square C_3.
\tag{3.2}
\]

Indeed write every element uniquely as `k t^r`, `r in {0,1,2}`. Right multiplication by `t^{±1}` moves cyclically in the `C_3` coordinate. Since `t^r a_j t^{-r}=a_{j+r mod 3}`, right multiplication by an `a_j^{±1}` stays in the same `r`-layer and, after relabelling the free basis, gives a copy of the 6-regular free tree. This proves (3.2).

Finally, the full set

\[
 S=A\cup\{s\}
\]

has nine distinct nonidentity elements. The six `a_j^{±1}` are distinct free generators/inverses, `t,t^{-1}` have order 3, and `s` cannot lie in `H`: every nontrivial finite-order element of `C_3*Z` is conjugate into `C_3`, so `H` has no element of order 2. Since `s,t` already generate `Gamma`, `S` generates `Gamma`. Thus `Cay(Gamma,S)` is a simple 9-regular Cayley graph.

## 4. Exact `p_c` upper bound from triangle fibres

We prove

\[
 p_c(T_6\square C_3)<\frac{19}{125}.
\tag{4.1}
\]

Root the `T_6` factor. Every nonroot base vertex has five forward children. Regard the three vertices over one tree vertex as a triangle fibre. During a forward exploration, the **type** of an active fibre is the number `k in {1,2,3}` of its vertices connected to the parent side after all open edges inside that triangle are exposed.

If a parent fibre has type `k`, then in a fixed forward child fibre each of those `k` active layers independently sends an open horizontal edge with probability `p`. Let `j` be the number of resulting seeds, so `j~Bin(k,p)`. Closing those seeds under iid bond percolation on the child triangle gives the following exact distribution.

For one seed,

\[
 C_{1,1}=(1-p)^2,
 \qquad
 C_{1,2}=2p(1-p)^2,
 \qquad
 C_{1,3}=3p^2-2p^3.
\tag{4.2}
\]

For two seeds,

\[
 C_{2,2}=(1-p)^2,
 \qquad
 C_{2,3}=2p-p^2,
\tag{4.3}
\]

and for three seeds `C_{3,3}=1`. Consequently the probability that one forward child has type `ell` given parent type `k` is

\[
 P_{k\ell}(p)
 =\sum_{j=1}^k {k\choose j}p^j(1-p)^{k-j}C_{j,\ell}(p).
\tag{4.4}
\]

Different forward child fibres use disjoint horizontal and internal triangle edges. Since the base is a tree, each fibre has a unique parent. Therefore the forward exploration is exactly a three-type Galton–Watson process whose mean offspring matrix is

\[
 M(p)=5P(p).
\tag{4.5}
\]

At

\[
 p_0=\frac{19}{125}
\]

the executed exact-arithmetic checker evaluates (4.4) and verifies, for

\[
 v=(20,39,57)^T,
\]

that

\[
 M(p_0)v-v=
 \left(
 \frac{5285319}{48828125},
 \frac{1177640378}{6103515625},
 \frac{250214919852}{762939453125}
 \right)^T>0.
\tag{4.6}
\]

All entries of `M(p_0)` are positive. By Collatz–Wielandt,

\[
 \rho(M(p_0))\ge
 \min_i\frac{(M(p_0)v)_i}{v_i}>1.
\]

Hence this finite-type Galton–Watson process survives with positive probability. Its survival produces an infinite open cluster in `T_6 square C_3`. Because the entries of `M(p)` are polynomials in `p` and (4.6) has strict positive slack, the same componentwise inequality holds for all `p<p_0` sufficiently close to `p_0`. Therefore (4.1) is strict.

By (3.2), every left coset of `H` in the ambient Cayley graph carries this subgraph, hence

\[
 p_c(G)\le p_c(T_6\square C_3)<\frac{19}{125}.
\tag{4.7}
\]

This is the source-valid percolation transfer on the `p_c` side.

## 5. Ambient nonbacktracking operator bound gives `p_u>4/25`

Let `A_G` be the adjacency operator of the 9-regular ambient Cayley graph. Split it according to the generating set:

\[
 A_G=A_K+(R_t+R_{t^{-1}})+R_s.
\]

The six free-kernel generators preserve left cosets of `K` and induce `T_6` on each coset, so

\[
 \|A_K\|=2\sqrt5.
\]

The two `t`-translations are unitary and `R_s` is a unitary involution. Thus

\[
 \|A_G\|\le a:=2\sqrt5+3.
\tag{5.1}
\]

For completeness, recall the nonbacktracking transfer used in the preceding reports. On a simple `D`-regular graph, if `N_n` is the endpoint kernel for length-`n` nonbacktracking walks, then

\[
 N_n=A_GN_{n-1}-(D-1)N_{n-2}\qquad(n\ge3).
\]

If `||A_G||<=a`, spectral calculus shows

\[
 \limsup_n\|N_n\|_{2\to2}^{1/n}\le\beta_D(a),
\]

where `beta_D(a)` is the larger positive root of

\[
 z^2-az+(D-1)=0
\]

when `a>2sqrt(D-1)` (and equals `sqrt(D-1)` below that threshold). Every open connection has a self-avoiding, hence nonbacktracking, witness, so entrywise

\[
 T_p\le\sum_{n\ge0}p^nN_n.
\]

Therefore `T_p` is a bounded `l^2` operator whenever `p beta_D(a)<1`, proving

\[
 p_{2\to2}(G)\ge\beta_D(a)^{-1}.
\tag{5.2}
\]

Above `p_u`, uniqueness and FKG give

\[
 T_p(x,y)\ge\mathbb P_p(x\leftrightarrow\infty,\,y\leftrightarrow\infty)
 \ge\theta(p)^2>0,
\]

so `T_p` cannot be bounded on `l^2` of an infinite Cayley graph. Hence

\[
 p_{2\to2}(G)\le p_u(G).
\tag{5.3}
\]

Here `D=9`, so `D-1=8`. Set `z_0=25/4`. The exact checker records

\[
 453^2-5\cdot200^2=5209>0,
\]

hence `sqrt(5)<453/200`, and therefore

\[
 a=3+2\sqrt5<\frac{753}{100}.
\]

But exactly

\[
 z_0+\frac8{z_0}
 =\frac{25}{4}+\frac{32}{25}
 =\frac{753}{100}.
\tag{5.4}
\]

For `z>sqrt8`, the function `z+8/z` is strictly increasing. The larger root `beta_9(a)` is `>sqrt8`, so (5.4) gives

\[
 \beta_9(a)<\frac{25}{4}.
\]

Combining (5.2)-(5.3),

\[
 p_u(G)\ge p_{2\to2}(G)>\frac4{25}.
\tag{5.5}
\]

Together with (4.7),

\[
 \boxed{
 p_u(G)-p_c(G)
 >\frac4{25}-\frac{19}{125}
 =\frac1{125}.
 }
\tag{5.6}
\]

This completes Theorem A.

## 6. Application to every `SL_n(Z)`, `n>=5`

Two external group-theoretic inputs are used, and both were rechecked in this run.

First, the completed `(2,3)`-generation classification for integer special linear groups states that `SL_n(Z)` is generated by an involution and an element of order 3 if and only if `n>=5`; see M. A. Vsemirnov, *On (2,3)-generation of matrix groups over the ring of integers, II*, St. Petersburg Math. J. 32 (2021), 865–884, DOI `10.1090/spmj/1674`. Thus fix

\[
 SL_n(\mathbb Z)=\langle s_n,t_n\rangle,
 \qquad s_n^2=t_n^3=1.
\tag{6.1}
\]

Second, Janssens–Temmerman–Thilmany, arXiv:2510.23957v1 (submitted 28 October 2025), Theorem 3.23, proves abundance of simultaneous ping-pong partners in Zariski-dense subgroups of products of inner real forms of `SL_n`/`GL_n`. In the paper's notation, a finite subgroup that almost embeds in an adjoint simple quotient admits an infinite-order regular semisimple partner with the asserted free-product canonical map.

Apply this to the real algebraic group `SL_n`, the Zariski-dense arithmetic subgroup `SL_n(Z)`, and

\[
 A=\langle t_n\rangle\cong C_3.
\]

The center of `SL_n(R)` has no nontrivial element of order 3, so

\[
 A\cap Z(SL_n(\mathbb R))=\{1\}.
\]

The quotient to the adjoint `PGL_n` therefore restricts injectively to `A`, satisfying Theorem 3.23's hypothesis. Consequently there exists an infinite-order `g_n in SL_n(Z)` such that

\[
 \langle t_n,g_n\rangle\cong C_3*\mathbb Z.
\tag{6.2}
\]

Theorem A now applies. We obtain:

> **Corollary B.** For every `n>=5`, `SL_n(Z)` admits a simple degree-9 Cayley graph `G_n` satisfying
> \[
> \boxed{p_c(G_n)<19/125<4/25<p_u(G_n)},
> \qquad
> \boxed{p_u(G_n)-p_c(G_n)>1/125.}
> \]

These are not hyperbolic-group examples: `SL_n(Z)` contains `Z^2`. They also lie outside the later all-Cayley acylindrically-hyperbolic theorem; higher-rank lattices such as `SL_n(Z)`, `n>=3`, are not acylindrically hyperbolic. Thus the ambient family is genuinely outside the principal checked all-Cayley scopes. The comparison subgraph `T_6 square C_3` is only the `p_c` witness inside the higher-rank-lattice Cayley graph; the ambient graph is not itself being claimed as a new product case.

## 7. Requested current literature scopes, checked 2026-09-20

The bounded current check retained the following exact distinctions.

1. **Hutchcroft, arXiv:1804.10191v3**, last revised **26 March 2019**, proves `p_c<p_u` for connected locally finite **nonamenable Gromov-hyperbolic quasi-transitive graphs**. It explicitly describes this as verifying the Benjamini–Schramm conjecture under the additional hypothesis of hyperbolicity. It does not contain the higher-rank-lattice graphs above.

2. **Hutchcroft–Pan, arXiv:2409.12283v1**, submitted **18 September 2024**, studies behavior **at `p_u`**. It proves nonuniqueness at `p_u` for groups containing an amenable `wq`-normal subgroup of exponential growth and proves a co-heredity result for a strong endpoint property. This is not a quantitative fixed-Cayley `p_c<p_u` theorem of the form proved here.

3. **Terlov–Timár, arXiv:2502.02560v2**, revised **14 September 2025**, concerns weighted/level amenability in nonunimodular settings and proves a relaxed Pak–Smirnova-Nagnibeda-style result involving the heavy threshold `p_h<p_u`. It is not the ordinary unimodular fixed-Cayley `p_c<p_u` target.

4. **Choi–Seo, arXiv:2508.08932** (checked as a later enlargement), proves the nonuniqueness phase for every Cayley graph of every acylindrically hyperbolic group. Higher-rank `SL_n(Z)` is outside that scope.

5. **Janssens–Temmerman–Thilmany, arXiv:2510.23957v1**, submitted **28 October 2025**, supplies the torsion-relative ping-pong partner used in Section 6. Its Theorem 3.23 is a group-theoretic input, not a percolation theorem; the new percolation transfer is Sections 3–5 above.

A bounded exact-phrase/current search did not surface a prior percolation theorem for these degree-9 `SL_n(Z)` generating sets or this `C_3*Z` triangle-fibre transfer. This is negative search evidence only, not a worldwide novelty or priority certificate.

## 8. Exact executable check

The essential finite calculations were executed with exact rational arithmetic and archived in this namespace.

Checker:

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T05-50-00+0300__t09-triangle-fibre-check.py`

creation commit:

`f586328e735e78fa37de610cc665c6cafd2315af`

Executed output:

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T05-50-00+0300__t09-triangle-fibre-check.out`

output commit:

`8cf38312fac144ff9bf4acd6e6dc2890ff741efc`

The output records the exact `P` and `M=5P` matrices at `p=19/125`, the positive Perron–Frobenius test vector `v=(20,39,57)`, the three exact positive slacks in (4.6), the rational `sqrt5` certificate, the exact identity `25/4+8/(25/4)=753/100`, and

`ALL_EXACT_CHECKS_PASS`.

This is a self-check, not an independent review.

## 9. What remains / next attack

The universal parent remains OPEN. This run weakens the previous extra hypotheses in a source-relevant way—from an artificially adjoined rank-four free core and degree 11 to a torsion-relative `C_3*Z` core and degree 9—but it still chooses a favorable generating set rather than handling an arbitrary Cayley graph.

The next obstruction is therefore not another decimal improvement. A materially useful next route is to generalize the triangle-fibre theorem to a finite-subgroup partner already present in an arbitrary small generating set: for a finite subgroup `F` and a ping-pong partner `g`, identify the free kernel of `F*<g>`, compute the exact finite-state fibre branching operator on `Cay(F,B_F)`, and compare its `p_c` gain against the ambient nonbacktracking norm. The objective is a criterion expressed in terms of a *pre-existing* torsion block plus the remaining generators, reducing the amount by which the generating set is engineered. If that fails, the distinct route is a colored nonbacktracking recurrence on the original generators rather than further enlarging the free core.

No unknown quantity is recorded as zero.

## 10. `ledger_delta`

```yaml
ledger_delta:
  target: T09
  parent_problem: "pc(G)<pu(G) for every locally finite Cayley graph of every finitely generated nonamenable group"
  parent_status_before: OPEN
  parent_status_after: OPEN
  source_scope_before: "degree-11 favorable Cayley graphs for groups containing F2 with a symmetric 3-element generating set; SL_n(Z), n>=5; gap > 1/287"
  source_scope_after: "degree-9 Cayley graphs of SL_n(Z), n>=5, and abstract (2,3)-generated groups with a C3 ping-pong partner; pc<19/125<4/25<pu"
  certified_gap_before: "> 1/287"
  certified_gap_after: "> 1/125"
  mechanism_advance: "C3*Z index-3 F3 kernel + exact 3-type triangle-fibre Galton-Watson pc transfer + degree-9 nonbacktracking p2->2 transfer"
  restricted_theorem_status: CANDIDATE_FULL
  external_novelty: UNVERIFIED
  checker: "proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T05-50-00+0300__t09-triangle-fibre-check.py"
  checker_commit: "f586328e735e78fa37de610cc665c6cafd2315af"
  output: "proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T05-50-00+0300__t09-triangle-fibre-check.out"
  output_commit: "8cf38312fac144ff9bf4acd6e6dc2890ff741efc"
  unchanged_substantive_runs: 0
  failed_recoveries: 0
  residual_obstruction: "arbitrary fixed Cayley generating sets; current theorem still engineers a favorable torsion/free-product block"
  next_attack: "finite-subgroup fibre branching criterion for a pre-existing torsion block, then colored nonbacktracking if the scalar ambient norm remains blocking"
```
