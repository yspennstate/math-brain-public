# T067-UNIVERSAL-FUSION-001 v1: PASS

Exact proof SHA256: `73f4b59ee80e447a94d5a6e23ce19513c70f37b68b8b0a896ea138d1b1d00112`.
Checked 2026-10-15T18:51:26.715428+03:00. Source `~\brain_workers\w682\proofs\T067-UNIVERSAL-FUSION-001_v1.md`.

Kind: audit. Target: T067 critical q3 regular degree6 and its finite-experiment algorithm.
Mathematical PASS; no priority or admission decision. The required exact
independent review/ledger procedure remains separate. Actual execution
account4 is recorded; this verdict does not manufacture an additional
account. No claim file or live mathematical ledger was edited.

## Exact algorithm statement

For uniform-prior symmetric three-color broadcast, integer d>=2,
rational0<=eta<=1, grid N a positive multiple of3 and integer S=2^b,
the specified physical-edge and independently grouped fusion algorithm
Blackwell-dominates the fully observed finite-depth leaves. Thus its
expected posterior squared distance from uniform is an upper bound.
This is an abstract exact-arithmetic theorem, not an infinite-depth
nonreconstruction statement or a machine-resource promise for all grids.

## Sections1-2: calibrated physical edge and both upgrades

For a posterior observation law mu under a uniform root,
P(Y in dy|root=i)=3p_i mu(dy). Across a symmetric channel, root marginals
remain uniform and the parent posterior is u+eta(p-u). Consequently its
scaled GRID coordinates are ((B-A)N+3A*k_i)/(3B); these are N times the
parent posterior, not the unscaled probabilities. Nonnegative weights
sum to N, so fractional deficits are0,1,2. The printed simplex vertices
and their weights have exactly the original barycenter and total mass1.
Every denominator divides3B, including eta0 and eta1.

For any split p=sum w_v q_v, the kernel conditional on root i is
w_v*q_vi/p_i when p_i>0. It is nonnegative and sums to1. On a null event
p_i=0, nonnegativity forces q_vi=0 for every positive-weight vertex; the
kernel may be arbitrary there. The resulting refined posterior is q_v,
and forgetting its added label yields the old experiment. This is an
explicit Blackwell upgrade, including boundary posterior vectors.

Round each ORBIT mass down and root-reveal precisely the removed
observations. Fractions are chosen independently of the root conditional
on the old observation, and uniformly across orientations of each orbit.
Permutation symmetry makes the aggregate removed root marginal uniform,
so root revelation is exactly the pure orbit of the removed total mass.
The old observation can be recovered by a root-independent garbling of
the refined experiment. Storing only its posterior is harmless because
the posterior statistic is sufficient for the root. No independence of
rounding errors and no global sum-of-rounding-loss estimate is assumed.

## Section3: unit fusion, zero events, and integer rows

Given conditionally root-independent experiments with laws mu,nu, their
unconditional joint density relative to mu*nu is3 sum p_i r_i. For positive
dot product their posterior is p_i*r_i/sum p_j*r_j. A zero dot product
means exactly zero unconditional joint mass and is skipped BEFORE any
division. This is valid even for pure boundary laws. The joint law
normalizes because each posterior mean is uniform.

By simultaneous permutation invariance a left representative may be
fixed while averaging over all v distinct right orientations, v=1,3,6.
Set z_i=9k_i*h_i and total=sum z. Each barycentric destination weight w
has coefficient (36/v)*total*w over108N^2. Dividing indeed yields
3(sum k_i*h_i)/(v*N^2) times w, the required joint density. The integer
remainder construction cancels total in w;36/v is integral. Coefficients
are nonnegative and every ordered row sums to108N^2. Null orientations
add zero. No additional eta appears: both branch laws have already
undergone their physical parent edge.

## Section4: independent grouping and depth induction

A garbling remains a garbling after taking a conditionally independent
product: use its root-independent kernel on the affected observation.
Physical edge passage preserves a child-observation garbling for the
same reason. Every reuse of a previously computed LAW instantiates fresh
independent conditional-root observations, not a shared random variable.
Repeated squaring gives groups1,2,4,... and binary expansion combines
fresh groups totaling d. Applying each split/root-revelation upgrade
preserves domination. Induct over the grouping tree and depth from pure
fully known leaves. Conditional Jensen for the convex squared posterior
norm gives the stated EXPECTED signal comparison; no pointwise signal
ordering or monotonicity of successive numerical envelopes is claimed.

## Independent finite and arithmetic checks

Our checks/t067_universal_control_own.py imports no author code. At N6 it
derives every one of49 ordered unit rows by averaging BOTH orientations
with exact Fraction Bayes, and separately by fixing the left orientation.
All49 agree, include all36 zero-likelihood ordered point pairs, normalize,
and have integer coefficients over108N^2. It derives28 one-body rows at
eta0,1,89/218,53/237 and verifies barycenters and denominators. Its962
barycenter controls check total weight, nonnegativity and each coordinate.
Four complete degree6 depth trajectories are obtained by a separate
Fraction law update. All7 masses, all4 node revelation amounts and the
signal at every depth match our separately adapted native evaluator.
Every native N6 unit and physical-edge row also matches the rational rows.
An independent direct multinomial six-child depth1 computation is bounded
above by the algorithmic signal. It checks the direction of domination.

Raw fusion accumulation sums to S^2*108N^2; one-body sums to S*3B.
Each summand is nonnegative, so each partial destination sum is bounded
by the same total. The stated128/64bit conditions therefore suffice;
our code also checks them and uses checked operations. The own packed
two-limb controls compare100 products/accumulations to BigInteger,
including expected carry and3 overflow rejections. The generic theorem
can instead use arbitrary integers and has no machine caps.

No sampled numerical row establishes the general theorem: the exact
formulas and experiment constructions above do. The current N96 degree6
implementation is covered separately by its full independent audit.
