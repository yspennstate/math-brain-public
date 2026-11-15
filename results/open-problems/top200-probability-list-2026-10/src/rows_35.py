# Added 13 Nov 2026 by an agent: replacement for T422 (no kept candidate in REPLACEMENTS_1113b; new candidate).
ROWS = [
 {'id': 'T467',
  'd': 'NNT',
  't': 'The optimal convergence exponent of gradient descent with a stepsize schedule',
  's': 'For L-smooth convex f on R^d run gradient descent x_{k+1} = x_k - (h_k / L) grad f(x_k) with a predetermined '
       'sequence of positive stepsizes h_k. (a) With the horizon N known in advance, find the largest p such that '
       'some schedule gives f(x_N) - min f = O(N^{-p}) for every such f; known: 1.2716 = log_2(1 + sqrt 2) <= p <= '
       '1.450. (b) Anytime: with one schedule fixed in advance and the bound required at every stopping time T, find '
       'the largest p with f(x_T) - min f = O(T^{-p}); known: 1.119 <= p <= 1.184. Determine either exponent.',
  'c': 'Constant stepsizes give Theta(N^{-1}); Nesterov momentum gives N^{-2}, so the question is how much of the '
       'acceleration a plain gradient method can recover through stepsizes alone. For the squared gradient norm the '
       'anytime rate cannot beat o(n^{-1}) (Tsai, Fatkhullin, Zhang and He). T230 and T295 are about sample '
       'complexity of gradient methods in statistical models, not about stepsize schedules.',
  'src': 'G. Kornowski and O. Shamir, Open Problem: Anytime Convergence Rate of Gradient Descent, COLT 2024, PMLR 247, '
         '5335-5339. J. M. Altschuler and P. A. Parrilo, Acceleration by Stepsize Hedging: Silver Stepsize Schedule '
         'for Smooth Convex Optimization, arXiv:2309.16530. Z. Zhang, J. D. Lee, S. S. Du and Y. Chen, Anytime '
         'Acceleration of Gradient Descent, arXiv:2411.17668. C.-E. Tsai, I. Fatkhullin, L. Zhang and N. He, Lower '
         'Bounds for Anytime Acceleration of Gradient Descent, arXiv:2607.02053. M. Jung, H. Cho and C. Yun, Stronger '
         'Lower Bounds for (Non-)Anytime Acceleration of Gradient Descent, arXiv:2609.04032.',
  'loc': 'Kornowski-Shamir (the open-problem note, whose question o(T^{-1}) anytime was answered yes by Zhang et al.); '
         'the current gaps are as stated in the abstract of Jung-Cho-Yun 2609.04032 v2 (read from the arXiv API, '
         '13 Nov 2026): upper O(N^{-1.271}) and O(N^{-1.119}), lower barriers Omega(N^{-1.450}) and Omega(N^{-1.184}). '
         'Tsai et al. 2607.02053 call the improvement of these upper bounds open.',
  'url': 'https://proceedings.mlr.press/v247/kornowski24a.html',
  'why': 'Large and non-monotone stepsizes are how networks are trained in practice; this is the cleanest setting in '
         'which their benefit can be measured exactly, and the silver-stepsize result showed it is a real one.',
  'st': 'Open: both exponents lie in intervals of positive length after the 2026 lower bounds. The original COLT '
        'question (any anytime rate o(T^{-1})) is settled in the affirmative by Zhang et al.',
  'n': 'Added 13 Nov 2026 by an agent. Abstracts of 2411.17668, 2607.02053 and 2609.04032 read from the '
       'arXiv API on 13 Nov 2026; the 1.2716 exponent is the silver rate quoted there as O(N^{-1.271}). Replaces '
       'T422 (critical batch size: an empirical quantity with no mathematical statement).'},
]
