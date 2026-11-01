Runtime model: **GPT-5.6 Sol**. Reasoning effort: **UNVERIFIED**.

# NM13-11 / T09 — arbitrary perturbations of high-degree virtually simple BMW Cayley graphs

Status: **PARTIAL / CANDIDATE_FULL for the restricted theorems below; universal T09 remains OPEN.** Exact arithmetic for the load-bearing parameter inequalities was executed and archived in this run. No independent review has yet occurred. Exact worldwide priority is **UNVERIFIED**.

## 1. Parent target and compact handoff

The parent target remains the Benjamini--Schramm conjecture for iid bond percolation:

> For every locally finite Cayley graph `G` of every finitely generated nonamenable group, prove `p_c(G)<p_u(G)`.

The controlling policy is `operations/PROGRESS20_2026-09-20.md`; current LIVE20 assigns NM11 to T09 at `proofnet24/NM13-11/progress-percolation/`. `POSTED.md` does not close the universal target and explicitly preserves restricted percolation results as restricted.

The latest own substantive predecessor is

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T17-25-00+0300__t09-two-seed-arbitrary-four-pairs-gap.md`

at commit `9d928247be54817b37352b79093e80142bbbf3c8`. It proves that every four-pair arbitrary augmentation of a `(12,8)` BMW marking has a positive gap, using a new two-seed fibre Galton--Watson comparison. Its residual obstruction was that five arbitrary pairs cannot be reached by any `p_c` estimate using only the fixed degree-20 base graph together with the same scalar `p_u` estimate.

The latest neighboring PROB10-09 work remains in the quotient/extension/vertical-spectral-budget lane and explicitly leaves the Rattaggi/BMW product-fibre lane to NM13-11; commit `1a21781e73ecd8bd79d1a76cdab08c5c5aa9c96d` records that separation. No ownership collision is introduced here.

Preserved older Benjamini--Schramm mechanisms include finite-set escape/BK last-exit, killed-SAW and susceptibility-weighted boundary energy, global `ell^2` SAW, scalar nonbacktracking polynomials, quotient/fibre-shell and bridge criteria, followed by free-core, triangle-fibre, S-arithmetic, Rattaggi perturbation, power-layer, factor-branching, pure-torsion and multiseed fibre constructions. Routes without an actual `p_c`-to-`p_u` transfer remain mechanism history only.

## 2. Source-level before/after

### Before

The strongest fully arbitrary perturbation theorem on this lane concerned one fixed BMW degree pair `(12,8)` and exactly four arbitrary new inverse pairs:

`p_c < 1353/25000 < 677/12500 < p_u`.

Five arbitrary pairs on that fixed base were UNKNOWN.

### After

The present run changes the base degree instead of trying to squeeze the fixed `(12,8)` constants. It gives an unbounded family of virtually simple BMW groups and an arbitrary perturbation budget growing linearly with the tree degree.

> **Theorem A (abstract BMW perturbation criterion).** Let `Gamma` act freely and transitively on the vertices of `T_d x T_e`, and let `S_0` be the neighbor marking, so `Cay(Gamma,S_0) ~= T_d square T_e`. Assume `d>=e>=3`. Add `k` genuinely new inverse pairs, all `2k` added elements distinct and disjoint from `S_0`, with no algebraic hypothesis on them. Let
> 
> `D=d+e+2k`, `Q=D-1`,
> 
> `a=2sqrt(d-1)+2sqrt(e-1)+2k`.
> 
> If there is a real `z` such that
> 
> `sqrt(Q)<z<d-1` and `z+Q/z>a`,
> 
> then
> 
> `p_c(G) <= 1/(d-1) < 1/z < p_u(G)`,
> 
> in particular
> 
> `p_u(G)-p_c(G) > 1/z-1/(d-1)>0`.

No simplicity, property of the perturbation subgroup, free layer, quotient, or fibre alignment is used in Theorem A.

Radu, arXiv:1712.01091, constructs in the BMW setting infinite families of virtually simple lattices in `Aut(T_6) x Aut(T_{4n})` for every `n>=2`. Swapping factors, put `d=4n`, `e=6`.

> **Theorem B (linear arbitrary perturbation budget on Radu's family).** For every integer `n>=8`, every Radu BMW group of degree `(6,4n)` in the above family, equipped with its natural product marking, remains in the nonuniqueness phase after adjoining **any `k<=n` genuinely new inverse pairs**, with no relation assumptions. More precisely,
> 
> `p_c <= 1/(4n-1) < 1/(4n-2) < p_u`,
> 
> hence
> 
> `p_u-p_c > 1/((4n-2)(4n-1))`.

At the first certified endpoint `n=8,k=8`, this is a degree-54 Cayley graph obtained from the degree-38 product marking by eight completely arbitrary inverse pairs, and

`boxed(p_c <= 1/31 < 1/30 < p_u)`,

so

`boxed(p_u-p_c > 1/930)`.

This is a strict scope expansion from four arbitrary perturbing pairs on one degree pair to an unbounded sequence of virtually simple BMW groups with an arbitrary perturbation budget tending to infinity.

The perturbation density can be pushed further.

> **Theorem C (near-two-n arbitrary perturbation density).** Fix `0<epsilon<=2`. For every integer
> 
> `n >= ceil(16/epsilon^2)`,
> 
> and every integer
> 
> `k <= (2-epsilon)n`,
> 
> the same Radu BMW graphs satisfy
> 
> `p_c <= 1/(4n-1) < 1/(4n-2) < p_u`.

Thus, for any fixed positive `epsilon`, almost `(2-epsilon)n` completely arbitrary inverse pairs can be added. A sharper finite corollary proved below is `k<=3n/2` already for every `n>=25`.

**Original-problem delta:** universal T09 is still OPEN. The proved fixed-graph scope grows from a bounded arbitrary perturbation theorem on one `(12,8)` base to unbounded arbitrary perturbations on an infinite virtually simple BMW family.

**Mechanism delta:** instead of further improving `p_c` on the same base, the argument couples a spanning high-degree tree critical bound with the exact product-tree adjacency norm. The tree degree contributes linearly to `1/p_c` but only by a square root to the base operator norm, leaving a linear spectral budget for completely arbitrary extra generators.

## 3. Proof of Theorem A

Fix a base vertex `o` in `T_d x T_e`. Simple transitivity identifies `Gamma` with the vertex set by `g -> go`. For each neighbor of `o` there is a unique group element carrying `o` to it; these elements form a finite symmetric neighbor marking `S_0`, and the corresponding Cayley graph is exactly `T_d square T_e`.

### Critical side

The product graph contains a copy of `T_d` as a spanning-factor subgraph, obtained by fixing the `T_e` coordinate. The augmented graph still contains every edge of this tree. Bernoulli bond percolation on `T_d` is supercritical for `p>1/(d-1)`, so monotonicity under adding edges gives

`p_c(G) <= 1/(d-1)`.                                             (3.1)

This is an actual percolation transfer, not an auxiliary isoperimetric inequality.

### Operator side

The adjacency operator of the product marking is the sum of the two factor adjacencies, hence

`||A_0|| = 2sqrt(d-1)+2sqrt(e-1)`.                                (3.2)

Each added inverse pair `c^{+-1}` contributes `R_c+R_{c^{-1}}`; right translations are unitary, so its norm is at most `2`. Therefore, without any relation assumption,

`||A_G|| <= a := 2sqrt(d-1)+2sqrt(e-1)+2k`.                       (3.3)

Let `N_m` be the length-`m` nonbacktracking walk operator on the `D`-regular augmented Cayley graph and put `Q=D-1`. Then

`N_0=I`, `N_1=A_G`, `N_2=A_G^2-DI`,

`N_m=A_G N_{m-1}-Q N_{m-2}` for `m>=3`.                           (3.4)

By spectral calculus for the scalar recurrence, if `z>sqrt(Q)` and

`z+Q/z>||A_G||`,                                                  (3.5)

then the `ell^2` exponential growth rate of `N_m` is strictly smaller than `z`. Every open connection contains a shortest open path, and every shortest path is nonbacktracking, so entrywise

`T_p(x,y) <= sum_{m>=0} p^m N_m(x,y)`.                            (3.6)

The strict growth bound in (3.5) implies that this operator series is bounded for all `p` in an interval strictly beyond `1/z`; hence

`p_{2->2}(G)>1/z`.                                                (3.7)

For `p>p_u`, uniqueness and FKG give `T_p(x,y)>=theta(p)^2>0` uniformly in `x,y`; such a kernel is not bounded on `ell^2` of an infinite graph. Thus

`p_{2->2}(G)<=p_u(G)`.                                            (3.8)

Combining (3.1), (3.7), (3.8), and `z<d-1` proves Theorem A.

## 4. Proof of Theorem B

Set `d=4n`, `e=6`, and choose

`z=4n-2`.

For `0<=k<=n`,

`Q=4n+5+2k`,

`a=2sqrt(4n-1)+2sqrt(5)+2k`.

For fixed `n`, the root-test margin

`L_n(k)=z+Q/z-a`

is affine in `k` with coefficient `2/z-2<0`, so its minimum on `0<=k<=n` occurs at `k=n`. At that endpoint define

`M(n)=2n-2 +(6n+5)/(4n-2)-2sqrt(4n-1)-2sqrt(5)`.                 (4.1)

At `n=8`, use the exact rational radical bounds

`sqrt(31)<39/7`, `sqrt(5)<9/4`.

Then

`M(8) > 30+53/30-78/7-9/2-16 = 13/105 >0`.                       (4.2)

For real `x>=8`,

`M'(x)=2-32/(4x-2)^2-4/sqrt(4x-1)`.                              (4.3)

Since `4x-2>=30` and `sqrt(4x-1)>=sqrt(31)>11/2`,

`M'(x) > 2-8/225-8/11 = 3062/2475 >0`.                           (4.4)

Therefore `M(n)>0` for every integer `n>=8`, proving (3.5) for every `k<=n`.

The other root requirement is also uniform in `k`: at the worst endpoint `k=n`,

`z^2-Q = (4n-2)^2-(6n+5)=16n^2-22n-1`,                          (4.5)

which is `847` at `n=8` and strictly increasing thereafter. Hence `z>sqrt(Q)`.

Finally `z=4n-2<4n-1=d-1`, so Theorem A yields

`p_c <=1/(4n-1)<1/(4n-2)<p_u`,

and subtraction gives the displayed gap. At `n=8`, the gap is exactly larger than

`1/30-1/31=1/930`.

## 5. Stronger perturbation densities

For `k<=3n/2`, the same monotonicity in `k` reduces the root test to the continuous worst-case bound `2k=3n`. The margin is

`M_{3/2}(n)=n-2 +(7n+5)/(4n-2)-2sqrt(4n-1)-2sqrt(5)`.             (5.1)

At `n=25`, using `sqrt(99)<10` and `sqrt(5)<9/4`,

`M_{3/2}(25) > 23+90/49-20-9/2 = 33/98>0`.                       (5.2)

For real `x>=25`,

`M'_{3/2}(x)=1-34/(4x-2)^2-4/sqrt(4x-1)`

`>1-17/4802-4/9=23857/43218>0`.                                  (5.3)

Thus every `n>=25` permits all integers `k<=3n/2`.

More generally let `0<epsilon<=2` and `k<=(2-epsilon)n`. Since the root-test margin decreases with `k`,

`L_n(k) >= 2epsilon n-2 + ((8-2epsilon)n+5)/(4n-2)
             -2sqrt(4n-1)-2sqrt(5)`.                             (5.4)

Dropping the positive fraction and using `sqrt(4n-1)<2sqrt(n)`, `2sqrt(5)<9/2`, gives

`L_n(k) > 2epsilon n-4sqrt(n)-13/2`.                              (5.5)

If `n>=16/epsilon^2`, then `sqrt(n)>=4/epsilon`, whence

`2epsilon n-4sqrt(n) >=16/epsilon >=8>13/2`,                     (5.6)

so the margin is positive. Also

`Q<= (8-2epsilon)n+5 <=8n+5`,

while `(4n-2)^2>8n+5` for every `n>=2`. This proves Theorem C.

The important point is asymptotic: the allowed number of **completely arbitrary** added inverse pairs can approach `2n`, whereas the large tree factor has degree `4n`.

## 6. Why this is outside the checked source families

This section records exact current source scope rather than claiming an exhaustive novelty certificate.

**Hutchcroft, arXiv:1804.10191.** Current arXiv is v3, 26 March 2019; v3 changed metadata only. The theorem is `p_c<p_u` for connected locally finite nonamenable **Gromov-hyperbolic quasi-transitive** graphs. A BMW group acting cocompactly on `T_6 x T_{4n}` is quasi-isometric to a product of two unbounded trees, hence is not a hyperbolic group; all of its finite Cayley graphs are quasi-isometric to that product. Thus the present arbitrary-perturbation Cayley graphs are not in the hyperbolic graph class.

**Hutchcroft--Pan, arXiv:2409.12283.** Current arXiv is v1, 18 September 2024. It studies nonuniqueness at `p_u` via subgroup relativization. Its sufficient obstacle-to-uniqueness classes include: (Theorem 1.13) amenable `wq`-normal subgroups having exponential growth in an ambient finite-set metric; (Theorem 1.14) nonamenable direct products; and (Theorem 1.15) property (T), more generally relative property (T) with respect to an infinite `wq`-normal subgroup.

The Radu BMW groups used here are outside those checked sufficient classes for structural reasons:

1. They act properly and cocompactly on the finite-dimensional CAT(0) cube complex `T_6 x T_{4n}`. Sageev--Wise's cubical Tits alternative implies every amenable subgroup is finitely generated virtually abelian. The Flat Torus Theorem makes such subgroups undistorted, so their intersections with ambient word balls have polynomial, not exponential, growth. Thus the Theorem 1.13 hypothesis cannot hold.
2. Proper cubical actions give the Haagerup property. A proper affine Hilbert action restricts unboundedly to every infinite subgroup, so relative property (T) with respect to an infinite subgroup is impossible. This excludes the generalized Theorem 1.15 hypothesis (and in particular property (T)).
3. Virtual simplicity excludes a decomposition as a direct product of two infinite groups: intersecting a finite-index infinite simple subgroup with each direct factor gives two infinite commuting normal subgroups of the simple subgroup. Hence Theorem 1.14 does not apply.

This makes the class genuinely outside the explicit Hutchcroft--Pan sufficient families checked in this run, rather than merely providing a new constant inside an already-listed family.

**Terlov--Timar, arXiv:2502.02560.** Current arXiv is v2, 14 September 2025. It concerns weighted/level amenability and a relaxed weighted `p_h<p_u` theorem in the nonunimodular setting; it is not an ordinary fixed-unimodular-Cayley `p_c<p_u` theorem.

**Choi--Seo, arXiv:2508.08932.** They prove a nonuniqueness phase for every Cayley graph of every acylindrically hyperbolic group. The Radu virtually simple BMW groups here are not acylindrically hyperbolic: an infinite simple finite-index subgroup is normal (take the finite-index core); infinite normal subgroups of an acylindrically hyperbolic group are acylindrically hyperbolic, while every acylindrically hyperbolic group is SQ-universal. An infinite simple group cannot be SQ-universal because its only quotients are itself and the trivial group.

The natural product markings themselves have additional product symmetry and may be accessible by older product/nonunimodular-graph methods. The counted advance here is the robust family after **arbitrary finite generator perturbations**, where that exact Cartesian-product automorphism structure need not survive. A bounded search did not locate a theorem specifically covering these arbitrary perturbations. External priority remains UNVERIFIED.

## 7. Executed checks

The final load-bearing checker is

`proofnet24/NM13-11/progress-percolation/artifacts/2026-09-20/2026-09-20T17-50-50+0300__radu-bmw-arbitrary-perturbation-final-check.py`

created at commit `d936ed999648811b1dcc7b370206ec047cb59bde`.

Its actually executed output is

`proofnet24/NM13-11/progress-percolation/artifacts/2026-09-20/2026-09-20T17-50-50+0300__radu-bmw-arbitrary-perturbation-final-check.out`

at commit `27a7f1eb212c62926ee6418d80becca2e0fb0325`, ending

`ALL_EXACT_CHECKS_PASS`.

The checker verifies exactly the `n=8` endpoint margin `13/105`, derivative lower bound `3062/2475`, gap `1/930`, the `k<=3n/2,n>=25` endpoint margin `33/98` and derivative lower bound `23857/43218`, plus high-precision stress tests for several values in the asymptotic density theorem. The finite decimal grid is a sanity check only; the proof is the exact symbolic argument above.

## 8. Residual obstruction and next attack

This run avoids the previous fixed-`(12,8)` five-pair wall by increasing the base tree degree. It does **not** solve five arbitrary pairs on the original Rattaggi `(12,8)` marking, and it does not approach arbitrary fixed Cayley graphs of BMW groups that do not visibly retain a high-degree tree factor in the marking. Those remain UNKNOWN.

The next materially distinct route should therefore target generator sets not containing the full product neighbor marking. Two plausible mechanisms are: a comparison that extracts a high-branching tree minor/subgraph from a coarsened natural block without requiring all standard edges, or a colored nonbacktracking estimate that uses the horizontal/vertical product decomposition at operator level even after some standard generators are replaced rather than merely added. Repeating deeper fibre calculations on the fixed `(12,8)` base is no longer the right next move.

## ledger_delta

- `parent`: T09 Benjamini--Schramm iid bond-percolation nonuniqueness conjecture.
- `universal_status_before`: OPEN.
- `universal_status_after`: OPEN.
- `before_scope`: arbitrary four-pair augmentations of one `(12,8)` BMW product marking; five arbitrary pairs on that fixed base UNKNOWN.
- `after_scope`: abstract BMW criterion; Radu virtually simple `(6,4n)` family with every `n>=8` and every `k<=n` arbitrary added inverse pairs; endpoint `n=8,k=8` has `p_c<=1/31<1/30<p_u`; every `n>=25` allows `k<=3n/2`; for every fixed `epsilon>0`, all `n>=ceil(16/epsilon^2)` allow `k<=(2-epsilon)n`.
- `source_level_gap`: `p_u-p_c > 1/((4n-2)(4n-1))`; endpoint gap `>1/930`.
- `mechanism_advance`: exploit linear branching of a retained high-degree tree against square-root product adjacency norm, leaving a linear arbitrary-generator spectral budget; complete transfer through nonbacktracking `p_{2->2}` and FKG uniqueness.
- `checked_source_exclusions`: outside arXiv:1804.10191 hyperbolic graphs; outside the explicit arXiv:2409.12283 Theorems 1.13--1.15 sufficient families by cubical Tits alternative/undistortion, Haagerup vs relative-(T), and virtual simplicity; arXiv:2502.02560 is weighted rather than ordinary target; outside Choi--Seo acylindrically-hyperbolic all-Cayley class by virtual simplicity/SQ-universality.
- `proof_status`: CANDIDATE_FULL for Theorems A--C pending independent review; external priority UNVERIFIED.
- `checker_commit`: `d936ed999648811b1dcc7b370206ec047cb59bde`.
- `executed_output_commit`: `27a7f1eb212c62926ee6418d80becca2e0fb0325`.
- `residual`: arbitrary replacement/non-product markings, and five arbitrary pairs on the fixed `(12,8)` base, remain UNKNOWN.
