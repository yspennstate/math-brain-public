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
