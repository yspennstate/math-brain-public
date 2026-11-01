# Results, limits and next directions

This is the continuation checkpoint for work beyond the prior 30-worker campaign. The main target was selected from the actual unresolved dossier and moves, not merely the stale catalog status. Do not count the already solved T069, T228, T353 or scalar finite-rank T336 work again.

## T384 — primary advance

The complete scalar theorem is `research/T384_SCALAR_LIMIT.md`. It gives the joint initialization law, the all-label output path limit, the effective positive-stable kernel, and failure of finite-time equivalence to the initial kernel. Independent probability and dynamics reviews pass. `research/T384_boundary_layer.md` identifies the vanishing-time transition as a marked Poisson gate-death process in J1; its proof now includes the reviewer's finite-jump alignment and right-continuity repairs. `research/T384_fractional_loss.md` gives annealed fractional-loss decay with a stretched-exponential time law. Expected squared loss in the limiting model is infinite; no finite mean-square claim is made.

The earlier, simpler large-label counterexample remains in `research/T384_NONFREEZING.md`, with a separate elementary tightness/event proof. It is now a corollary of the stronger scalar theorem, but is retained as a short independently checkable route.

The exact-gate numerical solver and all experiments are preserved in `code/`; validation is `research/T384_event_clock_validation.md`. The alpha=1.5 widths do not show a convincing decreasing kernel-error trend, and that limitation is recorded rather than hidden. Root reran the 48-path independent solver audit; maximum direct kernel discrepancy was 1.14e-13, and maximum residual change under tighter tolerances was 2.51e-7. Simulations are checks, not proofs of the limit.

Priority directions after the proved scalar result:

1. The fixed-coordinate-input extension `x_j=e_j` is now proved and separately reviewed; see `research/T384_COORDINATE_LIMIT.md`. Its shared-Poisson effective rate vector depends on the initial residual sign partition. The next geometry is a nontrivial orthogonal rotation or two nonorthogonal inputs; rotation is not a free reduction for iid stable coordinates. Do not repeat the proved coordinate case as a new result.
2. Nonorthogonal inputs: competing residual directions and activation hyperplanes can interact. The scalar common clock does not apply. Seek a precise finite-dimensional Poisson-driven limiting system before claiming a general theorem.
3. Discrete gradient descent: compare the step size with the `(log m)^(-1/alpha)` switching time. Euler crossing and absorbing continuous-flow dynamics need not agree at a fixed step.
4. Quantitative convergence and finite-width corrections: the available bounds eliminate opposing mass but give slow width dependence. Obtain rates uniform in a controlled residual/energy event, then validate those rates numerically.
5. Smooth activation or leaky ReLU: examine whether the gate-loss mechanism becomes a continuous transition or disappears. The current theorem uses exact ReLU and does not cover a smoothing limit.
6. External mathematical review and broader priority checking: the source paper explicitly leaves first-layer fluctuations unresolved, and the bounded search found no exact-model resolution. This is not a certified novelty search.

## Other newly preserved work

- T084: B01 proves the leading small-fugacity Rayleigh term and explicit graph-dependent positivity windows. This does not bridge the random-cluster regime near lambda=1/n; that gap remains the useful target.
- T268: B02's smooth spectral-product obstruction and below-threshold layer-norm bound are scoped extensions. The catalog's original ReLU obstruction was already in Vardi–Shamir–Srebro; do not reopen it. Related 2025 function-space bounds make external novelty uncertain.
- T364: B03's exact finite off-component strict maximum and robust positive-probability event do not settle asymptotic high-probability existence. The latter remains open.
- T336: B04 composes finite hierarchical RBF-mixture evidence, encoder quantization and unconditional NLL-ERM. Preserve as an unreviewed candidate until a fresh adversarial proof audit is complete. It builds on the previous package, not on a new scalar baseline closure.
- T262: B05 proves a clipped, compact-state inverse-angle one-step generator. B03 reviewed it and B05 applied all three formal repairs. Entrance from a fixed angle, compact containment over order-n layers, and the joint norm diffusion remain unpaid. A corrected local generator is not a full diffusion theorem.

## Coordination and continuation

The prior 59-file package is verified in both repositories; native claim ingestion remains unconfirmed. This continuation also uses append-only research-package paths and create-only inbox handoffs to the known coordinator. Do not mutate native graph, claim or event stores directly. Request native IDs separately and distinguish transport delivery from actual ingestion.

The user-authorized hourly continuation is enabled with no preset end date. Its next run should read this directory, the latest row moves/reviews and live ownership before doing new work. It should continue an unpaid direction, not regenerate a proved scalar lemma as a new discovery. Record all failures, corrected assumptions, code and new directions in both Brain repositories and verify readback.
