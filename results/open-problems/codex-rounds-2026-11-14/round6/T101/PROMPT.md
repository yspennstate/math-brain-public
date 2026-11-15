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

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T101 (read it, never
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
VERDICT: PARTIAL exact probability of vertex-simple periodic orbits with at most twelve mirrors

The earlier ten-mirror result holds. An independent unit-vertex enumeration
recovers all 528 individual rank polygons, their strip weights, generating
function, exact probability values, rooted counts, and small-density
coefficient.

The new contribution of all vertex-simple periodic orbits with exactly
twelve mirrors, over arbitrary positive integer coordinate gaps, is

\[
 R_{12}(p)=\frac{p\,H((1-p)^2)}
 {2048(2-p)^{11}[1+(1-p)^2]^5},
\]

where

\[
\begin{aligned}
 H(r)={}&3+129r+1928r^2+10326r^3+28484r^4\\
        &+45522r^5+43964r^6+25510r^7+8121r^8+1093r^9.
\end{aligned}
\]

Thus the exact restricted-family probability is
\(B_{12}(p)=B_{10}(p)+R_{12}(p)\), with the full expression in PROOF.md.
This strictly improves the earlier lower bound on periodicity for every
\(0<p<1\). Its small-density coefficient increases from
\(1943/65536\) to \(518043/16777216\). At \(p=1/2\),
the extra term is \(25440181/56687040000\) and the total is
\(1459458421/56687040000\).
The almost-sure periodicity conjecture remains unresolved.

Unlike the six-, eight-, and ten-mirror terms, the twelve-mirror term is
positive at \(p=1\): the five-cell cross has an all-turning twelve-step
boundary. Its six translates through the root contribute \(3/2048\).
Consequently \(B_{12}(1)=259/2048\).

The classification contains 9,901 rank polygons. One exhaustive method
tests 5,484,964 cyclic coordinate-word pairs using disjoint half-open
unit-vertex sets, retaining 118,812 representations, twelve per polygon.
An independent cell-row construction visits 129,988 prefixes, obtains
18,525 local candidates, and rejects 8,624 disconnected boundaries.
The methods agree on every boundary and both oriented strip lists.
The complete grouped table is in PROOF.md.

The unrooted semiperimeter series is

\[
 F_{12}(r)=
 \frac{r^6(1+36r+454r^2+1964r^3+4246r^4+5068r^5+
                 3378r^6+1196r^7+165r^8)}
 {(1-r)^{10}(1+r)^4}.
\]

Weight-three strips occur, but their factor \(1+r+r^2\) cancels in the
full sum. Independent exact polynomial expansions verify this cancellation
and the derivative giving \(R_{12}\). Rooted unit walks independently give
twelve-corner counts \(6,294,5560,51012,304800\) at perimeters
\(12,14,16,18,20\). A signed-binomial expression agrees with positive gap
dynamic programming through perimeter 80. Exact gap sums agree at four
rational densities. Independent perimeter partial sums also agree at
those densities and \(p=1\), with rigorous exact tail bounds below
\(10^{-30}\). Separate gap singularities recover the small-density constant.

Commands, run from this folder in order:

    nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 twelve.py --stage recheck
    nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 twelve.py --stage twelve
    nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 audit_twelve.py

All scripts use only the standard library, one thread, a 180-second CPU
limit and a 900-second wall alarm. Runs took under five seconds each and
the measured full-run peak, including JSON serialization, was 137,625,600
bytes (under 138 MB). Actual nice is 20; macOS rejects the
relative nice adjustment from that inherited priority, which does not
increase priority. Both scripts verify nice >=15 and OMP_NUM_THREADS=1.
LOG.md records commands and outputs. ten_recheck.json, twelve_data.json
and twelve_audit.json retain the exact data.
measure_resources.py independently measures complete runs; its commands
and the two resource JSON files are recorded in LOG.md.

The bounded literature check found no later solution. Opened sources include
Martin P. W. Zerner, [*Infinite light rays and infinite clusters with
infinitely many pivots*, arXiv:2610.12460](https://arxiv.org/html/2610.12460v1),
which still states the square-lattice conjecture; Gady Kozma and Vladas
Sidoravicius, [*Lower bound for the escape probability in the Lorentz Mirror
Model on the lattice*, arXiv:1311.7437](https://arxiv.org/abs/1311.7437);
and Jian Gu and Qin Hao, [*Boundary transmission and excursion geometry in
the Lorentz mirror model: a numerical study*,
arXiv:2609.14949](https://arxiv.org/abs/2609.14949), which leaves localization
unresolved. Additional opened papers concerned a hierarchical model and
loop weight 2; details are in LOG.md. The search took less than five minutes
and was not exhaustive.

What failed or remains uncertain: no mathematical discrepancy or failed
mathematical computation was found. The optional /usr/bin/time resource
wrapper failed on a sandbox-denied sysctl query after a successful audit;
the standard-library resource wrapper replaced it successfully. Two
plausible extrapolations from earlier corner
counts are false: the twelve-corner contribution does not vanish at \(p=1\),
and the new weight-three factor does not survive the complete summation.
The finite classification depends on explicit exhaustive computations,
with independent implementations and full data supplied; no hand
classification or literature novelty is claimed. The result omits every
orbit with repeated vertices and every simple orbit with at least fourteen
mirrors. It gives no estimate forcing infinite-orbit probability to zero.

Next worker: the cell-row algorithm is a better starting point for fourteen
corners than enumerating all subsets of a six-by-six cell box or all pairs
of seven-coordinate words. Use the exact twelve-corner list as a regression
target. For an independent construction, generate cyclic side coordinates
with early intersection rejection and fix starting-corner redundancy before
forming all word pairs. Seven horizontal sides still allow strip weights
only 1,2,3; retain \(1-r^3\) until exact cancellation is checked. A
fourteen-corner all-turning polygon cannot close, since it would have seven
horizontal unit sides, so its contribution at \(p=1\) must vanish.
More corner enumeration improves this bound; the localization problem
still requires control of unrestricted orbit geometry.

Task: “take the NEXT checkable step on this problem, building on that work” —
received approximately 08:18 Asia/Tbilisi, 15 November 2026.
