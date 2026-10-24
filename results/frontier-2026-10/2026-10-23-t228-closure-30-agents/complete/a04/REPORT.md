# A04 — T228 independent source, theorem-boundary, and explicit-model report

Date: 2026-10-23. This is a mathematical research note, not a priority certificate. No external records were modified.

## Status and recommended closure route

The retrieved T228 dossier says Targets 1, 2, and 3 are proved and reviewed. Target 2 v2 addresses the leaky-ReLU discontinuity; Target 3 v2 reports two independent reviews. Consequently I found no remaining unresolved theorem among the dossier's three targets. The best narrow closure certificate is the explicit smooth scalar example proved below. It supplies actual average contraction, positive stationary tail constants, and an infinite-variance interval using explicit parameters. It does not depend on extending a continuity-based theorem to a discontinuous map.

The general tail machinery is known. The distinct contribution of this certificate is the complete verification for an honest nonlinear SGD model with Gaussian data. A claim of firstness would require a broader literature audit than the searches here.

## Explicit theorem, with all numerical parameters fixed

Let delta = 10^-3 and sigma(z) = z + delta tanh(z). At every step independently draw a and epsilon as independent standard normal variables. Use squared sample loss

    f(w; a, epsilon) = (sigma(a w) - epsilon)^2 / 2

and batch size b = 1, target w* = 0, and any fixed step eta in [0.99, 1.01]. Thus

    W_(n+1) = Psi_eta(W_n),
    Psi_eta(w) = w - eta a sigma'(a w)(sigma(a w) - epsilon).

Then:

1. The Markov chain has exactly one invariant probability pi_eta, and it has finite first moment. For every deterministic initial state, its law converges to pi_eta in Wasserstein distance of order one, at a geometric rate.
2. There is a unique kappa_eta in (1, 2) satisfying

       E |1 - eta a^2|^kappa_eta = 1.

3. There is C_eta in (0, infinity) such that

       lim_(t -> infinity) t^kappa_eta pi_eta((t, infinity)) = C_eta,
       lim_(t -> infinity) t^kappa_eta pi_eta((-infinity, -t)) = C_eta.

4. For p > 0, the stationary pth absolute moment is finite exactly when p < kappa_eta. In particular the stationary variance is infinite, although every fixed finite iterate from a deterministic start has all polynomial moments.

### Proof: deterministic envelopes

Put z = a w, h = sech^2(z), and v = tanh(z). Then sigma' = 1 + delta h and sigma'' = -2 delta h v. Let A = 1 - eta a^2. Exact expansion gives

    Psi_eta(w) = A w + R_eta(w),
    R_eta(w) = -eta a [delta z h + (1 + delta h)(delta v - epsilon)].

The elementary inequalities |v| <= 1, 0 < h <= 1, and |z|h <= 1 imply

    sup_w |R_eta(w)| <= B_eta,
    B_eta := eta |a| [(2 delta + delta^2) + (1 + delta)|epsilon|].

B_eta has moments of every positive order. A and B_eta may be dependent; none of the following arguments assumes their independence. They are independent of the current state because data are freshly sampled.

Differentiation gives

    Psi_eta'(w) = 1 - eta a^2 [(1 + delta h)^2
                              - 2 delta h v (z + delta v - epsilon)].

Hence a valid Lipschitz envelope is

    L_eta = |1 - eta a^2|
            + eta a^2 [delta (4 + 2|epsilon|) + 3 delta^2].

This conservative envelope follows by bounding the two terms of order delta by 2 and 2|z|h, the epsilon term by 2|epsilon|, and the terms of order delta^2 by 3.

### Proof: a uniform contraction constant strictly below one

For a standard normal a, direct integration gives

    E|1 - a^2| = 4 exp(-1/2)/sqrt(2 pi) = 4/sqrt(2 pi e).

Indeed E(1-a^2)=0 and integrating (1-x^2) times the normal density over (-1,1) gives twice the normal density at 1. The triangle inequality and E a^2 = 1 yield

    E|1 - eta a^2| <= 4/sqrt(2 pi e) + 0.01.

As a and epsilon are independent,

    E L_eta <= 4/sqrt(2 pi e) + 0.01
               + 1.01 [10^-3(4 + 2 sqrt(2/pi)) + 3*10^-6]
             = 0.983537654889395... < 1.

This bound is uniform over the whole interval. Its strict inequality can be checked without numerical quadrature: pi > 3.14 and e > 2.718 give 4/sqrt(2 pi e) < 0.969; sqrt(2/pi) < 0.8 then gives the displayed bound below 0.985.

Existence can be established directly. Backward compositions F_n = Psi_1 o ... o Psi_n(0) obey

    E|F_(n+1) - F_n| <= lambda^n E|Psi(0)|,

where lambda = E L_eta < 1. Thus the increments are summable almost surely and in L1, producing a stationary limit. Coupling two starts with identical future maps contracts their expected distance by lambda^n. To exclude an additional stationary law with infinite first moment, couple its almost surely finite initial state R to the zero-start chain. The product of the L_j tends to zero almost surely, so their difference tends to zero almost surely; the two stationary laws must coincide. This proves uniqueness among all probability laws.

### Proof: the exponent lies strictly between one and two

Define q_eta(p) = E|A|^p. It is finite for every p >= 0 and strictly log-convex, since |A| is nonconstant. The preceding bound gives q_eta(1) < 1. Also

    q_eta(2) = E(1 - eta a^2)^2 = 1 - 2 eta + 3 eta^2
              >= 1.9603 > 1

on [0.99,1.01]. Moreover q_eta(0)=1, E log|A| <= log q_eta(1) < 0, and P(|A|>1)>0. Therefore q_eta has exactly one positive root equal to one, and that root belongs to (1,2). Its derivative at the root is strictly positive and finite.

For every p < kappa_eta, q_eta(p)<1. The bound |Psi_eta(w)| <= |A||w|+B_eta gives uniformly bounded pth moments along the zero-start chain: use subadditivity for p <= 1 and Minkowski's inequality for p >= 1. Weak convergence and Fatou's lemma give E_pi |W|^p < infinity.

### Proof: stationary tails and positivity

For this model Psi_eta is smooth and satisfies the bounded-error envelope above with the SAME asymptotic slope A at both ends. Its two-state tail matrix is

    P(p) = [[d(p), o(p)], [o(p), d(p)]],
    d(p) = E |A|^p 1_(A>0),
    o(p) = E |A|^p 1_(A<0).

Both transition types occur with positive probability. The spectral radius is q_eta(p). The logarithmic increment on the positive-slope event has a continuous component, which rules out every arithmetic coboundary. All required slope/logarithmic and perturbation moments are finite.

For each fixed current state w and almost every a != 0, the next state is conditionally Gaussian, with variance

    eta^2 a^2 sigma'(a w)^2 > 0.

Therefore every nonempty open interval has positive transition probability from every state. Stationarity implies pi_eta has full, and hence unbounded, support. Applying the known scalar asymptotically linear recursion theorem gives the two finite limits; the unbounded-support positivity criterion makes both positive. The left Perron vector is (1/2,1/2), so the two constants are equal. These facts are supplied by Alsmeyer–Brofferio–Buraczewski, Theorem 2.1 and Proposition 8.1 [S1]. The positive tail limits imply divergence of every pth moment with p >= kappa_eta by the layer-cake integral.

For completeness, the total tail constant can also be expressed by scalar implicit renewal as

    2 C_eta = E[ |Psi_eta(R)|^kappa_eta - |A R|^kappa_eta ]
              / (kappa_eta E[|A|^kappa_eta log|A|]),

where R has pi_eta and is independent of current data. The numerator means the expectation of the difference, not a subtraction of two separately infinite expectations. Absolute integrability of the difference follows from the B_eta envelope, E|R|^(kappa_eta-1)<infinity, and Holder's inequality.

### The model is genuinely nonlinear and its input is light-tailed

The loss is nonlinear in w because delta != 0. Its population minimum is zero: sigma has the sign of its argument, |sigma(z)| >= |z|, and sigma'(z)>=1, so w E[a sigma'(a w)sigma(a w)] >= w^2. At the target the gradient innovation is (1+delta)a epsilon, which has moments of every positive order. Thus the infinite-variance stationary tail is created by repeated random multiplication, not inserted through a heavy-tailed label or gradient at the optimum.

## New October 2026 paper: exact scope distinction

Li–Lei–Wei–Wu, arXiv:2610.23750v1, assumes regularly varying target innovation with index t in (1,2) (Assumption 4). Its Theorem 1 takes gamma down to zero, n_gamma gamma to infinity, and u_gamma=c gamma^a down to zero, with (t-p)/t<a<(t-1)/t. The leading measure propagates existing large innovations through the local Hessian flow. Corollary 4 allows fixed u for globally affine population gradients, still as gamma tends to zero. Appendix H's random-design example uses Student-t_1.5 labels [S2].

Our conclusion about non-overlap is an inference from those hypotheses: the explicit model's innovation has all moments, so it cannot satisfy their Assumption 4; our asymptotic fixes eta and sends the stationary radius to infinity. Therefore this paper does not prove or subsume the theorem above. It does require replacing broad novelty language such as “first exact tails for nonlinear SGD” with the precise scope “fixed-step stationary power tails generated from Gaussian data.” This assessment does not prove priority against all other literature.

## Adversarial lemmas and concrete counterexamples

### A. Moment-root conditions do not force a positive tail constant

Let A have the mixture 0.9 Uniform[0.2,0.3] + 0.1 Uniform[2.5,3.5]. Then E log A < 0 (bound it above by 0.9 log(0.3)+0.1 log(3.5)), E A^kappa=1 for a positive kappa, and log A is nonarithmetic because it has a density. Set B=(1-A)c for any fixed c. The stationary law of X'=AX+B is delta_c and every tail constant is zero. Thus nondegeneracy or unbounded support is essential.

The same obstruction occurs within scalar neuron regression if label noise is removed: set Y=sigma(w* a) exactly. The residual and every sample gradient vanish at w*, so delta_(w*) is stationary, even if the far-field multipliers have an expansion event and a moment root. This does not contradict T228 because its label noise variance is strictly positive.

### B. An arithmetic multiplier can prevent a constant tail limit

Let A=2 with probability p=1/4 and A=0 otherwise, and B=1. The recursion resets to one and its unique stationary law is

    X = 2^(N+1)-1,  P(N=k)=(1-p)p^k, k=0,1,... .

It has E A^2=1, bounded B, and unbounded stationary support. Exactly,

    P(X>t)=p^floor(log_2(t+1)),  t>=1.

Along t_n=2^n-1 the product t_n^2 P(X>t_n) tends to 1, while along s_n=2^(n+1)-2 it tends to 4. A nonarithmetic assumption cannot simply be dropped. This is a direct computation, independent of any source theorem. The arithmetic renewal literature treats periodic alternatives [S5].

### C. A ReLU derivative convention can create a second invariant law

For beta=0 and sigma'(0)=0, the SGD update fixes zero for every sample. Thus delta_0 is invariant. A claim of a unique nondegenerate invariant law on all of R is false under that convention. Target 2 v2 correctly separates this case. For positive-only covariates, ordinary ReLU further freezes every negative state.

### D. Equal marginal slope laws do not make the full affine pair independent of the state

For scalar leaky-ReLU SGD with symmetric covariates, A_+ and A_- have the same law. If the fresh step is independent of W, then the selected multiplier A_(sign W) is independent of W. This follows by conditioning on the sign. The analogous statement about the pair (A_(sign W),Q_(sign W)) need not hold because the conditional offset laws need not agree. A proof may use scalar implicit renewal with the selected multiplier, but must not silently replace the actual update by an iid affine recursion with an independent additive coefficient.

### E. Fixed finite-time tails and stationary tails have different limits

If W_0 is deterministic and every data moment is finite, the envelope |W_(n+1)| <= |A_(n+1)||W_n|+B_(n+1) proves inductively that E|W_n|^p<infinity for every finite n and p. For any fixed kappa, choose p>kappa and use Markov's inequality to get

    lim_(t -> infinity) t^kappa P(|W_n|>t) = 0.

The stationary limit can instead have a strictly positive kappa-power constant. Therefore one cannot interchange infinite time and infinite threshold, or infer the stationary asymptotic solely from a finite-run Hill plot. Related affine finite-iteration bounds appear in Damek–Mentemeier [S4].

## Source map and what is known

- [S1] Alsmeyer, Brofferio, Buraczewski. *Asymptotically linear iterated function systems on the real line*. Annals of Applied Probability 33(1), 161–199 (2023). https://arxiv.org/html/2102.02299 ; DOI https://doi.org/10.1214/22-AAP1812 . Theorem 2.1, Proposition 8.1, Proposition 9.1. Known general tail mechanism; a continuity hypothesis must be checked.
- [S2] Li, Lei, Wei, Wu. *Exact Tail Laws for Nonlinear SGD with Infinite-Variance Gradients*. arXiv:2610.23750v1 (16 October 2026). https://arxiv.org/html/2610.23750v1 . Relevant assumptions and limit described above.
- [S3] Gurbuzbalaban, Simsekli, Zhu. *The Heavy-Tail Phenomenon in SGD*. ICML 2021. https://proceedings.mlr.press/v139/gurbuzbalaban21a.html . Establishes the Gaussian-data multiplicative-tail phenomenon for linear regression; general nonlinear transfer requires additional verification.
- [S4] Damek, Mentemeier. *Analysing heavy-tail properties of Stochastic Gradient Descent by means of Stochastic Recurrence Equations*. https://arxiv.org/html/2403.13868 . Theorems 3.1 and 3.5 distinguish stationary affine regular variation and lighter fixed finite-iteration tails.
- [S5] Kevei. *Implicit renewal theory in the arithmetic case*. Journal of Applied Probability. https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/implicit-renewal-theory-in-the-arithmetic-case/B5D27B461C0263B2B75808FB60CD6200 . Relevant to the need for nonarithmetic hypotheses.
- [S6] Buraczewski, Damek. *A simple proof of heavy tail estimates for affine type Lipschitz recursions*. https://arxiv.org/html/1604.06943v1 . Separates existence of tail limits from positivity and supplies positivity methods.
- [S7] Mirek. *Heavy tail phenomenon and convergence to stable laws for iterated Lipschitz maps*. https://arxiv.org/pdf/0907.2261 . Assumption 1.6(H1) is a similarity-group hypothesis in dimensions greater than one, so its direct applicability to general sample-Hessian matrices must not be assumed.

Local dossier inspected: ../a01/DOSSIER.md; ../a01/claude_4af6ff1a/T228_B_v2.md; ../a01/claude_b1e26540/T3_CLAIM.md.


## Independent check of parent candidate v1

Read `campaign/proofs/T228_EXPLICIT_CLOSURE.md` after completing the derivation above. Verdict: PASS on the actual average-contraction interval, Gaussian-model assumptions, exponent interval, remainder integrability, symmetry, and scope comparison. Its conservative bound 0.98606303 is valid; the exact-normal-moment bound above improves it to 0.983537654889395. I found no issue in its forward positivity proof: the occupation bound gives uniform overshoot tightness, the tilted remainder moment accounts correctly for dependence within each (xi,B) pair, and the last-exit inequality is in the correct direction. I did not independently recheck every printed hypothesis of the cited Jelenkovic–Olvera-Cravioto theorem in this pass; the smooth scalar model alternatively falls directly under the verified ABB Theorem 2.1 and Proposition 8.1 assumptions above.
