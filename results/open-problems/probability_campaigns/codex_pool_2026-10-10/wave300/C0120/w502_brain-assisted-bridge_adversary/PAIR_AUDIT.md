# C0120 paired-proof adversarial audit

Auditor: w502. Author: w501. Final assigned referee: w503. Served-model identity of author/auditor is UNKNOWN; this audit does not satisfy a different-model promotion gate.

Independent source/OU derivation was saved in ATTEMPT.md before reading w501's proof. Audited file: ~/brain_workers/w501/LEMMAS.md (hash to be pinned in review_packet.json). All KEEP statements below are conditional reductions or method obstructions, not a solution of C0120.

L1: KEEP within the specified n-vertex Gaussian, right/up, free-endpoint model. Independent derivation: the weak gradient of M_n is the selected-path indicator. Gaussian covariance interpolation gives the integral; self-adjoint OU contraction gives monotonicity. Splitting at tau yields both inequalities. Constants must be uniform in n; alpha denotes OU time exponent, not noise amplitude exponent. A positive overlap power remains a hypothesis.

L2: KEEP. With f_v an indicator and s=t/2, Gaussian hypercontractivity uses p=1+e^{-t}, not 1+e^{-2t}. Its squared Lp norm is q_v^{2/p}; 2/p=1+tanh(t/2). This argument uses the product Gaussian environment, not independence of selected path-site events. It applies to the actual original marginal q_v; shifted/averaged BKS derivatives would need their own calculation.

L3: KEEP as a lower bound on an upper-bound certificate. Every path visits exactly one vertex on layer k-1, which has k vertices, so the layer marginals sum to one. Convexity of x^{1+a} gives a layer contribution at least k^{-a}. Summing gives B_n(t)>=n^{1-a(t)}. At t=n^{-alpha}, a(t)<=t/2, hence exp[-n^{-alpha}log(n)/2]<=B_n(t)/n<=1. For the integral, u=e^{-t} gives a=(1-u)/(1+u)<=1-u; integrating n^{u} from zero to one gives (n-1)/log n. Boundary checks: q=0 contributes zero; t=0 exponent is one; n=2 has a deterministic origin contribution one. All integrals are finite because B_n(t)<=n.

The most important attempted break is the direction of this inequality: Q_n(t)<=B_n(t) and B_n(t)>=c n/log n do NOT imply Q_n(t)>=c n/log n or Var(M_n)>=c n/log n. The proof states the distinction explicitly and survives this attack. It also does not exclude BKS shifting, block estimates, or new geometry. Keeping this distinction in the brain card is essential.

L4: KEEP as conditional exponent arithmetic. From the two explicitly assumed relations, the variance exponent is 4xi-2. xi<1 alone does not force it below one; xi=4/5 gives 6/5. xi<3/4 does give a strict gap, so the o(1) term can be absorbed into a smaller epsilon. A weak inequality at the exact endpoint xi=3/4 does not yield a strict power improvement. The KPZ identity is not established for this model by these computations.

Parent verdict: UNSOLVED. The single hardest missing premise is Q_n(n^{-alpha})<=C n^{1-delta} for fixed positive alpha,delta and C independent of n. Neither the logarithmic source theorem nor the per-site hypercontractive certificate proves it.

Additional source bridge gap: converting a fixed finite-beta log-partition theorem to the zero-temperature maximum requires a uniform estimate as beta grows with n. See ATTEMPT.md and claim L03 below. A source hash or formal receipt for a different theorem does not supply this estimate.
