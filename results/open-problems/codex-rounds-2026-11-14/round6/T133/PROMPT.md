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

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T133 (read it, never
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
VERDICT: PROVED positive curvature on every open candidate arc at Delta = 1/sqrt(2), for all weight ratios

This is a deterministic theorem about the candidate formulas, proved by
an exact integer certificate. It does not prove T133 or identify a
probabilistic liquid region.

New beyond round 4: at gamma=pi/4, the sign
`C(theta)=x0 a''+y0 b''-e'' > 0` holds for every
`0<u<3pi/4` and `|theta|<3pi/4-u`. Thus it includes the previously
missing weights u<gamma and the entire open southwest arc. The arc is an
embedded strictly convex graph, with x0'>0, y0'<0 and
`d²y/dx²=W²/(C b³)>0`. Reflection and u↔T give the other three open arcs.
The small-B critical branch gives a locally convex-side collar at every
interior point, with injectivity uniform on compact subarcs. Distant
critical points are not excluded.

[PROOF.md](PROOF.md) gives the complete reduction. Setting
`x=tan((T+theta)/6)`, `y=tan((T-theta)/6)` turns the domain into
`x,y>0, x+y+xy<1` and the curvature numerator into positive elementary
factors times a symmetric polynomial Q. The substitution
`x=r/(1+r)`, `y=s/((1+s)(1+2r))` turns Q, after clearing positive
denominators, into a polynomial R with 324 positive coefficients and
zero constant term. In fact `R(r,s)>=63(r+s)>0`.

The full coefficient arrays are in [certificate.json](certificate.json).
The rational identity and every coefficient sign are independently checked
by [audit_certificate.py](audit_certificate.py), using standard-library
integer arithmetic. This check shares no symbolic algebra implementation
with the SymPy derivation. Both give coefficient sum 17765219441341512
and maximum coefficient 692394213766656; these checksums are supplementary
to equality of every coefficient.

Reproduce from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 recheck.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 derive_certificate.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_certificate.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_geometry.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_branch.py
```

The earlier midpoint result passes 25 independent derivative/decomposition
checks. The new formula passes 63 comparisons with derivatives of the
original trigonometric coefficients, including near parameter edges.
Four direct finite-B computations enter the convex side and recover the
quadratic displacement, with relative extrapolation error at most
7.66e-6. Detailed commands and output are in [LOG.md](LOG.md). Runs take
under seven seconds each, configure one thread, use under 74 MiB measured
peak RSS, and confirm effective nice 20.

What failed: the general midpoint decomposition still has a negative
summand at u<gamma; no general-parameter sign proof was obtained. The
independent numerator audit initially used an insufficient common
denominator; its assertion caught this and the power was corrected.
Near simultaneous parameter edges, 100-digit evaluation lost enough
precision to fail the numerical identity tolerance; 160 digits passed
without relaxing it. These failures and two exploratory SymPy Boolean
counting errors are recorded in LOG.md. The shell cannot raise inherited
nice 20 to 15.

Literature: the bounded check found no later complete solution. Alexey
Bufetov's [arXiv:2609.20576v1](https://arxiv.org/abs/2609.20576) still
announces results with 1/2<Delta<1 omitted. No absence claim beyond that
search is made.

Remaining gaps: other Delta values, joining-point control, global
critical-point classification, and convergence of the random model.
No antiferroelectric extension is claimed. No literature priority is
claimed for the deterministic geometry lemma.

Next worker: use the rational formulas at gamma=pi/4 to compute and match
the four joining-point limits, then determine whether these open-arc
collars combine into a collar of a simple closed convex candidate curve.
For a parameter extension, seek a positive representation of C for
general gamma; the all-positive polynomial here supplies an exact
special-case check for such a representation.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 15 November 2026, 08:29 Asia/Tbilisi.
