# Sharp depth/width rates on a positive ray for bias-free ReLU networks

## 1. Model and result

Let d,n,h be positive integers. There are h hidden layers, all of width n, a scalar linear output, and no biases. All weights are independent centered Gaussians, of variance 2/d in the first layer and 2/n in every subsequent layer, including the output. The hidden activation is r(s)=max(s,0). Thus h counts hidden layers; the total number of weight layers is h+1.

Fix u in R^d with ||u||_2^2=d and a compact T subset of [0,infinity), with R=max T>0. Set K={tu:t in T}. Write P_{n,h} for the law of the network f on C(K), and P_infinity for the law of the Gaussian field

    F(tu)=sqrt(2) t G,    G ~ N(0,1).

All W2 distances on C(K) use the supremum norm. Define

    a2=1+5/n,
    a3=1+15/n+44/n^2,
    a4=1+30/n+251/n^2+558/n^3,
    D2=a2^h-1,
    D4=a4^h-4a3^h+6a2^h-3,
    A=sqrt(2) R.

The following bounds hold for all n,h:

    dTV(P_{n,h},P_infinity) <= min(1,6 D2),                         (1)
    W2(P_{n,h},P_infinity)
       <= A [4 sqrt(D4)+64 D4+sqrt(2) D2].                       (2)

For n>=100 there is also an all-depth lower bound

    W2(P_{n,h},P_infinity)
       >= A sqrt(2/pi) [1-exp(-h/(3n))].                        (2a)

In particular, along sequences n -> infinity, functional W2 convergence holds if and only if h/n ->0.

Here dTV(P,Q)=sup_B |P(B)-Q(B)|. For any function Phi on C(K) such that g(z)=Phi(tu -> sqrt(2)t z) is C^4 with bounded derivatives through order four,

    |E Phi(f)-E Phi(F)| <= ||g''''||_infinity D2/8.               (3)

In particular, if Phi has bounded Frechet derivatives through order four, its fourth derivative bound M gives ||g''''||_infinity <= M A^4.

Put rho=h/n. Uniformly along every sequence n -> infinity, h>=1, rho ->0, the smooth bounded test Phi(q)=cos(q(Ru)/A) satisfies

    E Phi(f)-E Phi(F) = [5 exp(-1/2)/8] rho + o(rho).             (4)

Consequently both functional TV and functional W2 have order h/n in this regime: each has upper and lower bounds by positive constants times h/n (with the W2 constants scaled by A). In particular the rate at fixed positive depth is n^(-1), including for this smooth test. The same TV distance holds for every k-point marginal containing at least one nonzero input, independently of k. These statements concern a rank-one special case only.

## 2. Exact reduction to an independent product

Positive homogeneity of ReLU and linearity of the output imply, for every realization of all weights,

    f(tu)=t f(u),    t>=0.                                      (5)

Let Q_j be the average of the squares of the j-th hidden layer activations at u, and put Q_0=1. First-layer preactivations have law sqrt(2)G_i, independently. At every later hidden layer, conditionally on the previous activations, the preactivations are independent N(0,2Q_{j-1}). Therefore their squared positive parts give the transition

    Q_j | Q_{j-1}=q  has law q B,
    B=(1/n) sum_{i=1}^n Y_i,    Y_i=2(G_i^+)^2.                 (6)

This statement remains true at q=0, where the next layer is zero. The transition kernel in (6) can be realized using independent copies B_1,...,B_h, so the joint norm process has the law Q_j=product_{l<=j} B_l. Independence of these copies is a representation of the transition law, not an assertion that ratios on a zero-norm event are defined.

Conditionally on the last hidden layer, the output is N(0,2Q_h). Thus, jointly with the entire field,

    f(tu) has law sqrt(2) t X,
    X=sqrt(V)G,    V=product_{j=1}^h B_j,                       (7)

where G is independent of the B_j. In particular EV=1. This also identifies the NNGP covariance as 2st at su,tu.

The map J:z -> (tu -> sqrt(2)t z) is continuous, injective, and has inverse q -> q(Ru)/A on its image. Its image is closed, and ||J(z)-J(w)||_infinity=A|z-w|. Both laws are supported on that image. Pulling back and pushing forward arbitrary couplings gives

    W2(P_{n,h},P_infinity)=A W2(Law(X),Law(G)),
    dTV(P_{n,h},P_infinity)=dTV(Law(X),Law(G)).                  (8)

The TV equality follows in both directions by measurable pushforward and the evaluation inverse. The same reasoning applies to a vector of k evaluations if any input is nonzero; it also applies when that vector's covariance matrix is singular. If all inputs are zero, both vector laws are identical.

## 3. Product moments

Symmetry of G and the Gaussian even-moment recursion give

    EY^r=2^(r-1)(2r-1)!!,    r>=1,

so EY=1, EY^2=6, EY^3=60, EY^4=840. Hence for Z=Y-1,

    EZ=0, EZ^2=5, EZ^3=44, EZ^4=633.

If U=B-1=n^(-1) sum Z_i, independence and centering give

    EU^2=5/n,
    EU^3=44/n^2,
    EU^4=[n*633+3n(n-1)*25]/n^4
         =75/n^2+558/n^3.                                    (9)

Expanding (1+U)^r for r=2,3,4 yields EB^r=a_r as stated above. Independence across hidden layers then gives EV^r=a_r^h. Thus

    E(V-1)^2=D2,    E(V-1)^4=D4.                              (10)

In particular these quantities are nonnegative; formulas with cancellation should be evaluated with sufficient precision. The fourth cumulant of X is exactly

    EX^4-3(EX^2)^2=3 D2.                                     (11)

## 4. A total-variation bound for arbitrary nonnegative variance mixtures

This section uses only V>=0, EV=1, and E(V-1)^2<infinity. Let N_v be the centered Gaussian probability measure of variance v, including N_0=delta_0. For v>0 let p_v denote its density. Differentiation gives

    p_v'(x) = (1/(2v)) H2(x/sqrt(v)) p_v(x),
    p_v''(x)= (1/(4v^2)) H4(x/sqrt(v)) p_v(x),                 (12)

where H2(z)=z^2-1 and H4(z)=z^4-6z^2+3. The primes here refer to variance, not spatial differentiation. The triangle inequality and Gaussian moments imply

    ||p_1'||_1 <=1,
    ||p_v''||_1 <=3/v^2 <=12,    v>=1/2.                     (13)

For v>=1/2, Taylor's formula along the interval between 1 and v therefore bounds the variation norm of the signed remainder

    R_v=N_v-N_1-(v-1)p_1'(x)dx

by 6(v-1)^2. For 0<=v<1/2, the variation norm is at most 2+|v-1|<=3, hence at most 12(v-1)^2. This includes v=0 without assuming a density. Consequently ||R_v||_var<=12(v-1)^2 for every v>=0.

Averaging these signed measures cancels the linear term because E(V-1)=0. The variation norm of their average is at most 12D2, and TV for probability measures is half their variation norm. This proves (1), using (8).

## 5. A W2 bound using fourth moments and truncation

This section again applies to any V>=0 of mean one with finite fourth centered moment. Write delta=V-1 and set

    Vbar=V if |delta|<=1/4, and Vbar=1 otherwise;
    e=Vbar-1,    b=Ee,    q=Ee^2.

Then |e|<=1/4, q<=D2, and centering of delta gives

    |b|=|E[delta 1_{|delta|>1/4}]| <=64 D4.                   (14)

Indeed |delta|<=64 delta^4 on the indicated event. With the same independent G, a coupling of X=sqrt(V)G and Xbar=sqrt(Vbar)G has squared cost

    E(sqrt(V)-sqrt(Vbar))^2
      <=E[delta^2 1_{|delta|>1/4}] <=16 D4.                  (15)

The first inequality uses (sqrt(v)-1)^2 <=(v-1)^2 for v>=0. Hence W2(X,Xbar)<=4sqrt(D4).

Let p=E p_{Vbar}, and let phi=p_1 be the standard normal density. For v,w in [3/4,5/4], direct Gaussian integration yields

    integral p_v(x)p_w(x)/phi(x) dx
       =(v+w-vw)^(-1/2).                                   (16)

For independent e,e' with the law above, this identity and Tonelli's theorem give

    chi^2(p,phi)=E[(1-ee')^(-1/2)]-1.                       (17)

For |z|<=1/16, Taylor's formula for F(z)=(1-z)^(-1/2) gives

    0<=F(z)-1-z/2<=z^2.                                    (18)

In fact F''(z)=(3/4)(1-z)^(-5/2)<2 on this interval, so the integral Taylor remainder is bounded by z^2. It follows that

    chi^2(p,phi) <= b^2/2+q^2.                              (19)

For completeness, the needed one-dimensional Gaussian transport bound is proved here. Let T be the increasing quantile map taking G to density p. The density p is smooth, positive, and a mixture of centered Gaussians of variances in [3/4,5/4]. Symmetry and Gaussian tail comparison imply

    sqrt(3/4)|x| <= |T(x)| <= sqrt(5/4)|x|,
    sign T(x)=sign x.                                      (20)

The change-of-variables formula p(T(x))T'(x)=phi(x) gives

    H(p|phi)=E[(T(G)^2-G^2)/2-log T'(G)].                    (21)

All terms are integrable: the mixture density has upper and lower Gaussian bounds with these two fixed variances; (20) then bounds its logarithm after composition by a constant times 1+x^2. Also integration by parts, first on a bounded interval and then letting its endpoints diverge, gives E[G T(G)]=E[T'(G)]. Boundary terms vanish by (20), and T'>0 makes the derivative integral finite. With u=T-id, (21) therefore becomes

    H(p|phi)=E[u(G)^2]/2 + E[T'(G)-1-log T'(G)]
             >= E[u(G)^2]/2.                               (22)

The coupling (G,T(G)) implies W2(p,phi)^2<=E u(G)^2. Finally log r<=r-1 implies H(p|phi)<=chi^2(p,phi). Combining (19)-(22) gives

    W2(Xbar,G) <=sqrt(b^2+2q^2) <=|b|+sqrt(2)q
                  <=64D4+sqrt(2)D2.                         (23)

The triangle inequality, (15), and (8) prove (2). This argument handles the atom V=0 by truncation; it never applies a density or entropy calculation directly to X.

## 6. Smooth tests and a matching lower bound

Let g be C^4 with bounded derivatives through order four, and define H(v)=E g(sqrt(v)G), v>=0. The Gaussian heat equation, or two integrations by parts against a Gaussian density, gives

    H'(v)=(1/2)E g''(sqrt(v)G),
    H''(v)=(1/4)E g''''(sqrt(v)G),    v>0.                   (24)

Dominated convergence extends these formulas to right derivatives at zero. Taylor's formula about v=1 thus gives

    |H(v)-H(1)-H'(1)(v-1)| <=||g''''||_infinity (v-1)^2/8.

Average at V, cancel the linear term, and use (7) to prove (3).

For g(z)=cos z, the Gaussian characteristic function gives the exact gap

    Delta=E cos X-E cos G=E exp(-V/2)-exp(-1/2).              (25)

It is nonnegative by convexity. The third derivative of v -> exp(-v/2) has absolute value at most 1/8 on [0,infinity), so Taylor expansion through order two yields

    |Delta-exp(-1/2)D2/8|
       <= E|V-1|^3/48 <=sqrt(D2 D4)/48.                     (26)

Since cos is 1-Lipschitz and bounded by one,

    W2(Law(X),Law(G)) >=Delta,
    dTV(Law(X),Law(G)) >=Delta/2.                            (27)

The first follows directly by applying the Lipschitz inequality to any coupling and then Cauchy-Schwarz. The second is the usual bound |E_P g-E_Q g|<=2dTV(P,Q) for |g|<=1; it also follows by integrating the positive and negative parts of the signed difference of the measures. Thus (26) supplies explicit finite-n lower bounds when its right-hand-side remainder is smaller than its main term.

## 7. Uniform depth control

First, Bernoulli's inequality and 1+x<=exp(x) give

    5rho <=D2 <=exp(5rho)-1,
    0<=D2-5rho <=(25/2)exp(5rho)rho^2.                      (28)

Here and below h is an integer; these inequalities do not require h to be fixed.

To bound D4 without an unproved uniform expansion, for x>=0 set

    b2(x)=1+5x,
    b3(x)=1+15x+44x^2,
    b4(x)=1+30x+251x^2+558x^3,
    B(x)=b4(x)^h-4b3(x)^h+6b2(x)^h-3.

Then B(0)=B'(0)=0, and D4=B(1/n). For 0<=x<=1/n with n>=100,

    1<=bj(x)<=exp(33x),    j=2,3,4;
    b2'<=5, b3'<=16, b4'<=36;
    b3''=88, b4''<=536, b2''=0.                            (29)

For example b4(x)<=1+(30+2.51+0.0558)x<=exp(33x), and b4'(x)<=30+5.02+0.1674<36. When h>=2, twice differentiating bj(x)^h, bounding the powers by exp(33hx), and using the triangle inequality gives

    |B''(x)| <=exp(33hx)
       [h(h-1)(36^2+4*16^2+6*5^2)+h(536+4*88)]
      <=3358 h^2 exp(33hx).                                (30)

For h=1 the terms with h(h-1) are absent and the same bound holds. Integrating twice from zero proves the explicit bound

    D4 <=1679 exp(33rho)rho^2,    n>=100.                   (31)

Equations (28) and (31) imply D2=5rho+O(rho^2), D4=O(rho^2) uniformly when rho<=1, with absolute constants. In (26) the remainder is therefore O(rho^(3/2))=o(rho) when rho->0. This proves (4). Combining (1), (2), and (27) proves both matching orders claimed in Section 1. Constants in (31) are deliberately coarse; the sharp assertion is the order in depth/width and the coefficient in (4), not a sharp W2 multiplicative constant.

## 8. A second lower bound and the depth threshold

The one-layer multiplier B has mean one, variance 5/n, and fourth centered moment 75/n^2+558/n^3. If n>=100 this last quantity is at most 81/n^2. Since (B-1)^2 <=(B-1)^4 when B>2,

    E[(B-1)^2 1_{B<=2}] >=5/n-81/n^2 >=4/n.                (32)

The identity (sqrt(B)-1)^2=(B-1)^2/(sqrt(B)+1)^2, together with EB=1, gives

    1-E sqrt(B)=(1/2)E(sqrt(B)-1)^2
       >= [1/(2(sqrt(2)+1)^2)] E[(B-1)^2 1_{B<=2}]
       >=1/(3n),                                          (33)

where (sqrt(2)+1)^2<6 was used in the last inequality. By independence,

    E|X|=sqrt(2/pi) (E sqrt(B))^h
         <=sqrt(2/pi) exp(-h/(3n)).                         (34)

The function |z| is 1-Lipschitz. Comparing its expectations for X and G, and using (8), proves (2a). This is independent of the cosine lower-bound argument. If h/n fails to tend to zero, (2a) is bounded away from zero along a subsequence. If h/n tends to zero, (2) and (28)-(31) tend to zero. This proves the stated W2 convergence threshold.

## 9. Scope and boundary cases

The proof requires no positive lower bound on a k-input covariance matrix. Its functional conclusion is possible because the support of both process laws is the same one-dimensional subspace of C(K). It says nothing about the infinite-rank kernel case on a set containing non-collinear inputs, added biases, general Lipschitz activations, or the best constant in W2.

If K={0}, both fields are zero and the lower bounds are inapplicable. Inputs of both signs are not covered by (5). The quantitative matching statement assumes h/n->0; the all-n,h upper bounds (1)-(3) remain valid outside this regime. This proof establishes a checkable special case and makes no claim of literature priority.
