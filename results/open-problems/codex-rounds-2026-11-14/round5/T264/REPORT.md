VERDICT: PROVED Infinite high-order risk moments at every fixed sample size for homogeneous minimum-norm ReLU interpolation on the sphere.

The earlier three-observation result holds. An independent re-derivation of
the mass-localization estimate and a fresh numerical audit confirm its risk
coefficient 2/d. Direct circle integration agrees with the earlier exact
special-case risks to 1.03e-9 relative error; 9,000 signed atom directions
also pass the localization inequality.

The new result extends the close-pair mechanism to any fixed number n>=3 of
observations. If the other n-2 distinct points all lie in one separation
hemisphere, bounded-cost corrections can vanish at both members of the close
pair. Every minimum-parameter-norm interpolant therefore satisfies

```text
theta f_theta(x) -> -2 epsilon sigma(-epsilon e2 dot x),
theta^2 R(f_theta) -> 2/d,
```

uniformly on the unit ball and over bounded labels. Here the close pair is
cos(theta/2)e1 +/- sin(theta/2)e2 with labels (1,-1), and epsilon is the common
sign of the other points' e2-coordinates. The convergence is uniform on compact
sets with positive cap distance and positive separation among the extra points.

The model is homogeneous two-layer ReLU regression, with objective one half
the sum of squared parameters in both layers. There are no biases, skips, or
output intercepts. Width is unrestricted, or fixed at any value m>=n.
The assertion covers every minimizer and permits off-plane inputs and weights.

Consequently, for n iid uniform inputs on S^(d-1) with independent Rademacher
labels and zero regression function, every measurable minimum-norm selection
has conditional squared excess risk R_n satisfying

```text
E[R_n^r] = infinity for every n>=3 and r >= (d-1)/2.

liminf(t -> infinity) t^((d-1)/2) P(R_n>t)
  >= 2^(2-n) C_d/(d-1) * (2/d)^((d-1)/2),
C_d = Gamma(d/2)/(sqrt(pi)*Gamma((d-1)/2)).
```

In particular, E[R_n]=infinity for every n>=3 in d=2 and d=3. The expected-risk
sequence thus has extended-real limit infinity in this precise model. Unlike
the predecessor's n=3 result alone, this establishes an expected large-sample
conclusion. It does not establish divergence in probability: the hemisphere
event used in the proof has probability 2^(3-n), which decreases to zero.
For d>=4 the mean-risk question remains open here. No matching upper tail or
finiteness of lower-order moments is proved.

The missing correction lemma is proved in PROOF.md: atom directions with
u dot e1<0 span arbitrary responses on distinct points in the positive
separation hemisphere. Each point's activation hyperplane meets this open
cone, so derivative jumps rule out any nonzero linear relation. Choose n-2
independent atoms; their response matrix inverse gives bounded corrections,
and their negative first coordinates make them vanish at both close samples
for small theta. Two base atoms plus these corrections give cost
2/sin(theta)+O(1). A compactness argument supplies the uniform constants needed
for the random-sample conclusion. On the full-measure subset of distinct
projected ratios, a separate explicit triangular construction proves the
same interpolation claim.

Reproduce from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_finite_n.py --prior-only > prior_output.txt
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_finite_n.py > verification_output.txt
```

Both commands passed. The full verifier checks 78 feasible networks in d=2,3,7
and n=3,4,5,6,10, both hemisphere signs, bounded labels and three angles. These
are explicit competitors, not computed minimizers. Maximum interpolation error
is 1.07e-13. A tied-projected-ratio example uses off-plane correction directions;
independent circle and S^2 integration check risk normalization. Sign enumeration
and spherical-cap integration separately check all tail factors for n=3..10,
d=2..7. The moment endpoint is checked by both angular and tail integration.
The full run took 0.626 seconds and 17,367,040 bytes peak RSS, one thread,
actual nice 20. Per-case data are in verification_data.json; LOG.md records
the commands, output, literature check and mathematical audits.

What failed or cannot be extended directly: duplicated points do not support
arbitrary labels, and projected-ratio ties defeat the triangular construction.
The general correction lemma covers distinct tied-ratio points, and a separate
numerical example verifies that case. Extra points in opposite separation
hemispheres contradict the sharp 2/sin(theta)+O(1) cost premise: localization
would force both limiting signed masses to zero although their sum tends to 2.
Their optimal leading cost and risk are not determined here. No mathematical
verification failed. The shell denied nice's attempted priority adjustment;
the script verified compliant inherited nice 20 before computing. An attempted
log patch had a context mismatch and was corrected without changing any result.

The literature check ended within five minutes and found no later full
resolution. The opened primary sources, exact author names and scope checks
are listed in LOG.md. No SOLVED_ELSEWHERE.md was warranted. This is a result
relative to the predecessor reports; no broader novelty claim is made.

Remaining uncertainty: conditional-risk convergence in probability, expected
risk in d>=4, lower-order moment finiteness, sharp tail constants, penalized
biases, full-dimensional homoscedastic designs, and GD selection. The constants
in the correction construction need not stay bounded as n increases.

Next worker: study a fourth point in the opposite separation hemisphere.
First take extras z=e2 and z'=-e2, both with bounded labels, and determine the
leading minimum cost and scaled-risk profile as theta decreases to zero.
The old sharp-cost premise is now provably impossible; a different limiting
atomic optimization is needed. This geometry occurs in typical large samples,
whereas putting every extra point in one hemisphere becomes exponentially rare.
Do not infer typical-risk behavior from the infinite expectations proved here.

Task: T264, "take the NEXT checkable step on this problem, building on that work" — 2026-11-15 08:58 +04.
