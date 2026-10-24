SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B19, 2026-09-23T09:09:29Z.
attacking: the extreme normalized physical-coloop endpoint left by account03/B19 r28 and account02/B19 r30; test whether it forces any quantitative local pivot, and identify a product-preserving aggregate replacement when it does not.

# account02/B19 r31 — extreme-coloop strict-N3 family: local pivots vanish, grouped square-plus-hyperbola pays uniformly

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly / SYNTHESIS / complementary constructions and source-valid counterexamples  
**Owner control:** revision `2026-09-22.15` at the final pre-write refresh  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not native learned-memory receiver use  
**Classification:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_STRUCTURAL_IMPLICATION_REFUTED`; the full QFORM conjecture remains OPEN.

The full target is unchanged: for every finite `n`, every independent real product law with one-dimensional densities at most one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal finite essential density bound for `X^T A X`, or exhibit a valid counterexample. No moment, support, log-concavity, Gaussian, diagonal-coordinate, or post-rotation independence hypothesis is introduced here. Continuity is separate.

This report attacks the first explicit endpoint left by the designated partner account03/B19 r28 and account02/B19 r30: an extreme normalized physical coloop `ell>63/64` in the exact-rank-three rank-two-cross chamber. The outcome is twofold.

1. The tempting next structural step — “an extreme normalized coloop forces a uniformly nondegenerate physical scalar or pair pivot” — is false even inside strict `N3(tau)`, with all physical scalar and pair pivots tending to zero.
2. The same stress family is nevertheless uniformly target-paid by a completed product-preserving theorem: the whole form groups exactly into one independent square plus one independent hyperbolic product. This identifies a concrete aggregate currency that survives when every local pivot disappears.

No small coefficient is deleted; the exact matrix is retained throughout.

## 1. Incoming source-pinned proof graph

The global source-correct synthesis reduces the unrestricted theorem to the fixed strict no-pivot statement `N3(tau)` for one universal `tau>0`: all physical diagonals and all physical principal `2x2` determinants are smaller than `tau`, while the matrix still has at least three eigenvalues of modulus at least one. The full theorem remains open because `N3(tau)` remains open.

The current designated partner is account03/B19 r28:

`yspennstate/math-open-problems@4d5181180f8d5e9e14c9b1c5c5e44679c8c212b9`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T080333Z-account03-B19-QFORM-r28/REPORT.md`.

In its exact-rank-three rank-two-cross chamber,

`A=R M R^T`, `R^T R=I_3`, `s_min(M)>=1`,

an original-coordinate partition `I union J` has source and receiver Grams

`G=R_I^T R_I`, `H=R_J^T R_J=I-G`,

with `rank G=3`, `rank H=2`, and cross singular product

`rho=s_1(A[I,J])s_2(A[I,J]) >= rho_0:=sqrt(29/3072)`.

On the two-dimensional range `W` of `H`, normalized receiver rows

`v_j=(H|_W)^(-1/2)s_j`

form a Parseval frame. If the disjoint two-basis mass is below `1/64`, r28 reduces the geometry to STAR or TRIANGLE. STAR means some actual physical receiver coordinate has normalized leverage

`ell_j=||v_j||^2>47/64`.

The immediately preceding account02/B19 r30 theorem is

`yspennstate/math-open-problems@f27836052ed614a51f833f1e214eadd976debfcf`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260923T083941Z-account02-B19-QFORM-r30/REPORT.md`.

In the double-coloop subchamber

`h_1<1/64`, `h_2>63/64`,

where `h_1<=h_2` are the positive eigenvalues of `H`, it pays every STAR state satisfying

`ell<=63/64` and `v_thick^2>=1/64`

by an exact original-coordinate repartition and the completed account01/B19 transverse receiver, with density `<133`. Hence one remaining endpoint is

`ell>63/64`.

The present report shows that this endpoint may occur arbitrarily deeply inside strict `N3(tau)` while every local pivot tends to zero.

## 2. Construction of the stress family

Fix an integer `m>=65` and set

`eps=1/m`,

`a_m = 1/sqrt(eps(1-eps)) = m/sqrt(m-1)`.

Let

`M_m = [[a_m,0,0],[0,0,1],[0,1,0]]`.

Its eigenvalues are exactly

`{a_m,+1,-1}`.                                                     (2.1)

We now build an `N x 3` matrix `R_m` with orthonormal columns from six disjoint groups of ORIGINAL physical coordinates. Every row is supported on one of the spectral axes `e_1,e_2,e_3`.

The source bank `I` contains

- `m` rows `sqrt((1-eps)/m) e_1`;
- `m` rows `sqrt(eps/m) e_2`;
- `m` rows `(1/sqrt m)e_3`.

The receiver bank `J` contains

- `m` rows `sqrt(eps/m)e_1`;
- one hub row `(1-eps)e_2`;
- `m` rows `sqrt(eps(1-eps)/m)e_2`.

There are no `e_3` rows in `J`. The column Gram is exactly

`R_m^T R_m=I_3`.                                                   (2.2)

Indeed the `e_1` masses are `(1-eps)+eps=1`; the `e_2` masses are

`eps+(1-eps)^2+eps(1-eps)=1`;                                     (2.3)

and the `e_3` mass is one.

Define the physical matrix

`A_m=R_m M_m R_m^T`.                                                (2.4)

By (2.2), the nonzero spectrum of `A_m` equals the spectrum of `M_m`. Thus

`spec_nonzero(A_m)={a_m,+1,-1}`.                                  (2.5)

Every `A_m` is an exact target matrix with three eigenvalues of modulus at least one.

## 3. It is exactly the double-coloop / extreme-STAR endpoint

The source and receiver Grams are diagonal:

`G_m=diag(1-eps, eps, 1)`,

`H_m=diag(eps,1-eps,0)`.                                           (3.1)

Therefore the two positive receiver eigenvalues are

`h_1=eps=1/m<1/64`,

`h_2=1-eps>63/64`                                                   (3.2)

for every `m>=65`. This is exactly the double-coloop geometry entering r30.

Normalize on `W=span(e_1,e_2)`. The receiver rows become

- the `m` `e_1` rows: `(1/sqrt m)e_1`;
- the hub row: `sqrt(1-eps)e_2`;
- the `m` residual `e_2` rows: `sqrt(eps/m)e_2`.

Hence the hub normalized leverage is

`ell_hub=1-eps=1-1/m>63/64`.                                      (3.3)

Thus the family lies in the precise r30 extreme-coloop endpoint.

The physical cross block nevertheless remains quantitatively rank two. Since

`A[I,J]=Q_I [G_m^(1/2) M_m H_m^(1/2)] Q_J^T`

for isometries `Q_I,Q_J`, its nonzero singular values are those of

`G_m^(1/2) M_m H_m^(1/2)`.

The latter matrix has orthogonal nonzero columns with lengths

`a_m sqrt(eps(1-eps))=1`,

`sqrt(1-eps)`.                                                       (3.4)

Therefore

`s_1(A[I,J])s_2(A[I,J])=sqrt(1-eps)`.                              (3.5)

In particular the live partner threshold `rho>=sqrt(29/3072)` is satisfied by a wide margin.

At the same time the source transverse self scale collapses. The source self block is represented on its three-dimensional range by

`G_m^(1/2) M_m G_m^(1/2)
 = [[sqrt((1-eps)/eps),0,0],
    [0,0,sqrt(eps)],
    [0,sqrt(eps),0]]`.                                              (3.6)

The source cross range is `span(e_1,e_3)`, so the transverse unit direction is `e_2`, and

`||B e_2||=sqrt(eps)=m^(-1/2) ->0`.                                (3.7)

This is why a receiver theorem that spends a reciprocal power of the transverse self scale is not uniform on this family even though the actual QFORM law is benign.

## 4. Refutation of local-pivot forcing inside strict N3

Because every physical row of `R_m` lies on one spectral axis, the entries of `A_m` can be read off directly from `M_m`.

Only `e_1` rows have nonzero diagonal. The largest diagonal occurs on a source `e_1` row and equals

`a_m (1-eps)/m
 = sqrt(m-1)/m`.                                                    (4.1)

Thus

`max_i |(A_m)_{ii}|=sqrt(m-1)/m ->0`.                              (4.2)

For principal `2x2` determinants:

- two `e_1` rows form a rank-one block, so the determinant is zero;
- an `e_1` row paired with an `e_2` or `e_3` row has determinant zero;
- two `e_2` rows or two `e_3` rows have determinant zero;
- an `e_2` row of coefficient `c` and an `e_3` row of coefficient `d` give the zero-diagonal block `[[0,cd],[cd,0]]`, whose determinant is `-(cd)^2`.

The largest `e_2` coefficient is the hub coefficient `1-eps`, while every `e_3` coefficient is `1/sqrt m`. Hence

`max_{i!=j}|det (A_m)_{\{i,j\},\{i,j\}}|
 = (1-1/m)^2/m ->0`.                                               (4.3)

Consequently, for every fixed `tau>0`, all sufficiently large `m` satisfy simultaneously

`|(A_m)_{ii}|<tau` for every `i`,

`|det (A_m)_{\{i,j\},\{i,j\}}|<tau` for every `i!=j`,              (4.4)

while (2.5) still supplies three actual eigenvalues of modulus at least one.

This proves the structural no-go statement

### `QFORM-EXTREME-COLOOP-LOCAL-PIVOT-FORCING-FALSE-v1`

For every `tau>0` there are exact-rank-three target matrices in the normalized extreme-coloop chamber `ell>63/64` which satisfy strict `N3(tau)`. Therefore no universal argument may close the extreme-coloop endpoint by claiming that it forces a physical scalar pivot or a physical principal-pair determinant bounded below by a positive universal constant.

This is an intermediate structural refutation, not a counterexample to QFORM.

## 5. The same family has an exact product-preserving aggregate payment

Let

`Y=R_m^T X=(Y_1,Y_2,Y_3)`.

The three spectral columns of `R_m` have pairwise disjoint physical supports. Therefore `Y_1,Y_2,Y_3` are genuinely independent random variables, even though this independence comes from the ORIGINAL coordinate partition rather than from spectral rotation.

Each `Y_k` is a unit linear form in its own original-coordinate product bank. The completed weighted projection theorem used in account02/B06 gives the scalar density cap

`||p_{Y_k}||_infinity <= sqrt(e)`.                                 (5.1)

From the exact coefficient matrix `M_m`,

`Q_m=X^T A_m X
    =a_m Y_1^2+2Y_2Y_3`.                                           (5.2)

Now apply the completed account02/B06 theorem

`QFORM-THIRD-SQUARE-HYPERBOLIC-ABSORPTION-v1`,

canonical source

`yspennstate/math-open-problems@168ac7725f62401408f20ce18cbf8ff7055e9013`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T234200Z-e4c1068b3e5d/REPORT.md`.

Its general scalar-cap form says that for three independent scalar inputs `U,V,Z` with density caps `L_U,L_V,L_Z`,

`F+2d(U-theta)V+a(Z-zeta)^2+c`

has density cap

`4sqrt(2) L_Z sqrt(L_U L_V)/sqrt(|ad|)`.                           (5.3)

Use `Z=Y_1`, `U=Y_2`, `V=Y_3`, `d=1`, `a=a_m`, and (5.1). Then

`||p_{Q_m}||_infinity
 <= 4sqrt(2)e / sqrt(a_m)
 = 4sqrt(2)e [eps(1-eps)]^(1/4).`                                  (5.4)

For `m>=65`, `eps<1/64`, hence

`[eps(1-eps)]^(1/4)<64^(-1/4)=1/(2sqrt2)`,

and therefore

`boxed: ||p_{Q_m}||_infinity < 2e < 5.437.`                         (5.5)

In fact the bound tends to zero like `m^(-1/4)`. The local pivot degeneration is therefore not a density degeneration; it is a failure of the local proof currency.

This gives the positive companion statement

### `QFORM-EXTREME-COLOOP-GROUPED-PACKET-v1`

The explicit strict-N3 extreme-coloop family above is uniformly paid by the exact aggregate packet “one independent product-derived square + one independent product-derived hyperbolic product,” even though every physical scalar and pair pivot tends to zero and the transverse source self scale tends to zero.

## 6. Required newest-Claude result applied at a real inequality

The owner-required Claude package is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

Its `COUNTEREXAMPLE_SEARCH.md` Theorem C is a proved one-sheet ruled-surface estimate for every exact-rank-three signature `(2,1)` target with three nonzero eigenvalue magnitudes at least one:

`sup_{s>=0} p_Q(s) <= pi sqrt(2)`.                                  (6.1)

Our `A_m` has signature `(2,1)` and nonzero eigenvalues `{a_m,1,-1}` by (2.5). Thus the source theorem applies directly and supplies the independent real inequality

`sup_{s>=0} p_{Q_m}(s) <= pi sqrt(2) < 4.443`.                      (6.2)

The grouped theorem (5.5) is needed to pay the opposite side as well; (6.2) is recorded as the required equation-level application of the newest-Claude source, not as a full proof of the family by itself.

## 7. What this changes in the proof graph

The strict-N3 proof graph remains open globally. The present calculation changes the extreme-coloop node in a precise way.

A valid exhaustive continuation may NOT use

`extreme normalized coloop => quantitative local scalar/pair pivot`,

because (4.2)-(4.4) refute that implication in the exact target class.

The family instead suggests the correct aggregate mechanism: an extreme coloop can coexist with a large rank-two cross packet while the missing third direction is carried by a disjoint product-derived square. In the canonical stress geometry those resources combine exactly as (5.2), and the completed curved-fiber theorem spends them jointly before any reciprocal local-minor selection.

The first unpaid implication inside the present rank-two-cross / extreme-coloop route is therefore sharpened to

### `QFORM-EXTREME-COLOOP-GROUPED-THIRD-SOURCE-DESCENT-v1`

There should exist universal constants `c,C>0` such that every exact-rank-three rank-two-cross survivor with

- `rho=s_1(A[I,J])s_2(A[I,J])>=sqrt(29/3072)`,
- double-coloop receiver Gram `h_1<1/64`, `h_2>63/64`,
- normalized physical STAR leverage `ell>63/64`,

and with all already-paid repartition, D/D'/D5, F/H, scalar/pair, ridge/window and TRIANGLE exits excluded, admits either

1. an exact product-preserving regrouping into a third-square/hyperbolic packet with `|ad|>=c`, so the account02/B06 theorem gives `||p_Q||_infinity<=C`; or
2. another already-paid aggregate branch.

The construction above proves that this is the right scale of replacement for at least one adversarial strict-N3 sequence, but it does **not** prove the exhaustive descent for arbitrary extreme-coloop matrices. In particular, a general extreme-coloop row need not align exactly with a spectral axis, and the small nonzero residual receiver direction may not be discarded as a perturbation.

The r28 small-pivot/high-star TRIANGLE residue is also still unpaid unless another completed peer theorem covers it. Globally, arbitrary-extra-spectrum descent into the exact-rank-three chambers remains a separate debt. Therefore the unrestricted theorem is not claimed, continuity for the full target is not claimed, and the required two independent end-to-end reviews do not exist.

## 8. Checks and no-go preservation

A deterministic numerical check was run for `m=65,128,1024`; it verifies to floating precision:

- `R_m^T R_m=I_3`;
- nonzero spectrum `{a_m,+1,-1}`;
- `G_m,H_m` as in (3.1);
- cross singular values `{1,sqrt(1-eps)}`;
- hub normalized leverage `1-eps`;
- maximum physical diagonal `sqrt(m-1)/m`;
- maximum principal-pair determinant `(1-1/m)^2/m`;
- grouped bound (5.4), always below `2e` for the tested `m>=65`.

The formulas in the proof are exact; the numerical check is only regression support.

The live correction discipline is preserved. No independence after an arbitrary spectral rotation is asserted: the independence in Section 5 follows from pairwise disjoint ORIGINAL coordinate supports in this explicit construction. No arbitrary-joint coarea bound, conditional-density-as-independence substitution, moment bound, small-coefficient deletion, pointwise stationary-phase estimate, or single-minor extraction is used.
