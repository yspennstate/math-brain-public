# Added 13 Nov 2026 by an agent: replacement for T415 (screen REPLACEMENTS_1113b_SCREENED.tsv, candidate C14).
ROWS = [
 {'id': 'T465',
  'd': 'NNT',
  't': 'Greedy low-rank learning in deep matrix factorization beyond the first phase',
  's': 'Let f be a convex loss on symmetric d x d matrices (for example matrix sensing with a low-rank ground truth), '
       'fix depth L >= 3, and run gradient flow on f(W_1 ... W_L) from the scaled identity initialization of size '
       'alpha. Li, Luo and Lyu prove that as alpha -> 0 the trajectory converges to the deep greedy low-rank learning '
       '(deep GLRL) trajectory, and that in the first phase the r-low-rankness of the limit is O(alpha), only a '
       'constant factor above the initialization, whereas at depth 2 it is raised to a power below one. Prove that the '
       'same holds in every later phase r = 2, 3, ..., so that the solution gradient flow reaches stays within '
       'O(alpha) of the rank-r deep GLRL point, or show that it fails.',
  'c': 'T234 is the depth-2 (U U^T) matrix-sensing case, where greedy low-rank learning is a theorem along the whole '
       'trajectory; this row asks for the multi-phase statement at depth L >= 3. Razin and Cohen showed that no norm '
       'explains the bias in deep matrix factorization, which is why the question is posed as rank-incremental '
       'learning rather than norm minimization.',
  'src': 'Z. Li, Y. Luo and K. Lyu, Towards Resolving the Implicit Bias of Gradient Descent for Matrix '
         'Factorization: Greedy Low-Rank Learning, ICLR 2021, arXiv:2012.09839. Background: N. Razin and N. Cohen, '
         'Implicit Regularization in Deep Learning May Not Be Explainable by Norms, NeurIPS 2020, arXiv:2005.06398.',
  'loc': 'Li-Luo-Lyu Section 6: Theorem 6.2, Definition 6.3, Theorem 6.4 and the paragraph "Interpretation for the '
         'advantage of depth with multiple phases" ("we ... speculate it to be true for later phases").',
  'url': 'https://arxiv.org/abs/2012.09839',
  'why': 'It is the cleanest open form of the claim that depth itself pushes gradient descent toward low rank, the '
         'question behind most implicit-bias work on linear networks.',
  'st': 'Open as stated in the source: the first phase is a theorem, later phases are supported by experiments '
        '(their Figure 2). The source also assumes ||grad f(0)||_2 = lambda_1(-grad f(0)) and says it believes '
        'this assumption can be removed.',
  'n': 'Added 13 Nov 2026 by an agent from the DL candidate screen (C14); locator read from the arXiv HTML of '
       '2012.09839 on 13 Nov. Replaces T415 (an empirical law with no mathematical statement).'},
]
