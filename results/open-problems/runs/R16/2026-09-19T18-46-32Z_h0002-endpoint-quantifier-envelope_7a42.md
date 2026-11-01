Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum. FIXED-METRIC MOVEMENT:** the nominal Beck--Fiala metric remains the current-preprint baseline `B(t,n)<3 sqrt(2 pi t)` for every integer `t>=1` and every `n`; on the active exclusive R16/H0002 successor, the proved giant-fraction envelope moves from `G_H2energy=min{1,G_coreavg+E_rfgap+eta_H2/4}` to the endpoint envelope `G_H2sup=min{1,G_coreavg+E_rfgap+eta_H2}`, with strict improvement whenever `G_H2energy<1`. Methods actually used: **#2 ATTACK THE NEGATION FIRST, #27 SWAP THE QUANTIFIERS, #5 ADD A PARAMETER AND DIFFERENTIATE IN IT**. All thirty Section-B moves have already appeared somewhere in the recovered H0002 history, so these are honest nonconsecutive reuses; the preceding triple was #25/#3/#26.

# R16 — H0002: remove the artificial quarter-loss by an endpoint/quantifier argument

Date: 2026-09-19 UTC.
Target: `H0002`, HARD OUTSIDE, exclusive owner R16.
Status: **PARTIAL / source OPEN-looking / ACTIVE**.

## 1. Continuity, required reads, ownership, and current sources

This run continues from

`runs/R16/2026-09-19T17-54-52Z_h0002-core-internal-energy-depletion_5b91.md`,

whose incoming bound is `G_H2energy`. It does not restart Beck--Fiala and does not reopen any retired R16 target.

Before new research I re-read/reconciled:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- canonical exclusive claim `operations/claims/H0002.md`;
- the H-intake identity `arxiv_2608_19145::Question 5.1; Section 5, Concluding remarks`;
- the newest own R16 report above and the immediately preceding H0002 reports needed to recover `E_rfgap`, `Theta`, `M_H2`, and `eta_H2`; and
- the newest recoverable same-paper neighboring G0011 handoff. G0011 is a distinct long-cycle target and does not conflict with H0002 ownership.

The root ledgers remain shared-state records and are not edited by this worker; the structured delta is recorded only in this immutable own-track report.

### Current primary-source check, 2026-09-19

The nominal Beck--Fiala title is no longer an honest unresolved existence target at the current manuscript level.

- Nikhil Bansal and Haotian Jiang, arXiv:2508.03961v2, prove the Beck--Fiala `O(sqrt(t))` scale directly for `t>=log^2 n`, and give a weaker polylogarithmic-loss estimate below that range; their result is algorithmic. URL: https://arxiv.org/abs/2508.03961 .
- Shengtao Guo, Ethan X. Fang and Junwei Lu, arXiv:2609.11189v1, submitted 2026-09-10, prove the stronger Komlos statement with constant `3 sqrt(2 pi)` and explicitly deduce imbalance `<3 sqrt(2 pi t)` for every integer `t>=1`, independent of `n`. URL: https://arxiv.org/abs/2609.11189 .
- Sankeerth Rao Karingula and Shachar Lovett, ECCC TR26-188, posted 2026-09-17, give an elementary proof of Komlos with constant `36`. URL: https://eccc.weizmann.ac.il/report/2026/188/ .

These are extremely recent preprints / technical reports rather than mature refereed consensus. On their stated theorems, however, literal Beck--Fiala is a **KNOWN CURRENT-PREPRINT BASELINE** rather than new R16 research.

The active source remains Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (2026-08-19), Question 5.1. The source asks for natural conditions under which `p>=(1+epsilon)/lambda(G)` forces a component of order `Omega(n)` with constant probability and explicitly identifies localization of the spectral radius as the main obstruction. A fresh bounded title/author/question search again surfaced the August 19 source and no later source-matching resolution. That is negative bounded-search evidence only, not a claim of worldwide novelty or openness.

## 2. Incoming theorem and the exact place where the metric was left on the table

The frozen H0002 class and notation are unchanged. In particular

`0<epsilon<=1`, fixed `rho,kappa>0`,

`alpha=(rho/64)*(1-exp(-epsilon^2/288))`,

`Delta=epsilon*(7-epsilon)/(8-epsilon)`,

and H1--H2--H3 are exactly those in `operations/claims/H0002.md` and the incoming report.

The preceding run proved the H2 internal-energy depletion

`chi_P=kappa^2*a_P^3/alpha^4>0`

and consequently the sharpened prefix-energy budget

`A_H2=a_P-chi_P-(u_P-b_0)*t_0^2`,

`M_H2=(V_0/b_0)*A_H2`.

With the exact Stieltjes weighted first moment `Theta>0` and

`g_Delta(z)=(1-exp(-Delta*z))/z`, `g_Delta(0)=Delta`,

it proved the endpoint weighted absorption correction

`boxed: eta_H2=Theta*g_Delta(M_H2/Theta)>0`.                 (2.1)

The incoming report then established a fact stronger than the bound it finally recorded:

> after choosing the actual connected-core density `a_3=c_3 a_P`, the finite sprinkling reserve `r<Delta`, a finite Stieltjes partition, and finite anchor/floor approximations, the resulting weighted correction can be made **arbitrarily close to `eta_H2`**, while the remaining trimming and concentration losses can be made arbitrarily small.

Nevertheless it froze one convenient receipt,

`delta_H2=eta_H2/4`,                                           (2.2)

and called

`G_H2energy=min{1,G_coreavg+E_rfgap+delta_H2}`.                (2.3)

Equation (2.2) is useful as a single fixed certificate, but it is not the strongest complete endpoint bound proved by the same construction. The tracked metric is the largest uniform endpoint coefficient for which **every fixed strictly smaller coefficient** is proved. For that metric, a permanent factor `1/4` is artificial.

## 3. Method #2 — attack the negation: can a fixed loss survive all finite approximations?

To invalidate the endpoint upgrade, there would have to exist a constant `ell_*>0`, depending only on the frozen H0002 parameters, such that every legal finite implementation of the proof loses at least `ell_*` from `eta_H2`.

The recovered proof architecture has no such term. Its losses are exactly:

1. `c_3<1` instead of the endpoint core factor `c_3=1`;
2. finite sprinkling rate `r<Delta` instead of `r=Delta`;
3. finite Stieltjes partition error;
4. finite old-anchor/floor approximation error;
5. `o(1)` core trimming and concentration errors after the finite parameters are frozen.

The incoming report already proves that items 1--4 can be chosen, as **fixed constants independent of `n`**, so that the deterministic correction differs from `eta_H2` by less than any prescribed `zeta>0`. Once they are fixed, item 5 tends to zero as `n->infinity`.

Thus the negation would require a sixth nonvanishing loss which is not present in the argument. No such loss exists in the recovered theorem. This is the key audit: the quarter in (2.2) is a safety receipt, not a structural obstruction.

There is also no illicit `n`-dependent tuning here. For a requested final coefficient `g`, all construction parameters are selected first as constants depending only on `g,epsilon,rho,kappa`; only then is `n` sent to infinity.

## 4. Method #5 — insert a slack parameter and watch the proved envelope move

For `theta in (0,1)` define

`E_H2(theta):=E_rfgap+theta*eta_H2`,                            (4.1)

`G_H2(theta):=min{1,G_coreavg+E_H2(theta)}`.                   (4.2)

### Lemma 1 (every subendpoint fraction is attainable)

For every fixed `theta<1` and every fixed

`g<G_H2(theta)`,                                               (4.3)

we have, uniformly over the frozen H1--H2--H3 class,

`P(L_1(G_p)>=g n)->1`                                          (4.4)

for every `p>=(1+epsilon)/lambda(G)`.

#### Proof

Fix `theta<1`. Put

`zeta:=(1-theta)*eta_H2/10>0`.                                 (4.5)

The definition

`E_rfgap=sup_{X in (t_0,Y]} min{P_run(X),Q_run(X)}`

allows us to choose a **fixed** threshold `X_zeta` with constant-weight contribution greater than `E_rfgap-zeta`.

Now freeze `c_3<1`, `r<Delta`, the Stieltjes partition, and the finite anchor/floor family sufficiently close to their endpoint values that simultaneously:

- the finite connected-core / constant-weight contribution at `X_zeta` is within `zeta` of the corresponding endpoint quantity;
- the H2-depleted weighted correction is greater than `eta_H2-zeta`; and
- every deterministic trimming reserve that precedes the final `n->infinity` step is smaller than `zeta`.

This simultaneous choice is legitimate because the incoming proof establishes convergence of all of these finitely many quantities under the same endpoint limit. After these constants are frozen, the remaining probabilistic `o(1)` losses vanish with `n`.

The weighted correction alone then exceeds

`eta_H2-zeta`
` > theta*eta_H2`,                                             (4.6)

because `zeta<(1-theta)eta_H2`. The base contribution can be made arbitrarily close to `G_coreavg+E_rfgap` by the same fixed-before-`n` diagonal choice already used in the earlier endpoint envelopes. Hence every fixed `g` satisfying (4.3) lies below the resulting finite proof for all sufficiently large `n`. This proves (4.4). `QED`

Before the cap at one, the slack family has the exact derivative

`d/dtheta [G_coreavg+E_rfgap+theta*eta_H2]=eta_H2>0`.          (4.7)

Thus this parameter is not cosmetic: it exhibits a genuine monotone continuum of proved uniform coefficients from the old safety receipt toward the endpoint.

## 5. Method #27 — swap the quantifiers correctly and take the endpoint supremum

Define

`boxed: E_H2sup:=E_rfgap+eta_H2`,                              (5.1)

`boxed: G_H2sup:=min{1,G_coreavg+E_H2sup}`.                    (5.2)

### Theorem 2 (endpoint H2-energy envelope)

On the unchanged frozen H1--H2--H3 class, for every fixed

`boxed: g<G_H2sup`,                                            (5.3)

and every

`p>=(1+epsilon)/lambda(G)`,                                    (5.4)

we have

`boxed: P(L_1(G_p)>=g n)->1`.                                 (5.5)

No endpoint attainment at `g=G_H2sup` is claimed.

#### Proof

Fix `g<G_H2sup`. Because `G_H2(theta)` increases to `G_H2sup` as `theta up to 1`, there exists a **fixed** `theta<1` such that

`g<G_H2(theta)`.                                               (5.6)

Apply Lemma 1 with this `theta`. `QED`

The order of quantifiers is the entire point:

`for every fixed g<G_H2sup`
` there exists fixed theta<1 and fixed finite proof parameters`
` such that for all sufficiently large n ...`.

We never choose `theta`, `c_3`, `r`, the partition, or the anchor family as functions of `n`.

## 6. Strict fixed-metric comparison

The incoming envelope was

`G_H2energy=min{1,G_coreavg+E_rfgap+eta_H2/4}`.                (6.1)

The new envelope is

`G_H2sup=min{1,G_coreavg+E_rfgap+eta_H2}`.                     (6.2)

Since `eta_H2>0`,

`G_H2sup>=G_H2energy`.                                         (6.3)

If the incoming metric is not already saturated,

`G_H2energy<1`,                                                 (6.4)

then the pre-cap increment available beyond it is exactly

`eta_H2-eta_H2/4=3*eta_H2/4>0`,                                (6.5)

and therefore

`boxed: G_H2sup>G_H2energy`.                                  (6.6)

A concrete fixed receipt outside the whole incoming envelope is

`boxed: g_receipt:=G_H2energy`
` +(1/2)*min{3*eta_H2/4,1-G_H2energy}`.                        (6.7)

For every nonsaturated frozen parameter triple,

`G_H2energy<g_receipt<G_H2sup`.                                (6.8)

If `G_H2energy=1`, the tracked giant-fraction metric is already at its absolute ceiling; the endpoint theorem remains stronger at the proof-expression level but cannot increase a number above one.

This is a correction to the phrase “complete envelope” in the incoming report: `G_H2energy` was a valid explicit safety envelope, while `G_H2sup` is the complete endpoint envelope actually supplied by that proof architecture.

## 7. Two broader routes tested but not promoted

### 7.1 Full convex/KKT obstacle route

I revisited the suggested continuum program

`min_x int (1-exp(-Delta*x(q))) dq`

subject to nondecreasing `x`, all prefix constraints, and the H2-depleted quadratic-energy budget. A tempting shortcut is to posit a single “least convex majorant” for the cumulative profile `X(b)=int_0^b x`, but the order structure is not sufficient for the needed conclusion: convex feasible majorants of the obstacle need not be pointwise ordered in the way required to compare all concave absorption integrals. Turning this into an exact finite-plateau theorem still needs a genuine dual/KKT argument. I therefore retain **no new metric claim** from this route.

### 7.2 Schur-complement use of H1 on the complement

Writing the adjacency matrix in core/complement blocks gives a resolvent inequality of the schematic form

`B (lambda I-D)^(-1) B^T <= lambda I-C`

when the inverse is interpreted off the top-eigenvalue boundary. H1 makes `lambda(D)` close to `lambda`, suggesting a potentially strong bound on the core/complement coupling. The obstruction is exactly the localization issue highlighted by CMW: without a quantitative lower bound on the projection of `B^T 1_W` onto the near-top spectral subspace of `D`, the resolvent does not improve the already-used operator-norm energy estimate uniformly. H2 gives macroscopic set expansion but does not by itself rule out a near-top vector localized below the relevant set scale. I therefore do not promote this route in this run.

These failures identify the next real theorem needed: a source-valid delocalization estimate for the complement Perron mass, or a complete dual/KKT solution of the isotonic obstacle problem. Another scalar safety factor is no longer a useful target.

## 8. Prior-art and source boundary

The endpoint upgrade itself is an internal quantitative consequence of the already-established H0002 proof chain. Its mechanisms — epsilon/endpoint quantifiers, monotone convergence of a finite-parameter proof family, and diagonal choice of finitely many approximation parameters — are standard and are **not** claimed as novel mathematical techniques.

The research contribution recorded here is narrower: the tracked H0002 metric was unnecessarily frozen at one quarter of a correction that the preceding theorem had already proved arbitrarily approximable. Restoring the correct quantifier order changes the complete proved bound from (6.1) to (6.2).

A bounded current search did not find a later resolution of CMW Question 5.1. This is not a novelty certificate. The nominal Beck--Fiala result is treated only as a current-preprint baseline because the Guo--Fang--Lu and Karingula--Lovett proofs are extremely recent.

## 9. Status, stuck counter, checker discipline, and next obstruction

H0002 remains **PARTIAL / source OPEN-looking / ACTIVE**. The source asks for natural conditions in general; R16 proves and strengthens one explicit sufficient-condition theorem on the fixed H1--H2--H3 class.

The supported unchanged count remains **0** because the complete numerical envelope moved this run. The HARD stuck protocol is not triggered.

No exact-arithmetic checker was manufactured. The new claim is analytic and entirely about quantifiers and convergence of a theorem-sized proof already written on the page; there is no finite-enumeration core to certify.

The strongest next route is not another conservative receipt. It is one of:

1. solve the H2-depleted all-prefix isotonic/KKT problem exactly enough to improve `eta_H2`; or
2. prove complement spectral delocalization from the combined H1/H2 hypotheses and feed it through the block resolvent to reduce the outside energy budget further.

## 10. Model, scheduler controls, and permission boundary

The runtime identifies the model as GPT-5.6 Sol. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is reported as **UNVERIFIED**. The currently exposed task-control schema still permits prompt/title, schedule or relative start, enablement and timing mode, but has **no binding model-family selector, no reasoning-effort selector, and no authenticated applied-model receipt**. GPT-6/maximum therefore remains prompt-only. Enforcing it would require platform-level model/reasoning fields plus per-run attestation.

No scheduler modification was attempted because the owner instruction for research workers forbids scheduler changes. The repository records that P26's historical `You cannot modify this task` denial was authorization-context-specific and that a later P26 update succeeded from an authorized context. If a task still returns that denial, the compliant workaround is modification from its owning authorized workspace/account or escalation to platform support; duplicating the task or bypassing permissions is not legitimate.

No email, Drive, public posting, purchase, permission change, workflow execution, or peer-track file edit was made.

## 11. Structured ledger delta

```yaml
ledger_delta:
  worker: R16
  claim: H0002
  source: Christoph-Morawski-Wigderson_arXiv_2608_19145v1_Q5.1
  nominal_source: Beck-Fiala_1981
  nominal_metric: complete_uniform_B(t,n)
  nominal_before: "B(t,n) < 3*sqrt(2*pi*t) for every integer t>=1, all n (Guo-Fang-Lu v1 current-preprint baseline)"
  nominal_after: "same KNOWN current-preprint baseline"
  nominal_movement: NONE_SOURCE_KNOWN
  metric_name: g_twoaxis_complete_envelope
  before: "G_H2energy = min(1, G_coreavg + E_rfgap + eta_H2/4)"
  after: "G_H2sup = min(1, G_coreavg + E_rfgap + eta_H2)"
  eta_H2: "Theta*g_Delta(M_H2/Theta)"
  comparison: "G_H2sup>=G_H2energy; strict whenever G_H2energy<1; pre-cap gain 3*eta_H2/4"
  movement: STRICT_POINTWISE_ON_NONSATURATED_TRIPLES
  status: PARTIAL
  source_status: OPEN_LOOKING
  supported_unchanged_count: 0
  methods: [2, 27, 5]
  method_history_note: "all 30 moves already appeared in recovered H0002 history; these are nonconsecutive reuses; preceding triple [25,3,26]"
  finite_checker: NOT_APPLICABLE_ANALYTIC
  checker_reason: "endpoint/quantifier theorem; no finite enumeration claim"
  next_obstruction: "H2-depleted all-prefix isotonic/KKT optimizer or H1/H2 complement spectral delocalization"
  shared_root_written: false
```
