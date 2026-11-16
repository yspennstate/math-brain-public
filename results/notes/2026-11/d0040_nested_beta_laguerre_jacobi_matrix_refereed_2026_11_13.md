---
name: d0040_nested_beta_laguerre_jacobi_matrix_refereed_2026_11_13
description: "[PROVISIONAL] Virag ICM 2014 Question 2 (nested beta-ensembles like Thm 4.1 beta-Hermite): yes for beta-Laguerre with fixed hard-edge exponent, two audits (referee MINOR)"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T08:41:10+02:00
  status: provisional
  evidence: ""
---

D0040 (Virag, Operator limits of random matrices, arXiv:1804.06953, Question 2 p.6). Claim D0040A, referee D0040AR MINOR, 13 Nov 2026. Proved: reversing and transposing the Dumitriu-Edelman bidiagonal Laguerre model gives ONE infinite Jacobi matrix whose leading n x n blocks have the unscaled beta-Laguerre law with hard-edge power beta(a+1)/2-1 for every n at once; the chi laws do not depend on n (the DE shape parameter does, stated correctly). Also: antisymmetric Gaussian beta ensemble nests; obstructions (dimension count vs full corners processes, reversed Jacobi candidate fails, ordinary unitary principal minors fail, two restricted Gaussian characterisations). Open: beta-Jacobi, one-cut potentials, a classification. Referee fixes: arXiv:1905.08684v2 eq (28)/(29) Hua-Pickrell parameter convention is wrong as printed for theta!=1 (s=0 is not CbetaE; use s=1-theta); add Valko-Virag Sine_beta operator 2017 Prop 20/Thm 21, Valko-Virag circular operator limit 2020 Thm 1, Krishnapur-Rider-Virag 2016. The answer is existential, not a classification. Elementary consequence of published models: a short note at most. Archives D0040A 56233d41 and D0040AR on the brain repo; ledger row in probability_1000_intake_D_20260908. Follow-on run D0043A (Conjecture 5, exotic edge operators) launched 13 Nov. status: provisional

POSTED 13 Nov 2026 (workstation ~15:50): paper D0040P (8 pp, Virag Q2 Laguerre case) refereed D0040PR MINOR (28 findings, all text/citation fixes applied: matrix product not entrywise, Dirichlet vector wording, notation before first use, Section 6 of Dumitriu-Forrester credited, KN eq refs, CMV expanded, added Anderson 1991 + Forrester 2010 Prop 4.2.1 + Kawamoto-Shibukawa Lemma 1.1 for Dixon-Anderson, Bufetov-Kawamoto JSP 2025 and Kawamoto-Shibukawa ALEA 2026 fixed-parameter kernels). Public repo github.com/yspennstate/nested-beta-laguerre commit 31ca4080. Lesson: a long \Dir(theta,...,theta) inline breaks into the margin; reword so it ends a sentence.
