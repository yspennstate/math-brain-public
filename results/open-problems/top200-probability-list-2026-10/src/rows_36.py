# Added 14 Nov 2026 by an agent: replacement for T420 (no kept candidate in REPLACEMENTS_1113b; new candidate).
ROWS = [
 {'id': 'T468',
  'd': 'NNL',
  't': 'Is the power of deep learning over linear models inherently distribution dependent?',
  's': 'The dimension complexity dc(H) of a class H of functions X -> {-1,1} is the least d such that some feature map '
       'phi: X -> R^d linearly realizes every h in H (h(x) = sign <w_h, phi(x)>). (a) Over X = {-1,1}^n, suppose a '
       'fully connected ReLU network with S parameters, Gaussian initialization of variance 1/fan-in, logistic loss and '
       'T steps of online SGD learns H to expected error eps < 1/4 under every input distribution D and every target '
       'h in H. Is dc(H) <= C T S for an absolute constant C? (b) If H is (m, tau)-SQ learnable to error eps < 1/4 '
       'under every input distribution, is dc(H) <= C m / tau^2? Polynomial bounds poly(S, T) or poly(m, 1/tau, n), '
       'and the probabilistic dimension complexities dc_{1/2} and dc_eps, are also asked.',
  'c': 'Every known separation between SGD-trained networks and linear or kernel models (parities on a mixed '
       'distribution, the staircase property of Abbe et al.) uses one fixed input distribution. The converse of (b) '
       'holds up to a dependence on n through the Dunagan-Vempala halfspace algorithm, and distribution-independent '
       'CSQ learnability is equivalent to polynomial margin complexity (Feldman 2008). A claimed bound of Karchmer and '
       'Malach (2025) on an approximate dimension complexity of SQ-learnable classes has a flaw (Karchmer and Malach '
       '2026). T302 asks whether standard SGD can learn parities beyond SQ; this row asks whether learning under all '
       'distributions collapses to linear models.',
  'src': 'V. Feldman, P. Kamath and N. Srebro, Invited Open Problem: Is the Power of Deep Learning over Linear Models '
         'Inherently Distribution Dependent?, COLT 2026, PMLR 336, 7117-7122. S. Ben-David, N. Eiron and H. U. Simon, '
         'Limitations of learning via embeddings in Euclidean half spaces, JMLR 3 (2002). E. Malach, P. Kamath, E. Abbe '
         'and N. Srebro, Quantifying the benefit of using differentiable learning over tangent kernels, ICML 2021, '
         'arXiv:2103.01210.',
  'loc': 'Feldman-Kamath-Srebro, Open Question 1 (Section 2, SGD learning vs. dimension complexity) and Open Question '
         '2 (Section 3, SQ learning vs. dimension complexity); relaxations in Section 4. Read from the PMLR PDF on '
         '14 Nov 2026.',
  'url': 'https://proceedings.mlr.press/v336/feldman26a.html',
  'why': 'It asks whether what gradient-trained networks gain over linear and kernel models comes only from fitting '
         'the input distribution, or survives the worst case; a yes to (a) would bound the representational power '
         'of benign SGD by linear models of the same cost.',
  'st': 'Open: posed as an invited open problem at COLT 2026 (San Diego, June-July 2026); the authors know no '
        'counterexample to either bound, even for deterministic dimension complexity.',
  'n': 'Added 14 Nov 2026 by an agent. Replaces T420 (deep learning as a renormalization group flow: no '
       'precise mathematical statement).'},
]
