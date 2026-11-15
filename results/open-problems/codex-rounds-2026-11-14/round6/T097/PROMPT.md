# Open problem T097: Critical behaviour of level-set percolation of the three-dimensional Gaussian free field

Statement: For the discrete Gaussian free field φ on Z^3, the excursion set {φ ≥ h} has an infinite cluster for h < h_* and none for h > h_*. Determine its behaviour at and near h_*: whether the percolation probability, the correlation length and the one-arm probability at h_* follow power laws, with which exponents, and whether these agree with those of the cable-system field.

Caveat: On the metric graph (cable system) the critical level is 0 and several exponents are known exactly; the lattice field has h_* > 0 and is not covered by those results.

Source: A. Drewitz, A. Prévost and P.-F. Rodriguez, Critical exponents for a percolation model on transient graphs, Invent. Math. 232 (2023), 229–299; H. Duminil-Copin, S. Goswami, P.-F. Rodriguez and F. Severo, Equality of critical parameters for percolation of Gaussian free field level sets, Duke Math. J. 172 (2023)

Where it stands (checked by us, Nov 2026): The transition is sharp, h_* = h_** = h̄ (Duminil-Copin–Goswami–Rodriguez–Severo, arXiv:2002.07735), and h_* > 0 on Z^d for every d ≥ 3 (Drewitz–Prévost–Rodriguez, arXiv:1708.03285). On the cable system h_* = 0 (Lupu 2016) and critical exponents are computed in low dimensions (Ding–Wirth, Ann. Probab. 48 (2020); Drewitz–Prévost–Rodriguez, Invent. Math. 232 (2023); Cai–Ding, arXiv:2406.02397, which gives the one-arm probability up to constants for 3 ≤ d ≤ 5); the recent arXiv:2406.02397 and arXiv:2610.03703 are also about the cable system. For the lattice field no critical exponent is known to exist.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T097 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T097 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T097 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T097 (read it, never
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
VERDICT: PARTIAL the actual cube-capacity coefficient with a bounded error and a strict improvement of the previous trial constant

The preceding result holds under independent verification. The brief web
check found no later solution of the lattice critical-exponent problem.

The new result identifies the true leading lattice cube-capacity
coefficient, rather than another restricted trial-family coefficient.
For SRW Green covariance, define

    kappa = inf { (1/6) integral |grad F|^2 :
                  F compactly supported and Lipschitz,
                  F=1 on [-1,1]^3 }.

PROOF.md proves, for every integer R>=1,

    kappa R <= cap(B_R) <= kappa(R+1/2).

Consequently cap(B_R)=kappa R+O(1), with the error in [0,kappa/2].
The new ingredient is a reverse transfer by trilinear interpolation;
the predecessor's unit-cell averaging supplies the other direction.
No continuum-limit theorem or existence of a minimizer is assumed.

A variation supported in six face regions also proves

    2 pi/3 <= kappa <= C_1 < C_cube,
    C_1 = C_cube - 486 pi^2 C_cube^2/(24+16 pi)^4,

where C_cube is the exact constant from round 4. Thus its distance-profile
class is strictly suboptimal for the actual leading capacity coefficient.
The value of kappa is identified variationally, not evaluated in closed form.

For the same relative one-arm radius as before, the consequence is

    liminf_{t->0} t^2 log(1/t) L_rel(t)
      >= (log 2)^2/(8 kappa)
      >= (log 2)^2/(8 C_1) > (log 2)^2/(8 C_cube).

This uses the same existing density input from Stephen Muirhead,
[arXiv:2206.10724v2](https://arxiv.org/html/2206.10724v2), Theorems 1.2
and 1.10. Its excluded endpoint is not used.

AUDIT.md checks the interpolation by a separate Gram-matrix calculation,
the decrement by a fixed-amplitude trial function, and the crossover
coefficient by Gaussian tails instead of Holder. It checks support,
boundary cells, normalization, every integer radius, and finite cutoffs.

Commands: predecessor files were discovered with `rg --files` and read
with `OMP_NUM_THREADS=1 nice -n 15 cat <paths>`. Final file and consistency
checks are recorded in LOG.md. No numerical script, simulation, numerical
workload, or decimal evaluation was run. The sandbox denied priority
changes; work remained analytic with lightweight file reads. All authored
files are in this folder. No git, subagents, external writes or edits to
earlier folders were used.

What failed or remains uncertain: the logarithmic loss is unchanged. No
connection-specific score estimate or comparison to a conventional
correlation length was obtained. No lattice critical exponent, exponent
existence, critical nonpercolation, or agreement with cable exponents is
proved. The capacity interpolation may be standard; novelty of this
elementary argument or the explicit face variation is not established.
The L_rel coefficient is a lower bound, not proved optimal.

Next worker: the deterministic capacity coefficient is now identified,
so further capacity improvements cannot change the logarithmic order.
The substantive next target remains a connection-specific estimate for
-d/dh log p_R(h) of order sqrt(R), uniform over
h in [h_*,h_*+c/sqrt(R)], or a comparison with a specified conventional
correlation length. For capacity questions, (1) in PROOF.md gives a
uniform bounded error and section 6 gives an explicit admissible angular
variation; neither should be mistaken for an exponent calculation.

Task: “take the NEXT checkable step on this problem, building on that work”
— 15 November 2026, first retained local clock reading 08:14:56 +0400
(Asia/Tbilisi).
