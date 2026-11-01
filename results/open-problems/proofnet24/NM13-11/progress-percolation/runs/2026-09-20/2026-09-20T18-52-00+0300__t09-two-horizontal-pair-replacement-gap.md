Runtime model: **GPT-5.6 Sol**. Reasoning effort: **UNVERIFIED**.

# NM13-11 / T09 — arbitrary replacement of two standard horizontal pairs on a `(12,8)` BMW marking

Status: **PARTIAL / CANDIDATE_FULL for the restricted theorem below; universal T09 remains OPEN.** The load-bearing arithmetic was executed with exact rational arithmetic and archived in this run. No independent review has occurred. Exact worldwide priority is **UNVERIFIED**.

## 1. Parent target, controlling scope, and compact handoff

The parent Benjamini--Schramm target is:

> For iid bond percolation on every locally finite Cayley graph `G` of every finitely generated nonamenable group, prove `p_c(G)<p_u(G)`.

The controlling policy is `operations/PROGRESS20_2026-09-20.md`. LIVE20 assigns NM11 to T09 under `proofnet24/NM13-11/progress-percolation/`. `POSTED.md` does not close the universal target; it explicitly preserves restricted percolation results as restricted. The neighboring PROB10-09 worker remains in the quotient/extension/vertical-kernel lane and has explicitly left the Rattaggi/BMW product-fibre lane to NM13-11, so this run does not overwrite peer ownership.

The latest own substantive predecessor was

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T17-50-50+0300__t09-radu-bmw-linear-arbitrary-perturbations.md`.

The immediately preceding fixed `(12,8)` result was

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T17-25-00+0300__t09-two-seed-arbitrary-four-pairs-gap.md`,

which proved a positive gap after **adding** four arbitrary inverse pairs while retaining the whole standard product marking.

Preserved earlier Benjamini--Schramm attempts include finite-set escape/BK last-exit, killed-SAW and susceptibility-weighted boundary energy, global `ell^2` SAW, scalar nonbacktracking polynomials, product/tree stress tests, quotient/fibre-shell and bridge criteria, followed by the September free-core, triangle-fibre, S-arithmetic, Rattaggi augmentation, power-layer, factor-branching, pure-torsion and multiseed-fibre constructions. Routes that produced only auxiliary inequalities without a complete `p_c`-to-`p_u` transfer remain mechanism history, not source-level results.

### Important source-status correction to the preceding Radu report

The high-degree Radu perturbation theorem in the 17:50 report is mathematically valid as a restricted theorem, but its novelty classification was too broad. Hutchcroft's 2022 `L^2`-boundedness paper (`arXiv:1904.05804`, published in PLMS 2022) explicitly states that the `L^2` condition applies to transitive graphs of normalized spectral radius `rho<1/2`. For the Radu subfamily with `k=n`, our own bound

`rho <= [2 sqrt(4n-1)+2 sqrt(5)+2n]/(6n+6)`

is already `<1/2` for every `n>=19`. Those parameter regimes therefore must **not** be counted as new source-level `p_c<p_u` cases. The finite theorem remains useful as a quantitative derivation, but the already-covered asymptotic region is demoted here. This correction is additive; no historical report is overwritten.

That issue motivates the present run: move from **augmentation** to **replacement**, where the full product graph is no longer retained and the available normalized-adjacency upper bound is far above `1/2`.

## 2. Original-problem before/after, separate from mechanism progress

### Before

On the Rattaggi/BMW lane, every complete arbitrary-perturbation theorem retained the full standard `(12,8)` neighbor marking and only added new generators. The track had no complete theorem allowing standard product generators to be deleted and replaced by arbitrary generators while still proving `p_c<p_u`.

### After

Let `Gamma` be any BMW group acting simply transitively on the vertices of `T_12 x T_8`, with natural symmetric neighbor marking

`S_0=A sqcup B`, `|A|=12`, `|B|=8`,

where `A` consists of horizontal neighbors and `B` of vertical neighbors. Choose any symmetric four-element set `R subset A` and put `A'=A\R`, so `|A'|=8`. Let `C` be **any** symmetric four-element subset of `Gamma` disjoint from `A' sqcup B` and from the identity, with arbitrary relations, subject only to the final set

`S=A' sqcup B sqcup C`

being a simple generating set. Then for

`G=Cay(Gamma,S)`

we prove

`boxed( p_c(G) < 3/40 < 19/250 < p_u(G) )`

and hence

`boxed( p_u(G)-p_c(G) > 1/1000 ).`

Equivalently, on Rattaggi's standard `(12,8)` marking one may delete **any two standard horizontal inverse generator pairs** and replace them by **any two arbitrary new inverse pairs**, provided the resulting symmetric set generates. The replacement pairs may have arbitrary relations with each other and with the retained generators.

This is a fixed-graph/source-level expansion from addition-only robustness to deletion-and-replacement robustness. These graphs generally do **not** contain the original `T_12 square T_8` Cayley graph as a spanning subgraph.

**Original-problem delta:** universal T09 remains OPEN. A genuinely new replacement class on the same nonhyperbolic product-lattice ambient group now has a certified positive gap `>10^{-3}`.

**Mechanism delta:** the critical comparison no longer needs the retained marked subgraph itself to be a Cartesian product. It only needs (i) an 8-regular horizontal tree component inside each horizontal fibre and (ii) all eight vertical geometric edges. A finite-radius fibre Galton--Watson process survives arbitrary twisting of horizontal labels across fibres.

## 3. General finite-radius fibre replacement lemma

The following is the mechanism actually used.

Let `Gamma` act simply transitively on `T_d x T_e` with the natural horizontal/vertical marking `A sqcup B`, `|A|=d`, `|B|=e`. Retain a symmetric subset `A' subset A` of cardinality `h>=2` and retain **all** of `B`. Add an arbitrary finite symmetric set `C`, disjoint from the retained marking, and suppose the final set generates `Gamma`.

Inside each geometric horizontal fibre `T_d x {v}`, the `A'`-edge graph is `h`-regular and acyclic, hence every component is a copy of `T_h`. This does not require `A'` to be invariant under the vertical local action. The full set `B` is retained, so from every vertex in a fibre there is exactly one retained vertical edge to each of the `e` neighboring geometric fibres.

Fix radius `R>=1` and a percolation parameter `p`; put `s=1-p`. Define

`u_0=s`,

`u_{j+1}=s(s+p u_j)^(h-1)`,

and

`C_R=s(s+p u_{R-1})^h`.

If `Z_R` is the size of the radius-`R` open cluster of a seed in its retained horizontal `T_h` component, then

`C_R=E[s^(Z_R)]`.

Root the geometric `T_e` factor. A particle in fibre `v` exposes its radius-`R` horizontal cluster. For each of the `e-1` forward neighboring fibres `w`, expose all vertical edges from that cluster into `w`; if at least one is open, retain one endpoint as a child seed. Conditional on `Z_R`, the success probability in each forward direction is `1-s^(Z_R)`, and the edge sets for different directions are disjoint. Distinct particles occupy distinct fibres of the rooted `T_e`, so all horizontal and crossing edge sets used by different particles are disjoint.

Thus this is an honest Galton--Watson subprocess with mean

`m_R(p)=(e-1)(1-C_R)`.

Consequently,

`m_R(p)>1  ==>  p_c(Cay(Gamma,A' sqcup B sqcup C)) < p`,

where strictness follows by continuity of the finite polynomial `m_R` and monotonicity under the ignored `C`-edges.

For the uniqueness side, let `c=|C|` and let

`kappa=||sum_{x in C} R_x||_{2->2}`.

The retained `A'`-operator is a direct sum of `T_h` adjacency operators, hence has norm exactly `2 sqrt(h-1)`. The full vertical operator has norm `2 sqrt(e-1)`. Therefore

`||A_G|| <= 2 sqrt(h-1)+2 sqrt(e-1)+kappa <= 2 sqrt(h-1)+2 sqrt(e-1)+c`.

Writing `D=h+e+c`, `Q=D-1`, any `z>sqrt(Q)` satisfying

`z+Q/z > 2 sqrt(h-1)+2 sqrt(e-1)+kappa`

gives, by the regular nonbacktracking recurrence and the shortest-open-path bound,

`p_{2->2}(G)>1/z`.

As in the earlier reports, uniqueness plus FKG implies `p_{2->2}(G)<=p_u(G)`. Hence if the finite-radius critical test also gives `p_c<p<1/z`, then `p_c<p_u` with an explicit gap.

This is a complete percolation transfer, not an auxiliary operator inequality.

## 4. Specialization: replace two horizontal pairs on `(12,8)`

Set

`d=12`, `e=8`, `h=8`, `c=4`, `D=20`, `Q=19`.

### 4.1 Critical side

Take

`p=3/40`, `s=37/40`, `R=3`.

The exact recursion is

`u_0=s`,

`u_1=s(s+p u_0)^7`,

`u_2=s(s+p u_1)^7`,

`C_3=s(s+p u_2)^8`,

and

`m_3=7(1-C_3)`.

The exact rational checker proves

`m_3 = 1.004037088083701031899859385... > 251/250 >1`.

Therefore, by continuity, there exists `p'<3/40` with `m_3(p')>1`, so the Galton--Watson subprocess percolates and

`boxed( p_c(G)<3/40 ).`

Notice what is and is not being used: the four replacement edges are ignored on the critical side, but unlike the previous augmentation theorems the four deleted standard horizontal edges are genuinely absent. The retained horizontal components have only degree eight.

### 4.2 Uniqueness side

The operator norm satisfies

`||A_G|| <= 2 sqrt(7)+2 sqrt(7)+4 = 4 sqrt(7)+4`.

Use the exact rational radical bound

`sqrt(7)<127/48`,

which gives

`||A_G|| < 175/12`.

Take

`z=250/19`.

The checker verifies exactly

`z^2-19 = 55641/361 >0`

and

`z+19/z-175/12 = 529/28500 >0`.

Hence the nonbacktracking `ell^2` growth exponent is strictly smaller than `z`, and

`p_{2->2}(G)>19/250`.

Since `p_{2->2}<=p_u`,

`boxed( p_u(G)>19/250 ).`

Combining the two sides,

`p_u(G)-p_c(G) > 19/250-3/40 = 1/1000`.

The actual executed checker is

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T18-52-00+0300__t09-horizontal-replacement-check.py`

at commit `9b12e680122b3f68060eeee0b0fe778810abeec0`. Its executed output is

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T18-52-00+0300__t09-horizontal-replacement-check.out`

at commit `07c24f9f9bdb147e43edf696c49885dd60656708`, ending `ALL_EXACT_CHECKS_PASS`.

## 5. Weakening of the extra hypotheses

The proof is stronger than the two-pair phrasing.

1. **No algebra on replacements.** `C` is only required to be a symmetric four-element set making the final marking simple and generating. It need not be free, torsion-free, a subgroup basis, aligned with either tree factor, or independent of the retained generators.

2. **No Cartesian retained subgraph.** Deleting horizontal labels may destroy the marked Cartesian-product structure. The critical proof uses only the geometric fibre map inherited from the BMW action, the acyclicity/regularity of the retained horizontal components, and retention of all vertical neighbors.

3. **General operator version.** For any `h,e,c,R`, the same finite-radius branching formula and operator condition above give a complete gap criterion with `kappa` in place of the crude cardinality cost `c`. Thus arbitrary larger replacement sets are allowed whenever their regular-representation operator norm is small enough and the nonbacktracking inequality remains strict.

4. **Up to four horizontal labels.** On the `(12,8)` base, the same `p_c<3/40` critical certificate remains valid whenever at most four horizontal labels are deleted, since the retained horizontal fibre contains an 8-regular subtree. The uniqueness bound is worst at four deletions/four arbitrary replacements among equal-cardinality replacements, so the displayed theorem also covers every smaller equal-cardinality replacement allowed by symmetry.

These weakenings are tied to the demonstrated percolation transfer above; they are not being counted as free-standing inequalities.

## 6. A materially different failed route preserved in this run

The unresolved degree-seven pure-torsion construction from the earlier `C_3*C_3*C_3` block was also tested with a colored run decomposition rather than the scalar nonbacktracking recurrence. Let `H=C_3*C_3*C_3` with its six nontrivial factor generators. Its adjacency norm is `5`, and the norm-generating function for nonbacktracking `H`-runs is bounded by

`G(x)=(1-x^2)/(1-5x+5x^2)`.

Alternating such runs with the seventh involution gives the renewal convergence condition

`x(G(x)-1)<1`,

whose boundary reduces exactly to

`6x^3-5x+1=0`.

The smallest positive root is

`x=(3-sqrt(3))/6 = 1/(3+sqrt(3)) = 0.2113248654...`,

which is exactly the old scalar bound. Thus this natural colored decomposition produces **no gain** toward the missing pure-torsion degree-seven endpoint `p_c approx 0.214003...`. It is preserved as a failed route rather than presented as progress.

## 7. Exact current source scopes

### Hutchcroft, arXiv:1804.10191

Current arXiv is **v3, last revised 26 March 2019**; the arXiv record says v3 changed metadata only. It proves `p_c<p_u` for connected, locally finite, nonamenable, **Gromov-hyperbolic quasi-transitive** graphs. The Rattaggi/BMW group is quasi-isometric to a product of two unbounded trees and is not Gromov hyperbolic, so this theorem does not cover its Cayley graphs.

### Hutchcroft--Pan, arXiv:2409.12283

Current arXiv is **v1, 18 September 2024**. It studies behavior **at `p_u`** via subgroup relativization; the abstract gives nonuniqueness at `p_u` for groups containing an amenable `wq`-normal subgroup of exponential growth and a co-heredity theorem. The body also contains broader obstacle-to-uniqueness results discussed in earlier reports. These are endpoint-`p_u` statements and do not themselves provide the strict fixed-graph `p_c<p_u` separation proved here.

### Terlov--Timár, arXiv:2502.02560

Current arXiv is **v2, last revised 14 September 2025**. It concerns weighted/level amenability in the nonunimodular setting and proves a relaxed weighted `p_h<p_u` result à la Pak--Smirnova-Nagnibeda, not the ordinary unimodular fixed-Cayley `p_c<p_u` target.

### Other checked coverage relevant to novelty classification

Hutchcroft's PLMS 2022 `L^2`-boundedness paper applies in particular to transitive graphs of normalized spectral radius `<1/2`; as noted above, this invalidates counting some large-degree Radu regimes as new. For the present replacement theorem, the available uniform adjacency estimate is

`||A_G||/20 <= (4 sqrt(7)+4)/20 approx 0.72915`,

so the small-spectral-radius corollary is **not** verified uniformly for this class. This does not prove that every member has spectral radius at least `1/2`; it means the checked theorem does not cover the replacement class from the available structural data. Exact worldwide priority remains UNVERIFIED.

Choi--Seo, arXiv:2508.08932 (2025), prove `p_c<p_u` for every Cayley graph of every acylindrically hyperbolic group. Rattaggi constructs an index-four finitely presented torsion-free simple subgroup `Sigma_0` of `Sigma<Aut(T_12)xAut(T_8)`. The standard finite-index/SQ-universality argument retained in this track excludes this ambient group from the acylindrically-hyperbolic class: an acylindrically hyperbolic finite-index simple subgroup would be SQ-universal, while the torsion-free simple `Sigma_0` has no nontrivial quotient capable of containing, for example, nontrivial torsion groups. Thus Choi--Seo does not supply an all-Cayley theorem here.

A bounded current search found no theorem specifically covering arbitrary two-pair **replacement** markings of this Rattaggi/BMW group. This is not an exhaustive priority certificate.

## 8. Residual obstruction and next attack

The next symmetric replacement step removes three horizontal inverse pairs, i.e. six oriented horizontal labels. Then the retained critical-side graph has degree only `6+8=14`. Any comparison that **ignores the replacement edges on the critical side** cannot certify below the universal degree bound `1/(14-1)=1/13 approx 0.076923`, while the same crude arbitrary-replacement operator estimate gives a scalar nonbacktracking `p_u` floor only about `0.06921`. Therefore the present architecture cannot reach three-pair replacement merely by increasing fibre depth.

The next attack must do one of two materially different things:

- make the replacement edges participate in a collision-controlled finite-state branching process, or
- obtain a relation/position-sensitive uniqueness estimate substantially sharper than charging the entire replacement operator by cardinality.

Three-pair arbitrary replacement is **UNKNOWN**, not negative.

## 9. ledger_delta

```yaml
ledger_delta:
  task: T09
  parent_status_before: OPEN
  parent_status_after: OPEN
  source_metric_before: "no complete arbitrary deletion-and-replacement theorem on the fixed (12,8) BMW marking"
  source_metric_after: "delete any two standard horizontal inverse pairs, replace by any two arbitrary inverse pairs (final marking simple/generating): pc < 3/40 < 19/250 < pu, gap > 1/1000"
  mechanism_advance: "finite-radius horizontal-fibre Galton-Watson survives arbitrary label twisting after pruning; combined with exact retained-tree operator norms and regular nonbacktracking transfer"
  corrected_prior_scope: "large-n Radu regimes whose own norm bound gives normalized rho<1/2 are already covered by Hutchcroft's 2022 L2 condition and are not counted as new source-level cases"
  exact_check: "PASS; executed Fraction arithmetic; output ends ALL_EXACT_CHECKS_PASS"
  failed_route: "colored H-run renewal for degree-7 C3*C3*C3 plus involution reproduces exactly the old 1/(3+sqrt(3)) scalar threshold"
  candidate_status: CANDIDATE_FULL_RESTRICTED
  universal_closure: false
  external_priority: UNVERIFIED
  next_obstruction: "three-pair arbitrary horizontal replacement; base-only critical comparison cannot cross the coarse uniqueness floor"
```
