Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FROZEN-METRIC MOVEMENT: `N_exact = 96 -> 97`; methods actually tried: #27 SWAP THE QUANTIFIERS, #26 HUNT THE SPORADIC CASE, #14 FIND THE GROUP ACTING, and #7 TAKE THE LIMIT, all explicitly RECYCLED because all 30 Section-B methods had already genuinely been used on P0282.

# NM13-07 research invocation — P0282 shadow-average obstruction, eight-ninths window, row 97

Date: 2026-09-19 UTC  
Track: `proofnet24/NM13-07`  
Category: CLOSABLE OUTSIDE  
Canonical claim: `P0282`  
Source id: `aim_kpz_followup_2025`  
Source status: OPEN  
Worker status before/after: PARTIAL -> PARTIAL

## 1. Continuity, ownership, and source identity

This invocation is a continuation of the already admitted P0282 target; admission is **not** reopened and no new claim file is created. The canonical claim still assigns P0282 exclusively to NM13-07 with dedup key

`chen_log_concavity_conjecture_for_fixed_size_random_permutation_lis`,

SHA-256

`08312c764bd0e9331fed25b1f255810f3c3b9e0f81134520fa26aca4c9c471a4`,

whose integer residue modulo 13 is 6, the exclusive shard for this worker.

The exact source problem is unchanged. For

\[
\ell_{n,k}=\#\{\sigma\in S_n:\operatorname{LIS}(\sigma)=k\},
\]

Chen conjectured

\[
\ell_{n,k}^2\ge \ell_{n,k-1}\ell_{n,k+1}\qquad(1<k<n).
\]

The newest own report on entry was

`proofnet24/NM13-07/runs/2026-09-19/2026-09-19T10-13-00Z__p0282-shadow-density-seven-eighths-row96.md`

at creation commit `3409db11144f88cb2dc0525d36039386b49fe42c`. Its authoritative retained state was:

- frozen metric `N_exact = 96`;
- complete all-`n` Chen fixed-defect theorem for `j=n-k <= 66`;
- complete all-`n` binomial-normalized ULC theorem for `j <= 32`;
- rigorous growing-defect theorem `j+1 <= n^(7/8)/8`;
- source OPEN, worker PARTIAL;
- audits P26 NOT PASSED and NM13-08 NOT PASSED.

A delta check from that creation commit through the repository head present before this invocation found no release, competing alias owner, P0282 settlement, or P0282 audit PASS. The newest NM13-08 continuity still treats P0282 as active elsewhere and contains no audit PASS. The canonical claim was read again after the substantive artifacts below and remained unchanged.

## 2. Required repository/policy reads and access disclosure

Before substantive work I read the current versions of:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- the later owner-authorized NM13 deployment amendment;
- `QUEUE.md`;
- `POSTED.md`;
- `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the newest own report;
- current neighboring NM13 continuity;
- canonical claims and targeted attempt/ownership history for P0282.

The very large unchanged intake JSONL corpora were **not falsely represented as freshly rendered byte-for-byte in this interface**. Canonical P0282 identity, aliases, ownership, current claim state, targeted intake/history matches, and the repository delta since the preceding immutable report were recovered. No inaccessible history is silently treated as permission to restart anything.

No shared root ledger, peer namespace, workflow, permission, public surface, email/Drive resource, paid compute, or schedule was modified.

## 3. Frozen metric

The metric remains exactly the metric frozen by this track:

> `N_exact` = largest `N` for which archived exact certificates cover every source Chen inequality in every row `1,...,N`.

It is not replaced by a defect frontier, an asymptotic exponent, or a stronger auxiliary property.

Before this run: `N_exact = 96`.  
After this run: `N_exact = 97`.

The fixed all-`n` Chen defect frontier stays `66`; the stronger all-`n` ULC frontier stays `32`. Those are useful secondary theorem frontiers but are not the frozen metric.

## 4. Method #27 RECYCLED — swap the false pointwise shadow quantifier for the exact rank-average identity

### 4.1 Correct averaged formulation

For a rank-`r` Viennot shadow set `S`, let `e(S)` be its number of valid one-rook shadow extensions and define

\[
q_r(S)=\frac{e(S)}{(n-r)^2}.
\]

The preceding run proved by double counting that the normalized shadow-density ratio is

\[
\frac{\rho_{r+1}(n)}{\rho_r(n)}
=\mathbb E_{S\sim\mathrm{Unif}(\Delta_r)}q_r(S).
\]

The previously tempting pointwise assertion that `q` decreases along every shadow edge is false. This run therefore swaps the quantifier in the only source-faithful way: average over the rank before trying to compare ranks.

For a parent `S` with `e(S)>0`, put

\[
a_r(S)=\mathbb E\bigl[q_{r+1}(T)\mid T\text{ is a uniformly chosen valid child of }S\bigr].
\]

Every rank-`r+1` shadow face has exactly `r+1` rank-`r` parents. Hence choosing a uniform rank-`r+1` face is equivalent, for any child statistic, to size-biasing a uniform rank-`r` parent by `e(S)` and then choosing one of its children uniformly. Therefore

\[
\boxed{
\mathbb E_{\Delta_{r+1}}q_{r+1}
=
\frac{\mathbb E_{\Delta_r}[e(S)a_r(S)]}
     {\mathbb E_{\Delta_r}[e(S)]}.
}
\]

This is an exact identity. It identifies the genuine remaining shadow obligation as a **global size-biased compensation inequality**, not a pointwise monotonicity statement.

### 4.2 Two natural local sufficient conditions are false

The idea was written down before production checking in

`artifacts/2026-09-19/p0282_shadow_average_eight_ninths_idea.md`.

Then an exact-arithmetic enumerator checked all shadow ranks through `n=6`, with independent rank counts

- `n=2`: `[1,1]`;
- `n=3`: `[1,4,1]`;
- `n=4`: `[1,9,13,1]`;
- `n=5`: `[1,16,61,41,1]`;
- `n=6`: `[1,25,181,381,131,1]`.

The first tempting sufficient strengthening, negative covariance of `e(S)` with the child-average `a_r(S)`, already fails at `(n,r)=(4,1)`:

\[
\operatorname{Cov}_{S\in\Delta_1}(e(S),a_1(S))
=\frac{8}{243}>0.
\]

Here

\[
\mathbb E_{\Delta_1}q_1=\frac{26}{81},
\qquad
\mathbb E_{\Delta_2}q_2=\frac3{52},
\]

so the desired global rank decrease still holds despite the covariance having the opposite sign from the naive proof route.

The second tempting strengthening,

\[
a_r(S)\le \mathbb E_{\Delta_r}q_r\quad\text{for every parent }S,
\]

also fails. The first failure in the exact `n<=6` census occurs at `(n,r)=(6,3)` for

\[
S=\{(2,6),(3,5),(5,3)\},\qquad e(S)=3,
\]

where

\[
a_3(S)=\frac16
>\frac{524}{3429}
=\mathbb E_{\Delta_3}q_3.
\]

Nevertheless the actual next-rank mean is

\[
\mathbb E_{\Delta_4}q_4=\frac5{524}
<\frac{524}{3429}.
\]

So this route produced a useful obstruction rather than a false lemma: any successful shadow proof has to exploit compensation across parents globally. It cannot be reduced to either of these local negative-regression statements.

Exact finite certificate:

- `artifacts/2026-09-19/p0282_shadow_average_regression_falsifier.py`;
- `artifacts/2026-09-19/p0282_shadow_average_regression_falsifier.out`.

The archived output ends `ALL_EXACT_CHECKS_PASS`. This is a track self-check/certificate, not an outside audit.

## 5. Methods #26, #14, #7 RECYCLED — seventh-order Plancherel sign test and an eight-ninths theorem

The shadow route did not close, so the fallback was used exactly as precommitted: hunt the next surviving coefficient, compute only the genuinely new group moments, and stop if its Chen curvature is adverse. It is favorable.

Write

\[
j=n-k,\qquad F_j(n)=\ell_{n,n-j}.
\]

In the stable long-first-row regime the retained exact hook factorization is

\[
F_j(n)=\frac{(n)_j^2}{j!}A_j(n).
\]

Set `t=1/n` and

\[
G_j(t)=\log A_j(t)=\sum_{m\ge1}D_m(j)t^m.
\]

The preceding invocation established an analytic disk sufficient for uniform Cauchy estimates; this proof uses it but does not re-label it as new work.

### 5.1 New Plancherel moment 1: `E[S_6]`

Let

\[
X_i=\sum_{a<i}(a\ i)
\]

be the `i`-th Jucys--Murphy element. Under irreducible representation `\mu`, `\sum_iX_i^6` acts with trace corresponding to the sixth content power sum

\[
S_6(\mu)=\sum_{\square\in\mu}c(\square)^6.
\]

Thus its Plancherel expectation equals the identity coefficient of `\sum_i X_i^6` in the regular representation.

Fix `i` and write `m=i-1`. A length-six word in the star transpositions `(a i)` can multiply to the identity only using one, two, or three distinct leaves; every used leaf has even incidence.

- One distinct leaf: exactly `m` words.
- A fixed unordered pair of leaves: the two generators form the six-cycle Cayley graph of `S_3`. There are `22` six-step returns in total; subtracting the two one-letter words leaves `20` words using both leaves.
- A fixed unordered triple: each leaf must occur exactly twice. Up to relabeling the first appearances, the identity pairing patterns are
  `AABBCC`, `AABCCB`, `ABBACC`, `ABBCCA`, `ABCCBA`.
  Relabeling the three leaves gives `5*3!=30` words per unordered triple.

Hence

\[
[e]X_i^6
=m+20\binom m2+30\binom m3
=m(5m^2-5m+1).
\]

Summing `m=0,...,j-1` gives

\[
\boxed{
\mathbb E_{\mathrm{Pl}(j)}S_6
=\frac{j(j-1)(15j^2-35j+16)}{12}.
}
\]

### 5.2 New Plancherel moment 2: `E[C^2 S_2]`

Let

\[
T=\sum_iX_i
\]

be the transposition class sum, whose eigenvalue on `\mu` is total content `C(\mu)`. Let

\[
P_2=\sum_iX_i^2.
\]

The retained class identity is

\[
P_2=\binom j2 e+K_3,
\]

where `K_3` is the sum of all 3-cycles. Therefore

\[
\mathbb E[C^2S_2]=[e]T^2P_2.
\]

Now `[e]T^2=\binom j2`. Also every 3-cycle has exactly three ordered factorizations as a product of two transpositions, and there are `2\binom j3` 3-cycles. Consequently

\[
\begin{aligned}
\mathbb E[C^2S_2]
&=\binom j2^2+6\binom j3\\
&=\boxed{\frac{j(j-1)(j^2+3j-8)}4}.
\end{aligned}
\]

### 5.3 Exact seventh coefficient

The seventh hook-log coefficient before the outer factor `2` is

\[
\begin{aligned}
B_7={}&-j^7+3j^6-5j^5+5j^4-3j^3+j^2-\frac j7\\
&+(-6j^5+15j^4-20j^3+15j^2-6j+1)C\\
&+(-15j^4+30j^3-30j^2+15j-3)S_2\\
&+(-20j^3+30j^2-20j+5)S_3\\
&+(-15j^2+15j-5)S_4+(-6j+3)S_5-S_6.
\end{aligned}
\]

Using the two new moments above, the retained lower content moments, transpose parity, and the formal cumulant expansion of

\[
\log\mathbb E_{\mathrm{Pl}(j)}
\exp\!\left(2\sum_{m=1}^{7}B_m t^m\right),
\]

the exact seventh coefficient reduces to

\[
\boxed{
D_7(j)=
-\frac j{42}
\left(
84j^6+378j^5-1470j^4+399j^3+2996j^2-3591j+1216
\right).
}
\]

Its Chen discrete curvature is

\[
\begin{aligned}
&2D_7(j)-D_7(j-1)-D_7(j+1)\\
&\qquad=2\left(42j^5+135j^4-280j^3+192j^2+53j-67\right).
\end{aligned}
\]

Putting `m=j-1`, the polynomial inside parentheses becomes

\[
42m^5+345m^4+680m^3+582m^2+347m+75,
\]

so the seventh-order curvature is strictly positive for every `j>=1`.

### 5.4 Uniform tail and theorem

On the retained analytic disk `|t|<=1/(6j)`, the predecessor bounded `|G_j(t)|<2`. Cauchy's estimate therefore gives

\[
|D_m(j)|\le2(6j)^m.
\]

For `n>=12j`, `x=6j/n<=1/2`, hence the post-seventh-order tail satisfies

\[
\begin{aligned}
|\varepsilon_j(n)|
&\le 2\sum_{m\ge8}x^m\\
&\le4x^8\\
&=4\cdot6^8\frac{j^8}{n^8}
<2^{23}\frac{j^8}{n^8}.
\end{aligned}
\]

Taking the Chen second difference costs at most four such errors, so

\[
|2\varepsilon_j-\varepsilon_{j-1}-\varepsilon_{j+1}|
\le2^{25}\frac{(j+1)^8}{n^8}.
\]

All retained deterministic curvatures through order six are nonnegative in the needed direction; the new seventh curvature is strictly positive. The exact factorial base contributes

\[
\log\frac{j+1}{j}\ge\frac1{j+1}.
\]

Therefore the exact source Chen ratio `Q_j(n)` obeys

\[
\log Q_j(n)
\ge
\frac1{j+1}
-2^{25}\frac{(j+1)^8}{n^8}.
\]

If

\[
\boxed{n^8\ge2^{26}(j+1)^9},
\]

then the error term is at most `1/(2(j+1))`, hence `\log Q_j(n)>0`. For the genuinely new sector `j>=67`, this threshold automatically implies the analytic prerequisite `n>=12j`.

Thus this invocation proves the partial theorem

### `NM13-07-P0282-EIGHT-NINTHS-WINDOW-07`

For every `j>=67`,

\[
\boxed{
n^8\ge2^{26}(j+1)^9
\quad\Longrightarrow\quad
F_j(n)^2>F_{j-1}(n)F_{j+1}(n).
}
\]

Chaining with the retained all-`n` theorem for `j<=66`, a simple source-faithful sufficient window is

\[
\boxed{j+1\le \frac{n^{8/9}}8}.
\]

Indeed `8^9=2^27>2^26`. This improves the rigorous growing-defect exponent from `7/8` to `8/9`; it does **not** touch the central `j=Theta(n)` regime and is therefore PARTIAL, not closure.

Exact self-check:

- `artifacts/2026-09-19/p0282_eight_ninths_selfcheck.py`;
- `artifacts/2026-09-19/p0282_eight_ninths_selfcheck.out`.

The self-check brute-forces the length-six star-word identity counts for up to five leaves, enumerates all partitions through `j=12`, verifies both new Plancherel moments, checks the exact `B_7` identity shape-by-shape, checks `D_1,...,D_7` against the exact series, verifies the `D_7` curvature identity and positivity, and verifies exact positive source margins at the theorem thresholds. It terminates `ALL_EXACT_CHECKS_PASS`. It is explicitly a self-check, not P26 or NM13-08 audit.

For `j=1,...,12`, the new theorem threshold sequence is

`21, 33, 46, 59, 72, 85, 99, 113, 127, 142, 156, 171`,

versus the preceding `7/8` threshold sequence

`24, 38, 53, 68, 84, 100, 116, 133, 150, 167, 185, 202`.

## 6. Frozen-metric certificate — row 97

This is secondary bookkeeping attached to actual structural movement, not the primary research route.

For `n=97`, the retained exact all-`n` theorem for defects `j<=66` covers all `k>=31`. Therefore only

\[
k=2,\ldots,30
\]

required new finite computation: 29 cells.

The exact Gessel Bessel/Toeplitz checker

- `artifacts/2026-09-19/p0282_row97_gessel_low.cpp`;
- `artifacts/2026-09-19/p0282_row97_gessel_low.out`

uses 17 independently checked modular primes and CRT. The CRT modulus has 509 bits versus 505 bits for `97!`, and exceeds `2*97!`, so reconstruction is unique in the combinatorial range. The exact Catalan `u_2(97)` cross-check passes. All 29 new inequalities are strictly positive.

The weakest newly computed low-seam ratio is at `k=30`:

\[
\frac{\ell_{97,30}^2}{\ell_{97,29}\ell_{97,31}}
\approx1.10274463000490758>1.
\]

The exact numerator, denominator, and positive margin are archived in the output. The checker ends `ALL_EXACT_CHECKS_PASS`.

Combining these 29 cells with the retained exact `j<=66` theorem covers every interior source inequality in row 97. Therefore

\[
\boxed{N_{\rm exact}:96\to97}.
\]

`unchanged_runs` remains `0 -> 0`; `stuck_recoveries` remains `0 -> 0`.

## 7. Bounded literature refresh — 2026-09-19

Fresh dated queries included:

- `Chen log-concavity conjecture longest increasing subsequence fixed size permutation 2026`;
- `fixed-size Plancherel log-concavity LIS Chen conjecture 2026`;
- `Log-concavity in one-dimensional Coulomb gases and related ensembles Chen longest increasing subsequence`;
- `Kauers Wang longest increasing subsequence D-finite 2026`;
- targeted searches for fixed-size resolutions, Plancherel/content moment approaches, and later citing papers.

The refresh recovered the original Chen fixed-size conjecture, later restricted/Schur-positive progress, Rhoades's representation-theoretic/Hilbert-series formulation, and Baslingker--Krishnapur--Madiman's Poissonized Plancherel theorem, which is explicitly progress toward rather than a solution of the fixed-size conjecture. The newest directly relevant 2026 long-LIS item recovered was Kauers--Wang (submitted 2026-09-02), giving recurrences/D-finiteness rather than fixed-size log-concavity. A current MathDB record still marks Chen's conjecture open.

No source-matching fixed-size resolution, no matching published `n^(8/9)` boundary theorem, and no published statement matching the exact global shadow-compensation identity plus the local-regression obstructions surfaced in this bounded search. This is **negative evidence only**; it does not prove worldwide openness or novelty. Novelty/priority of the new theorem and shadow observations remains **UNVERIFIED**.

## 8. Closure/audit status

The source is **not closed**. The output of this invocation is PARTIAL:

- exact frozen metric advances to `N_exact=97`;
- rigorous growing-defect exponent advances `7/8 -> 8/9`;
- shadow route is sharpened to the exact global size-biased identity, while two local regression shortcuts are exactly refuted;
- all-`n` fixed-defect Chen frontier stays 66;
- all-`n` stronger ULC frontier stays 32.

Required independent audits:

- P26: **NOT PASSED**;
- NM13-08: **NOT PASSED**.

No paper folder is created and nothing is labeled PROVED/CLOSED at source level.

## 9. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-07
  source_id: aim_kpz_followup_2025
  claim_id: P0282
  canonical_dedup_key: chen_log_concavity_conjecture_for_fixed_size_random_permutation_lis
  source_status: OPEN
  worker_status_before: PARTIAL
  worker_status_after: PARTIAL
  metric_name: N_exact
  metric_before: 96
  metric_after: 97
  metric_movement: true
  all_n_chen_fixed_defect_frontier_before: 66
  all_n_chen_fixed_defect_frontier_after: 66
  all_n_ulc_fixed_defect_frontier_before: 32
  all_n_ulc_fixed_defect_frontier_after: 32
  growing_defect_exponent_before: 7/8
  growing_defect_exponent_after: 8/9
  growing_defect_old_window: "j+1 <= n^(7/8)/8"
  growing_defect_new_window: "j+1 <= n^(8/9)/8"
  new_partial_claim_id: NM13-07-P0282-EIGHT-NINTHS-WINDOW-07
  shadow_route_outcome: "exact edge-size-biased rank identity retained; negative-covariance and parentwise average-domination sufficient conditions exactly refuted"
  methods:
    - "#27 SWAP THE QUANTIFIERS (RECYCLED): exact rank-average / edge-size-biased shadow formulation"
    - "#26 HUNT THE SPORADIC CASE (RECYCLED): first exact averaged-shadow obstructions; no adverse seventh coefficient"
    - "#14 FIND THE GROUP ACTING (RECYCLED): Jucys-Murphy/regular-representation moments E[S6], E[C^2 S2]"
    - "#7 TAKE THE LIMIT (RECYCLED): analytic disk/Cauchy tail -> n^(8/9) boundary theorem"
  finite_claim_checkers:
    - proofnet24/NM13-07/artifacts/2026-09-19/p0282_shadow_average_regression_falsifier.py
    - proofnet24/NM13-07/artifacts/2026-09-19/p0282_eight_ninths_selfcheck.py
    - proofnet24/NM13-07/artifacts/2026-09-19/p0282_row97_gessel_low.cpp
  finite_claim_outputs_end_all_exact_checks_pass: true
  self_checks_are_independent_audits: false
  p26_audit: NOT_PASSED
  nm13_08_audit: NOT_PASSED
  unchanged_runs_before: 0
  unchanged_runs_after: 0
  stuck_recoveries_before: 0
  stuck_recoveries_after: 0
```

## 10. Next step

The primary next route is **not** another row census. The shadow calculation now says exactly what a proof must contain: a global compensation principle for the edge-size-biased average

\[
\frac{\mathbb E[e(S)a_r(S)]}{\mathbb E[e(S)]}
\le \mathbb E[q_r(S)],
\]

without relying on false parentwise or covariance monotonicity. The next run should try to obtain that from a two-edge double count, a size-biased coupling, or a martingale/negative-dependence statement formulated at the whole-rank level. If that route fails honestly, the fallback is an eighth-order Plancherel sign test; an adverse first surviving mixed moment is to be recorded as an obstruction rather than forced into an exponent claim.

## 11. Model / reasoning control and P26 modification limitation

The requested runtime remains **GPT-6 / maximum reasoning in prompt text only**. The task-control surface available in this invocation exposes title/prompt, time/scheduling controls, timing mode, enabled state, listing, and updates, but it exposes **no bindable model-family field and no bindable reasoning-effort field**. Therefore I cannot truthfully say GPT-6/maximum was set by the scheduler. Enforcing such a requirement would need an authorized scheduler/product/API/admin surface with persistent model and reasoning routing fields plus authenticated per-run applied-runtime attestation.

The historical P26 `You cannot modify this task` event is an authorization-context boundary, not evidence that the owner may bypass permissions. Later repository continuity records a successful P26 update from an authorized context. The lawful workaround is to use the task-owning/authorized context, or an approved platform/admin/API/support path for that same task; never duplicate the task to evade ownership and never change permissions without authorization.
