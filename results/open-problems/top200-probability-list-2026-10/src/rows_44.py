# Famous-list addition, 15 Nov 2026 (an agent): the two-colour stable matching of Poisson processes. The list had
# the Poisson-Lebesgue allocation (T454) but not this question. Sources read on 15 Nov 2026: the arXiv v3 text of
# Holroyd-Pemantle-Peres-Schramm (Theorem 6, Theorem 19 and the Open Problems section), the Crossref record for its
# journal version, and the arXiv abstracts of Holroyd-Martin-Peres (1708.04519) and Holroyd-Janson-Wastlund (2012.07129).
ROWS = [
 {'id': 'T477',
  'd': 'GEOM',
  't': 'The tail exponent of two-colour stable matching of Poisson processes in dimension two and higher',
  's': 'Let red and blue points form independent unit-intensity Poisson processes in R^d, d >= 2, and match them by the '
       'Gale-Shapley stable marriage (iteratively matching mutually closest red-blue pairs). Let X be the distance from '
       'a typical point to its partner. Determine the power law of the tail of X; Holroyd, Pemantle, Peres and Schramm '
       'conjecture that E X^a is finite if and only if a < d/2.',
  'c': 'Holroyd, Pemantle, Peres and Schramm proved, for every d >= 1, that E X^d is infinite and that P(X > r) <= C r^(-s(d)) '
       'with s(d) in (0, 1) the root of an explicit equation, s(1) = 1/2, s(2) = 0.496..., s(3) = 0.449... (their '
       'Theorems 6 and 19). For any translation-invariant two-colour scheme, E X^(d/2) is infinite in d = 1 and 2, while '
       'in d >= 3 schemes with finite exponential moments exist, so stable matching is close to optimal in d = 1 and far '
       'from it in d >= 3. They call the correct power law for d >= 2 a fascinating unsolved question and list it as '
       'their first open problem; the second asks for a translation-invariant two-colour matching in R^2 whose segments '
       'do not cross.',
  'src': 'A. E. Holroyd, R. Pemantle, Y. Peres and O. Schramm, Poisson matching, Ann. Inst. Henri Poincare Probab. Stat. '
         '45 (2009), 266-287, doi:10.1214/08-AIHP170, arXiv:0712.1867.',
  'loc': 'arXiv v3, after Theorem 6: "It is a fascinating unsolved question to determine the correct power law for d >= 2"; '
         'Open Problems (i): "what is the correct power law for the tail behavior of X in dimensions d >= 2? We conjecture '
         'that E*X^a < infinity if and only if a < d/2."',
  'url': 'https://arxiv.org/abs/0712.1867',
  'why': 'Stable matching is the canonical local, greedy way to pair two random point clouds, and its tail measures how '
         'far the greedy rule is from optimal transport. The gap between the proved exponent s(2) = 0.496... and the '
         'conjectured d/2 = 1 is wide, and closing it needs a handle on the long chains of displaced partners that the '
         'greedy rule creates, the same structure that controls the Poisson-Lebesgue allocation tails.',
  'st': 'Open as of the sources read: Holroyd, Martin and Peres (arXiv:1708.04519, 2017) treat an asymmetric colour '
        'restriction in high dimension and Holroyd, Janson and Wastlund (arXiv:2012.07129, 2020) the gamma-minimal '
        'matchings, focusing on d = 1; neither abstract claims the d >= 2 exponent. A full literature search beyond '
        'these was not done.',
  'n': 'Added 15 Nov 2026 by an agent, one of the famous places freed by the retirements. Related to T454 (the '
       'Poisson-Lebesgue allocation tail) but a different model: two random point sets, no Lebesgue side.'},
]
