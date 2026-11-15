# Famous-list addition, 15 Nov 2026 (an agent): percolation of the contact process's upper invariant measure on Z^d.
# Sources read on 15 Nov 2026: Liggett-Steif (arXiv math/0504530v1, Section 3(a) and Section 8, Question 2), the abstract
# of Rath-Valesin (arXiv:1912.09825v3), and the introduction of Fernley-Jacob (arXiv:2609.09972v1, 9 Sep 2026), which
# still calls the nearest-neighbour question on Z^d, d >= 2, a difficult open problem.
ROWS = [
 {'id': 'T479',
  'd': 'IPS',
  't': 'Percolation of the upper invariant measure of the contact process on Z^d: is the percolation threshold above the survival threshold?',
  's': 'For the nearest-neighbour contact process on Z^d, d >= 2, with infection rate lambda, let nu-bar be the upper invariant '
       'measure (the limit law started from all sites infected), non-trivial exactly when lambda > lambda_c. Let lambda_p be '
       'the threshold above which the infected set under nu-bar has an infinite nearest-neighbour cluster. Is lambda_p > '
       'lambda_c, that is, is there lambda > lambda_c for which nu-bar does not percolate?',
  'c': 'Liggett and Steif showed that nu-bar dominates the product measure of density (lambda - 2)/lambda for lambda >= 2, so '
       'nu-bar percolates on Z^d, d >= 2, once lambda >= 6.25; on Z, lambda_p is infinite. Rath and Valesin proved, for the '
       'spread-out process of range R, that lambda_p(R) tends to 1/(1 - p_c) and that lambda_p(R) > lambda_c(R) for R '
       'large, answering the question in the spread-out case. Fernley and Jacob proved lambda_1 < lambda_p on the regular '
       'tree T_d for every d >= 3, which they describe as the first such result on a graph with finite lambda_p.',
  'src': 'T. M. Liggett and J. E. Steif, Stochastic domination: the contact process, Ising models and FKG measures, Ann. Inst. '
         'H. Poincare Probab. Statist. 42 (2006), 223-243, doi:10.1016/j.anihpb.2005.04.002, arXiv:math/0504530.',
  'loc': 'Section 8, "Some open questions", Question 2: "For d >= 2, does there exist lambda > lambda_c such that nu-bar does '
         'not percolate? (In words, is the critical value for percolation different than the usual critical value?)"',
  'url': 'https://arxiv.org/abs/math/0504530',
  'why': 'It asks whether the stationary state of the basic interacting particle system changes its geometry at a point of its '
         'own, separate from survival. The answer needs control of the near-critical upper invariant measure, which has '
         'long-range positive correlations and no known comparison with a product measure close to lambda_c. Liggett and '
         'Steif observe that a positive answer to their Question 1, a stochastic comparison between nu-bar just above lambda_c and product measure, would give a positive answer here.',
  'st': 'Open for the nearest-neighbour process as of the sources read: Fernley and Jacob (arXiv:2609.09972, September 2026) '
        'state that lambda_1 < lambda_p on Z^d, d >= 2, "remains a difficult open problem"; the spread-out case is solved '
        '(Rath-Valesin, Ann. Inst. Henri Poincare Probab. Stat. 58 (2022) 1808-1848). A full literature search was not done.',
  'n': 'Added 15 Nov 2026 by an agent from the contact-process source scan. Different from T099 (critical exponents '
       'and directed-percolation universality) and T475 (the one-dimensional critical value).'},
]
