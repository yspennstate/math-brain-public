# Open problem T102: Random walk on the two-dimensional incipient infinite cluster

Statement: For simple random walk on Kesten's incipient infinite cluster of two-dimensional critical percolation, the quenched return probability is p_{2n}(0,0) = n^{−d_s/2+o(1)} and the mean exit time from the ball of radius r is r^{d_w+o(1)}. Determine the spectral dimension d_s and the walk dimension d_w; in particular decide whether the Alexander–Orbach value d_s = 4/3 holds.

Caveat: Alexander and Orbach conjectured d_s = 4/3 in every dimension; the value is believed to fail in low dimensions, with numerical estimates near 1.32 in two dimensions (d_s = 2d_f/d_w with the resistance exponent 0.9826 of Grassberger, Physica A 262 (1999) 251). By the Einstein relation d_w = d_f + β_res with d_f = 91/48, so the question is the resistance exponent β_res; the Alexander–Orbach value would need β_res = 91/96.

Source: S. Alexander and R. Orbach, Density of states on fractals: fractons, J. Physique Lett. 43 (1982); H. Kesten, Subdiffusive behavior of random walk on a random cluster, Ann. Inst. H. Poincaré Probab. Statist. 22 (1986)

Where it stands (checked by us, Nov 2026): Kesten (1986) proved subdiffusivity on the 2D incipient infinite cluster. The Alexander–Orbach value holds in high dimensions (Kozma–Nachmias 2009), and for the critical level set of the cable-system Gaussian free field in high dimensions (Ganguly–Nam, arXiv:2403.02318). For the incipient infinite cluster of critical site percolation on the triangular lattice, Dankovic, Markering, Miller and Yuan (arXiv:2604.14122, Corollaries 1.3–1.4) prove that the exponents exist: 2(91/48)/(91/48 + β_res) for the almost-sure return probability and 91/48 + β_res for the mean exit time, with β_res not identified. The values are open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T102 (read it,
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
VERDICT: PARTIAL exact resistance-gluing reduction and planar obstruction

The values of d_s and d_w remain open. The bounded literature search found
no solution or substantial advance beyond the supplied brief. The opened
paper by Irina Đanković, Maarten Markering, Jason Miller, Yizheng Yuan,
*The scaling limit of random walk and the intrinsic metric on planar critical
percolation*, [arXiv:2604.14122](https://arxiv.org/abs/2604.14122), has only
v1 listed. Corollaries 1.3–1.4 leave the resistance exponent unidentified.

The completed piece is in PROOF.md. For two connected networks meeting at
an interface, it proves

    R_full = R_A + R_B + D,

where R_A,R_B are the separately wired resistances and D is an explicit
nonnegative quadratic cost of matching their optimal interface currents.
It also gives an exact version for several layers, allowing disconnected
annular pieces, and a sufficient estimate for transferring an annular
resistance exponent to the rooted resistance exponent.

A simple planar unit-resistance cycle gives

    R_A=R_B=L/(L+1),   R_full=(L+1)/2,
    D=(L-1)^2/[2(L+1)].

Consequently no universal constant bounds R_full by the sum of the separately
wired resistances, even at maximum degree 2. This is an obstruction to a
scalar gluing argument, not a counterexample to an IIC probabilistic estimate.
The identities follow from the standard minimum-energy principle; no novelty
claim is made for that principle or its quadratic consequences.

Verification command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_gluing.py
```

All exact rational checks passed: seven cycle sizes, all 255 connected
configurations in the specified three-vertex-interface family, and a
disconnected middle layer. Full-network Kirchhoff solves agreed with local
quadratic composition. An independent combinatorial count gives 255 cases,
including 210 with positive correction. Cycle numbers were independently
re-derived by series/parallel reduction. Data are in cycle_data.csv,
interface_data.csv, and validation_summary.json; commands and outputs are
in LOG.md.

The final run took 0.168 seconds and peaked at 17,039,360 bytes RSS. The
requested nice command warns that setpriority is denied; a direct check
confirms inherited nice 20. Computation used one process and the Python
standard library. Initial attempts to set AS and DATA memory limits failed
before calculation; the successful run checked actual peak RSS. CPU and
wall-time limits were 90 and 120 seconds.

What failed or remains uncertain: no quantitative control of the matching
cost under the IIC law was obtained. The reduction provides no sharper bound
on beta_res and does not decide Alexander–Orbach. The cycle example has no
IIC probability estimate, and the search cannot certify absence of all
later work.

Next worker: for a dyadic decomposition of one IIC realization, retain all
shell components and study the correction D_m defined in PROOF.md (5).
To transfer a candidate scalar shell exponent b>=0, it suffices to establish
sum_i R_i=2^{mb+o(m)} and D_m<=2^{o(m)}sum_i R_i almost surely. A proof with
b>91/96 would imply d_s<4/3 using the existing Einstein relations. Neither
of those two IIC estimates is established here.

Task: “push this problem forward by one checkable piece” — session start
14 November 2026, approximately 21:59 Asia/Tbilisi.
