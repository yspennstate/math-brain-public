The operator criterion in the unmodified positive radial reduction reaches its numerical ceiling near rho = 0.44101422. Its Hilbert–Schmidt norm with the published center crosses 2 near 0.43251274. Equation (139) and its sharpened form (142) show no grid failure. These are numerical estimates; no new Gaussian noise-stability interval is proved.

Target 1(a) reproduces the published output exactly. Commit `6b720fe57bfe2a3c8fffc51521d00b31011aa1a3`, unmodified `plur_cert_positive.py`, gives 90 accepted slabs from 150 attempts, worst slab [0.38625,0.3875], finite upper 3.99929063236 and total certified upper 3.99929096609. Runtime here is 424.84 seconds. The full output and dependency/input hashes are in `logs/reproduction.txt` and `logs/reproduction_metadata.json`.

Targets 1(b,c) use the literal center in (150), literal kernel in (149) and denominator in (148). The weighted operator is compressed to the mean-zero subspace; additive centering cancels there. Radial Gauss–Legendre Nyström quadrature gives:

| Radial nodes | Cutoff | Angular nodes | rho_HS | rho_op |
|---:|---:|---:|---:|---:|
| 256 | 20 | 128 | 0.432512741320 | 0.441014219195 |
| 512 | 20 | 192 | 0.432512741320 | 0.441014219195 |
| 768 | 30 | 256 | 0.432512741320 | 0.441014219195 |

The largest root drift is 4.54e-13. This is observed convergence, not a rigorous error bar. The 56-point sweep covers [0.4,0.95] in steps of 0.01. The largest positive eigenvalue controls the operator norm throughout the sweep; the negative branch is small. Representative values follow (256 nodes, cutoff 20, 128 angular nodes):

| rho | HS norm | Mean-zero operator norm |
|---:|---:|---:|
| 0.40 | 1.89736807 | 1.87963496 |
| 0.43 | 1.99201407 | 1.96774632 |
| 0.44 | 2.02386950 | 1.99703031 |
| 0.45 | 2.05594599 | 2.02631640 |
| 0.50 | 2.22118340 | 2.17377235 |
| 0.60 | 2.59700751 | 2.48646183 |
| 0.70 | 3.09798138 | 2.85705723 |
| 0.80 | 3.88140866 | 3.35750987 |
| 0.90 | 5.40845686 | 4.18092711 |
| 0.95 | 7.04973798 | 4.91265584 |

At rho = 0.4 the finest HS estimate is 1.897368072736 and the operator estimate is 1.879634961484. Their ratio is 1.0094343378, a 0.943434% HS excess. The squared-norm ratio is 1.0189576824. At rho = 0.95, increasing the cutoff from 20 to 30 while fixing 512 radial and 192 angular nodes changes HS by 2.7e-10 and the operator by -1.27e-12. Doubling angular nodes alone at the same cutoff changes HS by -1.59e-12 and the operator by -3.11e-13.

Target 1(d) has no observed failure at any requested rho: 0.45, 0.5, 0.6, 0.7, 0.8 or 0.9. Each rho uses 81 values of a, spanning zero through all radial couplings induced by x,y in [0,7], with logarithmic coverage near zero. Each a uses 621 scalar coordinates (600 uniform panels plus exact simplex coordinates and perturbations near 1/3), and all pairs of the 496 simplex vectors of denominator 30. This is 187,421,526 scalar pairs and 119,563,776 vector pairs per inequality across the run. The largest signed residuals are 6.66e-16 for (139) and 6.66e-16 for (142), at the scale of rounding; the failure threshold is 1e-10. Eighteen selected cases repeat with doubled Fourier truncation. This grid does not prove the inequalities globally. Lemma A.2 and Corollary A.3 already state them for every a >= 0: rho enters only through a = 2rho xy/(1-rho^2).

The checks address the strongest ways these estimates could be wrong: a missing radial Jacobian, a wrong J normalization, failure to impose the weighted mean constraint, a center that changes the constrained operator, inadequate cutoff, or unresolved angular quadrature. Twenty J values agree with a direct radial marginal to relative 3.51e-13. Sixteen K entries agree with independent Bessel arc formulas to relative 2.9e-14. Projection, eigenvector and centered-versus-uncentered controls pass. Cutoff and angular refinements vary one setting at a time. Detailed rows, metadata and commands are saved under `logs/` and `proofs/NUMERICAL_METHOD.md`.

The dossier's 3.99929 is a certified slab upper bound, not the actual value of h_+^2. A bound close to 4 at rho about 0.387 does not locate the actual HS crossing. A proposed dossier correction is saved in `patches/01_t039_measured_reach.diff`; the live dossier is untouched.

Target 2 is worth a modest certification effort below approximately 0.441. HS alone has room until approximately 0.4325, so interval refinements may already extend the published 0.4 range. A certified operator estimate may recover the small further gap. The unmodified operator is numerically above 2 by rho = 0.45; reaching 0.615 requires a stronger estimate or another reduction. The hardest remaining piece is a rigorous infinite-dimensional upper bound over a whole rho interval, with every quadrature and tail error enclosed. No theorem beyond the published range is claimed.

Primary sources: Steven Heilman, [arXiv:2608.00333v1](https://arxiv.org/abs/2608.00333v1), Sections 1.3–1.4, 8–9, Appendix A pp.38–43, especially (139), (142), (148)–(152) and Lemma A.4; [author's certificate at the pinned commit](https://github.com/sheilman77/cut_bounds/tree/6b720fe57bfe2a3c8fffc51521d00b31011aa1a3). PDF pages 40–41 were inspected visually to restore the symbols dropped by extraction. Primary abstract metadata confirms author, v1 date and arXiv nonexclusive distribution license. Brain queries did not return the aligned-arc or positive-simplex results; attributed card drafts and the numerical owner-work draft are staged under `bundles/`, inside this task's permitted folder, for the reviewer to copy to the inbox.

2026-10-14T22:32:35.694571+00:00 | 1(a) | Certificate reproduction completed and measured.
2026-10-14T22:32:35.694571+00:00 | 1(b) | Literal published-center HS crossing estimated and refined.
2026-10-14T22:32:35.694571+00:00 | 1(c) | Weighted mean-zero norm crossing estimated and refined; independent normalization and centering controls passed.
2026-10-14T22:32:35.694571+00:00 | 1(d) | All requested arc grids completed; no failure candidate.
Rung: numerical evidence for the extension; reproduction of an existing directed certificate for the published range. No independent PASS has been received.
NEXT: Reviewer audit T039-C001–C003 v1 and the proposed dossier correction, then decide staffing for target 2.

2026-10-14T22:42:12.550800+00:00 | PACKAGE | Four card drafts and one measured hook proposal staged locally; exact edge quotes and dependency graph checked. Log encoding originals preserved. Chart visually inspected. Source/script hashes match the experiment metadata. All assigned foreground computations completed; no process is left running by this task.

2026-10-14T22:50:13.915332+00:00 | RECONCILE | Original package identities rechecked; target 1(a)-(d) remain complete, with no repeated mathematical run. The repeated reminder reads the superseded parent checkpoint. Task status remains NEEDS_REVIEW for an agent.
