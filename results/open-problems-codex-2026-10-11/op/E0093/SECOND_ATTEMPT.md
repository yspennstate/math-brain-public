# Second serious attempt at E0093 — 2026-10-12

## Gap reread and two approaches not used in the first attempt

The first attempt did not obtain sharp typical rates for sparse random
generators on arbitrary groups, even after making the walk lazy and
conditioning on generation. Its concentration argument requires k of
order log|G|. I considered the following two new approaches.

**A. Normal-subgroup averaging and rapid equilibration within fibers.**
Average over a normal subgroup N, separate the quotient walk from the
orthogonal complement, and use short commutator words to force a spectral
gap in that complement. Test this on a genuinely nonabelian, nonnilpotent
sparse-generator family, S_3 x C_p with two random generators. A complete
quotient comparison may then turn elementary random Fourier estimates
into a sharp typical order of mixing for this family.

**B. Random-word collisions in quasirandom groups.** Expand the averaged
return probability as a sum over pairs of words and try to use a large
minimum nontrivial representation degree to bound nontrivial word-map
fibers. This would target alternating groups or unbounded-rank simple
groups directly, rather than an extension with a bounded normal subgroup.
The obstacle is that representation degree alone controls convolution of
independent measures, whereas here every occurrence of a generator is
the same sampled element; words with repeated letters and short relations
can retain large correlations. A proof would need a uniform word-map
estimate, not just the standard quasirandom convolution inequality.

I pursue A. It offers concrete algebra, exact finite checks, and a possible
full mixing-scale result for random **pairs**, outside the nilpotent setting.
This does not replace the arbitrary-group source question by a special case.

## Gap-specific math-store recall

`math_recall.py "random Cayley sparse generators mixing nilpotent quotient
abelianization Hermon Huang Hildebrand"` returned mostly sparse-Ising cards,
which are off target and were not used. A more focused normal-subgroup query
is recorded in LITERATURE.md and in the saved recall output. All brain
material is treated as a hint, not as verified mathematics.

## Model to investigate

For a prime p>3 let G_p=S_3 x C_p. Sample g_1,g_2 independently uniformly
and condition on <g_1,g_2>=G_p. Retain multiplicities and take the lazy
symmetric walk

    Q=(1/2)I+(1/8)(R_g1+R_g1^-1+R_g2+R_g2^-1).

Potential endpoint: for fixed epsilon, a deterministic lower bound of
order p and a tight upper tail for t_mix(epsilon)/p. A tight random order
is weaker than concentration at a fixed deterministic multiple of p.
The latter must not be claimed from a first-moment bound.

## Theorem 5: deterministic normal-subgroup reduction

Let G have order n, N be a nontrivial normal subgroup, and q=|G/N|.
Take k fixed generators and the symmetric half-lazy Q from ATTEMPT.md.
Suppose every h in N is a word of length at most D>=1 in these generators
and their inverses. Let d_G(t) and d_A(t) be the identity-start TV distances
on G and A=G/N. For every integer t>=0,

    d_A(t) <= d_G(t) <= d_A(t)
                +(sqrt(n-q)/2)(1-1/(2kD^2))^t.              (8)

This is a general reduction, not a claim of a sharp arbitrary-group rate.
The concept is already in Hermon–Huang, Lemma 3.2 (continuous time);
here the constants and the half-lazy discrete-time proof are supplied directly.

### Complete proof

Use the uniform-weighted complex L2 inner product. Define
Pi f(x)=|N|^-1 sum_{h in N} f(xh). Averaging twice equals averaging once;
inverse symmetry makes Pi self-adjoint. Thus Pi is the orthogonal
projection onto functions constant on cosets xN. Normality makes
R_g Pi=Pi R_g: conjugating N by g just permutes the terms in the average.
Consequently Q preserves the image and kernel of Pi.

For every f, averaging the identity
||f-R_h f||_2^2=2||f||_2^2-2 Re<f,R_h f> gives

    ||f-Pi f||_2^2=(1/(2|N|))sum_{h in N}||f-R_h f||_2^2.

If h=s_1...s_l, l<=D, telescope I-R_h into
sum_{j=1}^l R_{s_1...s_{j-1}}(I-R_{s_j}). All prefix translations are
unitary. Cauchy–Schwarz gives

    ||f-R_h f||_2^2 <= l sum_j ||f-R_{s_j}f||_2^2
                    <= D^2 sum_{i=1}^k||f-R_gi f||_2^2.

For an inverse generator the squared difference norm is the same as for
the generator. A word can repeat an index up to D times, explaining the
last D^2 and avoiding any assumed congestion bound. Meanwhile

    <f,(I-Q)f>=(1/(4k))sum_i||f-R_gi f||_2^2.

Combining these formulas, on ker Pi we have
||f||_2^2 <= 2kD^2 <f,(I-Q)f>. Q is self-adjoint with eigenvalues in
[0,1], because it is half the identity plus half a self-adjoint Markov
contraction. Applying the preceding inequality to each eigenvector in
ker Pi bounds every such eigenvalue by 1-1/(2kD^2). Thus the norm of Q^t
on ker Pi is at most this number to the power t. This spectral step
does not equate a Dirichlet form to a norm deficit for arbitrary f.

The initial density is f_0=n 1_{e}. Its projected density is q 1_N,
the density of the uniform law on N. The squared L2 norm of their
difference is n-q, by direct summation over N and its complement.
Reversibility evolves densities by Q^t. Therefore their evolved laws
differ in TV by at most (sqrt(n-q)/2)(1-1/(2kD^2))^t.

The evolution started uniformly on N remains constant on quotient
fibers and projects to the identity-start walk on A. Its TV distance
to uniform on G is exactly d_A(t), since summing a constant signed
density over each fiber multiplies by the fiber size. The triangle
inequality proves the upper bound in (8). Projection can only decrease
TV: the inverse image of any quotient event is an event in G. This
proves the lower bound and completes the proof.

## Theorem 6: explicit quotient approximation for every generating pair

For every prime p>3 and every generating pair of G_p=S_3 x C_p, put
N=A_3 x {0}, A=G_p/N=C_2 x C_p, and

    rho=1/2+sqrt(3)/4 < 1.

Then for all integer t>=0,

    0 <= d_G(t)-d_A(t) <= sqrt(p) rho^t.                    (9)

In particular quotient profiles uniformly approximate group profiles on
every time range t>=eta p, eta>0, as p tends to infinity.

### Generation and a first fiber bound

Write g_i=(h_i,a_i). The pair generates G_p iff h_1,h_2 generate S_3
and (a_1,a_2)!=(0,0). Necessity is projection. For sufficiency, the
subgroup K generated by the pair contains an element (h,a) with a!=0.
Because h^6=e, its sixth power is (e,6a), which generates {e} x C_p
since p>3. Surjectivity of K onto S_3 then gives every (h,0) by
subtracting the cyclic coordinate. Hence K=G_p.

The generating S_3 pairs are precisely two different transpositions,
or one transposition and one 3-cycle, in either order. Two distinct
transpositions have product a 3-cycle and generate S_3. A transposition
and a 3-cycle do also. Every other possibility generates a proper
subgroup: an identity adds nothing, two 3-cycles stay in A_3, and a
repeated transposition generates order two. There are 6 pairs of the
first kind and 12 of the second, for 18 out of 36 total pairs.

For either kind the commutator is a nonidentity element of A_3:
for distinct transpositions [s,t]=(st)^2; for a transposition s and
a 3-cycle r, srs=r^-1 gives [s,r]=r^-2=r. The cyclic components cancel.
This commutator and its inverse are the two nonidentity elements of N,
and each is a word of length 4. Thus D<=4 and (8) already gives the
valid, weaker error sqrt(p)(63/64)^t.

### Complete improvement to rho

Fourier transform the cyclic factor. At frequency j the right translation
by (h,a) is e^(2pi i ja/p)R_h on functions on S_3. Write S_3=<r,s> with
r^3=s^2=e and srs=r^-1. Every element is uniquely r^l s^epsilon,
l=0,1,2 and epsilon=0,1. Let omega=e^(2pi i/3). For u=0,1,2,
functions of the form f(r^l s^epsilon)=omega^(ul)v_epsilon form an
orthogonal two-dimensional subspace. Orthogonality follows by summing
the powers of omega over l. These three spaces exhaust dimension 6.
On the u-space, right multiplication by r and s acts on the vector v as

    R=diag(omega^u,omega^-u),  T=[[0,1],[1,0]].

Indeed multiplication by r replaces l by l+(-1)^epsilon and multiplication
by s switches epsilon. The u=0 space is exactly the image of averaging
over A_3. Thus only u=1,2 are in the fiber complement.

On each such space, any transposition is a Hermitian involution with
trace zero. For two distinct transpositions T,U, TU+UT=-I: their product
is a nontrivial 3-cycle whose eigenvalues are omega,omega^-1, and its
inverse has reversed eigenvalues; their sum is -I. If their cyclic
phases are alpha,beta, their Q block is

    (1/2)I+(1/4)(xT+yU),  x=cos alpha, y=cos beta.

Its eigenvalues are 1/2 +/- (1/4)sqrt(x^2+y^2-xy), because
(xT+yU)^2=(x^2+y^2-xy)I and its trace is zero. For |x|,|y|<=1,
x^2+y^2-xy<=3. Hence its largest eigenvalue is at most rho.

For a transposition and a 3-cycle (the order of the pair is irrelevant),
conjugate so the cycle matrix is R=-I/2+i(sqrt(3)/2)Z, where Z is a
Hermitian involution with trace zero. The transposition matrix T
anticommutes with Z, as it swaps the two cycle eigenspaces. The Q block is

    (1/2-cos beta/8)I+(cos alpha/4)T-(sqrt(3)sin beta/8)Z.

Its largest eigenvalue is

    1/2-cos beta/8+(1/8)sqrt(4cos^2 alpha+3sin^2 beta)
    <=1/2+(1/8)[-x+sqrt(7-3x^2)], x=cos beta.

Weighted Cauchy–Schwarz bounds the bracket by sqrt(28/3): write
y=sqrt(7-3x^2), so 3x^2+y^2=7 and
(-x+y)^2 <= (1/3+1)(3x^2+y^2)=28/3.
The bracket is nonnegative; hence the largest eigenvalue is at most
1/2+sqrt(21)/12 < rho (since 21/144<3/16).
All block eigenvalues are nonnegative by half-laziness. Thus the norm
of Q^t on the entire fiber complement is at most rho^t. The density
argument in (8), with n-q=6p-2p=4p, proves (9).
For t>=eta p its error is at most sqrt(p)rho^(eta p), tending to zero.

## Theorem 7: sharp typical order for random pairs on S_3 x C_p

Under the conditioned sampling model above, for each fixed epsilon in
(0,1), t_mix(epsilon) has order p **in probability**, in this precise sense:

1. Every generating pair obeys

       t_mix(epsilon) >= ((1-epsilon)/4)
               (sqrt(p(1-epsilon))-1)_+^2.                 (10)

2. Define for integer t>=1

       B_p(t)=[4^-t+2(p-1)(1/p+sqrt(pi)/(2sqrt(t)))^2]
                    /(1-p^-2),
       e_p(t)=sqrt(p)rho^t.

   Whenever e_p(t)<epsilon,

       Pr(t_mix(epsilon)>t | generation)
           <= B_p(t)/[4(epsilon-e_p(t))^2].                (11)

3. For every fixed u>0,

       limsup_{p->infinity} Pr(t_mix(epsilon)>ceil(up) | generation)
                    <= pi/(8u epsilon^2).                 (12)

Thus the normalized mixing times are tight and uniformly bounded away
from zero asymptotically. This gives a typical scale, not a deterministic
constant, a limit law, cutoff, or a full answer for arbitrary G.

### Complete proof of (10)

Project to A=C_2 x C_p, an Abelian group of order 2p. The walk can be
written W_1(t)gbar_1+W_2(t)gbar_2, where at each step either counter
changes by +1 or -1 (each of these four changes has probability 1/8),
or both stay put (probability 1/2). Each counter has mean zero and
variance t/4. These variance claims use independence across time only;
the two counters need not be independent of one another.

Set eta=(1-epsilon)/2 and, when t>0, L=sqrt(t/(2eta)). A union bound
and Chebyshev give Pr(max_i|W_i(t)|>L)<=eta. The image of the box
[-floor L,floor L]^2 in A therefore has walk mass at least 1-eta and
cardinality at most (2floor L+1)^2 <= (2L+1)^2. The uniform mass of
this image is at most (2L+1)^2/(2p). Consequently

    d_A(t)>=1-eta-(2L+1)^2/(2p).

At a time with d_G(t)<=epsilon, projection gives d_A(t)<=epsilon,
forcing (2L+1)^2>=2p(1-eta-epsilon)=p(1-epsilon).
Solving gives t>=eta/2 (sqrt(p(1-epsilon))-1)_+^2, which is (10).
If t=0 and the right side is positive, then p(1-epsilon)>1 and
d_A(0)=1-1/(2p)>epsilon, so such a mixing time cannot be zero.
This handles the t=0 boundary separately.

### Complete proof of the Fourier first-moment upper bound

Conditioning on generation splits into independent conditions on the
S_3 coordinates and the cyclic coordinates, by the generation criterion
in Theorem 6. The former selects 18 generating pairs. The latter is
uniform on (a,b) in F_p^2 minus {(0,0)}. In particular there is no
unjustified independence assumption *after* conditioning on (a,b)!=(0,0).

Fix a generating S_3 pair and let epsilon_i in {0,1} be its signs in
S_3/A_3. At least one epsilon_i is 1. The quotient characters are

    chi_{v,j}(epsilon,a)=(-1)^(v epsilon)exp(2pi i ja/p),
    v=0,1, j=0,...,p-1.

They are an orthonormal basis under uniform measure by the binary sum
and the cyclic geometric sum. Their Q eigenvalues are

    lambda_{v,j}=1/2+(1/4)[(-1)^(v epsilon_1)cos(2pi ja/p)
                           +(-1)^(v epsilon_2)cos(2pi jb/p)].

They lie in [0,1]. The nontrivial j=0 character has eigenvalue 0 if both
signs are odd and 1/2 otherwise, so its 2t power is at most 4^-t.
For j!=0, first use unconditioned independent uniform a,b in F_p;
multiplication by j preserves that distribution. For s_1,s_2 in {+1,-1},
1-z<=exp(-z) for z>=0 gives

    lambda_{v,j}^{2t} <= exp(-2t(1-lambda_{v,j}))
      = product_{i=1}^2 exp(-(t/2)(1-s_i cos theta_i)).

This remains valid at lambda=0 for t>=1. It therefore suffices to bound

    F_{p,s}(t)=p^-1 sum_{a=0}^{p-1}
                    exp(-(t/2)(1-s cos(2pi a/p))).

For s=+1 measure a/p from the nearest integer; for s=-1 measure a/p-1/2
from the nearest integer. In either case this is a shifted grid of
spacing 1/p, represented in [-1/2,1/2], and
1-cos(2pi x)=2sin^2(pi x)>=8x^2 there, by concavity of sine.
Consequently each summand is at most exp(-4t x^2).

For completeness, a Gaussian grid sum of spacing h is at most
1+h^-1 integral_R exp(-4t x^2)dx. Choose the grid point x_0 closest to
zero and remove its term, which is at most 1. For every point to its
left, the interval from that point to its next right neighbor has
Gaussian values at least the value at the left point; this follows
from monotonicity, and also for the last interval since |x_0| is
minimal. Apply the analogous argument to every point to the right
using its left interval. These intervals have length h, are disjoint
apart from endpoints, and cover the real line. Integrating proves
the grid bound. The finite circular grid is a subset of such an
infinite shifted grid, so the bound applies to it as well.
The Gaussian integral is sqrt(pi)/(2sqrt(t)). Hence

    F_{p,s}(t)<=1/p+sqrt(pi)/(2sqrt(t)).

Independence of unconditioned a,b now gives
E[lambda_{v,j}^{2t}] <= (1/p+sqrt(pi)/(2sqrt(t)))^2 for j!=0,
uniformly in the fixed sign pattern. Conditioning on (a,b)!=(0,0)
can increase the expectation of a nonnegative quantity by at most
(1-p^-2)^-1. There are 2(p-1) characters with j!=0. Therefore

    E[sum_{(v,j)!=(0,0)}lambda_{v,j}^{2t} | generation]<=B_p(t).

Fourier expansion of the initial density and orthogonality identify
this sum with the squared L2 norm of the quotient density minus one.
Cauchy–Schwarz gives E[d_A(t)^2 | generation]<=B_p(t)/4.
By (9), d_G(t)>epsilon implies d_A(t)>epsilon-e_p(t).
Markov's inequality applied to d_A(t)^2 proves (11).
TV contracts under every Markov step, so t_mix>t is equivalent to
d_G(t)>epsilon at integer t; no assumption about oscillatory distances
is made. Finally t=ceil(up) gives e_p(t)->0 and

    B_p(t)->pi/(2u),

because the square's leading term is pi/(4t), the other terms after
multiplication by 2(p-1) are O(t^-1/2)+O(p^-1), and 4^-t tends to zero.
This proves (12). Together with (10), whose right side divided by p
tends to (1-epsilon)^2/4>0, it proves the typical-order assertion.

## Theorem 8: no deterministic cutoff time in probability for this model

For random generating pairs on S_3 x C_p, there is no deterministic
sequence t_p with the property that for every fixed delta in (0,1),

    d_G(floor((1-delta)t_p)) -> 1,
    d_G(ceil((1+delta)t_p)) -> 0

in probability over the pair as p tends to infinity. This assertion
specifies the cutoff convention; it does not assert a theorem about all
possible definitions involving random, environment-dependent centers.

The same conclusion holds for environment-dependent random centers under
the identical two convergence-in-probability requirements; a full extension
argument is given after the deterministic-center proof.

### Complete proof

Put B=floor(sqrt(p-1)). Partition [0,1)^2 into B^2 half-open squares
of side 1/B. The p points (ja/p mod 1,jb/p mod 1), j=0,...,p-1, fall
in fewer than p squares. Two points share a square. Their distinct
indices differ by a nonzero m modulo p, and the circular distances
of ma/p and mb/p from integers are each less than 1/B. Therefore
the quotient character with v=0,j=m has eigenvalue

    lambda=1/2+(1/4)(cos(2pi ma/p)+cos(2pi mb/p)),
    1-lambda <= pi^2/B^2.                                  (13)

Here 1-cos x<=x^2/2 bounds each of the two terms by 2pi^2/B^2.
The eigenvalue is strictly below 1: both phases could be zero only if
a=b=0, excluded by generation. It is nonnegative by laziness. The
real part of this nontrivial character has uniform expectation zero,
supremum norm at most one, and expectation lambda^t from the identity.
Its pullback to G has the same properties. Hence

    d_G(t)>=lambda^t/2
          >=(1/2)(1-pi^2/B^2)^t                            (14)

for all sufficiently large p, when the base in the second bound is
positive. The character m can depend on the generator pair; the lower
bound is nevertheless uniform over every pair. In particular the
relaxation time is at least B^2/pi^2, of order p.

Suppose a deterministic cutoff time t_p existed. Applying its definition
at any fixed delta would put t_mix(1/4) between (1-delta)t_p and
(1+delta)t_p with probability tending to one (rounding has no effect).
The lower bound (10) shows t_p must diverge. The tightness in (12)
forces limsup t_p/p<infinity: if that ratio were unbounded, pass to
a subsequence with t_p/p tending to infinity; the lower cutoff inequality
would then force t_mix(1/4)/p to tend to infinity in probability along
that subsequence, contradicting tightness.

Thus there is a finite C>0 with t_p<=Cp for all sufficiently large p.
At t=ceil(3t_p/2), (14) gives

    d_G(t)>=(1/2)(1-pi^2/B^2)^(3Cp/2+1).

As B^2/p->1, the right side tends to (1/2)exp(-3Cpi^2/2)>0.
This deterministic positive lower bound contradicts the post-cutoff
requirement with delta=1/2. The contradiction proves the theorem.

For the claimed extension, let tau_p be a random center with the two cutoff
requirements. At delta=1/2, the pre-cutoff requirement implies
t_mix(1/4)>floor(tau_p/2) with probability tending to one. Hence
tau_p<=2t_mix(1/4)+2 with probability tending to one. By Theorem 7,
tau_p/p is tight. Choose a finite C so that tau_p<=Cp has probability
at least 3/4 for all sufficiently large p. On this event, the uniform
bound (14) at ceil(3tau_p/2) gives a positive lower bound converging to
(1/2)exp(-3Cpi^2/2). Thus the post-cutoff distances are bounded away
from zero with probability at least 3/4, contrary to their convergence
to zero in probability. This rules out random centers under precisely
the stated convention as well.

## An explicit exceptional pair: the order-p bound cannot hold for all pairs

Choose two different transpositions h_1,h_2 and set g_1=(h_1,1),
g_2=(h_2,1). This pair generates S_3 x C_p by Theorem 6. Projection
to C_p gives exactly the half-lazy nearest-neighbor cycle walk, since
both forward generators add 1 and both inverses add -1. By Theorem 4
of ATTEMPT.md its mixing time at threshold 1/4 is at least
(log 2)p^2/(2pi^2) for p>=5. Projection transfers this lower bound to G.
Thus a deterministic O(p) bound for **every** generating pair is false.
This does not contradict Theorem 7: the specified cyclic pair has a
probability tending to zero in the conditioned random model. For example
the event a=b!=0 has probability (p-1)/(p^2-1)=1/(p+1).

## Theorem 9: worst-case order for this family

Over **all** generating pairs on S_3 x C_p, the largest mixing time at
any fixed threshold epsilon in (0,1/2) has order p^2.

Here is a complete upper-bound argument, complementing the exceptional
pair's lower bound. In the quotient C_2 x C_p write the pair as
(epsilon_1,a),(epsilon_2,b). If either generator has odd binary coordinate
and nonzero cyclic coordinate, it alone generates the quotient of order
2p. Write Q_i for the half-lazy walk on that single generator. The
two-generator Q is (Q_1+Q_2)/2. On a nontrivial quotient character its
eigenvalue is (lambda_1+lambda_2)/2, with 0<=lambda_i<=1, and hence

    lambda^{2t}<=exp(-t(1-lambda_1)).

Since the first generator is a quotient generator, its character phases
range over the 2p roots and lambda_1=cos^2(pi j/(2p)). With
r=min(j,2p-j), sin(pi r/(2p))>=r/p, so summing as in Theorem 4 gives

    d_A(t)<=(1/2)sqrt(2/(exp(t/p^2)-1)).                   (15)

If no generator with nonzero cyclic coordinate is odd, generation forces
the pair, up to ordering and an automorphism of C_p, to be (0,1),(1,0).
Indeed some cyclic coordinate is nonzero, all such coordinates have even
sign, and at least one sign is odd. With two generators, the latter one
must have cyclic coordinate zero. For the v=0 characters the eigenvalues
are 3/4+(1/4)cos(2pi j/p), giving a nontrivial-character sum at most
2/(exp(4t/p^2)-1); for v=1 all p eigenvalues are at most 1/2. Thus

    d_A(t)<=(1/2)sqrt(2/(exp(4t/p^2)-1)+p4^-t).           (16)

To verify the first sum, its gap is (1/2)sin^2(pi j/p), so its 2t power
is at most exp(-t sin^2(pi j/p))<=exp(-4t r^2/p^2); extend the sum
to all r>=1 and use r^2>=r. These are all possible sign/coordinate
patterns for generating pairs. At t=ceil(c p^2), the bounds (15),(16)
can be made arbitrarily small by choosing c large; their negligible
p4^-t term tends to zero. The additional group/quotient error in (9)
also tends to zero uniformly. This proves the worst-case O(p^2) upper
bound for every fixed threshold. The exceptional pair projects to the
cycle, whose lower bound at threshold epsilon<1/2 is
log(1/(2epsilon))/[-log cos^2(pi/p)], of order p^2 by the proof of
Theorem 4. It establishes the matching lower bound and the theorem.

## Theorem 10: tails and mean differ from the typical scale

Let T_p=t_mix(1/4) in the conditioned random-pair model. For every fixed
u>=1,

    1/(16pi^2 u) <= liminf Pr(T_p>floor(up))
                 <= limsup Pr(T_p>floor(up)) <= 2pi/u.      (17)

Moreover E[T_p]=Theta(p log p), although T_p has typical order p.
Consequently T_p/p does not converge in probability to any finite constant.
All probabilities and expectations here condition on generation.

#### Complete lower-tail proof

Put C=4pi^2 and R=floor(sqrt(p/(Cu))). Consider the positive integer
vectors (r,s) with 1<=r,s<=R and gcd(r,s)=1. At least R^2/4 such
vectors exist: a noncoprime vector has a common divisor m>=2, so the
number of noncoprime vectors is at most

    sum_{m=2}^R floor(R/m)^2 <= R^2 sum_{m=2}^infinity m^-2
                           <= (3/4)R^2.

The final estimate uses 1/4+integral_2^infinity x^-2 dx=3/4 and the
decreasing-integrand comparison for the tail starting at m=3.

Distinct primitive vectors in this box give distinct one-dimensional
subspaces of F_p^2. Indeed equality of their lines forces rs'-sr'=0
modulo p. The integer determinant has absolute value at most R^2<p,
so it is zero as an integer. From gcd(r,s)=1, r divides r', and the
zero determinant gives (r',s')=l(r,s) with a positive integer l.
Primitivity of (r',s') forces l=1, hence the vectors were identical.

Conditioned on a cyclic pair (a,b)!=(0,0), its projective line is uniform
among the p+1 lines, since each line has exactly p-1 nonzero vectors.
Thus it hits one of these primitive-vector lines with probability at
least R^2/[4(p+1)]. On that event some nonzero m in F_p obeys
(ma,mb)=(r,s). The quotient character with v=0,j=m has gap

    1-lambda <= pi^2(r^2+s^2)/(2p^2) <= pi^2 R^2/p^2.

At t=floor(up), Bernoulli's inequality gives
lambda^t >= 1-t(1-lambda) >= 1-pi^2/C=3/4.
The character TV lower bound therefore gives d_G(t)>=3/8>1/4, so T_p>t.
As p tends to infinity, R^2/p->1/(Cu). The probability bound tends to
1/(4Cu)=1/(16pi^2 u), proving the first inequality in (17).
The upper inequality follows from (11) with t=floor(up): the same
limit calculation as (12) gives pi/(8u(1/4)^2)=2pi/u. Rounding down
instead of up does not alter that calculation.

If T_p/p converged in probability to a finite c, choose u>max(c,1).
The probability in (17) would tend to zero, contradicting its positive
lower bound. This proves the nonconcentration assertion, rather than
merely inferring it from the Monte Carlo plots.

#### Complete expectation proof

For each integer t with p<=t<=p^2/(4C), repeat the lower proof with
u=t/p and R=floor(p/sqrt(Ct)). Now the quantity inside the floor is at
least 2, so R>=p/(2sqrt(Ct)). The same Bernoulli argument gives

    Pr(T_p>t)>=R^2/[4(p+1)]>=p/(32Ct).

Summing over these integer times and using
E[T_p]=sum_{t>=0}Pr(T_p>t) gives a lower bound
(p/(32C))(log p-O(1)), hence Omega(p log p).

For the upper bound, Theorem 9 supplies a constant K such that every
generating pair has T_p<=ceil(Kp^2) for all sufficiently large p.
Also e_p(t)<=1/8 for all t>=p when p is sufficiently large, by rho<1.
Expanding B_p(t) in (11) gives, with an absolute constant C_1,

    Pr(T_p>t)<=16B_p(t)
       <=C_1(4^-t+p/t+1/sqrt(t)+1/p), t>=p.

The sum of these bounds for p<=t<=ceil(Kp^2) is O(p log p): the
four terms contribute O(1), O(p log p), O(p), and O(p), respectively,
by a geometric sum and integral comparisons. Times below p contribute
at most p, and times beyond the deterministic bound contribute zero.
This proves O(p log p) and the matching mean-order claim.

## Current remaining gap

These results reach the sparse regime k=2 for one explicit nonnilpotent
family, with complete constants and a quotient-profile approximation.
They do not control arbitrary groups with large commutator subgroups,
where short commutator words need not cover the normal subgroup and
its relative diameter may grow. In particular they do not give a
sharp general mixing time, all-group cutoff, or the alternating-group
worst-case-pair conjecture. They exclude cutoff under the stated
in-probability convention, including random centers, but do not establish
a limit law. At threshold 1/4, Theorem 10 disproves concentration of
t_mix/p at any finite deterministic constant for this family.

## Completed checks

The full checklist is in SECOND_AUDIT.md. second_checks.json records
the spectral blocks, generation criterion, quotient moment bound,
full-group/quotient profiles, and both worst-case upper-bound cases.
second_boundary_checks.json records the slow-mode bound and exceptional
pairs. tail_checks.json records 12 primitive-direction checks at
p=101,503,1009,5003 and u=1,2,4: exact modular injectivity and primitive
counts, plus floating-point checks of the slow-mode power >=3/4.
All passed. These computations support finite checks; the asymptotic
tail and expectation statements are established by the full proofs above.

## Completed Lean verification

FiberAlgebra.lean kernel-checks six integral 2x2 matrix identities for
the standard S_3 representation, using Matrix.ext and decide +kernel.
I2 and Z2 are the explicit identity and zero matrices. The successful
command is recorded in lean_second.log, run from ~/lean_verify
with a 3600-second timeout. No sorry or native_decide is used.
Only the finite algebra is formalized; the operator bounds, Gaussian
grid estimate, probability formulas and asymptotic conclusions are
complete paper proofs, not Lean-verified theorems.

The first finite matrix attempts failed on missing instance/import
requirements; these errors did not establish any result. Only the
corrected exit-zero run is called checked.
