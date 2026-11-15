# Open problem T101: Closed orbits in the Lorentz mirror model

Statement: At each vertex of Z^2 place, independently, a two-sided mirror along one of the two diagonals, each with probability p/2, or no mirror, with probability 1 − p. A light ray moving along the edges is reflected by mirrors and passes straight through empty vertices. Prove that for every p ∈ (0, 1) every orbit is periodic almost surely.

Caveat: For p = 1 the statement follows from critical bond percolation on Z^2. In three dimensions the opposite is expected at small p: infinite orbits with positive probability.

Source: T. W. Ruijgrok and E. G. D. Cohen, Deterministic lattice gas models, Phys. Lett. A 133 (1988); G. Grimmett, Percolation, 2nd ed. (Springer, 1999)

Where it stands (checked by us, Nov 2026): For p = 1 every orbit is closed, through critical bond percolation. Kozma and Sidoravicius showed that the probability that the ray reaches distance n is at least 1/(2n+1) at every mirror density (arXiv:1311.7437). arXiv:2610.12460 (2026) states that finiteness of all orbits on Z^2 is still a conjecture and builds infinite rays on other decorated planar graphs; arXiv:2609.14949 is a numerical study. Open for 0 < p < 1.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T101 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T101 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T101 (read it,
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
VERDICT: PARTIAL exact probability of vertex-simple periodic orbits with at most ten mirrors

The earlier eight-mirror result holds. An independent cell-interior
enumeration recovers its 38 rank polygons, its generating function, its
probability formula, and its small-density coefficient.

The new contribution of all vertex-simple periodic orbits with exactly ten
mirrors, over arbitrary positive integer coordinate gaps, is

\[
 R_{10}(p)=
 \frac{p(1-p)^2
 [12+110(1-p)^2+312(1-p)^4+405(1-p)^6+247(1-p)^8+58(1-p)^{10}]}
 {128(2-p)^9[1+(1-p)^2]^3}.
\]

Thus the exact probability for at most ten mirrors is

\[
 B_{10}(p)=
 \frac{p}{8(2-p)^3}
 +\frac{p(1-p)^2}{4(2-p)^5}
 +\frac{p(1-p)^2[10+23(1-p)^2]}{64(2-p)^7}
 +R_{10}(p).
\]

This improves the earlier lower bound on periodicity strictly for every
\(0<p<1\). The small-density coefficient increases from
\(225/8192=1800/65536\) to \(1943/65536\). At \(p=1/2\),
the extra term is \(33971/39366000\), and the total increases from
\(95/3888\) to \(497923/19683000\).
The almost-sure periodicity conjecture remains unresolved.

The finite classification contains 528 ten-corner rank polygons.
Two independent exhaustive methods agree on every individual boundary:
all 65,535 nonempty subsets of a four-by-four cell box, and all 72,900
pairs of cyclic surjective corner-coordinate sequences. The latter
retains 5,280 representations, ten per polygon.
The unrooted semiperimeter series is

\[
 F_{10}(r)=
 \frac{r^6(16+112r+220r^2+176r^3+48r^4)}
 {(1-r)^8(1+r)^2}.
\]

Unlike the eight-corner case, its pole at \(r=-1\) remains.
Independent rooted unit walks give counts
\(96,1456,10080,46440,165160\) at perimeters \(12,14,16,18,20\).
Positive gap dynamic programming and a separate signed-binomial formula
agree through perimeter 60. Exact rational gap sums agree with the
closed probability at four densities. Independent perimeter partial
sums agree at those densities and at \(p=1\), with rigorous tail bounds
below \(10^{-30}\). Leading gap singularities separately recover the
small-density coefficient.

Commands, run from this folder:

    nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 ten_cells.py --stage recheck
    nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 ten_cells.py --stage ten
    nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 audit_ten.py --max-length 20

All scripts use only the standard library, one thread, and a 180-second
CPU limit. Successful calculations took under three seconds per run and
under 21 MB peak RSS in the initial runs. They inherited nice 20; the
nice warning reflects the rejected attempt to set relative priority,
and the scripts verify their actual priority remains at least 15.
PROOF.md supplies the full argument and the finite classification rule;
ten_data.json records every polygon; ten_audit.json records the
independent checks and exact tail bounds. LOG.md records commands and
outputs.

The literature check ended within five minutes and found no later
solution. Opened sources were Martin P.W. Zerner,
[*Infinite light rays and infinite clusters with infinitely many pivots*,
arXiv:2610.12460v1](https://arxiv.org/html/2610.12460v1), whose abstract
and introduction retain the square-lattice conjecture; Gady Kozma and
Vladas Sidoravicius,
[*Lower bound for the escape probability in the Lorentz Mirror Model on
the lattice*, arXiv:1311.7437](https://arxiv.org/abs/1311.7437); and
Jian Gu and Qin Hao,
[*Boundary transmission and excursion geometry in the Lorentz mirror
model: a numerical study*, arXiv:2609.14949](https://arxiv.org/abs/2609.14949),
whose abstract explicitly leaves infinite-plane localization unresolved.
This bounded search was not an exhaustive review.

What failed or remains uncertain: macOS rejected an attempted address-space
resource limit before the first enumeration; that unsupported limit was
removed, while the small data structures, CPU limit and RSS checks remain.
No mathematical discrepancy was found. The classification is supported
by explicit exhaustive computations, rather than a hand classification
of all ten-corner shapes. No literature novelty claim is made for this
restricted-family enumeration. The formula excludes every orbit that
repeats a vertex and every simple orbit with at least twelve mirrors;
it supplies no estimate forcing infinite-orbit probability to zero.

Next worker: twelve corners fit in a five-by-five cell box, but exhaustive
cell subsets grow to 33,554,431, so do not scale the present cell loop
blindly. A cyclic six-horizontal-side coordinate enumeration, with early
intersection rejection, is a more promising primary method. Strips can
then have half-crossing weight 3, so retain the factor \(1-r^3\) in the
gap algebra. Use the present counts and individual boundaries as
regression targets before extending the classification. Further corner
enumerations improve this bound; localization still requires control of
unrestricted orbit geometry.

Task: “take the NEXT checkable step on this problem, building on that work” —
received approximately 04:52 Asia/Tbilisi, 15 November 2026.
