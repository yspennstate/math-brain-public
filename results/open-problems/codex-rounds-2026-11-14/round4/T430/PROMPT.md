# Open problem T430: Asymptotic independence in the supermarket model with general service times

Statement: Consider N FIFO unit-rate servers, Poisson arrivals of rate lambda N with 0<lambda<1, iid service requirements of a fixed law G of mean one, and routing to a shortest queue among d>=2 uniformly sampled servers. In the stationary law, does the joint state of every fixed k servers converge, as N tends to infinity, to pi_G^{tensor k} for a single-server law pi_G? The state includes the queue length and service age or residual requirement.

Caveat: The proposed statement fixes FIFO and the full queue state; it does not conflate queue lengths with Markov states.

Source: Bramson-Lu-Prabhakar, general-service supermarket ansatz; Decay of tails at equilibrium for FIFO join the shortest queue networks (arXiv:1106.4582).

Where it stands (checked by us, Nov 2026): 1106.4582 states the ansatz and proves tail results conditional on it; it records decreasing-hazard-rate cases where the ansatz is known. General-service transient propagation of chaos does not by itself justify exchange with the stationary limit.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T430 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T430 (read it,
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
VERDICT: PARTIAL explicit counterexample to the arrival-rate monotonicity lemma supporting a claimed stationary result

The earlier result holds. An independent second-moment expansion gives Var(M(t))=Var(M(t)|B=0)/2+p_N(t)^2/4 for its fair empty/busy initial mixture and t<1. This recovers its exponential lower bound. The separate covariance bound 1/8 and the stationary variance decomposition also check out; see LOG.md.

The new result audits the paper singled out by the earlier report. For uniform sampling without replacement, append a queue shorter than the tagged queue. Its routing rate changes exactly by

\[
 a_{N+1}=\frac{N+1-d}{N}a_N.
\]

Every positive rate therefore strictly decreases. The single infinite configuration (1,2,0,1,2,0,...) has such a decrease at every N=3m+2. All the count assumptions in the cited argument hold for sufficiently large m. The empirical initial measures converge to equal masses at zero, one and two. For d=2, a_{3m+2}=lambda*(3m+2)/(3m+1) and a_{3m+3}=lambda; in particular a_5=5lambda/4 and a_6=lambda.

This refutes Lemma 3.3 of Maria Clara Fittipaldi, Matthieu Jonckheere, Sergio I. Lopez, *Convergence properties of many parallel servers under power-of-D load balancing*, [arXiv:1809.05373](https://arxiv.org/pdf/1809.05373), in the retrieved PDF dated 13 November 2021. Its Appendix A.2 omits the case of an appended queue shorter than the tag. The lemma is invoked in the tagged-process convergence argument that precedes the stationary claim. This is a definite failure of a supporting lemma, beyond the earlier report's conditional-variance concern. It does not establish that Proposition 4.1 itself is false.

PROOF.md contains the complete routing calculation, an independent Poisson-thinning derivation, the fixed periodic witness, exact pair-count checks, and the witness's rate limit. That limit exists despite infinitely many decreases; no claim of nonconvergence is made. The routing states can be completed to full FIFO states with G=delta_1. This is not a stationary counterexample.

The literature check finished within five minutes. No verified later solution was found. Opened papers included the audited paper and Pooja Agarwal and Kavita Ramanan, *Invariant states of hydrodynamic limits of randomized load balancing networks*, [arXiv:2008.08510](https://arxiv.org/pdf/2008.08510), Section 4.2, as well as Reza Aghajani and Kavita Ramanan, *The hydrodynamic limit of a randomized load balancing network*, [arXiv:1707.02005](https://arxiv.org/pdf/1707.02005). The retrieved versions do not supply the missing general stationary-limit argument. The search was brief and is not an exhaustive literature certification. No SOLVED_ELSEWHERE.md was created.

Validation used exact symbolic calculations, with every rate and decrease checked in two ways. No numerical script, simulation, fitted constant, or computational evidence is claimed. Shell commands read the earlier files and startup/compute state, and checked local files with `OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c 'wc -l LOG.md PROOF.md; rg -n "Proposition|tag\\{|stationary|count|converg" PROOF.md'`. Web search/open/find were used for the papers. PDF screenshots failed with cache misses; extracted PDF text was read. File writes used apply_patch and stayed in this folder. The shell reported a priority-setting restriction, so no numerical program was run.

What failed: the first candidate with a unique queue at the tagged length did not satisfy the paper's count assumptions and was discarded before writing the proof. The periodic replacement satisfies them. No estimate of stationary conditional-mean forgetting was obtained. The original arbitrary-G full-state product-limit assertion remains unresolved here. Whether the proposed stationary theorem can be recovered by another proof is not decided.

Next worker: replace the false monotonicity step by an estimate based on convergence of empirical full-state measures, while retaining their possibly random stationary limit. Then address whether the limiting stationary empirical measure must be deterministic. Convergence to a unique invariant point alone is insufficient without ruling out other invariant laws of the limiting evolution. The earlier report's conditional-mean concentration criterion remains a precise target; the present audit does not prove it.

Task: “Open problem T430: Asymptotic independence in the supermarket model with general service times”; received 15 November 2026, approximately 03:54 Asia/Tbilisi (14 November 23:54 UTC).
