# Open problem T097: Critical behaviour of level-set percolation of the three-dimensional Gaussian free field

Statement: For the discrete Gaussian free field φ on Z^3, the excursion set {φ ≥ h} has an infinite cluster for h < h_* and none for h > h_*. Determine its behaviour at and near h_*: whether the percolation probability, the correlation length and the one-arm probability at h_* follow power laws, with which exponents, and whether these agree with those of the cable-system field.

Caveat: On the metric graph (cable system) the critical level is 0 and several exponents are known exactly; the lattice field has h_* > 0 and is not covered by those results.

Source: A. Drewitz, A. Prévost and P.-F. Rodriguez, Critical exponents for a percolation model on transient graphs, Invent. Math. 232 (2023), 229–299; H. Duminil-Copin, S. Goswami, P.-F. Rodriguez and F. Severo, Equality of critical parameters for percolation of Gaussian free field level sets, Duke Math. J. 172 (2023)

Where it stands (checked by us, Nov 2026): The transition is sharp, h_* = h_** = h̄ (Duminil-Copin–Goswami–Rodriguez–Severo, arXiv:2002.07735), and h_* > 0 on Z^d for every d ≥ 3 (Drewitz–Prévost–Rodriguez, arXiv:1708.03285). On the cable system h_* = 0 (Lupu 2016) and critical exponents are computed in low dimensions (Ding–Wirth, Ann. Probab. 48 (2020); Drewitz–Prévost–Rodriguez, Invent. Math. 232 (2023); Cai–Ding, arXiv:2406.02397, which gives the one-arm probability up to constants for 3 ≤ d ≤ 5); the recent arXiv:2406.02397 and arXiv:2610.03703 are also about the cable system. For the lattice field no critical exponent is known to exist.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T097 (read it,
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
VERDICT: PARTIAL a capacity-based lattice reduction and a relative one-arm crossover lower bound

For the lattice GFF with simple-random-walk Green covariance, PROOF.md proves
the finite-scale inequality

    p_R(h+t) >= Phi(Phi^{-1}(p_R(h))-t sqrt(cap(B_R))),
    cap(B_R) <= (28R-1/R)/3.

Here p_R(h) is the lattice probability of connecting 0 to the sup-norm sphere
of radius R at level h. The capacity coefficient is optimal over all
increasing events measurable on the box, as witnessed by half-spaces.
Optimality for the connection event is not asserted.

The resulting checkable consequences are:

- If theta(h_*-t)=t^{beta+o(1)} and p_R(h_*)=R^{-rho+o(1)} with finite
  nonnegative exponents, then beta >= 2 rho.
- Combining the comparison with Stephen Muirhead's existing density theorem
  gives p_R(h_*) >= R^{-2-epsilon} for every epsilon>0 and all sufficiently
  large R. No existence of rho is required.
- Let L_rel(t) be the first integer R for which
  p_R(h_*+t)<=p_R(h_*)/2. Then L_rel(t) is finite and
  L_rel(t)>=c t^{-2}/log(1/t) for small t. A logarithmic exponent for this
  particular radius, if it exists, is at least 2.

This is a proved reduction using standard Gaussian methods. Novelty is not
established. It does not settle any of the requested exact lattice exponents.

The external input is Stephen Muirhead, *Percolation of strongly correlated
Gaussian fields II. Sharpness of the phase transition*,
[arXiv:2206.10724v2](https://arxiv.org/html/2206.10724v2), Theorems 1.2 and
1.10. In this dimension they give theta(h_*-t)>=c_q t^q for every q>4;
using q=4 itself would be unjustified. LITERATURE.md records the opened
sources. The new November paper
[arXiv:2611.05357](https://arxiv.org/abs/2611.05357) concerns cable clusters
in the high-dimensional regime, so does not settle this lattice question.

The literature search took less than ten minutes. No numerical computation
or data file was needed. Exact numerical command: none. Read-only orientation
used commands prefixed with `OMP_NUM_THREADS=1 nice -n 15`; the sandbox denied
the priority change, and no numerical workload followed. Mathematical outputs
are the proofs in PROOF.md. AUDIT.md records two derivations of the comparison,
an independent Hölder check of the exponent calculations, and two exact
calculations of the energy constant. LOG.md records the steps and searches.

What failed: the comparison alone does not yield a constant-factor
`L_rel(t)>=c t^{-2}` bound; the normal-tail loss grows at that proposed scale.
It does not equate L_rel with a two-point or crossing correlation length.
It does not rule out critical percolation, establish exponent existence,
or transfer cable exponents to the lattice. The literature check cannot
certify that these elementary consequences have not appeared elsewhere.

Next worker: seek a connection-event-specific improvement of the score bound
in PROOF.md section 2, or prove a comparison between L_rel and a chosen
correlation length. Either would address a missing step; merely substituting
cable exponents would not. A sharper density lower bound in (12) would also
improve the unconditional one-arm bound immediately.

Task: “push this problem forward by one checkable piece” — 14 November 2026,
first recorded local time 21:16:48 +04 (Asia/Tbilisi).
