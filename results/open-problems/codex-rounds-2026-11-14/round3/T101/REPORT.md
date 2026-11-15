VERDICT: PARTIAL exact probability of vertex-simple periodic orbits with at most eight mirrors

The earlier four/six-mirror result holds. An independent coordinate-rank
enumeration recovers its formula, its coefficient \(3/128\), and its value
\(11/486\) at \(p=1/2\).

The new result is the exact contribution of all vertex-simple periodic orbits
with eight mirrors, with arbitrary positive integer side lengths:

\[
 R_8(p)=\frac{p(1-p)^2[10+23(1-p)^2]}{64(2-p)^7}.
\]

Thus the probability that a fixed directed edge has a vertex-simple periodic
orbit with at most eight mirrors is exactly

\[
 B_8(p)=\frac{p}{8(2-p)^3}
       +\frac{p(1-p)^2}{4(2-p)^5}
       +\frac{p(1-p)^2[10+23(1-p)^2]}{64(2-p)^7}.
\]

This is a lower bound on its periodicity probability. It improves the earlier
bound strictly for every \(0<p<1\). Its small-density coefficient is
\(225/8192\), increased from \(3/128=192/8192\), and
\(B_8(1/2)=95/3888\), increased from \(11/486=88/3888\).
The all-orbit periodicity conjecture remains unresolved.

`PROOF.md` supplies the rooting argument, the complete finite classification
of 38 rank polygons, the summation over all coordinate gaps, and the algebra.
Two independent exhaustive methods verify the classification: 1444 pairs of
cyclic corner-coordinate sequences and all 511 nonempty subsets of a
three-by-three cell box. Their individual polygon lists agree. The unrooted
semiperimeter series simplifies to

\[
 F_8(r)=\frac{2r^5(4+7r)}{(1-r)^6}.
\]

Consequently the rooted perimeter count is

\[
 N_8(2m)=40\binom{m+1}{6}+92\binom m6.
\]

Independent unit-step walks reproduce the earlier targets \(40,372,1764\)
at perimeters \(10,12,14\), and give \(5936,16128,37800\) at \(16,18,20\).
Exact rational shape sums agree at four densities; the endpoint \(p=1\) is
checked separately. Independent binomial-series sums agree at all five
densities, with rigorous omitted tails smaller than \(10^{-30}\). The linear
coefficient is also checked from the separate gap-family singularities.
All runs used one thread, inherited nice 20, under 18 MB reported peak RAM,
and less than one second per run. The `nice` warning reflects an attempted
relative priority change from an already lower priority; no priority increase
was made.

Commands, from this folder:

```sh
nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 eight_corners.py --stage earlier --max-length 16 --output earlier_recheck.json
nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 eight_corners.py --stage eight --max-length 20 --output eight_data.json
nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 audit_cells.py
```

`LOG.md` records commands and output; the three JSON files retain exact data.
Scripts use only the standard library and impose 180-second CPU limits.

The literature check, limited to less than five minutes, found no later
solution. Opened sources were Martin P.W. Zerner,
[*Infinite light rays and infinite clusters with infinitely many pivots*,
arXiv:2610.12460v1](https://arxiv.org/html/2610.12460v1), which retains the
square-lattice conjecture; Gady Kozma and Vladas Sidoravicius,
[*Lower bound for the escape probability in the Lorentz Mirror Model on the
lattice*, arXiv:1311.7437](https://arxiv.org/abs/1311.7437); and Jian Gu and
Qin Hao, [*Boundary transmission and excursion geometry in the Lorentz mirror
model: a numerical study*, arXiv:2609.14949](https://arxiv.org/abs/2609.14949),
which does not resolve infinite-plane localization.

What failed or remains uncertain: no mathematical discrepancy was found in the
earlier result or this extension. The finite classification relies on the
explicit exhaustive calculations, with both implementations and the full table
provided for inspection. No novelty claim is made for this restricted-family
enumeration. The result excludes vertex-simple orbits with ten or more mirrors
and every orbit with repeated vertices. It gives no estimate forcing the
infinite-orbit probability to vanish. The bounded literature search is not an
exhaustive review.

Next worker: extend the rank/cell calculation to ten-corner simple polygons.
They fit in a four-by-four cell box, so 65,535 nonempty cell subsets suffice
for an independent exhaustive classification. Generalize the hardcoded box
and corner count, sum the coordinate gaps, and compare rooted unit-walk
coefficients. This would further improve the explicit bound; localization
still requires control of unrestricted orbit geometry.

Task: “take the NEXT checkable step on this problem, building on that work” —
received approximately 01:28 Asia/Tbilisi, 15 November 2026.
