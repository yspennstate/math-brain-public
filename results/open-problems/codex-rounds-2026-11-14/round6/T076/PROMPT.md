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

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T076 (read it, never
edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

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
VERDICT: PARTIAL sharp two-logarithm bound for noncommuting quadratic errors and a bounded-variation criterion

The round-4 commuting quadratic-drift bound holds. Its exact time factor
and its M=3 check were independently rederived. A literature search under
five minutes found no later solution to T076. The latest inspected
two-dimensional paper remains Xujie Lai and Fan Yang,
*Localization Lengths for Two-Dimensional Random Band Matrices:
Exponential Lower Bounds*,
[arXiv:2609.24426v4](https://arxiv.org/abs/2609.24426v4).
Its improvement over the original brief was already recorded in round 1.

New beyond round 4: [PROOF.md](PROOF.md) removes translation invariance
from the deterministic analysis of the same quadratic term. Write
\(A=I-B\), \(G_u=(I-uB)^{-1}\), \(Q=I-P\), and parametrize the
pointwise envelope by real symmetric contractions \(E(u)=QE(u)Q\):
\[
D(u)=\delta uW^{-2}A^{1/2}G_uE(u)G_uA^{1/2}.
\]
This is equivalent, on \(Q\), to the previous strong Loewner envelope
\(-\delta uW^{-2}AG_u^2Q\preceq D(u)\preceq\delta uW^{-2}AG_u^2Q\).

For the exact two-coordinate Duhamel integral \(\mathcal J_t[D]\),
if \(E\) has operator-norm total variation \(V\) on \([0,t]\), then
\[
-\delta^2tW^{-2}(1+2V)G_tQ
\preceq\mathcal J_t[D]
\preceq\delta^2tW^{-2}(1+2V)G_tQ.
\]
Thus bounded variation independent of the torus size preserves the
single return-kernel logarithm. A time-independent contraction needs
no commutation assumption. Integration by parts and a separate
telescoping argument give the same factor \(1+2V\).

The pointwise envelope alone has a sharp worst-case diagonal order
\(\delta^2(\log M)^2/W^2\). The proof gives a general upper bound
and an explicit continuous family attaining it: for
\(M=8^{R+2}\), \(t=1-M^{-4}\),
\[
\mathcal J_t[D]_{00}
\geq\frac{\delta^2\log8}{720000W^2}R(R+1).
\]
The construction swaps successive squares of low cosine modes with
modes at the currently active diffusion scale. Its total variation is
\(2R\). With \(W=\lceil R^{3/4}\rceil\), all error entries tend
uniformly to zero, but this quadratic diagonal tends to infinity.
This obstruction satisfies the stronger envelope from round 4;
that round's obstruction used a weaker one.

What failed: extending the single-logarithm estimate using only the
noncommuting pointwise Loewner envelope. A preliminary single-output-mode
example broke only an operator comparison, so it was replaced by the
simultaneous-mode construction above. No numerical experiment ran:
the sandbox refuses to set the requested nice priority. Verification
was analytic, including independent matrix factorizations, a direct
two-by-two swap check, and two harmonic-sum lower bounds. Commands,
constants, opened sources and failed steps are in [LOG.md](LOG.md).

Limits: these are conditional deterministic statements. The constructed
errors are not shown to arise from random resolvents or to preserve the
full observable's entrywise positivity and Ward identities. The normalized
random error may have infinite total variation. No new eigenvector,
localization-length, or local-statistics theorem is proved; T076 remains
open. No claim of novelty in the underlying operator inequalities is made.

Next worker: test whether the actual two-loop positivity and Ward
constraints exclude the simultaneous mode transfers in the example.
A concrete sufficient target, after establishing a suitable normalized
envelope, is the square-function estimate
\[
\int_0^t u^2E(u)A|B|G_u^2E(u)\,du\preceq Ct^2Q
\]
with size-independent \(C\). It would replace the bounded-variation
assumption and recover a single logarithm for this quadratic term.
The general envelope proved here gives only \(C(1+\log M)Q\).

All writes stayed in this folder. No git, external messages, registrations,
numerical jobs or subagents.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, approximately 08:02 Asia/Tbilisi.
