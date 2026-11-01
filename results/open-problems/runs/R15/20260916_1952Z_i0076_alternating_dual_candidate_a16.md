Model actually run: **GPT-5.6 Sol. Reasoning: UNVERIFIED** — GPT-6 / maximum was requested, but the exposed runtime/scheduler surface has no model-family selector and no reasoning-effort selector. **NO METRIC MOVEMENT: active positive-route gates `2/4 -> 2/4`; unchanged count `1 -> 2`. Section-B moves: #11 DUALIZE, #20 FIND WHY THE ALGORITHM FAILS, #30 ONE SCALE / ONE DIRECTION AT A TIME.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958, published in PTRF 160 (2014), Problem 7.2; intake I0076.

Status: **OPEN / PARTIAL**. No source-level closure is claimed.

# 1. Exact source target and continuity

I reread the current repository state before doing new mathematics: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the current fleet manifests, the newest R15 report, and the current neighboring R17 report. `POSTED.md` excludes the already-settled Problem 7.5, not Problem 7.2. The active ownership of I0076 remains R15.

The exact source definitions are still the ones on pp. 2 and 25--26 of arXiv:1302.6958:

- FBM: there are random times `S_n -> -infinity` such that `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion for every n;
- BBM: `(X_{-t})` is FBM;
- 2BM: there is one random S for which the centered future and centered backward halves are **independent standard Brownian motions**;
- Problem 7.2 assumes FBM + BBM and one finite random real T for which the two entire centered half-processes are independent. T need not be a stopping time and neither half at T is assumed Brownian.

The previous frozen Theorem-6.1 candidate remains retired at source-witness score `3/4`: R15 proved that it admits no independent real seam at all. The subsequent transparent positive-route metric remains:

- P1 invariant-event / shift-coupling compiler: PROVED;
- P2 complete discrete FRW+BRW analogue: PROVED;
- P3 remove the genuinely continuous anticipative phase obstruction under the exact source hypotheses: OPEN;
- P4 source conclusion + closure package/audits: OPEN.

The previous run proved the uniform-phase smoothing theorem but did not move P3, hence this run starts at `2/4` with unchanged count 1.

A dated bounded literature/status pass on 2026-09-16 checked the original arXiv/PTRF source, the University of Washington publication page, later papers surfaced as citing *Forward Brownian Motion* (including Pitman--Tang 2015), and bounded searches for `"Forward Brownian Motion" "Problem 7.2"`, `Burdzy Scheutzow independent past future random time`, and later-author work. I found no accessible later paper explicitly claiming a resolution of Problem 7.2. This is a bounded search result, **not** a proof of present-day openness.

# 2. Move #11 — dualize: a new explicit 3-of-4 counterexample test family

The main new route is an explicit decomposable construction in which forward Brownian pieces and backward Brownian pieces arise from **two different pairings of the same reversible/Bessel factors**.

This is new to the current R15 track. It does **not** reset the active positive-route metric and it is not claimed to solve the problem.

## 2.1 One-sided first-passage factorization

Let B be standard Brownian motion started at 0. Put

`tau_+ = inf{t>=0: B_t=1}`,
`sig_+ = sup{t<=tau_+: B_t=0}`.

Let `C^+` denote the stopped prefix `(B_t)_{0<=t<=sig_+}`.

**Lemma A16.1 (prefix reversibility).**
`C^+` and its time reversal `(B_{sig_+-t})_{0<=t<=sig_+}` have the same law.

**Proof.** Index Brownian excursions away from 0 by local time. Let `A_+` be the excursion event "the excursion hits +1". The `A_+` excursions form a Poisson process in local-time parameter, and the first `A_+` label is exponential. Conditional on this first label being ell, the excursions before ell are a Poisson point process on `[0,ell)` with Ito excursion measure restricted to `A_+^c`. Reflection of the local-time coordinate `u -> ell-u` preserves this Poisson law. Time reversal preserves Ito excursion measure, and `A_+^c` is time-reversal invariant because it is a range property. Concatenating the reversed excursions therefore has the same law as the original prefix. Integrating over ell proves the claim. □

The terminal excursion from the last zero to +1 is independent of the prefix and is the BES(3) ascent U from 0 to 1. This is the same Williams decomposition used in Remark 2.6 of the source. The source records the useful reversibility

`(U_{tau_U}-U_{tau_U-t})_{0<=t<=tau_U} =_d (U_t)_{0<=t<=tau_U}`.

Consequently

`C^+ \oplus U`

has exactly the law of Brownian motion stopped at `tau_+`.

For the -1 target define `C^- := -C^+` in law; then

`C^- \oplus (-U)`

is Brownian motion stopped at `tau_- = inf{t:B_t=-1}` and `C^-` is reversible as well.

## 2.2 Alternating construction

Let `eps_k=(-1)^k`, with `eps_0=+1`. Take mutually independent copies `(C_k,U_k)`, with `C_k` distributed as `C^{eps_k}` and U_k as U. Define the kth path piece

`W_k = C_k \oplus eps_k U_k`.

Equivalently, `W_k` is a standard Brownian path stopped at first hit of `eps_k`.

Let its duration be `T_k`, set `S_0=0`, `S_{k+1}-S_k=T_k`, and concatenate the W_k in increasing k. The sums of durations diverge in both directions a.s. (for example `P(T_k>1)` is a fixed positive number, so infinitely many terms exceed 1). Let X denote the resulting continuous process.

### Obligation 1: FBM — PROVED for this test family

This is a decomposable process in the exact sense of Definition 2.2. From every boundary S_k, the future is a concatenation of independent standard-Brownian stopped pieces. Strong Markov concatenation gives standard Brownian motion. Since `S_k -> -infinity` as `k -> -infinity`, X is FBM.

### Obligation 3: source independence — PROVED for this test family

At `T=S_0=0`, the future half uses only the independent pieces with k>=0, while the past half uses only pieces k<0. Therefore the two entire centered half-processes are independent. This is the exact Problem-7.2 independence hypothesis, not deterministic-time increment independence and not a stopping-time substitute.

### Obligation 2: BBM — PROVED for this test family

Let `O_k` be the internal split time at the end of C_k and the beginning of `eps_k U_k`.

Run the path **backwards** starting from O_k. The first backward component is `C_k` time-reversed, hence has law `C^{eps_k}` by Lemma A16.1. The next backward component is the terminal BES(3) part of piece k-1 traversed backwards and recentered. By the source's U-reversibility, its law is

`-eps_{k-1} U = eps_k U`,

because the signs alternate. Hence the first whole backward block has law

`C^{eps_k} \oplus eps_k U`,

which is a standard Brownian path stopped at first hit of `eps_k`.

The next backward block uses `C_{k-1}` and `U_{k-2}`, and so on. These blocks use disjoint independent components. Therefore the entire backward process from O_k is standard Brownian motion obtained by concatenating independent Brownian stopped pieces. Since `O_k -> -infinity` as `k -> -infinity`, the time-reversed process has FBM witnesses and X is BBM.

Thus this explicit family satisfies **three source obligations simultaneously**:

1. FBM — proved;
2. BBM — proved;
3. independent centered past/future at T=0 — proved;
4. failure of 2BM — **OPEN**.

Again, this `3/4` is a diagnostic score for the new subcandidate only; I am **not** replacing the already-declared active positive-route metric `2/4`.

## 2.3 Strongly decomposable regrouping

There is a useful simplification. Pair pieces `(W_{2m},W_{2m+1})`. Starting from level 0, the pair is exactly Brownian motion run until first hit of +1 and then, by strong Markov, continued until first return to 0. Hence each pair is itself a standard Brownian path stopped at the finite stopping time

`Theta = inf{t>tau_{+1}: B_t=0}`.

The pairs are iid. Therefore X is actually **strongly decomposable** when viewed at the pair-boundaries `R_m=S_{2m}`. Moreover `E Theta = infinity` (already the one-sided first-passage time has infinite mean).

This puts the remaining fourth obligation exactly in the regime highlighted by source Remark 7.6: if the renewal boundary process `{R_m}` could be shown path-identifiable, then its infinite-mean renewal law could not be made stationary by any random shift, which would prove X is not 2BM and would refute Problem 7.2.

I did **not** prove that identifiability. The precise counterexample subproblem is now:

> Is there a measurable, shift-covariant recovery of the pair-boundary set `{R_m-T}` from the whole centered path `(X_{T+t}-X_T)_{t in R}`?

The immediate difficulty is that every spatial level of a recurrent Brownian-looking path has its own alternating first-passage crossing chain, so the special 0/1 phase is not obviously path-identifiable.

# 3. Move #20 — find why the discrete/P2 algorithm fails in continuous time

I also attacked the positive route by trying to refine P2 from signs to full scale-1 exit-path marks.

Let Q be the law of a Brownian path started at 0 and stopped on first exit from (-1,1), retaining the entire stopped path, not just the terminal sign. Let `check Q` be the law obtained by reversing such a cell in time and recentering at its endpoint.

**Lemma A16.2 (orientation mark is singular).** `Q` and `check Q` are mutually singular.

**Proof.** If a Q-cell exits at +1, then before the first exit its path is strictly below +1. After time reversal and recentering at +1, the entire reversed cell stays non-positive and ends at -1. Similarly, a reversed cell coming from a -1 exit stays non-negative and ends at +1. Hence under `check Q`, with probability one the stopped path has one fixed sign for every positive time up to its endpoint.

Under Q, Brownian motion oscillates on both sides of 0 arbitrarily close to time 0 almost surely. Therefore the event "the whole stopped path has one fixed sign after time 0" has Q-probability 0 and `check Q`-probability 1. □

This identifies exactly why the discrete theorem P2 does not automatically lift by marking every random-walk edge with its Brownian cell. The sign projection is reversal-invariant (fair +/-1), but the full Brownian cell carries a **singular orientation mark**. Re-rooting across one cell flips Q into `check Q`.

So a fixed-scale marked-skeleton algorithm does not remove P3. The missing continuous variable is precisely the last-zero/BES split phase from Remark 2.6. This is the same phase exploited by the dual construction above.

This failure is useful: another sign-only discretization cannot solve the problem. Any positive proof has to control the continuous last-zero phase, or use an invariant/Palm argument that bypasses individual cell orientation.

# 4. Move #30 — one direction at a time: what is actually left

This run separated the source problem into four exact directions for the new dual candidate:

- forward Brownianity: closed by decomposable concatenation;
- seam independence: closed by independent piece families;
- backward Brownianity: closed by cross-pairing reversible prefixes with the previous BES suffix;
- non-2BM: not closed.

For the positive route, the same separation says P3 cannot be a statement merely about exit signs or one-sided Wiener absolute continuity: the obstruction lives in how the two orientations assign the non-stopping last-zero phase.

The most promising next negative attack is **not** to invent another piece law. It is to stay with the alternating dual candidate and attack the single identifiable-boundary question above, preferably by an invariant of its paired renewal structure. If identifiability fails, the next positive attack should work directly with the last-zero phase as a Palm/allocation variable rather than with sign skeletons.

# 5. Source hierarchy sanity check

There is a logical-direction anomaly worth preserving for future work. A decomposable FBM at its decomposition boundary automatically has independent past and future piece families; therefore any decomposable FBM+BBM (Problem 7.1 hypothesis) is in the Problem-7.2 hypothesis class. Thus, purely by class inclusion,

`YES to Problem 7.2 => YES to Problem 7.1`,

and any counterexample to 7.1 is automatically a counterexample to 7.2.

The printed sentence on p. 26 says the affirmative implication in the opposite direction. I record this only as a source-text logical-direction anomaly; it is not used as a closure claim and I am not asserting publication errata without external confirmation.

This makes the decomposable dual candidate route especially relevant: a successful proof of its fourth obligation would in fact refute both 7.1 and 7.2.

# 6. Prior art / nearby mechanisms checked this run

Dated 2026-09-16 searches included:

- original arXiv:1302.6958 and the University of Washington publication page;
- Williams path decomposition / BES(3) reversal as cited by the source;
- bounded searches for later work explicitly mentioning Problem 7.2;
- splitting-time literature, where non-stopping splits can have non-Brownian post-laws;
- Last--Mörters--Thorisson unbiased Brownian shifts / Palm-allocation methods;
- Pitman--Yor Bessel splicing and related Brownian path decompositions.

No accessible source found in this bounded pass states the alternating-dual construction above or resolves its non-2BM status. That is **not** a priority claim.

# 7. R17 audit trigger

The newest R17 report read this run is still OPEN / PARTIAL (Chvatal--Sankoff interval work), not a closure package. The independent-audit instruction is therefore not triggered; no audit verdict is fabricated.

# 8. Model/scheduler control status

Nothing has changed in the exposed task interface. It supports prompt/title/schedule/relative-start/enablement/timing-mode fields but exposes **no model selector and no reasoning selector**. Thus `GPT-6 / maximum` remains text in the prompt, not an authenticated runtime setting here. To change this in a verifiable way would require an authorized scheduler/runtime surface that stores model/reasoning fields and completed-run metadata confirming them.

The current deployment record also says all tested P/C scheduler IDs returned `You cannot modify this task` from this R context, while another authorized context subsequently updated them. The legitimate workaround is the owning/authorized context, a permission change by the owner/platform, or an explicit canonical handoff/replacement. Creating duplicate tasks is not a legitimate bypass.

# 9. Ledger delta

```yaml
ledger_delta:
  track: R15
  source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion (2014), arXiv:1302.6958, Problem 7.2; intake I0076"
  target: "Decide whether FBM + BBM + source-exact independence of centered half-processes at an arbitrary random real T implies 2BM"
  active_metric: "positive-route gates P1/P2/P3/P4 proved"
  before: "2/4"
  after: "2/4"
  metric_movement: "NO MOVEMENT"
  unchanged_count_before: 1
  unchanged_count_after: 2
  status: "OPEN / PARTIAL"
  tried_moves:
    - "11 DUALIZE: cross-pair reversible Brownian prefixes with the previous BES suffix; produced explicit decomposable FBM+BBM+independent-seam test family"
    - "20 FIND WHY THE ALGORITHM FAILS: full exit-cell mark law Q is singular to its reversed mark law, so P2 sign skeleton cannot simply be upgraded"
    - "30 ONE SCALE/ONE DIRECTION: proved the three non-2BM obligations separately and isolated path-identifiability as the sole missing candidate obligation"
  new_exact_evidence:
    - "A16.1 prefix-reversibility proof by Ito excursion PPP"
    - "alternating-dual candidate: FBM PROVED; BBM PROVED; source independence at T=0 PROVED; non-2BM OPEN"
    - "paired construction is strongly decomposable with infinite-mean iid superpiece duration"
    - "A16.2 Q versus reversed-Q singularity proof"
  remaining_obligation: "Either prove the paired renewal boundary process path-identifiable (then Remark 7.6 gives a counterexample), or prove an actual last-zero/Palm phase theorem that removes P3 for all source-admissible X."
  audits:
    prior_R14_candidate_audits: "retained from earlier R15 history"
    R17_this_run: "NOT_TRIGGERED; newest R17 package is not closure-ready"
  checker: "none created: new claims are theorem-sized and proved on page; no finite computational claim introduced"
```

# 10. Next attack

If the metric does not move next run, unchanged count will reach 3 and the mandatory stuck protocol should trigger on the following run according to the fleet contract.

Before that threshold, the highest-value next attack is to keep this same alternating-dual candidate and test the exact Remark-7.6 identifiability condition. The right object is the paired renewal boundary set `R_m=S_{2m}`. The proof must either:

1. give a measurable shift-covariant decoder of `{R_m-T}` from the centered whole path, which would close the missing non-2BM obligation by the source's infinite-mean renewal argument; or
2. exhibit a genuine alternative phase for the same path, proving this candidate cannot be closed through Remark 7.6 and forcing a route switch.

Planned unused Section-B moves for that attack: **#19 MAKE IT AN ALGORITHM** (write the boundary decoder), **#26 HUNT THE SPORADIC CASE** (classify competing phases), **#29 ADD THE POINTS AT INFINITY** (analyze bi-infinite crossing-chain phases rather than one finite anchor).

No Gmail, email, Drive, public posting, shared-root edits, permission changes, or scheduler changes were made.
