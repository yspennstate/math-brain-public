# T336: a quantitative ERM bridge for genuine, unbounded GP labels

Author: A05, 2026-10-23. Status: complete mathematical derivation, not independently audited or formally verified. This is an elementary statistical completion candidate, not a claim of a novel concentration theorem. The deterministic continuous-kernel construction is owned by A02. All task distributions and optimization assumptions are explicit below.

## 1. Setting and the precise statistical claim

Fix a zero-mean real GP with positive-semidefinite kernel k satisfying k(x,x) <= K, where K >= 0, and independent observation noise N(0,s), s > 0. Fix a maximum context length n >= 1. Set V0 = s+K. The covariates of a task, its context length t <= n, and its query can have any fixed joint distribution, but are independent of the sampled GP and its noises. Each pretraining task is an independent draw of this entire experiment, with a fresh GP draw. All assertions average over this specified joint distribution; the query covariates are included in the conditioning information.

Write Z for all context inputs/labels and the query input, Y for the noisy query target, and

    p(.|Z) = N(m(Z),v(Z)).

Then s <= v(Z) <= V0. Conditional on the covariates, Y is centered Gaussian of variance <= V0, and the random posterior mean m is centered Gaussian of variance <= K. No target labels are clipped or assumed bounded.

We construct a class of Gaussian predictors q_theta(.|Z), with input context labels clipped at a threshold B and final outputs constrained to

    |m_theta(Z)| <= M,     s <= v_theta(Z) <= V0.

An ERM bound is proved for negative log likelihood. Its population excess risk above the exact Bayes predictor equals

    R(theta) = E_Z KL(p(.|Z) || q_theta(.|Z)).

The bound controls this average conditional forward KL. It does not control the supremum over all contexts, out-of-distribution tasks, arbitrary larger context lengths, or an SGD training trajectory.

## 2. From a bounded-context construction to average KL

Suppose a fixed transformer construction, when supplied labels |y_i| <= B, has uniform scalar errors

    |m-m_raw| <= d_m,     |v-v_raw| <= d_v.

Feed it clipped context labels c_B(y) = max(-B,min(B,y)), and clip its two outputs to [-M_B,M_B] and [s,V0], where

    M_B = B sqrt(n K/s).

The formula M_B is valid for the true posterior on every bounded-label context: putting A=G+sI and k_*=(k(x_i,x_*)) gives

    |m|^2 = |k_*^T A^{-1} y|^2
          <= (k_*^T A^{-1}k_*) (y^T A^{-1}y)
          <= K n B^2/s.

The first factor is at most k(x_*,x_*) <= K by the Gaussian Schur complement; the second is at most ||y||^2/s.

On the event E_B = {max_i |Y_i| <= B}, context clipping does nothing. Scalar output clipping preserves both displayed error bounds because the true mean and variance lie in the clipping intervals. For a,b >= s the variance-only part of Gaussian KL satisfies

    (log(b/a)+a/b-1)/2 <= (a-b)^2/(4s^2).

Indeed its derivative with respect to b is (b-a)/(2b^2), and integrating from a to b in either direction proves the inequality. Thus on E_B,

    KL(p || q) <= epsilon_app := d_m^2/(2s) + d_v^2/(4s^2).       (1)

This argument uses scalar-error preservation. Clipping the predicted variance is NOT in general monotone for full Gaussian KL when the means differ, so a claim based only on monotonicity of KL would be invalid.

Hereafter assume K>0; K=0 has the exact constant predictor N(0,s). Choose t0 >= 1 and set

    B = sqrt(2 V0 t0),     M = M_B.

The union bound and Gaussian tails give

    P(E_B^c) <= 2n exp(-t0).                                  (2)

A useful stronger tail-moment bound is

    E[m^2 1_{E_B^c}] <= (3/sqrt(pi)) n K sqrt(t0) exp(-t0).     (3)

Proof of (3). Condition on all covariates and fix a context coordinate i. The pair (m,Y_i) is jointly centered Gaussian. Write Var(m)=w<=K, Var(Y_i)=a_i<=V0, and let r be the correlation (the case w=0 is immediate). For a standard normal U,

    E[m^2 1_{|Y_i|>B}]
      = w[(1-r^2) P(|U|>B/sqrt(a_i))
           + r^2 E(U^2 1_{|U|>B/sqrt(a_i)})]
      <= K E(U^2 1_{|U|>sqrt(2t0)}).

The latter expectation is 2[a phi(a)+Phi(-a)], a=sqrt(2t0). Integration by parts and Phi(-a)<=phi(a)/a bound it by

    ((2 sqrt(t0)+1/sqrt(t0))/sqrt(pi)) exp(-t0)
      <= (3/sqrt(pi)) sqrt(t0) exp(-t0).

Sum over the at most n context coordinates and remove the covariate conditioning. This does not assert independence between m and the bad-label event.

Every clipped predictor, including the constructed one, obeys everywhere

    KL(p || q) <= (m-m_q)^2/(2s) + K^2/(4s^2)
                <= m^2/s + M^2/s + K^2/(4s^2).

Combining (1)--(3), with M^2=2 n K V0 t0/s, proves the explicit bridge

    E KL(p || q) <= epsilon_app + T_tail(t0),                  (4)

    T_tail(t0)
      = n exp(-t0) [ (3K/(s sqrt(pi))) sqrt(t0)
                      + (4 n K V0/s^2) t0 + K^2/(2s^2) ].

There is no replacement of the GP law by a bounded or truncated label law. The clipped predictor is compared to the posterior conditioned on the original labels.

For a fully explicit choice targeting T_tail<=eta, put

    C_tail = n [3K/(s sqrt(pi)) + 4nKV0/s^2 + K^2/(2s^2)],
    t0 = max(1, 2 log(max(1, 2 C_tail/(e eta)))).              (5)

For t0>=1, T_tail<=C_tail t0 exp(-t0), while t exp(-t)<= (2/e)exp(-t/2), so (5) proves the claim. The constants are conservative, and B only grows as the square root of a logarithm of the tail accuracy.

## 3. Finite-class ERM with unbounded Gaussian targets

Let H be any finite class of H0 Gaussian predictors, all with means in [-M,M] and variances in [s,V0]. Context clipping is allowed but is not needed for the concentration step. Define the shifted NLL

    ell_h(Z,Y) = (1/2) log(v_h(Z)/s)
                   + (Y-m_h(Z))^2/(2v_h(Z)).

The shift from usual NLL is independent of h. Put

    a0 = (1/2)log(V0/s) + M^2/s,
    A0 = 2 a0/log(2) + 4 V0/s.                              (6)

Then 0<=ell_h<=a0+Y^2/s, and

    E exp(ell_h/A0) <= 2                                   (7)

uniformly over H. To prove (7), a0/A0<=log(2)/2 and 1/(sA0)<=1/(4V0), while conditioning on the covariates gives E exp(Y^2/(4V0))<=sqrt(2). Dependence of the prediction on Y through correlated context labels causes no problem, since the envelope is pointwise.

For J independent pretraining tasks, any u>0 and every h,

    P(|(P_J-P)ell_h| > A0[sqrt(8u/J)+u/J]) <= 2 exp(-u).    (8)

Here P_J is empirical averaging. A self-contained derivation is as follows. Equation (7) implies E ell_h^k<=2 k! A0^k. For |lambda| A0<1,

    log E exp(lambda(ell_h-E ell_h))
       <= 2 A0^2 lambda^2/(1-A0|lambda|).

For positive lambda, use log x<=x-1 and the exponential series starting at k=2. For negative lambda, use exp(-x)-1+x<=x^2/2 for x>=0, which gives an even smaller bound. Chernoff optimization for the sum yields (8), with variance factor 4A0^2 and scale factor A0.

Let h_hat be a xi-approximate empirical risk minimizer over H:

    P_J ell_{h_hat} <= min_{h in H} P_J ell_h + xi.

With probability at least 1-delta over the J pretraining tasks,

    E KL(p || q_{h_hat})
      <= min_{h in H} E KL(p || q_h)
          + 2 A0 [sqrt(8 log(2H0/delta)/J)
                         + log(2H0/delta)/J] + xi.          (9)

Proof. Union-bound (8) with u=log(2H0/delta), then use the usual two-deviation ERM comparison. Conditional Gaussian entropy is finite and bounded, so

    P ell_h - P ell_Bayes = E KL(p(.|Z) || q_h(.|Z))

holds exactly and justifies the final conversion. The fact that the Bayes predictor is not in H is immaterial.

For the statistical term in (9) to be <=eta, it suffices that

    J >= max(128 A0^2 u/eta^2, 4 A0 u/eta),
    u = log(2H0/delta).                                    (10)

This supplies an actual finite-sample ERM theorem, not merely a population proper-scoring-rule identity.

## 4. Finite parameter grids and their explicit assumption

Suppose a fixed transformer architecture has P trainable scalar parameters in Theta=[-W,W]^P, W>=1. After the fixed input/output clips, suppose uniformly over admissible inputs

    |m_theta-m_theta'| <= L_m ||theta-theta'||_infinity,
    |v_theta-v_theta'| <= L_v ||theta-theta'||_infinity.       (11)

This hypothesis is verified quantitatively for the architecture in Section 6; it is not assumed to follow from parameter count alone. For r>0 choose a coordinate grid with infinity-norm covering radius r and

    H0 <= (2+2W/r)^P.                                     (12)

A safe population loss Lipschitz constant in parameter distance is

    C_pop = L_m (M+sqrt(V0))/s
              + L_v [1/(2s)+(M+sqrt(V0))^2/(2s^2)].         (13)

To obtain (13), differentiate the loss with respect to its mean/variance coordinates, use v>=s, and then E|Y|<=sqrt(V0), E Y^2<=V0. Linear interpolation stays inside the output rectangle. Therefore each theta has a grid point theta_g with |P ell_theta-P ell_theta_g|<=r C_pop.

If a constructed theta_star belongs to the box and meets (4), grid ERM satisfies, with probability >=1-delta,

    E KL(p || q_{theta_hat})
      <= epsilon_app + T_tail(t0) + r C_pop + xi
           + 2 A0 [sqrt(8u/J)+u/J],
    u = P log(2+2W/r)+log(2/delta).                         (14)

This is a completely specified ERM over a finite parameter quantization. Its computational cost may be enormous; the theorem is a sample-complexity result, not an efficient training theorem. W can be chosen as max(1, the largest absolute fixed or trainable matrix entry or bias in the deterministic core construction and readout), so existence of the comparator in the box and the coefficient bounds used in Section 6 are explicit once that construction is fixed.

## 5. An optional bound for ERM over the entire parameter box

One need not restrict training to the grid. For the same grid, use

    u = P log(2+2W/r)+log(4/delta),
    Q_J = 2V0 log(2) + 4V0 log(2/delta)/J,
    C_emp = L_m (M+sqrt(Q_J))/s
              + L_v [1/(2s)+(M+sqrt(Q_J))^2/(2s^2)].

With probability >=1-delta/2, P_J Y^2<=Q_J. This follows directly from E exp(Y^2/(4V0))<=sqrt(2) and Markov's inequality for the J independent tasks. On this event the empirical parameter loss is r C_emp-Lipschitz over net neighborhoods. The finite-net deviation event has probability >=1-delta/2. Hence, simultaneously for every theta in the box,

    |(P_J-P)ell_theta|
      <= A0[sqrt(8u/J)+u/J] + r(C_pop+C_emp).               (15)

Thus a xi-approximate empirical minimizer over all of Theta obeys

    E KL(p || q_{theta_hat})
      <= epsilon_app + T_tail(t0) + xi
           + 2A0[sqrt(8u/J)+u/J] + 2r(C_pop+C_emp).         (16)

Exact empirical minimizers exist: the parameter box is compact, every sample loss is continuous in parameters, and the final variance clip gives a positive denominator. Population losses are also continuous by the same envelope and dominated convergence. No assertion is made that a particular optimizer finds the minimizer. Taking r=1/J yields the familiar sqrt((P log J+log(1/delta))/J) leading rate with all other construction constants fixed.

## 6. Explicit parameter Lipschitz constants for residual ReLU attention

This section verifies (11) without a hidden covering-number oracle. Consider fixed width D, at most h attention heads, and a tokenwise two-layer ReLU MLP of hidden width F per block. Let every fixed or trainable matrix entry and bias in these blocks and the affine readout lie in [-W,W], W>=1. The external fixed input/output clips are treated separately. For N_tok=n+1 padded tokens use exactly the C002/Bai length-normalized attention

    a_i = z_i + (1/N_tok) sum_{heads,j}
                ReLU(<Q z_i,K z_j>) V z_j,
    z_i^+ = a_i + U2 ReLU(U1 a_i+b1)+b2.

Heads may be zeroed and MLPs may be identities, so this upper architecture covers the deterministic encoder and solver. Unlike row-normalized kernel attention, its denominator is the fixed sequence length and never approaches zero.

Let R_0 >=1 bound the infinity norm of input tokens after the fixed context-label clip; compact raw covariates and bounded constants supply such an explicit R_0. Define bounds recursively for l=0,...,L-1:

    A_l = R_l + h D^4 W^3 R_l^3,
    R_{l+1} = (1+FDW^2) A_l + F W^2 + W,
    C_0 = 0,
    C_l^att = (1+3hD^4W^3R_l^2) C_l
                  + 3hD^4W^2R_l^3,
    C_{l+1} = (1+FDW^2) C_l^att
                  + 2FW(D A_l+1)+1.                      (17)

Then every token after block l has infinity norm <=R_l, and for two parameter choices at distance d_theta the corresponding tokens differ by at most C_l d_theta.

Proof. ||Qz||_infinity<=DW R_l and the score is bounded by D^3W^2R_l^2. Each head contribution is bounded by D^4W^3R_l^3. Varying hidden states changes the cubic head expression by at most 3D^4W^3R_l^2 times their difference; varying Q,K,V at fixed states changes it by at most 3D^4W^2R_l^3 d_theta. ReLU is 1-Lipschitz. Summation with 1/N_tok cancels the token count. The affine-ReLU-affine residual has input Lipschitz constant 1+FDW^2 and parameter contribution bounded by 2FW(D A_l+1)+1. These observations give (17) by induction.

For a two-coordinate affine readout with entries/biases bounded by W, followed by the fixed output clips, one may take

    L_m = L_v = DW C_L + D R_L + 1.                        (18)

The bounds can be extremely loose but are explicit and finite. Fixed parameters in the construction can be included among the P parameters or kept fixed; either choice is covered provided their absolute values are also bounded by W. For varying layer widths/head counts one can use their maxima or the corresponding layerwise recursion.

The clips are themselves exact ReLU maps: clip_[a,b](x)=a+ReLU(x-a)-ReLU(x-b). A residual implementation writes the difference from x and can use four hidden ReLU units per clipped scalar. Thus a context-label clip and the two output clips require only fixed finite tokenwise MLP overhead. They do not require clipping target labels during training.

## 7. How to combine this with A02's deterministic theorem

1. Specify n, k, s and a joint input/query law independent of the GP/noises.
2. Choose a tail budget eta and B by (5), then M=B sqrt(nK/s).
3. Invoke the continuous-kernel construction with this B and scalar accuracies making (1) <=epsilon_app. Add fixed context and output clips.
4. Put the resulting architecture and comparator weights inside a finite parameter box [-W,W]^P. Record D,F,h,L,R0 and compute (17)--(18).
5. Apply (14) for finite-grid ERM or (16) for full-box ERM. The final error is approximation + explicit label tails + finite-sample generalization + stated empirical optimization error.

This closes the missing *statistical bridge* conditional on the deterministic approximation theorem, for the genuine GP experiment. It does not remove the continuity requirement for a uniform raw-input construction: arbitrary bounded discontinuous kernels remain subject to C003's obstruction.

## 8. Primary literature and novelty boundary

- Müller, Hollmann, Arango, Grabocka and Hutter, *Transformers Can Do Bayesian Inference*, ICLR 2022, https://arxiv.org/abs/2112.10510 . PFNs train on prior-sampled tasks to approximate posterior predictives. The proper-scoring identity is established background, not a new part of this report.
- Bai, Chen, Wang, Xiong and Mei, *Transformers as Statisticians: Provable In-Context Learning with In-Context Algorithm Selection*, https://arxiv.org/abs/2306.04637 . Supplies the residual normalized ReLU-attention architecture and constructive algorithmic/generalization precedents. The report's generic finite-net concentration is deliberately elementary and does not claim to improve their sharp complexity results.
- Kang, Lee and Cheng, *Transformers Can Learn Posterior Predictive Distributions In-Context*, ICML 2026, https://arxiv.org/html/2605.26713v1 . Provides a GP moment construction and binned-distribution approximation. Its population NLL statement is not by itself a finite-sample ERM theorem for Gaussian forward KL.
- Current nearby work requiring a separate overlap check: Hülskamp et al., *How Well Do Prior-Data Fitted Networks Amortize Bayesian Inference?*, https://arxiv.org/abs/2610.13764 . Located but not relied on in any proof here.

All inequalities above are proved in this report; literature citations identify precedents and delimit claims. No SGD convergence, novel universal transformer lower bound, or formal verification is asserted.
