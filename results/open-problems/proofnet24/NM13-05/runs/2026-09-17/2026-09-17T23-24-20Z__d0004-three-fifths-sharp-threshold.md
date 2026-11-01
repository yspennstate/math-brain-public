Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. MOVEMENT: `epsilon_sep >= 1/2` -> `epsilon_sep = 3/5`. Methods actually tried: #18, #19, #24.**

# NM13-05 — D0004 exact three-fifths threshold for the frozen smooth two-bump family

Run UTC: 2026-09-17T23:24:20Z  
Track: `NM13-05 Coupling Extremal Problems`, CLOSABLE OUTSIDE.  
Canonical source/claim: `D0004`, `operations/claims/D0004.md`.  
Parent source status after this run: **OPEN / PARTIAL**.  
Frozen-family metric status after this run: **exactly solved: `epsilon_sep = 3/5`**.

## 1. Continuity, ownership, exclusions, and runtime controls

I continued the already admitted D0004 target; I did not reopen intake or create a second claim.

Canonical identity remains:

- Ruodu Wang, *Current Open Questions in Complete Mixability*, Probability Surveys 12 (2015), 13–32, DOI `10.1214/14-PS250`, arXiv:`1411.6190v3`, Section 2.4, Open Problem 4;
- canonical dedup key `complete_mixability_open_2014::open_problem_4`;
- SHA256 residue modulo 13: `4`, matching NM13-05's exclusive shard;
- exclusive owner: NM13-05 under `operations/claims/D0004.md`.

Before doing mathematics I reread/recovered the current controlling surfaces required by the owner: `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; the later owner-authorized NM13 deployment amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; the D0004 claim; the D0004 intake/attempt history; my newest NM13-05 report; and the newest accessible neighboring NM13-04 and NM13-06 reports. NM13-06 remains admission-pending and has not supplied an audit. Historical attempt `D0004-A001` (the n=2 case) remains preserved and is not recounted as progress.

The newest NM13-05 report established `D0004-SYM3`, the universal n=3 symmetry theorem for the source norm inequalities, and then improved the frozen-family nonmixability threshold from `1/3` to `1/2` by the sharp support-bounded absolute-moment inequality `E|X| <= 2M/3`. It also produced connected-support smooth counterexamples and an asymmetric finite counterexample. Its actual method triple was #5/#15/#20, so this run did not repeat it.

Large repository roots and JSONL inventories are connector-truncated when fetched wholesale. I therefore used their current root views plus exact target/claim/report/attempt retrieval and canonical-ID searches. I do not treat truncated visibility as proof that inaccessible history is empty. No current conflicting claim, release, handoff, posted D0004 closure, or source-specific correction superseding this assignment was recovered.

The current task-control surface still exposes prompt/title, schedule or offset, timing mode, and enabled state, but **no binding model-family selector and no reasoning-effort selector**. Therefore the requested `GPT-6 / maximum` remains prompt text only. This invocation actually reports GPT-5.6 Sol; reasoning telemetry is unavailable, hence `UNVERIFIED`. The historical `You cannot modify this task` response for one P26 context is an authorization/context issue, not permission to duplicate or bypass the task. The current repository also records a later successful P26 update in another authorized context. A denied edit must be handled through the owning account/workspace or an authorized product/admin/support surface; no support escalation is claimed here.

## 2. Exact source and fresh bounded literature check

Wang's Theorem 5 gives, for an integrable law `F` with mean `mu`, necessary inequalities for n-complete mixability: for every law-determined norm, every real `t`, and `s=(n mu-t)/(n-1)`, the positive- and negative-part norms are bounded by the corresponding factor `(n-1)`. Open Problem 4 asks under what additional conditions, possibly smoothness conditions, these all-law-determined-norm inequalities become sufficient for n-complete mixability. The source separately records positive classes such as symmetric unimodal continuous densities and monotone densities under the appropriate mean condition.

Fresh bounded searches dated 2026-09-17 UTC used the exact Open Problem 4 wording, `law-determined norm complete mixability`, `smooth complete mixability sufficient condition`, `joint mixability negative dependence 2024 2025 2026`, the source title, and Ruodu Wang's current publication/working-paper listings. I rechecked:

- Wang's 2015 source / arXiv:1411.6190;
- Puccetti–Wang, *Detecting complete and joint mixability* (2015);
- later mixability sufficient-class literature referenced by the source and subsequent surveys;
- Koike–Lin–Wang, *Joint Mixability and Notions of Negative Dependence* (2024), which develops negative-dependence/optimal-transport viewpoints but does not present a resolution of Wang Open Problem 4;
- Ruodu Wang's current publication and working-paper pages.

I did not locate a later source-matching resolution of the general Open Problem 4, nor a paper stating the exact three-fifths frozen-family theorem below. This is **bounded negative evidence only**, not proof of worldwide openness or a novelty certificate. The fractional-matching/transport reformulation and elementary cut duality used below are standard mechanisms in spirit; no novelty is claimed merely for naming them.

## 3. Frozen metric and statement of movement

The claim file freezes, for `epsilon>0`, the family

`F_epsilon = (1/2) Law(1+U_epsilon) + (1/2) Law(-1+U_epsilon)`,

where `U_epsilon` has an even `C^infinity` density, is strictly positive on `(-epsilon,epsilon)`, and vanishes outside `[-epsilon,epsilon]`.

The tracked quantity is

`epsilon_sep = sup{epsilon : every F_epsilon in this family is proved to satisfy all n=3 Theorem-5 law-determined-norm inequalities but is not 3-CM}`.

Before this run, the certified statement was

`epsilon_sep >= 1/2`.

After this run,

`epsilon_sep = 3/5`.

The family, normalization, source inequality, and meaning of the metric are unchanged.

The proof has two independent mathematical halves:

1. every frozen member with `0<epsilon<3/5` is not 3-CM;
2. for every `epsilon>3/5` there exists a frozen member that **is** 3-CM.

Because `D0004-SYM3` already proves that every member of the frozen family satisfies both source inequalities for every law-determined norm and every threshold, these two halves determine the supremum exactly. The endpoint `epsilon=3/5` itself need not be classified to determine the supremum.

---

## 4. Method #18 — SAY IT IN ANOTHER LANGUAGE: zero-sum coupling as a Schur-triple fractional matching

Fix `0<epsilon<1` and write

`a = 1-epsilon`, `b = 1+epsilon`.

For a frozen marginal let

`K = Law(1+U_epsilon)`.

Because `U_epsilon` is even, `K` is supported on `[a,b]`, is symmetric about 1, and has a density strictly positive throughout `(a,b)`.

Suppose, for contradiction, that a frozen marginal is 3-CM. Let `(X1,X2,X3)` be a complete mix, so the three coordinates have the frozen marginal and

`X1+X2+X3=0` almost surely.

Since `epsilon<1`, the marginal support avoids zero. Therefore every realized zero-sum triple has exactly two entries of one sign and one entry of the opposite sign. If `p,q` are the magnitudes of the same-sign pair and `r` is the magnitude of the opposite-sign entry, then

`p,q,r in [a,b]`,  and  `r=p+q`.

Thus every complete mix induces a random **Schur triple** `(p,q,r)` on

`T_epsilon = {(p,q,r) in [a,b]^3 : p+q=r}`.

Moreover the average empirical vertex law of this random Schur triple is exactly `K`. Indeed, `|Xi|` has law `K` for each i: on the positive bump it is `1+U_epsilon`, while on the negative bump it is `1-U_epsilon`, which has the same law by evenness. Hence for every bounded measurable `phi`,

`E[phi(p)+phi(q)+phi(r)] = sum_i E phi(|Xi|) = 3 int phi dK`.

Equivalently,

`K = (Law(p)+Law(q)+Law(r))/3`.

This is the source-faithful transport/fractional-matching reformulation: 3-CM is possible only if the magnitude law is the average vertex marginal of a probability measure on the zero-sum/Schur hypergraph.

### A sharp cut dual obstruction

Assume now

`1/3 <= epsilon < 3/5`.

Choose a number `c` with

`max(a,b/2) <= c < 2a`.

Such a `c` exists exactly because

`b/2 < 2a`

is equivalent to

`(1+epsilon)/2 < 2(1-epsilon)`

which is equivalent to

`epsilon < 3/5`.

Set

`h = 2-c`,
`L = [a,c]`,
`H = [h,b]`.

Reflection `x -> 2-x` carries `L` onto `H`, so symmetry of `K` gives

`K(L)=K(H)`.

Consider any feasible Schur triple `(p,q,r)` with `p+q=r`.

First, neither summand can lie in `H`. Since the other summand is at least `a` and `r<=b`,

`p <= b-a = 2epsilon`,  and similarly `q <= 2epsilon`.

But `c<2a=2-2epsilon` implies

`h=2-c > 2epsilon`.

Thus `p,q<h`, so among the three vertices only the sum `r` can lie in `H`. Consequently

`N_H := 1_H(p)+1_H(q)+1_H(r) <= 1`.

Second, at least one summand lies in `L`. If both `p>c` and `q>c`, then

`r=p+q > 2c >= b`,

contradicting `r<=b`. Therefore

`N_L := 1_L(p)+1_L(q)+1_L(r) >= 1`.

Pointwise we have `N_L >= N_H`. But the average-vertex identity and `K(L)=K(H)` give

`E N_L = 3K(L) = 3K(H) = E N_H`.

A nonnegative random variable `N_L-N_H` with zero expectation vanishes almost surely. Hence every Schur triple in the coupling satisfies

`N_L=N_H=1`.

Since only `r` can lie in `H`, every used sum satisfies `r>=h`, while both summands are at most `2epsilon`. Therefore no vertex of any used triple lies in the open interval

`(2epsilon,h)`.

This interval is nonempty because `h>2epsilon`. The average-vertex law would therefore satisfy

`K((2epsilon,h))=0`.

That is impossible: the frozen density is strictly positive on all of `(a,b)`, and here `(2epsilon,h)` is a nonempty open subinterval of `(a,b)`. (For `epsilon>=1/3`, `2epsilon>=a`; also `h<=b` because `c>=a`.)

We have proved:

### Theorem D0004-SCHUR-CUT

Every frozen member is non-3-CM for

`1/3 <= epsilon < 3/5`.

For `0<epsilon<1/3`, the earlier elementary support obstruction applies: two same-sign magnitudes are each at least `a`, so their sum is at least `2a>b`, and no zero-sum triple exists. Combining the two ranges gives

`every frozen F_epsilon is non-3-CM for 0<epsilon<3/5`.

By `D0004-SYM3`, every one of these laws nevertheless satisfies all n=3 source norm inequalities. Thus

`epsilon_sep >= 3/5`.

This is a genuine strengthening of the previous `1/2` absolute-moment obstruction.

---

## 5. Method #19 — MAKE IT AN ALGORITHM: an explicit complete mix beyond three-fifths

To prove the opposite inequality for the **same frozen metric**, it is enough to construct, for every `epsilon>3/5`, one member of the frozen family that is 3-CM.

The construction starts with an exact boundary complete mix at radius `3/5` and then smooths it by adding an independent smooth complete mix.

### Step 1: a boundary Schur-triple process

Let

`T ~ Uniform(4/5,6/5)`.

Conditional on `T=t`, let

`L | (T=t) ~ Uniform(2/5, t-2/5)`.

Define

`S = T-L`,
`M = 2-T`,
`R = 2-S`.

Conditional on `T=t`, the interval for `L` is `(2/5,t-2/5)`. Reflection inside that interval sends `L` to

`t-L = S`,

so `S` has the same conditional law as `L`; hence unconditionally

`Law(S)=Law(L)`.

The ranges are

`L in (2/5,4/5)`,
`M in (4/5,6/5)`,
`R in (6/5,8/5)`.

Moreover

`L+M = L + 2 - T = L + 2 - (L+S) = 2-S = R`.

Thus `(L,M,R)` is a Schur triple exactly on the three natural boundary zones.

Because `T` is uniform on `(4/5,6/5)`, `M=2-T` has the same law as `T` and is symmetric about 1. Since `R=2-S` and `S` has the same law as `L`, the law of `R` is the reflection of the law of `L` about 1.

Define the magnitude law

`K0 = (Law(L)+Law(M)+Law(R))/3`.

Then `K0` is symmetric about 1 and supported on `[2/5,8/5]`.

Its density is positive almost everywhere on the full open interval `(2/5,8/5)`:

- `M` has constant positive density on `(4/5,6/5)`;
- for `ell in (2/5,4/5)`, the conditional construction gives a strictly positive density

  `f_L(ell) = (5/2) int_{ell+2/5}^{6/5} dt/(t-4/5) > 0`;

- `R` has the reflected density `f_R(r)=f_L(2-r)>0` on `(6/5,8/5)`.

Now take the zero-sum triple

`(L,M,-R)`.

It sums to zero identically because `L+M=R`. Randomly permute its coordinates, and independently multiply all three coordinates by a common Rademacher sign. The result is an exchangeable complete mix. Each coordinate has a symmetric marginal whose magnitude law is `K0`.

Let

`U0 = K0-1`

in distribution. Symmetry of `K0` about 1 says that `U0` is even and supported on `[-3/5,3/5]`. Therefore the common marginal can be written exactly in frozen form

`F0 = (1/2) Law(1+U0) + (1/2) Law(-1+U0)`.

This boundary law is 3-CM, although `U0` is not required to be smooth.

### Step 2: smooth while preserving the zero-sum coupling

Fix an arbitrary

`epsilon > 3/5`

and put

`delta = epsilon-3/5 > 0`.

Let `V_delta` have the standard even compactly supported `C^infinity` bump density

`g_delta(x) = C_delta exp(-1/(delta^2-x^2)) 1_{|x|<delta}`,

with normalizing constant `C_delta`.

This density is symmetric and unimodal. The classical sufficient theorem quoted in Wang's source therefore gives a 3-complete mix `(Z1,Z2,Z3)` with each `Zi ~ V_delta`. Take it independent of the complete mix constructed above. Adding coordinates gives another complete mix because

`sum_i (Xi+Zi) = sum_i Xi + sum_i Zi = 0`.

Hence the convolution

`F0 * V_delta`

is 3-CM.

Set, in marginal distribution,

`U = U0 + V_delta`

with independent summands. Then `U` is even and supported on

`[-3/5-delta, 3/5+delta] = [-epsilon,epsilon]`.

The density of `U0` is positive almost everywhere on `(-3/5,3/5)`. Convolution with the bump `g_delta` is `C^infinity`. For every `x` with `|x|<epsilon`, the intervals

`(-3/5,3/5)` and `(x-delta,x+delta)`

have a nonempty open overlap. On that overlap the first density is positive almost everywhere and `g_delta(x-y)>0`; therefore the convolution density is **strictly positive at x**. It vanishes outside `[-epsilon,epsilon]`.

Finally, convolution distributes over the two frozen bumps:

`F0 * V_delta
 = (1/2) Law(1+U0+V_delta) + (1/2) Law(-1+U0+V_delta)
 = (1/2) Law(1+U) + (1/2) Law(-1+U)`.

Thus `F0*V_delta` is a bona fide member of the **same frozen family at radius epsilon**, and it is 3-CM.

We have proved:

### Theorem D0004-SMOOTH-MIX-ABOVE-3/5

For every `epsilon>3/5`, there exists a frozen `C^infinity`, strictly-positive-interior member at radius `epsilon` that is 3-completely mixable.

Therefore no `epsilon>3/5` belongs to the defining set for `epsilon_sep`, and

`epsilon_sep <= 3/5`.

Together with the cut obstruction,

### Theorem D0004-THREE-FIFTHS

`epsilon_sep = 3/5`.

This is an exact theorem about the frozen source-faithful family. It does **not** solve Wang's full Open Problem 4.

---

## 6. Method #24 — FIND THE EXTREMAL OBJECT: why three-fifths is the exact cut boundary

The preceding proofs expose the extremal geometry rather than merely sandwiching a number.

The cut argument requires a separator `c` obeying

`b/2 <= c < 2a`.

The interval of choices collapses exactly when

`b/2 = 2a`,

that is

`(1+epsilon)/2 = 2(1-epsilon)`,

which gives

`epsilon=3/5`.

At that value the magnitude interval is

`[2/5,8/5]`

and the forced three-zone partition is

`[2/5,4/5]`, `[4/5,6/5]`, `[6/5,8/5]`.

The explicit process from Method #19 saturates the cut exactly: each Schur triple has one magnitude in the low zone, one in the middle zone, and one in the high zone, with

`low + middle = high`.

Thus the dual cut obstruction and the constructive coupling meet at the same `3/5` boundary. This also shows why the previous absolute-moment threshold `1/2` was not the true frozen-family boundary: the moment inequality sees only the largest magnitude budget, while the sharp obstruction also uses the **location of mass across reflected low/high cuts**.

The exact boundary law itself need not satisfy the frozen `C^infinity` hypothesis, and I have not classified whether every/some smooth frozen law at exactly `epsilon=3/5` is 3-CM. That endpoint question does not affect `epsilon_sep`, whose value is now exact.

---

## 7. What is proved, what is not, and why no new checker was manufactured

New proved internal results this run:

1. `D0004-SCHUR-CUT`: a source-faithful fractional-matching/cut obstruction proving every frozen member non-3-CM for `epsilon<3/5`.
2. `D0004-SMOOTH-MIX-ABOVE-3/5`: an explicit complete-mix construction followed by smooth complete-mix convolution, producing a frozen smooth 3-CM member for every `epsilon>3/5`.
3. `D0004-THREE-FIFTHS`: the frozen metric is exactly `epsilon_sep=3/5`.
4. Extremal interpretation: the cut feasibility condition `b/2<2a` becomes equality precisely at `3/5`, and the boundary construction saturates its three zones.

This run did **not** create a finite checker just to satisfy bookkeeping. The new claims are theorem-sized analytic statements, so the required validation is the complete argument on this page. There is no finite enumeration core whose correctness would be strengthened by an arithmetic checker. The previous asymmetric finite witness and its exact checker remain valid historical evidence but are not reused as movement here.

Not proved:

- a full characterization of all marginals satisfying Wang's all-law-determined-norm inequalities that are n-CM;
- source-level sufficient extra hypotheses answering Open Problem 4 in general;
- a classification of the exact smooth endpoint `epsilon=3/5`;
- novelty beyond the bounded literature screen;
- any P26 or NM13-06 audit.

Therefore the parent source remains **OPEN / PARTIAL**, even though the frozen metric is now exactly solved.

## 8. Counters, audit state, and next new-method route

Because the frozen metric moved from a one-sided lower bound to an exact value:

- unchanged-run count before: `0`;
- unchanged-run count after: `0`;
- stuck-recovery count: `0`;
- P26 audit: `NOT_REQUESTED / NOT_PASSED`;
- NM13-06 audit: `NOT_REQUESTED / NOT_PASSED`.

Do not repeat #18/#19/#24 next run.

The next research triple is:

- **#3 PROVE SOMETHING STRONGER:** seek a source-level sufficient condition phrased directly in terms of zero-sum hypergraph fractional matchings plus a regularity/interiority hypothesis, strong enough to contain the positive classes already known but still checkable;
- **#11 DUALIZE:** derive the full measurable LP/Kantorovich dual for n=3 complete mixability and identify whether the source's all-law-determined-norm inequalities correspond to only a proper subcone of dual witnesses;
- **#27 SWAP THE QUANTIFIERS:** instead of asking whether all source norm inequalities imply one coupling, ask for a single finite or parametrized family of dual witnesses that detects every nonmixable compactly supported symmetric law, and determine exactly where this stronger statement fails.

The frozen `epsilon_sep` metric is now saturated and must not be silently replaced by a new quantity. Any later report on D0004 must continue to state `epsilon_sep=3/5` before/after while distinguishing source-level progress from metric movement. If subsequent runs cannot advance the source obligation, the closable-target unchanged/stuck/rotation rules still apply.

## 9. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: NM13-05
  category: CLOSABLE OUTSIDE
  source_id: D0004
  claim_id: D0004
  canonical_dedup_key: complete_mixability_open_2014::open_problem_4
  status: PARTIAL
  source_status: OPEN
  target: Wang_Open_Problem_4_all_law_determined_norm_sufficiency
  metric:
    name: epsilon_sep
    family: smooth_even_two_bump_F_epsilon_frozen_in_claim
    before: ">= 1/2"
    after: "= 3/5"
    movement: exact_threshold_certified
  methods:
    actually_attempted: [18, 19, 24]
    outcomes:
      18: Schur_triple_fractional_matching_reformulation_and_sharp_reflected_cut_obstruction
      19: explicit_boundary_complete_mix_plus_smooth_complete_mix_convolution_for_every_epsilon_above_3_over_5
      24: extremal_cut_boundary_identified_and_saturated_at_three_fifths
  claims_this_run:
    - D0004-SCHUR-CUT
    - D0004-SMOOTH-MIX-ABOVE-3/5
    - D0004-THREE-FIFTHS
  counters:
    unchanged_run_count_before: 0
    unchanged_run_count_after: 0
    stuck_recovery_count: 0
  ownership:
    owner: NM13-05
    existing_claim_preserved: true
    new_claim_created: false
    conflict_found: false
  audits:
    P26: NOT_REQUESTED
    NM13-06: NOT_REQUESTED
  literature_check:
    date_utc: 2026-09-17
    scope: Wang_2015_source_exact_wording_plus_current_mixability_negative_dependence_author_publication_searches
    source_matching_resolution_found: false
    caveat: bounded_negative_search_not_worldwide_openness_or_novelty_certificate
  artifacts:
    new_finite_checker: none_not_applicable_analytic_theorem
  next_methods: [3, 11, 27]
  next_step: derive_full_n3_transport_dual_and_test_source_level_sufficiency_without_changing_frozen_metric
```

END OF IMMUTABLE NM13-05 RUN REPORT
