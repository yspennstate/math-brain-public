# PROB20-21 n=6 coverage manifest — 2026-09-16_16-34-58_UTC

## Scope

Fixed fleet metric: largest `n` for which the Courtade–Kumar Conjecture 1 inequality is certified for **every Boolean function on `n` inputs and the entire continuous BSC interval `alpha in [0,1/2]`**, under the source-valid compression convention.

This manifest supports metric movement `5 -> 6`. It does **not** claim the universal conjecture.

## Runtime / arithmetic

- Model exposed to this run: GPT-5.6 Sol.
- Reasoning-effort selector / actual effort metadata: UNVERIFIED. GPT-6 / maximum was requested but not exposed.
- Compiler: `g++ (Debian 14.2.0-19) 14.2.0`.
- Architecture: `x86_64`.
- Exact rational arithmetic: GMP / `mpq_class`.
- Transcendental enclosure: MPFR shared library `/lib/x86_64-linux-gnu/libmpfr.so.6`, 192-bit precision, directed rounding from exact rational inputs.

## Frozen source reduction / enumeration

Courtade–Kumar Theorem 2 and Corollary 1 reduce the fixed-noise maximization problem to the family `S_n` of sets compressed on all one- and two-coordinate sections. For `n=6`, the source reports `|S_6|=1173`.

The final C++ checkers independently regenerate this family as order ideals of the source section constraints, sort masks numerically, and directly verify every generated mask section-by-section. A separately written Python enumerator reproduces:

- candidate count: `1173`;
- sorted-mask SHA-256, frozen encoding as 16 lower-case hexadecimal digits plus newline per mask: `e626f58f6448f43d575d976bffce232771098f5f8157c2f13054ebd3c709f404`;
- constants: `2`;
- dictator in frozen compressed orientation: `1`;
- nontrivial nondictators requiring certification: `1170`;
- balanced candidates total: `41`, hence balanced nondictators: `40`.

The deterministic middle-certificate index convention is the ascending list of the 1170 nontrivial masks after constants/dictator are removed from this sorted list.

## Counterexample-first exact finite search

Executed checker:
`2026-09-16_16-34-58_UTC__n6_counterexample_grid.cpp`

Executed output:
`2026-09-16_16-34-58_UTC__n6_counterexample_grid_output.txt`

The checker evaluates every nontrivial compressed representative at the exact rational grid

`alpha = j/128`, `j=1,...,63`,

using exact rational degree-six transition polynomials and outward-rounded MPFR entropy/logarithm bounds.

Coverage: `1170 * 63 = 73710` function/noise points.

Result:

- certified negative gaps: `0`;
- outward-rounding inconclusive signs: `0`;
- minimum directed lower gap: `6.8015800431331628e-06` nats;
- worst grid mask: `1537228672809129301`;
- worst grid noise: `63/128`.

The grid is diagnostic only; it receives no continuous-interval credit.

## Analytic low-noise regime

Interval: `[0, 1/524288]`.

Exact finite invariants regenerated from all 1170 nontrivial compressed candidates:

- minimum balanced-nondictator average sensitivity: `5/4`, mask `1537228672809129303`;
- minimum higher-level Fourier mass `Delta = Var(f)-W_1(f)`: `57/1024`, mask `1`.

Biased case, after output complementation: `p <= 31/64`. Directed MPFR evaluation certifies

`ln 2 - h(1/524288) - h(31/64) > 0.00046133401388981707` nats.

Balanced case: the final batch source uses `c0=(1-1/524288)^5` and certifies the uniform analytic margin, after division by `alpha`,

`> 0.052592775515960845`.

Thus the entire low-noise continuum is certified analytically.

## Analytic high-noise regime

Interval: `[69/140, 1/2]`, equivalently `rho=1-2 alpha in [0,1/70]`.

For every nonconstant nondictator, let `mu=E f`, `V=1-mu^2`, `Delta=V-W_1`. At endpoint `rho0=1/70`, the exact candidatewise checker verifies

`L=(1-rho0^2) Delta - 63 rho0^2 V > 0`

and

`L^2 - 4 mu^2 rho0^2 * 63 V > 0`.

Global exact minima over the 1170 candidates:

- `min L = 107397/2508800`, mask `1537228672809129301`;
- `min squared margin = 254319669/6294077440000`, mask `1`.

The report derives why this endpoint condition implies the full high-noise interval via a Taylor bound for `psi(x)=ln2-h((1+x)/2)`, Parseval, and Cauchy–Schwarz over the 63 nonconstant Walsh characters.

## Middle continuous interval

Interval: `[1/524288, 69/140]`.

Executed batch checker:
`2026-09-16_16-34-58_UTC__n6_middle_batch.cpp`

Executed output:
`2026-09-16_16-34-58_UTC__n6_middle_batches_output.txt`

Each posterior `q_y(alpha)` is represented exactly as a degree-six rational Bernstein polynomial. Exact de Casteljau subdivision restricts it to a rational subinterval. The convex-hull property of Bernstein coefficients encloses the posterior range. Concavity/symmetry of binary entropy and 192-bit directed MPFR rounding give a rigorous lower bound for the Courtade–Kumar gap on the **entire subinterval**. Failed lower bounds are bisected exactly at the rational midpoint.

Accepted deterministic successful batch partition:

- `[0,50),[50,100),...,[950,1000)`;
- `[1000,1020),[1020,1040),...,[1140,1160),[1160,1170)`.

The manifest checker requires a clean `BATCH_PASS` and shell exit status `0` for every accepted block and ignores incomplete or duplicate scratch blocks.

Aggregate certified coverage:

- candidates: `1170/1170`;
- missing accepted batches: `0`;
- failed candidates: `0`;
- subdivision nodes: `176148`;
- certified leaves: `88659`;
- maximum bisection depth: `21`;
- minimum strictly positive outward lower gap: `1.3657107213430298e-10` nats;
- corresponding mask: `78556906072250199`;
- corresponding interval: `[9215803567/18790481920, 461242375/939524096]`;
- corresponding accepted batch: `[350,400)`.

## Independent coverage-manifest checker

Executed:
`2026-09-16_16-34-58_UTC__coverage_manifest_check.py`

Output begins:

`PROB20-21 N=6 COVERAGE MANIFEST CHECK: PASS`

It independently parses the batch log, verifies exact non-overlapping index coverage of all 1170 nontrivial candidates, requires zero failed candidates, verifies the exact-grid coverage count/sign results, and checks the independent enumeration hash.

## Final artifact hashes

- `2026-09-16_16-34-58_UTC__n6_middle_batch.cpp`: `c4c1c4ec795199d1e1a6e1489f917ef2e046314601771c9249964ecb1a5bd7ac`
- `2026-09-16_16-34-58_UTC__n6_middle_batches_output.txt`: `03ec6979aa49e3572213153e8ea456bb73efffe72b320211c5409fb7e961655e`
- `2026-09-16_16-34-58_UTC__n6_counterexample_grid.cpp`: `1506c658469d15b6fab125dfdcc91de020a63e8769d4c83fb4190cfba6d8d9fa`
- `2026-09-16_16-34-58_UTC__n6_counterexample_grid_output.txt`: `2d60fcbc96edfd743329b1961e0c805cc83674dce8986e0601cf6e438db30375`
- `2026-09-16_16-34-58_UTC__s6_independent_enumerator.py`: `1c151512ae8be1b5ffb54f205f81790b704219770efb44672fc17258875213d6`
- `2026-09-16_16-34-58_UTC__s6_independent_enumerator_output.txt`: `f0afea46688ebf917a41537f6d1b180e63c2768400249d1767d8fd419545b840`
- `2026-09-16_16-34-58_UTC__coverage_manifest_check.py`: `30e2b37617f74822ce54558a9d584a0691fafcb9295df62cb5aa544ade174971`
- `2026-09-16_16-34-58_UTC__coverage_manifest_check_output.txt`: `cb21c7145e22fe00eb25f5e98df284c7fdb779757cabe98f5c2258dbde1ed812`

## Exploratory execution archive

Performance-oriented scratch checkers that timed out or were superseded receive **no coverage credit**. Their exact source text and hashes are preserved together in:

`2026-09-16_16-34-58_UTC__scratch_executed_sources.txt`

with status/hashes in:

`2026-09-16_16-34-58_UTC__scratch_execution_log.txt`.

This prevents a timeout or abandoned performance variant from being mistaken for a certificate.

## Coverage conclusion

By the source compression theorem, full continuous certification of all 1173 `S_6` candidates (trivial/equality cases plus 1170 checked nondictators) certifies **all Boolean functions on six variables** for every `alpha in [0,1/2]`. Lower dimensions embed by dummy coordinates. Therefore the fixed metric moves from `5` to `6`.

This is **PARTIAL** for the universal Courtade–Kumar conjecture. It has self-checks and independent executable enumeration/manifest checks, but it has not received a P26 audit or the required distinct OTHER-task audit.
