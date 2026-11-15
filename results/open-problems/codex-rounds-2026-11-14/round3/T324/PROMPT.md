# Open problem T324: Metastable clustering times in mean-field transformer dynamics

Statement: In the self-attention particle system of T323 with large beta, tokens first form several clusters that persist for a time exponentially long in beta before merging. Bruno, Pasqualotto and Agazzi describe this metastable phase in the mean-field limit. Prove the number of metastable clusters and the exponential time scales of their merging (a Freidlin–Wentzell-type or slow-manifold description), for the deterministic dynamics and for the dynamics with small noise.

Caveat: Partial results describe the first stage (number of clusters ~ sqrt(beta) on the circle) in a linearized or mean-field regime.

Source: G. Bruno, F. Pasqualotto and A. Agazzi, Emergence of meta-stable clustering in mean-field transformer models, arXiv:2410.23228 (2024); B. Geshkovski, C. Letrouit, Y. Polyanskiy and P. Rigollet, A mathematical perspective on Transformers, arXiv:2312.10794 (2023)

Where it stands (checked by us, Nov 2026): Open (partial mean-field results).

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T324 (read it,
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
VERDICT: PARTIAL two-token deterministic merging asymptotic and joint small-noise mean merging exponent

For two equal-weight tokens on the circle with identity matrices and normalized attention including self-attention, PROOF.md proves the following. Start at fixed angular gap x and stop at first entrance into gap delta, with 0<delta<x<pi. Write a=1-cos(x).

- Deterministic time: T_beta ~ exp(beta a)/(2 beta sin(x)^2).
- Give each token independent angular noise sqrt(2 nu_beta) dW. If -log(nu_beta)/beta -> r in [0,infinity), then log(E[tau_delta])/beta -> min{a,r}.
- An exact double-integral formula and explicit finite-parameter bounds underlie the noisy result. The upper bound controls excursions toward larger, more weakly attracting gaps.

Thus exponentially small independent noise can change the deterministic exponential merging scale even in the smallest normalized-attention system. Polynomially small diffusivity gives zero exponential rate on the beta scale. This is a theorem about a mean first entrance time; it does not claim a transition-time distribution or permanent merging.

The short literature check found relevant earlier advances, documented with links and theorem limitations in LITERATURE.md. No resolution after the supplied November 2026 status was found. The 2025 multiscale paper's closest-pair limit stops before collapse; the October 2026 noisy result concerns conditional applications to unnormalized attention. No SOLVED_ELSEWHERE.md was created. Priority for this special case has not been established.

Verification command, run from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py
```

The successful run exited 0 in under one second. The launcher warns that changing priority is not permitted; a separate check confirmed inherited effective nice=20. Computation was single-threaded and used only the standard library with small arrays.

Two deterministic coordinate integrals agree to relative error 1.071e-11. An integrating-factor calculation and an independent finite-difference boundary-value solve agree to relative error 3.143e-07. Numerical results are in verification.json and crossover.csv; exact output is in LOG.md. These floating-point checks support the algebra but are not the proof.

What failed: the first numerical implementation integrated a sharp derivative layer with the trapezoidal rule and failed a mesh-convergence assertion at beta=160. Exact integration within each constant-drift cell fixed that issue without loosening tolerance. An argument based only on local attraction would not control rare outward excursions, so the proof bounds that contribution explicitly. Connecting the general model's phases was not attempted.

Limits and doubts: no generic cluster count, many-token noisy reduction, unequal-mass theorem, beta-dependent gap theorem, or exactly antipodal theorem is proved. Independent noises break coincidence within a larger cluster, so the noisy result cannot simply be lifted to two multi-token groups. Deterministic exact collision takes infinite time. The literature search was brief and does not establish novelty.

Next worker: extend the scalar method to unequal two-atom masses, then determine whether clusters of small but nonzero width stay concentrated over the relevant waiting scale under independent noise. That concentration estimate is needed before treating a cluster center as a single noisy token. Retain separate attention and noise parameters.

Task: T324, “push this problem forward by one checkable piece.” Date: 14 November 2026; first recorded session clock 22:13 +04 (Asia/Tbilisi). The prompt's own timestamp was not supplied.
