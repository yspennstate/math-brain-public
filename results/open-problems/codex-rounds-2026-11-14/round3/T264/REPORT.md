VERDICT: PROVED Exact three-constraint minimum-norm ReLU interpolants with risk coefficient 2/d.

The earlier two-point result holds. Independent odd/even decomposition recovers its singular risk coefficient 1/d, and fresh direct integration checks its exact risk formula at acute and obtuse angles.

The new result solves the next suggested three-constraint problem for a specific third-point geometry in every ambient dimension d>=2. Put a=cos(theta/2), b=sin(theta/2), 0<theta<pi/3, and

```text
x1=(a,b), x2=(a,-b), x3=(0,1), labels=(1,-1,tau), tau in {-1,+1}.
```

The points lie in a plane embedded in R^d. The norm is one half the sum of squared parameters of both layers, with no biases, skip, or intercept. Width is unrestricted. Explicit dual certificates prove uniqueness as a function, including when ambient directions outside the plane are allowed.

Writing v=(b,-a), the exact solutions are:

- tau=+1: W=((1-b)/a,1), L=sqrt(2/(1+b)), C=(1-b)/(ab). The function is sigma(W dot x)-C*sigma(v dot x), with minimum cost L+C. Two units suffice.
- tau=-1: C=a/b, D=(1+b)/a. The function is sigma(x1 dot x)-C*sigma(v dot x)-D*sigma(-v dot x), with minimum cost 1+1/(ab)+1/a. Three units suffice.

For either third label, theta*f converges uniformly on the unit sphere to -2*sigma(-x_2). Therefore its conditional squared excess risk against the zero regression function satisfies

```text
lim(theta -> 0) theta^2 * R_d(theta) = 2/d.
```

The old odd linear component survives with leading risk coefficient 1/d. An even component contributes another 1/d. Thus this additional interpolation constraint doubles the leading risk coefficient, rather than removing the close-pair divergence. Exact finite-angle risks and every dual-feasibility/equality step are in PROOF.md.

Reproduce from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_three_point.py > verification_output.txt
```

All assertions passed in 2.32 seconds, peak RSS 15,204,352 bytes, one thread, actual nice 20. The sandbox denied nice's attempted priority adjustment; inherited priority already satisfied the requirement. Independent direct circle integration agrees with the new exact risks to 3.95e-10 relative error. Exhaustive continuous dual pricing, separately recovered dual multipliers, interpolation, primal/dual equality, an S^2 surface integral, and odd-part coefficients all passed. Full commands, output, and audit are in LOG.md; per-case data are in verification_data.json.

What failed: the preliminary angular-grid LP only approximates kink atoms and emitted NumPy floating-point warnings. It supplied candidates, and none of its numerical values is needed for the theorem. The final proof and verification use no NumPy or optimizer. Deliberately extending the positive-label formula to theta=1.2 fails interpolation by 0.12928494679; the stated angle restriction is necessary for that formula.

The bounded literature check found no later resolution; opened sources and their scope are recorded in LOG.md. No SOLVED_ELSEWHERE.md was warranted.

What remains uncertain: random-triple risk, stability under perturbing the third point out of this geometry, additional interpolation constraints, penalized biases, and GD selection. This deterministic three-point family has probability zero under iid continuous inputs. It supplies no classification of the n-to-infinity risk limit and no new risk-moment assertion for random samples. No novelty claim is made for the elementary atomic calculation.

The next worker should perturb x3 to a general point at a fixed nonzero angle, including an out-of-plane component when d>=3. Prove or refute a uniform lower bound R>=c/theta^2 on an open set of third-point locations for bounded third labels. A positive-measure version is needed before inferring anything about training-averaged risk for random triples. The explicit certificates here give a starting point, but their kink equalities mean robustness cannot simply be assumed.

Task: T264, "take the NEXT checkable step on this problem, building on that work" — 2026-11-15 03:38 +04.
