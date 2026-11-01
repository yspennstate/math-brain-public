# Exact unpaid directions after this run

1. **OPEN: full rotated two-input switching limit.** Prove the first switching time and post-switch path under a transverse return of J_j(t)=integral r_j to zero. Track already absorbed gate populations; a gate population cannot be restored by a later sign change. The deterministic same-sign imbalanced example is a concrete target. The finite-width proof here establishes nonfreezing without supplying the path limit. First audit c01's local stopped-clock proposition, then derive an event-clock description valid in a shrinking neighborhood of the crossing.
2. **OPEN: multiple critical Euler steps.** Extend the reviewed one-step expansion to k fixed steps with shared Poisson atoms and updated residuals. Then determine whether an all-grid boundary limit and a macroscopic GD limit hold. Preserve signed overshoots. Do not replace the real ReLU output by the initial tangent prediction. The one-step nonzero correction and held-path discrepancy show why that shortcut fails.
3. **OPEN: quantitative rates.** The proofs use tight localization, rare gate probability O(1/log m) at fixed cutoffs, and truncated square mass O(epsilon^(2-alpha)). A useful rate requires an explicit joint coupling and balancing the cutoffs with the random residual margin and energy tail. No uniform rate follows merely from those two displayed orders.
4. **OPEN: smooth activations and nonorthogonal inputs.** The absorbing-gate arguments rely on exact ReLU zeros and orthogonal projected flow equations. A smooth activation may retain a restoring force, and nonorthogonal inputs allow cross-coordinate parameter motion; neither extension is proved here.
5. **Fallback OPEN: T262 entrance/containment.** Parent package's reviewed local generator does not establish global containment or entrance from the relevant initialization. Switch mechanism if repeated attempts on the rotated path law remain unchanged.

## Preserved unsuccessful approaches

- Mixed-sign two-input initial residuals: the transformed residual system is Metzler, making the sign cone invariant; their cumulative coordinates cannot reverse. Use same-sign imbalance to test later gate deaths.
- Globally freezing the kernel after the initial boundary: disproved by the reviewed rotated finite-width theorem.
- Copying the continuous boundary J1 path law to held Euler steps at fixed critical gamma: disproved at a single deterministic interior grid time, although the first endpoint kernel and integrated output formula agree.
- Treating an exact candidate crossing time as an established finite-width switching law: unsupported; this remains the main gap.
- Symbolic execution with SymPy: dependency unavailable; no symbolic check ran. A standard-library numerical sanity check succeeded and is explicitly subordinate to the analytic proof.
