Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO SOURCE-METRIC MOVEMENT: I0076 remains OPEN / PARTIAL / RETIRED-HANDOFF at the historical carried `2/4`, with no surviving frozen counterexample candidate; admission `E_ready: 0 -> 0`. RETAINED-SCREEN MOVEMENT: for Talagrand F0111, every `k=2` weak-dual witness supported on points with at most two nonzero coordinates is impossible at a homogeneous base `q=c 1_n`, for every `n>=3` and every `0<gamma<=gamma_*`, where `gamma_*=1/x_*=0.1069901829...` and `x_*>0` is the nonzero solution of `x=4 log(1+x)`. Methods #4 PROVE SOMETHING WEAKER COMPLETELY, #16 COMPUTE EVERY SMALL CASE, #27 SWAP THE QUANTIFIERS.**

# R15 successor screen — homogeneous pair-support obstruction is completely eliminated

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

All new mathematical statements below are **SELF_CHECK_ONLY** unless explicitly identified as source material. Their proofs are written on the page. No independent fleet audit or novelty claim is asserted.

## 1. Continuity: source-exact I0076 remains retired and unreopened

Before doing mathematics I reread/recovered `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the intake ledger `probability_1000_intake_I_20260914/problems.jsonl`, the controlling six-run R15 handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`, the immediately preceding R15 report `runs/R15/20260918_1528Z_successor_screen_f0111_forest_dual_f60k.md`, and the neighboring R20 F0111 handoff `runs/R20/2026-09-18T07-52-02Z_successor_admission_f0111_tropical_handoff_a6e91c.md`.

I also rechecked the primary source, Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4. Definition 2.1 says that `X` is FBM when there are random origins `S_n -> -infinity` a.s. from which each complete centered future is standard Brownian motion; BBM means time reversal is FBM; 2BM means that at one random origin `S`, the complete centered forward and backward half-paths are **independent standard Brownian motions**. Problem 7.2 asks whether FBM + BBM + existence of an arbitrary random time `T` at which the two complete centered half-paths are independent forces 2BM. The source does **not** assume `T` is a stopping time and does **not** separately assume either half-path at `T` is Brownian. Problem 7.5 is a different source problem and remains excluded.

The six-run handoff is still controlling. The source-Theorem-6.1-derived candidate was eliminated because no source-valid independent seam survived. The later Brownian-prefix/Bessel candidate satisfied the first three intended features but was proved actually 2BM and therefore failed the counterexample obligation. There is presently **no surviving frozen counterexample candidate**. The copied-continuous-Brownian-cell construction remains only an architecture. Consequently the historical `2/4` is a carried retirement value, not a statement that an active frozen candidate currently has two certified obligations.

Fresh exact-problem searches dated 2026-09-18 again recovered the original Burdzy--Scheutzow paper but no accessible later primary source explicitly claiming to settle exact Problem 7.2. This is bounded negative search evidence only; it is not a worldwide openness certificate.

The current queue still says newly certified READY entries remain zero and explicitly keeps I0076 assigned to R15 rather than in reserve. I therefore create no successor claim and do not promote a PENDING row to READY. Admission stays `E_ready=0 -> 0`.

## 2. Retained screen: exact Talagrand target and prior state

The retained screen is Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Problem 10.9 (`F0111`). For the threshold up-class

`A_{n,k}={X subset [n]: |X|>=k}`

with independent coordinate inclusion probabilities `1-exp(-t_i)`, write

`F_{n,k}(t)=-log P_t(|X|<k)`.

Talagrand's Definition 10.1 asks, for a fixed `gamma>0`, that at every base point `q>=0` there be a multilinear polynomial with nonnegative coefficients and zero constant term,

`P(t)=sum_{empty != I subset[n]} beta_I t_I`, `beta_I>=0`,

such that `F_{n,k}(t)<=P(t)` for all `t>=0` and `P(gamma q)<=gamma F_{n,k}(q)`. Problem 10.9 asks whether one universal positive `gamma` works for every cardinality threshold.

The preceding R15 run changed the pair-supported `k=2` dual search into graph language and proved that pair-support graphs which are forests cannot refute the target at the source endpoint constant. It identified the triangle as the first unresolved pair-only topology for `n=3`, and one full-support atom plus one lower-support atom as the other first unresolved topology. The neighboring R20 handoff had independently shown that radial and first-order tropical routes do not provide the obstruction. This run attacks the cycle branch directly rather than adding another forest lemma.

A fresh 2026-09-18 literature check recovered Talagrand's primary STOC paper and related later threshold work including DeMarco--Kahn and Warnke. Those later papers concern related expectation-threshold / `p`-small formulations; the bounded search did not surface an accessible theorem explicitly resolving this Definition-10.1 / Problem-10.9 positive-multilinear-majorant statement. This remains bounded negative evidence, not a novelty certificate.

## 3. Weak-dual setup

I use the same necessary weak-dual condition as in the preceding R15 reports. Fix a base `q` and `gamma>0`. If a positive finite measure `mu` on `R_+^n` satisfies all monomial budgets

`int t_I dmu(t) <= (gamma q)_I` for every nonempty `I subset[n]`,       (3.1)

then any valid `C_gamma` certificate implies

`int F_{n,k}(t) dmu(t) <= gamma F_{n,k}(q)`.                           (3.2)

Thus a strict reverse inequality in (3.2) would be a weak-dual refutation certificate.

This run proves that, for homogeneous base points and `k=2`, **no measure supported on coordinate sets of size at most two can do this**, even if its pair-support graph has arbitrarily many cycles.

## 4. Methods #27 and #4 — symmetrize first, then close the whole pair-supported sector

Let `q=c 1_n`, with `c>=0`, and suppose `mu` satisfies (3.1) and every support point of `mu` has at most two nonzero coordinates. Since `F_{n,2}` and the homogeneous budget are invariant under `S_n`, replace `mu` by

`mu_bar=(1/n!) sum_{sigma in S_n} sigma_# mu`.                         (4.1)

The objective and every feasibility inequality are preserved, as is the property `|supp(t)|<=2`. This is the useful quantifier swap: rather than classify all possible collections of pair atoms and then optimize weights, first average **any** hypothetical witness over the group.

Points with support size zero or one contribute zero to `F_{n,2}`, so discard them from the objective. By exchangeability, the restriction of `mu_bar` to every exact pair plane `{i,j}` is the same symmetric positive measure `nu` on `R_+^2`. Put

`m_1 = int x dnu = int y dnu`,

`m_2 = int x y dnu`.                                                   (4.2)

For a fixed coordinate `i`, there are `n-1` incident pair planes. The singleton budget in (3.1) gives

`(n-1)m_1 <= gamma c`.                                                 (4.3)

For a fixed pair `{i,j}`, no other pair plane contributes to `t_i t_j`, so the pair budget gives

`m_2 <= gamma^2 c^2`.                                                  (4.4)

On a pair plane the threshold hazard is the two-coordinate all-elements hazard

`Phi(x,y)=-log(exp(-x)+exp(-y)-exp(-(x+y))).`                          (4.5)

Two elementary global bounds are enough:

`Phi(x,y) <= min(x,y) <= (x+y)/2`,                                    (4.6)

and

`Phi(x,y) <= x y`.                                                     (4.7)

For (4.6), the denominator in (4.5) is at least `exp(-x)` and at least `exp(-y)`. For (4.7), note `Phi(0,y)=0` and

`partial_x Phi(x,y)
 = exp(-x)(1-exp(-y)) / (exp(-x)+exp(-y)-exp(-(x+y)))
 <= 1-exp(-y) <= y`.

Integrating from `0` to `x` proves (4.7).

Therefore

`int Phi dnu <= min(m_1,m_2)
             <= min(gamma c/(n-1), gamma^2 c^2)`.                     (4.8)

There are `binom(n,2)` pair planes, so

`int F_{n,2}(t) dmu_bar(t)
 <= gamma min(n c/2, binom(n,2) gamma c^2)`.                           (4.9)

The remaining task is now a one-variable lower bound for the base hazard.

## 5. Method #16 — the `n=3` triangle exposes the two scales, and the exact calculation generalizes

At the homogeneous base,

`F_{n,2}(c 1_n)
 = (n-1)c - log(n-(n-1)exp(-c)).`                                     (5.1)

Put `x=(n-1)c`. Since `1-exp(-c)<=c`,

`F_{n,2}(c 1_n) >= x-log(1+x)`.                                      (5.2)

The small `n=3` triangle case shows that the objective has two competing scales: a singleton-moment linear scale and a pair-moment quadratic scale. Keeping the algebra exact rather than numerically scanning the triangle makes the same mechanism work for all `n>=3`.

Indeed, with

`alpha_n = n/(2(n-1)) <= 3/4`,

we have

`n c/2 = alpha_n x`,

`binom(n,2) gamma c^2 = alpha_n gamma x^2`.                           (5.3)

Thus it is enough to prove

`x-log(1+x) >= (3/4) x min(1,gamma x)`.                               (5.4)

Define `x_*>0` to be the nonzero solution of

`x_*=4 log(1+x_*)`,                                                   (5.5)

and

`gamma_* = 1/x_* = 0.106990182965...`.                               (5.6)

The nonzero solution is unique because `x/4-log(1+x)` decreases initially, has derivative `1/4-1/(1+x)`, and then increases strictly for `x>3` to `+infinity`.

### Lemma R15-F0111-PAIR1

For every `0<gamma<=gamma_*` and every `x>=0`, inequality (5.4) holds.

#### Proof

First suppose `gamma x<=1`. Let

`A(x)=[x-log(1+x)]/x^2` for `x>0`.

Its derivative has the sign of

`N(x)=x^2/(1+x)-2x+2log(1+x)`.

A direct differentiation gives

`N'(x)=-x^2/(1+x)^2 <=0`, and `N(0)=0`, so `A` is decreasing. Therefore on `0<x<=1/gamma`, its minimum occurs at `x=1/gamma`. Because `1/gamma>=x_*` and `z/4-log(1+z)` is increasing for `z>=x_*>3`,

`log(1+1/gamma) <= 1/(4gamma)`.

Hence

`A(1/gamma)
 = gamma^2(1/gamma-log(1+1/gamma))
 >= (3/4)gamma`,

which yields

`x-log(1+x) >= (3/4)gamma x^2`.

Now suppose `gamma x>=1`. Then `x>=1/gamma>=x_*`, and therefore

`log(1+x)<=x/4`.

Thus

`x-log(1+x)>=3x/4`.

The two cases give exactly (5.4). QED.

Combining (4.9), (5.2), (5.3), and the lemma proves the main theorem.

### Theorem R15-F0111-PAIR2 — homogeneous pair-supported weak-dual witnesses are impossible

Let `n>=3`, `c>=0`, and `0<gamma<=gamma_*`, where `gamma_*` is defined by (5.5)--(5.6). If a positive finite measure `mu` satisfies all weak-dual monomial budgets at the homogeneous base `q=c1_n` and every point in the support of `mu` has at most two nonzero coordinates, then

`int F_{n,2}(t) dmu(t) <= gamma F_{n,2}(c1_n)`.                       (5.7)

Therefore such a measure cannot refute Talagrand's `k=2` threshold statement at this base and this `gamma`.

No numerical path samples, floating-point grids, or finite-case checks enter this theorem. The decimal in (5.6) is only a convenience; the proof uses the exact defining equation (5.5).

## 6. What moved, and what did not

This strictly extends the previous pair-support analysis in a direction the forest theorem could not reach. The preceding theorem handled **arbitrary base vectors** but required an acyclic pair-support graph. The new theorem handles **arbitrary pair-support graphs, including every cycle**, but requires a homogeneous base and `gamma<=gamma_*`. Neither theorem subsumes the other.

In particular, for `n=3,k=2` at a homogeneous base, the triangle cycle is now completely eliminated. Every remaining weak-dual refutation at `gamma<=gamma_*` must place positive mass on at least one full-support point. Combined with the earlier one-atom no-go theorem, a remaining homogeneous `n=3` counterexample cannot be a single atom; the first unresolved topology is therefore at least two atoms with at least one full-support atom, such as one full-support atom plus one lower-support atom.

This is **not** a proof of Talagrand Problem 10.9. It does not handle heterogeneous bases, it does not rule out full-support witnesses, and it does not address `k>=3`. It is a closed restricted theorem inside the retained screen. Publication novelty is **UNVERIFIED**; the symmetrization and moment bounds are elementary enough that prior occurrence is plausible.

## 7. Prior-art/current-status check

Dated 2026-09-18 queries for the exact Talagrand title, `Problem 10.9`, `C_gamma`, cardinality thresholds, and later papers recovered the STOC 2010 source, DeMarco--Kahn's later note on a Talagrand problem, and later threshold work including Warnke. The latter literature is related but does not, in the accessible material found, state this exact Definition-10.1 positive-multilinear-majorant problem as solved. I did not infer novelty from non-retrieval.

Dated 2026-09-18 queries for Burdzy--Scheutzow Problem 7.2 recovered the original arXiv/PTRF work and mirrors/citation pages but no accessible later primary source explicitly settling exact Problem 7.2. Again this is bounded negative evidence only.

## 8. Validation / artifacts

No checker was created. The movement is theorem-sized and analytic, and the complete proof is on this page. Creating a grid or sample certificate would not strengthen it and would violate the 90/10 instruction. No numerical Brownian path samples were used anywhere.

No audit is claimed. If this restricted Talagrand theorem ever becomes relevant to a source-level closure package, it still needs the normal independent audit path and prior-art review.

## 9. Scheduler/model-control status

The exposed scheduler surface still has no binding model-family selector, no reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed hour-long execution control. Therefore GPT-6 / maximum remains prompt-only, and this run is honestly labelled GPT-5.6 Sol / UNVERIFIED.

The implementation manifest still records P26 scheduler ID `6aa7b43682948191b697d72fec69d539` returning `You cannot modify this task` in one authorization context. Root reconciliation later records successful P26 updates from a different authorized context. The legitimate workaround is an owning/admin-authorized product/backend context or platform support that exposes the needed controls; duplication, permission bypass, or pretending the selector was set is not a valid workaround. No scheduler change was attempted in this run.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R15
  lane: CLOSABLE_OUTSIDE
  source:
    canonical: "Burdzy-Scheutzow, Forward Brownian Motion, arXiv:1302.6958v4, Problem 7.2"
    intake: I0076
    exact_scope: "FBM + BBM + independence of the two complete centered half-paths at an arbitrary random time T; decide whether 2BM follows"
    exclusions: ["Problem 7.5", "deterministic-time substitution", "stopping-time strengthening", "posted work"]
  source_metric:
    name: "number of four source-matching obligations proved for one frozen counterexample candidate"
    before: "historical carried 2/4; no surviving frozen candidate"
    after: "historical carried 2/4; no surviving frozen candidate"
    movement: none
    status: "OPEN / PARTIAL / RETIRED-HANDOFF"
    unchanged_count: "6, frozen at retirement"
  admission_metric:
    name: E_ready
    before: 0
    after: 0
    status: "no newly certified source-clean current-open ownership-clear CLOSABLE successor"
  retained_screen:
    source: "Talagrand, Are Many Small Sets Explicitly Small?, STOC 2010, Problem 10.9 / F0111"
    status: "PARTIAL / SELF_CHECK_ONLY / NOT CLAIMED"
    movement: "homogeneous k=2 weak-dual witnesses supported on coordinate sets of size <=2 eliminated for all n>=3 and 0<gamma<=gamma_*"
    gamma_star: "1/x_*, x_*>0 solves x_*=4 log(1+x_*); approximately 0.106990182965"
  tried_moves: [4, 16, 27]
  remaining_obligation: "first unresolved homogeneous n=3,k=2 dual topology has at least two atoms and at least one full-support atom; source Problem 10.9 additionally requires heterogeneous q and all n,k"
  evidence:
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "runs/R15/20260918_1528Z_successor_screen_f0111_forest_dual_f60k.md"
    - "runs/R20/2026-09-18T07-52-02Z_successor_admission_f0111_tropical_handoff_a6e91c.md"
    - "this report"
  audit_ids: []
  audit_status: "none requested or claimed this run"
```

## 11. Next fresh methods

The next run should not repeat #4/#16/#27. The mathematically minimal target is the remaining `n=3,k=2` homogeneous configuration containing a full-support atom. A useful fresh triple is **#3 PROVE SOMETHING STRONGER, #15 BREAK THE SYMMETRY ON PURPOSE, #20 FIND WHY THE ALGORITHM FAILS**: first ask whether every homogeneous feasible dual measure, not merely pair-supported ones, satisfies the desired inequality; then isolate a one-full-support-plus-one-lower-support witness without imposing exchangeability inside each atom; finally identify exactly which mixed third-order budget prevents extending the pair-support proof.
