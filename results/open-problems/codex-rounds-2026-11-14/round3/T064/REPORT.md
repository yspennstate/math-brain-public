VERDICT: PROVED explicit finite-scale level-stability bound for random-plane-wave rectangle crossings

The earlier report holds: nonzero levels are understood, while the
Cardy/SLE(6) conjecture remains open in the sources checked. No later
solution was found in the five-minute literature check. The old folder
contains no PROOF.md or scripts; its existing files were read and left
untouched.

New beyond that report: an explicit bound uniform in the level and
rectangle dimensions. Let p_Q(u) be the left-to-right crossing probability
of {f>=u} in a rectangle of area A and perimeter P, with covariance
J_0(|x-y|). For delta=|u|<=1,

    |p_Q(u)-p_Q(0)|
      <= delta/sqrt(2*pi)
         * [A/(4*pi) + P/(2*pi)*(1+delta^2/3) + 4].

PROOF.md also gives the stronger exact bound for every pair of levels,
with closed-form integrals. It follows that levels u_R=o(R^(-2)) leave
fixed-aspect-ratio crossing probabilities unchanged up to o(1). For
squares, the crossing probability therefore tends to 1/2 at these levels.
The proof counts stratified critical values using Kac–Rice and includes
edge and corner terms. This is a derived quantitative lemma; no claim of
literature priority is made.

The proof and independent audits are in [PROOF.md](PROOF.md). The numerical
audit [check_level_stability.py](check_level_stability.py) checks the
conditional Gaussian expectations by direct quadrature, integrates the
height densities, and recovers the spectral moments independently.
Interior intensity is 0.091888149237 per unit area, agreeing with
Proposition 1.1 of Dmitry Beliaev, Valentina Cammarota and Igor Wigman,
*Two point function for critical points of a random plane wave*,
[arXiv:1704.04943](https://arxiv.org/abs/1704.04943).

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_level_stability.py
```

The first run passed in 0.075 seconds with 12.64 MiB peak RSS and verified
inherited niceness 20. Full output and the final rerun are in
[LOG.md](LOG.md). The numerical checks support the algebra; the proof
does not depend on numerical quadrature.

What failed or remains uncertain: rectangular threshold delocalisation
in Proposition 2.15 of Stephen Muirhead, Alejandro Rivera and Hugo
Vanneuville, with an appendix by Laurin Köhler-Schindler,
*The phase transition for planar Gaussian percolation models without FKG*,
[arXiv:2010.11770v3](https://arxiv.org/abs/2010.11770v3), is qualitative.
It does not justify an explicit logarithmic window for rectangles. The
bound proved here removes only o(R^(-2)) sprinkling; it gives no RSW for
nonsquares, critical exponent, or conformal limit. A short search cannot
certify exhaustive literature novelty. The sandbox denied ps and nice
reported a priority-change warning; the script independently confirmed
that the actual priority already meets the author's requirement.

Next worker: replace the count of all critical points by a Kac–Rice count
weighted by crossing pivotality. The first missing input is a quantitative
conditional four-arm estimate for an interior saddle near level zero,
with the corresponding boundary-arm estimates. Improving that step
would enlarge the level range in which sprinkling can be removed.

Task: “take the NEXT checkable step on this problem, building on that
work” — 15 November 2026, approximately 01:08 Asia/Tbilisi.
