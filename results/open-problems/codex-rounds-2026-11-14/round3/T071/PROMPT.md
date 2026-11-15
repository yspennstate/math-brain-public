# Open problem T071: Branching Brownian motion with selection: the Bolthausen–Sznitman genealogy of N-BBM

Statement: For N-BBM (branching Brownian motion in which, at each branching, the leftmost particle is removed to keep N particles), the genealogy on time scale (log N)³ converges to the Bolthausen–Sznitman coalescent. The Brunet–Derrida speed v_N = v_∞ − c/(log N)² + o((log N)^{−2}) is proved; see where it stands.

Source: É. Brunet and B. Derrida, Shift in the velocity of a front due to a cutoff, Phys. Rev. E 56 (1997); É. Brunet, B. Derrida, A. H. Mueller and S. Munier, Noisy traveling waves: effect of selection on genealogies, Europhys. Lett. 76 (2006)

Where it stands (checked by us, Nov 2026): Speed: proved for N-BBM (Maillard, arXiv:1304.0562, published 2016) and recovered in a time-inhomogeneous joint limit, log N ≪ T^{1/3} (Legrand–Maillard, arXiv:2402.04917 v4, Theorem 1.1(i) and Corollary 2.1); also for N-branching random walk (Bérard–Gouéré 2010) and noisy FKPP (Mueller–Mytnik–Quastel 2011). Genealogy: proved for BBM with absorption at a moving barrier (Berestycki–Berestycki–Schweinsberg 2013); for N-BBM itself it is open (the w672 audit read Legrand–Maillard in full; no genealogy theorem there).

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T071 (read it,
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
VERDICT: PARTIAL exact three-lineage reduction and J1 obstruction

The fixed-size N-BBM genealogy conjecture remains unproved here. The bounded
opening literature search found no solution or later N-BBM genealogy theorem.

## What was proved

[PROOF.md](PROOF.md) proves an exact criterion for the three-label part of the
conjecture. Let S_N be the first sampled merger time, and H_N the interval
between the two sampled mergers, on a proposed rescaled clock. For uniformly
labelled samples with increasing available history, finite-dimensional
convergence to the normalized three-label Bolthausen–Sznitman coalescent is
equivalent to

    E exp(-s S_N-r H_N) -> (r+4)/[2(s+2)(r+1)],  s,r>=0.

The limiting first time is Exp(2), independently of a holding time with law
(1/4) delta_0+(3/4) Exp(1). In particular the conjecture requires

    lim_(h down to 0) lim_N P(S_N<=T,H_N<=h)
      = (1-exp(-2T))/4.

The proof also gives an explicit finite-grid lower bound for short intervals
between mergers. No Markov assumption on the finite-N ancestral process is
needed.

Binary finite-N genealogies cannot converge to this limit in the usual J1
topology on the finite partition space. A bounded continuous path test has
expectation difference (1-exp(-2T))/4 at every N, equal to 3/16 at T=log 2.
This concerns a stronger interpretation of convergence; it does not disprove
the intended finite-dimensional conjecture.

## Checks

[AUDIT.md](AUDIT.md) independently derives the constants using forward
equations and discounted backward equations. The joint transform also agrees
with the separately derived absorption-time density. An explicit exchangeable
binary-process counterexample shows why the two separate time marginals are
insufficient: their dependence must be checked. The audit covers finite
histories, sample labels, Brownian collisions, suppressed branches, and
vanishing intermediate holding times.

This is an elementary auxiliary reduction, not a claim of a new theorem in
the literature. No N-BBM asymptotic estimate was obtained.

## Literature checked

- [Pascal Maillard, arXiv:1304.0562v4](https://arxiv.org/html/1304.0562v4):
  Section 1.4 explicitly explains why its spatial comparison does not transfer
  genealogy.
- [Alexandre Legrand and Pascal Maillard, arXiv:2402.04917v4](https://arxiv.org/abs/2402.04917v4):
  the current abstract describes displacement results, consistent with the
  supplied audit.
- [Julien Berestycki and Oliver Tough, arXiv:2407.05792](https://arxiv.org/abs/2407.05792):
  a stationary empirical-measure selection principle.
- [Jacob Mercer, arXiv:2605.04860](https://arxiv.org/html/2605.04860v1):
  rank-based selection, hydrodynamics and velocity results.
- [Emmanuel Schertzer and Alejandro H. Wences, arXiv:2301.07762v2](https://arxiv.org/html/2301.07762v2):
  a genealogy theorem for a different model with discrete generations and
  noisy selection.
- [Julien Berestycki, Nathanaël Berestycki and Jason Schweinsberg,
  arXiv:1001.2337v3](https://arxiv.org/html/1001.2337v3):
  Theorem 3 for the absorption model explicitly uses finite-dimensional
  convergence. Section 1.3 supplies the coalescent definition used here.

Only opened sources are listed. The negative search result is not an
exhaustive certification of the literature.

## Commands and limits

The proof and audit are analytic; no simulation or computational data are
claimed. Web queries and file operations are recorded in [LOG.md](LOG.md).
The proof was read back using

    env OMP_NUM_THREADS=1 nice -n 15 cat PROOF.md

The sandbox returned `nice: setpriority: Operation not permitted`; no numerical
workload was launched. All created files stayed in this task folder.

The missing step is the displayed joint-transform limit for actual N-BBM.
The physical time constant, an admissible observation regime, a quantitative
shrinking-window rate, and samples larger than three remain unresolved.

The next worker should target the joint law of the first sampled merger time
and the interval to the second, retaining their dependence. Formula (7) in
PROOF.md gives a finite-grid necessary check before attempting the full
transform. A three-label result alone will not establish the full conjecture.

Task: “push this problem forward by one checkable piece” — 14 November 2026,
approximately 20:50 Asia/Tbilisi.
