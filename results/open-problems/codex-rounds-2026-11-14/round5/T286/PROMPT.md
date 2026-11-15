# Open problem T286: Bayes-optimal learning of extensive-width networks with quadratically many samples

Statement: Learn a two-layer teacher network with width m proportional to the input dimension d from n = alpha·d² samples. Maillard, Troiani, Martin, Krzakala and Zdeborová obtain the Bayes-optimal error for quadratic activation by mapping to extensive-rank matrix denoising, and conjecture a formula for general activations. Prove the Bayes-optimal error for a general activation (e.g. ReLU or tanh) in this regime, and decide whether gradient descent achieves it.

Caveat: For quadratic activation the formula rests on a matrix-denoising reduction (rigorous status to verify); the general case is conjectural.

Source: A. Maillard, E. Troiani, S. Martin, F. Krzakala and L. Zdeborová, Bayes-optimal learning of an extensive-width neural network from quadratically many samples, arXiv:2408.03733 (2024)

Where it stands (checked by us, Nov 2026): Open beyond quadratic activation as far as the writer knows.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T286 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T286 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T286 (read it,
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
VERDICT: PROVED quantitative cubic Gaussian replacement for finitely many cavity replicas

The round-3 self-covariance constants hold. This session adds an explicit Gaussian integration-by-parts and smooth replacement bound for the normalized cubic Hermite activation, Gaussian weights and Gaussian inputs. The general Bayes-error formula and the gradient-descent question remain open.

The new lemma permits any joint coupling of finitely many networks as long as each marginal is the Gaussian weight prior and the tested input is independent of their joint law. In particular, it applies to a teacher and replicas drawn from the matched posterior after removing one observation. It does not assume the replicas are independent after averaging the data.

For T=k^-1/2 sum_i(w_i/sqrt(d))^tensor3, the exact prior contraction moment is

```
delta = E[||T contraction_2 T||_F^2]
      = M6/k + ((k-1)/k)*M3^2*(1/d + 3/(d*(d+2)) + 15/(d*(d+2)*(d+4))),
M_p = product_{j=0}^{p-1}(1+2*j/d).
```

A deterministic mixed-contraction inequality makes this useful for dependent replicas. The resulting averaged Stein discrepancy epsilon is O(d^-1/2), with the explicit bound in [PROOF.md](PROOF.md), equation (1). If k/d tends to gamma>0, sqrt(d)*epsilon tends to sqrt(14*(1+1/gamma)). This is the asymptotic constant of the proved upper bound; no optimality of that bound is claimed. Smooth replacement uses the true random covariance K, or the displayed Hermite covariance C with an additional O(d^-1) error for Gaussian row-norm fluctuations. The bounds cover singular covariance matrices.

For smooth tests with uniform derivative bounds, averaging the remainder over n samples costs no additional factor of n. Normalization by d^2 costs n/d^2, so the bound still vanishes when n/d^2 tends to alpha. These conclusions concern the cavity law at each omitted input.

Verification: [check_stein.py](check_stein.py) integrates the contraction moment directly over Gaussian weight coordinates, independently of the proof's row-parity enumeration. Six exact moment checks pass. Seven deterministic mixed-network checks verify the Wick expansion, integration by parts, and contraction inequalities, including identical, opposite, permuted and zero-row cases. Four further checks directly integrate the actual Stein residual over weights and inputs. All pass. The final run took 0.052 seconds, used 15,204,352 bytes peak RSS, and ran at inherited nice priority 20 with one thread. Complete output: [check_stein.out](check_stein.out).

Commands:

```
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T286/check_cubic.py > recheck_cubic.out 2>&1
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_stein.py > check_stein.out 2>&1
```

Failures and limits: macOS rejected a proposed 512 MB RLIMIT_DATA guard before any calculation; the unsupported guard was removed. The numerical workload is fixed and tiny, and retains a 120-second CPU cap. `nice -n 15` reports a denied relative adjustment because the inherited priority is already 20. No mathematical check failed. No proof of a likelihood-normalization estimate, full-posterior Gaussian replacement, distinct-replica concentration, Bayes error or optimizer optimality was obtained. No literature novelty is claimed for this use of Gaussian polynomial contractions.

The bounded literature check found no later rigorous general-activation solution. Jean Barbier, Francesco Camilli, Minh-Toan Nguyen, Mauro Pastore and Rudy Skerk, [arXiv:2510.24616v5](https://arxiv.org/html/2510.24616v5), still retain Gaussian replacement and concentration assumptions in Appendix B.6. The new result addresses a finite-dimensional cavity version of their replacement assumption, not their complete sum rule. Search details and the independent rederivation of the previous constants are in [LOG.md](LOG.md).

Next worker: express the likelihood-weighted term (158) through the posterior with sample mu removed. For a specified smooth output channel, first identify a class of cavity functionals whose derivatives have uniformly summable bounds when represented by replicas. Prove control of the random one-sample likelihood normalization and of the log-partition derivative, then apply the present Stein identity. A finite-replica central limit theorem alone does not bound that functional. Treat the separate replica concentration and hidden-unit permutation issue in (166) afterward.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, 06:30 Asia/Tbilisi.
