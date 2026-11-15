VERDICT: PARTIAL exact probability of vertex-simple periodic orbits with at most six mirrors

For a fixed directed lattice edge, the probability that its orbit is vertex-simple, periodic, and contains at most six mirrors is

\[
 B(p)=\frac{p}{8(2-p)^3}+\frac{p(1-p)^2}{4(2-p)^5}
 =\frac{p(6-8p+3p^2)}{8(2-p)^5}.
\]

The two terms count all rectangles and all L-shaped orthogonal hexagons, respectively, over arbitrary positive side lengths. Thus the probability of a periodic orbit is at least B(p). In particular its liminf after division by p, as p decreases to zero, is at least 3/128. At p=1/2 the bound is 11/486. The full almost-sure periodicity conjecture remains unresolved.

`PROOF.md` gives the shape classification, exact probability of each prescribed boundary, disjointness of rooted-orbit events, translation counts, series evaluations, and a second derivation by perimeter. No novelty claim is made for this elementary restricted-family bound.

Verification command, run from this folder:

```sh
nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 audit.py --max-length 14 --output audit_data.json
```

The independent walk enumeration gives four-turn counts 2, 6, 12, 20, 30, 42 at perimeters 4 through 14, and six-turn counts 0, 0, 16, 80, 240, 560. These agree with m(m-1) and 16 binom(m,4), where the perimeter is 2m. An independent reflection-table tracer exhausts all 19,683 environments in a three-by-three box and agrees with the geometric calculation at three rational densities. Five exact rational series checks bound the omitted tails below 10^-25. The final run used about 17.5 MB and 0.065 seconds, one thread, inherited nice 20. The `nice` warning is explained in `LOG.md`. Exact tail bounds are stored alongside decimal approximations, which can underflow to zero.

The bounded literature search found no solution or substantial advance for the stated square-lattice model. Opened sources include Gady Kozma and Vladas Sidoravicius, [arXiv:1311.7437](https://arxiv.org/abs/1311.7437); Martin P. W. Zerner, [arXiv:2610.12460](https://arxiv.org/html/2610.12460v1); and Jian Gu and Qin Hao, [arXiv:2609.14949](https://arxiv.org/html/2609.14949v1). Zerner's introduction explicitly retains the conjecture. Additional opened leads concerned a hierarchical model, loop weight 2, or the Manhattan lattice; references and search details are in `LOG.md`. This was a short search, not an exhaustive literature review.

What failed or remains uncertain: the search did not yield a proof of localization. No attempted mathematical claim failed its audit, but the initial decimal-only representation of tiny tail bounds was insufficient and was corrected. The formula omits simple orbits with eight or more mirrors and every orbit that repeats a vertex. The enumeration already finds 40 eight-turn simple polygons of perimeter 10; each has positive probability for 0<p<1, so B(p) is strictly smaller than the full periodicity probability. The result supplies no estimate forcing the probability of an infinite orbit to vanish.

Next work: derive and sum the eight-corner family, using the independent counts 40, 372, 1764 at perimeters 10, 12, 14 as audit targets. Such an extension would improve this explicit lower bound, but a solution of T101 still needs control of unrestricted orbit geometry. Do not identify vertex-simple polygons with all mirror trajectories.

Task: “push this problem forward by one checkable piece” — received approximately 21:58 Asia/Tbilisi, 14 November 2026.
