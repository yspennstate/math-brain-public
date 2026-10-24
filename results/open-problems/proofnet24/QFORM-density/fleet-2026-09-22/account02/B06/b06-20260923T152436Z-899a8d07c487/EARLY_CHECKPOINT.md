SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B06, 2026-09-23T15:24:36Z.
attacking: partner r38 recursive rank-two cross tube: derive a tail-retaining weighted reciprocal receiver on an exact physical null bank, then identify why nonzero self-curvature must consume the third large direction.

# Early substantive checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full conjecture remains OPEN.

## Candidate theorem already reduced to one explicit integral

Let the ORIGINAL coordinates be partitioned into independent product banks I,J. Assume the physical principal block on J is exactly null, A_JJ=0. Write M=A_IJ and let s1>=s2>0 be its two largest singular values. All curvature on the I bank is arbitrary, as are all affine terms. Then the expected bound is

  ||p_Q||_infinity <= 2 sqrt(pi) / sqrt(s1 s2).

Reason: condition on X_I=x. The J-bank is then a single linear form with coefficient c(x)=2M^T x+b_J. The completed product-projection inequality from the pinned newest-Claude package gives the conditional density cap sqrt(2)/||c(x)||. If u1,u2 and v1,v2 are the first two singular directions of M and U=(u1.X_I,u2.X_I), then the same source gives ||p_U||_infinity<=2. Project c(x) to span(v1,v2):

  ||c(x)|| >= |(2s1 U1+d1, 2s2 U2+d2)|.

The displayed two-vector has density cap K=1/(2s1s2). The remaining step is the exact two-dimensional bathtub identity

  sup_{h<=K, integral h=1} integral h(z)/|z-z0| dz = 2 sqrt(pi K),

attained by the saturated disk centered at z0. Hence

  E ||c(X_I)||^{-1} <= sqrt(2pi/(s1s2)),

and averaging the conditional linear-form cap gives 2sqrt(pi)/sqrt(s1s2).

This keeps the entire cross matrix M, including every small nonzero tail singular direction: only a lower bound from its top two singular directions is used. No spectral-coordinate independence and no fiber supremum is invoked.

## Immediate partner application if proof closes

Partner account03/B06 r38 inherits the r37 N3 near-rank-two chamber for the literal ORIGINAL-coordinate cross cut N, where E=||N||_F^2>11907/16384 and s2(N)^2>=E/64. Therefore, if either same-bank principal block on that physical partition is exactly null, the theorem would give

  ||p_Q||_infinity <= 16sqrt(pi)/sqrt(E)
                    < 2048sqrt(pi)/sqrt(11907)
                    = 33.2662396488... .

This would pay that whole null-bank subbranch before the r38 cofactor split and, in particular, retain the full small cross tail in the recursive rank-two tube.

## Boundary obstruction to the naive perturbative extension

The exact-null hypothesis cannot simply be replaced by a small self-block while discarding the third spectral direction. For any 0<delta<=1, with independent cap-one symmetric uniforms x1,x2,y1,y2,

  q_delta = delta(y1^2-y2^2)+2x1y1+2x2y2+delta^{-1}(x1^2-x2^2)
          = delta^{-1}(x1+delta y1)^2-delta^{-1}(x2+delta y2)^2.

The cross block is the 2x2 identity and the y-self block has operator norm delta, yet q_delta has a logarithmically unbounded density at zero. Its matrix has only two nonzero eigenvalues, so this is a counterexample to the perturbative receiver, NOT to QFORM. It shows why the third large direction has to be consumed rather than treating nonzero same-bank curvature as a small random error.
