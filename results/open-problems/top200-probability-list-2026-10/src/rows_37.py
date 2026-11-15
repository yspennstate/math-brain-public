# Added 14 Nov 2026 by an agent: replacement for T339 (no kept candidate in REPLACEMENTS_1113b; new candidate).
ROWS = [
 {'id': 'T469',
  'd': 'NNT',
  't': 'How much overparameterization does alternating least squares need to decompose a tensor?',
  's': 'Let T = sum_{j<=r} a_j (x) b_j (x) c_j in R^{n x n x n} with r much smaller than n, where each factor is an '
       'arbitrary well-conditioned vector plus independent Gaussian noise N(0, sigma^2 I_n / n), sigma = 1/poly(r) '
       '(smoothed setting). Run alternating least squares (or gradient descent) on min || T - sum_{i<=k} x_i (x) y_i '
       '(x) z_i ||_F from random initialization with algorithmic rank k >= r. (a) Does some k = o(r^2) suffice to '
       'reach relative error eps in time poly(n, r, log(1/eps)) with high probability? (b) Or is there an absolute '
       'c > 0 such that with k <= r^{1+c} these methods converge to a point of positive objective with constant '
       'probability? The general question is the least k(r) for which the iterative methods reach a global optimum.',
  'c': 'Arvanitakis, Srinivas and Vijayaraghavan prove that a parallel variant of ALS with random initialization and '
       'k = O(r^2) converges to a global optimum, essentially independently of n; earlier, Wang, Wu, Lee, Ma and Ge '
       'needed k = O(r^{7.5} log n) for a gradient method. The proof needs the Khatri-Rao features x_i (.) y_i to span '
       'all pairwise products of the true factors, which forces k of order r^2, and experiments suggest superlinear '
       'overparameterization is necessary. Algebraic methods (simultaneous diagonalization, Koszul-Young flattenings) '
       'already decompose such tensors in polynomial time; the question is about the iterative methods. A toy model of '
       'feature learning under overparameterization; T212 (tensor PCA) is a detection threshold, not this.',
  'src': 'D. Arvanitakis, V. Srinivas and A. Vijayaraghavan, Open Problem: How much overparametrization is needed for '
         'ALS in tensor decomposition?, COLT 2026, PMLR 336. D. Arvanitakis, V. Srinivas and A. Vijayaraghavan, '
         'Guarantees for alternating least squares in overparameterized tensor decompositions, NeurIPS 38 (2025). '
         'X. Wang, C. Wu, J. D. Lee, T. Ma and R. Ge, Beyond lazy training for over-parameterized tensor decomposition, '
         'NeurIPS 33 (2020). R. Ge and T. Ma, On the optimization landscape of tensor decompositions, NeurIPS 30 (2017).',
  'loc': 'Arvanitakis-Srinivas-Vijayaraghavan, COLT 2026 open problem, Section 2: Open Problem 1 (least k(r)), Open '
         'Problem 2 (k = o(r^2) suffices), Open Problem 3 (lower bound k >= r^{1+c}). Read from the PMLR PDF on '
         '14 Nov 2026.',
  'url': 'https://proceedings.mlr.press/v336/arvanitakis26a.html',
  'why': 'It is the simplest setting in which to ask exactly how much overparameterization a local method needs to '
         'find the planted features, the question behind overparameterized training of networks.',
  'st': 'Open: posed at COLT 2026; the best upper bound is k = O(r^2) and no superlinear lower bound is proved; the '
        'authors suspect a lower bound holds even for random tensors.',
  'n': 'Added 14 Nov 2026 by an agent. Replaces T339 (approximation rates of generative networks: loose '
       'statement, unverified locator).'},
]
