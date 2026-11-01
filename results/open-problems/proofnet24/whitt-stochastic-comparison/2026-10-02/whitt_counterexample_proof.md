# A candidate counterexample to Whitt's 1983 stochastic waiting-time conjecture

Status: exact rational certificate passes; independent mathematical and
source-status audits are still required before declaring this a new result.
This concerns the full stochastic-order conjecture, not its weaker mean
waiting-time version.

## Original claim

Ward Whitt, *Comparison conjectures about the M/G/s queue*, Operations
Research Letters **2** (1983), 203–209, doi:10.1016/0167-6377(83)90026-3,
Conjecture 1.1 states that increasing the iid service-time distribution
in increasing convex order increases the stationary FCFS waiting-time
distribution in usual stochastic order, for Poisson arrivals and fixed
homogeneous parallel servers.

Author-hosted primary PDF:
https://www.columbia.edu/~ww2040/comparisonConjectures1983.pdf

The original setting explicitly permits mass at zero: Section 6 studies
mixtures of an exponential distribution and a zero atom. Conjecture 1.1
does not assume strictly positive service times.

## The two service laws

Use two servers and Poisson arrivals of rate lambda0=11/10. Let E be an
independent exponential random variable of mean one. The base service S is

    S=E/5 with probability3/7;
    S=8E/5 with probability4/7.

The spread service T is

    T=0 with probability3/14;
    T=2E/5 with probability3/14;
    T=8E/5 with probability4/7.

Both means are one and the common traffic intensity is lambda0/2=11/20<1.
An explicit martingale coupling chooses the base class and E, leaves the
large class unchanged, and replaces E/5 in the small class by zero or
2E/5 with equal probabilities. Consequently E[T|S]=S and S<=cx T,
hence also S<=icx T.

We will certify

    P(W_S>0) > .39287,
    P(W_T>0) < .39172,
    P(W_S>0)-P(W_T>0) > .00115.

This is the opposite of the stochastic ordering asserted by Conjecture1.1.
It does not imply a decrease in mean waiting time; simulations find that
the mean wait increases under this spread, as one might expect.

## Removing zero work without removing tagged arrivals

For T, zero-service jobs have zero work but may experience a positive FCFS
wait. Remove them only from the workload process. Doing so preserves the
start times of all positive jobs: a zero job consumes no server time when
its turn arrives. A virtual arriving job has the same waiting time before
and after the removal. PASTA applies to **all original arrivals**, including
zero jobs, so their delay probability equals the stationary probability
that both servers are occupied by positive jobs in the thinned system.

The positive-job subsystem has Poisson rate

    lambda=(11/10)*(11/14)=121/140,

with small exponential mean2/5 chosen with conditional probability3/11
and large exponential mean8/5 chosen with probability8/11. The base
system's positive-job parameters are lambda=11/10, p=3/7, mu_s=5,
mu_l=5/8. The spread subsystem has lambda=121/140, p=3/11,
mu_s=5/2, mu_l=5/8.

## Three-phase queue representation

For either positive-job system, jobs are independent mixtures of two
exponentials. Sampling the exponential class when service begins yields
the same queue law as sampling it on arrival, since a job's own service
time is independent of its pre-service wait. With both servers busy,
record the number i in{0,1,2} serving the small class, and record q>=0
positive jobs waiting. With fewer than two busy servers, record an empty
state e, one small job s, or one large job l. These are the complete CTMC
states. In particular there are three phases at every q>=0 level.

For the three phases, put

    M=diag(lambda+i*mu_s+(2-i)*mu_l), i=0,1,2.

When q>=1, a completion reduces q by one and immediately chooses the
new service class. The downward-transition matrix B has entries

    B[i,i] = i*mu_s*p+(2-i)*mu_l*(1-p),
    B[i,i-1] = i*mu_s*(1-p), if i>0,
    B[i,i+1] = (2-i)*mu_l*p, if i<2.

The up-level matrix is lambda I and the within-level matrix is -M.
If a nonnegative matrix R with spectral radius<1 satisfies

    lambda I - R M + R^2 B=0,

then stationary row vectors v_q=v_0 R^q satisfy every interior-level
balance equation, because

    v_(q-1)*lambda I-v_q*M+v_(q+1)*B
      =v_0 R^(q-1)*(lambda I-RM+R^2B)=0.

Thus it suffices to find and certify the fixed point

    R=Phi(R):=(lambda I+R^2B)M^(-1).

## Rational enclosure of R

The verifier `whitt_qbd_exact.py` contains rational matrices L,U,W for
each of the two parameter choices. It checks exactly

    0<L<=U,
    L<=Phi(L), Phi(U)<=U,
    J_U(W):=(UW+WU)B M^(-1) < W,
    maximum row sum(U)<1.

The positive map Phi is monotone and maps the box[0,U] into itself.
For X,Y in this box, E=X-Y, the identity X^2-Y^2=XE+EY gives

    |Phi(X)-Phi(Y)| <= ||X-Y||_W * (UW+WU)B M^(-1),
    ||A||_W=max_(ij)|Aij|/Wij.

The checked inequality J_U(W)<W makes Phi a strict contraction of[0,U]
in this weighted norm. Banach's theorem gives a unique fixed point in
the box; iteration from the subsolution L increases toward it. Therefore

    L<=R<=U, rho(R)<=maximum row sum(U)<1.

Every assertion above uses exact Fraction arithmetic. The rational
enclosures are about10^-9 wide; no floating-point root is accepted
without these independent algebraic checks.

## Boundary stationary vector and normalization

Set the unnormalized empty-state mass to1. Let x be the row vector for
states(s,l,q0i0,q0i1,q0i2). In this ordering, the boundary equations for
these five states read

    x K_R=-b,
    b=(lambda p,lambda(1-p),0,0,0),

where the matrix K_R has upper two rows

    (-(lambda+mu_s),0,0,lambda(1-p),lambda p),
    (0,-(lambda+mu_l),lambda(1-p),lambda p,0),

and its lower-left3x2 block is

    [[0,2mu_l],[mu_l,mu_s],[2mu_s,0]],

while its lower-right3x3 block is -M+R B. Thus

    x=b(-K_R)^(-1).

The verifier checks that -K_U and -K_L are Z-matrices with positive
inverses, and computes both inverses exactly. Such matrices are
nonsingular M-matrices. Since

    -K_U <= -K_R <= -K_L,

their inverse ordering gives x_L<=x<=x_U. This use of inverse monotonicity
can also be proved directly: take v=(-K_U)^(-1)1>0. Each intermediate
Z-matrix A satisfies Av>=1, so diagonal scaling by v makes A strictly
row diagonally dominant and its inverse nonnegative. The identity
A^(-1)-B^(-1)=A^(-1)(B-A)B^(-1) then establishes the inverse bounds.

Define unnormalized busy and idle masses

    H=x_busy*(I-R)^(-1)*1,
    A=1+x_s+x_l.

The interior and boundary balance equations hold by construction.
The omitted empty-state equation follows by summing all other equations:
the generator has zero row sums, transition rates are bounded, and the
geometric stationary series is summable. Therefore the constructed
normalized positive measure is a stationary distribution. The chain is
irreducible, so this is the queue's unique stationary law.

The delay probability is H/(A+H). Positivity and monotonicity give

    H_L<=H<=H_U, A_L<=A<=A_U,
    H_L/(A_U+H_L) <= P(delay) <= H_U/(A_L+H_U).

## Certified results

All decisive inequalities below are exact rational assertions; decimals
only display the rational bounds.

    Base delay lower  .3928726168122538515345628736619...
    Base delay upper  .3928726219432107714003844437179...
    Spread delay lower .3917098123314243741403404296907...
    Spread delay upper .3917098158911753482853962814961...

The rigorous lower bound on the difference is

    .00116280092107850324916659216584... >23/20000=.00115.

Thus the conjectured stochastic ordering fails.

## An explicit positive threshold also violates the order

This is not solely a comparison at zero. In the base queue, whenever an
arrival waits, its wait can end within h only if one of the currently busy
servers completes within h. The combined completion rate is at most10.
Hence P(0<W_S<=h)<=10h. Consequently, at h=1/100000,

    P(W_S>h)-P(W_T>h)
       >=P(W_S>0)-10h-P(W_T>0)
       >.00115-.00010=.00105.

This supplies an explicit strictly positive tail threshold for the
failure of usual stochastic order.
