Model: GPT-5.6 Sol. Reasoning: UNVERIFIED — GPT-6 maximum was requested, but the scheduler exposes no model selector or reasoning-effort selector; I do not claim otherwise.
Problem: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (2014), arXiv:1302.6958, Problem 7.2; intake I0076. Metric **NO MOVEMENT: 3/4 -> 3/4** source-witness obligations for the same frozen candidate `X_BS`.

# Status

**PARTIAL / OPEN source problem.** This run keeps the same frozen candidate from the preceding two R15 runs: the Burdzy–Scheutzow Theorem 6.1 FBM+BBM process `X_BS`, obtained from the Theorem-6.1 discrete increment process by Remark 2.6(i).

The frozen witness ledger is now stronger but the source metric remains 3/4:

| source-witness obligation for `X_BS` | status |
|---|---|
| FBM | **PROVED (source: Theorem 6.1 + Remark 2.6(i))** |
| BBM | **PROVED (source: Theorem 6.1 + Remark 2.6(i))** |
| existence of a random `T` with independent centered future and past half-processes | **DISPROVED FOR THIS CANDIDATE in this run** |
| failure of the 2BM law | **PROVED (source: Theorem 6.1)** |

The metric therefore stays `3/4`: the third *witness* obligation is not established; it is now proved impossible for this candidate. This is the second consecutive no-movement run after the 3/4 baseline, so `unchanged_count = 2`.

This run completes a **documented route switch trigger**: the frozen Theorem-6.1 candidate is eliminated as a counterexample to Problem 7.2 at *every real random time*, not merely at skeleton/integer seams. A subsequent run may switch candidate or switch to the positive route; it must not silently continue treating `X_BS` as viable.

# Exact source definitions and Problem 7.2

Definition 2.1 of the source says:

- `X=(X_t)_{t in R}` is an **FBM** if there exist random times `S_n -> -infinity` a.s. such that, for every `n`, `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion.
- `X` is **BBM** if `(X_{-t})_{t in R}` is FBM.
- `X` is **2BM** if there exists a random time `S` such that `(X_{S+t}-X_S)_{t>=0}` and `(X_{S-t}-X_S)_{t>=0}` are independent standard Brownian motions.

Problem 7.2 asks exactly:

> Assume that `X` is an FBM and BBM and there exists a random time `T` such that the processes `X_{T+t}-X_T, t>=0` and `X_{T-t}-X_T, t>=0` are independent. Do these assumptions imply that `X` is 2BM?

The Problem-7.2 independence hypothesis does **not** assume that either half-process at `T` is Brownian.

Problem 7.5 remains excluded: the campaign index records it as already settled.

# Required repository continuity

Read/query before continuing this run:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FLEET_2026-09-16.md` and `operations/RFLEET_2026-09-16.md`;
- the I-intake `probability_1000_intake_I_20260914/problems.jsonl` and mirrored intake/search records for I0076;
- newest own report `runs/R15/20260916_1457Z_i0076_integer_seam_list_a12.md` and preceding baseline report `runs/R15/20260916_1356Z_i0076_bs_candidate_a11.md`;
- recovered older P0030 state (“Compatibility of forward and backward Brownian decompositions”) through the prior R15 report/search record;
- newest visible R14 neighboring report `runs/R14/2026-09-16T15-09-09Z_r14-c177-alpha2168.md`;
- newest R17 report `runs/R17/20260916_1515Z_spantrunc_a63e.md` for the directed audit duty.

The GitHub connector bounds/truncates large repository and JSONL search outputs, so I do not claim that all roughly 780 intake records were displayed verbatim. The current ownership/assignment files and relevant intake/attempt mirrors were queried. R15/I0076 remains assigned and is neither posted nor settled in the root exclusion records.

P26 alone edits shared ledgers. This run does **not** edit `RESULTS.md`, `QUEUE.md`, `POSTED.md`, or another track.

# Current outside-source/status check — 2026-09-16

Primary source re-read from arXiv/source PDF and publication record:

- Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 (29 March 2013), published in *Probability Theory and Related Fields* 160 (2014), 95–126, DOI `10.1007/s00440-013-0524-x`.
- Definition 2.1, Remark 2.6(i), Theorem 6.1, Proposition 6.2, and Problem 7.2 were rechecked.

Dated bounded queries included:

1. `"Forward Brownian Motion" Burdzy Scheutzow 2014 arXiv 1302.6958 Problem 7.2`;
2. `"Forward Brownian Motion" Burdzy Scheutzow Problem 7.2 independent past future random time`;
3. `"Burdzy" "Scheutzow" "Problem 7.2" Brownian`;
4. `"Forward Brownian Motion" 1302.6958 Burdzy Scheutzow cited by`;
5. `"independent" "forward Brownian motion" Burdzy Scheutzow`.

The bounded search found the original source/publication and later citations (including the 2015 Pitman–Tang Slepian-zero-set paper in the citation graph) but no paper explicitly claiming a resolution of Problem 7.2. This is a bounded dated search outcome, **not** proof that no uncatalogued resolution exists.

# Retained state from run a12

Run a12 proved a finite-list common-word lemma and used the Theorem-6.1 copied blocks to show:

1. the discrete Theorem-6.1 process has no independent random **integer** seam at all, even without a random-walk marginal hypothesis;
2. consequently the Remark-2.6 Brownian embedding has no independent seam at any skeleton time `T=M_S`.

Its exact self-check remains archived at

- `artifacts/R15/i0076_integer_seam_list_checker.py`, commit `28b2f606a28b42fa37aac2eb8864d81582b45097`;
- output commit `d94471b70babb6db6fdb5fca88c6893cb55e10fe` (PASS).

The only apparent hole was an arbitrary **interior** real random time. The present run closes that hole by a different argument; no lattice-phase decoding is needed.

# I0076-R15-L5 — universal Brownian tail normality from an arbitrary finite center

**Status: PROVED.**

Let `X` be any FBM and let `T` be any a.s. finite real random time; `T` need not be a stopping time and may depend on the whole trajectory. Then

`(X_{T+t}-X_T)/sqrt(t) => N(0,1)` as `t -> infinity`.       (L5.1)

Moreover, if `q_n -> infinity` is deterministic and `tau_n/q_n -> 1` in probability, with `tau_n` arbitrary and possibly path-dependent, then

`[X_{tau_n}-X_{q_n}]/sqrt(q_n) -> 0` in probability.       (L5.2)

The analogous two statements hold at `-infinity` for every BBM.

## Proof

Choose one FBM origin `S` from Definition 2.1 and put

`B_u = X_{S+u}-X_S, u>=0`.

As a process, `B` is standard Brownian motion. No independence between `S` and `B`, or between any subsequently chosen random time and `B`, is needed.

First prove L5.2. Fix `eta in (0,1/4)`. On

`E_n(eta)={|S|<=eta q_n, |tau_n-q_n|<=eta q_n}`,

the two Brownian-time parameters `q_n-S` and `tau_n-S` lie in

`[(1-2eta)q_n,(1+2eta)q_n]`.

Therefore

`|X_{tau_n}-X_{q_n}|/sqrt(q_n)`

is bounded by the oscillation of `B/sqrt(q_n)` on that deterministic interval. By Brownian scaling, its tail probability is bounded by the probability that a standard Brownian path has oscillation bigger than the same fixed threshold on `[1-2eta,1+2eta]`. Brownian continuity makes this bound tend to zero as `eta downarrow 0`. For each fixed `eta`, `P(E_n(eta)^c)->0` because `S/q_n->0` a.s. and `tau_n/q_n->1` in probability. This proves L5.2.

For L5.1, write

`X_{T+t}-X_T`
` = [X_{T+t}-X_{S+t}] + [X_{S+t}-X_S] + [X_S-X_T]`.

The middle term is `B_t`, so divided by `sqrt(t)` it is exactly `N(0,1)`. The first term is an endpoint perturbation by the a.s.-finite random shift `T-S`; the same oscillation argument (now even with a tight absolute shift) makes it `o_P(sqrt(t))`. The last term divided by `sqrt(t)` tends to zero a.s. Slutsky proves L5.1.

For BBM apply the same argument to the FBM `Y_u=X_{-u}`. `□`

This lemma is general, not candidate-specific: FBM/BBM gives Brownian *one-point diffusive tails about any finite random center*, even though the finite-time half-process at that center need not be Brownian.

# I0076-R15-L6 — the Theorem-6.1 copied blocks lock the two opposite diffusive tails together

**Status: PROVED for the frozen `X_BS`.**

Use the exact Theorem-6.1 notation. At stage `n`, the source has random integers

`a_n < 0 < b_n`,

a deterministic `c_n`, and a deterministic copied-block length `d_n`. It chooses

`P(|a_n| vee b_n >= c_n) < 1/n^2`                         (6.1)

and copies the fresh right block by

`V_k = V_{k-a_n+d_n+b_n+1}`

for `k=a_n-d_n,...,a_n-1`.

For the continuous embedding the source then chooses `epsilon_n,s_n` and enlarges `d_n` so that

`4 c_n / sqrt(d_n) <= epsilon_n/2`                       (6.7)

and, with the Remark-2.6 skeleton times `M_j`, equation (6.8) gives

`M_{a_n-d_n}/d_n -> -1`,
`M_{b_n+d_n}/d_n -> +1`

in probability; in fact the source gives probability at most `2/n^2` for the respective relative errors exceeding `s_n/2`.

The signs in the first centering are forced by `a_n-d_n<0` and `M_0=0`; the PDF's displayed (6.8) is the source used here. Also `s_n<epsilon_n`.

The choice (6.3) forces `epsilon_n->0`: taking `x=0` and the single time `t=1`,

`P(|B_1|<=2 epsilon_n) <= 1/n^2`,

so a subsequence bounded away from zero is impossible. Hence `s_n->0`, and (6.7) yields

`c_n/sqrt(d_n) ->0`.                                      (L6.1)

Now use the copied-block identity. Put

`L_n=a_n-d_n`, `R_n=b_n+d_n`.

Because

`sum_{k=a_n-d_n}^{a_n-1} V_k`
` = sum_{k=b_n+1}^{b_n+d_n} V_k`,

and `Z_{k+1}-Z_k=V_k`, exact rearrangement gives

`Z_{L_n}+Z_{R_n}`
` = Z_{a_n}+Z_{b_n+1}-V_{b_n+d_n}`.                      (L6.2)

On the event `|a_n| vee b_n < c_n`, unit increments and `Z_0=0` imply

`|Z_{L_n}+Z_{R_n}| <= |a_n|+(b_n+1)+1 <= 2c_n`.          (L6.3)

Remark 2.6 has `X(M_j)=Z_j`. Therefore (6.1), (6.7), and L6.3 give

`[X(M_{L_n})+X(M_{R_n})]/sqrt(d_n) ->0` in probability.  (L6.4)

By (6.8), L5.2 applied to the positive tail and its BBM analogue applied to the negative tail give

`[X(M_{R_n})-X(d_n)]/sqrt(d_n) ->0`,

`[X(M_{L_n})-X(-d_n)]/sqrt(d_n) ->0`.                     (L6.5)

Hence

`[X(d_n)+X(-d_n)]/sqrt(d_n) ->0` in probability.          (L6.6)

Finally, for any a.s.-finite random real `T`, the finite-shift part of L5 yields

`[X(T+d_n)-X(d_n)]/sqrt(d_n) ->0`,

`[X(T-d_n)-X(-d_n)]/sqrt(d_n) ->0`,

and `X_T/sqrt(d_n)->0`. Combining with L6.6,

`{[X(T+d_n)-X_T]+[X(T-d_n)-X_T]}/sqrt(d_n) ->0`          (L6.7)

in probability, for **every** a.s.-finite random `T`.

`□`

Interpretation: the source's duplicated discrete word produces an asymptotic *anti-lock* of the forward and backward centered diffusive tails: their sum is forced to vanish along the deterministic source scale `d_n`.

# I0076-R15-T1 — the frozen Theorem-6.1 candidate has no independent real seam

**Status: PROVED. Candidate-specific theorem; this does not solve Problem 7.2.**

For the Brownian process `X_BS` constructed in Theorem 6.1 / Remark 2.6(i), there is **no a.s.-finite random real time `T`** such that

`F=(X_{T+t}-X_T)_{t>=0}`

and

`P=(X_{T-t}-X_T)_{t>=0}`

are independent random processes.

## Proof

Assume such a `T` exists. For the deterministic copied-block scale `d_n`, define

`F_n=[X(T+d_n)-X(T)]/sqrt(d_n)`,

`P_n=[X(T-d_n)-X(T)]/sqrt(d_n)`.

Because the two half-processes are independent, `F_n` and `P_n` are independent for every `n`.

The candidate is FBM and BBM. By L5,

`F_n => N(0,1)`,

`P_n => N(0,1)`.                                        (T1.1)

Independence at every `n` therefore implies joint convergence to two independent standard Gaussians: for all real `u,v`, the joint characteristic function factors and converges to

`exp(-u^2/2) exp(-v^2/2)`.

Consequently

`F_n+P_n => N(0,2)`.                                    (T1.2)

But L6.7 gives

`F_n+P_n ->0` in probability.                            (T1.3)

A sequence cannot converge in distribution both to `N(0,2)` and to the point mass at zero. Contradiction. `□`

This strictly extends the candidate-specific exclusions retained from the source and run a12:

- source Proposition 6.2(i) excluded independent halves when the future half at `T` is standard Brownian;
- run a12 excluded every integer/skeleton seam without any marginal Brownian hypothesis;
- T1 excludes **every real random seam**, with no Brownian assumption on either half at `T`.

Thus the Theorem-6.1 process cannot be the desired Problem-7.2 counterexample.

# Exact finite self-check

Created, executed locally with exact integer/rational arithmetic, archived, and read back from GitHub:

- `artifacts/R15/i0076_any_seam_clt_checker.py`
  - creation commit `ec9bd583a176851c0a2ac3e401d4a2c1af2a25b4`;
- `artifacts/R15/i0076_any_seam_clt_checker.out`
  - creation commit `61f827dfeb775003e490f85ef2f48d3dd9af87a9`.

Archived output:

- copied endpoint-sum identity: PASS on 1,260 exact symbolic-index cases;
- deterministic `2c` endpoint bound: PASS on the same 1,260 cases;
- exhaustive sign realizations: PASS on 720 cases;
- independent Gaussian sum variance: exact `2`;
- source-scale squared implication: PASS on 3,781 exact-rational instances;
- final verdict: **PASS**.

This is a **self-check** of the finite/algebraic core. The stochastic theorem is proved on the page above; the script is not substituted for the proof.

# Adversarial checks / limitations

1. **Random `T` need not be a stopping time.** L5 never uses a stopping-time property; random shifts are controlled by unconditional Brownian oscillation bounds.
2. **Random synchronization times may depend on the path.** L5.2 only uses `tau_n/q_n->1` in probability and an unconditional Brownian modulus over a deterministic relative window; no independence is assumed.
3. **No exchange of asymptotic laws with exact Brownianity.** T1 uses only marginal diffusive tail convergence to `N(0,1)`, derived from FBM/BBM, plus the exact independence hypothesis at `T`.
4. **Candidate-specific copied-block input.** L6 uses Theorem 6.1's exact copied-block relation and its continuous-scale choices (6.1), (6.7), (6.8). T1 is not a theorem about all FBM+BBM processes.
5. **No source closure.** Eliminating one natural 3/4 candidate does not answer Problem 7.2 either positively or negatively.

# Route decision

The frozen candidate is now **dead** for the counterexample-first route. This report is the documented route-switch point required by the protocol.

The next run must choose one of two source-matching directions:

1. **new explicit pasting candidate** that is FBM+BBM, has a provable independent non-Brownian seam, and is not 2BM; or
2. **positive route**, transparently changing the metric once, proving that *every* source-admissible FBM+BBM with one independent seam must have Brownian halves at that seam.

The old Theorem-6.1 process and all its proofs remain preserved as a negative candidate test and must not be renamed into a new candidate.

A useful necessary condition for any future counterexample follows from L5: at its independent seam, each half must be asymptotically Brownian under diffusive scaling, even though it may fail finite-time Brownianity. Any pasting construction whose two independent halves have a non-Gaussian diffusive tail is immediately impossible under FBM+BBM.

# R17 directed audit check

The newest visible R17 report is

`runs/R17/20260916_1515Z_spantrunc_a63e.md`.

It explicitly labels the Chvatal–Sankoff target **OPEN**, keeps the certified interval width unchanged, and says its next run must be a stuck/thinking run. It is not a closure package. Therefore the instruction “independently audit R17 when a package is ready” is **not triggered** this run; no audit verdict is invented.

# Old R15 Cugliandolo–Kurchan handoff

The retired CK assignment remains preserved exactly as in the preceding R15 handoff: **OPEN; no verified full-aging closure**. No CK file, schedule, or claim was modified or revived.

# ledger_delta

```yaml
ledger_delta:
  track: R15
  source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion (2014), arXiv:1302.6958, Problem 7.2; I0076"
  target: "Decide whether FBM + BBM + source independence at a random T forces 2BM; counterexample-first"
  frozen_metric: "number of four source-witness obligations proved for one frozen candidate: FBM; BBM; required independence at T; failure of 2BM"
  candidate: "Theorem-6.1 / Remark-2.6(i) process X_BS"
  before: "3/4"
  after: "3/4"
  movement: "NO MOVEMENT"
  status: "PARTIAL / source OPEN; frozen candidate eliminated"
  unchanged_count: 2
  exact_evidence:
    - "source Theorem 6.1 + Remark 2.6(i): FBM, BBM, non-2BM"
    - "I0076-R15-L5: arbitrary-center FBM/BBM tail normality"
    - "I0076-R15-L6: copied-block opposite-tail lock"
    - "I0076-R15-T1: no independent real seam for X_BS"
    - "artifacts/R15/i0076_any_seam_clt_checker.py @ ec9bd583a176851c0a2ac3e401d4a2c1af2a25b4"
    - "artifacts/R15/i0076_any_seam_clt_checker.out @ 61f827dfeb775003e490f85ef2f48d3dd9af87a9 (PASS)"
  audits:
    p26: "NONE for T1"
    other: "NONE for T1; prior R14 finite-core audit concerns earlier L1 only"
  route_switch: "DOCUMENTED: X_BS eliminated; next run must use a new source-matching candidate or transparently switch to universal positive proof"
```

# Overall conclusion

**Problem 7.2 remains OPEN in this track. Metric remains 3/4.**

The substantive result is that the most natural source candidate is now eliminated completely: its copied-block geometry forces the two opposite diffusive tails to have vanishing sum along `d_n`, whereas FBM+BBM plus independence at an arbitrary random seam would force those same two scaled tails to converge jointly to independent standard normals, whose sum is `N(0,2)`.

No Gmail, Drive, email, public publication, purchase, permission change, shared-ledger edit, or schedule change was performed.
