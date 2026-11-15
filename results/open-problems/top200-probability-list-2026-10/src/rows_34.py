# Added 13 Nov 2026 by an agent: replacement for T419 (screen REPLACEMENTS_1113b_SCREENED.tsv, candidate C18,
# restated after the conjecture it was built on was disproved).
ROWS = [
 {'id': 'T466',
  'd': 'NNT',
  't': 'Does exact ReLU representation of the maximum of n numbers need depth growing with n?',
  's': 'Every continuous piecewise-linear function on R^n is computed exactly by a ReLU network with '
       'ceil(log_3(n-1)) + 1 hidden layers, and max(x_1, ..., x_n) by one with ceil(log_3(n-2)) + 1 hidden layers '
       '(n >= 4). Decide whether, for ReLU networks with arbitrary real weights, the number of hidden layers needed '
       'to compute max(x_1, ..., x_n) exactly tends to infinity with n, or whether some fixed depth computes every '
       'continuous piecewise-linear function in every dimension.',
  'c': 'Hertrich, Basu, Di Summa and Skutella conjectured that ceil(log_2(n+1)) hidden layers are needed; Bakaev, '
       'Brunck, Hertrich, Stade and Yehudayoff disproved this (two hidden layers compute the maximum of five numbers). '
       'Lower bounds growing with n are known only for restricted weights: integer weights (Haase, Hertrich and Loho) '
       'and decimal-fraction weights, ceil(log_3 n) (Averkov, Hojny and Merkert). T383 counts linear regions of '
       'typical networks and T276 is about rank in deep networks; neither asks for exact depth.',
  'src': 'C. Hertrich, A. Basu, M. Di Summa and M. Skutella, Towards Lower Bounds on the Depth of ReLU Neural Networks, '
         'NeurIPS 2021 and SIAM J. Discrete Math. 37 (2023), arXiv:2105.14835. E. Bakaev, F. Brunck, C. Hertrich, '
         'J. Stade and A. Yehudayoff, Better Neural Network Expressivity: Subdividing the Simplex, arXiv:2505.14338 '
         '(v3, Feb 2026). C. Haase, C. Hertrich and G. Loho, Lower Bounds on the Depth of Integral ReLU Neural '
         'Networks via Lattice Polytopes, ICLR 2023. G. Averkov, C. Hojny and M. Merkert, ICLR 2025.',
  'loc': 'Bakaev et al. abstract (read from the arXiv API on 13 Nov 2026): the log_2 conjecture of Hertrich et al. '
         'is disproved, the upper bounds above, and "almost match the ceil(log_3(n)) lower bound of Averkov, Hojny, '
         'and Merkert (ICLR\'25) in the special case of ReLU networks with weights that are decimal fractions". The '
         'unbounded-depth question for real weights is the one the Hertrich et al. conjecture was posed to settle.',
  'url': 'https://arxiv.org/abs/2505.14338',
  'why': 'It is the basic question of what depth buys in ReLU networks, asked exactly rather than up to '
         'approximation; a fixed-depth answer would mean depth beyond a constant never helps exact representation.',
  'st': 'Open for real weights as far as the 13 Nov 2026 abstracts say: the 2021 conjecture is false, and every lower '
        'bound growing with n assumes integer or decimal-fraction weights. Read the open-questions section of '
        '2505.14338 before quoting this as their stated problem.',
  'n': 'Added 13 Nov 2026 by an agent from the DL candidate screen (C18), restated: the screened form (minimal '
       'width at depth k) was not the question the literature asks. Replaces T419 (LoRA, no precise statement and '
       'an unverified locator).'},
]
