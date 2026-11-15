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
