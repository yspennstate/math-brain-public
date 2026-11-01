Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED**. This is not GPT-6 at maximum.

# P03 / P0456 run report — 2026-09-18T06:30:46Z

**MOVEMENT: `c_LK^cert : 1/2 -> 0`; P0456 unchanged count `1 -> 0`.** This run uses Section-B methods **#12 FIND WHAT IS CONSERVED, #25 COUNT THE SAME THING TWICE, #5 ADD A PARAMETER AND DIFFERENTIATE IN IT**. The movement is source-scale: for every fixed negative coefficient the graph is now rigorously disconnected whp, and for every fixed positive coefficient it is rigorously connected whp, at the source scale `sqrt(log n) log log n`. The coefficient metric has therefore reached its optimal value `0`. This does **not** determine the finer `o(sqrt(log n) log log n)` window, in particular the exact behavior at coefficient zero.

## 1. Continuity, source and ownership

Current exclusive claim: `operations/claims/P0456.md`, creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

Predecessor P03 report: `proofnet24/P03-fei/runs/2026-09-18/2026-09-18T05-39-57Z__p0456-admission-harris-isolation.md`, creation commit `da9ace6e0a754fba633ccfa84187d23440faa847`, blob `c633272bca8921f7e583083d55f8f16def86cefe`.

I reread/recovered the current root README, hourly protocol, FLEET rules / owner directive, operations/FLEET, campaign INDEX/RANKING, POSTED, RESULTS, QUEUE, current claim and newest P03 report, newest visible task-health state, and neighboring P0457 ownership/work. `RESULTS.md` and `QUEUE.md` are large connector-truncated surfaces, so I do not claim a byte-for-byte reread; I used exact path-scoped reads/searches and current blobs for the needed state. P0457 remains separately claimed/owned by NM13-04 and was used only for nonduplication.

Primary source rechecked on 2026-09-18: Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, DOI `10.1017/jpr.2025.10051`, Journal of Applied Probability 63(2), June 2026, Section 1.1. The source still states that the coefficient band between `-1/2` and `+1/2` at scale `sqrt(log n) log log n` is unresolved. A bounded fresh search for later 2026 work recovered the primary article but no later source-matching closure. This is dated bounded evidence only, not a worldwide openness or novelty certificate.

The exact source ingredients used below are Lemma 3 (the multitype permutation lower-tail bound), Lemmas 10--14 (two-vertex isolation decomposition), Theorem 4 / Corollary 1 (small-component route), and the spanning-tree / crossing-edge argument of Theorem 5. I do not change the LK model or its quantifiers.

## 2. Idea before code, and attempted refutation

The source repeatedly fixes an auxiliary cutoff `s=floor(sqrt(k))`. The resulting application of Lemma 3 contains the term

`(1/2) sqrt(k) log k`,

which becomes the entire `1/2` coefficient barrier in both directions. The first question was therefore whether `sqrt(k)` is forced by the source combinatorics. It is not.

The conserved quantity is the expected number of type-0 objects in the relevant early prefix. With `s` competing nonzero types, the prefix length is asymptotically `s k` and the type-0 density is asymptotically `1/(s+1)`, so the expected type-0 count remains asymptotically `k` as `s` changes. The event used by the source asks for only about `s` type-0 objects. Thus changing `s` does not alter the underlying rare event's mean scale; it only trades the finite-depletion term against the entropy of choosing the exceptional type-0 positions.

I tried to refute the smaller-cutoff route before using it. For the choice eventually used below, `s=Theta(sqrt(k/log k))`:

- `s -> infinity`, `s=o(k)`, and `s<=k`;
- `s=o(n^(1/4))` and all type-size perturbations are `O(s^2)=O(k/log k)=o(n^(1/4))` because here `k=O(log n)`;
- the source prefix length `ell=Theta(s k)=o(n^(1/4))` and `s=o(ell)`;
- the Lemma-3 threshold condition `t<=ell/s` holds since `t=Theta(s)` while `ell/s=Theta(k)`;
- in the pair proof the number of nonzero types is either `s` or `s-1`; the `s-1` case has a *smaller* leading loss and is therefore covered by the same uniform upper bound;
- in the low-degree proof replacing the source threshold `s-1` by the exact `s-1` value changes only lower-order terms.

No source step forces `s=sqrt(k)`. The obstruction was therefore an optimization artifact, not a structural condition.

## 3. B5 — optimize the source Lemma-3 exponent

I first isolate the reusable asymptotic calculation.

### Optimized occupancy lemma

Assume fixed constants `a,b,d=O(1)`, let `k->infinity`, and put

` s = c sqrt(k/log k) + O(1),     c>0,`

` ell = (s-b)(k-s-a),     t=s+d.`

Apply the first (general) inequality in source Lemma 3 with `s` nonzero types. Its exponent is

`E = -ell/(s+1) + t log(ell/(t s)) + t + log(t+1).`

Then

`E = -k + ((b+1)/c + c/2 + o(1)) sqrt(k log k).`          (3.1)

#### Proof

Since `s~c sqrt(k/log k)`,

`ell/(s+1) = k - (b+1)k/s + o(sqrt(k log k))`,

because the omitted terms are `O(s+k/s^2+1)=o(sqrt(k log k))`. Hence

`-ell/(s+1) = -k + ((b+1)/c+o(1)) sqrt(k log k).`

Also

`log(ell/(t s)) = log(k/s)+o(1)
 = (1/2)log k + (1/2)log log k - log c + o(1).`

Multiplying by `t=s+O(1)` gives

`t log(ell/(t s)) = (c/2+o(1)) sqrt(k log k).`

Finally `t+log(t+1)=O(s)=o(sqrt(k log k))`. Summing proves (3.1). QED.

The leading loss is

`phi_b(c)=(b+1)/c+c/2.`

Differentiating gives `phi_b'(c)=-(b+1)/c^2+1/2`; the unique minimizer is

`c=sqrt(2(b+1)),     min phi_b=sqrt(2(b+1)).`               (3.2)

This is the entire gain. The source's `s=sqrt(k)` corresponds to a much larger scale, where the entropy term is `(1/2)sqrt(k)log k`; the balanced scale is instead `sqrt(k/log k)`.

### B25 cross-count

The same leading rate is visible by collapsing all nonzero types and counting the positions occupied by type 0 in the early prefix. In the equal-size idealization the count is hypergeometric with population type-0 fraction `1/(s+1)`, prefix size `ell~sk`, and threshold `t~s`. Expanding the hypergeometric lower-tail mass gives exactly the two leading costs in (3.1): finite depletion contributes `(b+1)k/s`, while choosing the exceptional type-0 positions contributes `s log(k/s)`. The source's Lemma 3 supplies the rigorous finite-population correction for the actual slightly unequal type sizes and the order restrictions. Thus the permutation/urn description and the binary type-0 occupancy description agree on the optimized rate.

## 4. Pair-isolation gate: `sqrt(k) log k` becomes `sqrt(k log k)`

Let `B` be exactly the source Lemma-10 overlap event, namely the union of the direct-neighbor, top-k-neighbor-set intersection and directed-overlap events used in Section 4. The source proves

`P(B)=O(k^3/n)`                                                   (4.1)

and, on `B^c`, exact conditional independence of the two isolation events (Lemma 13).

In source Lemma 11, conditional on

`A_1 = B_{1;2} union B_{1 union 2} union B_{1->2}`,

the permutation argument shows that isolation of vertex 1 requires at most `s` type-0 objects among the first

`ell=(s-1)(k-s-2)`

positions. The proof is valid for any `s->infinity`, `s=o(k)` satisfying the Lemma-3 hypotheses; `s=floor(sqrt(k))` is chosen only at the final numerical substitution.

Take instead

` s = floor(2 sqrt(k/log k)).`

If the number of nonzero types is `s`, (3.1) has `b=1,c=2`, so

`P(I_1 | A_1) <= exp(-k+(2+o(1))sqrt(k log k)).`             (4.2)

If vertex 2 belongs to the first `s` neighbors, there are only `s-1` nonzero types. Writing `q=s-1`, the same prefix is `q(k-q-3)` and the threshold is `q+1`; direct substitution in Lemma 3 gives leading coefficient `1/c+c/2=3/2` at `c=2`, which is stronger than (4.2). Thus (4.2) is uniform. By symmetry the same holds for vertex 2.

Combining (4.1) and (4.2) exactly as in source Lemma 12 gives

`P(I_1 I_2 intersect B)
 <= exp(-log n-k+(2+o(1))sqrt(k log k)).`                     (4.3)

The source's `+(1/2)sqrt(k)log k` pair loss is therefore replaced by `+(2+o(1))sqrt(k log k)`.

## 5. Disconnection for every fixed negative source coefficient

Set

`L_n = sqrt(log n) log log n,     S_k=sqrt(k log k).`

Fix a constant `tau<0` and first take the boundary sequence

`k=floor(log n+tau L_n)`.

Then `k/log n ->1` and

`S_k = (1+o(1))sqrt(log n log log n)=o(L_n).`                 (5.1)

From retained Claim `P03-P0456-HARRIS-ISOLATION-ROOT2-274`, for every fixed `eta>0`,

`p_n:=P(I_1) >= exp(-k-(sqrt(2)+eta)S_k+o(S_k)).`             (5.2)

Therefore

`log(n p_n) >= log n-k-(sqrt(2)+eta)S_k+o(S_k)
             = -tau L_n-o(L_n) -> +infinity`,

so the expected number of isolated vertices diverges.

Next, from (4.1) and (5.2),

`log(P(I_1 intersect B)/(p_n P(B^c)))
 <= k-log n+O(S_k)+3log k
 = tau L_n+o(L_n) -> -infinity.`

Hence, using the source's identity (10),

`P(I_1 | B^c)/P(I_1) ->1.`                                   (5.3)

For the exceptional pair contribution, (4.3) and (5.2) give

`log( P(I_1I_2 intersect B)/p_n^2 )
 <= k-log n+(2+2sqrt(2)+2eta+o(1))S_k
 = tau L_n+o(L_n) -> -infinity.`                              (5.4)

On `B^c`, source Lemma 13 gives exact conditional independence. Equations (5.3)--(5.4) therefore yield

`limsup P(I_1I_2)/p_n^2 <=1.`

The same second-moment calculation as source Theorem 3 now gives

`P(sum_v I_v=0) ->0.`

Thus `LK(n,k)` is disconnected whp at the boundary sequence for every fixed `tau<0`. Since `LK(n,k)` is nested increasingly in `k`, the same is true for every smaller `k` satisfying

`k <= log n+tau L_n.`                                         (5.5)

This proves the disconnection frontier coefficient is `c_-=0`.

## 6. Connectivity for every fixed positive source coefficient

The same optimization improves the source low-degree theorem, but I do not rely on the source's particular `sqrt(2)` order-statistic envelope for medium components. I give a self-contained fixed-constant envelope below.

### 6.1 Optimized fixed-degree exclusion

Fix an integer `kappa>=0`. In source Theorem 4, if vertex 1 has degree at most `kappa`, then for the first `s` preferred neighbors a necessary condition is that at most `s-1` type-0 objects occur among the first

`ell=(s-kappa)(k-s-1)`

positions. Choose

`s=floor(sqrt(2(kappa+1))*sqrt(k/log k)).`

The optimized occupancy lemma with `b=kappa` gives

`P(deg(1)<=kappa)
 <= exp(-k+(sqrt(2(kappa+1))+o(1))S_k).`                      (6.1)

Consequently, if `tau>0` and

`k=ceil(log n+tau L_n)`,

then for every fixed `kappa`,

`P(exists v: deg(v)<=kappa)
 <= exp(log n-k+O(S_k))
 = exp(-tau L_n+o(L_n)) ->0.`                                (6.2)

### 6.2 A uniform medium-component exclusion at `k/log n ->1`

Transform the Uniform edge weight `U_e` to the exponential preference score `Y_e=-log U_e`; larger scores are preferred. Let `T_i` be the kth largest score incident to vertex `i`, and set

`m=log((n-1)/k).`

Use the fixed constant `C=3`. For one vertex,

`P(T_i>m+C) <= exp[-k(C-1+e^{-C})]`,

because the number of incident scores above `m+C` is binomial with mean `k e^{-C}`. Similarly,

`P(T_i<m-C) <= exp[-k(e^C-1-C)].`

Both are standard Chernoff bounds. Since

`C-1+e^{-C}=2+e^{-3}>1`,

and `e^C-1-C=e^3-4>1`, while `k/log n->1`, a union bound over all vertices gives

`P(A_C^c)->0`,

where

`A_C={ for every i, T_i in [m-C,m+C] }.`                     (6.3)

On `A_C`, define

`p=e^C k/(n-1),     pbar=e^{-C}k/(n-1).`

If a set `S` of size `r<=n/2` is a connected component of `LK(n,k)`, then it contains a spanning tree whose `r-1` edge scores all exceed `m-C`, and every crossing edge from `S` to `S^c` has score at most `m+C` (otherwise it would be preferred at both endpoints and would be present). Distinct edge scores are independent, so by Cayley's formula

`P(exists a component of size r and A_C)
 <= binom(n,r) r^(r-2) p^(r-1) (1-pbar)^(r(n-r)).`

Using `binom(n,r)<=(en/r)^r`, `1-x<=e^{-x}`, `r<=n/2`, and `1/p<=n` for large `n`, this is at most

`n exp{ r[1+log(np)-n pbar/2] }.`                             (6.4)

Because `k/log n->1`,

`1+log(np)-n pbar/2
 = -(e^{-3}/2+o(1))log n+O(log log n)
 <= -0.02 log n`

for all large `n`. Summing (6.4) for `100<=r<=n/2` gives

`P(exists component with 100<=r<=n/2) <=
 n sum_{r>=100} n^{-0.02r}+o(1) ->0.`                         (6.5)

For `1<=r<=99`, any component has every vertex degree at most `98`. Taking `kappa=98` in (6.2) excludes all such components whp. Thus no component of size at most `n/2` remains, and the graph is connected whp at the boundary sequence for every fixed `tau>0`. By monotonicity in `k`, connectivity holds for every larger `k` satisfying

`k >= log n+tau L_n.`                                         (6.6)

Therefore `c_+=0`.

## 7. Main promoted claim and exact metric movement

### `P03-P0456-OPTIMIZED-CUTOFF-WINDOW-ZERO-276 = PROVED / SOURCE-SCALE-WINDOW-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`

Let

`L_n=sqrt(log n) log log n`.

For the Dabirian--Subramanian bilateral-preference graph `LK(n,k)`:

1. for every fixed real `tau<0`, if `k<=log n+tau L_n`, then `LK(n,k)` is disconnected with high probability;
2. for every fixed real `tau>0`, if `k>=log n+tau L_n`, then `LK(n,k)` is connected with high probability.

Hence the frozen symmetric coefficient metric moves

`c_LK^cert : 1/2 -> 0`.

This closes the **fixed nonzero coefficient** gap left in Section 1.1 at the paper's displayed scale. It does not identify the smaller transition window, does not decide `k=log n+o(L_n)`, and does not assert a limiting law at `tau=0`. Publication novelty is unverified.

No code or numerical certificate is used in this theorem. The improvement is analytic and comes from optimizing an auxiliary cutoff inside the source's own multitype permutation inequality, plus the fixed-constant Chernoff/spanning-tree argument in Section 6.2.

## 8. Failures and exact remaining obligation

The run deliberately did **not** repeat the one-vertex Harris proof or use mean degree. The initial pair-overlap concern was real: keeping `s=sqrt(k)` leaves a `sqrt(k)log k` loss and cannot exploit Claim 274. The failure disappears only after balancing the Lemma-3 exponent.

The frozen metric is now saturated at its theoretical minimum `0`, so further work cannot honestly report movement in `c_LK^cert`. The remaining source-level question is finer: determine the actual width and location inside

`k=log n+o(sqrt(log n) log log n).`

The bounds proved here already show that the source's displayed `±1/2` window is not the right coefficient-scale obstruction. At the next visible scale `sqrt(log n log log n)`, the current arguments still have nonsharp constants: the bad-pair second-moment term contains the constant `2+2sqrt(2)` when normalized by Claim 274, while the fixed-degree connectivity side has a constant depending on the finite component cutoff. Those constants are not promoted as a new frozen metric in this report.

A sensible next attack is to derive exact moderate-deviation asymptotics for the pair occupancy and the one-vertex isolation probability rather than only upper/lower exponential envelopes. Suggested next Section-B triple: **#2 ATTACK THE NEGATION, #14 EXACT FINITE REDUCTION, #30 DO ONE SCALE / ONE DIRECTION AT A TIME**. Any new metric for the finer window should be explicitly admitted/frozen before numbers are assigned; `UNKNOWN` is not zero.

## 9. Directed second audit: P04/I0101 Claim 38

I audited a new P04 claim not in the prior P03 audit list:

`P04-I0101-P4177-THETAPLUS-FRONTIER-38 = PROVED / FINITE-PARTIAL`.

Peer report path:
`proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T04-42-09Z__run-report.md`

Creation commit: `8dfa764c9197417414a9f5480a21b4821bbee75c`.
Actual report blob recovered by exact-commit fetch: `81cc0662a36c0d154c5f62bf3935850e6abd1d07`.

The claimed exact checker is
`proofnet24/P04-closure-local-paley/artifacts/2026-09-18T04-42-09Z__p4177_exact.py`, creation commit `3228f0c4a862652995d6e91923916f229396a58d`; exact-commit fetch gives actual Git blob `9891292b01347faab43e522bfd9ff1fd85610425`.

The archived output is
`proofnet24/P04-closure-local-paley/artifacts/2026-09-18T04-42-09Z__p4177_exact.out`, creation commit `f79d4a7e8948cbc2fce56b1f9434479d26615c69`; exact-commit fetch gives actual Git blob `e4122dd8c3585662d492e402a7a867070aa7b23c`.

I independently regenerated the finite field / localized graph counts and S3 orbit census and checked the exact acceptance logic. The frontier `(4157,4177]` contains exactly the admissible prime `4177`; the localized graph has `1043` vertices, `271185` graph edges and `272218` complement edges; vertex orbit census is `[(2,1),(3,1),(6,173)]`; the `45501` free nonedge orbits have census `[(1,1),(3,261),(6,45239)]`. The exact source comparison is

`4*100^2*4177 - 9*4308^2 = 50224 > 0`,

which is equivalent to `43.08 < (2/3)sqrt(4177)`.

All free rational `B` orbit weights have negative numerators (`[-1704,-257]/1024`), so the stronger Szegedy theta-plus sign condition holds. For positive definiteness, the checker writes the integral residual in the form

`FACQ^2 Mint = Lq Lq^T + R + SLACK_I FACQ^2 I`.

It verifies the exact row-sum norm bound

`max_i sum_j |R_ij| = 465316633 < 3221225472 = SLACK_I*FACQ^2`.

Since `R` is symmetric, its operator norm is bounded by that maximum absolute row sum, so the right side is strictly positive definite. Floating eigensolvers and Cholesky are therefore proposal mechanisms only; acceptance is exact integer arithmetic. Fixed entries and S3 invariance are also checked exactly. The mathematical finite claim passes.

There is, however, a **peer metadata defect**: the P04 report text states checker/output blob IDs `162173925850e61abfa8afcda796108471803cd4` and `9cb82f90db02063a514c310867d2b05cb9e69b68`. Direct blob lookup returned 404 for both. Exact-commit `fetch_file` instead identifies the actual Git blobs as `9891292b01347faab43e522bfd9ff1fd85610425` and `e4122dd8c3585662d492e402a7a867070aa7b23c` above. I did not edit the peer file.

Audit verdict:

`P03-AUDIT-P04-I0101-P4177-THETAPLUS-FRONTIER-277 = PASS (CLAIM-SCOPED) / METADATA-CORRECTION-REQUIRED`.

This validates the finite `p=4177` theta-plus certificate, not Randomstrasse Conjecture 27 asymptotically.

## 10. Ledger delta for P26

```yaml
ledger_delta:
  track: P03
  source_id: P0456
  claim_path: operations/claims/P0456.md
  mathematical_status: PARTIAL
  claim_promoted: P03-P0456-OPTIMIZED-CUTOFF-WINDOW-ZERO-276
  metric:
    name: c_LK^cert
    before: 1/2
    after: 0
    direction: lower_is_better
    unchanged_count_before: 1
    unchanged_count_after: 0
  exact_scope:
    disconnected: "every fixed tau<0 at k <= log n + tau sqrt(log n) log log n"
    connected: "every fixed tau>0 at k >= log n + tau sqrt(log n) log log n"
    unresolved: "coefficient zero and the finer o(sqrt(log n) log log n) window"
  source_status: PARTIAL_OPEN_AT_FINER_SCALE
  publication_novelty: UNVERIFIED
  peer_audit:
    id: P03-AUDIT-P04-I0101-P4177-THETAPLUS-FRONTIER-277
    verdict: PASS_CLAIM_SCOPED_METADATA_CORRECTION_REQUIRED
    peer_claim: P04-I0101-P4177-THETAPLUS-FRONTIER-38
    peer_report_creation_commit: 8dfa764c9197417414a9f5480a21b4821bbee75c
    peer_report_blob: 81cc0662a36c0d154c5f62bf3935850e6abd1d07
  recoveries_used: 0
  next_state: P0456_ACTIVE_FINE_WINDOW_REFINEMENT
```

P26 alone should reconcile shared root ledgers. No shared root file and no peer file was edited by P03.

**End of complete run report.**