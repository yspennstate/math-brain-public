---
name: t248_row_centered_ck_tracy_widom_edge_posted_2026_11_16
description: "T248 posted: largest eigenvalue of the row-centered conjugate kernel of a one-layer random-feature network (polynomial activation) has Tracy-Widom fluctuations; proof via Chen-Lyu edge universality with a quadratic form bound from hypercontractivity (Zenodo 24246777)"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T00:20:03+02:00
  status: verified
  evidence: "fillq_ctl/t248_public/paper/main.tex"
---

T248, posted (paper "Tracy-Widom fluctuations for the row-centered conjugate kernel", public repo row-centered-conjugate-kernel-tracy-widom, Zenodo 10.5281/zenodo.24246777; source fillq_ctl/t248_public/paper/main.tex).

Result: Y = sigma(WX/sqrt d) with W an m x d standard Gaussian matrix, the N data columns uniform on the sphere of radius sqrt d, and sigma a fixed polynomial with E sigma(Z) = E[Z sigma(Z)] = 0. With m, d, N proportional and m != N asymptotically, the largest eigenvalue of the row-centered kernel K_P = Y P Y^T / N (P removes each row's mean over the data) has Tracy-Widom fluctuations of order N^{-2/3} around v(1+sqrt(m/N))^2, v = E sigma(Z)^2. The same holds for the uncentered Y Y^T / N when a_2^2 N/d < v sqrt(N/m) (a_2 the second Hermite coefficient); above that, a He2 spike sits above the edge.

Method: conditionally on the data, the edge universality theorem of Chen and Lyu (Corollary 1.4: sample covariance with independent, not necessarily independent-entry, sample vectors satisfying a quadratic form bound). For polynomial features the quadratic form bound follows from the Gaussian Poincare inequality and hypercontractivity, with dimension-free constants. Prior work: Pennington-Worah, Louart-Liao-Couillet, Benigni-Peche, Fan-Wang, Wang-Wu-Fan; edge fluctuations had not been determined.

Plain words: the top eigenvalue of a random one-layer network's feature Gram matrix wobbles like the top eigenvalue of a classical random covariance matrix, once each feature row is centered.

Earlier notes on the same problem: [[t248_gaussian_inputs_put_a_he2_spike_above_the_ck_edge_2026_10_30]], [[t248_hek_outlier_is_the_heaviest_row_rho2_over_rho_minus_1_2026_10_20]], [[t248_ck_ipn2_eps03_places_the_edge_on_three_reps_2026_10_21]]. Why this memory exists: the 16 Nov posted-abstract recall probe missed the Chen-Lyu wording because no memory stated the posted theorem (fillq_ctl/recall_probe_1115_RESULTS.md).

