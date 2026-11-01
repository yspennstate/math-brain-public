# Prime gates can approach a zero-reserve boundary

All logarithms are natural. Physical inputs are independent signs with
Pr(X_i=+1)=p_i. Put v_i=4p_i(1-p_i), and expand f in the centered product
basis with coefficients c_S, so P(S)=v_S c_S^2. This is the actual normalized
Boolean Fourier law. Set Delta=sum_(S nonempty)(|S|-1)P(S),
R=sum_(|S|>=3)(|S|-2)P(S), J1=ln4 sum_i P(i)j_i, and
Jhi=ln4 sum_(|S|>=2)P(S)j_S. On occupied coefficients use the unique
upper dyadic convention 1/2<2^j |c_S|<=1. L1=sum_i P(i)ln(1/u_i^2),
and Bstar=ln4(2Delta-R)-J1-ln2 L1. Zero coefficients contribute zero.

## 1. Independent reconstruction of A044's new statement

Reviewed source: A044-SHARP-RESERVE-EQUALITY-AND-SUPPLIER-OBSTRUCTION@1,
statement hash b5994d2b1e43e28fe80c303b72b2d28878d5c922fdd5bde46d354407a901f38c,
PROOF.md hash 9483b602160d6d3b957c1432816cdf92b3836021b9cf783a87515d33e4753a77.
The new equality/classification/account obstruction HOLDS at its stated scope.
This review does not count as independent acceptance of A045's own earlier
dependency. The source does not assert a universal supplier.

Here is a separate reconstruction of its critical step. For D_i=(f_+-f_-)/2,
let t=|ED_i| and d=ED_i^2. Because D_i is in {-1,0,1}, d>=t; equality
means one sign on its support. For x=1/t in [2^j,2^(j+1)),
F(x)=x-1-j-ln(x/2^j) has derivative 1-1/x>=0. Its left value is
2^j-1-j>=0, zero only for j=0,1. Strict increase away from x=1 implies
the scalar equality only at t=1 or1/2. The exact reserve decomposition is

    Bstar/ln4 = sum_i v_i[(d_i-t_i)+t_i(1-t_i)
                         -t_i^2(j_i+ln(1/u_i))].            (1)

At t=0 the term is v_i d_i. Interior support and (1) prove the all-product
equality characterization: every coordinate is irrelevant, a literal, or
one-sign pivotal with d_i=t_i=1/2. If a coordinate is literal the whole
gate is that literal. No derivative admission is asserted for arbitrary
reference laws or spectrally conditioned laws.

At fair inputs, orient relevant coordinates positively. Every nonliteral
singleton coefficient is1/2. Parseval gives at most4 relevant coordinates;
equality at4 would force f=(x1+x2+x3+x4)/2, contradicting Booleanity.
With2 relevant coordinates monotonicity gives AND/OR. With3, every
direction has two crossing edges. The positive up-set has even size; sizes
2 and6 give only2 relevant coordinates. An up-set of size4 is either a
literal or the majority up-set. Thus the all-dimensional classification is
constants, literals, signed AND2, signed Maj3, with labelled count
2+2n+8 binom(n,2)+8 binom(n,3). This also independently proves the finite
equality predicate used by the integer checker.

Their local Jhi/Delta is at most ln4 (AND2 equality), and their corrected
entropy/Delta at most3ln4. The exact positive-weight genuine disjoint
composition identity telescopes the latter without a depth factor, under
the source's explicit fair-ACTUAL-input condition. The empty entropy term
is at most Var in nats, giving H_bits<=6I. A non-root AND2 cannot keep its
parent input fair. The source's AND2 obstruction, all-product AND_n
pivotal-half example, and Maj3 tower follow respectively from their direct
coefficients, c_S=2^(1-|S|)p^(n-|S|), and the finite weighted recurrences.
Both complete terminal reference laws and their ordinary KL stay in place;
these observations do not erase the positive singleton entropy slack.

## 2. An explicit prime boundary in every arity

For every fixed n>=3 put m=n-2. Let f=T_2^n be the sign that is+1 iff at
least two of its n physical inputs are+1. Use

    p1=p2=1/2, p3=...=pn=epsilon,
    0<epsilon<=1/(8m).                                  (2)

This gate is essential and PRIME under the disjoint Boolean-wire notion.
For any proposed proper block A with 2<=|A|<=n-1, choose block assignments
with0,1,2 positive inputs, and outside assignments with0 and1 positive
input. Restricted to these two columns its rows are (-,-),(-,+),(+,+).
They are three distinct rows. Factoring through a single Boolean wire
permits at most two distinct rows, impossible. This is an all-n argument,
not an inference from the finite module check. The finite pigeonhole step
has a separate core-Lean target in code/PrimeRows.lean.

Write K for the number of positive rare inputs, q_r=Pr(K=r), and
a=binom(m,2)epsilon^2. Monotonicity makes every D_i a0/1 variable, so d_i=t_i.
For the two fair coordinates,

    t1=t2=(q0+q1)/2 >= (1-a)/2,                         (3)
    c12=(q0-q1)/2 >= (1-2m epsilon)/2 >=3/8.             (4)

Equation(3) uses Pr(K>=2)<=binom(m,2)epsilon^2: union-bound the events
that a specified pair of rare bits is positive. Equation(4) uses
Pr(K>=1)<=m epsilon. Both t1,t2 and c12 are at most1/2 and exceed1/4,
so their scales are EXACTLY1, including the upper boundary1/2. Therefore

    Jhi >= ln4 P({1,2}) >=9ln4/64.                     (5)

For any rare coordinate, pivotality is
(1/2)Pr(K_other=0)+(1/4)Pr(K_other=1)<=1/2. Thus
I<=1+2m epsilon. The output mean lies between-1/2 and
-1/2+2Pr(K>=1)<=-1/4: activating rare inputs can only increase the
AND2 slice, with a sign change of at most2. Hence Var>=3/4 and

    Delta<=1/4+2m epsilon,
    J1/ln4>=2[(1-a)/2]^2 >=1/2-a.                     (6)

The second inequality discards other NONNEGATIVE singleton scale terms.
Since L1>=0 and ln2/ln4=1/2, the SAME original reserve obeys

    0 < (Bstar+ln4 R)/ln4
       =2Delta-J1/ln4-L1/2
       <=4m epsilon+a <=5m epsilon.                   (7)

The final inequality uses a<=(m epsilon)^2/2 and m epsilon<=1/8.
Strict positivity in(7) follows from R>0: the top coefficient of T_2^n is
(-1)^n(n-1)/2^(n-1), nonzero, and every retained v_i>0. Bstar>=0 follows
from(1). Combining(5)-(7) gives the exact all-parameter certificate

    Jhi/(Bstar+ln4 R) >=9/[320m epsilon] -> infinity.   (8)

It also refutes Jhi<=K Bstar. For every arity cutoff N and every finite
K>=0, choose any n>max(N,2) and a sufficiently small dyadic epsilon
satisfying(2) and9/[320m epsilon]>K. Thus deleting any fixed finite list
of prime gates, or all small-arity primes, cannot repair either supplier.
The constants in(5)-(8) are conservative certificates, not claimed sharp.

## 3. Admission and scope guards

Every positive epsilon in(2) is an actual interior PRODUCT physical law
of a fixed explicit Boolean prime gate, with disjoint distinct coordinates.
There is no repeated variable and no inverse admission problem. At
epsilon=0 the rare coordinates deterministically contract and the actual
gate is fair AND2; its masses are1/4 on empty,{1},{2},{1,2}. This endpoint
is used only as a physical boundary control, never as division by a zero
variance or as a spectral-conditioning substitution. At interior epsilon
the rare inputs are still present, so the AND2 endpoint does not supply
a proper Boolean-wire decomposition of the prime gate.

The divergence in(8) concerns a proposed DIMINISHED source, not H/I.
T_2^n is a symmetric threshold and is already covered by the supplied
product-biased threshold theorem. An exception that separately pays ALL
symmetric thresholds is NOT refuted here. Nor does(8) refute a supplier
restricted to a uniformly nondegenerate bias domain. No reference law is
changed: all normalizers, imported mantissas, genuine low/high carries,
positive S_tree, and BOTH full terminal KL costs remain with their original
owners. These gates demonstrate that a prime-only or finite-exception
argument cannot make the diminished reserve the whole high-sector owner.

## 4. Exact first unpaid universal step

An original high-sector payer must survive the degeneration in(2), with
actual core entropy retained after deterministic contraction. One possible
next interface is a complete rare-input/core transfer that separately
books the AND2 core bill and prices the perturbation from SAME unused
original influence, after all previous imports/carries and both full
terminals. No such universal payment is supplied here. Full FEI remains
OPEN. The new result closes an objection to the account obstruction,
not a restricted-class FEI theorem.
