---
name: dg08_cartan_hadamard_solved_2026_key_inequality_checked_2026_11_12
description: "Cartan-Hadamard conjecture solved 2026: Chen-Ghomi-Wang 2609.20517 (n 3..9); every n and kappa<=0 via a sharp hypersurface Sobolev (L2 Michael-Simon) inequality - OpenAI 23 Sep 2026, Agnoletto et al 2610.37817, Case-Mengesha 2610.12309. Inequality proof re-derived, 150 numeric cases pass; regularity and rigidity unread; unrefereed"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T04:08:59+02:00
  status: provisional
  evidence: "06_math_research/dg08_cartan_hadamard_agent_2026_11_12/DG08_CHECK.md, dg08_check.out; push b27778db2713a4a319dc0d190707b949743d43cd"
---

Row DG08 of the top-200 general list (Cartan-Hadamard conjecture: the Euclidean, or model-space, isoperimetric inequality in complete simply connected manifolds with sectional curvature at most kappa <= 0) is solved in 2026 by two routes.

Route 1: Chen, Ghomi, Wang, arXiv 2609.11005 (n = 5) and 2609.20517 (3 <= n <= 9, kappa = 0, with rigidity): integrals over pairs of boundary points, Jacobi fields along chords, then Kleiner's confined profile.

Route 2: a sharp critical Sobolev inequality on hypersurfaces, int 4/(m-2)|grad v|^2 + m(h^2 - b^2)v^2 >= m|S^m|^(2/m) ||v||_q^2 (m = n-1 >= 3, q = 2m/(m-2), h the normalized mean curvature, sec <= -b^2). OpenAI preprint of 23 Sep 2026 (openai/math, number 337, 42 pages) proves it and gets the conjecture for every n and kappa <= 0 by one ODE: I'(v) >= m sqrt(b^2 + (s_m/I)^(2/m)), integrated against the model. Agnoletto, Da Silva, Nardulli, Resende, arXiv 2610.37817, give their own proof of the inequality and rigidity for every kappa. Case, Mengesha, arXiv 2610.12309, prove the Euclidean case independently. With v = 1 on a CMC hypersurface the inequality is exactly Chen-Ghomi-Wang's Theorem 1.2, so the two routes agree where they meet.

Checked by us: the proof of the inequality in 2610.37817 by hand (comparison map to the sphere, completed square, Brezis-Lieb minimizer, balancing); the model identities and the algebra symbolically; equality on 45 model spheres; 150 numerical cases in R^4..R^6 (lowest ratio 1.000000 on the round sphere). The step from the inequality to the profile (OpenAI Lemma 5.4 to Theorem 5.6) by hand. Not checked: regularity of confined minimizers, finite-volume passage, both rigidity arguments, the Chen-Ghomi-Wang proof. All sources unrefereed, none in the Lean index.

How to apply: do not work DG08 as open. The least-checked claim is rigidity for kappa < 0 (only in 2610.37817). Same routine as [[ag10_cubic_fourfold_solved_2025_hassett_claim_unverified_2026_11_12]] and [[nt02_landau_siegel_zeros_excluded_proof_read_in_full_2026_11_12]].

Evidence: 06_math_research/dg08_cartan_hadamard_agent_2026_11_12/DG08_CHECK.md, dg08_check.out.

