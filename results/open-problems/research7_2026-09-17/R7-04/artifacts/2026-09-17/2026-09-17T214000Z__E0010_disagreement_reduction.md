Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum reasoning was requested, but no authenticated runtime reasoning telemetry or binding model/effort selector is exposed.

# E0010 — exact attractiveness, second-class-particle drift, and the relative-replacement obstruction

Source target: Rick Durrett, *Coexistence in stochastic spatial models* (2009), Problem 4. For the source sexual-reproduction process with `beta>4.5`, prove uniqueness of the positive/nontrivial stationary phase for sufficiently fast stirring. The source convention is the additive correction in `research7_2026-09-17/R7-04/admissions/2026-09-17T213700Z__E0010_source_scope_correction.md`: uniqueness means a unique stationary law with no mass on the all-zero configuration; convex mixtures with the absorbing law are not counted as additional positive phases.

Mathematical status of this artifact: **PARTIAL / OPEN**. The source theorem is not proved here. What is proved is an exact monotone-coupling reduction identifying a concrete necessary obstruction to nonuniqueness.

## 1. Source dynamics and notation

Let `eta in {0,1}^{Z^d}`. A `1` dies at rate 1. Let `N_x` be the finite source birth neighbourhood of `x`, of cardinality `n`. At rate `beta`, a vacant site `x` samples two distinct neighbours from `N_x`; it becomes occupied iff both sampled sites are occupied. Equivalently, with ordered pairs,

`A_x(eta) = [1/(n(n-1))] sum_{y != z in N_x} eta_y eta_z`

and the `0 -> 1` rate at `x` is `beta A_x(eta)`.

The fast-stirring process additionally exchanges the occupations at the endpoints of each stirring edge at rate `epsilon^{-2}`. Write the stirring neighbour set of `x` as `S_x` and its degree as `d_s=|S_x|` (the derivation only needs translation invariance and finite degree).

The mean-field reaction is

`f(u) = -u + beta u^2(1-u)`.

For `beta>4`, the positive equilibria are

`rho_- = (1-s)/2`, `rho_+ = (1+s)/2`, `s=sqrt(1-4/beta)`.

We write `rho=rho_+`. Since the source assumes `beta>4.5`, this is the stable positive root on the survival side of the fast-stirring wave threshold.

## 2. The source process is attractive

### Proposition 2.1

The fast-stirred sexual-reproduction process is attractive for the coordinatewise order on `{0,1}^{Z^d}`.

### Proof

Use one common Harris system for two configurations `eta <= xi`.

1. **Death mark at x.** The update sets coordinate `x` to 0. Applying the same map to two ordered configurations preserves order.

2. **Birth mark `(x;y,z)`.** The update is the Boolean map

   `eta_x <- eta_x OR (eta_y AND eta_z)`

   for an ordered pair of distinct birth neighbours `y,z`. Boolean AND and OR are increasing in every coordinate, hence the map is order preserving.

3. **Stirring mark on {x,w}.** The update simultaneously swaps coordinates `x,w`. Applying the same permutation of coordinates to two ordered configurations preserves coordinatewise order.

Every graphical update is monotone; therefore the coupled process preserves `eta_t <= xi_t` for all times. ∎

### Consequence

The prior intake attempt `E0010-A001` said the model was “not attractive” because births require two occupied neighbours. That statement is false: requiring two occupied neighbours makes the birth rate increasing, not decreasing. This correction is substantive because it restores the basic monotone-coupling/second-class-particle route to uniqueness.

## 3. Exactness of the frozen metric

Let `bar_nu_{beta,epsilon}` be the upper invariant law obtained as the weak limit from the all-one initial state. In the source survival regime it is a positive invariant law. Let

`I_nt(beta,epsilon) = {mu stationary : mu({all-zero})=0}`.

Define the frozen source-matching metric

`Q_SR(beta,epsilon) = sup_{mu in I_nt} [ bar_nu(eta_0) - mu(eta_0) ]`.

At admission its numerical/analytic value is `UNKNOWN/UNMEASURED`.

### Proposition 3.1

For fixed `(beta,epsilon)` in the survival regime,

`Q_SR(beta,epsilon)=0`

if and only if `bar_nu` is the unique element of `I_nt(beta,epsilon)`.

### Proof

Uniqueness trivially implies `Q_SR=0`.

Conversely, attractiveness and the maximal all-one initial state imply every invariant law `mu` is stochastically dominated by `bar_nu`. By Strassen, couple `mu <= bar_nu`; evolve the pair with the basic coupling. Since both marginals are stationary, Cesaro averages of the joint law have the same marginals, remain supported on ordered pairs, and by compactness admit a subsequential stationary coupling `pi`.

Suppose `Q_SR=0`. Translation invariance of the dynamics implies every translate `tau_x mu` also belongs to `I_nt`. Hence the origin equality in the definition of `Q_SR`, applied to every translate, gives

`mu(eta_x)=bar_nu(eta_x)` for every x.

Under `pi`, let `D_x=xi_x-eta_x >=0`. Then

`E_pi D_x = bar_nu(eta_x)-mu(eta_x)=0`.

Thus `D_x=0` almost surely for each fixed `x`. The lattice is countable, so with probability one `D_x=0` for all `x`; the coupled configurations coincide and `mu=bar_nu`. ∎

This shows that the frozen metric is not merely a density proxy: exact zero is logically equivalent to the source uniqueness assertion under the source convention.

## 4. Exact second-class-particle drift

Fix any stationary basic monotone coupling `(eta,xi)` with `eta<=xi`, lower marginal `mu in I_nt`, and upper marginal `bar_nu`. Set

`D_x = xi_x-eta_x in {0,1}`, `q_x=E D_x`.

The variables `D_x` are the second-class/disagreement particles.

### Proposition 4.1 — exact one-site stationarity identity

For every site `x`,

`0 = epsilon^{-2} sum_{w in S_x}(q_w-q_x) - q_x`

`    + beta E[(1-xi_x)(A_x(xi)-A_x(eta)) - D_x A_x(eta)].`  (4.1)

Moreover

`A_x(xi)-A_x(eta)`

`= [1/(n(n-1))] sum_{y != z in N_x} [D_y xi_z + eta_y D_z].`  (4.2)

### Proof

For the observable `D_x`:

- a death mark at `x` annihilates a disagreement at rate one and never creates one, contributing `-q_x`;
- a stirring mark on `{x,w}` swaps `D_x,D_w`, contributing `epsilon^{-2}(q_w-q_x)`;
- if `D_x=0`, a birth can create a disagreement only when both configurations have `x=0`, the upper selected pair is occupied, and the lower selected pair is not, which after averaging over ordered pairs gives `(1-xi_x)(A_x(xi)-A_x(eta))`;
- if `D_x=1`, the upper site is already occupied and a lower birth annihilates the disagreement exactly when the lower selected pair is occupied, giving `-D_x A_x(eta)`.

Stationarity makes the expected generator equal zero, proving (4.1).

For each ordered pair `(y,z)`, use the exact algebra

`xi_y xi_z - eta_y eta_z = (xi_y-eta_y)xi_z + eta_y(xi_z-eta_z)`

`= D_y xi_z + eta_y D_z`.

Averaging proves (4.2). ∎

### Interpretation

There is no spontaneous creation of a disagreement. Every birth-created disagreement is charged to a pre-existing disagreement in one of the two selected parent positions. Disagreements diffuse rapidly under stirring, die at ordinary death marks, and receive extra annihilation when the lower process gives birth at a disagreement site. This is the exact interacting “second-class particle” formulation of E0010.

## 5. Stable-root linearization and the contraction margin

At `rho=rho_+`,

`f'(rho) = -1 + beta(2rho-3rho^2)`.

Write

`lambda_beta = -f'(rho)`.

Since `rho=(1+s)/2` and `beta=4/(1-s^2)`, direct algebra gives

`lambda_beta = 2s/(1-s) > 0`.  (5.1)

Normalize by `beta`:

`kappa_beta = lambda_beta/beta = s(1+s)/2`.  (5.2)

At the source threshold `beta=4.5`, `s=1/3`, hence

`lambda_4.5 = 1`, `kappa_4.5 = 2/9`.

As `beta` increases, `kappa_beta` tends to 1.

Thus the positive mean-field phase is not merely stable: it has an explicit strict linear killing margin for infinitesimal disagreements.

## 6. Exact factorization-defect decomposition

Let

`bar q_x = (1/n) sum_{y in N_x} q_y`.

Define the signed local relative-equilibrium remainder

`R_x = [1/(n(n-1))] sum_{y != z in N_x} {`

`  E[(1-xi_x)D_y xi_z] - (1-rho)rho q_y`

` +E[(1-xi_x)eta_y D_z] - (1-rho)rho q_z`

`} - [E[D_x A_x(eta)] - rho^2 q_x].`  (6.1)

This is an identity, not an approximation.

Substituting (4.2) into (4.1), adding and subtracting the three mean-field products in (6.1), and noting that each neighbour appears `n-1` times in each ordered-pair position gives

`0 = epsilon^{-2} sum_{w in S_x}(q_w-q_x)`

`    - q_x + beta[2rho(1-rho) bar q_x - rho^2 q_x + R_x].`  (6.2)

If local variables around a tagged disagreement behaved like a background Bernoulli phase of density `rho`, then `R_x` would be negligible relative to `q_x`, and (6.2) would have the strictly negative mass coefficient `f'(rho)=-lambda_beta`.

## 7. A necessary obstruction to nonuniqueness

### Theorem 7.1 — relative replacement obstruction

Fix `beta>4.5` and `epsilon>0`. Suppose there exists a stationary ordered coupling as above with a nonzero disagreement field, and put

`Q = sup_x q_x > 0`.

Choose any sequence `x_m` such that `q_{x_m} -> Q`. Then one may choose it fast enough that

`epsilon^{-2} d_s (Q-q_{x_m}) / q_{x_m} -> 0`,

and along such a sequence,

`liminf_{m->infinity} R_{x_m}/q_{x_m} >= kappa_beta = s(1+s)/2`.  (7.1)

### Proof

Since `q_w<=Q`, the stirring term at `x` satisfies

`epsilon^{-2} sum_{w in S_x}(q_w-q_x) <= epsilon^{-2} d_s (Q-q_x)`.  (7.2)

Also `bar q_x<=Q`. Rearranging (6.2) gives

`beta R_x`

`= [1+beta rho^2]q_x - 2 beta rho(1-rho) bar q_x`

`  - epsilon^{-2} sum_{w in S_x}(q_w-q_x)`

`>= [1+beta rho^2]q_x - 2 beta rho(1-rho)Q`

`   - epsilon^{-2}d_s(Q-q_x)`.  (7.3)

Divide by `q_x` and send `x=x_m` to a supremum sequence. Because `q_{x_m}->Q>0`, the two ratios involving `Q-q_{x_m}` vanish. Therefore

`beta liminf R_{x_m}/q_{x_m}`

`>= 1+beta rho^2 -2beta rho(1-rho)`

`= 1- beta(2rho-3rho^2)`

`= -f'(rho) = lambda_beta`.

Divide by `beta` and use (5.2). ∎

### Corollary 7.2 — sufficient local lemma for the full source theorem

For fixed `beta>4.5`, it would suffice to prove the following uniform fast-stirring statement:

There exist `epsilon_0(beta)>0` and `delta(beta)>0` such that, for every `epsilon<epsilon_0`, every stationary basic ordered coupling with lower marginal in `I_nt`, and every approximate-maximal disagreement sequence `x_m`, one has eventually

`R_{x_m}/q_{x_m} <= kappa_beta-delta(beta)`

whenever `q_{x_m}>0`.

Indeed Theorem 7.1 would then forbid any nonzero stationary disagreement field, so Proposition 3.1 would give uniqueness.

## 8. Why ordinary hydrodynamic/local-equilibrium estimates are not enough

A tempting route is to prove simply `R_x=o_epsilon(1)` by rapid stirring. That is insufficient. If nonuniqueness persists but its disagreement density itself satisfies `Q_SR(beta,epsilon)->0`, then an absolute error tending to zero can still be much larger than the signal `q_x`.

The required missing ingredient is therefore a **relative Palm replacement lemma**, not ordinary propagation of chaos:

conditional/local correlations containing one disagreement factor must factorize around the stable positive density with error `o(q_x)`, or at least with coefficient strictly below `kappa_beta q_x`, uniformly over all stationary monotone couplings.

This identifies the exact scale at which a complete proof must operate.

## 9. Section-B method outcomes

### B2 — attack the negation first

Assume a second positive stationary law exists. Attractiveness yields a nonzero stationary disagreement process below the upper invariant law. Theorem 7.1 shows that every such counterexample must sustain a local normalized factorization defect at least `kappa_beta` at approximate-maximal disagreement sites despite arbitrarily fast stirring. Thus nonuniqueness has a concrete, quantitative obstruction rather than merely “different invariant laws”.

Outcome: **successful reduction, not source closure**.

### B18 — say it in another language

The source uniqueness problem is translated into extinction/nonexistence of stationary second-class particles in a rapidly stirring attractive system. The mean-field tangent equation has killing rate `lambda_beta>0`, and the exact lattice drift differs from it only by the signed relative-equilibrium remainder `R_x` plus spatial diffusion.

Outcome: **new exact formulation**. The remaining theorem is a tagged-disagreement averaging problem.

### B25 — count the same thing twice

The pair identity

`xi_y xi_z-eta_y eta_z = D_y xi_z + eta_y D_z`

charges every excess successful upper birth to a disagreement in exactly one ordered parent position. Counting the same birth discrepancy through the generator and through its parent disagreement yields (6.2), and maximizing the disagreement field yields the sharp threshold (7.1).

Outcome: **new exact quantitative obstruction**.

## 10. Exact gap and next attack

Frozen metric: `Q_SR(beta,epsilon) = UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED`; **no movement** on the source metric in this first E0010 research run. The run moves the proof structure, not the frozen endpoint.

The exact missing lemma is:

> **Relative Palm replacement.** For every fixed `beta>4.5`, uniformly over all stationary ordered basic couplings with a positive lower phase, the local correlations in (6.1), when normalized by the tagged disagreement probability `q_x`, approach the Bernoulli-background factors at approximate maxima as `epsilon->0` strongly enough to put `R_x/q_x < kappa_beta`.

This must remain valid even when `q_x` itself tends to zero with `epsilon`; an absolute replacement theorem is insufficient.

Next Section-B methods, deliberately different from B2/B18/B25:

- **B6 (deform to a solvable point):** introduce an auxiliary independent-refresh/stirring model where exact local equilibrium makes `R_x=0`, then identify the precise comparison term generated while deforming back to conservative stirring.
- **B11 (dualize):** derive the backwards genealogy of a single disagreement under the basic coupling and seek a Feynman-Kac/adjoint representation whose spectral radius is controlled by `lambda_beta`.
- **B30 (one scale/direction at a time):** prove a finite-block relative replacement estimate conditional on one tagged disagreement, then identify exactly how block size versus stirring rate must scale to glue it uniformly over stationary couplings.

No claim of source resolution, audit closure, or publication novelty is made.
