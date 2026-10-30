# T250 moves on the obstruction

- 2026-10-16, bound (agent A): Deep linear program: W1 to the GP limit equals sigma^L (sqrt L - 1)/sqrt(pi n) to 3 digits (n=1000, L<=32): no poly-in-depth constant without a stability assumption; critical benchmark sqrt(L/n). Rate n^-1/2 for Lipschitz Netsor is in 2607.06290 Thm 1.2
- 2026-10-18, proved (agent A): Lemma (ii) proved uniformly in theta via the exact identity sin theta = theta q(a,b,m) with closed-form means (q = sin F/theta at the means), sub-exponential |d_i| <= theta(|x_i|+|w_i|), Bernstein, Taylor; good event |T|>=2. With lemma (i) (concavity, numerical) the log-angle chain error is O(sqrt(L/n)). Left: analytic concavity of F; Gram-root W2 conversion.
- 2026-10-18, proved (agent A): Lemma (i): the ReLU angle map F is concave on (0, pi/2], computer-assisted (series bounds on [0,1/4], 200-bit intervals on [1/4, pi/2]); H = p^2 - 2pp - pp^2/(2pi-p) >= 0 with p = pi(1-k).
- 2026-10-18, proved (agent A): p=2 critical ReLU MLP: W2 of the two-input outputs to the GP limit <= C sqrt(L/n), C absolute, uniform in theta0, L <= n. Gram-root step by Araki-Yamagami (Lipschitz, no Holder loss). p>=3 open (frame not uniformly Lipschitz). Needs a second reader.
- 2026-10-18, proved (agent A): p>=3 inputs: W2 <= C(p,rho) sqrt(L/n) via correlation frame C^(1/2)D + van Hemmen-Ando, per-pair log-angle chain from p=2, rho=inf_l lam_min(Cbar_l)/thetamax_l^2 >0 (F expansion theta - theta^2/(3pi) - theta^3/(18pi^2); rho_l->1/2 regular simplex; each rho_l>0 by linear independence of relu ridge functions). Needs a second reader.
- ,  (): 
- ,  (): 
- ,  (): 
- 2026-10-18, moved (agent A): W2 <= C sqrt(L/n) finite-width ReLU MLP vs GP: p=2 every input angle in (0,pi], p>=3 non-parallel inputs; refereed PASS by agent C (lemma ii' with good event G')
- 2026-10-20, narrowed (agent C): Target 1 for the one-input critical tanh chain (zero bias, N(0,1/n) weights): joint normalized preactivation trajectory W2^2<=1152L/n for all n,L (postactivations 2304L/n), via an abstract concave scalar-kernel lemma (conditional relative variance, no independence across layers); the relative kernel error obeys E(q_l/qbar_l-1)^2<=192l/n. Deterministic multi-input correlation amplification is bounded by exp(48(q0+r0)) uniformly in depth. Open: the stochastic multi-input Gram estimate, transposes, general chain programs.
