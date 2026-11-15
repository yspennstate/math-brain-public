# Added 14 Nov 2026 by an agent: replacements for T386 and T412 (screening in ../top200_vet_agent_2026_11_11/SCREEN_REPL_T386_T412_1114.tsv).
ROWS = [
 {'id': 'T470',
  'd': 'NNT',
  't': 'Is there a first-order method that converges only to local minimax points?',
  's': 'Let f : R^n x R^m -> R be smooth and nonconvex-nonconcave, and call (x*, y*) a local minimax point in the sense '
       'of Jin, Netrapalli and Jordan: there are delta_0 > 0 and h(delta) -> 0 such that for all delta <= delta_0 and '
       'all |x - x*| <= delta, |y - y*| <= delta, f(x*, y) <= f(x*, y*) <= max over |y1 - y*| <= h(delta) of f(x, y1). '
       'Find a first-order method (gradient queries only) whose limit points, from almost every initialization, are '
       'exactly local minimax points: it converges locally to every local minimax point, or at least to every point in '
       'a natural class containing the non-strict ones (degenerate Hessian in y), and to no stationary point that is not '
       'local minimax. Alternatively, show that no such method exists for this notion and identify the notion of local '
       'optimality for which one does.',
  'c': 'Jin, Netrapalli and Jordan show that two-timescale gradient descent ascent with a large ratio converges only to '
       'strict local minimax points (second-order sufficient condition, Hessian in y negative definite), so it misses '
       'the non-strict ones, which are common in practice. Chae, Kim and Kim (arXiv:2305.16242) prove that two-timescale '
       'extragradient with a large ratio converges locally to a stationary point if and only if it satisfies a refined '
       'second-order necessary condition (a restricted Schur complement is positive semidefinite) together with a '
       'condition on the step size and a quantity s_0 < 1/(2L), and their open-problem note records the remaining gap '
       'between these limit points and the local minimax points. The note also gives a concave-linear quadratic with a '
       'non-strict local minimax point and no global one, which questions the definition itself. The motivation is GAN '
       'training, where convergence to a maximin rather than a minimax point is associated with mode collapse. T312 asks '
       'for global convergence of GAN dynamics; this row asks which local points a method can select.',
  'src': 'J. Chae, K. Kim and D. Kim, Open Problem: Is There a First-Order Method that Only Converges to Local Minimax '
         'Optima?, COLT 2023, PMLR 195. J. Chae, K. Kim and D. Kim, Two-timescale Extragradient for Finding Local Minimax '
         'Points, arXiv:2305.16242. C. Jin, P. Netrapalli and M. I. Jordan, What is local optimality in '
         'nonconvex-nonconcave minimax optimization?, ICML 2020. J. D. Lee, M. Simchowitz, M. I. Jordan and B. Recht, '
         'Gradient descent only converges to minimizers, COLT 2016.',
  'loc': 'Chae-Kim-Kim, COLT 2023 open problem: the question in the abstract and Section 1; Section 2.1 (Proposition 2, '
         'Theorem 3 and the remaining gap); Section 2.2 (alternative notion, Example 1). Read from the PMLR PDF on '
         '14 Nov 2026.',
  'url': 'https://proceedings.mlr.press/v195/chae23a.html',
  'why': 'Gradient descent provably avoids strict saddles and so selects local minima; whether any first-order method '
         'selects the right local points of a min-max problem is the corresponding question for adversarial training.',
  'st': 'Open: posed at COLT 2023; two-timescale extragradient reaches a refined second-order necessary condition with a '
        'gap to local minimax points; an arXiv abstract search on 14 Nov 2026 found no later answer.',
  'n': 'Added 14 Nov 2026 by an agent. Replaces T386 (agnostic single neuron by gradient descent: solved for '
       'Gaussian and log-concave marginals).'},
 {'id': 'T471',
  'd': 'NNP',
  't': 'The price of joint differential privacy in linear contextual bandits',
  's': 'In the linear contextual bandit with d-dimensional features, K actions per round, horizon T and adversarial '
       'contexts, determine the minimax regret of (epsilon, delta)-jointly differentially private policies (Shariff-Sheffet '
       'joint DP: changing the context and reward of round t does not change the distribution of the actions chosen after '
       'round t by more than the (epsilon, delta) margin). The best known upper bound is O(sqrt(dT log T) + '
       'd^(3/4) sqrt(T log(1/delta)/epsilon)) and the best known lower bound is Omega(sqrt(dT log K) + d/(epsilon + '
       'delta)). Close the gap; in particular decide whether joint DP is free, that is whether the privacy term can be '
       'made lower order in T for adversarial contexts, and if not, find the weakest assumption on how contexts are '
       'generated under which it is.',
  'c': 'For finite-armed and linear (non-contextual) bandits under DP the regret is known up to logarithmic factors and '
       'the privacy cost is an additive term that does not grow with sqrt(T) (Azize and Basu). In the contextual case the '
       'JDP variant of LinUCB of Shariff and Sheffet, which privatises the Gram matrix and the response sum with the tree '
       'mechanism, pays d^(3/4) sqrt(T) times a privacy factor, so the privacy cost is not negligible even asymptotically; '
       'the lower bound of He, Zhang and Zhang comes from a reduction of contextual regret to estimation and is proved for '
       'stochastic contexts. The mismatch is in both the horizon and the privacy dependence. Standard DP of the whole '
       'action sequence forces linear regret here, which is why joint DP is the relevant notion.',
  'src': 'A. Azize and D. Basu, Open Problem: What is the Complexity of Joint Differential Privacy in Linear Contextual '
         'Bandits?, COLT 2024, PMLR 247. R. Shariff and O. Sheffet, Differentially Private Contextual Linear Bandits, '
         'NeurIPS 2018 (arXiv:1810.00068). J. He, J. Zhang and R. Zhang, A reduction from linear contextual bandit lower '
         'bounds to estimation lower bounds, ICML 2022.',
  'loc': 'Azize-Basu, COLT 2024 open problem: questions Q1-Q3 in Section 1; Section 3 (existing upper bound, existing lower '
         'bound). Read from the PMLR PDF on 14 Nov 2026.',
  'url': 'https://proceedings.mlr.press/v247/azize24a.html',
  'why': 'Recommender systems and clinical-trial allocation run contextual bandits on personal data; whether privacy can be '
         'had at a lower-order cost there is the online-learning counterpart of the question whether private training '
         'must lose accuracy.',
  'st': 'Open: posed at COLT 2024; an arXiv abstract search on 14 Nov 2026 found extensions (generalized linear models '
        'under shuffle and joint DP, arXiv:2602.00417; local DP in hybrid decision making, arXiv:2501.14928) but no '
        'matching bounds for the linear case.',
  'n': 'Added 14 Nov 2026 by an agent. Replaces T412 (convergence of discrete diffusion models: largely solved).'},
]
