Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO METRIC MOVEMENT: `D_rev,0` stayed `0 -> 0`. Section-B methods actually tried: #3, #17, #30.**

# NM13-01 — P0292 single-crossing spectral modes and the full 3-state star classification

**Track:** NM13-01  
**Category:** CLOSABLE OUTSIDE  
**Source ID:** P0292  
**Claim:** `operations/claims/P0292.md` (exclusive owner NM13-01; canonical shard residue 0 mod 13)  
**Source:** Lasse Leskelä, *Ross's second conjecture and supermodular stochastic ordering*, Queueing Systems 100 (2022), Problem 4 on source page 215.  
**Source status:** OPEN in full generality.  
**Track status after this run:** PARTIAL, with a complete new restricted-class theorem.  
**Frozen metric:** `D_rev,0`, the normalized frozen-limit first-order supermodular speed defect over finite stationary irreducible reversible CTMCs.  
**Metric before / after:** `0 -> 0` (no movement; the sharp local constant was already exactly determined in the first NM13-01 run).  
**Unchanged runs since last metric movement:** 2.  
**Stuck recoveries used:** 0.  
**Audits:** P26 NOT REQUESTED / NOT PASSED; NM13-02 NOT REQUESTED / NOT PASSED.

## 1. Continuity and current controlling state

I continued the admitted P0292 target rather than restarting intake. Before doing new mathematics I reread/recovered the current controlling surfaces required by the owner: `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; the later owner-authorized NM13 deployment amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`; `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; the current P0292 claim; my newest two NM13-01 reports; the historical P0292/P0291 attempt material; and the newest neighboring NM13-02 report. No shared root or peer file was edited.

The published source was rechecked directly in the accepted-author PDF. Source page 215 labels the characterization as **Problem 4** and asks for a simple necessary-and-sufficient condition for stationary ergodic CTMCs under which

`c1 <= c2  ==>  lambda_{c1} >=_sm lambda_{c2}`.

The existing claim remains exclusive to NM13-01. The historical campaign state is important: P0292-A002 had already proved failure for the ordered three-state star when `b3>b2`, proved the equal-return case `b2=b3`, and conjectured that the entire star family satisfies the source order exactly when `b2>=b3`. Its `b2>b3` half had only LP evidence and was the live obstruction. I do not count the recovered equality/failure results as new work.

The previous NM13-01 run also closed the frozen-endpoint/Taylor route: for any stationary process the fully frozen coupling is comonotone, so higher derivatives at `c=0` cannot provide the desired positive defect. That is why this run moved to positive gaps rather than manufacturing another local certificate.

## 2. Methods actually tried

### #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

I checked the dependence-in-lag literature surrounding the source: Hu–Pan (2000), Kulik (2004), and Kulik–Wichelhaus (2007), in addition to Leskelä's source and the papers it cites. Hu–Pan gives dependence-comparison conditions for stationary Markov processes; Kulik proves a lag-covariance result for a special nonmonotone doubly stochastic class; Kulik–Wichelhaus develops supermodular-type lag comparisons under monotonicity hypotheses. These are genuinely adjacent, but the bounded check did not recover a theorem that directly gives Leskelä's **all-finite-dimensional** speed ordering for the asymmetric star below. In particular, Kulik's 2004 result is bivariate/covariance-oriented, whereas P0292 needs every finite grid and every supermodular test.

Outcome: **useful route guidance, no source-matching prior theorem found in this bounded search**. The spectral sign-change idea below should not be advertised as novel on the strength of a negative search; novelty remains UNVERIFIED.

### #30 — DO ONE SCALE / ONE DIRECTION AT A TIME

I froze every observation gap except one positive gap `g`. Reversibility then gives an exact two-exponential spectral representation. This isolates the whole problem at that gap into the signs of two spectral coefficients. The historical scripts had numerically observed those coefficients to be nonnegative in the unresolved `b2>b3` star regime; this run proves that fact for arbitrary dimension and arbitrary surrounding gaps.

Outcome: **successful**.

### #3 — PROVE SOMETHING STRONGER

Instead of proving only the historical endpoint condition `[E2]`, I proved a path-space lemma for any three-state reversible chain whose relevant signed eigenmeasure has one sign change at an extreme. Applied separately to both nonconstant modes, it makes **each spectral coefficient nonnegative**, not merely the derivative combination. This gives a new general sufficient condition for reversible three-state chains and completely settles the previously open strict `b2>b3` star regime.

Outcome: **successful; complete restricted-class theorem below**.

## 3. New theorem: a path-order criterion from signed eigenmodes

Let the state space be `1<2<3`, let `P_t` be a finite-state Markov semigroup, and let `r=(r1,r2,r3)` be a nonzero signed row measure with total mass zero satisfying

`r P_t = exp(-mu t) r` for every `t>=0`, with `mu>0`.

For a grid `0=t0<t1<...<tm`, define the signed cylinder measure

`Gamma_r(x0,...,xm) = r(x0) prod_{j=1}^m P_{t_j-t_{j-1}}(x_{j-1},x_j)`.

### Lemma 1 — extreme single-crossing eigenmeasures order the whole path

If, after multiplying `r` by `-1` if necessary, either

`r1 <= 0, r2 >= 0, r3 >= 0`                                      (A)

or

`r1 <= 0, r2 <= 0, r3 >= 0`,                                     (B)

then for every finite grid and every upper set `U` in the coordinatewise order on `{1,2,3}^{m+1}`,

`Gamma_r(U) >= 0`.

Equivalently, writing the Jordan decomposition `Gamma_r=Gamma_r^+-Gamma_r^-`, the normalized negative part is stochastically dominated by the normalized positive part on the entire finite path space.

#### Proof

Induct on `m`. For `m=0`, the nontrivial upper sets are `{3}` and `{2,3}`. In either sign pattern,

`r({3})=r3>=0`,

`r({2,3})=r2+r3=-r1>=0`.

Now let `m>=1`, let `U_i` be the section of an upper set `U` at first coordinate `i`, and let

`H_i(V)=P_i((X_{t1},...,X_{tm}) in V)`.

Upperness gives nested sections

`U_1 subset U_2 subset U_3`.

In case (A), use the bottom section as baseline:

`Gamma_r(U)`
` = sum_i r_i H_i(U_1) + r2 H_2(U_2\U_1) + r3 H_3(U_3\U_1)`.

The last two terms are nonnegative. For the first term, condition on `X_{t1}` and use the left-eigenmeasure identity:

`sum_i r_i H_i(U_1) = exp(-mu t1) Gamma_r^{(m-1)}(U_1) >= 0`

by the induction hypothesis.

In case (B), use the top section as baseline:

`Gamma_r(U)`
` = sum_i r_i H_i(U_3) - r1 H_1(U_3\U_1) - r2 H_2(U_3\U_2)`.

Again the last two terms are nonnegative because `r1,r2<=0`, and the first term is nonnegative by the same eigenmeasure/induction argument. This proves the lemma. `QED`

The lemma is elementary; I make no novelty claim for it as an abstract statement.

### Lemma 2 — two ordered signed blocks give a nonnegative supermodular coefficient

Let `Sigma_L` and `Sigma_R` be zero-mass signed measures on two finite coordinate blocks, and suppose each has nonnegative mass on every upper set. Then for every supermodular function `phi` on the concatenated coordinates,

`int phi(l,r) Sigma_L(dl) Sigma_R(dr) >= 0`.

#### Proof

Normalize the positive and negative Jordan parts. Upper-set nonnegativity is exactly the finite-poset stochastic order

`L^- <=_st L^+`, `R^- <=_st R^+`.

By Strassen, couple them with `L^-<=L^+` and `R^-<=R^+` coordinatewise, taking the two couplings independently. Supermodularity gives the block cross-difference inequality

`phi(L^+,R^+) + phi(L^-,R^-) - phi(L^+,R^-) - phi(L^-,R^+) >= 0`,

because the meet and join of `(L^+,R^-)` and `(L^-,R^+)` are `(L^-,R^-)` and `(L^+,R^+)`. Taking expectations and restoring the common Jordan masses proves the claim. `QED`

### Theorem 3 — two-mode single-crossing criterion for reversible three-state CTMCs

Let `X` be a stationary irreducible reversible CTMC on `1<2<3`, with two nonzero eigenvalues `-mu1,-mu2`. Let `r^(j)=pi v_j` be the signed left eigenmeasure corresponding to the `j`th nonconstant right eigenfunction. If **each** `r^(j)` can be oriented to satisfy (A) or (B), then

`c1 <= c2  ==>  X(c1 * .) >=_sm X(c2 * .)`

in the full all-finite-dimensional sense of Leskelä's equation (2).

#### Proof

Fix a finite observation grid and a supermodular `phi`. Freeze all gaps except one gap `g` between adjacent coordinates `k,k+1`. By stationarity and the Markov property,

`F(g)=sum_{x,y} pi(x) P_g(x,y) Phi(x,y)`,

where `Phi(x,y)` is the conditional expectation of `phi` given the two boundary states, with the prefix and suffix conditionally independent.

Reversibility gives the exact spectral expansion

`F(g)=C + A1 exp(-mu1 g) + A2 exp(-mu2 g)`,

with

`Aj = (1 / ||v_j||_pi^2) sum_{x,y} r^(j)(x) r^(j)(y) Phi(x,y)`.

For each `j`, form the signed measure on the left coordinate block by mixing the conditional prefix laws with weights `r^(j)(x)`, and similarly form the signed measure on the right block with weights `r^(j)(y)`. Reversibility identifies the time-reversed prefix with the same semigroup, so Lemma 1 applies to both signed block measures (coordinate reversal is an order isomorphism). Conditional independence then identifies the numerator of `Aj` with the product-signed-measure integral in Lemma 2. Therefore

`A1>=0` and `A2>=0`.

Hence `F(g)` is nonincreasing in `g`. Since the chosen gap was arbitrary, increase the scaled gaps from `c1` to `c2` one at a time. The expectation of every supermodular test can only decrease, which is exactly the source process order. `QED`

This theorem is stronger than the star calculation that motivated it, but it is still a restricted sufficient condition, not Leskelä's requested general characterization.

## 4. Corollary: the historical three-state star conjecture is completely resolved

Consider the ordered reversible star

`Q = [[-(a2+a3), a2, a3],`
`     [b2,       -b2, 0 ],`
`     [b3,        0, -b3]]`,

with `a2,a3,b2,b3>0`. Its stationary distribution is proportional to

`(1, a2/b2, a3/b3)`.

Assume first that `b2>b3`. The positive nonzero decay rates are the roots of

`p(mu)=mu^2-(a2+a3+b2+b3)mu + a2 b3 + a3 b2 + b2 b3`.

At the two return rates,

`p(b3)=a3(b2-b3)>0`,

`p(b2)=-a2(b2-b3)<0`.

Thus, writing `0<mu1<mu2`,

`b3 < mu1 < b2 < mu2`.

For a nonzero mode with decay `mu`, normalize the right eigenfunction by `v(1)=1`. The leaf equations give

`v(2)=b2/(b2-mu)`, `v(3)=b3/(b3-mu)`,

and the signed left eigenmeasure is therefore proportional to

`r(mu) = (1, a2/(b2-mu), a3/(b3-mu))`.

Consequently:

- at `mu1`, the signs are `(+,+,-)`, which after reversal are `(-,-,+)`;
- at `mu2`, the signs are `(+,-,-)`, which after reversal are `(-,+,+)`.

Both modes satisfy Lemma 1. Theorem 3 therefore proves the full source order for **every** `a2,a3>0` whenever `b2>b3`.

The equality case `b2=b3` was already proved in the historical P0291/P0292 memo by the two-state skeleton plus exact supermodular block certificate, and is not new here.

For `b3>b2`, the historical failure can also be seen directly from the same spectrum. Then the slow root lies between `b2` and `b3`, so the slow coefficient in `P_t(1,3)-pi3` is positive. Hence `P_t(1,3)` approaches `pi3` from above at large `t`; therefore the supermodular lower-orthant test

`phi(x,y)=1{x<=1} 1{y<=2}`

has expectation `pi1(1-P_t(1,3))` increasing for all sufficiently large `t`, contradicting the required gap monotonicity.

Combining the new strict case with the two recovered historical pieces gives the exact restricted classification:

> **STAR CLASSIFICATION.** For the ordered three-state star above, Leskelä's all-finite-dimensional speed order holds **if and only if**
>
> `b2 >= b3`.

This resolves the specific star-family conjecture recorded in P0292-A002. It does **not** close source Problem 4, which asks for a general necessary-and-sufficient condition for stationary ergodic CTMCs.

Internal claim label for audit/reference: `NM13-01-P0292-STAR-SINGLE-CROSSING-03`. Novelty/prior-art status: **UNVERIFIED**.

## 5. Why this is not a checker-driven result

The new claim is theorem-sized and the complete proof is on this page. It has no finite enumeration core, so I did not manufacture an exact-arithmetic artifact merely to create a receipt. The historical LP maps remain useful route-selection evidence only; they are not used as proof of Theorem 3 or of the star classification.

As an internal sanity check during the derivation, I evaluated the two spectral-coefficient LPs on several strict `b2>b3` parameter choices and finite grids; both minima were numerically zero up to solver tolerance, consistent with the proof. Those computations are not promoted as certificates and no mathematical statement depends on them.

## 6. Bounded literature/status check — 2026-09-17 UTC

Fresh checks in this invocation covered:

- the published accepted-author source PDF, DOI `10.1007/s11134-022-09824-0`, including source page 215 (Problem 4);
- Leskelä's current author/publication page and exact-title searches;
- exact/problem-wording searches for later resolutions;
- Hu & Pan, *Comparisons of dependence for stationary Markov processes* (2000), DOI `10.1017/S0269964800143025`;
- Kulik, *Monotonicity in lag for nonmonotone Markov chains* (2004), DOI `10.1017/S0269964804184040`;
- Kulik & Wichelhaus, *Dependence in Lag for Markov Chains on Partially Ordered State Spaces with Applications to Degradable Networks* (2007), DOI `10.1080/15326340701646007`.

The bounded search did not recover a later source-matching solution to Problem 4 or an explicit published statement of the asymmetric-star iff criterion above. The adjacent papers address lag dependence under conditions such as stochastic monotonicity, double stochasticity, or bivariate covariance/concordance structure. **This negative search is not proof of worldwide openness or novelty.** A publication-level novelty check would need broader citation-graph and theorem-by-theorem reconciliation.

## 7. Metric, status, counters, and next route

The frozen metric cannot honestly be changed by this theorem: `D_rev,0` remains exactly `0`, so this is a **no-metric-movement** run even though the mathematical restricted class advanced substantially. This is the second consecutive run without metric movement after the first run measured the sharp value.

Source Problem 4 remains **OPEN**; NM13-01 remains **PARTIAL**. No closure package is created, and no audit is presumed.

The strongest next source-relevant target is the historical candidate characterization for **all reversible three-state chains**. The old maps suggest that the bivariate slow-mode condition

`l_slow(1) l_slow(3) <= 0`

may already be sufficient for the full all-FDD speed order. The new theorem settles the subcase in which both nonconstant eigenmeasures are single-crossing. The remaining difficulty is precisely the configurations where the slow mode is single-crossing but the fast mode has two sign changes (`- + -` up to orientation).

Next untried Section-B methods if the target remains active: **#4 (prove the remaining reversible three-state special class completely), #12 (find the invariant behind sign-variation of the two modes), #27 (test whether the bivariate quantifier can be promoted to all finite dimensions).** If the frozen metric also fails to move on the next invocation, the three-unchanged-run Section-I stuck protocol will trigger even if the theorem obligation has changed; I will obey that rather than quietly changing the metric.

## 8. Model / scheduler control status

The task-control schema exposed in this environment still has title/prompt, schedule or relative start, timing mode, and enabled-state fields, but **no bindable model-family selector and no bindable reasoning-effort selector**. Thus `GPT-6 / maximum` remains request text only here; this invocation actually ran GPT-5.6 Sol and the reasoning level is UNVERIFIED. Changing that would require an authorized scheduler/product/API surface that actually exposes model and reasoning fields.

The historical P26 `You cannot modify this task` response is not treated as a permanent global condition: current repository receipts record later successful P26 edits in another authorized context. If such a refusal recurs, the valid workaround is to use the owning or otherwise authorized account/workspace/admin surface; cloning the task or bypassing access controls is not a valid workaround. No schedule was created, modified, or disabled in this run.

```yaml
ledger_delta:
  track: NM13-01
  category: CLOSABLE_OUTSIDE
  status: PARTIAL
  source_status: OPEN
  source_id: P0292
  claim_id: P0292
  canonical_dedup_key: characterize_ctmc_speed_monotonicity_in_supermodular_order
  shard_residue_mod_13: 0
  metric_name: D_rev_0_normalized_frozen_limit_first_order_supermodular_speed_defect
  metric_before: 0
  metric_after: 0
  mathematical_movement: false
  substantive_progress:
    - proved_full_path_upper_set_order_for_extreme_single_crossing_left_eigenmeasures
    - proved_two_mode_single_crossing_sufficient_condition_for_reversible_three_state_ctmcs
    - proved_strict_b2_gt_b3_asymmetric_star_regime
    - combined_with_recovered_history_to_classify_three_state_star_iff_b2_ge_b3
  new_internal_claim: NM13-01-P0292-STAR-SINGLE-CROSSING-03
  methods_actual: [3, 17, 30]
  methods_next: [4, 12, 27]
  unchanged_runs_since_metric_movement: 2
  stuck_recoveries_used: 0
  audits:
    P26: NOT_REQUESTED
    NM13-02: NOT_REQUESTED
  prior_art_scope: bounded_source_author_exact_title_citing_and_HuPan_Kulik_KulikWichelhaus_check_2026_09_17_UTC
  novelty: UNVERIFIED
  finite_checker: NOT_APPLICABLE_THEOREM_SIZED_FULL_PROOF_ON_PAGE
  shared_root_edits: NONE
  peer_file_edits: NONE
  next_step: attack_general_reversible_three_state_fast_mode_two_sign_change_case_without_changing_frozen_metric
```
