Runtime model: **GPT-5.6 Sol**. Reasoning effort: **UNVERIFIED**.

# NM13-11 / T09 — dependent free layers on Rattaggi's product-of-trees lattice

Status: **PARTIAL / CANDIDATE_FULL for the restricted theorem below; universal T09 remains OPEN.** The proof below is complete as written and the load-bearing endpoint arithmetic was executed exactly in this run. No independent review has yet occurred. External priority of this exact fixed generating-set family is **UNVERIFIED** after the bounded source check recorded below.

## 1. Frozen parent problem and source-level before/after

The parent problem remains:

> For iid bond percolation on every locally finite Cayley graph `G` of every finitely generated nonamenable group, prove `p_c(G)<p_u(G)`.

The universal statement is still **OPEN**.

### Before this run

The genuinely uncovered ambient group used earlier on this track is Rattaggi's `(12,8)` virtually simple lattice `Sigma`, whose standard Cayley graph is

`Cay(Sigma,S0) ~= T_12 square T_8`,

with

`S0={a_1^{+-1},...,a_6^{+-1},b_1^{+-1},...,b_4^{+-1}}`.

Earlier NM13-11 work proved a common critical bound

`p_c < 7/125`

for every finite generator augmentation retaining `S0`, and proved an operator-sparse uniqueness criterion. It instantiated that criterion for four through eight extra inverse pairs only when the extra marked generators were chosen to freely generate a free subgroup (later all finite free-augmentation sizes were covered). The track did **not** have a concrete four-pair augmentation on this ambient group in which the four new marked generators satisfy nontrivial algebraic relations and nevertheless have a demonstrated `p_c`-to-`p_u` gap.

The immediately preceding pure-triangle report changed to another subgroup mechanism. Its higher-rank `SL_n(Z)` applications remain valid as fixed-graph calculations, but the exact scope of arXiv:2409.12283 needed a correction/expansion in our handoff: that paper's full text contains Theorems 1.14 and 1.15 on nonamenable products and property-(T) groups as *obstacles to uniqueness*. Those are endpoint-`p_u` statements and do not by themselves supply the strict `p_c<p_u` inequality requested here, but they must be recorded when judging whether a proposed new class is genuinely distinct. In particular, this run deliberately does not count a direct-product construction as a new source-level family.

### After this run

For every pair of distinct integers `2<=e<f`, define

`C_{e,f}={a_1^{+-e},a_2^{+-e},a_1^{+-f},a_2^{+-f}}`

and

`G_{e,f}=Cay(Sigma,S0 union C_{e,f}).`

This is a simple degree-28 Cayley graph. The four added inverse pairs are **not** freely marked, since, writing `d=gcd(e,f)`,

`(a_i^e)^(f/d)=(a_i^f)^(e/d)`

for `i=1,2`.

Nevertheless:

> **Theorem A (dependent two-layer Rattaggi family).** For every distinct `e,f>=2`,
> 
> `boxed(p_c(G_{e,f}) < 7/125 < 289/5000 < p_u(G_{e,f}))`,
> 
> and therefore
> 
> `boxed(p_u(G_{e,f})-p_c(G_{e,f}) > 9/5000 = 0.0018).`

Thus the fixed-graph scope on the Rattaggi ambient group expands from globally-free four-pair augmentations to an infinite family of genuinely relation-bearing four-pair augmentations.

**Original-problem delta:** universal T09 remains OPEN. A new infinite degree-28 fixed-Cayley family on a checked non-hyperbolic, non-property-(T), non-direct-product, virtually simple product-of-trees lattice now has an explicit positive gap.

**Mechanism delta:** global freeness of the perturbation is replaced by a *layer decomposition*: each layer is free and therefore has a small exact regular-representation norm, while arbitrary relations are allowed between layers. The sum-of-layer operator estimate is then pushed through the already proved nonbacktracking `L^2` transfer to an actual lower bound on `p_u`, and the retained product subgraph gives the strict upper bound on `p_c`.

## 2. Compact continuity handoff

The controlling policy is `operations/PROGRESS20_2026-09-20.md`; LIVE20 assigns NM11 to T09 under `proofnet24/NM13-11/progress-percolation/`. The current `POSTED.md` registry does not close T09, and no posted theorem is overwritten or reopened.

Preserved Benjamini--Schramm attempts include:

- normalized-kernel finite-set escape and BK/last-exit boundary decompositions;
- killed-SAW interior growth and susceptibility-weighted boundary energy;
- global `ell^2` SAW growth, including amenable and product stress tests;
- scalar nonbacktracking polynomial estimates;
- quotient/fibre-shell and fixed-endpoint bridge criteria.

Several of these produced useful inequalities without a complete transfer to `p_c<p_u`; they remain mechanism history, not source-level advances. The September continuation supplied complete restricted transfers through free cores, triangle fibres, product-lattice perturbations, power layers, free-product factor branching, and pure-torsion blocks. This run returns to the Rattaggi ambient group specifically to remove *global* freeness of the added four-pair marked set.

## 3. The standard Rattaggi block and the critical side

Rattaggi's standard `(12,8)` generating set gives

`Cay(Sigma,S0) ~= T_12 square T_8`.

The horizontal subgroup

`A=<a_1,...,a_6>`

is free of rank six with free basis `a_1,...,a_6`: its standard Cayley graph is the `T_12` horizontal fibre.

The earlier depth-three fibre Galton--Watson argument proved

`boxed(p_c(T_12 square T_8)<7/125).`                 (3.1)

For completeness, the subprocess roots the `T_12` factor and, upon entering a `T_8` fibre, exposes the radius-three open fibre cluster `Z_3`. With `s=1-p`, its exact pgf recursion is

`h_0=s`,
`h_1=s(s+p h_0)^7`,
`h_2=s(s+p h_1)^7`,
`C_3=s(s+p h_2)^8=E[s^{Z_3}]`,

and the forward offspring mean is

`m_3(p)=11(1-C_3)`.

At `p=7/125`, the archived exact checker gives

`m_3(7/125)>1+1/5000`,

so strict continuity yields (3.1).

Every `G_{e,f}` retains all edges of the standard product as a spanning subgraph. Hence monotonicity immediately gives

`boxed(p_c(G_{e,f})<7/125).`                          (3.2)

This is the critical-side percolation transfer; no operator-only claim is being counted.

## 4. Two free layers with cross-layer relations

Fix `2<=e<f`. Split the added adjacency operator into the two symmetric layers

`C_e={a_1^{+-e},a_2^{+-e}}`,
`C_f={a_1^{+-f},a_2^{+-f}}`.

Because `a_1,a_2` are part of a free basis of the horizontal free group, the two elements `a_1^e,a_2^e` freely generate a rank-two free subgroup, and so do `a_1^f,a_2^f`. The adjacency operator of the standard Cayley graph of `F_2` has norm `2 sqrt(3)`. Decomposing `ell^2(Sigma)` into left cosets of each layer subgroup therefore gives the exact layer norms

`||K_e||=||K_f||=2 sqrt(3)`.                         (4.1)

The union is not free: for each `i=1,2`, the displayed power relation couples the two layers. No independence or free-product statement between `C_e` and `C_f` is used. The triangle inequality alone gives

`boxed(||K_e+K_f|| <= 4 sqrt(3)).`                    (4.2)

The standard product adjacency has norm

`2 sqrt(11)+2 sqrt(7)`,

so the full degree-28 adjacency satisfies

`boxed(||A_{G_{e,f}}|| <= 2 sqrt(11)+2 sqrt(7)+4 sqrt(3)).`  (4.3)

This is the structural gain: four relation-bearing inverse pairs cost strictly less than the crude arbitrary-pair cost `8` because they can be partitioned into two operator-sparse free layers.

## 5. Nonbacktracking transfer and the exact gap

For a simple `D`-regular graph write `Q=D-1`. If `N_n` is the length-`n` nonbacktracking-walk operator, then

`N_0=I`, `N_1=A`, `N_2=A^2-DI`,

and for `n>=3`,

`N_n=A N_{n-1}-Q N_{n-2}`.

If `||A||<=a`, spectral calculus bounds the exponential `ell^2` growth of `N_n` by

`beta_Q(a)=sqrt(Q)` for `a<=2sqrt(Q)`, and otherwise

`beta_Q(a)=(a+sqrt(a^2-4Q))/2`.

Every open connection contains a shortest open path and hence a nonbacktracking path, so entrywise

`T_p(x,y)<=sum_{n>=0} p^n N_n(x,y)`.

Thus `T_p` is `ell^2` bounded whenever `p beta_Q(a)<1`, giving

`p_{2->2}>=1/beta_Q(a)`.

For `p>p_u`, uniqueness and FKG imply `T_p(x,y)>=theta(p)^2` for every pair; this positive lower bound on every row is incompatible with `ell^2` boundedness on an infinite graph. Therefore

`p_{2->2}<=p_u`.                                      (5.1)

For `G_{e,f}`, `D=28` and `Q=27`. We use the exact rational upper bounds

`sqrt(11)<199/60`, `sqrt(7)<127/48`, `sqrt(3)<26/15`,

whose squared margins are respectively

`1/3600`, `1/2304`, `1/225`.

Hence (4.3) gives the rational upper estimate

`||A|| < 2263/120`.                                   (5.2)

Set

`z=5000/289`.

The executed exact checker verifies

`z^2-27 = 22744933/83521 >0`

and

`z+27/z-2263/120 = 7163/2167500 >0`.                  (5.3)

Since `z>sqrt(27)`, the larger characteristic root is strictly below `z`; combining (5.1)--(5.3) gives

`boxed(p_u(G_{e,f})>289/5000=0.0578).`                (5.4)

Together with (3.2),

`289/5000-7/125=9/5000`,

which proves Theorem A.

## 6. Weakening: a layer-decomposable perturbation theorem

The power construction is only one instance of a more general structural criterion.

> **Theorem B (free-layer perturbations with arbitrary cross-relations).** Let `Gamma` be any `(12,8)`-group with standard generating set `S0`, so `Cay(Gamma,S0)=T_12 square T_8`. Add `k` genuinely new inverse generator pairs and partition them into symmetric layers
> 
> `C=C_1 disjoint_union ... disjoint_union C_m`,
> 
> where layer `j` consists of `r_j` inverse pairs that freely generate `F_{r_j}` with those marked generators. No condition is imposed on relations involving generators from different layers. Put
> 
> `k=sum_j r_j`, `Q=19+2k`,
> 
> `a=2sqrt(11)+2sqrt(7)+sum_j 2sqrt(2r_j-1)`.
> 
> Then `p_c<7/125`, and for every `z>sqrt(Q)` satisfying
> 
> `z+Q/z>a`,
> 
> one has `p_u>1/z`. In particular, if also `1/z>7/125`, the graph has a strict nonuniqueness interval.

**Proof.** The critical bound is unchanged because the standard product remains a spanning subgraph. Each layer adjacency has norm exactly `2sqrt(2r_j-1)` by coset decomposition to the regular representation of `F_{r_j}`. Summing these norms gives `||A||<=a`, regardless of cross-layer relations. The nonbacktracking argument of Section 5 then gives `p_u>1/z`. This proves the theorem. `square`

Theorem A is the first nontrivial four-pair endpoint `r_1=r_2=2`; it weakens the earlier explicit `k=4` construction from *global free rank four* to *two free rank-two layers with arbitrary cross-layer relations*. The power family supplies systematic nontrivial cross-layer relations, so the weakening is realized by actual fixed Cayley graphs rather than left as an auxiliary inequality.

## 7. Exact current source scopes and the rejected direct-product route

The source-scope refresh in this run is important.

1. **Hutchcroft, arXiv:1804.10191.** Current arXiv version is v3, revised 26 March 2019; v3 changed metadata only. It proves `p_c<p_u` for connected, locally finite, nonamenable **Gromov-hyperbolic quasi-transitive** graphs. The Rattaggi group is quasi-isometric to `T_12 square T_8`, hence is not Gromov hyperbolic.

2. **Hutchcroft--Pan, arXiv:2409.12283.** Current arXiv record is v1, 18 September 2024. Its main object is nonuniqueness **at `p_u`**, not a general proof of a positive `p_u-p_c` gap. The full text's Definition 1.11 introduces *obstacles to uniqueness*; Theorem 1.13 treats amenable wq-normal exponential-growth subgroups, Theorem 1.14 says literal nonamenable direct products `H x K` are obstacles, and Theorem 1.15 treats property-(T) and a relative-property-(T) extension. These statements strengthen endpoint information but do not by themselves replace the `p_c` estimate required in this track.

3. **Terlov--Timar, arXiv:2502.02560.** Current record is v2, revised 14 September 2025. It develops weighted/level amenability and proves a relaxed weighted `p_h<p_u` statement; this is not the ordinary unimodular fixed-Cayley target here.

4. **Later acylindrically-hyperbolic scope.** Choi--Seo prove `p_c<p_u` for every Cayley graph of an acylindrically hyperbolic group. The Rattaggi group used here has an index-four infinite simple subgroup. That subgroup splits as `F_7 *_{F_73} F_7`, so it has a nontrivial Bass--Serre tree action and is not property (T). It is also not acylindrically hyperbolic: acylindrical hyperbolicity passes to finite-index subgroups, while a non-elementary acylindrically hyperbolic group is SQ-universal, incompatible with this finitely generated infinite simple subgroup. The standard product geometry also excludes Gromov hyperbolicity.

The literal direct-product scope in Hutchcroft--Pan matters for route selection. Early in this run I developed and exactly checked a product-fibre comparison on `(* C_3) x Z`; its arithmetic is valid, but I **reject it as the source-level advance** because it sits in the classical nonamenable-product regime explicitly isolated by Peres and by Hutchcroft--Pan Theorem 1.14. The exploratory checker/output were preserved at commits `d83ddc8a33ba7cc81b60a5a5c6d5bdd51ebb2a1a` and `afd2c1f59759b9f056d75722b788f3e80de8eb64` rather than silently deleted. The theorem counted in this report is instead the relation-bearing Rattaggi family above.

Rattaggi's ambient group is not a direct product of two infinite groups. Indeed, let `Sigma_0` be its simple index-four subgroup. If `Sigma=H x K` with `H,K` infinite, then `H cap Sigma_0` and `K cap Sigma_0` are normal in `Sigma_0`. Since `Sigma/Sigma_0` is finite, each infinite factor has nontrivial intersection with `Sigma_0`; simplicity forces both intersections to equal `Sigma_0`, contradicting `H cap K={1}`. Thus Hutchcroft--Pan Theorem 1.14 does not apply by its stated direct-product hypothesis.

A bounded source search found no theorem already giving the above dependent four-pair fixed graphs. Exact worldwide novelty remains **UNVERIFIED**.

## 8. Essential executed check

The load-bearing checker is

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T14-50-30+0300__t09-dependent-layer-check.py`

created at commit

`1376bbe2e20f1445c25a48cda3ad3e542664c035`.

Its actual executed output is archived as

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T14-50-30+0300__t09-dependent-layer-check.out`

at commit

`33c8a6a7d59d1fe244db9ccabf36ba342d0cb329`.

The output ends

`ALL_EXACT_CHECKS_PASS`.

## 9. Residual obstruction and next attack

The first unresolved perturbative boundary is still structurally meaningful: four **arbitrary** added inverse pairs on the Rattaggi standard graph are not certified by the scalar norm method. The crude arbitrary cost is `8`, and the resulting scalar nonbacktracking lower bound falls below the retained `7/125` critical upper bound. The new theorem crosses that boundary only when the four pairs admit an operator-sparse layer decomposition.

The next materially different attack should therefore not polish the present square-root constants. It should either:

- derive a colored nonbacktracking recurrence distinguishing horizontal, vertical, and perturbation edge types so that the perturbation does not enter solely through `||K_C||`; or
- strengthen the critical comparison using the added edges themselves, with a finite-state fibre branching process that remains valid for arbitrary four-pair placements.

Those are the two routes that can plausibly remove the remaining layer structure.

## ledger_delta

```yaml
ledger_delta:
  target: T09_Benjamini_Schramm_nonuniqueness_phase
  universal_status: OPEN
  restricted_status: CANDIDATE_FULL_pending_independent_review
  original_problem_progress:
    before: "On the checked Rattaggi ambient group, four-pair perturbations had explicit certificates when the four added generators globally formed a free marked F4; no concrete relation-bearing four-pair family had a demonstrated gap."
    after: "For every 2<=e<f, the degree-28 graph Cay(Sigma,S0 U {a1^+-e,a2^+-e,a1^+-f,a2^+-f}) satisfies pc<7/125<289/5000<pu, hence pu-pc>9/5000."
    source_scope: "Infinite fixed-graph family with systematic power relations among the added generators on Rattaggi's virtually simple product-of-trees lattice."
  mechanism_progress:
    - "Layer-decomposable perturbation theorem: free layers contribute exact norms 2 sqrt(2r_j-1) while cross-layer relations are unrestricted."
    - "For two rank-2 layers, kappa<=4 sqrt(3), giving the exact degree-28 root-test certificate."
    - "The operator bound is transferred all the way to pu through p_{2->2}, while pc is strictly controlled by the retained product-fibre Galton-Watson subprocess."
  source_scope_refresh:
    - "arXiv:1804.10191 v3 (2019-03-26): nonamenable Gromov-hyperbolic quasi-transitive graphs, actual pc<pu."
    - "arXiv:2409.12283 v1 (2024-09-18): endpoint-pu obstacle theory; full text includes Theorem 1.14 for nonamenable direct products and Theorem 1.15 for property-(T)/relative-(T) groups."
    - "arXiv:2502.02560 v2 (2025-09-14): weighted/level amenability and relaxed weighted ph<pu."
  rejected_route:
    route: "(* C3) x Z product-fibre branching"
    reason: "Valid quantitative calculation but rejected as the source-level advance because it lies in the classical nonamenable-product regime explicitly treated in the literature."
    preserved_checker_commits:
      - d83ddc8a33ba7cc81b60a5a5c6d5bdd51ebb2a1a
      - afd2c1f59759b9f056d75722b788f3e80de8eb64
  exact_check:
    code_commit: 1376bbe2e20f1445c25a48cda3ad3e542664c035
    output_commit: 33c8a6a7d59d1fe244db9ccabf36ba342d0cb329
    terminal_line: ALL_EXACT_CHECKS_PASS
  residual_obstruction: "arbitrary four-pair perturbations still defeat the scalar norm certificate; layer structure remains necessary."
  next_method: "colored nonbacktracking or added-edge finite-state critical branching"
  external_priority: UNVERIFIED
  runtime_model: GPT-5.6_Sol
  reasoning_effort: UNVERIFIED
```
