# Checks and limits

The previous interpolation theorem holds under independent re-derivation
and the new recheck.py. Earlier scripts were read but never executed in
their folders; all new output was written here.

The load-bearing lower bound in Theorem 1 was checked from two views:
local gradient jumps force each hyperplane's coefficient, while the
distance term has a support-function certificate. For 72 planar cases,
an independent rational convex-hull and edge-projection calculation
checks the distance. For 180 cases, rational attaining representations
match rational lower certificates exactly. Cases in dimension three
include v outside the span of the normals.

For the finite-sample comparison, the exact integers 144 and 81 avoid
all floating-point issues. The stronger intrinsic norms were computed
three ways: the displayed formula, the norms of exact gradient jumps,
and the path cost of a baseline-absorbing network. Both networks
interpolate the sample by exact rational arithmetic.

Attempts to overextend the result:

- Simply adding the baseline's linear norm overcounts: existing pairs
  can absorb a linear part. The explicit example x_1+|x_1|=2 rho(x_1)
  is included in audit.py.
- Summing absolute coefficients before merging coincident hyperplanes
  is false. The theorem requires distinct unoriented normals. Both
  identical and opposite duplicate inputs are rejected in the audit.
- Allowing extra neuron directions does not invalidate the lower
  bound: every extra hyperplane must have zero net kink, and its linear
  contribution obeys the triangle inequality used in the proof.
- Narrowing the cones increases the correction norm, but the full
  score has an additional distance term. Only the proved lower/upper
  comparison is used; monotonicity of that distance term is not claimed.
- The result is about intrinsic path norm with real weights and no
  biases. Fixed output weights, affine neurons, infinite-measure
  representations, and other norms are outside its stated scope.
- The positive-probability sample example has n=d=2. It is not an
  asymptotic theorem about random samples with n/d tending to infinity.
- A global margin optimum and a margin KKT point are different
  selection statements. The intrinsic-norm comparison excludes global
  optimality of the specified narrow score. Proposition 4 additionally
  excludes KKT stationarity of the displayed conical realization and
  its positive neuron rescalings. Other representations of the same
  score are not excluded, and GD's limit is not characterized.
- The wider comparator need not have better population risk. A norm
  comparison alone provides no generalization conclusion.

Both programs enforce one-thread environment and inherited niceness
at least 15, with 60-second CPU/wall limits. Observed RSS was below
17 MB and each run finished below one second. The shell's attempted
nice adjustment was denied, but actual niceness was 20 before either
program computed. No heavy jobs, external writes, git, or subagents
were used. No failed run or unresolved contradiction remains.

The local KKT refinement was checked in ten feasible-descent cases,
including negative first coordinates, a gap-limited width, and dimension
three. The tangent calculation uses rational logarithmic derivatives of
the balancing factors, avoiding numerical differentiation. All 78
sample/subgradient checks give exactly zero score derivative; at each
zero preactivation the weight tangent is individually orthogonal to
the input, so independent choices of derivatives in [0,1] are covered.
The parameter-objective derivative is negative and agrees with direct
differentiation of (15). Twenty-six widened sample scores remain exact.
