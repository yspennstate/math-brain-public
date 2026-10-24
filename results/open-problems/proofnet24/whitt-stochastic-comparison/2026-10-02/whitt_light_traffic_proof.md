# An analytic family of counterexamples to stochastic waiting-time monotonicity

This note supplies a purely analytic small-arrival-rate proof, independent
of the explicit numerical root enclosures. Priority and the present
literature status of Whitt's 1983 conjecture still require independent
checking. The mathematical result refutes the precise stochastic-order
assertion of Conjecture1.1, while respecting its weaker mean-order versions.

## The light-traffic formula

Consider a stationary M/G/2 FCFS queue with Poisson rate lambda and a
finite hyperexponential service law

    S=a_i E with probability p_i, i=1,...,k,
    a_i>0, p_i>0, sum_i p_i=1, E~Exp(1).

Set m=sum_i p_i a_i. Let A,B,C be independent random variables with the
size-biased mixing law

    P(A=a_i)=p_i a_i/m.

Then, as lambda decreases tozero,

    P(W_S>0)=m^2 lambda^2/2 + (K-m^3/2)lambda^3+O(lambda^4),
    K=m^3 E[A^2/((A+B)(A+C))].                         (1)

All parameters are fixed in this asymptotic statement.

## Analyticity and the infinite-queue remainder

The queue has a finite set of busy-server phases: unordered pairs of
exponential service classes. When both servers are busy, recording the
number q of waiting customers produces a finite-phase homogeneous QBD.
The queued service classes can be sampled at their service-start times,
since they are iid and independent of the pre-service waiting time.

Let M0 be diagonal with the total completion rates in each busy phase,
and let D be the downward-level transition matrix: after a completion,
one immediately starts a new iid service class. Interior balance is

    lambda I-R(M0+lambda I)+R^2D=0,
    R=Phi(lambda,R)=(lambda I+R^2D)(M0+lambda I)^(-1).

At(lambda,R)=(0,0), Phi is analytic and its derivative with respect to R
iszero. The analytic implicit-function theorem therefore yields an
analytic branch R(lambda)=O(lambda). For small nonnegative lambda, Phi
is a positive contraction on an O(lambda) box; monotone iteration from
zero shows that this branch is nonnegative and supplies the stationary
rate matrix. Its norm is less thanone for small lambda.

The boundary equations for empty, one-busy and two-busy states have an
invertible pure-death nonempty block at lambda=0. Fixing empty mass1
therefore gives analytic boundary masses. One-busy mass is O(lambda)
and two-busy mass is O(lambda^2); the latter follows by expanding the
boundary equations to first order, since arrivals from empty lead only
to one-busy states. Thus the stationary masses at queue levels q are
O(lambda^(q+2)). The exact mass at q>=2 is an analytic expression

    v_0 R^2(I-R)^(-1)1=O(lambda^4),

up to the analytic normalizing factor.

It follows rigorously that the delay expansion through cubic order can
be calculated in the finite queue with maximum total population3.
To see this without an informal truncation argument, restrict the
infinite stationary row to populations0,...,3. Its residual in the
capacity3 balance equations is a boundary vector of the form

    lambda*pi_3-pi_4*D=O(lambda^4),

and its total mass is1+O(lambda^4). The finite chain's augmented
stationary linear system is invertible at lambda=0: the pure-death chain
has empty as its unique closed class. Its inverse is consequently
analytic and bounded nearzero. The restricted infinite stationary row
and the capacity3 stationary row differ by O(lambda^4). This proves
the claimed remainder order in(1) for the genuine infinite queue.

## Derivation of the cubic coefficient

Write u_i=p_i a_i. The leading stationary one-busy probabilities are
lambda*u_i. Conservation of the long-run workload of each service class
gives the exact identity

    E[number of class-i servers busy]=lambda*p_i*a_i.

The leading two-busy phase masses are lambda^2*tau, where for unordered
pairs(i,j),

    tau_(ii)=u_i^2/2,
    tau_(ij)=u_i*u_j, i<j.

Their total is m^2/2. The expected number of busy class-i servers in
these leading masses is lambda^2*u_i*m, so the second-order one-busy
probability coefficient is -m*u_i.

Let M0 be the phase completion-rate diagonal above. The first nonzero
three-customer probability row is lambda^3*tau*M0^(-1). Expanding the
two-busy balance equations gives its cubic row as

    -m*tau - tau*M0^(-1) + tau*M0^(-1)*D*M0^(-1).

Adding the three-customer row cancels the middle term. Therefore the
cubic coefficient of the delay probability is

    -m*tau*1 + tau*M0^(-1)*D*M0^(-1)*1
    =-m^3/2+K.                                          (2)

The term K has a useful direct interpretation. At a rare arrival finding
two busy servers, after the first completion the surviving old job and
the new job share the two servers until the next completion. For an
old residual pair of exponential means a,b, the survivor has mean a
with probability a/(a+b), and mean b with probability b/(a+b). For a
new mean c, the mean time until either the survivor or new job completes
is ac/(a+c) or bc/(b+c), respectively. The leading old pair weights
are m^2/2 times the law of two independent size-biased means A,B.
Consequently

    K=(m^2/2) E_{A,B size-biased; C original}[
        A/(A+B) * AC/(A+C) + B/(A+B) * BC/(B+C)]
     =m^2 E_{A,B size-biased; C original}[
        A^2 C/((A+B)(A+C))]
     =m^3 E_{A,B,C size-biased}[
        A^2/((A+B)(A+C))],

which proves(1).

## Strict comparison with an exponential queue

Exchangeability of A,B,C yields

    K/m^3=(1/3) E[
       A^2/((A+B)(A+C))+
       B^2/((A+B)(B+C))+
       C^2/((A+C)(B+C))]
      =(1/3) E[1-2ABC/((A+B)(A+C)(B+C))].               (3)

The arithmetic-geometric mean inequality gives

    (A+B)(A+C)(B+C)>=8ABC.

Hence K>=m^3/4, with strict inequality whenever the mixing means are
not all equal. Define the strictly positive excess

    Delta=K-m^3/4>0.

An M/M/2 queue whose offered load is lambda*m has

    P(delay)=(lambda*m)^2/(2+lambda*m)
            =m^2 lambda^2/2-m^3 lambda^3/4+O(lambda^4).

Thus every nondegenerate finite hyperexponential service law has a
strictly *larger* probability of delay than this mean-matched exponential
benchmark for all sufficiently small positive arrival rates.

## A whole class of convex-order counterexamples

Let Bmax=max_i a_i, and assume the mixing means are nondegenerate.
Then Bmax>m. Construct a new service T by retaining the same E and,
conditional on class i, replacing the coefficient a_i byzero or Bmax
with probabilities1-a_i/Bmax and a_i/Bmax. The replacement has conditional
mean a_i, so E[T|S]=S and S<=cx T. Its unconditional law is

    T=0 with probability1-m/Bmax,
    T=Bmax*E with probabilitym/Bmax.

Deleting zero jobs only from the workload process gives an M/M/2 queue
with positive-job arrival rate lambda*m/Bmax and service rate1/Bmax.
All original arrivals see its virtual waiting by PASTA; zero jobs may
wait even though they contribute no work. Its delay probability is
exactly(lambda*m)^2/(2+lambda*m). Equation(3) therefore gives

    P(W_S>0)-P(W_T>0)=Delta*lambda^3+O(lambda^4)>0

for every sufficiently small positive lambda. This violates Whitt's
stochastic-order Conjecture1.1 for every nondegenerate finite
hyperexponential starting law.

## Counterexamples with strictly positive service times

The zero atom is unnecessary. Choose0<epsilon<min_i a_i and replace
the coefficient a_i conditionally by epsilon or Bmax, with probabilities

    (Bmax-a_i)/(Bmax-epsilon), (a_i-epsilon)/(Bmax-epsilon).

The conditional mean remains a_i, so the resulting two-exponential law
T_epsilon satisfies S<=cx T_epsilon and is strictly positive almostsurely.
Its unconditional small probability is(Bmax-m)/(Bmax-epsilon). The
two-component formula below gives cubic excess

    Delta_epsilon=
      epsilon*Bmax*m*(Bmax-m)*(m-epsilon)/[4(Bmax+epsilon)^2]
      <=epsilon*m^2*(Bmax-m)/(4Bmax).

Thus, for example, choosing

    epsilon=min{(min_i a_i)/2,
                Bmax*Delta/[m^2*(Bmax-m)]}

ensures0<epsilon<min_i a_i and Delta_epsilon<=Delta/4. It follows that

    P(W_S>0)-P(W_T_epsilon>0)
      =(Delta-Delta_epsilon)lambda^3+O(lambda^4)>0

for all sufficiently small positive lambda. Both service distributions
are finite exponential mixtures with smooth strictly positive densities
on the positive half-line. If the original means and probabilities are
rational, the displayed epsilon and the target mixing law are rational.

## Closed two-component formula

For a two-component law with means a,b and probabilities p,q,
set A0=pa, B0=qb, m=A0+B0, and z=a/(a+b). The four terms in K group as

    K=(A0^2/2+A0*B0*z)*(A0/2+B0*z)
      +(B0^2/2+A0*B0*(1-z))*(A0*(1-z)+B0/2)
      =(A0^3+B0^3)/4+A0*B0*m*(1-z+z^2)
      =m^3/4+A0*B0*m*(z-1/2)^2.

Therefore

    Delta=p*q*a*b*m*(a-b)^2/[4(a+b)^2].                 (4)

For the concrete base law a=1/5,b=8/5,p=3/7,q=4/7,m=1,

    Delta=8/675,
    P(W_S>0)=lambda^2/2-(643/2700)lambda^3+O(lambda^4).

For the strictly positive target with a=1/1000,b=8/5,p=200/533,

    P(W_T>0)=lambda^2/2-(64056049/256320100)lambda^3+O(lambda^4),
    P(W_S>0)-P(W_T>0)
       =(4068754/346032135)lambda^3+O(lambda^4)>0.

The independent exact coefficient verifier is `whitt_light_traffic.py`.
