SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B01, 2026-09-23T02:32:06Z.
attacking: a random physical cut that turns global disjoint 3-volume into an admissible averaged-frequency three-volume certificate before reciprocal-minor losses, with a bounded hub alternative.

# Early substantive checkpoint

Let

Z_disj(A) = sum det(A[S,T])^2

over ordered disjoint triples S,T of original coordinates.  Let R_i be the same sum restricted to i in S, so sum_i R_i = 3 Z_disj.

Fix theta in (0,1].  Put eta=theta/96 and H={i:R_i>eta Z_disj}; then |H|<288/theta.  Let Z_0 be the disjoint-minor mass with S cap H empty.  If Z_0>=theta Z_disj, force H onto the J side and independently toss every other original coordinate into I/J with probability 1/2.  Every eligible disjoint pair (S,T) lands as S subset I,T subset J with probability at least 2^-6.  Hence some cut satisfies

E3(A[I,J]) >= theta Z_disj/64.

For every row i in I, the actual third-volume row-marginal numerator of this cut is <=R_i<=eta Z_disj, hence its normalized marginal is <=64 eta/theta=2/3.  Therefore the current q=4/3 fractional three-volume Fourier theorem applies to this actual original-coordinate cross block and gives

||p_Q||_inf <= (9 sqrt(3)e/2) (64/(theta Z_disj))^(1/6).

At theta=1/2 this is <47.564 Z_disj^(-1/6), unless more than half of all disjoint three-volume has its ROW triple meeting a set H of at most 576 original coordinates.

This is a genuine aggregate-before-inversion split: no individual minor is selected and no law-uniform pointwise quadratic-phase estimate is used.  Remaining work this run: write the full proof with Cauchy--Binet identification of E3, verify arbitrary self-block/outside-affine scope from the source theorem, apply fleet04/B01 signed-Fejer to the resulting density inequality, and state exactly what the bounded-hub alternative does and does not pay in N3.
