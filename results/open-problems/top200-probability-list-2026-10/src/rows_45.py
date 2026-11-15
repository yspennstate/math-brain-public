# Famous-list addition, 15 Nov 2026 (an agent): percolation of the voter model's stationary measures in d = 3, 4.
# Sources read on 15 Nov 2026: the arXiv v2 text of Rath-Valesin (Theorems 1.1, 1.2 and the paragraph after them), the
# Crossref records of its journal version and of Rath-Valesin ECP 2017, and the introduction of the 2024 stirring paper
# (arXiv:2412.09532v2), which still describes the nearest-neighbour result as d >= 5 only.
ROWS = [
 {'id': 'T478',
  'd': 'PERC',
  't': 'Percolation phase transition for the stationary measures of the nearest-neighbour voter model in dimensions three and four',
  's': 'For the nearest-neighbour voter model on Z^d, d >= 3, the extremal stationary laws are a family mu_alpha, alpha in '
       '[0, 1], where alpha is the density of 1s; a sample has correlations decaying like |x - y|^(2-d). Viewing the set of 1s '
       'as a site percolation configuration, show for d = 3 and d = 4 that there is a critical alpha_c in (0, 1) with no '
       'infinite cluster below it and an infinite cluster above it.',
  'c': 'Rath and Valesin proved the non-trivial phase transition for d >= 5 and every range R >= 1 (Theorem 1.1), and for '
       'd = 3, 4 when the voter model is spread out with range R at least some R_0(d) (Theorem 1.2); for large R the '
       'threshold tends to Bernoulli site percolation\'s p_c (Rath-Valesin, ECP 2017). Simulations for d = 3, R = 1 '
       '(Lebowitz-Saleur 1986 and later numerical work cited there) indicate a transition with exponents different from '
       'independent percolation.',
  'src': 'B. Rath and D. Valesin, Percolation on the stationary distributions of the voter model, Ann. Probab. 45 (2017), '
         '1899-1951, doi:10.1214/16-AOP1104, arXiv:1502.01306.',
  'loc': 'arXiv v2, after Theorem 1.2: "Theorems 1.1 and 1.2 leave open the cases of dimension 3 and 4 and range R small, '
         'even though ... simulations and numerical work suggest that non-trivial phase transition should also occur"; '
         'Remark 7.3 explains why the method fails for d = 3, 4, R = 1.',
  'url': 'https://arxiv.org/abs/1502.01306',
  'why': 'The voter measures are a basic example of percolation with slowly decaying, non-summable correlations in low '
         'dimension, the regime where the tools of Bernoulli percolation fail. The coalescing-walk representation gives an '
         'explicit handle that Gaussian level sets do not have, so the question tests whether that structure can replace '
         'the decorrelation inequalities the known proofs need.',
  'st': 'Open as of the sources read: the 2024 voter-model-with-stirring paper (arXiv:2412.09532v2) still states the '
        'nearest-neighbour result as d >= 5 and the spread-out result for d >= 3. An arXiv search on 15 Nov 2026 found no '
        'later claim for d = 3, 4 with R = 1; a full literature search was not done.',
  'n': 'Added 15 Nov 2026 by an agent from the voter-model source scan. Different from the Lotka-Volterra '
       'coexistence row: that one is about the dynamics, this about the geometry of the invariant laws.'},
]
