# Two-token merging with exponentially small noise

Fix two tokens on the unit circle, identity query, key and value matrices, and row-normalized attention **including self-attention**. Write their angles as theta_1, theta_2. For beta > 0 and nu >= 0 the model considered here is

    d theta_i = [sum_{j=1}^2 exp(beta cos(theta_j-theta_i))
                  sin(theta_j-theta_i)
                 / sum_{j=1}^2 exp(beta cos(theta_j-theta_i))] dt
                + sqrt(2 nu) d W_i,

where W_1 and W_2 are independent real Brownian motions and angles are taken modulo 2 pi. Thus nu is the individual angular diffusivity; beta controls attention sharpness. The deterministic equation is the normalized SA model, as defined, for example, in Section 3.2 of Philippe Rigollet, [*The Mean-Field Dynamics of Transformers*, arXiv:2512.01868](https://arxiv.org/abs/2512.01868). The stochastic perturbation is specified explicitly above.

Let X_t in [0,pi] be the shorter angular distance between the tokens. Fix constants

    0 < delta < x < pi,        X_0 = x,

and let tau_delta = inf{t >= 0 : X_t <= delta}. This is a first entrance time into a prescribed merging neighborhood, not an exact collision time or a claim of permanent synchronization.

## Theorem

Set a(s) = 1-cos(s) and h_beta(s) = 2 sin(s)/(1+exp(beta a(s))).

1. With nu=0, the deterministic merging time is

       T_beta(x,delta) = (1/2) integral_delta^x
                            [1+exp(beta a(s))]/sin(s) ds,

   and, for fixed delta,x as beta tends to infinity,

       T_beta(x,delta) ~ exp(beta a(x))/(2 beta sin(x)^2).

2. For nu>0, write u_beta,nu(x) = E_x[tau_delta]. Its exact value is

       u_beta,nu(x) = (1/(2 nu)) integral_delta^x integral_y^pi
             exp[-(1/(2 nu)) integral_y^z h_beta(s) ds] dz dy.       (1)

   If nu=nu_beta>0 and -log(nu_beta)/beta tends to a finite r>=0, then

       lim_{beta->infinity} log(u_beta,nu_beta(x))/beta
             = min{1-cos(x), r}.                                  (2)

In particular, for nu_beta=exp(-r beta), noise changes the logarithmic mean merging scale precisely when r < 1-cos(x). If nu_beta decreases polynomially in beta, the logarithmic scale in (2) is zero.

## Proof of the reduction

For D=theta_2-theta_1, the self term has zero tangential component. The cross term divided by the row sum is

    sin(D)/(1+exp(beta(1-cos(D))))

for theta_1, and its negative for theta_2. Consequently the lifted difference satisfies

    dD = -h_beta(D) dt + sqrt(4 nu) dB,

where h_beta is extended as an odd 2 pi-periodic function and B=(W_2-W_1)/sqrt(2) is standard Brownian motion. Its generator is 2 nu d^2/dD^2 - h_beta(D) d/dD. Folding the difference circle to its shorter distance gives reflection at pi. On the interval (delta,pi), before killing at delta, the distance generator therefore is

    Lf(s) = 2 nu f''(s) - h_beta(s) f'(s),      f'(pi)=0.           (3)

Indeed, a function of the shorter distance lifts to an even function about pi on the difference circle, and differentiability across pi imposes exactly this Neumann condition. No boundary condition at zero is needed before tau_delta.

For nu=0 and s in (0,pi), h_beta(s)>0, so the gap decreases strictly, and separation of variables gives part 1's integral.

For its asymptotic, the contribution of the term 1 is a finite constant independent of beta. In the exponential term substitute v=a(s), so dv=sin(s) ds. It becomes

    (1/2) integral_{a(delta)}^{a(x)} exp(beta v) g(v) dv,
    g(v)=1/[v(2-v)].

The continuous function g is bounded on this fixed integration interval. Put w=beta(a(x)-v). The integral divided by exp(beta a(x))/(2 beta) is

    integral_0^{beta(a(x)-a(delta))} exp(-w) g(a(x)-w/beta) dw.

The integrand, extended by zero outside that interval, is bounded by a fixed constant times exp(-w), and converges pointwise to exp(-w)g(a(x)). Dominated convergence gives the limit g(a(x))=1/sin(x)^2. The constant contribution is negligible. This proves part 1, including its prefactor.

## Proof of the exact noisy formula

Define, for delta<=y<=pi,

    p(y) = (1/(2 nu)) integral_y^pi
                exp[-(1/(2 nu)) integral_y^z h_beta(s) ds] dz,
    u(s) = integral_delta^s p(y) dy.

All integrands are smooth on a compact interval. Direct differentiation gives

    p'(y) = -1/(2 nu) + h_beta(y) p(y)/(2 nu).

Hence Lu=-1, u(delta)=0, u'(pi)=0, and u>=0. In particular u is bounded. Apply Ito's formula to u(X_{t wedge tau_delta}). The reflection term vanishes because u'(pi)=0, while the stopped stochastic integral has mean zero because u' is bounded. Thus

    E[t wedge tau_delta]
        = u(x)-E[u(X_{t wedge tau_delta})] <= u(x).

Monotone convergence implies E[tau_delta]<=u(x)<infinity, so tau_delta is finite almost surely. Bounded convergence, continuity at delta, and X_{tau_delta}=delta then give E[u(X_{t wedge tau_delta})]->0. The same identity now proves E[tau_delta]=u(x), which is (1).

## Lower bound for the logarithmic scale

Choose eta>0 with x-eta>delta and x+eta<pi. If y is in [x-eta,x] and z in [y,y+eta], every s in [y,z] satisfies a(s)>=a(x-eta), and therefore

    0 <= h_beta(s) <= M_beta := 2 exp[-beta a(x-eta)].

Restrict both integrations in (1) to these ranges. Then

    u_beta,nu(x) >= eta [1-exp(-M_beta eta/(2 nu))]/M_beta.

For t>=0, 1-exp(-t) >= (1-exp(-1)) min{t,1}. It follows that

    u_beta,nu(x) >= (1-exp(-1)) eta
                          min{eta/(2 nu), 1/M_beta}.

Taking logarithms, dividing by beta, and using the assumed limit for nu gives

    liminf log(u_beta,nu_beta(x))/beta >= min{r,a(x-eta)}.

Let eta decrease to zero to obtain the lower bound min{r,a(x)}. This argument includes the equality r=a(x) and the case r=0.

## Upper bound, including outward excursions

Since h_beta>=0 on [delta,pi], the exponential in (1) is at most one. Consequently

    u_beta,nu(x) <= (x-delta)(pi-delta)/(2 nu).                    (4)

If r<=a(x), this already proves the required upper bound r.

Suppose r>a(x). Choose eta>0 so that x+eta<pi and a(x+eta)<r. For all sufficiently large beta, h_beta is decreasing on [delta,pi]. To verify this, differentiate:

    h_beta'(s)/h_beta(s)
      = cot(s) - beta sin(s) exp(beta a(s))/(1+exp(beta a(s))).

For s>=pi/2 this is negative. If delta<pi/2 and delta<=s<=pi/2, it is at most cot(delta)-beta sin(delta)/2, also negative for large beta. If delta>=pi/2 only the first case is needed.

Put b_beta=h_beta(x+eta)>0. For y in [delta,x] and z in [y,y+eta], monotonicity gives h_beta(s)>=b_beta for all s in [y,z]. For z>=y+eta it gives integral_y^z h_beta(s) ds>=eta b_beta. Splitting the inner integral in (1) at y+eta therefore yields

    p(y) <= 1/b_beta + [pi/(2 nu)] exp[-eta b_beta/(2 nu)],

and hence

    u_beta,nu(x) <= (x-delta)
           [1/b_beta + pi/(2 nu) exp(-eta b_beta/(2 nu))].        (5)

The second term is the explicit bound for possible excursions to larger gaps. Here

    log(b_beta)/beta -> -a(x+eta),
    log(b_beta/nu_beta)/beta -> r-a(x+eta)>0.

Thus b_beta/nu_beta grows exponentially in beta. The logarithm of the second term in the brackets of (5), divided by beta, tends to minus infinity: its positive part is r+o(1), whereas eta b_beta/(2 nu_beta beta) tends to infinity. The first term has logarithmic scale a(x+eta). Consequently

    limsup log(u_beta,nu_beta(x))/beta <= a(x+eta).

Let eta decrease to zero. This gives the upper bound a(x), proving (2).

## Scope and exceptional cases

The theorem concerns two equal-weight tokens, or the deterministic motion of two exactly coincident groups of equal size. Independent noises within larger groups do not preserve coincidence; no stochastic group reduction is claimed.

The fixed-gap assumptions matter. At x=pi the deterministic drift is zero and the merging time is infinite. At delta=0 the deterministic integral diverges, so exact deterministic collision takes infinite time. Neither endpoint is covered by the theorem. A beta-dependent initial gap or target requires different estimates.

The exponential scale arises from weak deterministic attraction, not exit from a stable potential well. Formula (2) is a joint-parameter first-passage result. It neither counts clusters formed from generic data nor proves a Freidlin–Wentzell law for a many-token system. No claim of priority over the existing two-particle literature is made.

## Independent algebraic checks

Write c=x_1 dot x_2 and w=1/(1+exp(beta(1-c))). Directly in vector coordinates, the deterministic equation gives

    dc/dt = 2 w (1-c^2).

Indeed, the two projected cross terms each contribute w(1-c^2). Thus the time to go from c=cos(x) to c=cos(delta) is

    (1/2) integral_{cos(x)}^{cos(delta)}
                       [1+exp(beta(1-c))]/(1-c^2) dc.

Endpoint asymptotics in this coordinate give

    exp(beta(1-cos(x))) / [2 beta (1-cos(x)^2)],

which agrees with part 1, including the factor 2 and the square of the sine.

For the stochastic coefficient, independent angular Brownian motions each have generator nu d^2/dtheta_i^2. Their sum acting on f(theta_2-theta_1) is 2 nu f'', verifying (3) independently of the Brownian difference representation. In vector Ito coordinates each token has the radial correction -nu x_i dt; the two corrections contribute -2 nu c to the cosine drift. Consequently

    L cos(D) = 2 w (1-c^2) - 2 nu c,

also obtained by applying (3) to cos(s).

Finally, the integral in the exponent of (1) has the explicit primitive

    integral_y^z h_beta(s) ds
      = (2/beta) [log(1+exp(-beta a(y)))
                  - log(1+exp(-beta a(z)))].

Differentiating the right side in z gives h_beta(z), and its value at z=y is zero. This checks the potential sign: the exponential in (1) is never greater than one. A reversed sign would incorrectly predict an activated barrier against the attractive drift.
