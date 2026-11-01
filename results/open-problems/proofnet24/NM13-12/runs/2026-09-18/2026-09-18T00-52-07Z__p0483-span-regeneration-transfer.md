Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT:** `c_slab^(d)(kappa,w) = -log rho(K_{d,w}(kappa))` stayed exact; methods actually tried this run: **B3, B13, B27**. Substantive route result: an exponential moment of the span of a single regeneration block in just one coordinate transfers quantitatively to moments of the regeneration time. In particular, if `E_hat exp(gamma W_j)<infinity` for some `gamma > (1/2) log(1/kappa)`, then the walk is ballistic. Contrapositively, any source-valid directionally transient zero-speed counterexample must have `E_hat exp(gamma W_j)=infinity` for every coordinate `j` and every `gamma>(1/2)log(1/kappa)`. P0483 remains OPEN because directional transience alone has not been shown to force such a span moment.

# NM13-12 — P0483 regeneration-span transfer criterion

Date: 2026-09-18 UTC  
Track: `NM13-12`  
Category: `HARD OUTSIDE`  
Repository: `yspennstate/math-open-problems`, branch `master`  
Canonical source / claim ID: `P0483`  
Canonical dedup key: `directional_transience_versus_positive_speed_under_uniform_ellipticity`  
Historical alias: `C0041`  
Overall source status after this run: **OPEN**  
Local status: **PARTIAL / source-level sufficient condition and zero-speed obstruction; frozen metric unchanged**

## 1. Runtime/model disclosure and task-control reality

The requested header asks for GPT-6 with maximum reasoning. That is not what I can verify ran. The actual model exposed to this invocation is **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**.

The task-control surface available in this runtime still exposes prompt/title, schedule/timing, enabled state and timing mode, but **no binding model-family selector and no reasoning-effort selector**. Therefore `GPT-6 / maximum` remains prompt text rather than a scheduler-enforced setting here. Making that binding would require an authorized product/scheduler/API surface that actually exposes model and reasoning fields. I did not create, modify, disable, or duplicate any schedule.

Repository policy records a historical `You cannot modify this task` response for P26 in one scheduler context and a later successful P26 update from another authorized context. A future denial is therefore an authorization/context boundary, not permission to bypass access control. The legitimate workaround is the owning account/workspace or another authorized product/admin surface; this worker does not clone an inaccessible task.

## 2. Continuity recovered before new mathematics

This run continues the already-admitted P0483 assignment. It does **not** reopen intake and does not create or overwrite a claim. The create-only claim `operations/claims/P0483.md` remains owned exclusively by NM13-12; its canonical dedup key has SHA-256 residue `11 mod 13`, matching this worker.

Before new mathematics I reread or targeted-search-recovered the current controlling and continuity surfaces required by the owner:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- `operations/claims/P0483.md`;
- the P0483/C0041 integrated source, alias, attempt and dedup records;
- all four prior NM13-12 reports, newest first, especially `proofnet24/NM13-12/runs/2026-09-17/2026-09-17T23-54-38Z__p0483-logcost-bypass-bundle.md`;
- newest visible neighboring reports from NM13-11 and NM13-13;
- current repository searches for P0483/C0041 ownership, assignments, handoffs, attempts, audits, posted/settled status, and source corrections.

No release, handoff, retirement, posted source resolution, competing owner, or completed P26/NM13-13 audit for P0483 was recovered. Large repository and search surfaces are connector-bounded; this is source-specific continuity recovery, not a claim of byte-for-byte omniscience.

The method sequence is preserved. Earlier NM13-12 runs used `B2/B6/B30`, then `B18/B24/B4`, then `B5/B21/B22`, then `B1/B11/B28`. The newest report explicitly nominated **B3/B13/B27**; those are the three methods genuinely attempted here.

## 3. Fresh bounded source/literature status check — 2026-09-18 UTC

The exact source remains Alexander Drewitz and Alejandro F. Ramirez, *Selected Topics in Random Walks in Random Environment* (2014), Open Question 2.20: for nearest-neighbor i.i.d. uniformly elliptic RWRE on `Z^d`, `d>=2`, does directional transience in direction `ell` imply positive limiting speed in that direction?

I ran fresh searches for the exact source question and combinations of `directional transience`, `positive speed`, `uniformly elliptic`, `iid`, `RWRE`, `ballisticity`, `2025`, and `2026`; for the Guerra--Ramirez `(T)`/`(T')` line; and for regeneration-time/radius/span moment criteria.

The current directly relevant literature recovered remains:

1. Guerra--Ramirez, *A Proof of Sznitman's Conjecture about Ballistic RWRE*, CPAM 73 (2020), 2087--2103, DOI `10.1002/cpa.21877`: `(T)`, `(T')`, `(T)_gamma` and the polynomial condition are equivalent under the stated uniformly elliptic i.i.d. hypotheses, while the paper still describes mere directional transience => ballisticity as believed rather than proved.
2. Enrique Guerra, *On the connection between transient and ballistic behaviours for RWRE*, arXiv:2006.00570: a stronger transience-to-`(T)` conjecture is attacked under polynomial decay hypotheses; qualitative directional transience alone is not upgraded there.
3. Fribergh--Kious, *Local trapping for elliptic random walks in random environments in Z^d*, PTRF 165 (2016), 795--834, DOI `10.1007/s00440-015-0646-4`: Section 2 records the regeneration structure under directional transience; its Theorem 2.1 gives independent regeneration blocks with the post-first block distributed as the first block under `0-regen`, and Theorem 2.2 states that finite conditional mean regeneration time yields positive speed. The same paper develops trapping criteria and shows how infinite regeneration-time moments arise in non-uniformly-elliptic examples.

No source-matching 2025--2026 resolution and no paper stating the exact one-coordinate regeneration-span criterion below was recovered in this bounded search. That is **bounded negative evidence only**. Publication novelty is **UNVERIFIED**. The ingredients used below—regeneration renewal, Markov's inequality, and the earlier strip-survival estimate—are elementary or classical; I do not claim that the synthesis is new in the literature.

## 4. Frozen metric and counters

The frozen metric remains exactly the admission metric:

`c_slab^(d)(kappa,w)` = the optimal universal quenched exponential exit-tail rate from subsets of a coordinate strip of width `w`, over all static nearest-neighbor environments whose transition probabilities are at least `kappa`.

The second NM13-12 run proved exactly

`c_slab^(d)(kappa,w) = -log rho(K_{d,w}(kappa))`.

**Before this run:** `-log rho(K_{d,w}(kappa))` exactly.  
**After this run:** `-log rho(K_{d,w}(kappa))` exactly.  
**Movement:** none.

I do not replace this saturated universal-static metric by the regeneration quantity below. This is the **third consecutive unchanged run** after the exact metric movement, so

`unchanged_runs = 3`,  
`stuck_recoveries_used = 0`.

Under the owner's Section-I rule, the **next NM13-12 invocation must be a thinking-only stuck-recovery report with no new claims**. This run is the ordinary run that reaches the three-unchanged threshold; it does not pre-consume a recovery episode.

---

# 5. Setup: the regeneration block and the earlier strip inequality

Fix a source-valid i.i.d. uniformly elliptic environment law with ellipticity constant `kappa`, assume directional transience in `ell`, and put

`b := log(1/kappa) > 0`.

Use the standard regeneration construction in direction `ell`. Let

`D = inf{n>=0 : X_n.ell < X_0.ell}`

be the backtracking time in the chosen regeneration convention, and let

`p_reg := P_0(D=infinity) > 0`.

Write

`P_hat( . ) := P_0( . | D=infinity)`

for the post-regeneration block law. Let `tau_1` denote the next regeneration time under this law. For each coordinate direction `e_j`, define the **full regeneration-block coordinate width**

`W_j := 1 + max_(0<=t<=tau_1) X_t.e_j - min_(0<=t<=tau_1) X_t.e_j`.     (5.1)

The first NM13-12 run proved the following uniform quenched range estimate. For every deterministic integer `w>=1`, every `n>=0`, every coordinate `j`, and every `kappa`-elliptic environment,

`P_(0,omega)( W_n^(j) <= w )
 <= w (1-kappa^ceil(w/2))^floor(n/ceil(w/2)),`                         (5.2)

where

`W_n^(j) := 1 + max_(0<=t<=n) X_t.e_j - min_(0<=t<=n) X_t.e_j`.        (5.3)

Because (5.2) is quenched and uniform in the environment, it also holds annealed.

On the event `{tau_1>n, W_j<=w}`, the first `n` steps of the regeneration block have coordinate width at most `w`. Conditioning on `D=infinity` can cost at most `p_reg^(-1)`. Hence

`P_hat(tau_1>n, W_j<=w)
 <= p_reg^(-1) w (1-kappa^ceil(w/2))^floor(n/ceil(w/2)).`              (5.4)

Equation (5.4) is the bridge from the solved strip problem to the source-level regeneration obstruction.

---

# 6. B13 — FIND WHAT ONLY INCREASES: range turns a long block into a two-term tail decomposition

For each coordinate `j`, the partial-path range `W_n^(j)` is nondecreasing in `n`. Thus a long regeneration block has only two possibilities at any chosen width scale `w`:

1. its final coordinate width exceeds `w`; or
2. its first `n` steps remain inside some coordinate strip of width `w`.

Precisely,

`P_hat(tau_1>n)
 <= P_hat(W_j>w)
    + p_reg^(-1) w (1-kappa^ceil(w/2))^floor(n/ceil(w/2)).`           (6.1)

This is a deterministic decomposition valid for every `n,w,j`. It isolates the exact missing source input: the strip term is already completely controlled; only the regeneration-block width distribution remains.

Outcome of **B13**: **success**. The nondecreasing range process converts the old finite-volume strip theorem into a regeneration-time tail mechanism without assuming `(T)`, `(T')`, or a polynomial unlikely-exit condition.

---

# 7. B3 — PROVE SOMETHING STRONGER: exponential span moments transfer to regeneration-time moments

The source asks only for positive speed. Instead I asked for a quantitative all-moment transfer from one coordinate span.

## Theorem `NM13-12-P0483-SPAN-TO-REGEN-06`

Assume the source hypotheses above. Fix a coordinate `j`. Suppose that for some `gamma>0`,

`M_gamma := E_hat[ exp(gamma W_j) ] < infinity`.                      (7.1)

Then for every real

`0 < q < 2 gamma / log(1/kappa)`,                                     (7.2)

we have

`E_hat[ tau_1^q ] < infinity`.                                       (7.3)

More quantitatively, for every

`0 < p < 2 gamma / b`,                                                (7.4)

put

`r := p/(2 gamma)`, so `b r < 1`.

Then for all sufficiently large `n`,

`P_hat(tau_1>n)
 <= M_gamma e^(2 gamma) n^(-p)
    + (p/(gamma p_reg)) log n
      exp[ -(gamma/p) n^(1-p b/(2 gamma)) / log n ].`                (7.5)

In particular, if

`gamma > (1/2) log(1/kappa)`,                                        (7.6)

then `E_hat[tau_1]<infinity`, and therefore the RWRE is ballistic in direction `ell`.

### Proof

Fix `p` as in (7.4), set `r=p/(2gamma)`, and for large `n` define

`m_n := floor(r log n) >= 1`,
`w_n := 2 m_n`.                                                       (7.7)

Use (6.1) with `w=w_n`. First, Markov's inequality and (7.1) give

`P_hat(W_j>w_n)
 <= M_gamma exp(-gamma w_n)
 = M_gamma exp(-2 gamma m_n)
 <= M_gamma e^(2 gamma) n^(-2 gamma r)
 = M_gamma e^(2 gamma) n^(-p).`                                      (7.8)

For the strip term, `ceil(w_n/2)=m_n`. Since `1-u<=e^(-u)`, for all sufficiently large `n`,

`(1-kappa^m_n)^floor(n/m_n)
 <= exp[-kappa^m_n floor(n/m_n)]
 <= exp[-kappa^m_n n/(2m_n)].`                                      (7.9)

Now `m_n<=r log n`, so

`kappa^m_n = exp(-b m_n) >= n^(-b r)`,                              (7.10)

and `2m_n<=2r log n`. Therefore

`kappa^m_n n/(2m_n)
 >= n^(1-br)/(2r log n)
 = (gamma/p) n^(1-pb/(2gamma))/log n.`                              (7.11)

Also `w_n=2m_n<=2r log n=(p/gamma)log n`. Substitution of (7.8)--(7.11) into (6.1) proves (7.5).

Now fix any `q` satisfying (7.2). Choose `p` with

`q < p < 2gamma/b`.

The first term on the right side of (7.5) is `O(n^(-p))`. The second term decays faster than every power because `1-pb/(2gamma)>0`. Hence

`sum_(n>=1) n^(q-1) P_hat(tau_1>n) < infinity`,

which is equivalent, up to standard discrete tail-sum constants, to `E_hat[tau_1^q]<infinity`. This proves (7.3).

If (7.6) holds, choose `q=1` in (7.2). Thus `E_hat[tau_1]<infinity`. Under directional transience, the standard regeneration renewal theorem gives independent post-first regeneration blocks, and the limiting velocity is the ratio of the mean regeneration displacement to the mean regeneration duration. Each regeneration increment makes strictly positive progress in the regeneration direction, so the finite denominator implies positive speed in direction `ell`. This proves the final assertion. `QED`

### What is and is not used

The theorem uses only:

- source directional transience, to have the standard regeneration law;
- uniform ellipticity, through the old strip estimate (5.2);
- one exponential moment of one coordinate span.

It does **not** assume `(T)`, `(T')`, `(P)_M`, a local drift sign, or the new log-cost bypass theorem from the preceding run.

Outcome of **B3**: **success**. The route proves more than positive speed under the added geometric input: it gives the explicit moment transfer threshold `q < 2 gamma / log(1/kappa)`.

---

# 8. B27 — SWAP THE QUANTIFIERS: what every zero-speed counterexample must look like

The theorem has a clean source-level contrapositive.

## Corollary `NM13-12-P0483-ZEROSPEED-SPAN-07`

If a source-valid i.i.d. uniformly elliptic RWRE is directionally transient in `ell` but has zero speed, then for **every** coordinate `j=1,...,d` and every

`gamma > (1/2) log(1/kappa)`,

we necessarily have

`E_hat[ exp(gamma W_j) ] = infinity`.                                (8.1)

Equivalently, no zero-speed counterexample can have an exponentially light regeneration-block width in even one coordinate at any exponent above the explicit threshold `(1/2)log(1/kappa)`.

### Proof

If (8.1) failed for some coordinate `j` and some `gamma>(1/2)log(1/kappa)`, Theorem 7 would imply `E_hat[tau_1]<infinity`, hence positive speed. This contradicts zero speed. `QED`

This does not prove that a zero-speed source counterexample exists. It says that if one exists, its regeneration blocks must spread with simultaneously heavy coordinate-width tails; a one-coordinate exponentially confined mechanism is impossible.

Outcome of **B27**: **success**. Instead of asking directly whether every directionally transient law is ballistic, the route now asks whether directional transience can coexist with the simultaneous failure (8.1) in all coordinates. That is a substantially narrower geometric obstruction.

---

# 9. Relation to the preceding low-log-cost channel theorem

The preceding run proved that directional transience itself forces a strict mean log-cost advantage in at least one coordinate direction pointing into `ell`, and that typical large cylinders contain a positive-density bundle of low-cost straight channels. That theorem did not control whether the walk actually reaches those channels.

The new span criterion identifies exactly one useful missing transfer target: it would suffice to show that directional transience plus the bypass-bundle geometry yields an exponential moment for the width of a regeneration block in **one** coordinate with rate exceeding `(1/2)log(1/kappa)`.

At present I do not see a valid argument for that step. The low-cost channels are environment objects, while `W_j` is sampled under harmonic measure of an entire random regeneration excursion. Treating route abundance as harmonic-measure mass would repeat the gap explicitly diagnosed last run.

This is why P0483 remains OPEN.

# 10. Stuck threshold reached: exact blocker for the next thinking-only run

Although this run produced a source-relevant theorem, the **frozen metric did not move for the third consecutive run**. Under the owner protocol, the next invocation must not add another lemma. Its required blocker is now especially concrete:

`Directional transience  ==>  ?  E_hat exp(gamma W_j) < infinity`

for some coordinate `j` and some `gamma > (1/2)log(1/kappa)`,          (10.1)

or else one must show rigorously why (10.1) cannot be expected and rotate the route according to Section I.

Provisional lenses for that mandated stuck analysis are **B12, B20, B25**. They are **not counted as tried in this run**. The next report must include the full five-part stuck diagnosis, choose exactly one recovery action, and increment `stuck_recoveries_used` only when that recovery is actually selected there.

# 11. Verification / closure accounting

The claims in Sections 7--8 are theorem-sized analytic statements. Their proofs are written on this page. No finite exhaustive assertion or floating-point computation is being promoted, so no exact-arithmetic checker artifact is warranted for this run.

This report is a **self-checking research report**, not an outside audit. No P26 or NM13-13 audit is requested or counted. The parent source remains **OPEN** and NM13-12 remains **PARTIAL**. No closure package is created.

Publication novelty of the span-to-regeneration criterion is **UNVERIFIED**. The bounded search found no exact match, but the proof is an elementary composition of classical regeneration structure with the already-proved strip estimate, so a negative search must not be treated as a novelty certificate.

## 12. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-12
  category: HARD_OUTSIDE
  source_id: P0483
  claim_id: P0483
  historical_alias: C0041
  canonical_dedup_key: directional_transience_versus_positive_speed_under_uniform_ellipticity
  source_status: OPEN
  mathematical_status: PARTIAL
  metric:
    name: c_slab^(d)(kappa,w)
    definition: optimal universal quenched coordinate-strip exit-tail exponent in static kappa-elliptic NN environments
    before: "-log rho(K_{d,w}(kappa)) exactly"
    after: "-log rho(K_{d,w}(kappa)) exactly"
    movement: none
  methods:
    - B3: "proved stronger quantitative transfer: E_hat exp(gamma W_j)<infinity implies E_hat tau_1^q<infinity for every q<2gamma/log(1/kappa); gamma>0.5log(1/kappa) implies ballisticity"
    - B13: "used monotone coordinate range to decompose a long regeneration block into wide-span or strip-confined alternatives, with the strip term controlled by the previous uniform theorem"
    - B27: "derived the contrapositive zero-speed obstruction: every coordinate span lacks every exponential moment above 0.5log(1/kappa)"
  strongest_new_claim: NM13-12-P0483-SPAN-TO-REGEN-06
  companion_claim: NM13-12-P0483-ZEROSPEED-SPAN-07
  finite_checker_created: false
  reason_no_checker: theorem-sized analytic proof only; no finite exhaustive claim
  unchanged_runs: 3
  stuck_recoveries_used: 0
  stuck_protocol_next_run: true
  audits:
    P26: NOT_REQUESTED
    NM13-13: NOT_REQUESTED
  literature_check_date_utc: 2026-09-18
  literature_scope: "exact source question; 2025-2026 directional-transience/ballisticity search; Guerra--Ramirez; Guerra; Fribergh--Kious; regeneration span/radius moment searches"
  literature_outcome: "no source-matching closure or exact span criterion recovered; bounded negative evidence only; novelty UNVERIFIED"
  next_obligation: "mandatory Section-I thinking-only stuck report; decide whether directional transience can force one-coordinate regeneration-span exponential moment above half log(1/kappa), or select a prescribed recovery/rotation route"
  provisional_next_lenses_not_yet_tried: [B12, B20, B25]
  shared_roots_edited: false
  peer_files_edited: false
  schedules_modified: false
```
