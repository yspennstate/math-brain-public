# Independent checks and attempted counterexamples

## The quadratic mass estimate by a second route

Write V=V_{4m}. Choose independent uniform vertices S,T of B_{4m},
independent of the edges. Conditional on a configuration, the probability
that S belongs to one of the R crossing components is W_m/V, and the
probability that S,T belong to the same such component is Q_m/V^2.
For nonnegative core masses s_1,...,s_R, the identity

    R sum_i s_i^2 - (sum_i s_i)^2
       = sum_{i<k} (s_i-s_k)^2 >= 0

proves the component inequality without using Cauchy–Schwarz on that
list. On G={J_m<=L}, it implies

    E[(W_m/V)^2 1_G] <= L E[Q_m/V^2]
                          <= L X(8m)/V.

Nonnegativity of the variance of (W_m/V)1_G then gives

    E[(W_m/V)1_G] <= sqrt(L X(8m)/V).

This independently reproduces the normalized good-event bound. The
one power of V in the denominator follows from pair sampling: the
pair-connectivity upper bound is V X(8m), divided by V^2. The count
appears as sqrt(L), rather than L or sqrt(E J_m).

For a uniform S=x, successful crossing on G^c requires the inner arm
to partial B_{7m}. This inner event has probability at most pi(3m),
independently of G^c. Averaging over x shows that the normalized
bad-event contribution is at most pi(3m)P(G^c). Adding both contributions
recovers PROOF.md (5).

## The recurrence by explicit summation

After j_0, replace q_{8^j} by its upper bound r/2 in (13). Iteration
gives, for j>j_0,

    f_j <= (r/2)^{j-j_0} f_{j_0}
              + A sum_{k=j_0}^{j-1} (r/2)^{j-1-k} r^k.

The sum equals

    r^{j-1} sum_{u=0}^{j-j_0-1} 2^{-u}
       <= 2 r^{j-1}.

Therefore

    f_j <= [f_{j_0} r^{-j_0} + 2A/r] r^j.

This agrees with the power obtained by induction in PROOF.md. It
also checks the factor 2A/r in the induction condition. No convergence
rate for q_{8^j} is needed: the finite initial segment is absorbed in
the constant. Merely having q_j bounded below the number 1 would not
suffice for all target exponents. A homogeneous recurrence with
q_j=8^{-b}, b<a-h, would retain the slower power n^{-b}.

## Geometry and constants

- The core radius is 4m. Core differences have norm at most 8m, so
  the pair sum is bounded by V_{4m}X(8m), with no restricted-path
  translation asserted.
- The inner stopping boundary is 7m. Its separation from every core
  vertex is at least 3m. All its internal edges have both endpoints
  of norm at most 7m.
- Annulus edges have both endpoints of norm at least 8m. Tangential
  edges on the annulus boundary therefore share no edge with the inner
  count. The gap is a full m, even when m=1.
- A center on the shell of radius 12m has its radius-2m box between
  norms 10m and 14m. The target boundary at 16m is at least 4m away
  from the center. This also follows by inspecting a coordinate of
  maximum absolute value, independently of the triangle inequalities.
- In d=3, the number of covering centers is
  25^3-23^3=15625-12167=3458. Partitioning by the first coordinate of
  absolute value 12 gives 2*25^2+2*23*25+2*23^2=1250+1150+1058=3458.
  This constant does not enter the exponent arithmetic.
- From a core vertex, a 20m arm reaches norm at least 16m. Since
  24m>=20m, monotonicity gives pi(24m)<=pi(20m), in the direction
  required by the recurrence. The factor 8 comes from 24m/(3m).
- For filling integer scales, 3*8^j<=n<24*8^j implies 8^j>n/24.
  Since a-h>0, this gives (8^j)^{-(a-h)}<=24^{a-h}n^{-(a-h)}.

## Exponents and second algebraic checks

The squared error in (12) has m power

    h+(s+h)-d = s-d+2h.

Its square root is m^{(s-d)/2+h}=m^{-a+h}. Alternatively, the
square root of the density X(8m)/V_{4m} contributes m^{-a+h/2},
and sqrt(L_m) contributes m^{h/2}, giving the same exponent.

The reverse arm estimate comes from
pi(n)^2 >= N^{s-d+o(1)} with log N/log n -> 1/t. Dividing the
negative logarithm by log n yields the upper bound (d-s)/(2t), not
its negative. Taking t to one gives a=(d-s)/2.

The volume-tail exponent is a/(d-a). Substitution gives
(d-s)/(d+s); independently, solving s=d-2a and delta=(d-a)/a
gives s=d(delta-1)/(delta+1), hence delta=(d+s)/(d-s).
As an exact consistency check, d=2 and s=43/24 give a=5/48 and
delta=91/5. These are algebraic checks, not computed percolation data.

## Failure cases examined

1. An annulus component can split inside a small covering box. This
   increases the possible small-box counts and does not invalidate the
   injection proving (3). Different annulus components cannot merge
   within a small box contained in the annulus.
2. Different annulus components can merge in the core or outside the
   annulus. The required inequality is R<=J_m, where R counts full-box
   components, so those mergers have the harmless direction.
3. A path can return to the core many times. Taking its last visit to
   partial B_{8m} before its outer endpoint gives a segment entirely
   within A_m. A first-visit argument would not suffice here.
4. J_m and W_m can be dependent, and {J_m>L} need not be increasing.
   The proof factors only U_m and the event {J_m>L}, using disjoint
   deterministic edge sets. No BK inequality is used.
5. Large rare values of K_m may dominate E K_m. No expectation bound
   is inferred from (P); the error depends only on the bad-event
   probability and an independent inner arm.
6. No exponent or bounded scale ratio for pi is assumed. The new
   recurrence proves the needed power upper bound from X alone.
   Good-scale extraction from an already existing arm exponent is
   not used in the new reverse proof.
7. The lower bound on pi requires subtracting at distinct power scales.
   At a fixed ratio, an X logarithmic exponent need not ensure
   X(N)-X(3n) is a positive fixed fraction of X(N).
8. The limits fix h>0 and t<1 before n tends to infinity. Afterwards
   h tends to zero and t to one. Thresholds need not be uniform in
   these parameters.
9. The endpoints s=0 and s=d are excluded. The former loses the
   subtraction gap; the latter gives a=0 and loses the positive
   contraction exponent. No endpoint theorem is asserted.
10. Wiring the boundary can connect core vertices without genuine open
    paths and would invalidate the pair estimate. All finite graphs
    retain free boundary conditions.
11. The proof establishes an averaged-to-arm transfer under (P), not
    existence of either input at criticality on Z^3. The volume-tail
    consequence is conditional as well.

No invalid step was found. All displayed arithmetic is exact and was
checked by the separate derivations above. No numerical program was run.
