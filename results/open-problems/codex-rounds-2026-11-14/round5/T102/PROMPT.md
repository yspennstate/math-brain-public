# Open problem T102: Random walk on the two-dimensional incipient infinite cluster

Statement: For simple random walk on Kesten's incipient infinite cluster of two-dimensional critical percolation, the quenched return probability is p_{2n}(0,0) = n^{−d_s/2+o(1)} and the mean exit time from the ball of radius r is r^{d_w+o(1)}. Determine the spectral dimension d_s and the walk dimension d_w; in particular decide whether the Alexander–Orbach value d_s = 4/3 holds.

Caveat: Alexander and Orbach conjectured d_s = 4/3 in every dimension; the value is believed to fail in low dimensions, with numerical estimates near 1.32 in two dimensions (d_s = 2d_f/d_w with the resistance exponent 0.9826 of Grassberger, Physica A 262 (1999) 251). By the Einstein relation d_w = d_f + β_res with d_f = 91/48, so the question is the resistance exponent β_res; the Alexander–Orbach value would need β_res = 91/96.

Source: S. Alexander and R. Orbach, Density of states on fractals: fractons, J. Physique Lett. 43 (1982); H. Kesten, Subdiffusive behavior of random walk on a random cluster, Ann. Inst. H. Poincaré Probab. Statist. 22 (1986)

Where it stands (checked by us, Nov 2026): Kesten (1986) proved subdiffusivity on the 2D incipient infinite cluster. The Alexander–Orbach value holds in high dimensions (Kozma–Nachmias 2009), and for the critical level set of the cable-system Gaussian free field in high dimensions (Ganguly–Nam, arXiv:2403.02318). For the incipient infinite cluster of critical site percolation on the triangular lattice, Dankovic, Markering, Miller and Yuan (arXiv:2604.14122, Corollaries 1.3–1.4) prove that the exponents exist: 2(91/48)/(91/48 + β_res) for the almost-sure return probability and 91/48 + β_res for the mean exit time, with β_res not identified. The values are open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T102 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T102 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T102 (read it,
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
VERDICT: PARTIAL sharp bounds for matching boundary currents on nested circuits

The two-dimensional values of d_s and d_w remain unidentified. The bounded
literature check found no newer solution. The opened arXiv page for Irina
Đanković, Maarten Markering, Jason Miller, Yizheng Yuan, *The scaling limit
of random walk and the intrinsic metric on planar critical percolation*,
[arXiv:2604.14122](https://arxiv.org/abs/2604.14122), still lists only v1.
Its Corollaries 1.3–1.4 and “Explicit lengths” discussion leave beta_res
unidentified. This does not decide Alexander–Orbach.

The round-3 result holds. An independent prescribed-divergence calculation
with exact rational LDL^T factorization reproduced all 255 earlier interface
cases, the 210 positive corrections, 729 weighted-star cases, and all 11
sharpness-family values. The latter agree exactly with the saved round-3
data. Its asymptotic factor 2 was also re-derived from the path upper bound
and corrected contraction lower bound. Earlier folders were only read.

The new piece in PROOF.md resolves the circuit-boundary case proposed by
round 3. Write A for the sum of separately wired layer resistances and
delta_i for the mismatch of their optimal currents on interface circuit C_i.
Then

    0 <= R_full-A <= sum_i Q_{C_i}(delta_i).

The coefficient 1 is sharp. All circuit edges carry zero current in the
local wired optima, and repairs on distinct circuits use disjoint edges.
Consequently no factor 2 is needed. All shell components are retained.
Circuit edges can even be split between adjacent layers: the bound works
when BOTH of the previous ordinary interface diameters are infinite.
Assigning a complete circuit to its inner layer guarantees a finite
diameter on that side, answering the previous connectivity question.

For a circuit with edge resistances rho_j, let H_j be the cumulative signed
mismatch in cyclic order, W=sum rho_j, and Hbar=sum rho_j H_j/W. The exact
repair energy is

    Q_C(delta)=sum_j rho_j(H_j-Hbar)^2 <= (W/4) TV(delta)^2.

It takes linear time to evaluate once the boundary profiles are known.
The actual demand matters: on an even unit circuit of length N, an
alternating demand of total variation 1 has energy 1/N, whereas an
antipodal unit dipole has energy N/4. This bound need not dominate the
previous harmonic diameter bound, since circuit-only repairs ignore
interior shortcuts.

A checked obstruction shows the limitation of circuit connectivity. Two
nested unit circuits, each of length 2L, with antipodal entry and exit
vertices and three connecting unit bridges, have

    A=3,  R_full=L+3,  R_full-A=Q_total=L.

The graph is planar, has maximum degree 3, and attains the circuit bound.
Thus nested circuits alone do not give a universally bounded gluing ratio.
This is an abstract planar network example, without an IIC probability
estimate or a prescribed triangular-lattice embedding.

Verification command, from this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_circuits.py
```

All exact checks passed. Beyond the earlier cases, these include 1,222
weighted-circuit/demand tests, all 3,600 square-interface networks with
nonempty terminal-neighbor sets and arbitrary circuit-edge ownership,
336 nested-circuit networks, and five sizes of the obstruction family.
Among the square cases, 328 have both old diameters infinite; 656 attain
the circuit bound, including 240 with zero correction. These counts have
separate combinatorial or voltage-based checks. The script verifies the
actual repaired flows as well as the resistance inequalities. Full output
is circuit_results.json; commands and audits are in LOG.md.

Final run: 2.9471 seconds, peak RSS 17,334,272 bytes, one process, standard
library only, single-thread environment, CPU/wall limits 90/120 seconds.
The nice command warned that setpriority was denied; inherited nice 20
was checked. There were no failed mathematical tests.

What failed: circuit connectivity does not itself control the gluing ratio,
as the equality family proves. What remains uncertain: no probability or
tail estimate on circuit mismatch energies, no improvement to beta_res,
and no decision on d_s=4/3. No percolation sample or exponent fit was made.
The literature check is bounded, and prior publication of these elementary
network consequences was not investigated systematically.

Next worker: choose nested open circuits in a finite origin-to-distance-R
conditioned triangular-lattice cluster, recording the selection rule and
all conditioning. Retain all shell components and compute, in each SAME
realization, A and C=sum_i Q_{C_i}(delta_i) using the cumulative formula.
Record circuit lengths, TV mismatches, and their cumulative-current variance
separately; the latter can be much smaller than length times TV squared.
The target sufficient estimate is C<=R^{o(1)} A, jointly with an identified
exponent for A. Selection of circuit scales and comparison with ball exit
resistance also need justification. This session supplies no evidence that
the probabilistic target holds; a repair using interior paths may be
necessary if the circuit bound is too large.

Task: “take the NEXT checkable step on this problem, building on that work” —
session start 15 November 2026, approximately 04:52 Asia/Tbilisi.
