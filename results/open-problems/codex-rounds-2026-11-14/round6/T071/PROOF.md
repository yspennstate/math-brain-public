# A rank-occupation representation of the descendant kernel

Particles perform standard Brownian motions, branch into two at rate one,
and at each branch the leftmost of the resulting N+1 particles is removed.
All times below are physical times. These finite-N identities do not assert
an asymptotic genealogy theorem.

## 1. Distinct roots and the selection loss

Fix N>=k>=1. At time zero give the N particles different colors. Colors
are inherited at branching. Let W_v(t) be the number of particles of color
v, so W_v(0)=1 and sum_v W_v(t)=N. The initial positions are arbitrary.

Let F be a homogeneous degree-k polynomial with nonnegative coefficients
which is multilinear: every monomial is a product of k different colors.
Write b(t) for the color of the leftmost particle just before an event.
Then, at configurations with a unique leftmost particle,

    generator F(W) = k F(W) - (N+k-1) partial_b F(W).       (1)

Here partial_b denotes a formal polynomial derivative. Brownian motion
contributes zero since it does not change color counts.

To prove (1), fix the current count vector x and the color b of the
leftmost particle. A birth of color a followed by selection changes x to
x+e_a-e_b. The deleted color is b for every parent: if the parent is
leftmost, one of its two daughters is removed; otherwise the old leftmost
particle is removed. Multilinearity gives

    F(x+e_a-e_b)-F(x)
      = partial_a F(x)-partial_b F(x+e_a),
    partial_b F(x+e_a)
      = partial_b F(x)+partial_a partial_b F(x).

These formulas also hold for a=b, since partial_b partial_b F=0; their
sum is then zero. There are x_a parents of color a. Summing the first
derivatives gives sum_a x_a partial_a F=kF. The total deletion term is

    N partial_b F + sum_a x_a partial_a partial_b F
      = (N+k-1) partial_b F,                               (2)

by Euler's identity for the homogeneous degree-(k-1) polynomial
partial_b F. This proves (1).

For arbitrary starting positions there can be ties at time zero or just
after a birth. On a bounded interval there are finitely many births almost
surely. Between consecutive births, differences of distinct particle
positions are nondegenerate Brownian motions. They spend zero Lebesgue
time at zero. The next independent exponential event time hits such a
tie with probability zero. Thus there is a unique pre-birth minimum
almost surely at every positive event time, even with tied starting
positions. Any fixed rule for deletion ties gives (1) in the integrated
generator formulas. Brownian crossings do not alter colors.

In particular, the round-5 loss R for its degree-four polynomial simplifies
to

    R(t) = (N+3) partial_(b(t)) F(W(t))                    (3)

at almost every time. This retains all ancestral restrictions already
encoded in F.

## 2. A killed process with k distinguished particles

Choose k distinct initial particles a_1,...,a_k. Distinguish one particle
from each of these roots, keeping the k marks different. Consider the
following auxiliary process until it is killed:

- Its N particles diffuse as independent Brownian motions.
- An undistinguished particle branches at rate one.
- A distinguished particle branches at rate two. One of its daughters,
  chosen with probability one half each, inherits the distinction. The
  other daughter is undistinguished.
- After every birth delete the leftmost particle, as in N-BBM. If the
  deletion removes a distinguished particle, kill the whole process.

Use the original tie rule without consulting distinguished marks. In
particular, the daughter chosen to inherit a mark is independent of the
tie decision between the two daughters.

Let zeta be its killing time. Its live event rate is N+k, so it is
nonexplosive. Write P^dagger for this law, including the specified initial
positions and distinguished roots. Then

    E[product_(j=1)^k W_(a_j)(L)]
       = exp(kL) P^dagger(zeta>L),       L>=0.             (4)

The expectation on the left is under the original rate-one N-BBM.

Here is a direct proof which also identifies the law on the right. Record
the finite branching history up to L, including parents, daughter identities
and Brownian path segments; record even events which leave the population
configuration unchanged. For any ordered terminal tuple containing one
descendant of each a_j, trace the k paths back to the initial roots. These
paths always occupy distinct particles because their initial colors are
different. At a branch on one path there is exactly one daughter on that
path. Thus terminal tuples correspond bijectively to choices of daughters
along k distinguished paths which survive every deletion.

Compare the density of any such marked history under the two constructions.
Under original N-BBM each parent has rate one and the total rate is N.
Under the auxiliary law an undistinguished parent still has rate one.
A distinguished parent has rate two, multiplied by one half for the
specified daughter choice; its contribution is again one. The Brownian
path laws agree. The waiting-time factors, including the final interval
without an event, have ratio

    exp(-(N+k)L)/exp(-NL) = exp(-kL).

Summing the densities over all surviving marked histories therefore gives
exp(-kL) times the expected number of terminal tuples. That number is
product_j W_(a_j)(L). Histories have finitely many events almost surely;
nonnegative summation is justified by Tonelli's theorem. This proves (4).
The same argument applies with any bounded measurable terminal function
of the full configuration and the distinguished tuple.

## 3. Exact killing rate and a conservative spatial law

Suppose the pre-birth minimum is undistinguished. No birth can remove a
distinguished particle, so the killing intensity is zero. Suppose instead
the minimum is distinguished. The killing contributions are:

| Parent | Number | Rate per parent | Killing probability |
|---|---:|---:|---:|
| Undistinguished | N-k | 1 | 1 |
| Distinguished, other than the minimum | k-1 | 2 | 1 |
| Distinguished minimum | 1 | 2 | 1/2 |

The last probability is one half regardless of which daughter the tie
rule deletes. Hence the total killing intensity is

    lambda_(N,k) 1_{minimum distinguished},
    lambda_(N,k) = N-k+2(k-1)+1 = N+k-1.                  (5)

Define a conservative auxiliary process by suppressing the killing
transitions, without changing the rates of any surviving transitions.
Equivalently, it has this description on configurations with marks:

- Brownian diffusion is always present.
- When the minimum is undistinguished, apply all branching and deletion
  rules of Section 2, with distinguished rate two and other rate one.
- When the minimum is distinguished, suppress all births. The only
  surviving birth in Section 2 would replace that minimum by its
  distinguished daughter at the same position, with the same color and
  mark; it changes no configuration and may be omitted.

Retain colors and distinguished marks, but ignore names of indistinguishable
unmarked particles. Replacing a particle by a daughter at the same position
does not change future Brownian laws. This explains the equivalence in the
last item. This process is well defined by bounded-rate Poisson proposals
and Brownian diffusion; in particular it has no explosion. Denote its law
by P^circ and define its occupation time

    A_L = integral_0^L 1_{minimum distinguished at u} du.

Construct killing by taking a rate-one exponential random variable E,
independent of this conservative process, and killing when
lambda_(N,k) A_u first exceeds E. The resulting killed process has the
same diffusion, surviving jumps, and killing rate as Section 2. Its law
therefore agrees with P^dagger. One can verify uniqueness directly by
successive bounded-rate Poisson proposals between Brownian path segments.
Conditioning on the conservative path gives

    P^dagger(zeta>L)
      = E^circ exp(-(N+k-1) A_L).

Together with (4), this proves the exact occupation formula

    E[product_j W_(a_j)(L)]
      = exp(kL) E^circ exp(-(N+k-1) A_L).                 (6)

The occupation time is under P^circ. This law is different from ordinary
N-BBM, both in the branching rates and in the suppression at a marked
minimum. No independence of the selected descendant counts is used.

## 4. The frozen four-lineage polynomial

Fix deterministic times t_0<t_1<t_2 and condition on the original forest
and positions through t_2; call this history H_2. Give each t_2 particle
its own color. For such a particle v let i(v) be its t_1 ancestor, and
let p(i) be the t_0 ancestor of i. Freeze these maps.

Let C be the set of ordered quadruples c=(a,b,c',d) of t_2 particles with

    a!=b, c'!=d, i(a)=i(b), i(c')=i(d),
    p(i(a))!=p(i(c')).

All four particles in every such quadruple are distinct. Put

    F(x) = sum_(c in C) x_a x_b x_(c') x_d,
    Q(u) = F(W(u))/(N)_4,

where W(u) counts descendants at t_2+u and (N)_4=N(N-1)(N-2)(N-3).
This is precisely the filtered terminal-weighted statistic of rounds 4–5.
For a uniform ordered terminal sample, the event of four distinct younger
ancestors, two middle pairs, and two distinct older ancestors has conditional
probability 3Q(u), since there are three disjoint possible pairings.

For each c in C, start the conservative four-distinguished-particle law
from the actual t_2 positions, distinguishing the four members of c. Let
A_L^c denote its occupation time. Formula (6) and finite summation give

    E[Q(L)|H_2]
      = exp(4L)/(N)_4
          * sum_(c in C) E_c^circ exp(-(N+3) A_L^c).       (7)

If C is nonempty, choose its member uniformly and then run its auxiliary
process. Denote expectation under this mixture by E_(H_2)^circ. Since
Q(0)=|C|/(N)_4, (7) becomes

    E[Q(L)|H_2]
      = Q(0) exp(4L) E_(H_2)^circ exp(-(N+3) A_L).        (8)

For C empty both sides of (7) are zero; no mixture is needed. The older
ancestor filter is present in every term of (7). Neither (7) nor (8)
replaces terminal weights by unweighted counts. Since the exponential is
at most one, they recover the preceding propagation inequality.

There is also a deterministic conditional-survival version. Write

    m(u) = E[F(W(u))|H_2],
    rho(u) = E[partial_(b(u)) F(W(u))|H_2]/m(u)

when C is nonempty. The denominator is positive at every finite u:
the event of no branching has probability exp(-Nu) and leaves F=|C|.
Equation (1) and boundedness of counts give, for almost every u,

    m'(u) = [4-(N+3)rho(u)] m(u),
    m(L) = |C| exp(4L-(N+3) integral_0^L rho(u) du).       (9)

The numerator in rho counts the admissible distinguished tuples containing
the unique current minimum: fixing that particular particle leaves precisely
partial_(b(u)) F(W(u)) choices for the other three particles. The marked
history argument in Section 2 therefore identifies rho(u) as

    P_(H_2)^dagger(minimum distinguished at u | zeta>u).

In particular 0<=rho(u)<=1. It is a probability conditional on survival,
not the probability that a uniform ordinary N-BBM particle is leftmost.

## 5. A lower-tail constraint and the remaining estimate

For a single k-tuple, the nonnegative counts obey

    product_j W_(a_j)(L) <= (N/k)^k

by the arithmetic-geometric mean inequality, including zero counts.
Consequently (6) yields

    E^circ exp(-(N+k-1) A_L) <= (N/k)^k exp(-kL).          (10)

For every a>=0, on {A_L<=a} the exponential in (10) is at least
exp(-(N+k-1)a), so

    P^circ(A_L<=a)
      <= min(1, (N/k)^k exp(-kL+(N+k-1)a)).                (11)

For example, for 0<epsilon<k and L>0,

    P^circ(A_L <= (k-epsilon)L/(N+k-1))
      <= min(1, (N/k)^k exp(-epsilon L)).                 (12)

This is uniform over initial positions and the distinguished tuple, hence
also over the mixture in (8). It controls the auxiliary occupation's
lower tail. It supplies no small factor beyond the elementary product
bound, since multiplying (10) by exp(kL) returns that bound exactly.

To relate (7) to the required estimate, use the previous regime
tau_N=(log N)^4 and a_N=(log N)^3, with

    t_0=tau_N-a_N(s+delta+e),
    t_1=tau_N-a_N(s+delta),
    t_2=tau_N-a_N s,         L=a_N s.

The expectation over the genuine forest through t_2 now gives exactly

    E Q_N(s,delta,e)
      = exp(4a_N s)/(N)_4
          * E[sum_(c in C) E_c^circ
                       exp(-(N+3) A_(a_N s)^c)].          (13)

The inner auxiliary law starts from that random younger configuration;
the outer expectation is over the original N-BBM forest. Correlation
between C and the positions is retained. At s=0 the inner exponential is
one, as required by the unweighted endpoint statistic.

A sufficient next estimate would bound the right side of (13) by
C_(T,e) delta^2 uniformly for 0<=s<=T in the large-N upper limit. An
averaged version suffices for the preceding sliding-window criterion.
Equations (10)–(12) do not establish either estimate: survival is weighted
by a potentially enormous family factor, and occupation at the critical
level 4L/(N+3) can leave order-one descendant products after multiplication
by exp(4L). The marked spatial law and its correlation with C remain to
be estimated. The marked-transform limits, physical clock constant and
genealogy convergence are not obtained here.
