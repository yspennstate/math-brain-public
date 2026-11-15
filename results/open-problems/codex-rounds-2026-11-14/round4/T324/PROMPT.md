# Open problem T324: Metastable clustering times in mean-field transformer dynamics

Statement: In the self-attention particle system of T323 with large beta, tokens first form several clusters that persist for a time exponentially long in beta before merging. Bruno, Pasqualotto and Agazzi describe this metastable phase in the mean-field limit. Prove the number of metastable clusters and the exponential time scales of their merging (a Freidlin–Wentzell-type or slow-manifold description), for the deterministic dynamics and for the dynamics with small noise.

Caveat: Partial results describe the first stage (number of clusters ~ sqrt(beta) on the circle) in a linearized or mean-field regime.

Source: G. Bruno, F. Pasqualotto and A. Agazzi, Emergence of meta-stable clustering in mean-field transformer models, arXiv:2410.23228 (2024); B. Geshkovski, C. Letrouit, Y. Polyanskiy and P. Rigollet, A mathematical perspective on Transformers, arXiv:2312.10794 (2023)

Where it stands (checked by us, Nov 2026): Open (partial mean-field results).

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T324 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T324 (read it,
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
VERDICT: PARTIAL unequal-mass two-atom merging laws, uniform deterministic crossover and joint small-noise exponent

The earlier equal-mass result holds. It was re-derived in cosine coordinates, and its noisy hitting-time formula was independently checked by direct kernel quadrature and a boundary-value solve. The short web update found no later resolution of T324; opened references and limitations are in LITERATURE.md. Publication priority for the special case below is not established.

The new result treats two atoms on the circle with masses p_beta and q_beta=1-p_beta, identity matrices, and normalized attention including self-attention. Fix 0<delta<x<pi. Let rho_beta=min(p_beta/q_beta,q_beta/p_beta), and suppose -log(rho_beta)/beta -> kappa, finite and nonnegative.

- Deterministic merging exponent: log(T_beta)/beta -> (1-cos(x)-kappa)_+.
- Give each atom independent angular noise sqrt(2 nu_beta)dW. If -log(nu_beta)/beta -> r, finite and nonnegative, then log(E[tau_delta])/beta -> min{(1-cos(x)-kappa)_+,r}.
- Set C_beta=p_beta/q_beta+q_beta/p_beta. Whenever exp(beta(1-cos(x)))/(C_beta beta) -> infinity, the sharper deterministic asymptotic is T_beta ~ exp(beta(1-cos(x)))/(C_beta beta sin(x)^2). This includes all fixed positive masses and all kappa<1-cos(x).

PROOF.md also gives a uniform finite-parameter estimate. Write B=log(tan(x/2)/tan(delta/2)) and J_beta=integral_delta^x exp(beta(1-cos(s)))/sin(s) ds. Then

    0 <= J_beta/C_beta + (1-2/C_beta^2)B - T_beta
       <= B/(C_beta exp(beta(1-cos(delta)))).

In particular, at the finer critical mass scale -log(rho_beta)=beta(1-cos(x))-log(beta)+b+o(1),

    T_beta -> B + exp(-b)/sin(x)^2.

This extends the previous report's suggested unequal-mass step and identifies where mass imbalance removes the exponential delay. The proof of the noisy law retains the outward-excursion estimate, which is needed for a mean entrance time.

Verification command, from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py
```

Final run: exit 0, 3.093 seconds, peak RSS 17.70 MiB, effective nice 20. The launcher warns that setting priority is not permitted, but the inherited priority is already lower than requested. Only the Python standard library and one thread are used. Angular and cosine deterministic quadratures agree within 3.152e-12 relative error. The noisy direct integral agrees with the independent BVP within 5.056e-8; a third cell-transfer calculation agrees within 8.920e-9. The maximum refined-mesh discrepancy in the exponential-scaling table is 2.047e-5. Full output is in LOG.md; parameter values and results are in verification.json. These are floating-point checks, not numerical certificates; the theorem has an analytic proof.

What failed: the address-space hard-limit call is unsupported in this environment; the first quadrature tolerance was insufficient for a small scaled integral; a uniform inner mesh missed a sharp kernel layer; and an overly strict adaptive tolerance reached roundoff. LOG.md records each failure and correction. No mathematical counterexample was found. The audit did identify an invalid extrapolation to avoid: applying the deterministic prefactor outside its divergence condition can predict a time tending to zero. At kappa=1-cos(x), corrections of order sqrt(beta) can instead produce either a diverging subexponential time or the finite limit B.

Limits: this does not prove a generic number of clusters, successive mergers of many clusters, a transition-time distribution, or stability of groups with nonzero width. The stochastic theorem adds noise directly to the two weighted atoms. It cannot be transferred to groups of independently noisy tokens without a concentration argument. The fixed-gap and non-antipodal assumptions remain essential.

Next worker: establish a concentration estimate for two finite-width groups up to the first merging threshold, initially for deterministic dynamics. For independent token noise, derive and justify the group-center diffusivity as well as the width estimate before using the scalar formula; the equal atom diffusivity assumed here is not automatic.

Task: T324, “take the NEXT checkable step on this problem, building on that work.” First recorded session clock: 15 November 2026, 03:47 +04 (Asia/Tbilisi); the prompt's own timestamp was not supplied.
