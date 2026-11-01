# Keep queue failure mass through every restriction

This is a supplied-reference transport theorem, not a universal root-cost
bound. It extends A014 DERIVATION.md(9)--(11), which assumes a normalized
nonempty reference, to a strict subprobability such as an actual forest
queue with failed/infinite runs. Logs are base two.

Let f be ANY sign Boolean function on a finite uniform cube, p its squared
Walsh spectrum, v=1-p(empty). Fix q(A)>0 for EVERY nonempty A, with
z=sum q(A)<=1. No dependence on a later restriction outcome is permitted.
Define the full supplied-reference cost

    C(f;q)=h2(v)+sum_(A!=empty) p(A) log(1/q(A)).             (1)

This is the cross-entropy of the subprobability with empty mass1-v and
nonempty masses v q(A). For v=0 it is zero. For a queried i put
w=p({i}), V=v-w. For nonempty T avoiding i define

    q_i(T)=[q(T)+q(T+i)]/[1-q({i})].                        (2)

For dimension>=2, positivity makes q({i})<1. This is a subprobability:
sum_T q_i(T)=(z-q({i}))/(1-q({i}))<=1. Its missing mass is
(1-z)/(1-q({i})); missing queue runs have NOT been normalized away.
The SAME q_i is supplied to both physical restrictions f_+,f_-.

Write a_T=fhat(T), b_T=fhat(T+i), so the two child coefficients are a_T+b_T
and a_T-b_T. Consequently their average squared coefficient is
g(T)=p(T)+p(T+i), and their average nonempty mass is V. All child costs in
the following identity are full costs, including their actual binary
empty/nonempty wrappers:

    Delta_i=C(f;q)-[C(f_+;q_i)+C(f_-;q_i)]/2
       = h2(v)-[h2(v_+)+h2(v_-)]/2
          + w log(1/q({i}))+V log(1/(1-q({i})))+R_i,        (3)

where the ORIGINAL conditional phase cost is

    R_i=sum_(T!=empty) [p(T) log((q(T)+q(T+i))/q(T))
                      +p(T+i) log((q(T)+q(T+i))/q(T+i))]>=0. (4)

Derive (3) by splitting each original q(T) into its pair total times its
original within-pair fraction. Then factor the pair total as
(1-q({i}))q_i(T). No replacement by the spectrum, new prime table,
symmetrization, or renewed influence reserve occurs.

For an explicit nonnegative decomposition, when v>0 let alpha=w/v. Set

    G=H(1-v,w,V)-h2(V)>=0,
    J=h2(V)-[h2(v_+)+h2(v_-)]/2>=0.

The first inequality is entropy under coarsening of the three categories;
the second is binary-entropy concavity, using (v_++v_-)/2=V. Equation(3)
becomes exactly

    Delta_i=G+J+v KL_bits(Ber(alpha)||Ber(q({i})))+R_i>=0.   (5)

Zero spectral masses use 0log0=0. If v=0 all terms vanish. If V=0 the
children are constant; if n=1 handle those children directly without (2).
Thus every denominator used is positive. This proves the all-dimensional
theorem for every such q, including strict subprobabilities.

## One original queue through arbitrary adaptive histories

For queried coordinate set D put e_D=sum_(nonempty B subset D)q(B). On a
nonempty surviving set A define

    q_D(A)=sum_(B subset D)q(A union B)/(1-e_D).             (6)

If unqueried coordinates remain, 1-e_D>0 by positivity. The surviving total
is (z-e_D)/(1-e_D), and its missing mass is (1-z)/(1-e_D). Sequential use of
(2) gives EXACTLY(6), by cancellation of the denominators; hence it is
independent of query order and observed input values, conditional on D.
It is the projection of the ORIGINAL reference conditioned on not having
an erased nonempty output; the cemetery outcome remains. It is not the
sampler rebuilt from the restricted function's prime table.

For every finite adaptive restriction tree and every stopping cut,

    sum_internal reach(h) Delta_h
       +sum_leaves reach(h) C(f_h;q_D(h))=C(f;q).            (7)

All summands are nonnegative. Every old debit is retained and every full
terminal is retained. Constant leaves cost zero; a fully queried leaf needs
no q_D. The equality follows by multiplying (3) by each actual reach and
telescoping. No child bank is reset. Delta is a full supplied-reference cost
decrease; it is NOT claimed equal to true Fourier entropy decrement or any
other application's inherited witness debit.

## Supplied paid queues from the current campaign

For A015 stage7's rare threshold products, its selected ACTUAL queue events
give positive q=Q_sel on all nonempty subsets, sum q<=1, C(f;q)<=107I(f).
This bound includes the entropy wrapper; it uses no source K_ref. Therefore
the entire account(7), for EVERY adaptive history/stopping cut, is <=107I(f)
at the SAME original reference, including r=0 and arbitrarily small core mass.
This application remains conditional on that author's pending-review root
certificate; the universal transport theorem itself does not depend on it.

For A008-CENTRAL-PRIME-COMPATIBLE-ROOT-AGGREGATION@1, the supplied q=Q_sel
has nonempty cost<=251I/5. On its family I>=1, so h2(v)<=1<=I and the full
account(7) is <=256I/5. A008's earlier optional261I/5 uses the general bound
h2(v)<=2I; the smaller256I/5 here uses I>=1 ONLY for that named family.
This is a wrapper refinement of a different quantity, not a revision of
A008's nonempty251I/5 bound.

## Necessary guard and precise frontier

The factor1-q({i}) is essential. For Maj3, choose q as a positive smoothed
multiple of its nonempty spectrum, retaining a cemetery atom. The exact
checker exhibits a negative cost decrease when (2)'s denominator is omitted,
while (3)--(5) hold. This is an actual Boolean fault control, not a relaxation.

The universal unpaid line is STILL existence of an original full reference
with C(f;q)<=K I(f) for every Boolean f. Transport cannot create that root
payment. Nor does it pay a genuinely different intermediate reference after
a reset: a new reference would need its full actual signed conversion bill
from the SAME unused bank. This theorem removes a failure-mass normalization
gap in carrying an already paid queue; it does not prove full FEI.
