# Audit of the variance reduction

The main result is in PROOF.md. This file records attempts to invalidate it.
All calculations below are analytic; no numerical program was run.

## Exact tour test of the combinatorial identities

Take independent points on the two sites (0,0),(1,0), each with probability
one half. This is a test of the product-space identities, not the uniform
square model of T222. It uses actual optimum closed Euclidean tours: their
length F_n is zero if all points coincide and two otherwise.

Let Z_i be independent signs representing the sites. Expanding the
indicator of the event that all sites agree gives

\[
 1_{\{\text{all agree}\}}
 =\prod_i\frac{1+Z_i}{2}+\prod_i\frac{1-Z_i}{2}
 =2^{1-n}\sum_{A:\,|A|\text{ even}}\prod_{i\in A}Z_i.
\]

Therefore

\[
 F_n-\mathbb E F_n
 =-2^{2-n}\sum_{A:\,|A|\ge2\text{ even}}\prod_{i\in A}Z_i.
\]

Distinct sign products are orthogonal and have squared norm one. Thus

\[
 V_{n,j}=\begin{cases}
 2^{4-2n}\binom nj,&j\ge2\text{ even},\\
 0,&\text{otherwise}.
 \end{cases}
\]

Summing independently by the binomial theorem gives

\[
 \sum_jV_{n,j}=2^{4-2n}(2^{n-1}-1)
 =2^{3-n}-2^{4-2n}.
\]

Directly, F_n is twice a Bernoulli variable with success probability
1-2^{1-n}, so its variance is
4(1-2^{1-n})2^{1-n} = 2^{3-n}-2^{4-2n}, the same value.

The first interaction moment is

\[
 \sum_j jV_{n,j}
 =2^{4-2n}n2^{n-2}=n2^{2-n},\qquad n\ge2.
\]

For a direct replacement check, changing coordinate i can alter the tour
length only when the other n-1 sites agree. That event has probability
2^{2-n}; conditionally, the two independent choices for coordinate i
disagree with probability one half. The squared length difference is then
four. Hence E[(F_n-F_n^{(i)})^2] = 2^{3-n}. Half the sum over i is
n2^{2-n}, exactly the interaction moment above. This checks the factor
one half and the factor j in the energy identity independently.

For n=2, the component energies are V_1=0,V_2=1, so the variance is 1
and the energy is 2. For n=3, only V_2=3/4 is nonzero, so the variance is
3/4 and the energy is 3/2. For n=4, V_2=3/8,V_4=1/16, giving variance
7/16 and energy 1.

Retaining each sign with probability rho gives the covariance

\[
 C_n(\rho)=2^{4-2n}
 \left(\frac{(1+\rho)^n+(1-\rho)^n}{2}-1\right).
\]

In particular, C_2(rho)=rho^2 and C_3(rho)=3rho^2/4, matching both
direct orthogonal expansions. These formulas also give C_n(0)=0 and
C_n(1)=Var(F_n), and their derivative at one is n2^{2-n}.

For the shared-sample formula, conditioning on k signs retains exactly the
even products supported on those signs. For k>=1,
K_{n,k}=2^{4-2n}(2^{k-1}-1); K_{n,0}=0.
For n=3, K_1=0,K_2=1/4,K_3=3/4. Formula (19) in PROOF.md gives
V_2=3(1/4)=3/4 and V_3=3/4-3(1/4)=0. This checks the binomial factors
and alternating signs independently of the formal inversion proof.

## A failed inference: bounded energy does not give convergence

Let X_i be uniform in Q and let Z_i be 1 when the first coordinate of
X_i is at most one half, and -1 otherwise. Put

\[
 G_n=\frac{a_n}{\sqrt n}\sum_{i=1}^nZ_i,
 \qquad a_n=1\text{ for even }n,\quad a_n=2\text{ for odd }n.
\]

This symmetric function has only order-one components, so its variance
and interaction energy both equal a_n^2. Its energy is uniformly bounded
by 4 but its variance oscillates between 1 and 4. Thus compactness and
the uniform tail estimate do not imply the convergence claimed in T222.
The example is not a TSP counterexample; it rules out an invalid inference
from the reduction's abstract inequalities.

Fixed-order convergence is sufficient but need not be necessary for total
variance convergence. For example, alternate between
n^{-1/2}sum_i Z_i and binom(n,2)^{-1/2}sum_{i<j}Z_i Z_j, for n>=2.
Both have variance one, but their energy lies entirely in order one and
order two, respectively. The interaction energies have no full-sequence
limit. This prevents describing the sufficient condition as an equivalence.

## Geometric and limiting cases checked

The asymptotic constant 1/pi in n E[R^2] was checked a second way. For
fixed interior x and fixed u>=0, the disk of radius sqrt(u/n) lies in Q
for all sufficiently large n. Consequently,

\[
 \mathbb P(nR(x,S)^2>u\mid x)
 =(1-\pi u/n)^{n-1}\longrightarrow e^{-\pi u}.
\]

For all x and n>=2, (6) in PROOF.md bounds this probability, on 0<=u<=2n,
by (1-u/(2n))^{n-1} <= e^{-u/4}; for u>2n it is zero. This integrable
bound permits dominated convergence over x in Q and u in [0,infinity).
The integral of e^{-pi u} is 1/pi. Boundary points form a set of area zero.
This gives the same limit as the explicit interior/boundary sandwich
(7b), through a different limiting argument.

The energy coefficient 4 multiplying n E[R^2] also follows directly from
conditional variance: each deletion cost has square at most 4R^2, so
sum_i E[Var(f_n|X_{-i})] <= 4n E[R^2]. This checks the asymptotic upper
bound 4/pi without replacement pairs. It is an upper bound, not an exact
value of the interaction energy or variance.

- Corners and edges: a quarter-disk area formula cannot be assumed at all
  radii in the square. The proof instead uses a homothetic copy of the
  entire square, valid for every radius from zero to sqrt(2).
- n=2: the deleted set is a singleton, its tour has length zero, and
  insertion costs exactly twice the distance. No nonexistent incident edge
  on a singleton is used.
- n=1: the tour length is zero. The theorem is stated for n>=2 because a
  nearest-neighbor distance to the deleted set would otherwise be undefined.
- Repeated points and ties: shortcutting and insertion work with zero
  lengths and with any chosen nearest point. No uniqueness of the optimal
  tour or of a nearest point is assumed.
- Centering: all K and C quantities are covariances or variances, and
  h_empty=E[L_n] is excluded from the spectrum. No raw second moment is
  substituted for the variance.
- Fixed sample size: all replacements use the same n and the same deleted
  (n-1)-point set. No Poissonization or change of mean point count occurs.
- Fixed domain: the proof concerns L_n in the unit square, without dividing
  the variance by n or invoking the first-order TSP constant.
- Global tour rearrangements: the insertion bound constructs a competitor;
  it does not assert that optimum edges change only near the inserted point.
- Positivity of the limiting constant is not proved. No lower-bound theorem
  is imported without proof to claim it here.
- No theorem about convergence of the remaining fixed-order terms is
  established. In (19), the factor binom(n,j) can amplify small errors in
  K_{n,k}; ordinary convergence of those unscaled covariances is insufficient.
- The constant 8 has independent geometric and conditional-variance checks
  in Section 5 of PROOF.md. The refined limiting energy bound 4/pi has the
  two nearest-neighbor derivations above and in Section 1 of PROOF.md.
  Neither is identified with the conjectured limiting variance.

No contradiction was found in the reduction. The original conjecture and
the convergence hypotheses of the reduction remain open in this work.
