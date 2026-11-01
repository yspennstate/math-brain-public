# T384: full orthonormal-input hybrid training law

This continuation closes the previously unpaid macroscopic switching law for fixed finite orthonormal training inputs, under the explicitly absorbing shallow ReLU flow. It also extends the scalar critical-step calculation to complete boundary-grid and macroscopic discrete-gradient-descent limits. **The general deep-network catalog problem T384 remains open.**

## Main result

For every fixed k<=d, orthonormal inputs in R^d, iid symmetric alpha-stable initialization with 0<alpha<2, any fixed labels, no biases, output scale (m log m)^(-1/alpha), and training multiplier (log m)^(2/alpha), the output converges uniformly on compact time intervals to an explicit random hybrid system. Its kernel converges in L1 over time. It starts with a sign-selected diagonal first-layer mass plus a frozen second-layer matrix. Each selected population is removed permanently when its cumulative residual first returns through zero. There are at most k later removals, almost surely distinct and transverse.

The main proof is [agents/d01_k_input_extension.md](agents/d01_k_input_extension.md). The key new argument is the [sensitivity lemma](SENSITIVITY_LEMMA.md): the sensitivity of the integrated residual to its initial value stays invertible because a quadratic energy decreases both within phases and when diagonal populations are removed. Sard's theorem then rules out grazing and simultaneous switches through every phase. This pays the gap that a first-stage calculation alone left open.

Independent checks are [the sensitivity audit](reviews/d04_sensitivity_review.md) and [the full stochastic k-input audit](reviews/d02_k_input_review.md). These are internal AI-agent mathematical reviews, not external expert certification. See [CLAIMS.json](CLAIMS.json) for precise scope and status.

## Other results and preserved routes

- [Full scalar discrete-GD theorem](agents/d02_discrete.md), with [independent review](reviews/d03_discrete_review.md): at h_m=gamma/(log m)^(1/alpha), the held boundary path has a fixed-grid marked-Poisson limit, while the macroscopic output and positive-time kernel agree with scalar gradient flow. Actual negative gate overshoots are retained.
- [Two-input main theorem](TWO_INPUT_LIMIT.md), [general-pair proof](agents/d01_hybrid.md), [compactness review](reviews/d04_compactness.md), and [general-pair review](reviews/d02_general_pair_review.md) preserve the route that led to the full fixed-k result.
- [Two-input classification](agents/d03_geometry.md) shows at most one later removal in dimension two. [First-stage transversality](agents/d04_transversality.md) and its deterministic three-input example show why that classification does not extend directly to k>=3. Its formerly unpaid later-phase genericity gap is resolved by the sensitivity lemma; the original route is retained for provenance.
- [Executed checks](outputs/check_identities.json) include 10,000 ReLU secant identities, with 3,100 negative overshoots, and 1,000 deterministic two-input classifications. The [three-input script](code/d04_three_input_demo.py) and [raw output](outputs/d04_three_input_demo.txt) exhibit two later removals. These finite numerical checks support algebraic sanity; they are not the proof of a width limit.

## Exact continuation

The next central obstruction is **nonorthogonal input geometry**, where the projected gate equations become coupled and a gate can reactivate. Absorption of each projected coordinate is no longer automatically compatible with the true parameter gradient. Derive the correct dynamics and boundary selection before transporting this proof. General deep-network training, multi-input discrete GD, quantitative rates, and test-input prediction laws also remain open. See [DIRECTIONS.md](DIRECTIONS.md).

The preceding checkpoint is [20261023T222120Z](../20261023T222120Z/README.md). Agent references to `research/...` resolve to the [parent research directory](../../research/). Prior scalar/standard-coordinate theorems are dependencies, not new discoveries of this run. All source pins, accepted model selections, actual executions and coordination states are recorded in [PROVENANCE.json](PROVENANCE.json). Git persistence and native ingestion are separate; package claim labels are not native claim IDs. External priority remains unverified; see [LITERATURE.md](LITERATURE.md).
