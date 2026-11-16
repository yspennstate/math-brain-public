---
name: e0057_mra_mle_consistency_marginal_known_quasi_mle_open_2026_11_13
description: "E0057 (Bandeira Open Problem 10.4, consistency of the MLE for multireference alignment) on 13 Nov 2026: the marginal MLE is consistent for every signal (Brunel COLT 2019) and the generic sample complexity is sigma^6 (Perry-Weed-Bandeira-Rigollet-Singer 2019); open is the source's hard-assignment quasi-MLE (109)-(110) after power correction - its population minimizer set is not identified. The Einstein-from-noise / confirmation-bias papers (Balanov-Bendory-Huleihel 2408.09718; Yin-Ling 2611.13546, Nov 2026) treat one align-and-average step, not the global quasi-MLE"
metadata:
  node_type: memory
  status: provisional
  type: project
  modified: 2026-11-13T15:35:11.252Z
---

E0057, rank 37 on the 200 list. Source: Bandeira, "Ten lectures and forty-two open problems", Open Problem 10.4 (ETH
copy p.139). It asks whether the quasi-MLE (109)-(110) (pp.136-137) gives consistent Fourier phases once its power
spectrum is fixed. The quasi-MLE minimizes jointly over the signal and each observation's shift, so it is a hard
assignment.

Status 13 Nov 2026: partial.
- Settled in print, and checked with page numbers in the Codex run E0057A
  (06_math_research/referee_reports/2026-11-13/E0057A/REPORT.md):
  - Brunel, COLT 2019, Theorem 9: the marginal MLE (the Gaussian mixture over the orbit) is consistent for every
    signal; symmetric signals add an n^{-1/4} term.
  - Perry-Weed-Bandeira-Rigollet-Singer, SIMODS 2019: generic sample complexity sigma^6.
  - Bandeira-Rigollet-Weed, appendix B: nongeneric (harmonic) signals break any universal sigma^6 law.
  - Fan-Sun-Wang-Wu (arXiv 2004.00041): the likelihood landscape has spurious high-noise optima for even L >= 6.
  - Katsevich-Bandeira (arXiv 2006.15202) and Dou-Fan-Zhou (AoS 2024) cover nearby models.
- Open: consistency of the quasi-MLE's phases at fixed sigma > 0, for both readings of "fix the power" (correct
  afterwards, or constrain during the minimization). E0057A narrows the gap to population identification: the
  minimizers of Q(x) = E min_l ||R_l x - y||^2 are not known to be the true orbit, with or without a power constraint.
- Nearest new literature, checked on arXiv 13 Nov:
  - Balanov, Bendory, Huleihel, "Confirmation bias in Gaussian mixture models", arXiv 2408.09718.
  - Yin and Ling, "Statistical analysis of the structure from noise phenomenon in generalized Procrustes problems",
    arXiv 2611.13546 (10 Nov 2026).
  - Both show that one hard step of aligning to a template and averaging reproduces the template's structure, even
    from pure noise. That is evidence that fixed points of hard alignment are plentiful. It is not a statement about
    the quasi-MLE's global minimizer, so it neither proves nor refutes Bandeira's conjecture.
- Unchecked lead, derived by heuristic and not verified: for Gaussian noise, max_l <R_l x, w> depends on x only
  through its autocorrelation, so the phases of x are invisible to the noise part of Q. Phase information should then
  enter the large-sigma expansion of Q first at third order, through the bispectrum, as in the sigma^6 theory. The
  conjecture would follow from showing that this third-order term is uniquely maximized at the true phases (up to
  shift) for generic signals. This is the step to attempt next, in the hard-loss analogue of Katsevich-Bandeira's
  moment expansion.

Related: [[e0055_projected_power_phase_sync_open_constant_snr_gao_zhang_o_sqrt_n_2026_11_13]] (the previous Bandeira
item on the list).
