Runtime model/effort: **UNVERIFIED**. GPT-6 maximum was requested, but no authenticated runtime model/effort telemetry or writable model/effort selector is exposed, so this report does not claim GPT-6 maximum. **Source status OPEN -> OPEN; PROB10-07 structural-family metric moves from complete bipartite graphs `K_{a,b}` with `min(a,b)<=9` to `min(a,b)<=30`, with the other side arbitrary; historical complete-all-graphs order metric remains `9 -> 9`.**

# PROB10-07 — symmetry-quotient Rayleigh certificates for `K_{m,n}`, widths 10 through 30

Repository/branch: private `yspennstate/math-open-problems` / `master`  
Parent: Grimmett–Winkler pairwise negative correlation for the uniform measure on **all forests**  
Status: **PARTIAL / universal conjecture OPEN**  
Artifact stem: `20260920T0234Z_integer-partition-quotient`

## 1. Continuity, ownership and evidence consumed

Before the new argument I read the current PROB10 contract and posting exclusions, the complete latest historical forest-owner handoffs, the newest own report, and the current same-parent structural follow-ups:

- `operations/PROB10_2026-09-20.md`;
- `POSTED.md`;
- `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T05-19-47Z__mandatory-handoff-report.md`, blob `bed2241d948b8a20b854efc248ccf5b46b4325cd`;
- `proofnet24/HARD10-01/runs/2026-09-16/2026-09-16T21-16-42Z__report.md`, the HARD10 handoff after the same source metric stalled at 9;
- own predecessor `runs/prob10_2026-09-20/PROB10-07/20260920T0133Z_k6789-transfer-a41f.md`, which proved the complete-bipartite widths `6,7,8,9` after the earlier `3,4,5` widths;
- `proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T02-18-30Z__split5-portfield-sign-theorem.md`, which owns split-graph / port-field atom work;
- `proofnet24/NM13-08/progress-forest-structure/runs/2026-09-20/2026-09-20T01-39-00Z__portfield-sp-macronetwork-report.md`, which owns the two-terminal PF series/parallel macro-decomposition route;
- preserved R13 refocus handoff `runs/R13/20260919T2345Z_handoff-to-PROB10-07-forest.md`;
- forest-owner handoff `artifacts/prob10_2026-09-20/PROB10-07/20260919T2347Z_forest-owner-handoff.md`.

There is no claim collision. P14/HARD10-01 own the complete graph-order census through nine, the 3-connected minimal-counterexample reduction, and the generic three-terminal obstruction. NM13-04/NM13-08 own the split/port-field and two-terminal substitution directions. This run stays on PROB10-07's distinct complete-bipartite transfer family and does not repeat graph-order enumeration.

The exact mathematical idea was written before the production checker in

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0234Z_integer-partition-quotient-idea.md`.

Its creation-before-code commit is `e669054865ffb0fc3419c3d805d1ef4ce6bbce9f`; a later wording correction (`both` -> `neither` in the same-left-star explanation) is commit `9e0c2cbf6b0883e626d4341c85ffe6807fe04ad6`. The mathematical formula and production checker were unchanged by that wording correction.

## 2. Exact source target and before/after metric

For a finite graph `G=(V,E)`, select uniformly from all acyclic subsets `F subseteq E`, retaining the full vertex set and allowing every component count. The source asks, for every distinct pair `e,f`,

\[
\Pr(e,f\in F)\le \Pr(e\in F)\Pr(f\in F).
\tag{2.1}
\]

This is not the uniform-spanning-tree law, random minimum spanning trees, or a fixed-component forest ensemble.

The preceding PROB10-07 report certified (2.1) for every `K_{m,n}` with `3<=m<=9` and every `n>=1`. This run proves:

### Theorem `PROB10-07-KMN-IPART-30`

For every integer

\[
10\le m\le30,
\qquad n\ge1,
\]

the uniform measure on all forests of `K_{m,n}` satisfies (2.1). For `n>=2` the inequality is strict for every distinct edge pair. For `n=1`, `K_{m,1}` is a tree and equality holds.

By bipartite symmetry and the already certified smaller widths, the combined exact family statement is

\[
\boxed{\text{every }K_{a,b}\text{ with }\min(a,b)\le30.}
\tag{2.2}
\]

The all-graphs finite-order metric remains `9 -> 9`. No list of complete bipartite graphs is being promoted as a proof of the universal conjecture.

## 3. Three materially different approaches compared

### Route A — quotient by the terminal permutation group: succeeded

The old transfer used all set partitions of the `m` left terminals, hence `B_m` Bell states. Once marked right vertices are placed first, every remaining right vertex is unmarked and the transfer commutes with the full `S_m` action. The correct state is therefore only the multiset of block sizes, i.e. an integer partition of `m`. This reduces `B_m` states to `p(m)` states: in particular `p(10)=42`, `p(20)=627`, `p(30)=5604`.

This quotient is exact and is the main new mechanism.

### Route B — continue the old unshifted coefficientwise positivity: exactly falsified

For widths through 14, the disjoint-pair Rayleigh polynomial also happens to have positive ordinary `n`-power coefficients. At width 15 this certificate form fails: the exact constant coefficient of the normalized disjoint-pair polynomial is

\[
-\frac{126638194577404627495822599}
{316912650057057350374175801344}<0.
\tag{3.1}
\]

This does **not** refute negative correlation. It refutes the tempting all-width claim that ordinary unshifted power-basis positivity is the reason. Shifting to the physical variable `x=n-2>=0` restores a manifest certificate through width 30.

### Route C — scalar deletion/contraction induction in the newest right vertex: does not close

Adding one right vertex is a legal-star deletion/contraction sum, but the Rayleigh scalar after the addition contains cross terms between different terminal-connectivity states. A single scalar gap is not an invariant closed under the update. The successful integer-partition transfer is a finite vector-valued replacement of that failed scalar induction. I make no generic deletion/contraction closure claim outside this family.

## 4. Exact integer-partition transfer

Fix `m`. Process right vertices one at a time. A partial forest induces a partition of the left terminals `[m]`; by symmetry only its block sizes matter. Write the resulting integer partition as

\[
\lambda=(s_1,\ldots,s_b),\qquad \sum_i s_i=m.
\]

For a new right vertex, choose its spoke set. Since the current graph is a forest, adding the star is acyclic iff it contains at most one vertex from each current block. If it hits a collection `J` of blocks with `|J|>=2`, those blocks merge and the transition is

\[
(s_1,\ldots,s_b)
\longmapsto
\operatorname{sort}\Bigl(\{s_i:i\notin J\}\cup\{\sum_{i\in J}s_i\}\Bigr).
\tag{4.1}
\]

For fixed labelled blocks `J`, the number of spoke sets inducing this transition is

\[
\prod_{i\in J}s_i,
\tag{4.2}
\]

because the new star chooses one vertex from each hit block. If a block size `s` occurs `c_s` times and the transition hits `r_s` of them, orbit aggregation gives the exact multiplicity

\[
\boxed{
\prod_s {c_s\choose r_s}s^{r_s}.}
\tag{4.3}
\]

The empty spoke set and the `m` singleton spoke sets preserve every state. Therefore the quotient transfer matrix satisfies

\[
M_m=(m+1)I+N_m.
\tag{4.4}
\]

Every nonzero transition of `N_m` strictly reduces the number of blocks, hence

\[
\boxed{N_m^m=0.}
\tag{4.5}
\]

Consequently, for every nonnegative integer `k`,

\[
M_m^k=
\sum_{j=0}^{m-1}{k\choose j}(m+1)^{k-j}N_m^j.
\tag{4.6}
\]

This is the same nilpotent mechanism as the Bell-state transfer, but on the exact `S_m` orbit quotient.

## 5. Exact marked initial vectors

There are exactly three pair orbits in `K_{m,n}`: two edges sharing their right endpoint (`R`), sharing their left endpoint but with different right endpoints (`L`), or vertex-disjoint (`D`). By automorphism symmetry, one count for each orbit suffices.

Put the marked right vertex or vertices first. Let `e_lambda` denote the basis vector of the integer-partition state `lambda`, and write

\[
\lambda_k=(k,1^{m-k}),
\]
with `lambda_1=(1^m)`.

The five initial vectors for the total count `Z`, one-edge count `E`, and pair counts `R,L,D` are as follows.

### Total

\[
v_Z=e_{(1^m)}.
\tag{5.1}
\]

### One marked edge

For `e=(0,R_1)`, a marked star of size `k` contains terminal `0` and any `k-1` of the other terminals, so

\[
\boxed{
v_E=\sum_{k=1}^m {m-1\choose k-1}e_{\lambda_k}.}
\tag{5.2}
\]

### Same-right pair

For `(0,R_1),(1,R_1)`,

\[
\boxed{
v_R=\sum_{k=2}^m {m-2\choose k-2}e_{\lambda_k}.}
\tag{5.3}
\]

### Same-left pair

For `(0,R_1),(0,R_2)`, the two marked stars share terminal 0. Any other touched terminal may be in the first star or the second star but not both, since a second common terminal would create a 4-cycle. Hence

\[
\boxed{
v_L=\sum_{k=1}^m {m-1\choose k-1}2^{k-1}e_{\lambda_k}.}
\tag{5.4}
\]

### Disjoint pair

Take `(0,R_1),(1,R_2)`. Let the first marked star be `S`, with `0 in S`; the second is `T`, with `1 in T`. After the first star, `S` is one connectivity block, so legality of the second requires

\[
|T\cap S|\le1.
\tag{5.5}
\]

If `1 in S`, then `T` already hits `S` at 1 and cannot hit it elsewhere. For final one-block size `k>=2`, choose the other `k-2` union vertices and assign each to `S` or `T`, giving

\[
{m-2\choose k-2}2^{k-2}
\tag{5.6}
\]

copies of `e_{lambda_k}`.

If `1 notin S`, put `s=|S|`. There are `{m-2\choose s-1}` choices for `S`. Let `u>=1` encode the second star's vertex `1` plus `u-1` vertices outside `S union {1}`. If `T` avoids `S`, the final marked connectivity has two blocks of sizes `s,u`, with multiplicity

\[
{m-2\choose s-1}{m-s-1\choose u-1}.
\tag{5.7}
\]

If `T` hits `S` once, there are `s` choices for that hit and the two marked pieces merge into a block of size `s+u`, with multiplicity

\[
{m-2\choose s-1}s{m-s-1\choose u-1}.
\tag{5.8}
\]

Equations (5.6)-(5.8) are the exact `O(m^2)` construction of `v_D` implemented in the checker.

As an independent regression of this quotient logic, the production checker reconstructs the five nilpotent coefficient vectors for `m=6,7,8,9` and requires exact equality with the already archived full Bell-state vectors from the preceding PROB10-07 checker. All four regressions pass.

## 6. Exact Rayleigh polynomials

Set

\[
q=m+1.
\]

For `X in {Z,E,R,L,D}`, define

\[
x_j=v_XN_m^j\mathbf1.
\]

Write the corresponding coefficient vectors as `a_j,b_j,c_j,l_j,d_j`. From (4.6), after division by `q^n`,

\[
\frac{Z}{q^n}=\sum_{j=0}^{m-1}a_j\frac{{n\choose j}}{q^j},
\tag{6.1}
\]

\[
\frac{E}{q^n}=\frac1q\sum_{j=0}^{m-1}b_j\frac{{n-1\choose j}}{q^j},
\qquad
\frac{R}{q^n}=\frac1q\sum_{j=0}^{m-1}c_j\frac{{n-1\choose j}}{q^j},
\tag{6.2}
\]

and, for `n>=2`,

\[
\frac{L}{q^n}=\frac1{q^2}\sum_{j=0}^{m-1}\ell_j\frac{{n-2\choose j}}{q^j},
\qquad
\frac{D}{q^n}=\frac1{q^2}\sum_{j=0}^{m-1}d_j\frac{{n-2\choose j}}{q^j}.
\tag{6.3}
\]

For `Q in {R,L,D}`, define the normalized Rayleigh numerator

\[
\delta_Q(n)=\frac{E^2-ZQ}{q^{2n}}.
\tag{6.4}
\]

Since `Z>0`, the source probability gap is

\[
\Pr(e)\Pr(f)-\Pr(e,f)=\frac{E^2-ZQ}{Z^2},
\tag{6.5}
\]

so it has the sign of `delta_Q`.

The exact checker expands (6.1)-(6.4) in rational arithmetic. For each integer `m=10,...,30` it proves the following stronger finite certificate. Put

\[
x=n-2.
\]

Then there are rational polynomials `P_{R,m},P_{L,m},P_{D,m}` **all of whose coefficients are strictly positive** such that

\[
\boxed{
\delta_R(n)=(n-1)P_{R,m}(n-2),
\quad
\delta_L(n)=P_{L,m}(n-2),
\quad
\delta_D(n)=P_{D,m}(n-2).
}
\tag{6.6}
\]

The degrees are respectively

\[
2m-3,\quad 2m-4,\quad 2m-4.
\tag{6.7}
\]

For every physical `n>=2`, `x>=0`; therefore every right-hand side in (6.6) is strictly positive. At `n=1`, `K_{m,1}` is a tree and the uniform forest law is simply independent Bernoulli-`1/2` on the tree edges, so equality holds. This completes the proof of `PROB10-07-KMN-IPART-30`.

The checker does not hide sign decisions behind floating point. It stores every coefficient as a `Fraction`, asserts strict positivity coefficient-by-coefficient, and prints a SHA-256 digest of the exact numerator/denominator table for each width. The master digest for widths 10 through 30 is

`6bd93c4ee9af251f8652a8d2279e5e634abda7c095b3a7013d277d189a277ed1`.

At the endpoint `m=30`, the quotient uses 5604 states rather than `B_30` labelled partitions; the exact shifted degrees are `57,56,56` and every coefficient is positive.

## 7. Exact obstruction to the naive old certificate

The same executable search asks when the *unshifted* ordinary `n`-power coefficients cease to be all positive. The first failure in the disjoint-pair polynomial is exactly `m=15`, where the constant coefficient is (3.1). Thus the previous positive-power-basis pattern through small widths is not a valid all-width structural theorem. The successful shift `x=n-2` is not cosmetic: it aligns the positivity basis with the actual domain for the two-right-vertex pair types.

This is an auxiliary mechanism gain, not a counterexample to Grimmett–Winkler.

## 8. Checker, execution and readback

Production checker:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0234Z_integer-partition-quotient_checker.py`

creation commit `61a73875bd2643afe1409d7938be2a33d2d81337`, read back at that exact commit; blob `19d461695a9c91bf408576450b86c2a43d332559`.

Executed archived output:

`artifacts/prob10_2026-09-20/PROB10-07/20260920T0234Z_integer-partition-quotient_checker.out`

creation commit `c5f30c88c75938f7832413f27686ce9251f3f77b`, read back at that exact commit; blob `88ef2d448afc3f6ec637e1206a188dafcddd47d7`.

The output ends

`PROB10_07_INTEGER_PARTITION_QUOTIENT_10_30_EXACT_PASS`.

The execution also prints all per-width state counts, minimum exact shifted coefficients, and coefficient-table digests.

This is a **self-check**, not an independent audit.

## 9. Current literature/source reconciliation

Fresh bounded source checks on 20 September 2026 retain the following scope distinctions.

- Grimmett–Winkler, `https://arxiv.org/abs/math/0302185`, is the exact uniform-all-forests source and reports the original finite verification through eight vertices plus the sparse nine-vertex sector.
- Erickson, `https://arxiv.org/abs/1008.3660`, proves the stronger weighted independent-set-Rayleigh property for series-parallel graphs; `K_{m,n}` with both parts at least 3 lies outside the series-parallel class.
- Tang–Zhang, `https://arxiv.org/abs/2603.10738`, concerns specified complete-graph ensembles, including forests with a **fixed** number of components for fixed `k` and sufficiently large ambient size. It is not the arbitrary-component uniform forest law on `K_{m,n}`.
- Bado's 2026 wheel theorem proves another 3-connected non-series-parallel family using a `2 x 2` transfer matrix; it is not a complete-bipartite theorem.

Bounded searches for combinations of `uniform forest`, `complete bipartite`, `K_{m,n}`, `negative correlation`, and `Rayleigh` did not surface this exact complete-bipartite family theorem or the integer-partition quotient certificate. That is only negative search evidence. **Novelty/priority remains UNVERIFIED.**

The owner's random-cluster parameter-nonmonotonicity paper is a different posted/personal object and supplies no source closure here.

## 10. Source-level accounting and remaining full-scope gap

```yaml
ledger_delta:
  track: PROB10-07
  parent_source: "Grimmett-Winkler uniform-all-forests pairwise edge negative correlation"
  source_status_before: OPEN
  source_status_after: OPEN
  structural_family_metric_before: "K_{a,b} with min(a,b)<=9, other side arbitrary"
  structural_family_metric_after: "K_{a,b} with min(a,b)<=30, other side arbitrary"
  newly_proved_widths: "m=10,...,30, all n>=1"
  strict_range: "n>=2"
  complete_all_graphs_order_before: 9
  complete_all_graphs_order_after: 9
  verified_counterexample: NONE
  mechanism_gain: "exact S_m quotient from Bell partitions to integer partitions; shifted x=n-2 positive-coefficient certificates"
  exact_obstruction: "unshifted disjoint-pair power-basis positivity first fails at m=15 via negative constant coefficient"
  checker: PASS
  independent_audits_of_new_theorem: "0/2"
  novelty: UNVERIFIED
```

The full-scope gap is still enormous: nothing here controls an arbitrary 3-connected graph, the generic three-terminal response obstruction from P14 is untouched, and no source-valid counterexample has been found. The correct status is therefore **OPEN / PARTIAL**, not PROVED.

## 11. Best next mathematical direction

Do not merely push the exact width cutoff from 30 to another finite number. The quotient has now exposed a more valuable question: prove symbolically, for arbitrary `m`, that the three physical-domain polynomials in (6.6) have nonnegative coefficients (or find the first exact width where the shifted certificate fails). The unshifted failure at `m=15` shows that the basis matters. A genuine all-`m` positivity theorem would settle **every complete bipartite graph** at once and would be a qualitatively stronger structural result than another finite-width computation.

A second nonduplicating route is to identify a combinatorial interpretation for the shifted coefficients in terms of ordered mergers of terminal blocks. If such an interpretation gives coefficientwise positivity without fixed-width expansion, it may then suggest a decomposition usable outside complete bipartite graphs.

No scheduler, cadence, enabled state, email, Drive, public posting, peer-owner file, workflow, permission, or access setting was changed.
