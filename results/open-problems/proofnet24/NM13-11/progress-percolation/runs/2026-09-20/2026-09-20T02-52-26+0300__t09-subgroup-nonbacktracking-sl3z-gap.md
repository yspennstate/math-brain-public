Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.

# NM13-11 / T09 — subgroup–nonbacktracking transfer and an explicit positive gap on a nonhyperbolic Cayley graph

Status: **PARTIAL / CANDIDATE_FULL for the restricted theorem below; full T09 remains OPEN.** External novelty is **UNVERIFIED** pending a broader prior-art check. The mathematical claim below is complete as a self-contained candidate, but has not received independent review.

## 1. Original problem versus this run

The parent problem is the Benjamini–Schramm nonuniqueness conjecture in the frozen Cayley-graph form: for every locally finite Cayley graph `G` of every finitely generated nonamenable group, prove

\[
 p_c(G)<p_u(G)
\]

for iid bond percolation.

**Source-level before.** The full parent conjecture was OPEN. The inherited June project had many conditional operator criteria and product/tree stress tests, but the strongest product examples were later recognized as already covered by Hutchcroft–Pan technology. No report existed yet under `proofnet24/NM13-11/progress-percolation/`. For a genuinely outside exact Cayley graph, the certified numerical gap was therefore **UNKNOWN**, not zero.

**Source-level after.** The full parent conjecture is still OPEN, but this run proves a positive gap for the explicit Cayley graph

\[
G=\operatorname{Cay}(\mathrm{SL}_3(\mathbb Z),S_{11})
\]

defined in Section 5, with the rigorous source-level quantitative milestone

\[
\boxed{p_u(G)-p_c(G)>\frac1{420}=0.00238095238\ldots.}
\]

More generally, Section 3 proves a subgroup–nonbacktracking comparison theorem that applies to any Cayley graph whose generating set contains a subgroup with a known percolation upper bound and whose complementary generator operator is sufficiently small. The free-subgroup corollary is only one specialization.

**Mechanism-level advance.** The new mechanism combines (i) a subgroup comparison giving an upper bound on `p_c`, with (ii) a nonbacktracking-walk operator bound giving a lower bound on `p_{2->2}`, and (iii) the general `p_{2->2}<=p_u` transfer. This is strictly more flexible than the inherited global-SAW route: the subgroup controls only `p_c`, while all generators enter the nonbacktracking operator estimate.

## 2. Essential continuity recovered

The controlling progress-first policy is `operations/PROGRESS20_2026-09-20.md`. The exact T09 instruction is also recorded in `operations/PROB10_2026-09-20.md`. The relevant inherited proof history is

- `probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/open_status.md`;
- `probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/proof_strategy.md`.

The latter already developed: finite-set escape criteria; killed-SAW and global `l^2` SAW criteria; nonbacktracking bounds; tree-product calculations; quotient/fiber shell criteria; and fixed-endpoint nonbacktracking bridge criteria. Crucially, its Round 042 records that the tree-times-amenable-factor and lamplighter product scope is already covered by Hutchcroft–Pan, so those examples are not counted here as new progress. Its later shell criteria were conditional: they did not themselves furnish a new uncovered Cayley class.

`POSTED.md` was checked for the current exclusions. It does not mark the full T09 source problem as posted/closed; the register explicitly distinguishes restricted percolation results from unrestricted parents.

## 3. New theorem: subgroup–nonbacktracking comparison

Let `Gamma` be a countable group and let `S` be a finite symmetric generating set with no identity and no duplicate unoriented edges, so that

\[
G=\operatorname{Cay}(\Gamma,S)
\]

is a simple `D`-regular Cayley graph, `D=|S|`. Suppose

\[
S=S_H\sqcup B
\]

is a disjoint union of symmetric sets, with `H=<S_H>`. Let `A_H` be the adjacency operator of `Cay(H,S_H)` on `l^2(H)`, and let

\[
\alpha_H=\|A_H\|_{2\to2}.
\]

On `l^2(Gamma)`, the `S_H`-adjacency operator is a direct sum over right cosets of `H`, hence has the same norm `alpha_H`. Let

\[
K_B=\sum_{b\in B}R_b,\qquad \kappa=\|K_B\|_{2\to2},
\]

where `R_b` is right translation. Thus the full adjacency operator `A` satisfies

\[
\|A\|_{2\to2}\le a:=\alpha_H+\kappa.
\]

For `D>=2`, define

\[
\beta_D(a)=
\begin{cases}
\sqrt{D-1},&a\le2\sqrt{D-1},\\[2mm]
\dfrac{a+\sqrt{a^2-4(D-1)}}2,&a>2\sqrt{D-1}.
\end{cases}
\]

### Theorem 3.1

Assume that

\[
p_c(\operatorname{Cay}(H,S_H))\le p_0
\qquad\text{and}\qquad
p_0\,\beta_D(a)<1.
\]

Then

\[
p_c(G)\le p_0<\beta_D(a)^{-1}\le p_{2\to2}(G)\le p_u(G),
\]

and in particular

\[
\boxed{p_u(G)-p_c(G)\ge \beta_D(a)^{-1}-p_0>0.}
\]

This theorem weakens the extra hypothesis from “the whole Cayley graph is tree-like/highly nonamenable” to “one subgroup supplies a percolating subgraph while the remaining generators have controlled `l^2` operator norm.” No normality, quotient, hyperbolicity, product decomposition, or amenability of `H` or `Gamma/H` is assumed.

### Proof

**Step 1: subgroup comparison for `p_c`.** The graph `Cay(Gamma,S)` contains, on every right coset of `H`, a copy of `Cay(H,S_H)` using only `S_H`-edges. Couple Bernoulli percolation by using the same edge variables on this subgraph. If `p>p_c(Cay(H,S_H))`, an infinite open component already occurs inside a coset with positive probability. Hence

\[
p_c(G)\le p_c(\operatorname{Cay}(H,S_H))\le p_0.
\]

**Step 2: nonbacktracking operator growth.** Let `N_n(x,y)` be the number of length-`n` nonbacktracking walks from `x` to `y` in `G`, and identify `N_n` with its kernel/operator. On any `D`-regular graph,

\[
N_0=I,\qquad N_1=A,\qquad N_2=A^2-DI,
\]

and, for `n>=3`,

\[
N_n=A N_{n-1}-(D-1)N_{n-2}.
\]

Thus `N_n=P_n(A)` for a scalar polynomial recurrence. Writing `q_D=D-1`, the characteristic equation at a spectral value `lambda` is

\[
z^2-\lambda z+q_D=0.
\]

For `|lambda|<=a`, the largest possible characteristic-root modulus is at most `beta_D(a)`. If the roots coincide, the scalar solution acquires only a linear prefactor. Equivalently, one may use the exact Chebyshev representation

\[
P_n(\lambda)=q_D^{n/2}U_n\!\left(\frac{\lambda}{2\sqrt{q_D}}\right)
-q_D^{(n-2)/2}U_{n-2}\!\left(\frac{\lambda}{2\sqrt{q_D}}\right),\qquad n\ge2.
\]

Spectral calculus therefore gives

\[
\limsup_{n\to\infty}\|N_n\|_{2\to2}^{1/n}\le\beta_D(a).
\]

**Step 3: percolation transfer.** Every open connection from `x` to `y` contains an open self-avoiding path, and every self-avoiding path is nonbacktracking. The union bound gives the pointwise kernel inequality

\[
T_p(x,y)=\mathbb P_p(x\leftrightarrow y)
\le \sum_{n\ge0}p^nN_n(x,y).
\]

If `p<1/beta_D(a)`, choose `c` with `beta_D(a)<c<1/p`. The preceding limsup gives `||N_n||<=C_c c^n` for all large `n`, so the operator series on the right converges absolutely in `l^2` operator norm. Because all kernels are nonnegative,

\[
|T_pf|\le\left(\sum_{n\ge0}p^nN_n\right)|f|,
\]

and hence `T_p` is `l^2`-bounded. Therefore

\[
p_{2\to2}(G)\ge\beta_D(a)^{-1}.
\]

**Step 4: `p_{2->2}<=p_u`.** For every `p>p_u` on a transitive graph there is almost surely a unique infinite cluster and `theta(p)=P_p(o<->infinity)>0`. By FKG and uniqueness,

\[
T_p(x,y)\ge P_p(x\leftrightarrow\infty,\ y\leftrightarrow\infty)\ge\theta(p)^2
\]

for every `x,y`. A kernel bounded below by a positive constant on an infinite vertex set is not bounded on `l^2` (test it on normalized indicators of growing finite sets). Hence no `p>p_u` lies below the `l^2` threshold, and `p_{2->2}<=p_u`.

Combining Steps 1–4 proves the theorem. `square`

## 4. Free-subgroup specialization

Suppose `S_H={a_1^{+-1},...,a_m^{+-1}}` freely generates the free group `F_m`. Put

\[
q=2m-1.
\]

Then `Cay(H,S_H)` is the `(q+1)`-regular tree, so

\[
p_c(H,S_H)=\frac1q,
\qquad
\alpha_H=2\sqrt q.
\]

If `r=|B|`, then the triangle inequality gives `kappa<=r`. Consequently a completely explicit sufficient condition is

\[
\boxed{\beta_{q+1+r}(2\sqrt q+r)<q.}
\]

Whenever this holds,

\[
p_u(G)-p_c(G)\ge
\frac1{\beta_{q+1+r}(2\sqrt q+r)}-\frac1q>0.
\]

This is the first actual percolation transfer in this run. The inequality is not merely an auxiliary operator estimate: it directly separates `p_c` and `p_u`.

## 5. Explicit application to `SL_3(Z)`

Let `Gamma=SL_3(Z)`. In the upper-left `2x2` block define

\[
u=I+2E_{12},\qquad v=I+2E_{21}.
\]

The classical Sanov ping-pong argument shows that `<u,v>` is the free group `F_2`. For completeness, on projective coordinates use the two cones `|x|>|y|` and `|y|>|x|`: every nonzero power of `u` sends the second cone into the first, and every nonzero power of `v` sends the first into the second.

For `j=0,...,10`, set

\[
a_j=u^jvu^{-j}.
\]

These eleven elements freely generate `F_11`. One direct way to see this is to map `F(u,v)` onto `Z` by `u->1`, `v->0`: Schreier rewriting gives the free basis

\[
\{u^jvu^{-j}:j\in\mathbb Z\}
\]

for the kernel, so every finite subfamily is free. Let

\[
S_H=\{a_0^{\pm1},...,a_{10}^{\pm1}\}.
\]

As a complementary generating set take all elementary unit transvections

\[
B=\{I\pm E_{ij}:1\le i\ne j\le3\}.
\]

There are `12` of them and they generate `SL_3(Z)` by elementary integer row operations. Moreover every `a_j` is congruent to `I` modulo `2`, while every element of `B` is not, so the two parts are disjoint. Freeness also guarantees the `22` elements `a_j^{+-1}` are pairwise distinct. Thus

\[
S_{11}=S_H\sqcup B
\]

is a simple symmetric generating set and

\[
D=22+12=34,\qquad q=21.
\]

The subgroup part has operator norm `2 sqrt(21)`. The complementary operator is the sum of twelve unitaries, so `kappa<=12`. Hence

\[
\|A_G\|\le12+2\sqrt{21}.
\]

The exact rational estimate

\[
\sqrt{21}<\frac{23}{5}
\]

gives

\[
a<12+\frac{46}{5}=\frac{106}{5}.
\]

Now test the nonbacktracking characteristic roots against `t=20`. Since

\[
D-1=33<20^2
\]

and

\[
a<\frac{106}{5}=\frac{424}{20}
<\frac{433}{20}
=20+\frac{33}{20},
\]

all characteristic roots for every spectral value `|lambda|<=a` have modulus strictly smaller than `20`. Thus

\[
\beta_{34}(a)<20.
\]

The free `F_11` subtree gives

\[
p_c(G)\le\frac1{21},
\]

while Theorem 3.1 gives

\[
p_{2\to2}(G)>\frac1{20}
\quad\text{and hence}\quad
p_u(G)>\frac1{20}.
\]

Therefore

\[
\boxed{
 p_u(G)-p_c(G)>
 \frac1{20}-\frac1{21}
 =\frac1{420}.
}
\]

This is a strict quantitative source-level gap for one exact Cayley graph, not a simulation and not an auxiliary inequality awaiting a transfer.

### Why the hyperbolic theorem does not cover this exact graph

`SL_3(Z)` contains `Z^2`; for example the commuting transvections `I+E_12` and `I+E_13` generate a rank-two free abelian subgroup. A finitely generated Gromov-hyperbolic group cannot contain `Z^2`. Hence no Cayley graph of `SL_3(Z)` is Gromov hyperbolic, and Hutchcroft's 2019 hyperbolic theorem (arXiv:1804.10191) does not apply to this graph.

## 6. Three routes compared in this run

1. **Subgroup relativization alone — not enough for the requested gap.** arXiv:2409.12283 studies behavior at `p_u` and proves nonuniqueness at `p_u` for groups containing an amenable `wq`-normal subgroup of exponential growth, plus a co-heredity theorem. That is important endpoint information but does not by itself produce the strict numerical `p_c<p_u` separation needed here.

2. **Classical adjacency/spectral perturbative route — deliberately stress-tested at the boundary.** The older literature contains “highly nonamenable” spectral criteria and, existentially, Pak–Smirnova-Nagnibeda-type results showing every nonamenable finitely generated group has some Cayley graph with a nonuniqueness phase. For the present exact generating set, the immediately available comparison is `||A_G||<=12+2sqrt(21)`, which is slightly **larger** than `21`; therefore the same coarse data do not certify the simplest adjacency comparison `||A_G||<q`. This does **not** prove that every older spectral criterion fails for the exact graph; it shows why the nonbacktracking recurrence extracts additional room from the same subgroup/operator data.

3. **Subgroup `p_c` + nonbacktracking `p_{2->2}` — succeeds.** The recurrence retains cancellation absent from the crude resolvent bound and gives `beta<20<21`, producing the explicit gap `>1/420`.

The successful method is therefore materially different from the inherited finite-set-escape bookkeeping and from the already-covered tree-product examples.

## 7. Current source scopes checked on 20 September 2026

The following bounded primary-source refresh was performed. It is a scope check, not a claim of exhaustive worldwide novelty.

- **Hutchcroft, arXiv:1804.10191, _Percolation on hyperbolic graphs_.** The abstract/Theorem 1.3 proves `p_c<p_u` for every nonamenable Gromov-hyperbolic quasi-transitive graph. The paper also defines `p_{2->2}` and records `p_c<=p_{2->2}<=p_u`. URL: https://arxiv.org/abs/1804.10191 . The explicit `SL_3(Z)` graph above is nonhyperbolic.
- **Hutchcroft–Pan, arXiv:2409.12283, _Percolation at the uniqueness threshold via subgroup relativization_.** Its stated new class is groups containing an amenable `wq`-normal subgroup of exponential growth, for which it proves nonuniqueness **at `p_u`**, together with a co-heredity principle. URL: https://arxiv.org/abs/2409.12283 . This is not itself a positive `p_u-p_c` estimate for the graph constructed here.
- **Terlov–Timar, arXiv:2502.02560v2, _Weighted-amenability and percolation_.** The current arXiv page (v2, 14 September 2025) states a relaxed Pak–Smirnova-Nagnibeda-style result for Hutchcroft's weighted/nonunimodular `p_h<p_u` conjecture and continuity at `p_h`. URL: https://arxiv.org/abs/2502.02560 . This is a different threshold and weighted/nonunimodular scope, not the ordinary `p_c` gap proved here.
- **Current adjacent 2026 endpoint result.** Mukherjee–Recke, _Haagerup property and group-invariant percolation_ (PTRF 2026), gives nonuniqueness at `p_u` for Cayley graphs of infinite property-(T) groups. This is relevant to `SL_3(Z)` but again does not by itself separate `p_c` from `p_u` quantitatively.

Hutchcroft's 2019 introduction also records older perturbative/high-nonamenability criteria and the Pak–Smirnova-Nagnibeda existential theorem that every nonamenable finitely generated group has **some** Cayley graph with `p_c<p_u`. Therefore the group-level statement “`SL_3(Z)` admits some good generating set” is not claimed as new. What is established here is the exact explicit generating set above plus the quantitative `1/420` certificate and the subgroup–nonbacktracking transfer. A bounded exact-search did not locate this exact statement, but **external novelty remains UNVERIFIED**.

## 8. Essential exact check

The executed exact-arithmetic checker is

`proofnet24/NM13-11/progress-percolation/artifacts/2026-09-20/sl3z_free_subgroup_nb_gap_exact.py`

created at commit `fad8553f231070359aaa0d1ebf74b064754c4b08`.

Its actual archived output is

`proofnet24/NM13-11/progress-percolation/artifacts/2026-09-20/sl3z_free_subgroup_nb_gap_exact.out`

created at commit `4f3b7e948e93221c45c5d45a60a1ed8d778ee381`.

The checker verifies: the `22+12=34` concrete generator bookkeeping; determinant-one and mod-2 disjointness; `sqrt(21)<23/5`; the adjacency-norm upper certificate `106/5`; the `t=20` nonbacktracking root gate `433/20`; and the exact gap `1/420`. It terminates `ALL_EXACT_CHECKS_PASS`. The freeness proof is theorem-sized and is written above; the script does not pretend to certify an infinite-group freeness theorem by finite enumeration.

## 9. Residual obstruction and next attack

The parent conjecture remains far broader. The new criterion still needs a subgroup whose own `p_c` is well controlled and enough operator separation between that subgroup and the added generators. It does not address a fixed arbitrary generating set that has no visible free/tree-like subgraph, and it does not yet exploit subgroup relativization when the useful subgroup is distorted or has a dense boundary in the ambient generating set.

The next useful weakening is therefore **not** to add more free generators. It is to replace the free-subgroup input by a subgroup with a proved `p_c` upper bound and a sharper complementary operator estimate `kappa<<|B|`, or to replace the literal subgroup by a Schreier/quotient block whose nonbacktracking transfer can still be proved. A particularly relevant stress test is a fixed low-degree higher-rank lattice generating set, where the free-subgroup domination used here is unavailable.

## 10. ledger_delta

```yaml
ledger_delta:
  worker: NM13-11
  parent: T09_Benjamini_Schramm_nonuniqueness_phase
  full_parent_status_before: OPEN
  full_parent_status_after: OPEN
  restricted_claim_status: CANDIDATE_FULL_PENDING_INDEPENDENT_REVIEW
  external_novelty: UNVERIFIED
  exact_graph: "Cay(SL_3(Z), S_11) with 22 Sanov-Schreier free generators plus 12 elementary transvections"
  source_metric: "certified lower bound on p_u(G)-p_c(G)"
  source_metric_before: UNKNOWN
  source_metric_after: "> 1/420"
  source_scope_advance: "one explicit nonhyperbolic Cayley graph, plus a general subgroup-nonbacktracking sufficient criterion"
  mechanism_advance: "p_c upper bound from a percolating subgroup + p_{2->2} lower bound from nonbacktracking operator growth"
  inherited_failures_preserved:
    - "finite-set escape boundary-energy route remained conditional"
    - "tree-times-amenable-factor examples were later recognized as already covered"
    - "shell/nonbacktracking bridge criteria had no new class transfer"
  routes_this_run:
    - "subgroup relativization endpoint route: insufficient for a p_c/p_u gap"
    - "coarse adjacency spectral route: same bounds do not certify at q=21"
    - "subgroup plus nonbacktracking operator route: success"
  exact_checker: "proofnet24/NM13-11/progress-percolation/artifacts/2026-09-20/sl3z_free_subgroup_nb_gap_exact.py"
  exact_output: "proofnet24/NM13-11/progress-percolation/artifacts/2026-09-20/sl3z_free_subgroup_nb_gap_exact.out"
  next_attack: "replace free subgroup by a less tree-like subgroup/Schreier block with a proved p_c upper bound and sharpen kappa"
```
