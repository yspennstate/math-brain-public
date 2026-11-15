# A ceiling on the direct local-hardness incidence certificate

Depth counts affine maps, including the output map. Thus depth 2 means one hidden ReLU layer. All norms on the input space are Euclidean. An error parameter denotes the L2 norm; its square is mean squared error.

## Statement

Let f: R^d -> R be globally L-Lipschitz, with L > 0. Let

    mu = sum_{i=1}^M p_i mu_i,

where p_i > 0, sum_i p_i = 1, and mu_i is a probability measure supported in the closed ball B_i = B(c_i,r_i). The balls need not be disjoint and their radii need not agree. Fix a positive integer v and epsilon > 0. Suppose that for every i and every depth-2 ReLU network h of hidden width at most v, with arbitrary real parameters,

    integral (f-h)^2 d mu_i >= epsilon^2.                 (1)

For an affine hyperplane H, let I(H) be the total mixture weight of the balls that H meets, and set

    alpha = sup_H I(H).

Suppose that for some unit vector u all projected centers <u,c_i> lie in an interval of length D. Then:

    r_i >= epsilon/L for every i,                       (2)
    alpha >= 2 epsilon / (LD + 2 epsilon).              (3)

Every depth-3 ReLU network g whose first and second hidden widths are W and at most v satisfies

    ||f-g||_{L2(mu)}^2 >= epsilon^2 max(0,1-W alpha).    (4)

Consequently the width threshold obtained from (4), for an approximation error at most eta with 0 <= eta < epsilon, is

    W >= T := (1-eta^2/epsilon^2)/alpha,

and that threshold obeys

    T <= (1-eta^2/epsilon^2)(1+LD/(2 epsilon)).          (5)

This is a ceiling on this specific numerical certificate. It is not an upper bound on the actual width required to approximate f.

## Proof

A constant function belongs to the depth-2 class in (1): take all hidden and output weights zero and use the output bias. In particular h(x)=f(c_i) is available. For x in B_i, Lipschitz continuity gives

    |f(x)-f(c_i)| <= L ||x-c_i|| <= L r_i.

Integrating and using (1) proves epsilon^2 <= L^2 r_i^2, hence (2).

Write r_0 = epsilon/L, a = min_i <u,c_i>, and b = max_i <u,c_i>; thus b-a <= D. Consider the parallel hyperplanes

    H_t = {x : <u,x> = t}.

Each smaller ball B(c_i,r_0) is contained in B_i. Since u is a unit vector, H_t meets this smaller ball exactly when |t-<u,c_i>| <= r_0. Define

    q(t) = sum_i p_i 1{|t-<u,c_i>| <= r_0}.

For every t, q(t) <= I(H_t) <= alpha. Each indicator has integral 2r_0, so finite summation gives

    integral_[a-r_0,b+r_0] q(t) dt = 2r_0 sum_i p_i = 2r_0.

The integration interval has length b-a+2r_0 <= D+2r_0. Therefore

    2r_0 <= alpha (D+2r_0).

Substitution of r_0 proves (3). This also covers D=0, in which case a hyperplane through the common projected coordinate meets every ball and alpha=1.

Write the depth-3 network as

    g = A_3 o sigma o A_2 o sigma o A_1,

where A_j are affine and sigma is coordinatewise ReLU. First-layer neurons with zero input vector are constant, including identically zero neurons; they do not switch anywhere. Each remaining first-layer neuron has a genuine activation hyperplane. There are at most W such hyperplanes.

Call a ball hit if at least one of these hyperplanes meets it. The total mixture weight of hit balls is at most W alpha, by the union bound on their index sets. If B_i is unhit, each nonconstant first-layer preactivation has a fixed sign on the connected ball B_i. Constant neurons have fixed activation too. Hence there is a fixed diagonal matrix S_i with diagonal entries in {0,1} such that

    sigma(A_1(x)) = S_i A_1(x) for all x in B_i.

Thus g agrees throughout B_i with

    h_i = A_3 o sigma o (A_2 o S_i o A_1),

a depth-2 network of width at most v. Its parameters may differ between balls. Assumption (1) applies because it allows arbitrary real parameters. Each unhit ball contributes at least p_i epsilon^2 to the mixture error. The sum of the unhit mixture weights is at least max(0,1-W alpha). This proves (4). Overlapping balls do not cause a problem: integration against a mixture is the weighted sum of its component integrals.

If ||f-g||_{L2(mu)} <= eta < epsilon, (4) implies 1-W alpha <= eta^2/epsilon^2, so W >= T. Taking reciprocals in (3), which is valid because alpha>0, gives (5).

## Consequence for polynomial weights and polynomial support scale

Suppose f is represented by a depth-4 network with hidden widths n_1,n_2,n_3 and every matrix entry of magnitude at most B. Biases do not affect its Lipschitz constant. ReLU is 1-Lipschitz, and a matrix with s rows, t columns and entries bounded by B has operator norm at most its Frobenius norm, which is at most B sqrt(st). Multiplying the four matrix bounds gives

    Lip(f) <= B^4 sqrt(d) n_1 n_2 n_3.                  (6)

Indeed the four square-root factors are sqrt(n_1 d), sqrt(n_2 n_1), sqrt(n_3 n_2), and sqrt(n_3). Their product is sqrt(d)n_1 n_2 n_3.

Assume the chosen patch centers lie in [-R,R]^d. Taking u to be a coordinate vector gives D <= 2R. Use the positive upper bound L_* = B^4 sqrt(d)n_1 n_2 n_3 in place of L in the theorem; this is legitimate because a function is also Lipschitz with any larger constant. Then (5) yields

    T <= (1-eta^2/epsilon^2)
         (1 + R B^4 sqrt(d)n_1 n_2 n_3 / epsilon).      (7)

For polynomially bounded R, B, and hidden widths, and inverse-polynomial epsilon, the right side is polynomial in d. This remains true for arbitrarily many balls and arbitrary mixture weights. Replacing alpha in the union bound by any valid upper bound on alpha only makes T smaller.

The local hardness hypothesis requires hardness against unrestricted depth-2 parameters. If instead it only concerns bounded parameters, the collapsed network must be checked against those bounds separately. Formula (7) makes no assertion about arguments exploiting that additional restriction, about non-ball patches, or about stronger incidence arguments that use joint structure of many hyperplanes. It also does not address exact-computation lower bounds, whose local error scale may tend to zero.

## Unequal local hardness levels

The ceiling does not require a common positive local hardness level. Replace (1) by a possibly different lower bound epsilon_i^2 >= 0 for each component, against the same depth-2 class, and put

    beta = sum_i p_i epsilon_i^2 > 0,
    gamma = sup_H sum_{i: H meets B_i} p_i epsilon_i^2.

The same collapse and union bound, now weighted by local squared hardness, give

    ||f-g||_{L2(mu)}^2 >= max(0,beta-W gamma).           (8)

For any t with 0 < t < sqrt(beta), let J = {i: epsilon_i >= t}. Components outside J contribute at most t^2 to beta, since their mixture weights sum to at most one. Therefore

    sum_{i in J} p_i epsilon_i^2 >= beta-t^2.

The constant-approximation argument proves r_i >= epsilon_i/L, hence r_i >= t/L on J. Repeat the parallel-hyperplane integration with smaller balls of radius t/L and weights p_i epsilon_i^2 on J. These weights need not sum to one. The result is

    gamma >= (beta-t^2) 2t / (LD+2t).                 (9)

Choose t = sqrt(beta)/2. Then beta-t^2 = 3beta/4 and 2t = sqrt(beta), so

    beta/gamma <= (4/3)(1+LD/sqrt(beta)).             (10)

For eta^2 < beta, define T_var = (beta-eta^2)/gamma. Formula (8) certifies W >= T_var whenever the approximation error is at most eta. Formula (10) bounds this numerical threshold:

    T_var <= (1-eta^2/beta)(4/3)(1+LD/sqrt(beta)).     (11)

Thus a polynomial ceiling still holds when LD and 1/sqrt(beta) are polynomially bounded, even if some individual local hardness levels are zero or exponentially small.

## Independent checks

The radius bound has a second proof using variance. For independent X,Y with law mu_i, the best constant approximation has error

    Var(f(X)) = (1/2) E[(f(X)-f(Y))^2]
              <= (L^2/2) E[||X-Y||^2]
              = L^2 (E||X-c_i||^2 - ||EX-c_i||^2)
              <= L^2 r_i^2.

All expectations exist because the ball is bounded and f is Lipschitz. Combining with (1) recovers (2).

The matrix calculation in (6) can also be obtained without operator norms. For a displacement z, the first hidden layer has each coordinate difference at most B||z||_1 <= B sqrt(d)||z||_2. The next two layers multiply this coordinate bound by n_1 B and n_2 B. The scalar output multiplies it by n_3 B. This again gives B^4 sqrt(d)n_1 n_2 n_3 ||z||_2.

The hyperplane integral can independently be evaluated by sorting the 2M interval endpoints and summing length times the constant incidence on each open interval. The accompanying exact-arithmetic script checks this identity against the sum of individual interval lengths, including unequal weights, equal projected centers, and touching endpoints. It also checks (9) directly for unequal local hardness levels and zero-hardness components. These finite checks validate algebra and edge cases; the proof above establishes the general statement.
