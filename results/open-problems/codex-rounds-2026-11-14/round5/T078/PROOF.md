# Sparse injections on the full cubic lattice

Write |x|=max_i |x_i| on Z^3. The lattice has one undirected edge between each pair at distance one in a coordinate direction. Every edge has conductance one. For a finitely supported real function f put

    D(f)=sum_{unordered edges {x,y}} (f(x)-f(y))^2.

Edges with one endpoint outside the support are included. This convention counts an edge once.

## 1. Statement

Let I be a finite index set, m=|I|, and let x_i in Z^3 be labels, with repetitions permitted. Suppose that, for some L>=0 and 0<=alpha<1,

    #{i: |x_i-z|<=r} <= L(1+r)^alpha                 (1)

for every z in Z^3 and every real r>=0. For each i let mu_i be a nonnegative finitely supported measure on Z^3, of total mass at most one, supported on |y-x_i|<=R, where R>=0. Set g=sum_i mu_i.

For a finite set Omega containing the supports of the mu_i, extend functions on Omega by zero and let

    (A_Omega f)(x)=sum_{y:y~x} (f(x)-f(y)),  x in Omega.

Then A_Omega is invertible and u_Omega=A_Omega^{-1}g satisfies

    D(u_Omega)=sum_x g(x)u_Omega(x)
       <= [1000 L/(1-alpha)] (1+R)^alpha m.          (2)

The constant is deliberately loose. The bound is uniform in Omega and in the measures. In particular, it allows distinct labels to send all their mass to the same site.

There also exists an antisymmetric current J on the full lattice, of divergence g, with

    sum_{unordered edges {x,y}} J(x,y)^2
       <= [1000 L/(1-alpha)] (1+R)^alpha m.          (3)

Here an arbitrary orientation is chosen for each summand; antisymmetry makes its square independent of that choice. The divergence is div J(x)=sum_{y~x} J(x,y).

For a finite set S satisfying (1), its Dirichlet capacity, defined by

    cap(S)=inf {D(f): f finitely supported, f>=1 on S},

obeys

    cap(S)>=[(1-alpha)/(1000 L)] |S|                (4)

when S is nonempty. The displacement exponent in (2) cannot be reduced uniformly for fixed 0<alpha<1. At alpha=1 there is no uniform bound of the form C L m even when R=0.

These are statements about the full lattice. No estimate for random removed sites, exchange-loop returns, or magnetization is assumed or concluded.

## 2. A Green-function bound, with its normalization

Let X_t be continuous-time simple random walk which jumps across each incident edge at rate one. Its generator is -A, where

    (Af)(x)=sum_{y~x}(f(x)-f(y)).

Write p_t(x)=P_0(X_t=x) and G(x)=integral_0^infinity p_t(x) dt. We prove

    0<=G(x)<=1000/(1+|x|).                          (5)

Each coordinate of X_t is the difference of independent Poisson(t) variables; the three coordinates are independent. Fourier inversion on Z gives

    p_t^(1)(n)=(1/(2pi)) integral_{-pi}^pi
                 exp[-2t(1-cos theta)] exp(-in theta) dtheta.

This inversion follows by expanding the two Poisson characteristic functions and using that the integral of exp(ik theta) over this interval is zero for nonzero integer k. Since 1-cos theta>=2theta^2/pi^2 for |theta|<=pi,

    sup_n p_t^(1)(n) <= sqrt(pi)/(4sqrt(t)).

The trigonometric inequality follows from sin v>=2v/pi on [0,pi/2], which follows from concavity of sin there. Independence and pi<4 now give, for t>0,

    sup_x p_t(x) <= min(1,t^(-3/2)).                 (6)

Consequently G(0)<=integral_0^1 1 dt+integral_1^infinity t^(-3/2)dt=3. The same argument proves that every G(x) is finite.

For a>=0, the one-coordinate moment generating function is

    E exp(lambda X_t^(1))=exp[2t(cosh lambda-1)].

For 0<=lambda<=1, the power series gives cosh lambda-1<=lambda^2: divide the series by lambda^2 and bound its sum by cosh(1)-1<1. The latter inequality also follows from e<3 and e^(-1)<1. Chernoff's inequality with lambda=min(a/(4t),1), including a=0 directly, gives

    P(|X_t^(1)|>=a)
       <=2 exp[-min(a^2/(8t),a/2)].

Indeed, if a<=4t the exponent -lambda a+2t lambda^2 is -a^2/(8t); otherwise it is at most -a/2. A union bound gives

    P(|X_t|>=a)<=6 exp[-min(a^2/(8t),a/2)].         (7)

Let r=|x|>=1. In the convolution p_t(x)=sum_z p_{t/2}(z)p_{t/2}(x-z), either |z|>=r/2 or |x-z|>=r/2. Equations (6)-(7) therefore imply

    p_t(x)<=12 min(1,(t/2)^(-3/2))
                   exp[-min(r^2/(16t),r/4)].       (8)

For 0<t<=r/4, integrate the bound 12 exp(-r/4). Its integral is 3r exp(-r/4), which is at most 48/r: the maximum of r^2 exp(-r/4) over positive reals is 64 exp(-2), and e>2.

For t>=r/4, enlarge the integration interval to (0,infinity) and use

    integral_0^infinity t^(-3/2) exp[-r^2/(16t)] dt
       =4sqrt(pi)/r.

The substitution v=r/(4sqrt(t)) gives this identity directly. Thus the second integral in (8) is at most

    12*2^(3/2)*4sqrt(pi)/r <384/r,

using 2^(3/2)<4 and sqrt(pi)<2. We have G(x)<432/r<=864/(1+r) for integer r>=1. Together with G(0)<=3, this proves (5).

## 3. Sparse labels bound the potential

Fix z in Z^3 and put d_i=|x_i-z|. The triangle inequality and the displacement hypothesis imply

    sum_y mu_i(y)/(1+|y-z|)
       <= 1/[1+max(d_i-R,0)].                      (9)

The mass bound at most one is used here. The right side has the integral representation

    1/[1+max(d_i-R,0)]
       = integral_R^infinity 1_{d_i<=r}/(1+r-R)^2 dr.

This is the elementary antiderivative of (1+r-R)^(-2), beginning at max(R,d_i). Summing over the finite index set and using (1),

    sum_i 1/[1+max(d_i-R,0)]
       <= L integral_0^infinity (1+R+t)^alpha/(1+t)^2 dt
       <= L(1+R)^alpha integral_0^infinity (1+t)^(alpha-2)dt
       = L(1+R)^alpha/(1-alpha).                  (10)

The second inequality uses 1+R+t<=(1+R)(1+t) and alpha>=0; the last integral converges precisely for alpha<1. Equations (5), (9), and (10) give the uniform potential estimate

    sum_y G(z-y)g(y)
       <= [1000 L/(1-alpha)](1+R)^alpha.           (11)

No separation of the displaced endpoints is required.

## 4. Killed Green functions and finite-volume energy

For f supported on a finite Omega, expansion and grouping of the two orientations of each edge give

    sum_{x in Omega} f(x)A_Omega f(x)=D(f).         (12)

If D(f)=0 then f is equal at every pair of neighbors. The full lattice is connected and f vanishes off a finite set, so f=0. Thus A_Omega is a positive definite real symmetric matrix, hence invertible.

Let tau_Omega be the first exit time of X_t from Omega and let

    G_Omega(x,y)=integral_0^infinity
                  P_x(X_t=y, t<tau_Omega)dt.

The killed transition matrix is exp(-t A_Omega). This follows either from the finite forward equation, or from the Poisson jump construction restricted to paths staying in Omega. Positive definiteness gives exp(-t A_Omega)->0 and

    G_Omega=integral_0^infinity exp(-t A_Omega)dt
           =A_Omega^{-1}.

Dropping the condition t<tau_Omega gives

    0<=G_Omega(x,y)<=G(y-x).                       (13)

Consequently u_Omega is nonnegative, and (11)-(13) yield

    D(u_Omega)=sum_x g(x)u_Omega(x)
       <= [1000 L/(1-alpha)](1+R)^alpha sum_x g(x)
       <= [1000 L/(1-alpha)](1+R)^alpha m.

This proves (2), including m=0. If m>0, (1) at a label and r=0 forces L>=1, so no division by zero occurs in the later capacity bound.

## 5. A current to infinity and capacity

Take an increasing sequence of finite cubes Omega_n exhausting Z^3 and containing the supports of g. A path up to a fixed finite time visits finitely many sites almost surely, since its number of jumps is Poisson(6t). Thus the killed probabilities increase to the unrestricted probabilities. Monotone convergence gives, for each x,

    u_{Omega_n}(x) -> u(x):=sum_y G(y-x)g(y).

Define J(x,y)=u(x)-u(y) on adjacent vertices. For each fixed x, A_{Omega_n}u_{Omega_n}(x)=g(x) for all sufficiently large n. Passing through its six-term sum proves div J(x)=g(x). Applying Fatou's lemma to the countable sum of squared edge differences and using (2) proves (3).

This construction also gives unit currents for each individual injection site: apply it to g=delta_a to obtain J^a(x,y)=G(a-x)-G(a-y), of divergence delta_a. Since g is finitely supported, the aggregate current just constructed is exactly sum_a g(a)J^a, equivalently sum_i sum_a mu_i(a)J^a. Thus the estimate bounds an aggregate of unit currents, as well as a current specified only by its total divergence.

For capacity, take R=0, labels the distinct points of S, mu_i=delta_{x_i}, and hence g=1_S. Given any finitely supported f>=1 on S, choose Omega containing S and the support of f. The bilinear version of (12) and Cauchy-Schwarz on the edges give

    |S|^2 <= (sum_{x in S} f(x))^2
       = [sum_{edges {x,y}}(u_Omega(x)-u_Omega(y))(f(x)-f(y))]^2
       <= D(u_Omega)D(f)
       <= [1000 L/(1-alpha)] |S| D(f).

For nonempty S cancel |S| and take the infimum over f. This proves (4). For the empty set capacity is zero, and its lower bound is zero without division by L.

## 6. The power of the displacement cannot be reduced

Fix 0<alpha<1, put b=1/alpha>1, and for a large integer R put m=floor(R^alpha). Take labels

    x_j=(floor(j^b),0,0),  j=1,...,m.

They are distinct and |x_j|<=R. For integers j>=1 and k>=0,

    (j+k)^b-j^b>=k^b.

To verify this, the left side minus k^b is nondecreasing in j>=0, since its derivative in j is b[(j+k)^(b-1)-j^(b-1)]>=0, and its value at j=0 is zero. Therefore

    floor((j+k)^b)-floor(j^b)>=k^b-1.

If a ball of radius r contains n of the labels, its extreme labels have coordinate difference at most 2r, so (n-1)^b<=2r+1. Hence

    n<=1+(2r+1)^alpha
      <=(1+2^alpha)(1+r)^alpha<=3(1+r)^alpha.

Thus (1) holds uniformly in m and R with L=3. Set every mu_j=delta_0, so g=m delta_0, and let Omega contain 0 and all the labels. The Cauchy-Schwarz argument from (12), now tested against delta_0, gives

    m^2=[sum_x g(x)delta_0(x)]^2
       <=D(u_Omega)D(delta_0)=6D(u_Omega).

The factor six counts the six edges incident to zero, including any boundary edges. Consequently D(u_Omega)>=m^2/6. Since m/R^alpha tends to one, a proposed uniform replacement of (1+R)^alpha by (1+R)^beta with beta<alpha would give m/6<=C(1+R)^beta, which fails for large R. This proves the displacement assertion.

An independent normalization check is probabilistic: G_Omega(0,0)>=1/6, the expected initial holding time before the walk's first jump. Thus D(u_Omega)=m^2 G_Omega(0,0)>=m^2/6, reproducing the same lower bound.

## 7. Why alpha=1 is excluded

Take the m distinct labels x_j=(j,0,0), 1<=j<=m, with mu_j=delta_{x_j} and R=0. Every ball of radius r contains at most 2r+1 of them, so (1) holds with alpha=1 and L=2. Put g_m=sum_j delta_{x_j}.

For cubes Omega_n increasing to the full lattice, monotone convergence of killed kernels gives

    D(A_{Omega_n}^{-1}g_m) -> Q_m
       :=sum_{j,k=1}^m G((j-k,0,0)).               (14)

We prove Q_m>=m log(m)/(16pi^2) for m>=2. Define

    lambda(theta)=2 sum_{i=1}^3 (1-cos theta_i),
    F_m(theta_1)=sum_{j=1}^m exp(ij theta_1).

The same Poisson Fourier inversion used in Section 2, followed by integration in t, gives

    Q_m=(2pi)^(-3) integral_{[-pi,pi]^3}
               |F_m(theta_1)|^2/lambda(theta) dtheta.   (15)

For completeness, first sum p_t(x_j-x_k) over j,k. Its Fourier numerator is |F_m|^2 and is nonnegative, so Tonelli permits integration over t before theta. The integral of exp(-t lambda) is 1/lambda except at the single point theta=0, which has measure zero. Finiteness follows already from (5), or directly from lambda(theta)>=(4/pi^2)sum theta_i^2 and local integrability of |theta|_2^(-2) in three dimensions.

On |theta_1|<=1/m, each cos(j theta_1)>=1/2, since cos v>=1-v^2/2. Thus |F_m|^2>=(Re F_m)^2>=m^2/4. Restrict the other coordinates to the planar annulus

    1/m<=r:=sqrt(theta_2^2+theta_3^2)<=1.

It lies inside the integration cube. Since 2(1-cos v)<=v^2,

    lambda(theta)<=theta_1^2+r^2<=2r^2.

Integration of this lower bound for the integrand in (15) gives

    Q_m>=(2pi)^(-3) (m^2/4)(2/m)
                       integral_{1/m}^1 (2pi r)/(2r^2) dr
       =m log(m)/(16pi^2).                        (16)

Consequently the left side of (14), divided by m, is unbounded as m and then the containing cube grow. There is no finite universal constant C with D(A_Omega^{-1}g_m)<=C L m at alpha=1, even on the full lattice and with zero displacement. The same example satisfies (1) for any alpha>1.

This failure also applies to currents to infinity. If an antisymmetric current J has divergence g_m and finite energy, summation by parts against the finitely supported u_Omega gives

    D(u_Omega)=sum_x g_m(x)u_Omega(x)
       =sum_{edges {x,y}} J(x,y)(u_Omega(x)-u_Omega(y)).

Cauchy-Schwarz implies energy(J)>=D(u_Omega). Letting Omega increase and applying (16) gives energy(J)>=Q_m>=m log(m)/(16pi^2).

## 8. Independent checks

The sparse potential estimate can be checked by dyadic shells without its integral representation. Put T=1+R. Labels with 1+|x_i-z|<2T contribute at most L(2T)^alpha. For each k>=0, labels with

    2T 2^k<=1+|x_i-z|<4T 2^k

number at most L(4T 2^k)^alpha, and their denominators in (9) are at least T 2^k. Therefore the sum in (10) is at most

    L[2^alpha T^alpha+
      4^alpha T^(alpha-1)/(1-2^(alpha-1))].        (17)

This independently recovers the uniform displacement power T^alpha and the threshold alpha<1, with a worse constant. In the integral proof, the substitution v=1/(1+t) gives integral_0^1 v^(-alpha)dv=1/(1-alpha), checking that denominator a second way. For alpha=0 the growth condition forces m<=L by taking a ball containing every label; then the potential bound follows directly from G<=1000, independently of R.

There is a second geometric check on the logarithmic endpoint lower bound. In (15) instead restrict |theta_1|<=1/m, 1/m<=theta_2<=1, and |theta_3|<=theta_2. On this region lambda<=3theta_2^2 and |F_m|^2>=m^2/4. Integrating the rectangle in theta_1,theta_3 and then theta_2 gives

    Q_m>=(2pi)^(-3)(m^2/4)(2/m)
                     integral_{1/m}^1 2/(3theta_2) dtheta_2
       =m log(m)/(24pi^3).

This is a weaker lower bound from a different region and again rules out a linear bound at alpha=1. The coefficient in (16) also checks as (m/2)*pi/(8pi^3)=m/(16pi^2).

The energy normalization has two checks: grouping neighboring terms proves (12), while Fourier transformation gives the symbol lambda(theta)=sum_i |1-exp(i theta_i)|^2 for the same edge energy. In particular D(delta_0)=6, and rate one per neighbor has mean first holding time 1/6. There is no hidden factor of two from oriented edges.

The Green estimate's arithmetic can also be retained before rounding: for r>=1 the two time intervals give

    G(x)<=[192 exp(-2)+96sqrt(2pi)]/r.

The first summand is less than 48 and the second less than 384. Thus 1000/(1+r) safely dominates it, including r=1; at r=0 use G(0)<=3. No numerical integration or fitted constant is used.

## 9. Relation to the remaining spatial input

The inspected source's [`regular_injection_energy`](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/Heisenberg/RegularKernels.lean) constructs currents on the complement of a finite set of removed sites, under regularity assumptions. It allows distributed endpoints within distance R of sparse labels, uses growth exponent 1/100, and bounds aggregated current energy by a constant times (1+R)^(1/100)|I|. Equations (2)-(3) prove the full-lattice special case in dimension three, for every exponent below one. The source counts graph darts; the present energy counts undirected edges, so its numerical constants are not identified with ours.

The dependency [`periodic_return_estimate`](https://raw.githubusercontent.com/openai/math/main/lean/OAI/MathematicalPhysics/Heisenberg/PeriodicReturnEstimate.lean) calls the leakage estimate; that estimate uses the routed spatial energy bound. The probabilistic regularity input in [`regularity_of_pin_induction`](https://raw.githubusercontent.com/openai/math/main/lean/OAI/MathematicalPhysics/Heisenberg/RegularPin.lean) concerns the random removed sites. None of the positivity comparisons above transfers the result to a lattice with removed sites: removing conductances can increase the required flow energy. The missing geometric step is to route currents around those sites with a uniform cost under the exact regularity hypothesis. The pinning bootstrap, its loop comparison, and the physical-spin and infinite-volume arguments remain unverified here. No claim of priority is made for these potential-theory estimates.

The source calls supplying that geometric step are [`regular_component_envelope`](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/Heisenberg/RegularComponents.lean) and [`connected_envelope`](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/Heisenberg/FlowCongestion.lean). Their statements and proof bodies were inspected to locate this dependency; they are not proved in this note.
