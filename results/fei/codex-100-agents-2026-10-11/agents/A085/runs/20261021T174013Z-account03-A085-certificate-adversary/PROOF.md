# A small absolute reference error can spend a fixed amount

The exact A099 reset criterion survives this audit. Replacing it by an absolute total-variation tolerance fails, even for a matching cheap root reference with full support and two nonconstant physical children. The counterexample below concerns reference costs, not FEI.

All logarithms are base two. CE(P,Q) means sum P(s) log2(1/Q(s)); the zero-P convention is used. Total variation is half the L1 distance. Physical bits are encoded by integers, and character s at vertex x is (-1)^(popcount(s & x)).

## 1. An actual Boolean family with full support

For every integer n>=2, use n+1 coordinates (j,y1,...,yn), with j the least significant bit. Define F_n=-1 exactly at vertices 0,1,3, and +1 elsewhere. Put t=2^-n. The mean is 1-3t. Every nonempty Fourier coefficient is

    -t [1 + (-1)^s_j + (-1)^(s_j+s_y1)].

The bracket is 3,-1, or 1, never zero. The empty coefficient is also positive because t<=1/4. Thus the matching root reference Q=P_F has strictly positive mass on EVERY Fourier subset. It is normalized by Parseval.

Query physical j. The j=0 child g_n is -1 only at y=0. The j=1 child h_n is -1 only at y=0,e1. For n>=2 both are nonconstant. The two child functions differ only at e1, so the queried influence is exactly t. The three negative root vertices have two internal cube edges. Counting boundary edges gives

    I(F_n)=[3(n+1)-4]/2^n = (3n-1)t.

In particular I(F_n) tends to zero. This family is a tiny finite union of points, not an FEI counterfamily.

## 2. The complete inherited reference

Both children inherit the SAME q(T)=Q(T)+Q(T+j). Since the root is matching, this is exactly the mean of their true spectral laws. For the one-point child P=P_g,

    P(empty)=p0=(1-2t)^2,
    P(T)=p=4t^2 for T nonempty.

Write a={y1}. The two-point child has zero coefficient at a and mean 1-4t. Therefore

    q(empty)=q0=1-6t+10t^2,
    q(a)=q_a=2t^2.

All q atoms are strictly positive because the root Q has full support. In particular q0>=p0/2>0. These are spectral marginals; neither is a physical-outcome conditional law of Q. Both full terminal CE costs must be retained.

The root conditional occupancy refund is exactly zero: P_root=Q_root, so their conditional distributions agree in every occupied fiber. This is an exact fact, not subtraction of two approximate KL numbers. With A=H(F_n), executed erasure debit d=B_j(F_n), and full old expected terminal CE T, the exact identity gives A=d+T. Hence the genuinely unused original account U is zero. If a larger quota is supplied, U must be measured from that same account rather than renewed at a child.

## 3. A normalized, support-preserving reset

Let M=2^(2n-2), so p M=1. Reset ONLY g_n's terminal reference, leaving the h_n terminal and the already executed debit untouched. Set

    d_n=q_a(1-2^-M),
    qtilde(a)=q_a 2^-M,
    qtilde(empty)=q0+d_n,
    qtilde(T)=q(T) on all other atoms.

Every atom remains positive, the reference stays normalized, and

    TV(q,qtilde)=d_n < q_a = 2^(1-2n) -> 0.

The active child's exact complete reset cost is

    Delta_n=CE(P,qtilde)-CE(P,q)
           =p M-p0 log2(1+d_n/q0)
           =1-p0 log2(1+d_n/q0).

The query has fair physical outcomes, so the expected reset bill is Z_n=Delta_n/2. This sum includes the unchanged complementary terminal through its zero reset term.

At n=2, q0=q_a=1/8, p0=1/4, M=4 and d_n=15/128. Thus

    Z_2 = 1/2 - (1/8) log2(31/16) > 3/8,

where the strict sign follows from 31<32. The explicit three-dimensional truth table in increasing integer order is

    [-1,-1,+1,-1,+1,+1,+1,+1].

Its g child is [-1,+1,+1,+1], its h child is [-1,-1,+1,+1]. Three dimensions are minimal for the simultaneous full-root-support and two-nonconstant-children conditions: in dimension two, both children on the single remaining bit must be signed dictators. Consequently the parent is x times a one-bit Boolean sign of j, hence a signed monomial, whose spectrum cannot have full support. In dimension one both children are constant. This is a minimality statement for these explicit additional conditions, not for unrestricted reference obstructions.

For n>=3, use ln(1+x)<=x for x>=0 and ln 2>1/2 (integrate 1/u>1/2 on [1,2)). Since p0/q0<=2 and d_n<q_a,

    0 <= p0 log2(1+d_n/q0) < 4 q_a <= 1/8.

Thus Delta_n>7/8, and Z_n>7/16>3/8. Together with the separately checked n=2 endpoint,

    Z_n>3/8 for EVERY n>=2,
    Z_n / Inf_j(F_n) > (3/8) 2^n -> infinity.

The same estimate shows Delta_n->1 and Z_n->1/2. No continuity of a quotient at zero influence is used.

## 4. The root is already inexpensive

The nonempty root masses are t^2 or 9t^2; the total nonempty mass is 6t-9t^2. Hence their entropy is at most 2n(6t-9t^2)<=12nt. For z=(1-3t)^2, the scalar inequality -z ln z<=1-z and ln 2>1/2 give empty-atom entropy <=2(1-z)<=12t. Therefore

    H(F_n)<=12(n+1)t<=8(3n-1)t=8 I(F_n), n>=2.

All denominators are positive. At n=2 the final comparison is 36<=40; after clearing constants it is 20<=12n. Consequently the construction begins with a matching complete reference at an absolute influence price. It is not exploiting an unpaid expensive source.

After the reset, the erasure-plus-complete-terminal cost is A+Z_n. The exactly paid A-account overspends by Z_n. More strongly, for any fixed K, K I(F_n)->0 while the new total cost is at least Z_n>3/8. Thus no fixed original influence quota can authorize ALL sufficiently small absolute-TV resets of this kind. For each fixed tolerance epsilon>0, sufficiently large n has TV(q,qtilde)<epsilon and still requires more than 3/8 bit.

This refutes only a proposed replacement of an exact cost test by absolute reference proximity. Neither A096 nor A099 asserts that replacement. Their exact criterion rejects this reset and is confirmed rather than contradicted. There is no statement that a useful permitted reset must choose this adverse qtilde.

## 5. The exact criterion and a safe numerical replacement

For any finite adaptive physical tree, supplied finite root CE, and complete references inherited by marginalizing queried spectral coordinates, actual signed child laws average to that spectral marginal. Disintegrating conditional cross entropy gives

    CE_root = sum_u w_u (B_u+R_u) + sum_l w_l CE_l,

with physical reach weights w_u=2^-depth and R_u the conditional occupancy KL. Q may have extra support; occupied true fibers always have positive reference marginal. Zero true fibers contribute zero. Reference-only atoms remain in the normalizers. R_u>=0 follows from ln x<=x-1, without deleting any such atoms. Each node has a fresh coordinate, so finite dimension bounds the depth. There is no sum-limit exchange, numerical cutoff, or unstated infinite-tree extension here.

Given an actual ancestor quota A, executed debit d, stopped terminal cost T and U=A-d-T, further no-reset queries satisfy T=b+r+T'. A prescribed reset adds signed complete cost Z. Substitution gives the exact balance

    A-(d+b)-(T'+Z)=U+r-Z.

Thus the specified erasure-and-terminal account admits the reset exactly when Z<=U+r. Additional channel or label bills must be subtracted too. A099 NR1, NR2 and RS1--RS2 HOLD at this elementary stated scope. This is a review of those clauses, not acceptance of its entire assembled FEI chain or the separate A097 source-floor price.

A useful sufficient certificate is multiplicative: if for every occupied true atom qtilde(s)>=(1-eta)q(s), with 0<=eta<1, then

    CE(P,qtilde)-CE(P,q)<=-log2(1-eta).

This is termwise monotonicity of the log followed by sum P=1. With several terminals use their physical reach weights and their actual eta_l. Add that upper bound to every other required bill and compare to U+r. It is dimension-independent; an absolute-TV error alone has no such guarantee without an atom floor or a weighted logarithmic bound. The counterfamily has qtilde(a)/q(a)=2^-M, so its relative error is not small. That is the failed condition.

## 6. Checks and the remaining universal line

The frozen finite domains are n=2,...,7, separately piloted at n=2,3, for the original spectator fixture and the strengthened full-support fixture. Independent direct character sums and the integer FWHT agree on every root and child coefficient. Physical edge counts verify both total and queried influence. Fraction arithmetic checks normalization, support, total variation, exact unchanged atoms and the root/terminal identities. Logs use outward dyadic arithmetic with a positive proved atanh remainder; the finite signs are not binary64 signs. The all-n theorem follows from Sections 1--4, not from six samples.

The key algebraic comparison after bounding the logarithmic gain is submitted separately to core Lean. That check covers only an integer-scaled inequality, not Fourier analysis, logarithms or FEI. Its exact receipt determines the reported rung. The mathematical claim above is an analytic proof with exact finite verification, awaiting independent review.

The first unpaid universal line is to choose useful reset references with a genuinely affordable signed log-likelihood bill from ONE unused ancestor account, including prior debits, complementary full terminals and any channel costs. A certificate needs this weighted likelihood or relative-error control; additional finite dimensions or smaller absolute tolerances cannot replace it.
