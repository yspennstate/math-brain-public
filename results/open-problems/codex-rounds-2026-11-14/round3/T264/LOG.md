# T264 work log

Task: "take the NEXT checkable step on this problem, building on that work". Start: 2026-11-15 03:38 +04 (2026-11-14 23:38 UTC).

## Orientation and bounded literature check

Read the previous worker's REPORT.md, LOG.md, PROOF.md and all of verify_two_point.py, without editing that folder. Read startup memory, brain index, and compute state. The state is warn / owner_away_open, CPU saturated; computation here will be small, standard-library where possible, one thread and nice >=15. No subagents, git, or external writes. The current folder-only order supersedes the general brain/checklist/mesh instructions: those commands mutate outside this folder and were not run.

Within the first five minutes, searched the web tool for fixed-dimension minimum-norm ReLU noisy interpolation and recent tempered-overfitting results. Opened:

- Junhyung Park, Patrick Bloebaum, Shiva Prasad Kasiviswanathan, *Benign Overfitting for Regression with Trained Two-Layer ReLU Networks*, arXiv:2410.06191, https://arxiv.org/abs/2410.06191 . No revision after the earlier report; NTK setting, previously checked growing-dimension condition.
- Ouns El Harzli, Yoonsoo Nam, Ilja Kuzborskij, Bernardo Cuenca Grau, Ard A. Louis, *Sufficient Conditions for Stability of Minimum-Norm Interpolating Deep ReLU Networks*, arXiv:2602.13910, https://arxiv.org/abs/2602.13910 . Conditional stability, not a resolution of the requested general limit; no revision after the earlier report.
- Nirmit Joshi, Gal Vardi, Nathan Srebro, *Noisy Interpolation Learning with Shallow Univariate ReLU Networks*, arXiv:2307.15396, https://arxiv.org/abs/2307.15396 . Univariate and loss-dependent, as stated in the task.
- Weizhao Li, Lei Shi, Hanfei Zhou, *Minimum-Norm Interpolation in Weighted Variation Spaces: Direct and Inverse Problems*, arXiv:2611.01105, https://arxiv.org/abs/2611.01105 . The target belongs to the variation space; not noisy-label asymptotics.
- Etienne Boursier, Nicolas Flammarion, *Simplicity bias and optimization threshold in two-layer ReLU networks*, arXiv:2410.02348, https://arxiv.org/abs/2410.02348 . Studies failure to interpolate beyond an optimization threshold, not the risk of interpolating solutions.

No new whole-problem solution found. This bounded search cannot establish absence; no SOLVED_ELSEWHERE.md is justified.

## Independent re-check of the earlier claim

With x1=(a,b), x2=(a,-b), a=cos(theta/2), b=sin(theta/2), the candidate atoms are u=(b,a), v=(b,-a). Their sample vectors are (2ab,0),(0,2ab), so coefficients +1/(2ab),-1/(2ab) interpolate. The maximum absolute atom difference is 2ab for theta<pi/2 (separate the activation cones); hence dual multipliers (+1/(2ab),-1/(2ab)) certify cost 1/(ab). Equality exposes only these two atoms, so this also checks uniqueness.

Independently expanding sigma(t)=(t+|t|)/2 gives odd component x_2/(2b). Its squared spherical norm is 1/(4*d*b^2). The even part is bounded by |x_1|/(2a) pointwise, hence its squared norm is at most 1/(4*d*a^2). Odd and even parts are orthogonal. Therefore R=1/(4*d*b^2)+O(1), recovering the earlier leading coefficient 1/d independently of its kernel integration. Integrating theta^(d-2-2q) at zero recovers q<(d-1)/2. The main claim holds. A fresh script below will independently integrate the actual two-atom function and check the exact expression.

## Choice of one extension (before implementation)

Solve the homogeneous three-constraint atomic problem for the symmetric close pair x1=(a,b), x2=(a,-b), labels (1,-1), and x3=e2 at a fixed angle near pi/2, with bounded label tau in {-1,+1}. Work in their plane, embedded in any d>=2. This is the previous report's suggested next step, in a case where the old interpolant predicts 1/(2b) at x3 and must change substantially. Determine exact cost/optimizers if possible, and whether the leading global odd component survives. No inference about n tending to infinity will be made.

## Exploratory computation and candidate formulas

Created explore_three.py (8192 planar directions, only 3 dual variables) and ran:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 explore_three.py > exploration_output.txt
```

Exit 0, 1.17 seconds, peak RSS 112,656,384 bytes. Nice inherited 20; the sandbox denied nice's attempted priority adjustment. The LP used one HiGHS thread. NumPy emitted unexpected floating-point warnings at its small matrix product, although all resulting LPs succeeded; this exploratory code will not be used for verification. A fresh standard-library-only analytic certificate and scalar quadrature will check all results. The angular grid splits an interior exposed atom between neighbors and slightly misses the kink atom, so these numbers are approximate only.

At theta=.1 the grid gave cost 22.04769847 for tau=-1, using +x1, -v and -(-v), where v=(b,-a). For tau=+1 it gave 20.42104885, using a positive first-quadrant atom and -v. This suggests the following exact formulas (proved and independently checked next):

- tau=+1: W=((1-b)/a,1), L=||W||=sqrt(2/(1+b)), C=(1-b)/(ab); f=sigma(W dot x)-C*sigma(v dot x), Q=L+C. Dual (1/s+L/2,-1/s,L/2-1/a), s=2ab.
- tau=-1: C=a/b, D=(1+b)/a; f=sigma(x1 dot x)-C*sigma(v dot x)-D*sigma(-v dot x), Q=1+C+D=1+1/(ab)+1/a. Dual (1+1/s,-1/s,-1/a).

For both labels, as theta tends to zero, theta*f converges uniformly on the unit sphere to -2*sigma(-x_2). Thus theta^2*R tends to 2/d, twice the two-observation coefficient. The old odd component is not canceled at leading order; the even component becomes equally large. The theta restriction 0<theta<pi/3 ensures that W is active at x2. Endpoint/out-of-range cases must be checked rather than extrapolated.

## Proof completed before final numerical audit

Wrote PROOF.md with explicit dual certificates and every activation region checked. Equality exposes exactly two atoms for tau=+1 and exactly three for tau=-1, proving uniqueness as a function and validity in all ambient d>=2. Domain: 0<theta<pi/3. No biases or free skip/intercept.

The negative-label cost simplifies to 1+1/(ab)+1/a. Exact risk: [1+(a/b)^2+((1+b)/a)^2]/(2d)-[a/b+(1+b)/a]/(pi*d). For the positive label the two-atom kernel formula is given in the proof. The asymptotic coefficient 2/d follows both from those formulas and from uniform convergence of theta*f to -2*sigma(-x_2). The odd-part coefficient is 1/d by a separate exact vector-sum computation.

Next audit: scalar direct integration, exact continuous pricing by independently enumerating activation arcs and stationary points, recovering dual multipliers from their exposed-atom equations, angle boundary checks, and a deliberately out-of-domain example.

## Independent verification passed

Created verify_three_point.py using only the standard library. Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_three_point.py > verification_output.txt
```

Exit 0. Resource report: 2.3183 seconds, peak RSS 15,204,352 bytes, nice 20, OMP_NUM_THREADS=1. The only stderr was the sandbox denying nice's attempted adjustment; inherited nice 20 satisfies the requirement. Full output is saved in verification_output.txt, and per-case data in verification_data.json.

```text
PASS: earlier exact two-point risk, independent scalar integration
theta=0.0001 tau=+1 Q=20000.4142115 theta^2*R2=0.999893179732 theta^2*oddR2=0.500000000417
theta=0.0001 tau=-1 Q=20002.0000333 theta^2*R2=0.999968170753 theta^2*oddR2=0.499949999167
theta=0.03 tau=+1 Q=67.0802804079 theta^2*R2=0.968901216614 theta^2*oddR2=0.500037501688
theta=0.03 tau=-1 Q=68.6767802273 theta^2*R2=0.990612871233 theta^2*oddR2=0.484927865438
theta=0.2 tau=+1 Q=10.4104600139 theta^2*R2=0.82528593652 theta^2*oddR2=0.501670005298
theta=0.2 tau=-1 Q=12.0720000137 theta^2*R2=0.945071579021 theta^2*oddR2=0.397612198889
theta=1 tau=+1 Q=2.39999834474 theta^2*R2=0.644720003979 theta^2*oddR2=0.543835662418
theta=1 tau=-1 Q=4.51628413888 theta^2*R2=1.23851471236 theta^2*oddR2=0.127616946701
PASS: interpolation, recovered multipliers, primal=dual, continuous pricing (max error 9.74e-13)
PASS: independent circle risk vs closed and kernel formulas (max relative error 3.95e-10)
PASS: S^2 direct surface integral 15.7513149432, formula 15.7511929854
PASS: out-of-domain theta=1.2 candidate fails interpolation by 0.12928494679; restriction is necessary for this formula
All assertions passed.
```

Continuous pricing is exhaustive over activation arcs, including boundaries and all interior stationary points. It is not a direction grid. Multipliers are separately recovered by solving their exposed-atom equations. The earlier exact risk is integrated independently for six acute/obtuse angles, including the right-angle junction. Fourteen new cases cover both third labels and angles from 1e-4 to just below pi/3.

## Attempt to break the result

1. Re-derived both costs from interpolation coefficients and independently from dual objective values. Recovered each dual from linear equations instead of its closed formula.
2. Used an activation-arc price calculation independent of the proof's inequalities; it checks the entire planar unit circle, with maximum deviation from price one below 9.74e-13. Off-plane atoms cannot improve the price because projecting into the sample plane scales all responses by a norm at most one.
3. Checked exact risks three ways: pairwise atom-product formula, simplified closed formulas, and direct scalar circle integration. A separate S^2 surface integration checked the ambient 1/d normalization.
4. Re-derived 2/d from uniform function convergence, from the leading quadratic coefficient in the exact risk, and from odd/even decomposition. The odd component alone still contributes 1/d, so this result does not rely on an accidental cancellation in a kernel expression.
5. Checked width and optimizer selection: equality in the dual certificates forces the exposed atoms; triangular interpolation equations fix coefficient totals. Splitting or repeating units cannot change the resulting function. At least two units are required for the stated positive-label construction and three are allowed for the negative-label theorem; no negative-label width-two assertion is made.
6. Tried extrapolating the positive-label formula beyond its domain. At theta=1.2 it misses the second label by 0.12928494679 because W dot x2 becomes negative. The condition theta<pi/3 is substantive. Endpoint uniqueness is not claimed.
7. The third-point family is deterministic and measure zero under iid continuous designs. There is no conclusion about the risk distribution for random triples, arbitrary n, biases, or GD. The n-to-infinity problem remains open in this report.

The exploratory NumPy/LP warnings and discretization errors did not enter the proof or final verification. All final checks use scalar standard-library arithmetic and exact continuous activation-arc pricing.

## Completion

Audited the final statements against the explicit atom sample-value matrices, the exact dual prices, the independent verification output, and the stated angle/width/model restrictions. REPORT.md records the new theorem, failed extrapolation, reproduction command, limitations, and next checkable step. PROOF.md and verify_three_point.py are self-contained. Only this folder was written; the previous worker's folder was read only. The large-sample T264 question is unresolved.

Task: T264, "take the NEXT checkable step on this problem, building on that work" — 2026-11-15 03:38 +04.
