# Open problem T133: The arctic curve of the six-vertex model with domain-wall boundary conditions

Statement: For the six-vertex model with domain-wall boundary conditions on an n × n square, in the disordered regime −1 < Δ < 1, the boundary between the frozen and disordered regions converges after rescaling by n to the curve predicted by Colomo and Pronko, and recovered by the tangent method of Colomo and Sportiello; the analogous prediction holds in the antiferroelectric regime Δ < −1.

Caveat: The predictions are explicit algebraic or transcendental curves depending on the weights; at Δ = 0 (free fermions) the curve is an ellipse, the arctic circle of domino tilings for equal weights.

Source: F. Colomo and A. G. Pronko, The limit shape of large alternating sign matrices, SIAM J. Discrete Math. 24 (2010); F. Colomo and A. Sportiello, Arctic curves of the six-vertex model on generic domains: the tangent method, J. Stat. Phys. 164 (2016)

Where it stands (checked by us, Nov 2026): At Δ = 0 the arctic circle is known (Jockusch–Propp–Shor 1995). At the ice point Δ = 1/2, which includes uniformly random alternating sign matrices, Aggarwal (arXiv:1812.03847, 2020) proved the Colomo–Pronko arctic curve for domain-wall boundary conditions, and the predicted boundaries for more general three-bundle domains. Other values of Δ are open; fluctuations of the height function are T063.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T133 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T133 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T133 (read it,
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
VERDICT: PROVED positive midpoint curvature and a local convex-side collar for the disordered candidate curve when gamma <= u < pi-gamma

This is a deterministic result about the candidate formulas, not a proof
of T133. The parameters are Delta=cos(gamma), 0<gamma<pi/2,
delta=pi-gamma, and T=delta-u.

New beyond round 3: [PROOF.md](PROOF.md) proves C(0)>0 whenever
gamma<=u<delta. In particular it covers equal weights u=T=delta/2
throughout the omitted interval 1/2<Delta<1. Continuity extends the sign
to a neighborhood of the midpoint boundary parameter.

An exact decomposition gives the sign. With h=pi/delta,
R=a''(0)/a(0), q=1/(1-cos T), qh=1/(1-cos(hT)), and
E=cot(T/2)-h cot(hT/2),

\[
2\pi C(0)=E(R-q)+h\cot(hT/2)(h^2q_h-q)>0.
\]

Both trigonometric differences are positive; R-q is nonnegative in
the stated weight range. The proof includes an explicit positive lower
bound. It also shows that the small-B critical branch enters the locally
convex side of the candidate envelope and gives one-to-one coordinates
on a neighborhood on that side. This supplies local uniqueness of small-B
critical parameters, which round 3 left open. It does not exclude other,
distant critical points.

The earlier expansion survives an independent check using scalar Neumann
iteration, composite Gauss quadrature and finite differences. Its two
quadratic constants were also recovered from even moments. Neither script
imports or executes code in the earlier directories.

Reproduce:

~~~sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 recheck.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_geometry.py
~~~

The geometry audit passes 40 derivative/decomposition/curvature checks
and three finite-B displacement comparisons. Quadratic-coefficient
extrapolation errors are at most 5.49e-7. Detailed data are in
[geometry_checks.json](geometry_checks.json); commands and material output
are in [LOG.md](LOG.md). Runs take under two seconds each, use under
20 MiB measured peak RSS, and confirm effective nice 20.

What failed: midpoint quadrature initially obscured the smaller
free-fermion residual; fourth-order Gauss quadrature resolves it.
Near a pole, 70-digit arithmetic lost enough precision to fail the
1e-55 identity tolerance; 100 digits resolves it without relaxing that
tolerance. The shell cannot raise the inherited priority from nice 20
to 15. Outside u>=gamma the first sign summand can be negative, so
this sufficient-condition proof does not extend there.

Literature: the bounded check found no newer complete proof. Alexey
Bufetov's [arXiv:2609.20576v1](https://arxiv.org/abs/2609.20576)
still presents an announcement, with the interval 1/2<Delta<1 omitted.
No absence claim beyond that bounded search is made.

Remaining gaps: the sign along the whole southwest arc, weights u<gamma,
endpoint control, global critical-point classification, and identification
with the model's limiting height remain unproved here. The collar is
geometric; no probabilistic liquid-region assertion follows from it.
No antiferroelectric extension is claimed.

Next worker: prove C(theta)>0 away from the midpoint. A useful reformulation
is C=-a[(b/a)']^2 d^2(e/a)/d(b/a)^2; thus strict concavity of e/a as a
function of b/a would extend the sign and the same collar argument along
the arc. First address u<gamma at theta=0, where the displayed
decomposition remains exact but its first summand has the opposite sign.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, 04:56 Asia/Tbilisi.
