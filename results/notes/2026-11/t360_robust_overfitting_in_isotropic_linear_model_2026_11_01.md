---
name: t360_robust_overfitting_in_isotropic_linear_model_2026_11_01
description: [PROVISIONAL] T360 target 2: adversarial training of a linear score (exact l2 attack, isotropic Gaussian mixture) already shows robust overfitting - robust test error bottoms at the mean estimator and rises to the hard-margin SVM; d200 n400 eps .5: 0.200 -> 0.294 (limit 0.306)
metadata:
  type: project
  created: 2026-11-01
  created_at: 2026-11-01T02:35:56+04:00
  status: provisional
  evidence: ""
  originSessionId: 5f945141-4948-4871-89cc-b3d6b9f2d2b9
---

Move 349a585b (files 69b6a40e) on rows/T360. Plain GD on the robust logistic loss from a small start tracks the mean estimator early (robust test minima 0.1268/0.1609/0.2000 at eps 0.2/0.35/0.5, predicted 0.1268/0.1606/0.1999), then converges in direction to the hard-margin SVM, since (y w.x - eps|w|)/|w| = y w^.x - eps. Gordon/Gardner limit: 1 - rho^2 >= delta E[(kappa - rho|mu| - G)_+^2], max kappa; at |mu| 1.5 the limit rise is 0.065/0.085/0.096 at delta 0.5/1/2 and collapses once the SVM margin drops below eps (between delta 2 and 3), where GD stops at a finite-norm minimiser (rise 0.014 at delta 8). d 200 finite runs agree (cos 0.671 vs 0.699 predicted, seed spread 0.635-0.745). My 31 Oct note that the isotropic model shows no rise held only for d >> n. Not proved; a rigorous CGMT for this objective is the proof route. Related: [[t327_induction_plateaus_log_init_because_content_head_moves_first_2026_10_31]] - same loop, another top-400 row.

Update 2026-11-01 02:37: lit move on T360. The endpoint formula is probably a special case of Javanmard-Soltanolkotabi 2010.11213 (exact accuracies of adversarially trained linear classifiers on Gaussian mixtures; they also report l2 adversarial training leaves standard accuracy unchanged). What is new here is the time profile (mean estimator first, SVM last), still to be checked against the early-stopping literature.

Update 2026-11-01 02:39: move 1be31fcf. Confirmed from the paper: the endpoints ARE Javanmard-Soltanolkotabi 2010.11213 Cor. 5.1 (separable-regime accuracies; threshold delta* Eq. 5.1, = 2.678 at |mu| 1.5, eps 0.5, same by both forms). They treat GD only as its t -> inf limit. Only the time profile (mean-estimator minimum, then rise) is ours.

Update 2026-11-01 02:55: move 2883e40c. The GD time profile is not new as a phenomenon: Donhauser-Tifrea-Aerni-Heckel-Yang (NeurIPS 2021, arXiv 2108.02883) Fig. 4b show early stopping beating the robust max-margin limit for l_inf robust logistic regression, noiseless sparse labels, d/n = 8 (experiment only; their theory is the ridge path). What stays ours: l2, Gaussian mixture, n >= d, minimum at the mean estimator, size of the rise from Gordon. A GD-path proof is still missing.

Folder: research-repo research_pushes/2026-10-31-t360-adversarial-time
