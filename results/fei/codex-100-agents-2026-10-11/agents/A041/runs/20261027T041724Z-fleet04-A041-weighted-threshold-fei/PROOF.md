# A nonsymmetric two-weight prime boundary

All logarithms are natural. This is a proposed diminished-source obstruction,
not a disproof of FEI. The proof and exact validation are recorded separately.

For m>=3 define a Boolean sign F_m on two core bits and m rare bits in {0,1}:

    F_m=+1 iff 3b_1+3b_2+2 sum_(i=3)^(m+2) b_i >=5.

Equivalently the two core weights are3/2, all rare weights1, and the threshold
is5/2. In fact every core weight w in(1,2), rare weight1 and threshold w+1
gives exactly the same truth table: the required rare counts at core counts
0,1,2 are3,1,0. Set core biases1/2 and rare biases epsilon, where
0<epsilon<=1/(8m). The corresponding physical sign variables are x_i=2b_i-1.
Write c_S for the coefficients in product(x_i-E x_i), v_i=4p_i(1-p_i),
P(S)=v_S c_S^2, Delta=sum_nonempty(|S|-1)P(S),
R=sum_(|S|>=3)(|S|-2)P(S). On occupied coefficients use
1/2<2^j_S|c_S|<=1. Put J1=ln4 sum_single Pj,
Jhi=ln4 sum_high Pj, L1=sum_single P ln(1/(2^j|c|)^2), and
Bstar=ln4(2Delta-R)-J1-ln2 L1.

## 1. Nonsymmetry, essentiality and disjoint-wire primeness

Two positive core bits pass; two positive rare bits fail, with all other bits
zero. Thus the function is not symmetric in its essential physical inputs.
Each core is pivotal when the other core is1 and every rare bit is0. Each rare
bit is pivotal when exactly one core is1 and every other rare bit is0.

A Boolean wire representing a proper block permits at most two distinct
cofactor rows indexed by assignments inside that block. We exhibit three for
every block A with2<=|A|<=m+1. Let k be its number of core bits and r its
number of rare bits. All unspecified coordinates below are0.

If k=2, the outside contains a rare bit. Use inside assignments with0,1,2
positive core bits, and outside assignments with0,1 positive rare bits.
The rows are (--),(-+),(++).

If k=1, then r>=1. Use inside assignments of weights0,1,5/2 (none, one
rare, and the core plus one rare), and outside assignments with its core0,1.
Again the rows are (--),(-+),(++).

If k=0 and r<m, use inside rare counts0,1,2. Use outside assignments
consisting of one core alone, or one rare alone, in that order. Their rows
are (--),(+-),(++): the total weights tested are3/2+s and1+s.

If k=0 and r=m, then m>=3. Use inside rare counts0,1,3, and outside core
counts0,1. The rows are (--),(-+),(++).

Every possibility is covered. No proper block can factor through one Boolean
wire; the gate is prime in the stated disjoint physical-wire sense. This
does not assert affine primeness or primeness under overlapping variables.

## 2. The same reserve vanishes at a nonsymmetric prime boundary

Let K~Binomial(m,epsilon), q_s=Pr(K=s), a=binom(m,3)epsilon^3.
For core count0,1,2 the required rare counts are respectively3,1,0.
Monotonicity implies physical derivatives D_i in{0,1}, hence d_i=t_i.
The two core derivative means and their pair coefficient are

    t_1=t_2=(q0+q1+q2)/2 >=(1-a)/2,
    c12=(q0-q1-q2)/2 >=(1-2m epsilon)/2 >=3/8.

The first inequality is the union bound for a positive rare triple; the
second uses Pr(K>=1)<=m epsilon. All three quantities lie in(1/4,1/2],
so their dyadic scales are exactly1. In particular

    Jhi >= ln4 P({1,2}) >=9 ln4/64.                 (1)

A rare derivative has mean
t_r=(1/2)Pr(K_other=0)+(1/4)Pr(K_other=2)<=1/2.
Consequently I<=1+2m epsilon. At K=0 the core gate is AND2 and its mean
is-1/2. Monotonicity and a sign change of at most2 give
-1/2<=E F<=-1/2+2m epsilon<=-1/4, hence Var>=3/4 and
Delta<=1/4+2m epsilon. The core singletons alone give
J1/ln4>=2[(1-a)/2]^2>=1/2-a; other singleton terms and L1 are nonnegative.
Thus

    0 < (Bstar+ln4 R)/ln4
      =2Delta-J1/ln4-L1/2
      <=4m epsilon+a <=5m epsilon.                 (2)

The last inequality uses a<=(m epsilon)^3/6<=m epsilon. Nonnegativity of
Bstar is the previously proved joint singleton inequality; it also follows
directly from d>=t and x-1-j-ln(x/2^j)>=0 on its dyadic cell.
Strict positivity follows from R>0. Indeed, fix all but the two core bits
and one rare bit to0. The restricted gate is Maj3, with multilinear degree3.
Thus the full gate has degree at least3. Affine centering preserves degree,
so some c_S with |S|>=3 is nonzero; all v_i>0 implies R>0.

Combining(1)-(2), with a strictly positive denominator, yields

    Jhi/(Bstar+ln4 R) >=9/(320m epsilon).           (3)

For every finite arity cutoff N and finite K>=0 choose m>=max(3,N), then
choose positive dyadic epsilon<=1/(8m) with9/(320m epsilon)>K. This is an
actual nonsymmetric two-weight prime gate beyond that cutoff and violates
Jhi<=K(Bstar+ln4R); it also violates Jhi<=K Bstar. Thus excluding ALL
symmetric gates and every fixed finite set of primes does not repair these
particular diminished-source suppliers. Formula/composition-prime here is
precisely the disjoint one-wire definition proved above.

## 3. Scope and the exact unpaid line

As epsilon tends to0, deterministic contraction gives fair AND2, whose core
high-sector bill is positive. The small denominator is a diminished account,
not total original influence or Delta. The ratio H/I is not shown to grow.
The family has two weight groups, positive real weights, independent interior
biases, and unbounded arity. It closes the symmetric-exception loophole in
A045's boundary obstruction; it does not refute an exception that separately
pays these nonsymmetric gates, a nondegenerate-bias theorem, or a different
source that retains the boundary core's original high bill.

All prior singleton imports, mantissas, low/high carries, positive S_tree,
normalization, ordinary KL and both complete terminal laws retain their
original owners. Conditional-input TC remains distinct from spectral
good-coordinate erasure. The recovered pivotal-credit failure remains
coefficient-one only. The first unpaid universal line is a complete
rare-input/core transfer, paying the boundary core from its own original
influence and the perturbation from unused original capacity after every
existing debit. No such universal payment is asserted here.

## 4. Validation and adversarial cuts

The frozen sixteen-case domain has m=3,4,5,6 and
epsilon=1/(k m), k=8,16,64,256. code/check.py checks actual product spectra,
Parseval, exact integer dyadic cells, the binomial formulas independently,
every proper Boolean block, and outward rational natural-log signs. The
separate pilot directly sums every product Fourier coefficient as a second
implementation of the transform. Main:2084 assertions; pilot:79 assertions.
These finite checks support the proof and do not replace its all-m argument.

The m>=3 condition matters: at m=2 the block consisting of the two rare bits
has only two distinct cofactor rows and factors through their OR. At m=1
the actual gate is symmetric Maj3. At epsilon=0 the rare coordinates must
be contracted; no division by their zero variance is used. These cuts
explain why neither a fixed-arity check nor a deterministic fake prime is
the claimed counterfamily. The sign of the physical output mean and the
strict positivity of the denominator are both used explicitly above.

A core-Lean check of the elementary fact that three Boolean values include
an equal pair returned RUNTIME_UNVERIFIED after121.3s. It certifies no
statement or axiom audit. The mathematical rung is analytic proof with
exact finite validation, pending independent review, not Lean-checked.
