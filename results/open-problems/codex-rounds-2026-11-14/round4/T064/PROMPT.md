# Open problem T064: Percolation description of the nodal lines of random waves (Bogomolny–Schmit)

Statement: The nodal set of the random plane wave (the centred Gaussian field on R^2 with covariance J_0(|x − y|)), and conjecturally of high-energy eigenfunctions of chaotic billiards, has the large-scale behaviour of critical percolation: crossing probabilities of nodal domains converge to Cardy's formula and nodal lines to SLE(6).

Caveat: The predicted number of nodal domains per unit area, (3√3 − 5)/π times a normalisation, is off by a few percent in numerics (Nastasescu 2011; Beliaev–Kereta 2013), so the conjecture is the scaling-limit statement, not that constant.

Source: E. Bogomolny and C. Schmit, Percolation model for nodal domains of chaotic wave functions, Phys. Rev. Lett. 88 (2002); M. V. Berry, Regular and irregular semiclassical wavefunctions, J. Phys. A 10 (1977)

Where it stands (checked by us, Nov 2026): The number of nodal domains grows like a constant times the area (Nazarov–Sodin 2009, 2016). Russo–Seymour–Welsh bounds and sharp thresholds hold for positively correlated planar Gaussian fields with fast decay (Beffara–Gayet 2017; Rivera–Vanneuville 2019; Muirhead–Vanneuville 2020). The random plane wave correlates slowly and changes sign, so none of this applies; open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T064 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T064 (read it,
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
VERDICT: PROVED explicit finite-scale level-stability bound for random-plane-wave rectangle crossings

The earlier report holds: nonzero levels are understood, while the
Cardy/SLE(6) conjecture remains open in the sources checked. No later
solution was found in the five-minute literature check. The old folder
contains no PROOF.md or scripts; its existing files were read and left
untouched.

New beyond that report: an explicit bound uniform in the level and
rectangle dimensions. Let p_Q(u) be the left-to-right crossing probability
of {f>=u} in a rectangle of area A and perimeter P, with covariance
J_0(|x-y|). For delta=|u|<=1,

    |p_Q(u)-p_Q(0)|
      <= delta/sqrt(2*pi)
         * [A/(4*pi) + P/(2*pi)*(1+delta^2/3) + 4].

PROOF.md also gives the stronger exact bound for every pair of levels,
with closed-form integrals. It follows that levels u_R=o(R^(-2)) leave
fixed-aspect-ratio crossing probabilities unchanged up to o(1). For
squares, the crossing probability therefore tends to 1/2 at these levels.
The proof counts stratified critical values using Kac–Rice and includes
edge and corner terms. This is a derived quantitative lemma; no claim of
literature priority is made.

The proof and independent audits are in [PROOF.md](PROOF.md). The numerical
audit [check_level_stability.py](check_level_stability.py) checks the
conditional Gaussian expectations by direct quadrature, integrates the
height densities, and recovers the spectral moments independently.
Interior intensity is 0.091888149237 per unit area, agreeing with
Proposition 1.1 of Dmitry Beliaev, Valentina Cammarota and Igor Wigman,
*Two point function for critical points of a random plane wave*,
[arXiv:1704.04943](https://arxiv.org/abs/1704.04943).

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_level_stability.py
```

The first run passed in 0.075 seconds with 12.64 MiB peak RSS and verified
inherited niceness 20. Full output and the final rerun are in
[LOG.md](LOG.md). The numerical checks support the algebra; the proof
does not depend on numerical quadrature.

What failed or remains uncertain: rectangular threshold delocalisation
in Proposition 2.15 of Stephen Muirhead, Alejandro Rivera and Hugo
Vanneuville, with an appendix by Laurin Köhler-Schindler,
*The phase transition for planar Gaussian percolation models without FKG*,
[arXiv:2010.11770v3](https://arxiv.org/abs/2010.11770v3), is qualitative.
It does not justify an explicit logarithmic window for rectangles. The
bound proved here removes only o(R^(-2)) sprinkling; it gives no RSW for
nonsquares, critical exponent, or conformal limit. A short search cannot
certify exhaustive literature novelty. The sandbox denied ps and nice
reported a priority-change warning; the script independently confirmed
that the actual priority already meets the author's requirement.

Next worker: replace the count of all critical points by a Kac–Rice count
weighted by crossing pivotality. The first missing input is a quantitative
conditional four-arm estimate for an interior saddle near level zero,
with the corresponding boundary-arm estimates. Improving that step
would enlarge the level range in which sprinkling can be removed.

Task: “take the NEXT checkable step on this problem, building on that
work” — 15 November 2026, approximately 01:08 Asia/Tbilisi.
