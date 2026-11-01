SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-24T09:16:31Z.
attacking: the overlap-one survivor by first removing the row-marginal gate from physical E2 half-Riesz control, then using the resulting determinant cancellation at an actual scalar anchor.

# fleet03/B04 r54 — marginal-free E2 half-Riesz and an overlap-one scalar-anchor receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: **NEW SUPPORTING THEOREM / OVERLAP-ONE NONZERO-ANCHOR CHAMBER SHRUNK / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Regularity: the new endpoint proves absolute continuity and an essential `L^infinity` bound. It does **not** prove continuity. Full-target continuity remains OPEN.

The owner target is unchanged: the coordinates are independent ORIGINAL real coordinates with one-dimensional density caps one, and `A` is arbitrary real symmetric with at least three eigenvalues of modulus at least one. No moment, Gaussian, log-concavity, compact-support, connected-support, iid, post-rotation independence, law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea bound, worst-fiber supremum, or deletion of a small random coefficient is used.


## 1. Source-valid inputs

### 1.1 Diffuse physical E2 half-Riesz theorem

I use the completed fleet01/B07 theorem `QFORM-E2-FRACTIONAL-TRACE-v1`, preserved at

`yspennstate/math-open-problems@3f8fe4c0920f41353374c50693ccdc741e245008`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B07/fleet01-B07-20260923T130435Z-r25/REPORT.md`.

For a literal disjoint original-coordinate cross block `M`, any positive physical `2x2` minor packet of squared-determinant mass `Z_2`, and one-side inclusion marginals `alpha_i`, if `1<=q<2` and `max alpha_i<=q/2`, the full ambient quadratic-plus-affine polynomial `R` satisfies

`H_(1/2)(R):=sup_s E|R-s|^(-1/2)
 <= [8 sqrt(e/2)/(2-q)] q^(-1/4) Z_2^(-1/8).`                    (1.1)

At `q=1`, the marginal gate is `alpha_i<=1/2` and the constant is

`C_diff=8 sqrt(e/2)=9.326575926388497... .`                       (1.2)

This is a fractional-potential theorem, not a bounded-density theorem for rank two.

### 1.2 Grouped product-Fourier input

The source-pinned weighted-subset / grouped-projection proof is preserved at

`yspennstate/math-open-problems@3f8fe4c0920f41353374c50693ccdc741e245008`,
`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

I only need its explicitly proved characteristic-function estimate in the borderline `k=1, ell=1` case and its exact-rank-two Plancherel estimate. I re-integrate those estimates below, because `k+ell=2` does not itself give an `L^1` characteristic function but it does give precisely the half-Riesz potential needed here.

### 1.3 Global overlap-one source

The fleet03/B20 third-compound operator funnel is preserved at

`yspennstate/math-open-problems@3f8fe4c0920f41353374c50693ccdc741e245008`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260923T234606Z-fleet03-B20-QFORM-r42/REPORT.md`.

Under `s_3(A)>=1` it forces at least one of

`P_3>=1/4`, `J_2^*>=1/144`, `J_1^*>=1/144`, `J_0>=1/16`.          (1.3)

The `P_3` and `J_0` exits already have completed density receivers, and B04 r53 pays the entire `J_2^*` branch. Thus the structurally distinct packet left by this compiler is the one-anchor overlap class `J_1^*`.

## 2. New incident E2 half-Riesz compiler

Let `M=A[I,J]` be a literal cross block between disjoint original-coordinate banks. Write its physical rows as `m_i` and put

`Z=e_2(MM^T)=sum_(i<k) ||m_i wedge m_k||^2>0`.                    (2.1)

For one physical row `i`, define its incident second-volume

`K_i=sum_(k!=i) ||m_i wedge m_k||^2`.                              (2.2)

The natural E2 row marginals are `alpha_i=K_i/Z`, and

`sum_i alpha_i=2`.                                                  (2.3)

### Lemma 2.1 — incident E2 is marginal-free at half-Riesz order

For every `i` with `K_i>0`, the full ambient polynomial `R` satisfies

`boxed: H_(1/2)(R) <= 8 K_i^(-1/8).`                              (2.4)

#### Proof

Set `w=m_i` and project every other row orthogonally off `w`:

`C=M[I\{i},J](I-P_w)`.                                             (2.5)

Gram-Schmidt and Cauchy-Binet give the exact aggregate identity

`K_i=||w||^2 ||C||_F^2`.                                           (2.6)

First suppose every one-volume row marginal of `C` is at most `1/2`. Keep the literal original coordinate `X_i` as the single hub. The `k=1,ell=1` grouped product-Fourier estimate specializes, using the cap-one hub density, to

`|phi_R(t)| <= min(1, 2 pi K_i^(-1/4)|t|^(-1)).`                  (2.7)

Under the Fourier convention used in the source, Abel regularization for `|x|^(-1/2)` gives

`H_(1/2)(R)
 <=(2 pi)^(-1/2) int_R |phi_R(t)||t|^(-1/2) dt`.                  (2.8)

For any `L>0`,

`int_R min(1,L/|t|)|t|^(-1/2)dt=8 sqrt(L)`.                       (2.9)

Substituting `L=2pi K_i^(-1/4)` in (2.8) proves (2.4).

Now suppose a projected residual row `c_k` has one-volume marginal `>1/2`. Then the literal two-row block `P=M[{i,k},J]` has

`D:=det(PP^T)=||w||^2||c_k||^2>K_i/2`.                            (2.10)

The exact-rank-two crossing Plancherel estimate applies to the two ORIGINAL row variables and the original-coordinate column bank. The row-side projected density cap is one, while the two-dimensional column projection cap is at most two. Hence

`|phi_R(t)|
 <=min(1, pi sqrt(2) D^(-1/4)|t|^(-1)).`                          (2.11)

Using (2.8)-(2.9),

`H_(1/2)(R)
 <=8*2^(-1/4)D^(-1/8)
 <8*2^(-1/8)K_i^(-1/8)
 <8K_i^(-1/8).`                                                    (2.12)

This proves the lemma. All conditioning is only on original coordinates, and every same-bank quadratic term and affine term is retained. QED.

## 3. Main theorem — `QFORM-CROSS-E2-MARGINALFREE-HALF-RIESZ-v1`

For every literal disjoint original-coordinate cross block `M` with `Z=e_2(MM^T)>0`, the full ambient quadratic-plus-affine polynomial `R` satisfies

`boxed:
 H_(1/2)(R)
 <= C_E2 Z^(-1/8),
 C_E2=8 sqrt(e/2)=9.326575926388497... .`                         (3.1)

### Proof

If every natural E2 row marginal is at most `1/2`, apply (1.1) at `q=1`.

Otherwise choose `i` with `alpha_i>1/2`, so `K_i>Z/2`. Lemma 2.1 gives

`H_(1/2)(R)
 <8*2^(1/8) Z^(-1/8)
 =8.724061861322062... Z^(-1/8).`                                 (3.2)

Since `8*2^(1/8)<8sqrt(e/2)`, the diffuse branch (1.2) is the worst constant. QED.

This theorem is deliberately only a half-Riesz estimate. Rank-two opposite-sign controls forbid promoting it to a general rank-two density theorem.

## 4. Scalar-anchor promotion of an overlap-one packet

Fix one literal original coordinate `h` with

`a=A_hh !=0`,                                                       (4.1)

and choose disjoint original-coordinate banks `R,C` outside `h`. Define the complete separated one-anchor third-volume packet

`F_h(R,C)
 =sum_(|U|=|V|=2)
   det A[{h} union U,{h} union V]^2.`                              (4.2)

### Theorem 4.1 — `QFORM-ONEANCHOR-E3-PIVOT-E2-RIESZ-v1`

If `F_h(R,C)>0`, the full ambient quadratic-plus-affine law has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= C_E2 |a|^(-1/4) F_h(R,C)^(-1/8).`                             (4.3)

No continuity claim is made.

#### Proof

Complete the square in the ORIGINAL coordinate `X_h`, without rotating random variables:

`Q=a(X_h+L(Y))^2+R_0(Y)`,                                         (4.4)

where `Y=X_(h^c)` remains a product vector. The cap-one law of `X_h` gives, uniformly in the moving shift,

`p_(a(X_h+L)^2)(u)<=|a|^(-1/2)|u|^(-1/2)`.                       (4.5)

Therefore

`p_Q(q)<=|a|^(-1/2) E|q-R_0(Y)|^(-1/2).`                         (4.6)

The quadratic matrix of `R_0` is the exact Schur complement

`S=A_(h^c,h^c)-A_(h^c,h)A_(h,h^c)/a`.                            (4.7)

For every `U subset R`, `V subset C`, `|U|=|V|=2`, the bordered determinant identity gives

`det A[{h} union U,{h} union V]=a det S[U,V]`.                    (4.8)

Hence the full E2 mass of the literal residual cross block is

`e_2(S[R,C]S[R,C]^T)=F_h(R,C)/a^2`.                               (4.9)

Apply (3.1) to the complete residual polynomial `R_0`, retaining its arbitrary diagonal, same-bank, affine and outside terms. Equations (4.6) and (4.9) give

`||p_Q||_infinity
 <=|a|^(-1/2) C_E2 (F_h/a^2)^(-1/8)
 =C_E2 |a|^(-1/4)F_h^(-1/8).`                                    (4.10)

QED.

The exponent cancellation is the point: the scalar square costs `|a|^(-1/2)`, while the aggregate Schur E2 packet returns `|a|^(1/4)`. This is still singular at an exact zero pivot, but much less singular than a direct scalar-pivot estimate.

## 5. Quantitative consequence for the global overlap-one branch

Assume the B20 funnel lands in

`J_1(h)>=1/144`.                                                    (5.1)

Randomly split every physical coordinate other than `h` into two banks `R,C`. Every overlap-one determinant has two row-only and two column-only coordinates and survives in the prescribed orientation with probability `1/16`. Therefore some literal split obeys

`F_h(R,C)>=J_1(h)/16>=1/2304`.                                    (5.2)

If, in addition,

`|A_hh|>=2^(-16)`,                                                  (5.3)

Theorem 4.1 gives the explicit universal payment

`boxed:
 ||p_Q||_infinity
 <= C_E2 2^4 2304^(1/8)
 =128 sqrt(2e) 3^(1/4)
 =392.782854609543... .`                                          (5.4)

Thus the live overlap-one structural debt is sharpened to the genuinely near-zero physical-anchor chamber

`J_1(h)>=1/144,
 |A_hh|<2^(-16),`                                                   (5.5)

plus the already-recorded inverse-free bi-star/E2 alternatives inside that chamber. The exact zero-pivot face remains unpaid by this theorem and is not discarded as a perturbation.

For comparison, the older generic scalar-pivot bound scales as `|a|^(-1/2)`; at the same `2^-16` threshold it is far larger. The new `|a|^-1/4` exponent comes directly from aggregate E2 Fourier/Riesz transport.

## 6. Genuinely rotated indefinite test with every entry nonzero

Let

`v=(1,2,3,4)^T/100`,
`M=[[5/2,1/2],[1/2,5/2]],`                                        (6.1)

and let

`S=[[0_2,M],[M,0_2]]`.                                             (6.2)

Define the fully dense symmetric `5x5` matrix

`A_*=[[2,v^T],[v,S+vv^T/2]].`                                     (6.3)

Every entry is nonzero. Completing the first physical coordinate gives the exact Schur complement `S`. For the residual banks `R={2,3}`, `C={4,5}`,

`det M=6,
 e_2(MM^T)=36,
 F_1(R,C)=2^2*36=144.`                                             (6.4)

Theorem 4.1 therefore gives, for every admissible independent cap-one product law,

`boxed:
 ||p_(X^T A_* X)||_infinity
 <= C_E2 2^(-1/4)144^(-1/8)
 =4.213756346951995... .`                                          (6.5)

This is an essential density bound; continuity is not asserted.

The target spectral condition is rigorous. Put `A_0=diag(2,S)`. Since the singular values of `M` are `3,2`,

`spec(A_0)={-3,-2,2,2,3}`,                                        (6.6)

so `s_min(A_0)=2`. The perturbation is

`E=A_*-A_0=[[0,v^T],[v,vv^T/2]]`,                                 (6.7)

and

`||E||_op<=||v||_2+||v||_2^2/2
 =sqrt(30)/100+3/2000
 <0.057.`                                                          (6.8)

Therefore

`s_min(A_*)>=2-0.057>1.943>1`,                                    (6.9)

so in fact all five eigenvalues have modulus greater than one, with both signs. A floating-point spectrum is recorded only as a redundant check, not as the proof.

## 7. Designated fleet04/B04 result applied

The newest completed designated partner remains fleet04/B04 r2:

`yspennstate/math-open-problems@4a54666abf2316bb79b939cef3ea940605a0af57`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B04/20260924T001353Z-fleet04-B04-QFORM-r2/REPORT.md`.

On its high-fourth-volume carrier branch, failure of its anchored entropy gate gives a literal physical pair with canonical fourth-volume inclusion mass

`eta_ab>2/75`.                                                       (7.1)

Apply the completed B04 pair-anchored E4 promotion theorem from r48 to this actual inequality. Since `H_ab=eta_ab E_4(M)`,

`boxed:
 ||p_Q||_infinity
 <4*75^(1/8) E_4(M)^(-1/8)
 =6.861872579851902... E_4(M)^(-1/8).`                             (7.2)

That partner branch has a continuous `C_0` density. The partner application is separate from the new half-Riesz theorem above.

## 8. What remains

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains OPEN.

The first B04 debt is now

`QFORM-OVERLAP1-NEARZERO-BISTAR-OR-E2-ENDPOINT-v1`:

> in the forced one-anchor packet `J_1(h)>=1/144`, assume the now-sharpened near-zero gate `|A_hh|<2^-16`. Use the exact inverse-free identity
> `F_h^(1/2)<=|A_hh| E_2(N)^(1/2)+||u|| ||w|| ||P_(u^perp)N P_(w^perp)||_F`
> to pay the aggregate two-star/projected-cross branch, or recover a literal E3/ridge/square-bank endpoint, without deleting the small nonzero pivot. The exact zero face must be included.

The new theorem should be reused rather than re-proving E2 half-Riesz marginal removal in future runs.
