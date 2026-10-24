# account02/B11 — balanced four-bank indefinite closure: the logarithmic saddle becomes an integrable three-mode product estimate

Status: `ESSENTIAL_STEP_APPLIED / SUPPORTING_COROLLARIES_PROVED / PARTNER_OBSTRUCTION_CLOSED / FULL_QFORM_OPEN`.

Programme: `QFORM-DENSITY-3EIG-20260922`. Role: indefinite signatures, complementary constructions/source-valid counterexamples. Execution: `WITHOUT_VERIFIED_BRAIN`.

The full conjecture remains OPEN. The result below closes the latest designated-partner obstruction family and a broader cross-cut class. It does not give the missing structural theorem that every N3 survivor has such a four-bank compiler.

## 1. Exact obligation and source-pinned premises

The full target is: for arbitrary independent real inputs with one-dimensional densities at most one and arbitrary symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential density bound for `X^T A X`, or give a target-valid counterexample. No moments, bounded supports, log-concavity, identical laws, or independence after rotation are assumed.

The first unpaid B11 implication at this run was the latest designated-partner obligation

`QFORM-BALANCED-FOUR-BANK-AGGREGATION-v1`:

aggregate the collective positive/negative defect of a balanced near-rank-one physical matrix over growing original-coordinate banks before any reciprocal-minor payment.

The designated partner source actually used is account03/B11 r26:

- repository/commit: `yspennstate/math-open-problems@c5a085c3995af258cb161d94cb051d58bbd98b24`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260923T093835Z-account03-B11-QFORM-r26/REPORT.md`.

That report proves that for its explicit target-valid family every fixed-size physical principal or cross packet loses the second/third direction, even though the full matrix has a large `(+,+,-)` core. Therefore a proof that first fixes `K` physical coordinates and only then pays a minor cannot be universal.

The pinned newest-Claude source actually used at equations below is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

Three proved results from that package are used with their stated scopes:

1. **Theorem F (Fresnel--Brascamp--Lieb).** If a rank-three spectral part `sum lambda_k r_k r_k^T` is added to a diagonal twist, and on the selected original-coordinate bank the normalized frame leverages are at most `1/2`, then

   `||p_Q||_infinity <= 12 (|lambda_1 lambda_2 lambda_3| det G)^(-1/3)`.

   The proof retains the original product factors; it does not make the spectral projections independent. It yields an `L^1` characteristic function and hence a continuous density in this scope.

2. **Theorem D (volume-sampling Brascamp--Lieb).** For an original-coordinate cross block `M=A_IJ` with 3-volume `Z=e_3(M^T M)` and row volume marginals at most `1/2`,

   `||p_Q||_infinity <= 6 sqrt(e) Z^(-1/6)`,

   with arbitrary same-side quadratic blocks, outside couplings and affine terms retained.

3. **Theorem C (ruled one-sheet estimate).** For an exact rank-three form of signature `(+,+,-)`, the one-sheet side of the critical value obeys `p(s)<=pi sqrt(2)` after the source normalization `lambda_1,lambda_2,mu>=1`. The theorem deliberately does not pay the two-sheet side.

The live corrections are respected: no arbitrary-joint coarea bound, conditional-density cap as independence, near-zero replacement of an exact null pivot, fixed physical packet, or small-random-perturbation argument is used.

## 2. The four-bank Walsh frame

Let `n=4m`. Choose `u,v in {+1,-1}^n` so that

`<u,1>=<v,1>=<u,v>=0`,

and each of the four sign pairs `(u_i,v_i)` occurs exactly `m` times. Put

`r0=n^(-1/2) 1`, `rv=n^(-1/2) v`, `ru=n^(-1/2) u`.

Then `r0,rv,ru` are orthonormal. The `i`th physical row of the frame `R=[r0 rv ru]` has exact leverage

`|R_i|^2 = 1/n+1/n+1/n = 3/n`.                                      (2.1)

This is the feature hidden from every fixed packet in the partner construction: each single coordinate sees only `O(1/n)` of each mode, but the whole original-coordinate product frame sees all three modes exactly.

## 3. First supporting result: arbitrary diagonal twist, both indefinite signatures

### Proposition 3.1 — `QFORM-WALSH-THREE-MODE-DIAGONAL-TWIST-v1`

Assume `n=4m>=8`. Let `D` be an arbitrary real diagonal matrix, let `ell` be arbitrary, and let `a,b,c` be nonzero real numbers. For independent cap-one coordinates `X_i`, define

`Q = X^T D X + a <r0,X>^2 + b <rv,X>^2 + c <ru,X>^2 + ell^T X + q0`.   (3.1)

Then `Q` has a continuous density and

`boxed: ||p_Q||_infinity <= 12 |abc|^(-1/3).`                        (3.2)

This covers `(+,+,-)` and `(+,-,-)` choices of the three displayed coefficients, and arbitrary coordinatewise quadratic curvature in `D`.

**Proof.** Apply pinned Theorem F with `I` equal to all original coordinates. Since `R^T R=I_3`, its Gram matrix is `G_I=I_3`. By (2.1), every normalized leverage is `3/n<=3/8<1/2`. The theorem therefore gives exactly (3.2). The spectral projections are never declared independent; the product structure used by the proof is the original factorization of the `X_i` laws. QED.

### Application to the designated partner r26 family

The partner matrix is

`A_delta = (1-2 delta) J + delta vv^T - delta uu^T + 2 delta I`,       (3.3)

with `0<delta<1/4`. In the normalized frame,

`A_delta = 2 delta I
 + ((1-2 delta)n) r0 r0^T
 + (delta n) rv rv^T
 - (delta n) ru ru^T`.                                                (3.4)

Thus Proposition 3.1 gives the actual full-matrix inequality

`||p_{X^T A_delta X}||_infinity
 <= 12 / [n delta^(2/3) (1-2 delta)^(1/3)].`                           (3.5)

No physical minor is selected. This directly closes the explicit family that defeats every fixed-size packet.

The full eigenvalues from the partner calculation are

`(1-2delta)n+2delta`, `delta n+2delta`, `-delta(n-2)`, and `2delta` on the orthogonal complement. For this family to satisfy the target through the negative mode it is enough and necessary here that

`delta(n-2)>=1`;                                                       (3.6)

the two positive displayed modes are then also at least one in magnitude.

On `0<delta<1/4`, the function `delta^2(1-2delta)` has derivative `2delta(1-3delta)>0`. Therefore (3.5), subject to (3.6), is worst at `delta=1/(n-2)`:

`||p||_infinity <= 12(n-2)/[n(n-4)^(1/3)].`                          (3.7)

For real `n>=8`,

`d/dn log[(n-2)/(n(n-4)^(1/3))]
 = 2/[n(n-2)] - 1/[3(n-4)] < 0`,                                    (3.8)

because `n(n-2)-6(n-4)=n^2-8n+24=(n-4)^2+8>0`. Hence among the admissible multiples of four the worst case is `n=8`, and

`boxed: ||p_{X^T A_delta X}||_infinity
        <= 9 / 4^(1/3)
        = 5.6696447245... .}`                                        (3.9)

At the partner stress scaling `delta=n^(-1/2)`, (3.5) is actually

`12/[n^(2/3)(1-2/sqrt(n))^(1/3)]`,                                   (3.10)

which decreases to zero. The collective third direction becomes stronger while every fixed physical packet becomes more singular; this is precisely why reciprocal local minors are the wrong quantity here.

## 4. Stronger bank compiler: arbitrary within-side self curvature

The diagonal twist in Proposition 3.1 is not essential if the four sign classes can be split product-preservingly across an original-coordinate cut.

### Proposition 4.1 — `QFORM-WALSH-FOUR-BANK-CROSSCUT-v1`

Assume `n=8m>=16`. In each of the four sign classes `(u_i,v_i)`, place exactly half its coordinates in `I` and half in `J`. Let `R_I,R_J` denote the restrictions of the three-column frame `R`.

Suppose the actual physical cross block of a symmetric quadratic form satisfies

`A_IJ = R_I diag(a,b,c) R_J^T`,                                      (4.1)

with `abc!=0`. The principal blocks `A_II,A_JJ`, all coefficients involving any further outside coordinates, and all affine terms are arbitrary. Then for arbitrary independent cap-one inputs,

`boxed: ||p_Q||_infinity <= 12 sqrt(e) |abc|^(-1/3).`                (4.2)

The density is continuous in this branch.

**Proof.** Exact balance of the four sign classes gives

`R_I^T R_I = R_J^T R_J = (1/2) I_3`.                                (4.3)

Thus `U=sqrt(2)R_I` and `V=sqrt(2)R_J` have orthonormal columns, and

`M=A_IJ=(1/2) U diag(a,b,c) V^T`.                                    (4.4)

The three nonzero singular values of `M` are therefore `|a|/2,|b|/2,|c|/2`. Since `M` has exact rank three,

`Z=e_3(M^T M)=a^2 b^2 c^2/64`.                                      (4.5)

For exact rank three, the volume-sampling row marginals in Theorem D equal the left singular-space leverages. A row of `U` has squared norm

`2*(3/n)=6/n <= 3/8 < 1/2`                                           (4.6)

for `n>=16`. Theorem D applies to the actual ORIGINAL-coordinate cut, while retaining all same-side and outside quadratic curvature. Hence

`||p_Q||_infinity <= 6 sqrt(e) Z^(-1/6)
                   = 12 sqrt(e) |abc|^(-1/3)`.                       (4.7)

QED.

For the partner family, take

`a=(1-2delta)n`, `b=delta n`, `c=-delta n`.

Its diagonal twist contributes nothing to the cross block. Proposition 4.1 therefore yields

`||p||_infinity <= 12 sqrt(e)/[n delta^(2/3)(1-2delta)^(1/3)]`.       (4.8)

Under the target gate `delta(n-2)>=1`, this is at most

`12 sqrt(e)(n-2)/[n(n-4)^(1/3)]`;                                    (4.9)

for the present `n>=16` range it is maximized at `n=16`, giving

`< 7.562`.                                                            (4.10)

The constant is weaker than (3.9), but the scope is stronger: arbitrary within-`I`, within-`J`, and outside curvature is free. This is the robust form of “aggregate before inversion” supplied by the partner obstruction.

## 5. The rank-two logarithmic singularity is inside the same geometry

The four-bank structure itself contains the mandatory rank-two failure. Denote by

`S_{++}, S_{+-}, S_{-+}, S_{--}`

the sums of the ORIGINAL coordinates in the four sign classes. Let

`U=<ru,X>`, `V=<rv,X>`.

A direct calculation gives

`V+U=(2/sqrt(n))(S_{++}-S_{--})`,
`V-U=(2/sqrt(n))(S_{-+}-S_{+-})`,                                    (5.1)

and hence

`V^2-U^2=(4/n)(S_{++}-S_{--})(S_{-+}-S_{+-}).`                       (5.2)

The two factors on the right use disjoint original-coordinate banks, so they are genuinely independent. This is not independence created by a spectral rotation.

Now take the `X_i` to be independent `Unif[-1/2,1/2]`. Let `Y=S_{++}-S_{--}` and `Z=S_{-+}-S_{+-}`. Each is a difference of two iid bank sums. Its density `h` is continuous near zero and

`h(0)=int g(x)^2 dx>0`,                                               (5.3)

where `g` is the density of one bank sum. Consequently there are `epsilon,c0>0` with `h>=c0` on `[-epsilon,epsilon]`. For `0<|t|<epsilon^2`, the product-density formula gives

`p_{YZ}(t)
 = int h(y) h(t/y) dy/|y|
 >= 2 c0^2 int_{|t|/epsilon}^{epsilon} dy/y
 = 2 c0^2 log(epsilon^2/|t|).`                                       (5.4)

Thus `V^2-U^2`, and any nonzero scalar multiple of it, has a logarithmically unbounded density at zero. This is an exact source-valid rank-two opposite-sign control in the same balanced four-bank geometry used above.

It also makes the role of the third direction precise. Algebraically, for the three-mode spectral core

`diag(a,b,-c)`, `a,b,c>0`,                                           (5.5)

the Schur complement after the positive `a` mode is exactly the opposite-sign saddle `diag(b,-c)`. The logarithmic endpoint is therefore not removed algebraically. What changes analytically is that the third mode supplies one more Fresnel half-power in the ORIGINAL-coordinate product integral:

- two opposite-sign modes sit at the non-integrable Fourier endpoint `|t|^{-1}`, matching (5.4);
- three low-leverage modes give `|t|^{-3/2}` through Theorem F, which is integrable.

No convolution of the dependent spectral coordinates is used.

For signature `(+,-,-)`, negate the form (or interchange the sign roles); density `L^infinity` is unchanged.

## 6. Sign-specific ruled comparison: one-sheet versus two-sheet

Set the diagonal twist to zero temporarily and consider

`Q_core=a<r0,X>^2+b<rv,X>^2-c<ru,X>^2`, `a,b,c>=1`.                  (6.1)

Pinned Theorem C applies on the one-sheet side and gives

`p_core(s) <= pi sqrt(2),   s>=0`.                                   (6.2)

The same ruled parametrisation does not control the two-sheet side `s<0`; the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction forbids promoting a mere X-ray cap to such a bound. Proposition 3.1 instead gives the global estimate

`p_core(s) <= 12(abc)^(-1/3)` for a.e. every `s`,                    (6.3)

and therefore closes the two-sheet side for this genuinely rotated flat-frame class by the product-preserving Fresnel mechanism. Restoring an arbitrary diagonal twist still leaves (3.2) valid, while the simple ruling argument no longer applies directly.

This is the sign-specific splice sought by B11: rulings pay the geometrically favorable sheet; the third Fresnel direction pays the opposite sheet without inventing independence.

## 7. What changed in the proof map

The partner r26 obstruction is not merely “not a counterexample”; it is now quantitatively solved:

- every fixed physical packet can have second/third singular values tending to zero;
- nevertheless the actual output density is uniformly bounded by `<5.670` in the whole target-valid one-parameter family;
- a growing original-coordinate cross cut gives a second proof robust to arbitrary same-side self curvature.

Therefore the next general argument should search for a **growing-bank volume certificate**, not a fixed packet.

The explicit rank-two limit (5.2)--(5.4) also shows why a proof cannot discard the third mode: the unbounded logarithmic saddle reappears immediately when that mode is removed.

## 8. First unpaid implication after this run

`QFORM-BALANCED-CROSSCUT-STABILITY-v1`:

In the general unfrustrated near-rank-one N3 survivor where every fixed physical packet degenerates, prove one of the following without a perturbative random-error argument:

1. there is a product-preserving growing cut `I,J` whose actual cross block has target-scale 3-volume and volume row marginals `<3/4`, so Theorem D/D' pays it even with arbitrary same-side curvature;
2. there is a low-leverage three-mode component with an exactly diagonal residual on a sufficiently large product bank, so Theorem F pays it;
3. failure of both structures forces an already-paid scalar pivot, indefinite physical pair, sign-frustrated triangle, ridge/volume, or hub certificate.

The partner family is the normalization test: an acceptable structural theorem must find the balanced growing cut while every fixed packet tends to rank one. A small operator-norm coefficient residual cannot simply be discarded because the inputs may have arbitrary unbounded support.

Independent end-to-end review of these new corollaries has not yet been performed. Full QFORM and full continuity remain open; continuity is proved only in the F/D branches stated above.
