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
VERDICT: PARTIAL a non-shell capacity bound and a larger relative crossover coefficient

The predecessor's shell optimization and coefficient (log 2)^2/32 hold
under independent verification. The brief web check found no lattice
resolution; the recent papers opened concern the cable system.

The new piece is a deterministic capacity estimate outside the predecessor's
restricted class. In SRW Green normalization, PROOF.md proves for R>=1

    cap(B_R) <= C_cube (R+1/2),
    C_cube = 2 pi delta/[3 log((3+delta)/(3-delta))],
    delta = sqrt(9-24/pi),
    C_cube <= 8/9+2 pi/3 < 3.

The proof averages continuum trial functions over unit cells to obtain
an exact upper bound on lattice energy. It then optimizes profiles depending
on Euclidean distance from the enlarged cube. This strictly improves the
earlier bound A_R>4R at every R>=2. At R=1 either bound can be used.
Optimality is asserted only within the specified continuum profile class,
not for actual cube capacity.

For exactly the same radius as before,

    L_rel(t) = min{R>=1: p_R(h_*+t)<=p_R(h_*)/2},

the improved consequence is

    liminf_{t->0} t^2 log(1/t) L_rel(t)
        >= (log 2)^2/(8 C_cube) > (log 2)^2/24.

This improves the previous guaranteed coefficient by a factor 4/C_cube>4/3.
It uses the same existing density theorem of Stephen Muirhead,
[arXiv:2206.10724v2](https://arxiv.org/html/2206.10724v2), Theorems 1.2
and 1.10, without using its excluded endpoint. The power and logarithmic
loss are unchanged.

AUDIT.md rechecks the geometric factors through the volume of a parallel
body, the exact integral by completing the square, the variational profile
by its Euler equation, and the crossover coefficient with Gaussian tails
instead of Holder. It checks finite support, nonsmooth boundaries, all
smaller radii, and the half-cell enlargement. No numerical computation,
decimal evaluation, simulation, or mathematical script was needed or run.

Commands: predecessor files were read with
`OMP_NUM_THREADS=1 nice -n 15 cat <absolute paths>`; source files were
discovered with `rg --files`. Final verification uses
`OMP_NUM_THREADS=1 nice -n 15 sh -c '<file checks>'`, recorded verbatim
in LOG.md. The sandbox denied priority changes, so no numerical workload
was launched. All authored files are in this folder. Earlier folders
were read only; there were no subagents, git operations, or external writes.

What failed or remains uncertain: this does not give a connection-specific
score bound or remove the logarithm. It does not compare L_rel to a
conventional correlation length. No exact lattice exponent, exponent
existence, critical nonpercolation, or equality with cable exponents is
proved. The true leading cube capacity coefficient and novelty of the
elementary estimate are not established.

Next worker: use the exact unit-cell transfer in PROOF.md section 2 if
sharper geometric bounds are useful, but further constant improvements
alone will not remove the logarithm. The substantive missing estimate is
still a connection-specific bound on -d/dh log p_R(h), of order sqrt(R)
uniformly for h in [h_*,h_*+c/sqrt(R)], or a comparison with a specified
crossing or two-point length. Neither is supplied here.

Task: “take the NEXT checkable step on this problem, building on that work”
— 15 November 2026, first retained local clock reading 04:49:23 +04
(Asia/Tbilisi).
