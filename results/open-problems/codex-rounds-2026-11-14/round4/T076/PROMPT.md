# Open problem T076: Random band matrices in dimensions two and three

Statement: For random band matrices indexed by the box {1, …, L}^d, with independent centred entries (up to symmetry) in a fixed symmetry class, H_xy = 0 unless |x − y| ≤ W, and a regular variance profile, bulk eigenvectors are delocalized with Wigner–Dyson local statistics when W ≫ √(log L) in d = 2, and for every W ≥ W_0 with W_0 fixed in d = 3; in d = 2 the localization length is of order exp(cW²).

Source: Y. V. Fyodorov and A. D. Mirlin, Scaling properties of localization in random band matrices: a σ-model approach, Phys. Rev. Lett. 67 (1991); P. Bourgade, Random band matrices, Proc. ICM 2018

Where it stands (checked by us, Nov 2026): d = 1 is settled (T035, retired). Delocalization when W is a power of L: d ≥ 7 (Xu–Yang–Yau–Yin, arXiv:2207.14533: quantum unique ergodicity for complex Gaussian entries when W ≥ L^ε, after Yang–Yau–Yin, arXiv:2104.12048, in d ≥ 8), d = 2 with W ≥ N^c (Dubova–Yang–Yau–Yin, arXiv:2503.07606) and d ≥ 3 with W ≥ N^c (Dubova–Yang–Yau–Yin, arXiv:2507.20274). In d = 2, Lai–Yang (arXiv:2609.24426) reach W ≥ (log N)^7 with localization length at least exp(W^{1/7}). The predicted exp(cW²) scale in d = 2 and bounded W in d = 3 are open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T076 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T076 (read it,
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
VERDICT: PARTIAL exact deterministic return-kernel asymptotic for the two-dimensional block profile

The earlier report's Lai–Yang theorem and scale conversion hold. A literature
search lasting under five minutes found no later solution to T076. The
latest inspected revision remains Xujie Lai and Fan Yang,
*Localization Lengths for Two-Dimensional Random Band Matrices: Exponential
Lower Bounds*, [arXiv:2609.24426v4](https://arxiv.org/abs/2609.24426v4),
8 November 2026. Its Gaussian periodic block model remains a restriction.

New beyond the earlier report: [PROOF.md](PROOF.md) proves, for its block
variance matrix \(B=(I+\mathrm{adjacency})/5\) on an \(M\)-by-\(M\) torus,
\[
[(I-(1-\mu)B)^{-1}]_{00}-\frac1{\mu M^2}
=\frac5{4\pi}\log\frac1{\mu+M^{-2}}+O(1),
\]
uniformly for \(M\geq3\), \(0<\mu\leq1/2\), with an absolute error
constant. After the physical normalization \(W^{-2}\), the centered
diagonal for \(\mu\leq M^{-2}\) is
\[
\frac5{2\pi}\frac{\log M}{W^2}+O(W^{-2}).
\]
The proof includes the precise site-level identity and a second derivation
of the coefficient from \(n p_n(0)\to5/(4\pi)\) for the associated walk.
It checks the smallest allowed torus explicitly, handles both parities,
and shows why negative Fourier eigenvalues cause no extra singularity.

This is a deterministic sublemma, not a new bandwidth threshold for random
matrices. The logarithmic order is standard; Lai–Yang already give propagator
upper bounds in Lemma 2.7. No claim of novelty in random-walk theory is made.
No localization-length, eigenvector, universality, or dimension-three
theorem has been proved here.

The failed shortcut is to use smallness of this centered kernel as smallness
of the full kernel. The latter also contains exactly \(1/(\mu N)\),
\(N=W^2M^2\). With \(M=\lfloor e^W\rfloor\), \(\mu=N^{-1}\), the
centered part tends to zero while the full diagonal tends to one. Moreover,
even the centered estimate supplies no control of the stochastic resolvent
error. That missing step prevents any conclusion for T076.

Commands and sources are recorded in [LOG.md](LOG.md). Verification used
`rg --files`, `cat`, the web search tool, and independent analytic
derivations. No numerical experiment ran. The priority probe
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 /usr/bin/true`
reported `nice: setpriority: Operation not permitted`; no simulation was
launched at default priority. No git commands, external writes, or subagents.

Next worker: take one quadratic drift term in the alternating two-loop
equation, Lai–Yang (2.33)–(2.34), and test whether its time-integrated estimate
can use \((\log M)/W^2\) without an additional logarithmic loss. Separate
the constant mode before estimating it. The present diagonal lemma alone
does not establish such an estimate.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, approximately 01:12 Asia/Tbilisi.
