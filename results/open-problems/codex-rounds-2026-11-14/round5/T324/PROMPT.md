# Open problem T324: Metastable clustering times in mean-field transformer dynamics

Statement: In the self-attention particle system of T323 with large beta, tokens first form several clusters that persist for a time exponentially long in beta before merging. Bruno, Pasqualotto and Agazzi describe this metastable phase in the mean-field limit. Prove the number of metastable clusters and the exponential time scales of their merging (a Freidlin–Wentzell-type or slow-manifold description), for the deterministic dynamics and for the dynamics with small noise.

Caveat: Partial results describe the first stage (number of clusters ~ sqrt(beta) on the circle) in a linearized or mean-field regime.

Source: G. Bruno, F. Pasqualotto and A. Agazzi, Emergence of meta-stable clustering in mean-field transformer models, arXiv:2410.23228 (2024); B. Geshkovski, C. Letrouit, Y. Polyanskiy and P. Rigollet, A mathematical perspective on Transformers, arXiv:2312.10794 (2023)

Where it stands (checked by us, Nov 2026): Open (partial mean-field results).

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T324 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T324 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T324 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Your job for this session: take the NEXT checkable step on this problem, building on that work.
1. Five minutes at most: check whether anything after the earlier report changes the picture. If the problem was
   solved elsewhere, write SOLVED_ELSEWHERE.md (reference, arXiv id, what exactly is proved) and REPORT.md, then stop.
2. First re-check the earlier result: re-derive its main claim or re-run its computation an independent way, and
   write in LOG.md whether it holds. If it does not hold, that finding is your result.
3. Then choose ONE piece that extends it: the next step its report names, a wider special case, a sharper constant,
   more cases computed, the missing lemma. Write the choice and why in LOG.md first, then do it. A proof goes in
   PROOF.md with every step written out; a computation is a script in this folder with the command and output in LOG.md.
4. Try to break your own result: re-derive every load-bearing number a second way; look for the case you miss.
5. Finish with REPORT.md: first line exactly one of  VERDICT: PROVED <what> | VERDICT: PARTIAL <what> | VERDICT: COMPUTED
   <what> | VERDICT: NO PROGRESS <why> | VERDICT: EARLIER RESULT WRONG <what> . Then what is new beyond the earlier
   report, the commands, what failed, what you are unsure of, and what the next worker should do.

Rules (the author's standing laws):
- Work only inside this folder. Read anything, but never edit files elsewhere, never use git, never push, post, email or
  create accounts. Nothing you write leaves this folder except when the coordinating agent copies it.
- Compute: every program you run stays under 1 GB of RAM, one thread (set OMP_NUM_THREADS=1), runs under `nice -n 15`,
  and finishes within 20 minutes per run. No GPU, no MLX, no torch. This Mac is shared; never fill it.
- Literature: use the web search tool. Cite only papers you actually opened, with the authors exactly as on the paper or
  its arXiv page. Never invent a reference, a number or a step.
- Save as you go: append to LOG.md after every step (what you did, the command, the output that matters). The account's
  weekly allowance runs out within hours and the session may stop at any moment; LOG.md is what survives.
- Write plainly, like a working mathematician: no hype, no talk about yourself or the process inside PROOF.md.



----- earlier REPORT.md -----
VERDICT: PARTIAL deterministic concentration and merging asymptotics for two groups of nonzero width

The earlier two-atom result holds. Its rational drift and uniform time identity were re-derived independently; angular/cosine quadratures agree to 6.704e-13 relative error, and the noisy kernel agrees with a separate boundary-value solve to 2.019e-8. The brief web update found no later resolution. Opened references and the limits of that check are in LITERATURE.md; publication priority is not established.

The new theorem closes the deterministic concentration gap named by the earlier report. Consider normalized identity-matrix attention on the circle, including self-attention, with two labelled groups of fixed positive masses p,q. Their initial arithmetic center gap is fixed x, and merging means first entrance of that center gap into a fixed delta, where 0<delta<x<pi. Suppose both initial group diameters are at most w_beta<=1/(4 sqrt(beta)). For sufficiently large beta:

- Each group diameter is at most w_beta exp(-t/2) until the merging threshold.
- The merging time satisfies log(tau_beta)/beta -> 1-cos(x).
- If beta^2 w_beta^3 -> 0, then tau_beta ~ exp(beta(1-cos(x)))/[(p/q+q/p) beta sin(x)^2]. This includes initial diameters O(1/beta).

The estimates are uniform in the number of tokens and their individual positive weights. The proof also covers compactly supported mean-field groups. PROOF.md supplies all steps, including the attention-velocity derivative, cancellation of internal mean motion, and an explicit scalar hitting-time sandwich after time 4 beta. The accumulated initial center displacement is O(beta w_beta^3) plus an exponentially small term; controlling it to o(1/beta) is what preserves the prefactor.

Verification command, run from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py
```

The final run exited 0 in 3.817 seconds, peak RSS 16.28 MiB, inherited effective nice 20. It uses one thread and only the Python standard library. The launcher prints a setpriority warning because the inherited priority is already lower than requested. The script checks derivative and symmetrization identities, two time-step resolutions of a six-token system with unequal weights, and finite-time contraction cases satisfying the explicit sufficient condition. At beta=18 the full-token/scalar time ratio is 0.999994235. Numerical values are consistency checks, not proof certificates; full output and commands are in LOG.md and data in verification.json.

What failed: an initial numerical assertion extrapolated the contraction bound to beta=6, where the proof's sufficient condition fails. The measured width excess was about .00551. The final script retains that out-of-regime datum and checks contraction separately at beta=500,1000,2000. An isolated skew-group experiment also shows why small initial width alone does not justify transferring the prefactor without controlling center displacement. No counterexample within the theorem's asymptotic hypotheses was found.

Limits and uncertainties: this does not prove a generic cluster count, formation of the two groups, successive mergers, a noisy concentration theorem, or general attention matrices. Group masses are fixed, unlike the previous report's singular atom-mass regime. The stopping event is a center-gap threshold, not exact collision. The prefactor width condition is sufficient and has not been shown necessary. The numerical checks do not simulate exponentially long waiting at large beta; the analytic sandwich supplies that conclusion.

Next worker: prove a stopped concentration estimate for independently noisy tokens in these two narrow groups. For equal token weights, derive the exact group-mean martingale variance (which depends on group size) before comparing to a scalar noisy gap. Control the internal drift residual and the probability of width excursions over the relevant merging interval; replacing each group by the earlier independently noisy atom is not justified without these estimates.

Task: T324, “take the NEXT checkable step on this problem, building on that work.” First recorded session clock: 15 November 2026, 06:31 +04 (Asia/Tbilisi); the prompt's own timestamp was not supplied.
