# C0097 — 2026-10-12

## Exact problem and scope

For nearest-neighbour strictly self-avoiding walks starting at 0 in Z^d,
let c_n(d) be their number and mu(d)=lim c_n(d)^(1/n). Put x=1/(2d).
The unique all-orders asymptotic Laurent series is
mu(d) ~ x^(-1)+sum_{j>=0} a_j x^j.
The problem is to prove that its regular tail has radius zero, equivalently
limsup_{j->infinity}|a_j|^(1/j)=infinity. The leading Laurent term does not
affect this question. No proof or counterexample to this statement is obtained here.

The folder was initially empty. The earlier intake attempt and the recorded
2026-10-10 report were read without changing their repositories. They establish
an information obstruction, not divergence: finite prefixes and factorial upper
bounds cannot exclude a convergent continuation. This report supplies a different
partial result and an explicit finite coefficient reduction.

## Proposition 1: every fixed finite-memory model has positive convergence radius

Fix an integer tau>=1. A memory-tau walk forbids omega_i=omega_j only when
0<|i-j|<=tau. Write mu_tau(d) for its connective constant. There exists a
complex analytic germ L_tau(x) at zero, with L_tau(0)=1, such that for every
sufficiently large integer d,

    mu_tau(d)/(2d) = L_tau(1/(2d)).

Consequently both the regular part of the Laurent expansion of mu_tau and the
power-series expansion of 1/mu_tau have strictly positive convergence radius.
This is a finite-memory result; it does not assert a radius uniform in tau.

Proof. Retain the last tau increments as a state. Within such a window the
increments form a strictly self-avoiding path, since every pair of times in a
window of length tau is separated by at most tau. Identify states under coordinate
permutations and independent changes of sign of coordinates. A canonical state is
a word of length tau in signed coordinate labels: the first appearance of a label
is positive, and labels are numbered in their order of first appearance. There
are finitely many states, say m, independent of d once d>=tau+1. Each uses
k<=tau coordinates.

Appending a step in a coordinate absent from the state is always legal: all
positions in the old window have the same component in that coordinate, and the
new endpoint has a different component. All 2(d-k) such steps give the same
canonical successor F(state), after forgetting the oldest increment. Appending
a step in one of the k used coordinates gives at most 2k possibilities. Whether
such a step is legal depends only on the state: it is legal exactly when the new
window of tau increments is self-avoiding. The omitted oldest vertex is at time
separation tau+1 from the new endpoint and must not be checked. Coordinates used
earlier than the retained window impose no restriction in the memory model.

Thus the orbit transition-count matrix is

    A_tau(d) = (2d) N + B,

where N_{s,F(s)}=1 and all other entries in row s of N are zero. The integer
matrix B has a contribution -2k at F(s), together with the counts of legal
steps in the used coordinates. For integers d>=tau+1, A_tau(d) is nonnegative
and counts extensions of every concrete representative of a state exactly.
There is no division by orbit size: each entry is the number of possible NEXT
steps from ONE representative, and equivariance makes this count independent of
the representative.

After tau successive applications of F, every retained increment uses a distinct
coordinate. Hence F^tau(s)=s_* for all s, where s_*=(1,2,...,tau), and F(s_*)=s_*.
It follows that N^tau=J, where J has its only nonzero column at s_* and that
column consists of ones. We have NJ=JN=J and J^2=J. Over C^m, the direct sum
im(J) plus ker(J) is invariant under N. On im(J), N is the identity; on ker(J),
N^tau=0. Therefore

    det(lambda I-N)=(lambda-1) lambda^(m-1).

In particular lambda=1 is a simple eigenvalue. The polynomial
p(x,lambda)=det(lambda I-N-xB) has p(0,1)=0 and partial derivative in lambda
equal to 1 at (0,1). The analytic implicit-function theorem gives an analytic
root L_tau(x) with L_tau(0)=1 on a disc of some radius r_tau>0.

We next verify that this root is the counting growth rate. All other roots of
p approach 0 as x approaches 0, by continuity of the multiset of roots of a
monic polynomial. For real x>0 sufficiently small, the root near 1 is real
(complex conjugation and uniqueness), positive, and has larger modulus than
all other roots. The nonnegative matrix N+xB therefore has spectral radius
L_tau(x). This also follows from Perron-Frobenius; irreducibility is not needed.

Every state is realized by some initial tau-step path when d>=tau+1. Let v_s(d)
be the positive number of concrete initial paths of state s. For n>=tau,

    c_n^(tau)(d) = v(d)^T A_tau(d)^(n-tau) 1.

If v_min and v_max are the minimum and maximum entries of v, this number lies
between v_min and v_max times the sum of all entries of A^(n-tau).
For a nonnegative m by m matrix M, its entry sum lies between its induced
infinity norm and m times that norm. The spectral-radius formula for matrix
powers gives lim ||A^q||_infinity^(1/q)=rho(A). Thus the displayed path count
has nth-root limit rho(A); shifting the exponent by fixed tau does not change
the limit. Consequently mu_tau(d)=(2d)L_tau(x), as asserted.

Finally, L_tau is nonzero in a smaller disc, so L_tau^{-1} is analytic there.
The reciprocal critical-point germ is x/L_tau(x), and the Laurent connective
constant germ is L_tau(x)/x. Both have positive convergence radius. QED.

## Proposition 2: reciprocal reformulation and a finite coefficient obstruction

Let A(x)=x mu_formal(x), so A(0)=1, and let H(x)=zc_formal(x)/x.
These are formal power series and H=A^{-1}. A has positive convergence radius
if and only if H does. Indeed, if one converges near zero its sum is analytic
and nonzero at zero; its analytic reciprocal exists on a smaller disc. The
Taylor series of that reciprocal is the unique formal inverse, since solving
the coefficient equations of a product equal to 1 determines each coefficient
recursively. Apply this argument in both directions. Multiplication or division
by x merely shifts the coefficients and preserves positivity of the radius.
Therefore C0097 is equivalent to zero radius for the reciprocal series.
This is a qualitative equivalence; it does not assert equality of positive radii.

Graham's equation (3.2), pp. 4-5, is

    H(x) = 1 + sum_{b>=1} sum_{a=b+1}^{2b} c_{a,b} x^b H(x)^a.             (R)

Here c_{a,b} are SIGNED aggregates of lace classes, not nonnegative counts.
This equation is well-defined formally because each coefficient uses finitely
many indices. Write H=1+sum_{n>=1} h_n x^n. Taking the coefficient of x^n in
(R) gives the exact triangular recurrence

    h_n = S_n + R_n,
    S_n = sum_{a=n+1}^{2n} c_{a,n},
    R_n = sum_{b=1}^{n-1} sum_{a=b+1}^{2b} c_{a,b} [x^(n-b)] H^a.         (T)

Proof: indices b>n cannot contribute; when b=n the constant coefficient of
H^a is 1; when b<n only h_1,...,h_{n-b} occur. In particular the right hand
side depends only on h_1,...,h_{n-1} and the c_{a,b} with b<=n. This proves
uniqueness and a recursive construction of H. QED.

Graham's finite-memory coefficients c_{a,b} stabilize to the infinite-memory
ones once tau>=a (p. 4). By induction in (T), h_1,...,h_n therefore agree
for memory tau and infinite memory whenever tau>=2n. Equivalently the reciprocal
coefficients alpha_1,...,alpha_(n+1) agree. This is also the consequence of his
Lemma 3.3 stated on p. 4. Combining this with Proposition 1: every finite prefix
of the actual SAW expansion is shared by an actual finite-memory model with a
convergent expansion. This does not imply the infinite series converges.

A precise sufficient missing estimate is: for some c,K>0 and unbounded n,

    |S_n| - |R_n| >= c K^n n!.

Then the triangle inequality yields |h_n|>=cK^n n!, and the nth roots are
unbounded, since n!>=floor(n/2)^ceil(n/2). The root test and Proposition 2
prove C0097. Neither that domination estimate nor any other superexponential
lower bound for the actual h_n is proved here. Such domination is sufficient,
not necessary; it could fail even if the conjecture is true.

## Auxiliary paired-coordinate return counts: exact cancellation test

Consider 2n-step simple random walk returns using exactly n axes, once in each
sign on every axis. There are binomial(d,n)(2n)! such step sequences: choose
the axes and permute their 2n distinct signed steps. The normalized probability
is the polynomial

    Q_n(x)=(2n-1)!! x^n product_{j=0}^{n-1}(1-2j x).

Indeed binomial(d,n)=(d)_n/n!, and (2n)!/(2^n n!)=(2n-1)!!.
Define Q(x)=1+sum_{n>=1} Q_n(x) formally; every coefficient is a finite sum.
The diagonal contribution to [x^n]Q is (2n-1)!!, which has unbounded nth roots
because it is >=n!. But lower-length contributions need not have that sign.
For example

    [x^5]Q = 945 - 12*105 + 8*15 = -195.

The contribution of length 10 alone is +945; the complete coefficient is
negative. Thus even this positive class of genuine lattice paths does not
yield coefficientwise lower bounds from its diagonal factorial count.
For x=1/(2d), all Q_n(x) are nonnegative, and Q_n(x)=0 for n>d.
Positivity of the values at physical dimensions is distinct from positivity
of coefficients in x. No radius theorem for Q or the full random-walk Green
function is claimed. These are not SAW connective-constant coefficients.

## Referee checklist and computational checks

1. State sufficiency: retaining tau increments is enough; one must test the
   NEW tau-increment window, not all tau+1 increments. This avoids inadvertently
   enforcing memory tau+1. Concrete transition counts include all 2(d-k) unused
   coordinate steps even if a coordinate occurred outside the retained window.
2. No quotient-counting error: orbit states classify recent increments, but
   transition entries count actual next steps from a fixed representative.
3. Reachability: every listed state is a valid initial tau-step SAW and has
   positive initial weight for d>=tau+1. No irreducibility assumption is used.
4. Simple eigenvalue: the rank-one reset proves this exactly. Analytic roots
   cannot be inferred merely from existence of a finite transfer matrix; a
   multiple root could have a Puiseux expansion. The reset excludes that here.
5. Limit issue: the analytic radii r_tau are not bounded below uniformly in tau.
   No passage from the finite-memory germs to an analytic infinite-memory germ
   is justified by coefficient stabilization alone.
6. Signed sums: Graham's c_{a,b} include inclusion-exclusion and falling-factorial
   signs. Taking absolute values establishes upper bounds, never the needed
   lower bound. The paired-coordinate example tests this distinction exactly.
7. Literature status: inaccessible API searches are recorded as inaccessible,
   not as evidence of absence of later solutions. No paper satisfying the
   user's exact SOLVED_IN_LITERATURE criterion was found in the accessible search.

The reproducible exact experiment is memory_check.py. Its output is saved in
memory_results.json and paired_return_results.json. Formal algebra checks and
their outcomes are recorded separately in the final check log; they certify
only the displayed finite identities, not the full analytic argument.

Completed verification: the state counts for tau=1,...,6 are respectively
1, 2, 6, 23, 109, 595. Every state reaches the all-fresh state after tau fresh
steps. Exact symbolic characteristic polynomials were computed through tau=4.
For tau=1, L=1; for tau=2,3, L=1-x. For tau=4 the branch satisfies

    L^3+(2x-1)L^2+(2x^2-x)L-x^3=0,
    L=1-x-x^2+x^3+0*x^4+4*x^5+x^6+11*x^7+O(x^8).

An initial test mistakenly expected L=1-x for tau=1 as well. That assertion
failed, was corrected to L=1, and the complete experiment was rerun. Memory
one forbids no possible nearest-neighbour return and correctly equals SRW.
This was a boundary-case expectation error, not a change to the transition rule.

brute_check.py independently enumerated concrete visited-position paths for
d=4,tau=4,n=6 and matched the orbit transfer calculation: 128072 paths on each
side (brute_result.json). The tested dimension is slightly below the convenient
proof assumption d>=tau+1; for this finite check no state can use more than d
coordinates, and transitions to a fifth coordinate have multiplicity zero.

FiniteChecks.lean passed with exit code 0 in 58.66 seconds, using
`lake env lean ~/brain_workers/TRIO_1011/op/C0097/FiniteChecks.lean`
from ~/lean_verify. It checks the memory-four polynomial at x=0,
the exact x^5-divisible residual of L=1-x-x^2+x^3, and the -195 return identity.
It imports only Mathlib.Tactic.Ring and Mathlib.Tactic.NormNum, uses no sorry,
no native_decide, and does not formalize the combinatorial enumeration or
analytic perturbation theorem. The full output is lean_check.txt.

## Remaining gap

There is no lower bound showing limsup |h_n|^(1/n)=infinity for the signed
infinite-memory SAW coefficients. There is also no proof that the convergence
radii of the finite-memory germs approach zero in a way forcing such a bound;
even that radius statement alone would need a careful coefficient argument.
The proof above handles every fixed finite memory and explains a limit
obstruction, but leaves the stated infinite-memory divergence problem open.
