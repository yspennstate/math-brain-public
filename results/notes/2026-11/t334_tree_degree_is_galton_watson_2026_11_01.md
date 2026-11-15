---
name: t334_tree_degree_is_galton_watson_2026_11_01
description: [PROVISIONAL] T334: tree of alpha(u+w)+beta uw has Fourier degree = Galton-Watson generation; kernel degree d^gamma, gamma = log2(2-2alpha^2) < 1; degree-2 learner d^(2log2(1/alpha)); exponential kernel cost forces alpha = 0
metadata:
  type: project
  created: 2026-10-31
  created_at: 2026-10-31T22:50:25+04:00
  status: provisional
  evidence: ""
  originSessionId: b9a49845-179c-4e8f-8401-adcc0c5c2952
---



T334 (deep vs kernel separation), target 1, 1 Nov. The row proposed a binary tree with constituents that have a linear term, so each level carries signal while the degree grows. For multilinear constituents g = alpha(u+w) + beta uw this is exactly solvable. The spectral generating function iterates phi(s) = 2 alpha^2 s + beta^2 s^2, so the degree is generation h of a Galton-Watson tree.

Kernels need degree d^gamma, with gamma = log2(2 - 2 alpha^2) < 1. At any polynomial sample size kernel ridge has error -> 1. A bottom-up degree-2 learner needs d^(2 log2(1/alpha)) samples. Exponential kernel cost forces alpha = 0, the parity tree, where the learner has no signal. So the row's exponential-in-d goal is out of reach for this family; superpolynomial is what it gives.

Checked with an exact Walsh transform at d = 16 (8e-15) and polynomial iteration to d = 1.7e7. Pushed research_pushes/2026-11-01-loop-T334-tree-degree-law (a6c7d29); card claim_091def21a206481db7b7b7728c86c03f (links: Kesten-Stigum, spectral sample, the T277 card); frontier move.

Scar: brain.py remember refuses slugs that are too long, and the round-close script went on to say "closed" anyway. Keep slugs under about 50 characters.

Related: [[t277_g_of_quadratic_form_is_csq_easy_above_op_norm_floor_2026_11_01]] (another degree-2 correlational learner). [[t274_mean_field_ticket_lags_rescaled_random_subnet_matches_full_2026_11_01]] (same session).
