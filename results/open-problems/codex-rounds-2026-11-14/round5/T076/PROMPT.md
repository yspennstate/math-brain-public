# Open problem T076: Random band matrices in dimensions two and three

Statement: For random band matrices indexed by the box {1, …, L}^d, with independent centred entries (up to symmetry) in a fixed symmetry class, H_xy = 0 unless |x − y| ≤ W, and a regular variance profile, bulk eigenvectors are delocalized with Wigner–Dyson local statistics when W ≫ √(log L) in d = 2, and for every W ≥ W_0 with W_0 fixed in d = 3; in d = 2 the localization length is of order exp(cW²).

Source: Y. V. Fyodorov and A. D. Mirlin, Scaling properties of localization in random band matrices: a σ-model approach, Phys. Rev. Lett. 67 (1991); P. Bourgade, Random band matrices, Proc. ICM 2018

Where it stands (checked by us, Nov 2026): d = 1 is settled (T035, retired). Delocalization when W is a power of L: d ≥ 7 (Xu–Yang–Yau–Yin, arXiv:2207.14533: quantum unique ergodicity for complex Gaussian entries when W ≥ L^ε, after Yang–Yau–Yin, arXiv:2104.12048, in d ≥ 8), d = 2 with W ≥ N^c (Dubova–Yang–Yau–Yin, arXiv:2503.07606) and d ≥ 3 with W ≥ N^c (Dubova–Yang–Yau–Yin, arXiv:2507.20274). In d = 2, Lai–Yang (arXiv:2609.24426) reach W ≥ (log N)^7 with localization length at least exp(W^{1/7}). The predicted exp(cW²) scale in d = 2 and bounded W in d = 3 are open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T076 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T076 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T076 (read it,
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
VERDICT: PARTIAL quadratic drift bound without an extra logarithm under a commuting low-mode envelope

The round-3 return-kernel asymptotic holds. An independent Fourier-cell
integral comparison and a covariance check recover its coefficient
5/(4*pi). A literature check under five minutes found no later solution
to T076; Xujie Lai and Fan Yang,
*Localization Lengths for Two-Dimensional Random Band Matrices: Exponential
Lower Bounds*, [arXiv:2609.24426v4](https://arxiv.org/abs/2609.24426v4),
remains the relevant inspected two-dimensional advance.

New beyond round 3: [PROOF.md](PROOF.md) treats the quadratic drift
\(W^2DBD\) with the exact two-coordinate Duhamel propagator from
Lai–Yang (2.33)–(2.39). Write \(G_u=(I-uB)^{-1}\), \(Q=I-P\),
\(a_k=1-b_k\). For real symmetric translation-invariant errors satisfying
\[
d_u(0)=0,\qquad
|d_u(k)|\leq\delta uW^{-2}a_k(1-ub_k)^{-2},
\]
the integrated term obeys
\[
-\delta^2tW^{-2}G_tQ\preceq\mathcal J_t[D]
\preceq\delta^2tW^{-2}G_tQ.
\]
Its entries are bounded by \(\delta^2tW^{-2}(G_tQ)_{00}\), retaining
the return kernel's single logarithm without another time logarithm.
The logarithmic order is sharp within this deterministic class.

The weaker envelope \(D(u)=\delta uW^{-2}G_uQ\) fails: its exact
quadratic integral is \(\delta^2t^3(3W^2)^{-1}BG_t^2Q\).
For \(0<1-t\leq M^{-4}\), its diagonal is
\[
\frac{\delta^2}{W^2}\left[c_*M^2+O(\log M)\right],\qquad
c_*=\frac{25}{48\pi^4}
\sum_{k\in\mathbb Z^2\setminus\{0\}}|k|^{-4}>0.
\]
Thus uniformly small centered error entries need not give a small
integrated quadratic drift. The coefficient is checked through a
real-space square-norm identity and Parseval, and the exact M=3 value
is independently verified as \(35\delta^2/(243W^2)\) at zero mass.

What failed and what remains uncertain: the weak family need not make
the approximate two-loop observable entrywise nonnegative. It is an
obstruction only under the explicitly stated envelope assumptions,
not a counterexample to the random-matrix dynamics. The sufficient
low-mode envelope has not been proved for a random resolvent error;
translation invariance also excludes its Fourier-mode couplings.
No new eigenvector, localization-length or local-statistics theorem is
claimed, and no novelty in deterministic Fourier analysis is asserted.

Commands and opened sources are in [LOG.md](LOG.md). Verification was
analytic; document inspection used `rg --files` and
`OMP_NUM_THREADS=1 nice -n 15 /bin/cat ...`. The sandbox emitted
`nice: setpriority: Operation not permitted`; no numerical experiment
was launched under unverified priority. All writes stayed here.
No git, external registration, external messages or subagents.

Next worker: examine the Fourier matrix elements of the actual centered
two-loop error. Seek a bound with the factor
\(a_k/(1-ub_k)\) before the diffusion time, or an averaged replacement
that controls noncommuting Fourier couplings. Establishing such a
bound, rather than improving the diagonal return estimate, is the
missing step needed to use this quadratic-drift lemma.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, approximately 04:39 Asia/Tbilisi.
