# T067-UNIVERSAL-FUSION-001 v1

Status: proof (unaudited), an algorithmic finite-depth upper-bound statement.
No new degree or infinite-depth theorem is asserted here.

## Statement and conventions

Let the root be uniform on three colors. Let d>=2 be an integer, let
0<=eta<=1 be rational, let N be a positive multiple of3, and let the
integer mass scale be S=2^b. An S3-invariant posterior law is stored as
orbit masses on the grid {k/N:k_i>=0,sum k_i=N}. Each orbit mass is spread
uniformly over its distinct coordinate permutations.

Start from the pure posterior law (the root color is known). At each depth:
(i) apply p -> (1,1,1)/3+eta(p-(1,1,1)/3), barycentrically split onto the
grid, then round each orbit mass down to a multiple of1/S and replace all
removed mass by the pure law; (ii) combine d fresh conditionally independent
copies of this experiment using a binary grouping, with the same splitting
and mass upgrade after each combination. Then the resulting experiment
Blackwell-dominates fully observed leaves of the symmetric ferromagnetic
three-state Potts broadcast process at that depth on the d-ary tree.
Consequently its second moment E sum_i(p_i-1/3)^2 is an upper bound for
the actual finite-depth posterior second moment.

The unit-strength fusion matrix is independent of eta and d, includes
boundary laws with zero components, and has integer coefficients with
common denominator108N^2. The physical edge matrix has integer coefficients
with common denominator3B, where eta=A/B in lowest terms.

The code currently restricts N<=96, 1<=b<=40, d<=1000 and checks both
S^2(108N^2)<2^128 and S(3B)<2^64. The abstract statement has no such
machine-size restriction when arbitrary exact integers are used.

## 1. Posterior experiments and the physical edge

For any observation Y with posterior p, calibration gives
P(Y in dy|root=i)=3p_i P(Y in dy). For the symmetric Potts edge,
P(parent=i|Y)=1/3+eta(p_i-1/3). The unconditional law of Y is unchanged:
both the child and parent have uniform priors. Thus the one-body map above
is exactly the parent experiment associated to one observed child subtree.

At a grid point k/N its scaled image has coordinates
((B-A)N+3A k_i)/(3B). Their floors and remainders have denominator3B.
When the sum of fractional parts is1, the barycentric vertices add one
unit to each coordinate with weights equal to these fractional parts.
When that sum is2, the three vertices add one unit to each coordinate
except one, with weights one minus the corresponding fractional part.
If the sum is0 there is only one vertex. In all cases the weights are
nonnegative, sum to1 and average to the original posterior. After merging
permutations, the one-body orbit transition therefore has denominator3B.

## 2. Why a barycentric split is an information upgrade

Suppose p=sum_v w_v q_v, with w_v>=0 and sum w_v=1. Conditional on the old
observation and on root color i with p_i>0, choose label v with probability
w_v(q_v)_i/p_i. These probabilities sum to1 and Bayes' formula gives
posterior q_v. If p_i=0 then every positive-weight q_v also has zero in
coordinate i; that conditional root event has probability0 and its kernel
can be defined arbitrarily. Forgetting v recovers the old experiment.
This construction explicitly proves the Blackwell upgrade, including
boundary posterior vectors. The simplex splitting in section1 has exactly
the required barycenter property.

Rounding is also an upgrade. For each orbit, retain an appropriate fraction
of every orientation's observation mass and on the removed observations
reveal the root color. This fraction depends on the orbit but not on the
root given the original observation. S3 symmetry makes the unconditional
root color on the total removed mass uniform. The removed posterior law
can therefore be replaced by the pure orbit. The old observation is a
garbling of the refined observation; its posterior statistic is sufficient
for the root, so compression back to the stored posterior law preserves
the Blackwell comparison. Integer floors and adding the missing mass to
the pure orbit implement precisely this experiment.

## 3. Universal fusion, including zero probability observations

Let two observations have unconditional posterior laws mu,nu and be
independent conditional on the root. Their joint unconditional mass at
(p,r) is 3 sum_i p_i r_i times mu(dp)nu(dr). If the dot product is positive,
their combined posterior is p_i r_i/(sum_j p_j r_j). If the dot product
is zero, this joint observation has probability exactly zero, and no
posterior need be assigned to it. It must be skipped before division.
The joint masses sum to1 since both posterior means are uniform.

Fix one left orbit representative k and average over the v distinct right
orientations h. Simultaneous permutation invariance justifies fixing the
left representative when the destination is another orbit. In the integer
generator z_i=9 k_i h_i, total=9 sum_i k_i h_i. Multiplying its barycentric
grid weight by (36/v)*total and dividing by108N^2 gives exactly
(3 sum_i k_i h_i/(v N^2)) times that grid weight. These are the joint
unconditional masses above. For v in{1,3,6}, 36/v is integral; cancellation
of total against the grid remainder makes every destination numerator an
integer. Zero totals contribute0, as required. Every ordered orbit-pair
row sums to108N^2 and has nonnegative numerators.

The implementation adapts the old asymmetric integer generator ONLY by
binding its right strength to1, using a separate cache namespace, and
skipping zero total before normalization. This proof establishes why those
three changes are sufficient. Both inputs have already undergone their
physical tree edge; no additional eta belongs in this fusion operator.

## 4. Independent grouping and induction

If an experiment E is a garbling of E', then replacing E by E' in a
conditionally independent product with another root experiment preserves
the Blackwell order: apply the garbling kernel on that observation alone.
For several branches use the product of their root-independent kernels.

Build powers containing1,2,4,... child observations by repeated fusion.
At every multiplication instantiate fresh observations independently
conditional on the root from each input experiment LAW. If a previously
computed law is used in two places this is two independent copies, never
one shared observation. Combine the powers selected by the binary
expansion of d. Section3 implements each independent product exactly,
followed by the upgrades of section2. Induction over the grouping tree
proves domination of d independent physical child experiments. Induction
over depth, starting from fully known leaves, proves the statement.

Posterior squared distance from the uniform vector is convex. Conditional
Jensen for a garbling therefore orders its expectation, giving the stated
finite-depth upper bound. This argument does not require successive
quantized upper bounds to decrease, and it does not claim they do.

## 5. Arithmetic and current verification limits

One-body raw accumulation sums to S(3B), and unit fusion raw accumulation
sums to S^2(108N^2). All summands are nonnegative; hence each individual
accumulator is bounded by that same total. The stated machine checks,
checked ulong operations for the one-body stage, and the unchanged packed
128-bit fusion core cover these raw sums. Final division uses the existing
exact integer division. Each rounded vector has integer mass total S.

checks/universal_fusion.py independently compares all49 N6 ordered rows
against all-orientation rational Bayes calculations, including36 excluded
zero-likelihood orientations. Twelve four-depth trajectories at degrees
3,5,21 and eta=0,1,161/360,53/237 match a separate Fraction implementation;
their first-depth signals also upper-bound direct multinomial calculations.
checks/balanced_bp_fast.py additionally matched the native degree21,
eta53/237 trajectory through four depths and every final mass on N6.
N96 performance, finite entry, and independent mathematical audit remain
open at the time of writing. Node-rounding losses are logged individually;
their simple sum is NOT asserted to equal a global error probability,
because binary powers reuse laws of separately sampled groups.
