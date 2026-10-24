SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-23T04:38:00Z.
attacking: balanced weak-direction separation: compare globally optimal admissible third-volume weights, one-scale ridge, and square-assisted half-Riesz smoothing on the same physical matrix.

# account02/B04 auto11 — balanced weak direction: volume vs ridge vs square smoothing

Programme: QFORM-DENSITY-3EIG-20260922. Full conjecture remains OPEN.
Execution status: WITHOUT_VERIFIED_BRAIN (authenticated repository retrieval occurred; no native learned-memory receiver/ingestion evidence was available).

## 1. Source boundary and first unpaid implication

Fresh brain control was resolved at `yspennstate/math-research-brain@a5ed45f708ca9e45d54d1fcdf2b1fd7456581844`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only, no slot pause.

Corrections consumed: no law-uniform pointwise quadratic-phase decay; no independence after spectral rotation; no arbitrary-joint rank-three coarea bound; no positive conditional projection-density moment; no worst-fiber supremum; no universally good fixed principal minor or rank-three cross cut. None is used below.

Required Claude/e5 sources were read at exact commit `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`: `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Theorem D is used at an actual inequality in Section 4.

The changed-mechanism obligation is not another near-coloop repair. It is:

`QFORM-BALANCED-WEAK-DIRECTION-ROUTING-v1`: when third-volume marginals are already perfectly admissible but the third cross singular direction is arbitrarily weak, determine whether an actual original-coordinate square can supply the missing fractional smoothing, and identify exactly what a pure ridge certificate still pays.

The remaining structural implication after this report is `QFORM-OUTER-SQUARE-PLUS-RANK2-OR-HUB-ROUTING-v1`: from the bare three-large-eigenvalue hypothesis, route every low-total-tail cut either to a quantitatively nonzero original scalar pivot whose Schur residual has two aggregate cross directions usable by square-assisted half-Riesz smoothing, or to a completed physical-pair/hub/grouped-bank mechanism. The zero/near-zero scalar-pivot branch remains unpaid.

## 2. A balanced physical cross block with one arbitrarily weak singular direction

Fix `0 < eps <= 1`. Let

`V=(1/7)*[[6,-2,-3],[-2,3,-6],[-3,-6,-2]]`.

Direct multiplication gives `V^T V=I_3` and `det V=-1`; every entry is nonzero.

Let `U` be the `10 x 3` matrix whose rows are

- rows 1,2: `(0,0,1/sqrt(2))`;
- rows 3,4,5,6: `(1/2,0,0)`;
- rows 7,8,9,10: `(0,1/2,0)`.

Then `U^T U=I_3`. Define

`M_eps = U diag(2,2,eps) V^T`.

Hence the singular values of `M_eps` are exactly `(2,2,eps)`. Every one of its 30 physical entries is nonzero: strong-bank rows are respectively the first or second row of `V^T`, while weak-bank rows are `eps/sqrt(2)` times the third row of `V^T`.

The row-space projection is `P=UU^T`; its diagonal is

`(1/2,1/2,1/4,1/4,1/4,1/4,1/4,1/4,1/4,1/4)`.

Thus the physical range leverage is already at the exact q=1 threshold; there is no near-coloop or heavy-row failure in this example.

## 3. Exact optimization of all admissible third-volume weights

There are exactly 32 nonzero `3 x 3` row minors because a nonzero minor must select one weak row, one first-strong-bank row, and one second-strong-bank row: `2*4*4=32` choices. For every such row triple `S`,

`|det (M_eps)_S| = (1/(4 sqrt(2))) * (2*2*eps) * |det V| = eps/sqrt(2)`.

Therefore every nonzero squared minor equals `eps^2/2`, and

`E_3(M_eps^T M_eps)=32*(eps^2/2)=16 eps^2`,

as also follows from the singular values.

The squared-minor Gibbs law `w_*` is uniform on the 32 nonzero minors. Its row marginals are exactly

`alpha_1=alpha_2=1/2`, and `alpha_i=1/4` for `i=3,...,10`.

So the original e5 Theorem D gate `max alpha_i <=1/2` is satisfied with equality.

More strongly, optimize over EVERY probability weight `w` supported on nonzero three-minors and satisfying the same marginal gate. The arbitrary-weight determinant functional appearing in e5 is

`G(w)=exp( sum_S w_S log det(M_S)^2 + H(w) )`.

All nonzero determinant squares are the same, hence

`G(w)=(eps^2/2) exp(H(w)) <= (eps^2/2)*32 =16 eps^2`,

with equality iff `w` is uniform. The uniform law is admissible, so it is the GLOBAL optimizer among all admissible weights; no KL/entropy reweighting can improve the volume scale at all.

This is qualitatively different from the preceding near-coloop families: the marginal problem is completely solved here, yet every third-volume certificate still pays the weak singular direction `eps`.

## 4. Required application of the completed e5 result

Apply Theorem D from exact source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` to the actual physical cut `M_eps`. Its conclusion is

`||p_R||_infinity <= 6 sqrt(e) E_3(M_eps^T M_eps)^(-1/6)`

for the full ambient quadratic form with arbitrary self blocks/outside couplings. Therefore

`boxed( ||p_R||_infinity <= 6 sqrt(e) 2^(-2/3) eps^(-1/3) )`

and the numerical coefficient is

`6 sqrt(e) 2^(-2/3) = 6.231775903093545...`.

Because Section 3 proved `G(w)<=16 eps^2` for every admissible weight, this is the BEST certificate obtainable from the e5 arbitrary-weight q=1 Theorem-D functional on this cut. The divergence `eps^(-1/3)` is thus not an artifact of a poor sampling law.

## 5. Target-valid genuinely rotated indefinite embedding

Let `Z`, the ten coordinates of `X`, and the three coordinates of `Y` be mutually independent original coordinates, each with an arbitrary probability density bounded by one. Set

`Q_eps = Z^2 + 2 X^T M_eps Y`.

Its symmetric coefficient matrix is the direct sum of `[1]` with the bipartite block `[[0,M_eps],[M_eps^T,0]]`. Its spectrum is therefore

`{1, 2,2,eps, -2,-2,-eps, 0,0,0,0,0,0,0}`

(counting the dimension-imbalance zeros). In particular at least five eigenvalues have modulus at least one for every `0<eps<=1`: `1,+2,+2,-2,-2`. The form is indefinite and physically rotated; every `X-Y` coefficient is nonzero.

The e5 inequality from Section 4 applies to the residual `2X^T M_eps Y`, and convolution with the independent `Z^2` cannot increase an existing L-infinity density bound. Thus it gives a target-valid but diverging estimate `6.2318 eps^(-1/3)` for this same family.

## 6. Pure one-scale ridge on the same physical block

Use the completed ridge theorem `QFORM-RIDGE-DENSITY-v1`, source `math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`. For `gamma>0`,

`K_gamma=M_eps M_eps^T (gamma^2 I + M_eps M_eps^T)^(-1)`.

Writing

`k=4/(4+gamma^2)`, `h=eps^2/(eps^2+gamma^2)`,

one has

`K_gamma=U diag(k,k,h) U^T`,

so every physical ridge leverage is at most `1/2`: strong rows have `k/4`, weak rows have `h/2`. The only nontrivial q=1 gate is the effective-dimension condition

`theta=tr K_gamma = 2k+h >2`.

The exact theorem gives the one-dimensional certificate

`R_eps(gamma)= e/(sqrt(2) gamma) * theta/(theta-2) * D^(-1/(2 theta))`,

where

`D=(1+4/gamma^2)^2 (1+eps^2/gamma^2)`.

The gate `theta>2` is equivalent after `x=gamma^2` to

`4 eps^2 - eps^2 x - 2x^2 >0`.

Thus pure ridge cannot fix a positive scale as `eps->0`; it must resolve some portion of the weak third direction.

For the concrete stress value `eps=10^(-6)`, direct minimization of this exact scalar expression over its admissible interval gives

`gamma = 2.3143390004 * 10^(-6)`,
`theta = 2.1573275707`,
`D = 6.6184044284 * 10^23`,
`boxed( R_(10^-6) = 34.3217841164... )`.

The natural asymptotic scale can be read off by putting `gamma^2=c eps^2` and `L=log(1/eps)`. For `1<<c<<eps^(-1)`,

`R_eps = (e/sqrt(2)) c exp(L/(2c)) (1+o(1))`.

The elementary minimizer of the displayed leading term is `c=L/2`, giving the logarithmic scale

`R_eps ~ [e^2/(2 sqrt(2))] log(1/eps)`

for the optimized one-scale-ridge functional. This asymptotic is only a statement about this certificate, not a lower bound for the actual density.

## 7. Square-assisted half-Riesz regularization is uniform

Now use the earlier B04 theorem `QFORM-SQUARE-WEIGHTED-DETERMINANT-HALFRIESZ-v1`, source

`math-open-problems@6155d85896070c87f6523a30646c38ac10be43a9`,

which is product-coordinate based and allows the square shift to overlap the residual. Here the outer coordinate is exactly `Z`, `a=1`, shift zero, and the residual cross block is `M_eps`.

At q=1 the range projection is `UU^T` and has maximum diagonal `1/2`, so the theorem gives

`||p_(Q_eps)||_infinity <= J_1(M_eps)`

with

`J_1(M_eps)=(1/sqrt(2pi)) int_R |t|^(-1/2)
 det(I+2t^2 M_eps M_eps^T/(pi^2 e^2))^(-1/4) dt`.

Discarding only the favorable weak factor and retaining the two strong singular values 2,2,

`J_1(M_eps) <= (1/sqrt(2pi)) int_R |t|^(-1/2)
 (1+8t^2/(pi^2 e^2))^(-1/2) dt`.

The beta substitution `u=8t^2/(pi^2 e^2)` evaluates the integral exactly:

`boxed( ||p_(Q_eps)||_infinity <= [sqrt(e)/2^(5/4)] B(1/4,1/4) )`

`= 5.140992379491866...`, uniformly for every `0<eps<=1` and every admissible product input law.

This is the central mechanism separation: perfectly admissible physical third-volume still pays `eps`; pure ridge still needs `theta>2` and hence some weak-direction mass; one genuine independent original-coordinate square supplies the missing half-Riesz smoothing, so two strong cross directions already suffice.

## 8. Ridge as mixed-dimensional virtual volume

The preceding contrast has an exact algebraic explanation. Let `M` be any `m x 3` matrix, `C=M^T M`, and augment it FORMALLY by three virtual rows:

`M_tilde_gamma = [ M ; gamma I_3 ]`.

Then Cauchy-Binet gives

`det(C+gamma^2 I)=e_3(C)+gamma^2 e_2(C)+gamma^4 e_1(C)+gamma^6`.

Under squared-volume sampling of three rows of `M_tilde_gamma`, the marginal probability of including physical row `i` is exactly

`m_i^T(C+gamma^2 I)^(-1)m_i = [M(C+gamma^2 I)^(-1)M^T]_(ii)`,

i.e. the ridge leverage. The total mass of triples containing exactly 3,2,1,0 physical rows is respectively

`e_3(C)`, `gamma^2 e_2(C)`, `gamma^4 e_1(C)`, `gamma^6`,

divided by their sum.

Proof: expand every three-row determinant by Cauchy-Binet; the marginal identity is the standard derivative identity

`d/d(log s_i) log det(M^T diag(s) M + gamma^2 I)|_(s=1)`.

For the present family and `gamma=1/2`, as `eps->0` these four mass fractions tend to

`0, 256/289, 32/289, 1/289`.

The expected number of physical rows tends to

`2*(256/289)+32/289 = 544/289 = 32/17 < 2`,

which is exactly the limiting ridge effective dimension. The virtual rows are algebraic regularizers, not random independent coordinates, so e5 Theorem D cannot simply be applied to them. The actual outer scalar square is the probabilistic ingredient that converts this mixed-dimensional determinant mass into a valid half-Riesz density bound.

## 9. Designated partner account03/B04 applied on the SAME family

The latest completed designated-partner handoff found on fresh brain main is account03/B04 run `20260923T004843Z-account03-B04-qform-auto11`, canonical math

`math-open-problems@370534c8763da810a1b81945e0e44344feab0b75`,

which proves `QFORM-SQUARE-PHYSICAL-PAIR-DETERMINANT-v1`:

`||p_Q||_infinity <= 63.11383495773493 |a|^(-1/2) D^(-1/4)`

for one outer original-coordinate square and any invertible physical two-coordinate pair of determinant magnitude `D` in the residual, with arbitrary outside contamination.

In `M_eps`, a strong physical entry has magnitude `|b|=6/7`. Choose the corresponding original pair `(X_i,Y_j)`. Its physical 2x2 quadratic block is `[[0,b],[b,0]]`, hence `D=b^2=36/49`; all other coordinates are exactly the allowed outside variables. With `a=1`, the partner theorem therefore gives on the SAME target-valid family

`boxed( ||p_(Q_eps)||_infinity <= 63.11383495773493 sqrt(7/6) )`

`= 68.17073314053160...`, uniformly in `eps`.

This application is intentionally complementary. It shows that this family is not a QFORM obstruction: a local determinant-plus-square mechanism already controls it. What the family refutes is the stronger strategy claim that a globally optimized admissible third-volume certificate should automatically match the best regularized/square-assisted certificate.

## 10. Quantitative comparison and remaining gap

At `eps=10^(-6)` on the exact same physical matrix:

- globally optimal e5 admissible 3-volume certificate: `623.177590309...`;
- optimized one-scale ridge certificate: `34.3217841164...`;
- designated-partner physical-pair-plus-square certificate: `68.1707331405...`;
- square-assisted determinant/half-Riesz certificate: `5.14099237949...`.

The hierarchy is not about the true density; it is about what each proved mechanism can certify. The exact all-weight optimization proves that the volume loss is intrinsic to physical 3-volume on this geometry. The virtual-volume identity explains why ridge improves it. The half-Riesz splice explains why an actual scalar square can remove the weak direction completely.

First unpaid implication: `QFORM-OUTER-SQUARE-PLUS-RANK2-OR-HUB-ROUTING-v1` as stated in Section 1. A proof must be structural and product-preserving: from `s_3(A)>=1`, either expose a quantitatively usable original scalar square plus two aggregate residual cross directions, or route the zero/near-zero-pivot survivors to already-completed pair/hub/grouped mechanisms. No post-rotation independence or small-random-perturbation assumption is allowed.
