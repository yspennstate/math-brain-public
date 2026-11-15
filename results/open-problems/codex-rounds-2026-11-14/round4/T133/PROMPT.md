# Open problem T133: The arctic curve of the six-vertex model with domain-wall boundary conditions

Statement: For the six-vertex model with domain-wall boundary conditions on an n × n square, in the disordered regime −1 < Δ < 1, the boundary between the frozen and disordered regions converges after rescaling by n to the curve predicted by Colomo and Pronko, and recovered by the tangent method of Colomo and Sportiello; the analogous prediction holds in the antiferroelectric regime Δ < −1.

Caveat: The predictions are explicit algebraic or transcendental curves depending on the weights; at Δ = 0 (free fermions) the curve is an ellipse, the arctic circle of domino tilings for equal weights.

Source: F. Colomo and A. G. Pronko, The limit shape of large alternating sign matrices, SIAM J. Discrete Math. 24 (2010); F. Colomo and A. Sportiello, Arctic curves of the six-vertex model on generic domains: the tangent method, J. Stat. Phys. 164 (2016)

Where it stands (checked by us, Nov 2026): At Δ = 0 the arctic circle is known (Jockusch–Propp–Shor 1995). At the ice point Δ = 1/2, which includes uniformly random alternating sign matrices, Aggarwal (arXiv:1812.03847, 2020) proved the Colomo–Pronko arctic curve for domain-wall boundary conditions, and the predicted boundaries for more general three-bundle domains. Other values of Δ are open; fluctuations of the height function are T063.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T133 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T133 (read it,
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
VERDICT: PROVED invertibility and local critical-branch continuation of the disordered Fredholm formulas for all -1 < Delta < 1

This is an analytic lemma about the candidate formulas, not a proof of T133.
The earlier worker reported a theorem announcement and supplied no original
proof or computation. The new result, proved in [PROOF.md](PROOF.md), checks
one possible obstruction in the announcement's omitted interval
$1/2<\Delta<1$.

With $\gamma=\arccos\Delta$, the disordered integral operator satisfies

\[
\|K_B\|_{L^2\to L^2}\le |1-2\gamma/\pi|<1
\]

for every $B>0$. Its Fredholm determinant is positive, and the rank-one
determinant quotient is a linear resolvent integral. Thus these formulas
remain well defined throughout the omitted interval.

At every interior parameter of the proposed southwest boundary arc, its
envelope determinant is strictly positive. Consequently, for each
sufficiently small $B>0$ and fixed boundary parameter $\theta$, the two
critical equations determine a unique real pair $(x(B,\theta),y(B,\theta))$
that extends analytically to the envelope at $B=0$. An explicit quadratic
displacement is derived; its constants are checked by a second moment
argument and an exact free-fermion calculation. Where the stated curvature
quantity $C$ is nonzero, the critical point is a nondegenerate saddle.
This does not assert uniqueness of $(B,\theta)$ for a prescribed $(x,y)$.

The source definitions are from Alexey Bufetov,
[*Limit shape for domain-wall six-vertex model*, arXiv:2609.20576v1](https://arxiv.org/html/2609.20576v1).
The bounded literature check found no later version or complete proof.
The earlier report's description of the announcement survives direct
comparison with the abstract page, HTML and PDF. The new proof does not
assume its announced limit-shape theorems. No claim of literature priority
is made for these operator facts.

Reproduce the numerical audit with:

~~~sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_local.py
~~~

The script requires NumPy and mpmath. Detailed output is in
[verification.json](verification.json); commands and material outputs are
recorded in [LOG.md](LOG.md). All 19 numerical checks passed: five kernel
mass checks, three scalar-determinant versus resolvent comparisons, eight
local-branch checks, and three exact free-fermion checks. The latter agree
within $2.70\times10^{-10}$. Branch checks include unequal weights, both
kernel signs, and parameters near $\Delta=\pm1$. Final runtime was
0.61 seconds with peak RSS 33.8 MiB, one thread configured, and effective
nice 20.

What failed: the first numerical run emitted warnings from unused
meromorphic evaluations and BLAS-backed operations. The unused evaluations
were removed; explicit sums and a separate scalar determinant routine
replaced the flagged operations. The final run treats runtime warnings as
errors and passes. A Markdown delimiter error was also repaired and audited.
The shell cannot set nice 15 because its inherited priority is already 20.

What remains uncertain: no full proof behind the announcement was located;
the search cannot establish its absence. The local analytic branch has not
been proved to lie on the physical liquid side. Global critical-point
existence and uniqueness, the sign or possible vanishing of $C$, endpoint
control, and identification with the model's height limit remain unproved
here. The estimates are not uniform as $\Delta\to\pm1$. No antiferroelectric
extension was attempted.

Next worker: prove the sign of
$C(\theta)=x_0a''+y_0b''-e''$ on the southwest arc for
$0<\gamma<\pi/3$, then use the explicit quadratic displacement to determine
whether the local branch enters the proposed liquid region. This is a
smaller checkable target than global uniqueness or a probabilistic
limit-shape proof. Continue to distinguish analytic candidate formulas
from convergence of the six-vertex model.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, 01:33 Asia/Tbilisi.
