# T384 continuation: rotated-input nonfreezing and critical-step Euler correction

This run advances two previously unpaid directions of T384. It does not close the full catalog problem. The proved scalar and standard-coordinate limits in the parent package are prerequisites, not new results of this run.

## Results and status

1. **PROVED (internal, separately reviewed):** For two 45-degree-rotated orthonormal inputs, fixed labels zero, iid symmetric alpha-stable coordinates with 0<alpha<2, and the specified absorbing ReLU gradient flow, there exist fixed 0<delta<2 and eta,p>0 such that the probability of kernel variation exceeding eta between delta and time 2 has liminf at least p. Thus the constant post-boundary kernel law for standard-coordinate inputs fails for arbitrary orthogonal rotations. See [the finite-width proof](ROTATED_NONFREEZING.md), [joint initialization](agents/c01.md), and [independent review](reviews/c03_root_review.md).
2. **PROVED (internal, separately reviewed):** For one scalar simultaneous Euler update at h_m=gamma/(log m)^(1/alpha), the endpoint kernel converges to the continuous boundary kernel at gamma, but the actual output increment uses its integrated area. The frozen-initial-kernel residual approximation misses a random order-(log m)^(-1/alpha) correction. It is nonzero with positive probability for alpha<1 and almost surely for alpha>=1. See [proof](agents/c02.md) and [review](reviews/c01_discrete_review.md). This is a one-step theorem.
3. **CONDITIONAL pending a separate full proof audit:** The local clock proposition in [c01](agents/c01.md) identifies the constant phase before a strictly separated cumulative-residual reversal. Its initialization and nonfreezing uses were reviewed; its complete stopped-process argument was not independently audited in this run.
4. **Failed route preserved:** Strictly mixed-sign residuals have an invariant sign cone and cannot provide the needed cumulative crossing. The successful example uses same-sign but imbalanced residuals. See [adversarial route](agents/c03.md).

The new mechanism is the off-diagonal second-layer Gram term. It couples residuals even for orthogonal rotated inputs. Gate death depends on the integral of each residual, and a later reversal of that integral can remove another order-one first-layer mass. The proof establishes positive-time nonfreezing without assuming convergence to a proposed hybrid process.

## Exact next target

Prove a full rotated-input path limit through the first transverse cumulative-residual crossing. Start from the joint initialization and the reviewed finite-width obstruction here. The candidate removes a sign-selected gate population at its cumulative clock's first return to zero. Unpaid work: control the width-dependent transition interval, establish the switching topology and random hitting-time convergence, and prove uniqueness of the post-switch continuation. A deterministic candidate at r0=(1,3), C0=[[1.5,1],[1,1.5]], A0=(.5,.5) crosses at log(1+sqrt(3)); this is not yet a theorem about the finite-width switching-time law. See [directions](DIRECTIONS.md).

## Prerequisites, evidence, and limits

Parent-relative paths cited as `research/...` in agent notes mean [the parent research directory](../../research/), especially [marked PPP](../../research/T384_marked_PPP.md), [coordinate initialization](../../research/T384_orthogonal_initialization.md), [coordinate dynamics](../../research/T384_orthogonal_dynamics.md), and [boundary layer](../../research/T384_boundary_layer.md). The parent subtree read at start was e7d44cc3f1d6845789ca7959a3ec756220075d90 in both repositories. New files are confined to this unique run directory.

[CLAIMS.json](CLAIMS.json) contains package-local statuses, not native claim IDs. [PROVENANCE.json](PROVENANCE.json) records source pins, selected worker configurations and coordination evidence. Reviews are independent AI-agent mathematical checks, not external expert certification. A bounded primary-source literature check was performed; external priority is not established.

[Executed numerical output](outputs/numeric_check.json) checks the displayed candidate formulas only. The optional SymPy script could not import SymPy in either available interpreter; [the failed execution record](outputs/symbolic_attempt.txt) is preserved. No finite-width simulation or successful symbolic execution is claimed.

Git persistence, inbox transport delivery and native ingestion are distinct. This package requests coordinator ingestion; native claim/proof IDs remain unconfirmed. The existing scalar/coordinate theorems and excluded solved problems are not relabeled or overwritten.
