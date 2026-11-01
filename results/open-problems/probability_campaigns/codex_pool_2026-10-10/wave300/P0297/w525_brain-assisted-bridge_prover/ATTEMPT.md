# P0297: finite Gaussian interpolation bridge

Author: w525, 2026-10-10. Author-checked finite lemmas; independent review pending from w526 and w527. P0297 is not solved. No novelty claim.

## Target and hardest gap

For gamma in (0,2), let h be a whole-plane GFF normalized by fixing an additive constant, and let D_h^gamma be the canonical gamma-LQG metric. Determine the deterministic almost-sure value d_gamma=dim_H(C,D_h^gamma), beyond d_sqrt(8/3)=4. A multiplicative normalization of D does not affect dimension. The LFPP bridge uses xi=gamma/d_gamma and Q=2/gamma+gamma/2; for the usual epsilon-normalized crossing distance the exponent is lambda(xi)=1-xi Q, not a formula for lambda itself.

The single hardest gap in this attempt is evaluating the scale-normalized integrated Gaussian response below for actual planar LFPP. Existence, concentration, constant-shift scaling, and an interpolation identity do not evaluate it. Current openness and precise primary locators are recorded separately in SOURCE_STATUS.json.

## Prior-attempt digest

The September P0297 attempt correctly observed that shifting h by c scales area by exp(gamma c) and metric distance by exp(xi c), and that a compatible volume exponent requires xi*d_gamma=gamma. It explicitly left the metric normalization exponent unresolved. Another intake attempt, D0049-A001, wrote d_gamma=2Q/xi. That equation fails the known Brownian parameter: gamma=sqrt(8/3), xi=1/sqrt(6), Q=5/sqrt(6) give 2Q/xi=10, while gamma/xi=4. This is an error in a prior attempt, not evidence that the target is solved. D0052's numerical check of candidate values cannot determine a function on all gamma. Targeted H/I and Lean searches and source locators are logged in the review packet.

The first independent packet sent to w526 was STATEMENT_FOR_ADVERSARY.md, with statements and assumptions only. This lane studies Gaussian response and minimizing-path changes; it does not repeat a KPZ or constant-shift derivation.

## Lemma 1: exact finite-network response

Let V be finite, X~N(0,C) where C is positive semidefinite, and P a finite nonempty family of nonempty paths. For each p, let a_pv>0 on its support. Set

f_p(y)=log(sum_{v in p} a_pv exp(y_v)),
r_pv(y)=a_pv exp(y_v)/(sum_{w in p} a_pw exp(y_w)) on p and 0 elsewhere,
q_p(y)=exp(-beta f_p(y))/sum_s exp(-beta f_s(y)), beta>0,
F_beta(y)=-(1/beta)log(sum_p exp(-beta f_p(y))).

Each r_p is a probability vector. Let rbar=sum_p q_p r_p and

A_beta(y)=sum_p q_p[sum_v r_pv C_vv-r_p^T C r_p],
B_beta(y)=sum_p q_p r_p^T C r_p-rbar^T C rbar.

For m_beta(xi)=E F_beta(xi X), xi>=0,

m_beta'(xi)=xi E[A_beta(xi X)-beta B_beta(xi X)].

Proof. Direct differentiation gives grad f_p=r_p and Hess f_p=diag(r_p)-r_p r_p^T. Differentiating q gives grad F_beta=rbar and

Hess F_beta=sum_p q_p Hess f_p-beta[sum_p q_p r_p r_p^T-rbar rbar^T].

At fixed finite beta, its derivatives through order two are uniformly bounded, and |F_beta(y)| is bounded by a deterministic constant plus max_v |y_v|. Differentiating the Gaussian expectation is legitimate by dominated convergence. Gaussian integration by parts, applied after writing X=C^(1/2)G if C is singular, yields

E[X dot grad F_beta(xi X)]=xi E tr(C Hess F_beta(xi X)),

which is the asserted identity, including xi=0. Positivity follows from

sum_v r_pv C_vv-r_p^T C r_p=sum_v r_pv (e_v-r_p)^T C(e_v-r_p)>=0,
B_beta=sum_p q_p (r_p-rbar)^T C(r_p-rbar)>=0.

No independence of coordinates or selected routes is assumed. Positivity of both terms does not determine the sign of their difference.

## Lemma 2: retain the term at route switches

Let D_xi=min_p sum_{v in p} a_pv exp(xi X_v), K=|P|. For 0<=a<b<infinity,

E log D_b-E log D_a=lim_{beta->infinity} integral_a^b xi E[A_beta(xi X)-beta B_beta(xi X)] dxi.

Proof. For every y, min_p f_p(y)-(log K)/beta <= F_beta(y) <= min_p f_p(y). Apply Lemma 1 and the fundamental theorem of calculus at fixed beta. The error in each endpoint is at most (log K)/beta. Hence the identity follows with endpoint-difference error at most 2(log K)/beta. There is no exchange of a limit with a derivative or a separately convergent A/B integral.

Exactly solvable obstruction. With two singleton paths, a=1, C=I_2, and xi>=0, log D_xi=xi min(X_1,X_2). Since min(X_1,X_2)=(X_1+X_2-|X_1-X_2|)/2 and X_1-X_2~N(0,2), E log D_xi=-xi/sqrt(pi). Each f_p is affine, so A_beta=0. But B_beta=2q_1q_2 and beta*xi*E B_beta->1/sqrt(pi) for every xi>0. Pointwise q becomes a single chosen route almost surely; nevertheless the beta-weighted expectation does not vanish.

Indeed, writing t=beta*xi and u=t(X_1-X_2)/2 gives

t E B_beta=(1/(2 sqrt(pi))) integral_R sech^2(u) exp(-u^2/t^2) du ->1/sqrt(pi).

Dropping route fluctuations predicts derivative 0 instead of -1/sqrt(pi). At xi=0, each fixed-beta derivative is 0 while the hard minimum has right derivative -1/sqrt(pi); another reason to retain the integrated identity.

## Lemma 3: concentration transfers median exponent to mean log exponent

Let v=max_i C_ii. For xi>=0, Var(log D_xi)<=xi^2 v, and any median M_xi of log D_xi satisfies |E log D_xi-M_xi|<=xi sqrt(v).

Proof. The Gaussian-coordinate gradient of f_p(xi C^(1/2)g) is xi (C^(1/2))^T r_p. Jensen for squared norm gives r_p^T C r_p<=sum_i r_pi C_ii<=v. Each f_p is therefore xi sqrt(v)-Lipschitz in g, and the minimum of finitely many functions with that common Lipschitz constant is also Lipschitz. Gaussian Poincare applies to this Lipschitz function and gives the variance bound (ties cause no problem). If a median is above the mean by t>0, Cantelli's inequality and P(Y>=M)>=1/2 imply t<=sqrt(Var Y); the other direction is identical. Constant Gaussian modes, negative covariances, and singular C are allowed.

For completeness, the Poincare step follows directly from Gaussian integration by parts. If f is smooth and L-Lipschitz and G,H are independent standard Gaussians, set psi(t)=E[f(G)f(tG+sqrt(1-t^2)H)]. For 0<t<1, integration by parts in G and H cancels the second-derivative terms and gives psi'(t)=E[grad f(G) dot grad f(tG+sqrt(1-t^2)H)]<=L^2. Integrating from 0 to 1 yields Var f(G)<=L^2. Mollification preserves the Lipschitz constant; Gaussian L^2 convergence extends the result to Lipschitz f with at most linear growth, including this minimum.

Brain theorem comparison: the corrected Gaussian-concentration card (claim_1dccd5251ab873de59d3ee5a16f929c03c20418aa3790ed1659191840b95b56b) requires a standard Gaussian vector and a globally Euclidean-Lipschitz function. The LFPP field X is correlated, so one must first write X=C^(1/2)G and prove the Lipschitz bound above. The retrieved tail alone gives a weaker sufficient variance bound; the sharp constant used here comes from the displayed Poincare proof. The earlier concentration card is superseded and is not used. The retrieved GMC vocabulary card has gamma in (0,2) but contains neither a crossing-exponent formula nor metric-volume hypotheses and cannot close the remaining gap.

Consequently, for a sequence of finite networks with L_n->infinity and v_n=O(L_n), a median crossing exponent M_xi,n/L_n->-lambda(xi) implies E log D_xi,n/L_n->-lambda(xi). This only transfers an existing exponent. It cannot calculate it.

## Lemma 4: finite comparison and an already-known LFPP bound

Under the finite hypotheses above, for 0<=a<b, E log D_b-E log D_a <= (v/2)(b^2-a^2), where v=max_i C_ii. Indeed A_beta<=sum_p q_p sum_i r_pi C_ii<=v and B_beta>=0, so Lemma 1 gives m_beta'(xi)<=xi v. Integrate at fixed beta and apply Lemma 2. If v_n/L_n->1 and the crossing exponents exist at a,b, divide by L_n to obtain lambda(b)-lambda(a)>=-(b^2-a^2)/2. This recovers the published monotonicity of lambda(xi)+xi^2/2, recorded in Gwynne-Pfeffer (1903.09561), equation (2.4), and is not a new LQG bound. To improve this step one needs quantitative control of B rather than only its sign.

## Conditional scale bridge

Assume the actual LFPP discretization used has covariance diagonals v_n=O(L_n), L_n=log(1/epsilon_n), and medians M_xi,n/L_n->-lambda(xi) at endpoints a,b. Choose beta_n so that log K_n/(beta_n L_n)->0. Lemmas 1-3 imply the exact conditional reduction

lambda(b)-lambda(a)=-lim_n (1/L_n) integral_a^b xi E[A_{n,beta_n}-beta_n B_{n,beta_n}] dxi.

This is derived by endpoint convergence and the deterministic soft-min error. It does not require existence of pointwise susceptibility limits. On a nearest-neighbor graph with N_n vertices and bounded degree Delta, the number of simple crossing paths is at most N_n^2(Delta+1)^(N_n+1), so log K_n=O(N_n+log N_n); beta_n=N_n^2 suffices when N_n,L_n->infinity. This is an existence bound, not an efficient enumeration algorithm. Positive costs allow minimization over simple paths.

## Independent smoothing counterexample and its scope

w526 derived the finite identity and variance transfer independently from STATEMENT_FOR_ADVERSARY.md; their saved proof is ~/brain_workers/w526/FINITE_BRIDGE_INDEPENDENT.md. Their C526.5 uses L_n=n, K_n=2^(n^2) singleton paths, X_i=Z for one shared standard Gaussian, and beta_n=n. Then log D_xi=xi Z, but F_beta_n(xi X)/L_n has mean -log 2. Thus beta_n->infinity by itself does not transfer an individual soft-min asymptotic to its hard minimum. The explicit log K_n/(beta_n L_n)->0 premise above rules out this example.

The shift in this particular example is independent of xi and cancels in endpoint differences. It is therefore not a counterexample to the integrated endpoint identity, and it does not prove that the entropy premise is logically necessary for every possible endpoint transfer. It exactly demonstrates the absence of a uniform bound for individual soft-min levels. No claim that this network is planar LFPP is made.

## What the proof attempt does and does not establish

The finite identity, its integrated limit, the two-route counterexample, and concentration transfer have complete author proofs above. The conditional reduction explicitly assumes the exponent and covariance estimates for the chosen discretization. Published discrete/continuum comparison must be checked before using a discrete network as a continuum LFPP surrogate. These lemmas do not evaluate the remaining limit, exclude other dimension formulas, or show a new bound for d_gamma.

Independent checks requested: verify the covariance contraction and the survival of beta B at near-ties; verify the median-to-mean transfer under the stated variance growth; verify that the LFPP convention includes epsilon in each vertex cost. No formal proof or trusted-axiom receipt is claimed.

NEXT: Evaluate or rigorously bound the normalized integrated route-response term for planar LFPP without replacing the minimizing route by a fixed route.
