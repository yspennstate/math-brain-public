# Famous-list replacements, 14 Nov 2026 (an agent), from the candidate screen and arXiv check in
# 06_math_research/top200_vet_agent_2026_11_11/FAMOUS_LITCHECK_1114.md.
ROWS = [
 {'id': 'T472',
  'd': 'SM',
  't': 'Polynomial mixing of the critical two-dimensional Potts model with four colours',
  's': 'Consider heat-bath Glauber dynamics (or Swendsen-Wang dynamics) for the q-state Potts model on the '
       'n x n torus at its critical inverse temperature, and Glauber dynamics for the critical FK random-cluster '
       'model with parameter q on the same torus. For 1 < q <= 4, where the phase transition is continuous, the '
       'inverse spectral gap is expected to grow polynomially in n. Prove this for q = 4, and for the FK dynamics '
       'at every non-integer q in (1, 4).',
  'c': 'For q = 2 (Ising) the critical dynamics mixes in polynomial time (Lubetzky and Sly). For q = 3 the inverse '
       'gap of critical Glauber dynamics is n^{O(1)}, while for q = 4 the best bound is n^{O(log n)} (Gheissari and '
       'Lubetzky, 2016); the same quasi-polynomial bound holds for the critical FK dynamics at every q in (1, 4]. '
       'For q > 4 the transition is discontinuous and the mixing time on the torus is exponential in n. T104 and '
       'T168 are mixing-time questions for other chains; T013 (conformal invariance of critical FK clusters) is '
       'the geometric input such arguments would draw on.',
  'src': 'E. Lubetzky and A. Sly, Critical Ising on the square lattice mixes in polynomial time, arXiv:1001.1613. '
         'R. Gheissari and E. Lubetzky, Mixing times of critical 2D Potts models, arXiv:1607.02182. R. Gheissari '
         'and E. Lubetzky, Quasi-polynomial mixing of critical 2D random cluster models, arXiv:1611.01147.',
  'loc': 'Gheissari and Lubetzky, arXiv:1607.02182, abstract (read from the arXiv API on 14 Nov 2026): the inverse '
         'spectral gap "should at criticality be polynomial in n for 1 < q <= 4"; they prove n^{O(1)} for q = 3 and '
         '"for q = 4, it is at most n^{O(log n)}". arXiv:1611.01147, abstract: an upper bound of n^{O(log n)} at '
         'p = p_c for all q in (1, 4], the critical slowdown being "believed" to give a power law.',
  'url': 'https://arxiv.org/abs/1607.02182',
  'why': 'Critical slowdown is the reason Monte Carlo at a continuous transition is hard, and q = 4 is the '
         'endpoint of the continuous regime, where logarithmic corrections make every estimate delicate; a '
         'polynomial bound there would complete the picture for the planar Potts family.',
  'st': 'Open as far as the arXiv record shows on 14 Nov 2026: no later paper on critical 2D Potts or FK mixing '
        'turned up in searches by author and by title, and the Semantic Scholar citation list of 1607.02182 has '
        'nothing after 2018 (its coverage is thin, so read the citing papers before quoting this as open).',
  'n': 'Added 14 Nov 2026 by an agent from famous candidate H11, restated after the arXiv check: '
       'Swendsen-Wang at criticality is settled for q = 2 and polynomial for q = 3, so the row asks for q = 4 and '
       'non-integer q. Replaces T013 (critical FK conformal invariance, retired as claimed solved).'},
]
