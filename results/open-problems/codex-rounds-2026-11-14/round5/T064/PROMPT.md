# Open problem T064: Percolation description of the nodal lines of random waves (Bogomolny–Schmit)

Statement: The nodal set of the random plane wave (the centred Gaussian field on R^2 with covariance J_0(|x − y|)), and conjecturally of high-energy eigenfunctions of chaotic billiards, has the large-scale behaviour of critical percolation: crossing probabilities of nodal domains converge to Cardy's formula and nodal lines to SLE(6).

Caveat: The predicted number of nodal domains per unit area, (3√3 − 5)/π times a normalisation, is off by a few percent in numerics (Nastasescu 2011; Beliaev–Kereta 2013), so the conjecture is the scaling-limit statement, not that constant.

Source: E. Bogomolny and C. Schmit, Percolation model for nodal domains of chaotic wave functions, Phys. Rev. Lett. 88 (2002); M. V. Berry, Regular and irregular semiclassical wavefunctions, J. Phys. A 10 (1977)

Where it stands (checked by us, Nov 2026): The number of nodal domains grows like a constant times the area (Nazarov–Sodin 2009, 2016). Russo–Seymour–Welsh bounds and sharp thresholds hold for positively correlated planar Gaussian fields with fast decay (Beffara–Gayet 2017; Rivera–Vanneuville 2019; Muirhead–Vanneuville 2020). The random plane wave correlates slowly and changes sign, so none of this applies; open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T064 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T064 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T064 (read it,
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
VERDICT: PROVED sharper crossing-stability bound with saddle-only interior counts and optimal corner coefficient

The preceding finite-scale bound holds. Its complete script was rerun,
and its Gaussian expectations and height integrals were independently
checked using different quadrature. No solution of the Cardy/SLE(6)
conjecture was found in the five-minute literature check.

New beyond round 3: classify the local types that can be a crossing
threshold, and count only those. Interior extrema are excluded. On
vertical edges only tangential maxima with positive inward derivative
are eligible; on horizontal edges only tangential minima with negative
inward derivative are eligible. Each corner has just one eligible
gradient quadrant. These necessary conditions give a strictly sharper
bound for every finite level interval.

For Q=[0,L]x[0,H], A=LH, P=2(L+H), and ordinary superlevel crossing
probability p_Q, the new result is

    0 <= p_Q(a)-p_Q(b) <= integral_a^b D_Q(t) dt,  a<b,

    D_Q(t) = A phi(t) exp(-t^2)/(4 pi)
             + P beta(t)/4
             + (H-L)t phi(t)/(4 sqrt(pi)) + phi(t),

where phi is the standard normal density and

    beta(t) = phi(t)exp(-t^2)/(2 pi)
              + t phi(t)erf(t)/(2 sqrt(pi)).

The edge term is nonnegative despite its signed representation.
The corner coefficient drops from 4 to 1, and 1 is optimal among
interval bounds of this form with fixed area and perimeter densities:
shrinking rectangles have thresholds converging to the field at a point.

For a square the small-|u| bound becomes

    |p_[0,R]^2(u)-1/2|
      <= phi(0)[R^2/(4 pi) + R/(2 pi) + 1]|u|
         + O((R^2+R+1)|u|^3).

The leading edge and corner terms are each divided by four. Removing
extrema saves order R^2|u|^5 near zero and does not change the leading
area term. Thus the sufficient level window remains o(R^(-2)).
PROOF.md contains the full interval bound, closed-form integrals,
local path arguments, orientation check and corner sharpness proof.
This is a derived lemma; no claim of literature priority is made.

Commands:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r3/briefs/T064/check_level_stability.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_local_threshold.py
```

Both passed. The new audit used 13.19 MiB peak RSS and 0.178 seconds
on its first run, with actual niceness 20. It checked direct conditional
Gaussian integrals, 24 interval comparisons, 644 pointwise comparisons,
eight edge normal-form examples and four affine corner cases. Exact
commands and output are in LOG.md. Numerical checks audit the algebra
and signs; the proof does not depend on them.

The topological inputs are genericity and the strict threshold crossing
path in Lemma 2.9 and Lemma B.4 of Stephen Muirhead, Alejandro Rivera
and Hugo Vanneuville, with an appendix by Laurin Köhler-Schindler,
*The phase transition for planar Gaussian percolation models without FKG*,
[arXiv:2010.11770v3](https://arxiv.org/abs/2010.11770v3), which was opened.

What failed or remains uncertain: no attempt here supplies a conditional
macroscopic four-arm bound. Local eligibility overcounts globally
nonpivotal saddles; there is no new large-scale crossing theorem, RSW
bound or conformal limit. Literature priority was not established.
The shell's nice command reports a priority-change warning, but both
scripts independently verified inherited niceness 20. No numerical
check failed. Only this folder was changed; no git or external writes.

Next worker: insert global pivotality into the eligible-point Kac–Rice
count. Seek a quantitative bound on determinant-weighted four-arm
probabilities under the field conditioned on f(x)=t, grad f(x)=0,
uniformly for small t and points far from the boundary. The analogous
boundary estimates should start with the one-sided signs proved here.
An estimate that decays with the distance to the sides is needed to
reduce the area contribution and enlarge the level window.

Task: “take the NEXT checkable step on this problem, building on that
work” — 15 November 2026, 04:33 Asia/Tbilisi.
