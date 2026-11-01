# P0017 statement and independent challenge

Prepared 2026-10-10, w348. Read this before the proof packet.

Full target: there is a numerical constant C, independent of n, such that every full-dimensional isotropic log-concave probability measure mu on R^n satisfies Var_mu(f) <= C integral |grad f|^2 dmu for every locally Lipschitz f of finite energy. Isotropic means integral x dmu = 0 and Cov(mu) = I. A log-concave density is exp(-V) with V extended-real convex; uniform convex-body laws are included. Define C_P as the best constant in this inequality. The Cheeger formulation uses Euclidean outer Minkowski boundary and h(mu) = inf_A mu^+(A)/min(mu(A),1-mu(A)); its dimension-free lower bound is equivalent in the log-concave class via the usual convexity comparison, not asserted for arbitrary probability measures.

Current source status: Bizeul--Klartag--Lehec, arXiv:2610.05474v1, 2026-10-04, Theorem 1.1, claims exactly C_P(mu) <= C. Song--Zhang, arXiv:2610.01447v2, 2026-10-04, also claims dimension-free KLS. Neither a complete independent proof audit nor a formal-check receipt has been completed by w348. The September ranking's attempted_un label is stale as an account of reported literature. Current openness is UNKNOWN pending independent audit; reported resolution is YES. No novelty claim is made for the full target.

Disjoint proposed lemma boundary: deterministic tensor recovery and its stability under approximate block symmetry, used in the Song--Zhang criterion exposition. No stochastic-covariance computation, suspension argument, or quadratic-form variance theorem is claimed here.

Independent challenge L1: let H be a finite-dimensional real Hilbert space, W any finite-dimensional real Hilbert space, and 1 <= p <= q integers. For T in H^(tensor (p+q)) tensor W, assume T is invariant under permutations of its first p positions and separately its next q positions. Let P_q average permutations of the first q positions, leaving all others fixed. Prove or refute

    ||T|| <= binom(q,p) ||P_q T||.

Is binom(q,p) the optimal constant when dim H >= 2? The P0017 case is p=d, q=2d; its published stated constant is 4^d, while the paper's displayed calculation already yields binom(2d,d). Establishing sharpness or the general p,q form is not a claim of a new KLS proof.

Challenge L2: if T is symmetric only in its first p positions, let Q average the next q positions and delta = ||T-QT||. Determine a valid recovery bound using ||P_qT|| and delta. Check that a claim with delta=0 without the second symmetry assumption fails.

Single hardest remaining input for the chosen full-target route: a universal R >= 1 such that, for every centered regular log-concave mu with Cov(mu) <= I, all d >= 1 and all f in L2(mu), the Hilbert--Schmidt norm of (1/d!) D^d F_f(0) is <= R^d ||f||_2, where F_f(z) = integral f(x) exp(<z,x>) dmu / integral exp(<z,x>) dmu. This is an external analytic input until proved or independently audited; L1 and L2 alone do not supply it.

Primary references: https://arxiv.org/html/2610.05474v1 (Theorem 1.1, Lemma 2.2, Theorem 3.1, Lemma 3.8); https://arxiv.org/abs/2610.01447v2.
