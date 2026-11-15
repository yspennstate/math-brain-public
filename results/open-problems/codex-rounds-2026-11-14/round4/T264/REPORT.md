VERDICT: PROVED Uniform open-set three-point risk coefficient 2/d and divergent random-triple risk moments of orders at least (d-1)/2.

The earlier exact three-point result holds. A separate piecewise-antiderivative integration of the actual networks agrees with its finite-angle risks to 3.33e-16 relative error; the singular coefficient is also recovered directly from the dominant atom.

The new theorem replaces the earlier single third-point location by an open set of positive surface measure. Write

```text
x1 = cos(theta/2)e1 + sin(theta/2)e2,
x2 = cos(theta/2)e1 - sin(theta/2)e2,
labels = (1,-1,tau).
```

For any fixed delta>0 and H<infinity, every minimum-parameter-norm homogeneous two-layer ReLU interpolant satisfies, uniformly over unit third points z with |z dot e2|>=delta and labels |tau|<=H,

```text
theta f(x) -> -2 sign(z dot e2) sigma(-sign(z dot e2) e2 dot x)
theta^2 R -> 2/d.
```

The function limit is uniform on the unit ball, with an explicit O(sqrt(theta)) error bound. The risk uses an independent uniform test point on S^{d-1} and zero regression function. Off-plane third points and weights are allowed. The norm is one half the sum of squared parameters in both layers, with no biases, skip, or intercept. Width is unrestricted or fixed at any value at least three. The theorem covers every minimizer and does not need uniqueness.

The proof constructs a three-unit competitor with cost at most 2/sin(theta)+K(delta,H). A quantitative signed-atom inequality then forces the scaled network close to A sigma(e2 dot x)-B sigma(-e2 dot x), with A+B tending to 2. The bounded third response removes one of these coefficients. All inequalities and the explicit error bound are in PROOF.md.

For three iid uniform spherical inputs with independent Rademacher label noise, this yields

```text
E[R^r] = infinity for every r >= (d-1)/2.
```

In particular, training-averaged squared excess risk is infinite at sample size three in d=2 and d=3. There is also the lower-tail bound

```text
liminf(t -> infinity) t^((d-1)/2) P(R>t)
  >= C_d/[2(d-1)] * (2/d)^((d-1)/2),
C_d = Gamma(d/2)/(sqrt(pi)*Gamma((d-1)/2)).
```

This uses only one designated close pair. It is a lower bound, not an exact tail asymptotic or a converse moment-finiteness claim. Unlike the earlier deterministic family, the third-point event here has positive probability.

The fixed-delta restriction cannot be removed uniformly. For z_theta=(-cos(3theta/2),sin(3theta/2)), third label +1, the old two-point minimum already interpolates the third point and remains optimal. Its risk coefficient is 1/d, while z_theta dot e2 tends to zero. Section 7 proves this counterexample, including the dual lower bound.

Reproduce from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 recheck_earlier.py > recheck_output.txt
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_robust.py > verification_output.txt
```

Both passed. The new verifier checks 18,102 signed atom directions, 162 explicit feasible networks with off-plane perturbations in d=2,3,7, both cap signs, and three bounded labels. Those networks satisfy the theorem's cost bound; they are not computed minimizers. Maximum interpolation error was 4.44e-16. A separate S^2 surface integral checks the risk normalization. Tail constants and the endpoint exponent have independent checks. The verifier took 0.2875 seconds, used 16,285,696 bytes peak RSS, one thread, and actual nice 20. Per-case data are in verification_data.json.

What failed: the environment rejected both address-space and data-heap rlimit settings before computation. The final script uses bounded small lists, CPU/wall limits, and a peak-RSS assertion. The nice command also reported a denied priority adjustment, while the script verified inherited nice 20. No mathematical assertion failed. Extending the coefficient uniformly to vanishing third coordinate was refuted by the exact counterexample above.

The literature check stayed within five minutes and found no later resolution. Opened sources, exact author names, links, and scope are recorded in LOG.md. No SOLVED_ELSEWHERE.md was warranted. No novelty claim is made beyond what this session proves relative to the predecessor reports.

What remains uncertain: finiteness of lower-order random-triple risk moments; the true random-triple tail constant; the transition near z dot e2=0; additional constraints; penalized biases; full-dimensional homoscedastic designs; and GD selection. This is a finite-sample theorem. It does not classify the n-to-infinity risk limit, in expectation or probability.

The next worker should test a fourth observation. First put both extra points in the same separation hemisphere and construct a bounded-cost correction vanishing at the close pair, aiming for cost 2/sin(theta)+O(1) on an open set. The mass-localization argument here would then apply directly. Extra points in opposite hemispheres present a different obstruction: the two bounded responses would force both limiting coefficients to vanish, incompatible with their sum tending to 2. The near-minimal-cost premise must then change. Do not infer a large-sample limit from any fixed-sample infinite moment.

Task: T264, "take the NEXT checkable step on this problem, building on that work" — 2026-11-15 05:15 +04.
