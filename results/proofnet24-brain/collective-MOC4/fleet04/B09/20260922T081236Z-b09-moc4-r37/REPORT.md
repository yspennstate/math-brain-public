# fleet04/B09 MOC4 report — zero-face spinor cofactor rigidity and aligned external reduction

Run: `20260922T081236Z-b09-moc4-r37`  
Outcome: **ESSENTIAL_STEP_APPLIED**. Full MOC4 remains **OPEN / not proved / not disproved**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Target and fresh control

For complex normal `4 x 4` matrices with spectra `a=(a_1,...,a_4)` and `b=(b_1,...,b_4)`, the target is

`det(A+B) in conv{ product_i(a_i+b_{sigma(i)}) : sigma in S_4 }`,

including repeated and singular spectra. After diagonalizing the relative position, for a unitary `U` and unit support direction `eta` put

`h(U)=Re(conj(eta) det(D_a+U D_b U*))`,

`M=max_sigma Re(conj(eta) product_i(a_i+b_{sigma(i)}))`.

A target counterexample is equivalent to a support direction having a genuine unitary `U` with `h(U)>M`; compactness then gives a positive-gap global maximizer.


## 2. Exact compatible mathematics consumed

### Latest complete campaign lead

Consumed fleet03/B07 `20260922T060726Z-fleet03-B07-MOC4-r11`, theorem `MOC4-SPIN4-SATURATION-TO-ZERO-FACE-v1`. At a genuine support maximizer every complementary-pair Spin(4) mixed-Hessian gate satisfies `T>=|C|`; equality yields a genuine coordinate `SU(2)` factor with zero pair Hessian, hence a flat pair orbit and an equal-support zero-entry representative.

Also retained fleet02/B09 `20260922T064517Z-fleet02-B09-MOC4-r17`, theorem `MOC4-SPIN4-SATURATION-EXCLUSION-v1`: the pair-specific endpoint roof makes a flat coordinate pair orbit target-safe, so a positive-gap global maximizer actually has `T>|C|` at every such gate. Its first explicit boundary residual is the strict zero-face quaternion/Haar-reserve branch.

### Assigned OTHER-account partner

Consumed the latest complete fleet01/B07 report `20260922T070244Z-b07-moc4-r11`, theorem `MOC4-EXTERNAL-SPINOR-HELLINGER-HOLE-v1`, together with the exact spinor identity it applies.

For every genuine exterior-square point, in each even-even complex gauge the real orthogonal action can be written as the Bogoliubov map

`z -> M z + N conjugate(z)`

with `3 x 3` complex blocks satisfying the orthogonality identities

`M M* + N N* = I`,

`M* M + N^T conjugate(N) = I`,

`M N^T + N M^T = 0`.                                             (2.1)

The partner's source-exact spinor theorem supplies

`det N=0`,                                                          (2.2)

and, for the gauge indexed by a singleton coordinate `(i,j)`,

`||N||_F^2 = 2(1-P_ij)`, `P_ij=|u_ij|^2`.                         (2.3)

The same report applies the Drury/Saxl 72-vertex outer relaxation: every normalized genuine point is a convex combination of 24 Weyl/permutation vertices and 48 external vertices, whose singleton coordinates satisfy

`P_sigma = permutation matrix of sigma`,

`P_ext(tau,rho') = (J-P_tau)/3`.                                  (2.4)

Finally, that partner gives an exact structured spectral stress direction in which one external value exceeds the 24-endpoint maximum by

`232716479/4000000000 > 0`.                                       (2.5)

That is a counterexample to the spectral-only shortcut `max_external<=M`, not to MOC4.

## 3. New theorem: `MOC4-ZERO-FACE-BOGOLIUBOV-COFACTOR-RIGIDITY-v1`

Fix a genuine unitary `U in U(4)` and an even-even gauge associated to singleton `(i,j)`. Assume

`u_ij=0`.

Let `M,N` be its Bogoliubov blocks as in (2.1)-(2.3). Then:

1. the singular values of `N` are **exactly `(1,1,0)`**;
2. `N` is a rank-two partial isometry and `M` is a rank-one partial isometry;
3. if `u in C^3` spans `ker N*` and `v in C^3` spans `ker N`, both unit, then for phases `phi,psi`,

   `M = exp(i phi) u v^T`,

   `adj(N) = exp(i psi) v u*`;                                    (3.1)

4. consequently every entry satisfies the exact cofactor-modulus identity

   `|M_{alpha beta}|^2 = |cof_{alpha beta}(N)|^2`;                 (3.2)

5. writing

   `q_{alpha beta}=|N_{alpha beta}|^2`,
   `r_alpha=sum_beta q_{alpha beta}`,
   `c_beta=sum_alpha q_{alpha beta}`,

   one has the entrywise factorization

   `|M_{alpha beta}|^2=(1-r_alpha)(1-c_beta)`.                     (3.3)

Thus on a true zero-entry face the complex-linear and anti-linear spinor blocks are not independent mixed-minor data. The mass-two anti-linear block is forced onto the rank-two partial-isometry locus, and the companion block is its cofactor/rank-one complement.

### Proof

Because `u_ij=0`, equation (2.3) gives

`||N||_F^2=2`.                                                     (3.4)

From `M M*+N N*=I`, the operator `N N*` is bounded by the identity, so every singular value `s_k(N)` lies in `[0,1]`. Equation (2.2) gives at least one zero singular value. Equation (3.4) says

`s_1(N)^2+s_2(N)^2+s_3(N)^2=2`.

The only possibility with three numbers in `[0,1]`, one of them zero, is

`{s_1,s_2,s_3}={1,1,0}`.                                         (3.5)

Let `u` span `ker N*` and `v` span `ker N`. Since (3.5) makes `N N*` the orthogonal projection onto `u^perp`,

`N N*=I-u u*`.

Likewise

`N* N=I-v v*`.

The first identity in (2.1) therefore gives

`M M*=u u*`.                                                       (3.6)

Taking complex conjugates of `N* N=I-v v*` gives

`N^T conjugate(N)=I-conjugate(v) v^T`.

The second identity in (2.1) gives

`M* M=conjugate(v) v^T`.                                          (3.7)

Equations (3.6)-(3.7) force the rank-one form

`M=exp(i phi) u v^T`.

For rank-two `N`, `N adj(N)=adj(N) N=0`. Hence every column of `adj(N)` lies in `ker N=span(v)`, while every row lies in `ker N*` as a row functional; therefore

`adj(N)=c v u*`

for a scalar `c`. The Frobenius norm of the adjugate equals the product of the two nonzero singular values of `N`, hence `|c|=1` by (3.5). This proves the second formula in (3.1).

Since `cof_{alpha beta}(N)=adj(N)_{beta alpha}`, (3.1) gives

`|cof_{alpha beta}(N)|^2=|u_alpha|^2 |v_beta|^2=|M_{alpha beta}|^2`,

which is (3.2).

Finally

`r_alpha=(N N*)_{alpha alpha}=1-|u_alpha|^2`,

`c_beta=(N* N)_{beta beta}=1-|v_beta|^2`.

Substitution into `|M_{alpha beta}|^2=|u_alpha|^2|v_beta|^2` proves (3.3). QED.

### Scope / boundary cases

The theorem uses only true-unitary exterior-square identities and the exact zero `u_ij=0`. It does not divide by a determinant, a spectral gap, a matrix entry or a mixed minor. Repeated spectra, singular `A` or `B`, endpoint ties, and rank-degenerate determinant values do not affect it. It is a unitary-orbit statement independent of spectral genericity.

## 4. New exact outer-face reduction: `MOC4-ZERO-FACE-ALIGNED-EXTERNAL-REDUCTION-v1`

Fix a genuine point with `P_ij=0`. In **every** convex decomposition of that point inside the inherited 72-vertex Drury/Saxl outer hull, only the following vertices may have positive coefficient:

- the 18 Weyl vertices `sigma` satisfying `sigma(i) != j`;
- the 12 external vertices `(tau,rho')` satisfying `tau(i)=j` (six possible `tau`, two external choices over each).

Consequently, if a genuine zero-face point has support `h(U)>M`, then at least one of those **12 aligned external vertices** has external support value `>M`.

### Proof

All singleton `P_ij` coordinates of the 72 vertices are nonnegative. At a Weyl vertex, `P_ij` is `1` exactly when `sigma(i)=j`, and otherwise `0`. At an external vertex, (2.4) gives `P_ij=0` exactly when `tau(i)=j`, and otherwise `1/3`.

Write the genuine zero-face point as a convex combination of the 72 vertices. Its `P_ij` coordinate is zero. A convex combination of nonnegative numbers equals zero only if every positively weighted term has zero coordinate. Thus all Weyl vertices with `sigma(i)=j` and all external vertices with `tau(i)!=j` have zero coefficient. Counting gives 18 allowed Weyl and 12 allowed external vertices.

Every allowed Weyl support value is at most `M`. If every allowed external support value were also at most `M`, their convex combination would be at most `M`. Therefore `h(U)>M` forces an aligned external value `>M`. QED.

This turns the zero-entry branch of the finite outer relaxation from 48 external directions into 12 precisely aligned directions, while retaining true-unitary compatibility as the remaining nonlinear constraint.

## 5. Decisive refutation of the tempting spectral-only closure

A natural next shortcut would assert:

> whenever a zero face `(i,j)` is selected, every aligned external vertex `tau(i)=j` has support at most `M` for determinant-product spectral data.

That statement is **false**.

Use the exact fleet01/B07 stress datum from (2.5). Its unique bad external vertex has a permutation label `tau`. Relabel the `b`-spectrum (equivalently relabel the column coordinates) by `tau` so that this external label becomes the identity. This relabelling merely permutes the 24 endpoint products and the external orbit, hence preserves `M`, `E_0`, and the exact excess

`E_0-M=232716479/4000000000>0`.

For the relabelled datum the bad external vertex is aligned with singleton `(0,0)` because `id(0)=0`. Therefore aligned-external safety does **not** follow from the spectra/support functional alone. A zero-face proof must use the genuine-unitary nonlinear constraint. The theorem in Section 3 supplies exactly such additional information: on that face the gauge block `N` must have singular values `(1,1,0)` and its companion is the cofactor complement.

This refutes only the shortcut, not MOC4 and not the Section-4 reduction.

## 6. Exact arithmetic verification

`verify_zero_face_cofactor.py` gives a rational, tolerance-free consistency instance. It chooses rational orthogonal `L,R` and sets

`N=L diag(1,1,0) R^T`,

`M=L diag(0,0,1) R^T`.

The standard-library `Fraction` calculation verifies exactly:

- `det N=0`;
- both orthogonality identities and the cross identity in (2.1);
- `||N||_F^2=2`, `||M||_F^2=1`;
- `adj(N)=M^T` in this determinant-`+1` real example;
- all nine instances of the factorization (3.3).

The captured output is in `verification.txt`. This finite example is a check of formulas; the theorem is the algebraic argument above.

## 7. Compact conditional end-to-end argument after this run

Assume MOC4 fails.

1. By fleet04/B09 `MOC4-OPEN-GAP-GENERICIZATION-v1`, there is a counterexample with simple nonzero spectra away from all finite conditioning degeneracies, so all spectral limits can be recovered after a generic contradiction.
2. Choose a genuine positive-gap global support maximizer.
3. By fleet02/B09 `MOC4-SPIN4-SATURATION-EXCLUSION-v1`, every coordinate Spin(4) pair gate is strict; no flat/saturated pair can support a violation.
4. If the maximizer has a zero entry, Section 4 forces any Drury/Saxl outer-hull excess into one of only 12 aligned external directions. Section 3 simultaneously forces the exact rank-two partial-isometry/cofactor equations on the corresponding true-unitary spinor gauge.
5. If the maximizer has no zero entry, it remains in the strict Spin(4) interior with the inherited mixed-Hessian, stationarity, subgroup-roof and same-unitary compatibility constraints.

Therefore the zero-entry branch has been sharpened from a free quaternion/Haar reserve plus 48 external possibilities to a **finite aligned external obstruction intersected with the exact cofactor variety (3.2)-(3.3)**. The old spectral-only attempt is ruled out by Section 5, so the next proof must actually exploit that intersection.

## 8. First essential missing implication

The first zero-face implication is now:

### `MOC4-ALIGNED-EXTERNAL-COFACTOR-PAYMENT-v1`

For generic spectral data, arbitrary support direction, and a genuine zero-entry global maximizer with positive gap, take the singleton even-even gauge aligned to the zero. Prove that the exact constraints

- `s(N)=(1,1,0)`;
- `|M_{alpha beta}|^2=|cof_{alpha beta}(N)|^2=(1-r_alpha)(1-c_beta)`;
- the residual zero-face quaternion/Haar identities and strict coordinate-pair gaps;
- the structured determinant-product coefficient identities;

force every aligned external support excess to be paid back to at most the endpoint maximum `M`.

Equivalently, rule out intersection of the positive aligned-external support cap with the genuine rank-two partial-isometry/cofactor locus under the structured MOC4 coefficients. This is a strictly stronger and more source-faithful target than metric distance from an external vertex alone and is not replaced here by an unsupported convexity claim.

The no-zero branch still independently requires strict-interior support payment. Neither implication is proved in this run, so there is no full-proof candidate and no truth promotion.

## 9. Verdict and integrity

**ESSENTIAL_STEP_APPLIED.** The exact zero-entry condition has been converted into a new same-unitary spinor rigidity theorem, and the finite Drury/Saxl outer branch has been reduced to 12 aligned external directions. An exact partner stress datum refutes the easiest remaining spectral-only shortcut, identifying precisely why the cofactor constraint must enter the next step.

Full MOC4 remains open.

Scoped privacy/provenance review: only owner-authorized MOC4 control text, existing private mathematical reports in the same campaign, and synthetic exact rational matrices were used. No benchmark gold/answers/keys, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, paid/API/Codex model, remote workflow, permission bypass, or public release was used. A manual changed-content scan found no such material; no dedicated repository secret-scan action was exposed in the connector used for these writes.
