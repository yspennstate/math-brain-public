# Deterministic work

Here `m=M`, `n=2m-1`, `L=max_i ||a_i||`, `G=A^T A`, and all rows are real. These deductions do not prove the exponential conjecture. The polynomial estimates below are established literature; no novelty is claimed for them.

## Distance and determinant identities

For `T` of size `m-1`, let `v_T=det(A_T A_T^T)>0`, let `H_T` be its span, and put `d(T,k)=dist(a_k,H_T)`, `k` outside `T`. A unit normal to `H_T` gives

    sigma_min(A_{T union {k}}) <= d(T,k).

The Gram determinant/Schur complement gives

    v_T d(T,k)^2 = det(A_{T union {k}})^2.

Writing `D=sum_|S|=m det(A_S)^2` and `V=sum_|T|=m-1 v_T`, Cauchy–Binet and its penultimate coefficient imply

    D=det(G),      V=e_{m-1}(G)=det(G) tr(G^{-1}).

Sample `T` with probability `v_T/V`, then sample `k` uniformly from its `m`-element complement. Each `m`-subset occurs `m` times in the numerator, so

    E d(T,k)^2 = D/V = 1/tr(G^{-1}) <= tr(G)/m^2 <= n L^2/m^2.

Thus this average certifies `omega(A) <= L sqrt(2m-1)/m`, a polynomial estimate weaker than the already known `L/sqrt(m)`. For a unit-norm tight frame equality holds in the last two steps, so simply imposing tightness does not turn this expectation into an exponential quantity. This only diagnoses this particular average; it does not rule out a different weighting or a tail argument.

For a square invertible matrix, the negative second moment identity also gives

    sigma_min(B) <= min_i dist(b_i,span(other rows)) <= sqrt(m) sigma_min(B).

The determinant argument supplies

    min_S |det(A_S)| <= ((n/m)^m / binom(n,m))^(1/2) L^m.

Taking an m-th root only gives a constant times `L`, asymptotically `L/sqrt(2)`. The inequality needed to divide out the other `m-1` singular values requires a LOWER bound for their product. Row-norm control gives an upper bound for that product, which has the wrong direction. A small product can be distributed across many singular values.

## Projection induction

Fix a row `a_i`, project the other rows orthogonally onto `a_i^perp`, and discard one other row. The resulting `(2m-3)`-by-`(m-1)` matrix `B` is full spark: a dependence of projected rows would make those rows together with `a_i` dependent. For any selected `m-1` projected rows, use a unit vector in `a_i^perp` in the variational formula. It follows that

    omega(A) <= omega(B),       max_j ||b_j|| <= L.

There is no uniform contraction of the maximum projected row norm in this argument. Iteration alone yields no exponential factor. Near-orthogonal rows retain nearly their original lengths after one projection.

## Plücker relations and circuit ratios

For a fixed ordered `(m-2)`-set `I` and four distinct indices outside it, oriented minors obey

    p_{Iij} p_{Ikl} - p_{Iik} p_{Ijl} + p_{Iil} p_{Ijk} = 0.

Because the minors are nonzero real numbers, the largest absolute product is the sum of the other two absolute products. Therefore the six minors cannot all have the same absolute magnitude. This local relation only forces a constant separation; no chain yielding an exponential neighboring-minor ratio was found. Treating each relation's gain as an independent multiplicative improvement would be unjustified.

A useful exact formulation is the circuit imbalance. Define

    kappa(A) = max_{|S|=m, j outside S, i in S}
                  | (a_j A_S^{-1})_i |.

Equivalently, it is the largest ratio of absolute coefficients in any minimal dependence among `m+1` rows, or the largest ratio of two maximal minors differing by one row. It is unchanged by invertible right multiplication of `A`. Cramer's rule verifies all three descriptions. In particular `kappa >= 1`.

For any full-spark `A`,

    omega(A) <= L/kappa(A).                                      (1)

Indeed take a circuit coefficient of largest-to-smallest ratio `kappa`, omit the row with the smallest coefficient, and apply the remaining coefficient vector to the transpose of that square submatrix. Its norm is at least the largest coefficient, whereas its image has norm at most `L` times the omitted coefficient.

If `B^T B=I`, the reverse estimate up to a polynomial factor is

    omega(B) >= 1/sqrt(m + m(m-1) kappa(B)^2).                    (2)

For a square subset `S`, `B B_S^{-1}` has identity rows on `S` and `(m-1)m` other entries of absolute value at most `kappa`. Isometry of `B` gives

    ||B_S^{-1}||_2 <= ||B_S^{-1}||_F
                     = ||B B_S^{-1}||_F
                     <= sqrt(m+m(m-1)kappa^2).

This proves (2). Whitening `A` produces such a `B` without changing its circuits. Its maximum row norm is at most 1. Consequently a universal exponential lower bound for circuit imbalance of real representations of `U_{m,2m-1}` would imply Conjecture 20 by (1). Conversely Conjecture 20 applied to `B`, together with (2), would force an exponential lower bound on this circuit imbalance, with a polynomial loss. This reformulation moves the missing step into an explicit extremal question; it does not answer it.

The 2025 excluded-line-minor theorem of Dadush et al. was checked after identifying this formulation. Its general column bound is `n <= pi d^4 kappa` (Theorem 1.1, p. 3); at `n=2d-1` this does not imply exponential imbalance. Its rank-two minor method gives polynomial information. Bondar–Vavasis (2026) proves exponential imbalance for a particular LP construction, not for all representations of this uniform matroid.

## Known polynomial bounds, with a self-contained rederivation

The `L/sqrt(m)` proof from Balan–Wang is obtained from any `m+1` rows and a null relation: omit a coefficient of minimum magnitude. The retained coefficient norm is at least `sqrt(m)` times the omitted magnitude. This is sharp when there are only `m+1` rows, by a regular simplex.

A stronger `O(L m^{-3/2})` estimate is already in Liu–Wang (2016), Lemma 2.4, for `m+2` rows, hence applies to the current problem for `m>=3`. Here is an explicit-constant derivation, retained as verification of an old result.

Take any `r=m+2` rows and an `r`-by-2 orthonormal basis `U` of their transpose kernel. Since the sum of squared row norms of `U` is 2, at least `q=ceil(r/2)` rows have norm at most `2/sqrt(r)`. Among their unoriented lines in the plane, two have angle at most `pi/q`. For the two-row matrix `U_R`, use a unit direction perpendicular to the bisector of these lines. This gives

    s = sigma_min(U_R) <= 2 sqrt(2/r) sin(pi/(2q))
                         <= sqrt(2/r) pi/q.

Choose a unit coefficient vector `t` attaining `s`, and set `z=Ut`. On `S=[r]\R`, `||z_S||=sqrt(1-s^2)` and

    A_S^T z_S = - A_R^T z_R.

Hence

    sigma_min(A_S) <= sqrt(2) L s/sqrt(1-s^2).

For `r>=5`, one has `s<=sqrt(2/5)`, so a sufficient explicit bound is

    omega(A) <= (4 pi sqrt(5/3)) L / (m+2)^(3/2).

The planar angle argument is also valid if a row of `U` vanishes: then the minimum is zero directly. Full spark excludes this in the relevant configurations. This bound is not classified as a new partial solution.

## Structured examples

The real harmonic frames used numerically are unit-norm tight and full spark: use consecutive Fourier frequencies, with a unitary change to cosine/sine pairs; half-integer centered frequencies handle even `m`. Any square row block is a Vandermonde matrix at distinct roots of unity, up to nonsingular diagonal and unitary factors.

These examples have an elementary exponential upper bound. Center `m` consecutive sample angles about zero, put `r=m-1`, and evaluate `(z-1)^r`. On these angles `|z-1| <= sqrt(2)`. The coefficient norm is `sqrt(binom(2r,r)) >= 2^r/sqrt(2r+1)`. The normalized evaluation matrix has factor `1/sqrt(m)`, canceling the square root of the number of sample rows. Thus

    omega(H_m) <= sqrt(2m-1) 2^{-(m-1)/2}.

The centered polynomial has real cosine/sine coordinates after multiplication by a constant phase (even `r`: cosine; odd `r`: sine), so this test vector is valid for the real frame. This is an illustration, not a claimed new structure-specific theorem: Fourier submatrix exponential ill-conditioning is already established, with sharper rates, in the literature.

No proof under the proposed additional condition-number or unit-norm-tight hypotheses, beyond established polynomial bounds, was obtained. No counterexample family with a proved subexponential lower bound was obtained.
