# E0093 research attempt, 2026-10-12

## Exact source and scope

Diaconis, *Some things we've learned (about Markov chain Monte Carlo)*,
Bernoulli 19(4) (2013), 1294–1305, DOI 10.3150/12-BEJSP09,
arXiv:1309.7754, Section 5, Question 2, PDF page 9, asks:

> The same set of problems can be considered for any group G. If a generating
> set S is chosen at random, what is the typical rate of convergence? This is
> the topic of random random walks.

The preceding example concerns uniform increments from an ordered list of
vectors in C_2^n, with ergodicity explicitly required in Wilson's theorem.
The question itself does not fix cardinality, sampling with replacement,
symmetrization, laziness, a group sequence, or the meaning of typical.
It also states a separate conjecture for **any** generating pair of A_n;
that conjecture is not silently substituted for the intake problem.

I do not regard this missing specificity as a counterexample to the research
question. The following are partial answers under explicit conventions.
No novelty is claimed: the logarithmic-generator expansion phenomenon and
hypercube cutoff are classical. The exact periodicity calculation is recorded
as a verified elementary result, without a novelty claim.

## Model

Let G have order n>=2. Sample g_1,...,g_k independently and uniformly from G,
with replacement. Retain multiplicities. The symmetric discrete-time walk has
P f(x)=(1/(2k)) sum_i [f(xg_i)+f(xg_i^{-1})]. Its lazy version is
Q=(I+P)/2. Uniform pi is stationary. Distances below are total variation,
started at the identity; translations imply that this also gives worst-case
distance. All randomness in a tail estimate is over the sampled tuple, not
over time-varying resampling. A set with duplicates removed is a different model.

## Theorem 1: explicit uniform high-probability bound

Let H be the real mean-zero subspace of functions on G with counting inner
product. Write A=P|_H. For integers m>=1 and k>=m and any a>0,

    Pr(||A|| >= a) <= (n-1) m m^(2m) / (m! k^m a^(2m))
                    <= (n-1) m (e m/(k a^2))^m.                 (1)

On the complementary event, for all integer t>=0,

    ||P^t(e,.)-pi||_TV <= (sqrt(n-1)/2) a^t.                 (2)

For Q replace a by (1+a)/2 (assuming a<1). In particular, put
m=ceil(2 log n), k>=ceil(16 e m), a=1/2. With probability at least
1-(n-1)m4^(-m), the nonlazy walk is irreducible and aperiodic and

    t_mix(epsilon) <= ceil(log(sqrt(n-1)/(2 epsilon))/log 2)

when the expression is nonnegative, and otherwise zero. The failure bound
tends to zero and this is an O(log n) bound uniform over all finite groups.
It does **not** prove mixing of order log n/log k or cutoff.
Let B=(n-1)m4^(-m). If B<1, the same successful-event conclusions,
conditioned on the sampled tuple generating G, fail with probability at
most B/(1-B). Indeed failure of generation implies ||A||>=1, and hence
is included in the bad event ||A||>=1/2. Thus Pr(generation)>=1-B;
conditional bad-event probability is at most B/Pr(generation)<=B/(1-B).
This addresses a conditioned-generating-tuple interpretation as well.

### Full proof of (1)

For g in G set R_g f(x)=f(xg). R_g is orthogonal, R_g^*=R_{g^{-1}},
and H is invariant. Put Y_i=(R_{g_i}+R_{g_i}^*)/2 restricted to H.
These independent matrices are self-adjoint contractions. For f in H,
E[R_g f](x)=(1/n)sum_y f(y)=0, so E Y_i=0. A=k^{-1}sum_i Y_i.

Since A is self-adjoint, tr(A^(2m))>=||A||^(2m). Expand the trace into
k^(2m) ordered words of length 2m in the Y_i. If an index i occurs exactly
once, condition on every other matrix. The product then has the form
B Y_i C, with B,C fixed under that conditioning, so its conditional
expectation is B (E Y_i) C=0. This argument does not commute the matrices.

Any surviving word has r distinct indices with 1<=r<=m. There are at most
binom(k,r) r^(2m) such words for each r: choose the labels then count all
words on them. This overcounts words missing labels and words with singleton
labels, which is harmless for an upper bound. Every product is a contraction.
For any real matrix B with ||B||<=1, |tr B|<=n-1, by summing
|<e_j,B e_j>|<=1 over an orthonormal basis of H. Products need not be
self-adjoint; this bound still holds. Thus

    E tr(A^(2m)) <= (n-1) k^(-2m)
                        sum_{r=1}^m k^r r^(2m)/r!.

Set T_r=k^r r^(2m)/r!. Because k>=m and r<=m,

    T_r/T_m = k^(r-m) (r/m)^(2m) m!/r!
             <= k^(r-m) m^(m-r) <= 1.

Consequently the sum is at most m T_m, proving the first bound by
Markov's inequality. Finally,
log(m!)>=integral_1^m log x dx=m log m-m+1>=m log m-m,
so m!>=(m/e)^m and the second bound follows.

### Full proof of (2) and the corollary

Use the pi-weighted L2 norm. The density of delta_e relative to pi minus
one has squared norm n-1. Reversibility implies that the time-t density
minus one is P^t applied to this function. Its norm is at most
a^t sqrt(n-1). Cauchy–Schwarz gives TV at most half this norm.
For Q, each eigenvalue on H is (1+lambda)/2, and if |lambda|<a<1,
its absolute value is at most (1+a)/2.

If the tuple fails to generate, a nonconstant function constant on the
sets xK, where K is the generated subgroup, is P-invariant; after subtracting its
mean it gives eigenvalue 1 on H. Thus ||A||<1 implies generation.
For an irreducible symmetric walk, a period can only be 1 or 2: returning
along a generator and its inverse gives a positive-probability two-step
return. Period 2 gives a bipartition and a +/-1-valued eigenfunction with
eigenvalue -1, contrary to ||A||<1. Hence the successful tuple is aperiodic.
For a=1/2 and k>=16 e m, the ratio in (1) is at most 1/4. With the selected
m, (n-1)m4^(-m)<=m n^(1-2 log 4), which tends to zero.
Solving (2) for the epsilon threshold gives the stated mixing bound.

## Theorem 2: exact periodicity probability for a binary vector space

Let d>=1 and k>=d. Sample k iid uniform vectors in V=F_2^d and condition
on their spanning V. For the nonlazy uniform-increment walk,

    Pr(period 2 | spanning) = (2^d-1)/(2^k-1).                (3)

Consequently for k=d+s with fixed s>=0 this probability tends to 2^(-s)
as d tends to infinity. In these regimes nonlazy convergence to uniform
fails with a probability bounded away from zero, even after conditioning
on generation. This is an obstruction to an unconditional convergence
assertion, not a solution of the general question with ergodicity imposed.

### Full proof

Arrange the vectors as columns of a d-by-k binary matrix M. They span iff
M has row rank d. The number of such matrices is

    N(d,k)=product_{j=0}^{d-1}(2^k-2^j).                     (4)

Indeed choose the ordered rows one by one: after j independent rows their
span has 2^j elements, all forbidden for the next row. Conditional on rank
d, the row space W is uniform among d-dimensional subspaces of F_2^k:
each such subspace has exactly product_{j=0}^{d-1}(2^d-2^j) ordered bases,
and those bases are exactly the matrices with row space W.

For nonzero v,w in F_2^k an invertible linear map carries v to w
(extend each to a basis and map the bases). Such maps permute the
d-dimensional subspaces bijectively. Therefore Pr(v in W) is the same
number p for all 2^k-1 nonzero v. Since every W has exactly 2^d-1
nonzero elements, summing their indicator expectations gives
p(2^k-1)=2^d-1.

It remains to show that period 2 is exactly the event 1_k in W. The latter
means there is a linear functional f:V->F_2 with f(g_i)=1 for every i.
Such an f is nonzero, partitions V into two equal parts, and every step
switches parts, so the walk has period 2 (two-step returns exist).
Conversely suppose period is 2. Equivalently all paths from zero to any
fixed x have the same length parity: two paths of opposite parity would
combine, by reversal, into an odd closed walk; by translation this is an
odd return at zero, contradicting period 2. Define f(x) as that parity.
Paths exist because the columns span V. Translating a path from 0 to y
and appending it to a path to x shows f(x+y)=f(x)+f(y). Thus f is a
linear functional over F_2 and f(g_i)=1. This is precisely 1_k in W.
The preceding probability computation proves (3). On this event, at every
time the law lies entirely in one part and has TV distance at least 1/2
from uniform. The limit for k=d+s follows by dividing numerator and
denominator by 2^d.

## Theorem 3: full mixing-scale answer for conditioned random bases

In the model of Theorem 2 with k=d, condition on spanning and use Q.
Every realization is carried by a linear automorphism to the lazy
coordinate-flip hypercube walk. In particular its TV profile is
deterministic, independent of the random basis. As d tends to infinity,
it has cutoff at (d/2)log d, with a window of order at most d.
The nonlazy walk always has period 2, by (3).

### Full proof and explicit bounds

The linear map sending the sampled basis to the coordinate basis is
bijective, preserves uniform measure, and conjugates the transition
operators, so it preserves TV distances at every time. It is enough to
consider the coordinate basis. Write chi_A(x)=(-1)^(sum_{i in A}x_i).
These 2^d functions are orthonormal under uniform measure: the product of
two is chi_{A symmetric-difference B}, whose expectation is zero unless
A=B, since any coordinate in that difference is an independent fair bit.
Under Q their eigenvalues are lambda_A=1-|A|/d: half the time stay and
otherwise choose a uniform coordinate to flip. The initial density at
zero is sum_A chi_A, because the sum is 2^d at zero and zero elsewhere.
Thus orthogonality and Cauchy–Schwarz give, for integer t>=1,

    TV(t) <= (1/2)sqrt(sum_{j=1}^d binom(d,j)(1-j/d)^(2t))
          <= (1/2)sqrt((1+exp(-2t/d))^d-1)
          <= (1/2)sqrt(exp(d exp(-2t/d))-1).                (5)

The middle inequality uses 1-u<=exp(-u), including u=1 when t>=1.

For the lower bound let Z(x)=sum_i (-1)^x_i and start at zero. For d>=2,
E Z=d(1-1/d)^t=:b. For distinct i,j,
E[(-1)^(X_i+X_j)]=(1-2/d)^t <= (1-1/d)^(2t).
Therefore covariances are nonpositive and Var(Z)<=d. Under uniform
measure E Z=0 and Var(Z)=d. Applying Chebyshev under both measures to
the event {Z>b/2} gives

    TV(t) >= 1-8d/b^2
          = 1-8/[d(1-1/d)^(2t)].                         (6)

Bounds may be clipped to [0,1]. At t=floor((d/2)log d-cd), for fixed c
and sufficiently large d, expansion log(1-1/d)=-1/d+O(1/d^2) shows
d(1-1/d)^(2t)->exp(2c). Hence liminf TV>=1-8exp(-2c).
At t=ceil((d/2)log d+cd), (5) gives limsup TV<=
(1/2)sqrt(exp(exp(-2c))-1). Letting c tend to infinity proves cutoff
with the stated window bound. Rounding alters neither limit. For d=1
the lazy walk is uniform after one step and is a separate finite case.

## Theorem 4: a fixed-generator boundary case has quadratic mixing

Let G=C_n, n>=3, sample a single uniform element, and condition on its
generating G. Use the symmetric lazy walk Q. Every such generator gives
exactly the same TV profile, by the bijection x -> gx from C_n to itself.
For the threshold 1/4, t_mix is Theta(n^2), not a polynomial in log n.
The nonlazy directed one-generator walk is deterministic and never mixes
when n>1; the symmetric nonlazy walk is periodic when n is even.

### Full proof

After conjugating to generator 1, Q stays with probability 1/2 and moves
to each neighbor with probability 1/4 (these are distinct for n>=3).
The characters exp(2 pi i j x/n) are an orthonormal basis under uniform
measure: the geometric series sums to zero at every nonzero frequency.
Their eigenvalues are

    lambda_j=(1+cos(2 pi j/n))/2=cos^2(pi j/n).

As in Theorem 3, the density at zero has all Fourier coefficients 1,
and hence TV(t)<= (1/2)sqrt(sum_{j=1}^{n-1} lambda_j^(2t)).
Put r=min(j,n-j), so 1<=r<=floor(n/2). Concavity of sine on [0,pi/2]
gives sin(pi r/n)>=2r/n. Thus
lambda_j=1-sin^2(pi r/n)<=exp(-4r^2/n^2). Each r has multiplicity at
most two. Since r^2>=r, extending the sum to all positive r gives

    TV(t)<= (1/2)sqrt(2/(exp(8t/n^2)-1)),  t>=1.            (7)

In particular t>=ceil((n^2/8)log 9) gives TV<=1/4.
For the lower bound use f(x)=cos(2 pi x/n), with ||f||_infinity<=1,
uniform mean zero and Q^t f(0)=lambda_1^t. For any two probability
measures and such an f, the expectation difference is at most 2 TV,
by the defining absolute-sum formula for TV. Therefore

    TV(t)>=lambda_1^t/2.

Consequently t_mix(1/4)>=log 2/(-log lambda_1). For n>=4,
u=sin^2(pi/n)<=1/2 and -log(1-u)<=u/(1-u)<=2u<=2pi^2/n^2.
Thus t_mix(1/4)>=(log 2)n^2/(2pi^2), proving the asymptotic order.
The finite n=3 case is covered by the exact eigenvalue formula and is
irrelevant to the asymptotic claim. A directed one-generator law at each
time is a point mass, giving TV=1-1/n. An even cycle is bipartite for
the symmetric nonlazy walk, so its TV is at least 1/2 at every time.

## Referee checks and remaining gap

Critical points: independent sampling is essential for singleton
cancellation; matrices need not commute; multiplicities must not be
discarded; generation and aperiodicity are different; nonlazy hypercube
profiles cannot be used as convergent profiles; a constant spectral gap
does not yield diameter-scale mixing; numerical checks and finite Lean
checks do not prove the general asymptotic theorems.

The broad problem remains unresolved by this attempt. Precisely, no
typical sharp mixing time or profile is obtained for arbitrary sequences
G_n with sparse random k_n-generators (even conditioned on generation and
using Q), beyond the general bound above. Nor is cutoff proved for every
group sequence in a growing-generator regime. The alternating-group
worst-case generating-pair conjecture is also not settled.

### Completed computation (checks.py, checks.json)

Exhaustive **integer** enumeration checked (3) and (4) at (d,k) equal to
(1,1), (1,2), (2,2), (2,3), (2,4), (3,3), (3,4), (3,5).
For example, for d=3,k=5 there are 26040 generating tuples among 32768,
and 5880 are periodic; 5880/26040=7/31, as predicted.

All tuples of length k=1,2,3 on S3 were enumerated, with symmetric
permutation matrices centered by the uniform projection. Their empirical
matrix sum is zero up to floating-point tolerance, and some pairs of
these matrices explicitly fail to commute. For every m<=k the averaged
trace moment and the tail at a=.5,.8 satisfied (1). These are numerical
checks of finite examples, not an exact or formal proof of Theorem 1.

For d=16,64,256, the lazy hypercube walk was computed by the transition
recursion on Hamming weight, using d+1 states. Symmetry makes this exactly
the same mathematical TV observable as the full cube; arithmetic used
floating point. Every computed time checked (5) and (6). At d=256 the
mixing times at TV thresholds .75,.5,.25,.1 were 500,634,825,1062,
respectively, around the center 709.783. Probability sums stayed within
1e-10 of 1. The finite jobs used tiny arrays and completed in under one
second of Python compute time (excluding shared-machine startup).

Cycle checks (cycle_check.py, cycle_checks.json) computed the full n-state
lazy recursion for n=3,4,5,8,16,32,64. Both character-based inequalities
in Theorem 4 held at every checked time; probability at threshold 1/4
was reached before the stated upper bound. At n=64 the measured integer
mixing time was 389; the explicit spectral lower bound was 287.549 and
the upper bound was 1125. This verifies constants on small cases, not
the asymptotic theorem by computation.

### Lean verification completed

FiniteChecks.lean imports only Mathlib.Data.ZMod.Basic and
Mathlib.Data.Fintype.BigOperators. It defines spanning through binary
linear combinations, and the existence of a functional evaluating to 1
on every generator. Using `decide +kernel`, Lean proves for F_2^2:

- k=2: exactly 6 generating tuples, all 6 with an odd functional;
- k=3: exactly 42 generating tuples, 18 with an odd functional.

The command was `lake env lean
~/brain_workers/TRIO_1011/op/E0093/FiniteChecks.lean`, run
from ~/lean_verify with a 3600-second subprocess timeout.
The corrected run returned exit code 0 in 52.207 seconds; stdout and
stderr were empty. See lean_check.log. No `sorry` or `native_decide`
occurs in the file. An earlier invocation failed because the optional
Mathlib.Tactic.Decide module was unavailable; removing that import fixed it.

**Scope:** these are kernel-checked finite algebraic counts only. The
equivalence with Markov-chain period and the all-dimension formula are
proved above on paper; they are not formalized in Lean. Likewise, the
matrix-moment and cutoff theorems are not Lean-checked.

## Second serious attempt (2026-10-12)

At the user's request I reopened the sparse-generator gap. Two approaches,
normal-subgroup averaging and quasirandom word-collision estimates, are
written in SECOND_ATTEMPT.md. I pursued the former and supplied complete
proofs there of Theorems 5–10:

- A deterministic quotient/fiber TV comparison for any finite normal subgroup
  whose elements have bounded word length in the chosen generators.
- For **every** generating pair on S_3 x C_p, prime p>3, a uniform quotient
  error at most sqrt(p)(1/2+sqrt(3)/4)^t, with quotient C_2 x C_p.
- For two iid uniform generators **conditioned on generation**, mixing time
  of order p in probability, with an explicit deterministic lower bound and
  upper tail. This is a sparse, nonnilpotent special case. No deterministic
  leading constant or limit law is obtained.
- Absence of cutoff for this model under the explicitly stated convergence-
  in-probability definition, including environment-dependent centers.
- An exceptional generating pair with an order-p^2 lower bound, showing
  why a uniform order-p bound over all pairs would be false.
- A matching uniform order-p^2 upper bound over all generating pairs,
  determining the worst-case scale for this same family.
- Matching order-1/u tails for t_mix(1/4)/p and mean mixing time of order
  p log p. In particular the normalized mixing time cannot converge in
  probability to a finite deterministic constant.

The remaining general gap is unchanged: no sharp typical mixing result for
arbitrary sparse random Cayley walks, and no answer to the alternating-group
worst-case generating-pair conjecture. The new full proofs and their audits
are in SECOND_ATTEMPT.md; finite computations are in second_checks.json and
second_boundary_checks.json. No novelty claim is made.
