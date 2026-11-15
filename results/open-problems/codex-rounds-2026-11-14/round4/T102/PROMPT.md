# Open problem T102: Random walk on the two-dimensional incipient infinite cluster

Statement: For simple random walk on Kesten's incipient infinite cluster of two-dimensional critical percolation, the quenched return probability is p_{2n}(0,0) = n^{−d_s/2+o(1)} and the mean exit time from the ball of radius r is r^{d_w+o(1)}. Determine the spectral dimension d_s and the walk dimension d_w; in particular decide whether the Alexander–Orbach value d_s = 4/3 holds.

Caveat: Alexander and Orbach conjectured d_s = 4/3 in every dimension; the value is believed to fail in low dimensions, with numerical estimates near 1.32 in two dimensions (d_s = 2d_f/d_w with the resistance exponent 0.9826 of Grassberger, Physica A 262 (1999) 251). By the Einstein relation d_w = d_f + β_res with d_f = 91/48, so the question is the resistance exponent β_res; the Alexander–Orbach value would need β_res = 91/96.

Source: S. Alexander and R. Orbach, Density of states on fractals: fractons, J. Physique Lett. 43 (1982); H. Kesten, Subdiffusive behavior of random walk on a random cluster, Ann. Inst. H. Poincaré Probab. Statist. 22 (1986)

Where it stands (checked by us, Nov 2026): Kesten (1986) proved subdiffusivity on the 2D incipient infinite cluster. The Alexander–Orbach value holds in high dimensions (Kozma–Nachmias 2009), and for the critical level set of the cable-system Gaussian free field in high dimensions (Ganguly–Nam, arXiv:2403.02318). For the incipient infinite cluster of critical site percolation on the triangular lattice, Dankovic, Markering, Miller and Yuan (arXiv:2604.14122, Corollaries 1.3–1.4) prove that the exponents exist: 2(91/48)/(91/48 + β_res) for the almost-sure return probability and 91/48 + β_res for the mean exit time, with β_res not identified. The values are open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T102 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T102 (read it,
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
VERDICT: PARTIAL sharp bounds for boundary-current matching costs

The values of d_s and d_w, and the two-dimensional Alexander–Orbach question,
remain open. The five-minute literature check located no newer solution.
The opened arXiv page for Irina Đanković, Maarten Markering, Jason Miller,
Yizheng Yuan, *The scaling limit of random walk and the intrinsic metric on
planar critical percolation*, [arXiv:2604.14122](https://arxiv.org/abs/2604.14122),
still lists only v1. Corollaries 1.3–1.4 express the triangular-lattice IIC
exponents in terms of the unidentified beta_res.

The earlier gluing identity and obstruction hold. They were re-derived from
energy orthogonality and independently checked with unit-voltage Dirichlet
solves. All 255 earlier interface configurations, including the 210 positive
corrections, and all seven earlier cycle values agree exactly. The previous
folder was only read.

The extension in PROOF.md gives an explicit upper bound on the earlier
matching cost. For two connected pieces, write t for the total variation
between their optimal interface-current profiles and a,b for the ordinary,
UNWIRED resistance diameters of that interface inside the two pieces. Then

    D_2 <= [ab/(a+b)] t^2.

Equality holds for every two-vertex interface. For several layers, let
k_i=a_i b_i/(a_i+b_i) and let t_i be the adjacent profile mismatch. Then

    D_m <= 2 sum_i k_i t_i^2.

The factor 2 is optimal, even for three planar layers of unit resistances
and maximum degree 3. An explicit family satisfies D_3/(sum_i k_i t_i^2)->2.
The proof also permits disconnected layers when each nonzero mismatch can
be repaired on at least one side having finite resistance diameter.

Consequently an annular approach can replace the previous condition on the
abstract minimum D_m by the sufficient estimate

    sum_i k_i t_i^2 <= 2^{o(m)} sum_i R_i.

Together with sum_i R_i=2^{mb+o(m)}, this transfers exponent b to the rooted
resistance along dyadic scales. No such estimate is proved for the IIC.
These are consequences of minimum energy and a boundary transport argument;
no claim of a new general electrical-network principle is made.

Verification command, run from this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_matching.py
```

All exact checks passed: the earlier cases above; 729 pairs of weighted
three-arm stars; 128 three-layer strips; 11 sharpness-family cases; and the
previous disconnected example. At L=1024 the sharpness ratio is
1.9970760280. Its full resistance agrees with a separate two-variable flow
minimization, and its asymptotics follow from a path upper bound and a
Rayleigh-contraction lower bound. Complete rational output is in
matching_results.json; commands and audit details are in LOG.md.

The final run used one process, standard-library rational arithmetic,
15,810,560 bytes peak RSS, and 0.3646 seconds. The requested nice command
warned that setpriority was denied; the program verified inherited nice 20.
The single-thread environment and 90-second CPU/120-second wall limits were
checked or set by the script.

What failed: coefficient 1 in the many-layer bound is false; repairs can
reinforce on a shared edge. During audit, the first quotient-network count
in the sharpness proof was found incorrect and replaced by contracting all
four unit edges. The corrected lower bound is (1/L+2/K)^(-1); the exact
network computations and limiting coefficient are unchanged.

What remains uncertain: no probability bound on these mismatch energies,
no improvement to beta_res, and no decision on d_s=4/3. Worst-pair unshorted
diameters may be too coarse, or infinite, for ordinary IIC shells. The
bounded literature search cannot certify absence of later work, and the
network inequalities have not been checked for prior publication.

Next worker: test a decomposition at nested open circuits, retaining all
shell components. First check whether at least one adjacent shell connects
each circuit boundary. For each interface compute t_i and the smaller finite
unshorted diameter, then compare sum_i k_i t_i^2 to sum_i R_i in the SAME
realizations. If worst-pair diameters dominate, use the dipole-coupling
bound in PROOF.md Section 2 on the actual signed mismatch instead. A
percolation tail estimate, rather than another scalar resistance identity,
is the missing step. This report gives no evidence that the needed ratio
is subpolynomial.

Task: “take the NEXT checkable step on this problem, building on that work” —
session start 15 November 2026, approximately 01:28 Asia/Tbilisi.
