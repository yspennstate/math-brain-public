VERDICT: PARTIAL exact probability of repeated-vertex periodic orbits with at most eight turning visits

The preceding twelve-mirror result holds. Re-running its independent cell-row
construction recovers all 9,901 boundaries and both strip lists, the exact
generating-function identities, rooted counts, probability values, and
small-density coefficient.

The new result counts a family omitted by every earlier round: all periodic
orbits that repeat a vertex and have at most eight turning visits, over
arbitrary positive integer coordinate gaps. A mirror visited twice counts
as two turning visits and one distinct mirror. With \(q=1-p\), \(d=2-p\),
the exact probability for a fixed directed edge is

\[
 C(p)=\frac{p}{16d^4}+\frac{9pq^2}{64d^7}
      +\frac{pq^3(15+34q^2+17q^4)}{32d^7(1+q^2)^2}.
\]

This family is disjoint from the earlier vertex-simple family. Thus the
periodicity probability is at least \(B_{12}(p)+C(p)\), a strict improvement
for every \(0<p<1\). The new contribution and combined bound satisfy

\[
\begin{aligned}
 \lim_{p\downarrow0}C(p)/p&=37/4096,\\
 \lim_{p\downarrow0}[B_{12}(p)+C(p)]/p&=669595/16777216,\\
 C(1/2)&=164/18225,\\
 B_{12}(1/2)+C(1/2)&=1969564021/56687040000
                      \ \simeq 0.03474452,\\
 C(1)&=1/16,\qquad B_{12}(1)+C(1)=387/2048.
\end{aligned}
\]

There are 62 non-simple rank circuits in five families, indexed by
(turning visits, double mirror vertices, double empty vertices):
(6,0,1):2; (8,0,1):40; (8,0,2):14; (8,0,3):4; (8,1,0):2.
The probability of a prescribed length-\(L\) circuit is
\((p/2)^{k-t}q^{L-k-c}\), since repeated visits do not require independent
copies of the same local state.

Two exhaustive methods agree on every circuit and both oriented strip lists:
cyclic corner-coordinate words, and local-state trajectories in the entire
four-by-four rank vertex grid. A separate rooted walk search checks all
coefficients through length 16. Exact polynomial identities, positive-gap
versus signed-binomial coefficients through length 80, and 25 rational
family sums with rigorous tails below \(10^{-30}\) also agree.
Direct tracing of all 19,683 environments in a three-by-three vertex box
checks the weights independently.

The first term \(p/(16d^4)\) also has a direct geometric proof: two rectangles
in diagonally opposite quadrants share a vertex. Either an empty state or
the joining mirror gives one orbit. The joining-mirror case has eight
turning visits and only seven distinct mirrors. Its contribution at \(p=1\)
is independently eight rooted circuits, each of probability \(2^{-7}\).

Commands, run from this folder:

    nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 recheck.py
    nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 repeated.py
    nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 audit_repeated.py
    nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 verify_artifacts.py

PROOF.md supplies every counting and probability step, the complete grouped
table, both exhaustive classification rules, algebra and tail proof.
repeated_data.json stores all 62 corner lists, strip lists and exact
coefficients; repeated_audit.json stores independent counts and rational
tail bounds. recheck.json records the preceding-result verification.
LOG.md records commands, results and corrections.

All scripts use the standard library, one thread, CPU limits of at most
180 seconds and wall alarms of at most ten minutes. Runs took under four seconds each and
under 100 MB peak RSS. Actual nice is 20; macOS rejects the relative nice
adjustment from that inherited priority, and each script checks nice >=15.
No prior folder was edited; no git, subagents, background jobs, shared-state
writes or external publication were used.

The bounded literature search found no later solution. Opened sources were
Martin P. W. Zerner, [*Infinite light rays and infinite clusters with infinitely
many pivots*, arXiv:2610.12460](https://arxiv.org/abs/2610.12460), whose abstract
retains the square-lattice conjecture; Gady Kozma and Vladas Sidoravicius,
[*Lower bound for the escape probability in the Lorentz Mirror Model on the
lattice*, arXiv:1311.7437](https://arxiv.org/abs/1311.7437); and Jian Gu and
Qin Hao, [*Boundary transmission and excursion geometry in the Lorentz mirror
model: a numerical study*, arXiv:2609.14949](https://arxiv.org/abs/2609.14949),
whose abstract leaves localization unresolved. The search ended within five
minutes and was not exhaustive.

What failed or remains uncertain: no discrepancy in the earlier mathematical
result or new computed classification was found. Extending the independent
walk audit to variable roots initially hit a leftover fixed-root assertion;
correcting it made the complete bounded-grid audit pass. A proof transcription
initially omitted one of two equal small-density summands; the table audit
identified it and the displayed sum was corrected.
The document checker initially confused the length-eight count row with a
classification row; distinguishing table headers corrected that checker.
The finite classification depends on the supplied exhaustive computations;
no hand classification of
all 62 circuits or literature novelty is claimed.

This is not a formula for all orbits with at most eight distinct mirrors.
Repeated-vertex orbits with ten or more turning visits and simple orbits with
at least fourteen mirrors remain outside the bound. No upper bound forcing
the infinite-orbit probability to vanish is obtained.

Next worker: extend the compatible-circuit classification to ten turning
visits, using these 62 individual circuits as a regression target. Keep
turning visits and distinct mirrors separate. The arbitrary-gap weight stays
\((p/2)^{k-t}q^{L-k-c}\); do not reuse the simple-polygon weight. Five
horizontal sides still allow only strip weights one and two. Generalize the
local-state grid search for an independent audit, or prune coordinate words
by repeated-edge and local-state consistency before constructing whole
circuits. Further finite enumeration improves the explicit bound; the full
conjecture needs control of unrestricted orbits.

Task: “take the NEXT checkable step on this problem, building on that work” —
received approximately 10:51 Asia/Tbilisi, 15 November 2026.
