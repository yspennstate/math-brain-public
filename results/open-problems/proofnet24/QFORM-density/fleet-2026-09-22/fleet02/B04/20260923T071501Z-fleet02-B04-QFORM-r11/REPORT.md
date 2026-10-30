SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B04, 2026-09-23T07:15:01.550774Z.
attacking: projected rank-two star extraction inside a full-rank near-star cross block, comparing the resulting product-rearrangement bound against admissible third-volume and ridge certificates on the same physical matrix.

# fleet02/B04 r11 — coefficient-projected row-star closure inside full cross rank

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control consumed: revision `2026-09-22.15`  
Role: Product Fourier rearrangement / complementary constructions and source-valid counterexamples  
Designated partner: `fleet03/B04`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Full QFORM: **OPEN**.  
Independent review status of the new theorem: **pending**.

## 1. First unpaid implication

The predecessor debt was `QFORM-QUANTITATIVE-NEAR-STAR-TO-AGGREGATE-RANK2-OR-HUB-v1`: a full physical cross block may have two-minor mass concentrated near a row/column star, while globally optimized full-block entropy weights still pay a logarithmic loss. The present run changes mechanism rather than optimizing that same loss again.

The first unpaid implication after this run is

`QFORM-NEARSTAR-COEFFICIENT-PROJECTION-OR-HUB-v1`:

> In a surviving clean-bank or square-peeled branch, start from near-star physical two-minor geometry and either produce a deterministic two-dimensional coefficient-space projection `P` for which `MP` is a target-scale row/column star packet, or prove that failure of every such projection forces a previously completed diffuse/ridge/grouped-hub exit. The projection must act only on coefficient norms, never on random variables. A quantitative approximate-star-to-exact-projection statement is still unpaid, as is the general two-sided-curvature structural routing.

The analytic point established below is that **arbitrarily many extra cross directions orthogonal to the selected coefficient plane cost nothing at all** once the clean-bank row-star packet is visible. Thus exact full cross rank is not itself an obstruction.

## 2. Source-pinned inputs actually used

### 2.1 Required Claude/e5 volume theorem

Required source:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`

and `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md` in the same directory.

The completed Theorem D permits arbitrary weights on nonzero physical `3x3` minors, with entropy-adjusted volume

`G=exp(E_w log det^2+H(w))`,

but the Fourier `L^p` step imposes a row marginal gate. The proved D' extension allows maximum row marginal `h<3/4`; it does not remove that gate. Section 6 below applies this theorem to an actual obstruction: on the stress matrix every nonzero three-volume weight has row marginal one, so the admissible set is empty.

### 2.2 Designated partner fleet03/B04 r27

Fresh completed partner source:

`yspennstate/math-open-problems@b0d436cae66ffaf557b60427db5ae2fd4d909e65`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/20260923T065845Z-fleet03-B04-qform-auto11-r27/REPORT.md`.

It proves `QFORM-2D-INVERSE-RADIUS-BATHTUB-v1` and `QFORM-ROWSTAR-CLEANBANK-LINF-v1`. In particular, for an exact rank-two physical row-star cross block `N`, with one opposite bank quadratically clean,

`||p_Q||_infinity <= 2^(3/4) sqrt(pi) E2(N)^(-1/4)`.             (2.1)

Its proof is product-preserving: the hub original coordinate is independent of the aggregate projection of the remaining original coordinates, and a two-dimensional decreasing-rearrangement estimate controls the inverse coefficient norm. No post-rotation independence occurs.

### 2.3 Own completed entropy-weighted two-volume compiler

Source:

`yspennstate/math-open-problems@10a74bd7d75466fe46f4ff6ecf3362fba6cb2e5d`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/20260923T052139Z-fleet02-B04-qform-auto11/REPORT.md`.

Its theorem `QFORM-ENTROPY-WEIGHTED-RANK2-HALFRIESZ-v1` says that for any probability weight `w` on nonzero physical `2x2` minors with row marginals at most `q/2`, `1<=q<2`,

`sup_s E|R-s|^(-1/2)
 <= [4 sqrt(2e) q^(-1/4)/(2-q)] G2(w)^(-1/8)`,                  (2.2)

where

`G2(w)=exp(sum w log det^2+H(w))`.

After one untouched original square of coefficient one, the same right side bounds the density. Section 7 globally optimizes all such weights for the stress matrix.

### 2.4 Ridge comparison

The square-assisted ridge source is

`yspennstate/math-open-problems@b129377880c18fe011dd4513282f2e0b60e412e0`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/B04-20260922T155815Z-qform-r11b/REPORT.md`.

For `K_gamma=BB^T(gamma^2 I+BB^T)^(-1)`, `theta=tr K_gamma`, `D=det(I+BB^T/gamma^2)`, if `1<=q<=2`,

`max_i (K_gamma)_ii <= q/2`, `theta>4q/3`,

then an outside original square gives

`||p_Q||_infinity
 <= 8*3^(-5/8)*sqrt(e)*q^(-1/4)
    *sqrt(3theta/(3theta-4q))
    *D^(-1/(4theta))/sqrt(gamma)`.                               (2.3)

The direct ridge theorem has the stronger gate `theta>2q`.

The immediate predecessor run is source-pinned at

`yspennstate/math-open-problems@c63eec6fd03d23bb41493a502670d52bed383d35`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/20260923T065059Z-fleet02-B04-qform-auto12/REPORT.md`.

It solved the full admissible-weight optimization for a different near-star family and showed why another full-block entropy optimization would not pay the remaining structural debt.

## 3. Main theorem: coefficient projection lifts the row-star estimate through arbitrary extra cross rank

### Theorem `QFORM-COEFFICIENT-PROJECTED-ROWSTAR-CLEANBANK-v1`

Let `I,J,K` be disjoint sets of ORIGINAL coordinates. Let `X_I`, `Y_J`, `W_K` inherit the independent cap-one product law. Consider

`Q=F(X_I,W)+2 X_I^T M Y_J+b(W)^T Y_J+c(W)`,                     (3.1)

where `F` is arbitrary measurable and finite a.s. and there is **no quadratic `Y_J` term**. Let `P` be an orthogonal projection on the deterministic coefficient space `R^J`, and put

`N=MP`.                                                           (3.2)

Assume `N` has exact rank two and there is a physical row `i0` such that deleting row `i0` leaves rank at most one. Then, writing

`E2(N)=e2(N^T N)>0`,

`boxed:
 ||p_Q||_infinity
 <= 2^(3/4) sqrt(pi) E2(N)^(-1/4).
`                                                                  (3.3)

The conclusion is completely independent of `rank(M)`, the singular values of `(I-P)M^T`, and the size of any extra cross packet outside the selected coefficient plane.

### Proof

Fix `W=w`; the final bound is uniform in `w`. Conditional on `X_I=x`, (3.1) is an affine function of the independent original-product vector `Y_J`, with deterministic coefficient

`q(x,w)=2M^T x+b(w)`.                                             (3.4)

The one-dimensional product-projection theorem gives, whenever `q!=0`,

`||p_{q^T Y_J | X_I=x,W=w}||_infinity <= sqrt(2)/||q||_2`.       (3.5)

Orthogonal projection can only decrease Euclidean norm, so

`||q||_2 >= ||Pq||_2
          = ||2 P M^T x+P b(w)||_2
          = ||2 N^T x+P b(w)||_2`.                               (3.6)

Now use the physical row-star factorisation of `N`. Relabel the hub `i0=0`; then

`N=[r^T ; a v^T]`,                                                (3.7)

where `a` is a nonzero vector over the nonhub original coordinates and `r,v` are linearly independent. The complete two-volume is

`E2(N)=||a||_2^2 ||r wedge v||_2^2`.                              (3.8)

Write `X_I=(X_0,X')` and `A=a^T X'`. The original-product projection bound gives

`||p_A||_infinity <= sqrt(2)/||a||_2`,                            (3.9)

and, crucially, the untouched original coordinate `X_0` is independent of `A`. Thus

`Z=(X_0,A)`                                                        (3.10)

has a two-dimensional density cap `K_A=sqrt(2)/||a||_2`. Moreover

`N^T X_I=r X_0+vA=:LZ`,                                          (3.11)

and the planar Jacobian of `L` is

`J_2(L)=||r wedge v||_2`.                                        (3.12)

Apply the designated partner's decreasing-rearrangement lemma to the translated coefficient vector. It gives

`E ||2LZ+d||_2^(-1)
 <= sqrt(pi K_A/J_2(L))`                                         (3.13)

for every deterministic `d` in the coefficient plane. The exceptional equation `2LZ+d=0` has probability zero because `L` has rank two and `Z` has a two-dimensional density.

Average (3.5), use (3.6) with `d=P b(w)`, then (3.13):

`||p_{Q|W=w}||_infinity
 <= sqrt(2) E||2N^T X_I+P b(w)||_2^(-1)`

` <= sqrt(2) sqrt(pi * [sqrt(2)/||a||_2]/||r wedge v||_2)`

` =2^(3/4)sqrt(pi)
   [||a||_2 ||r wedge v||_2]^(-1/2)`

` =2^(3/4)sqrt(pi) E2(N)^(-1/4)`.                                (3.14)

Average over `W`. This proves (3.3). QED.

### Scope check

`P` never acts on `Y_J` as a random variable. It is used only in the deterministic inequality `||q||>=||Pq||`. Thus no independence after rotation is asserted. Arbitrary self-curvature on the `I` side remains inside `F`; arbitrary outside-conditioned affine terms remain inside `b(W)`. The only clean-bank hypothesis is the absence of quadratic `Y_J` curvature, exactly as in the partner theorem.

## 4. A full-rank orthogonal-tail family paid uniformly by the projected star

Let

`M0 = [[2,1,1],
       [1,1,1],
       [1,1,1]]`,                                                 (4.1)

`w=(0,1,-1)/sqrt(2)`, and

`M_eps=M0+eps w w^T`

`     =[[2,1,1],
        [1,1+eps/2,1-eps/2],
        [1,1-eps/2,1+eps/2]]`,                                   (4.2)

for `0<eps<=1/4`. Every physical cross coefficient is nonzero.

The vector `w` spans the kernel of `M0`; on `w^perp`, `M0` has eigenvalues `2+sqrt(2)` and `2-sqrt(2)`. Hence

`spec(M_eps)={2+sqrt(2),2-sqrt(2),eps}`                           (4.3)

and

`det M_eps=2eps`.                                                  (4.4)

Let

`P=I-w w^T`.                                                       (4.5)

Because `M0P=M0` and `w w^T P=0`,

`M_eps P=M0` **exactly for every eps**.                            (4.6)

The projected packet `M0` is an exact row star: deleting its first row leaves rank one. Its two nonzero singular values are `2+sqrt(2)` and `2-sqrt(2)`, whose product is two, so

`E2(M0)=4`.                                                        (4.7)

Apply Theorem 3.1 to

`T_eps=2X^T M_eps Y`,                                             (4.8)

where `X,Y` are arbitrary independent cap-one original-product vectors in `R^3`. The `Y` bank is quadratically clean, and therefore

`boxed:
 ||p_{T_eps}||_infinity
 <= 2^(1/4)sqrt(pi)
 =2.1078147305108117...,
`                                                                  (4.9)

uniformly for every `0<eps<=1/4` and every admissible collection of input laws.

This estimate ignores the entire weak orthogonal third cross direction before any reciprocal is taken.

## 5. Genuinely rotated indefinite full-target form

Add one further independent original coordinate `Z` and define

`Q_eps=Z^2+2X^T M_eps Y`.                                        (5.1)

Its symmetric coefficient matrix is

`A_eps = diag(1,0_3,0_3)` with the `X-Y` off-diagonal blocks equal to `M_eps` and `M_eps^T`. Therefore its exact spectrum is

`{1,
  +(2+sqrt(2)),-(2+sqrt(2)),
  +(2-sqrt(2)),-(2-sqrt(2)),
  +eps,-eps}`.                                                     (5.2)

Thus `A_eps` is indefinite and has at least the three target-scale eigenvalues

`1`, `+(2+sqrt(2))`, `-(2+sqrt(2))`,                              (5.3)

all of modulus at least one. No diagonalisation of the input law is used; every physical `X-Y` entry is nonzero.

Since `Z^2` is independent of `T_eps`, convolution cannot increase the essential supremum. Hence

`boxed:
 ||p_{Q_eps}||_infinity
 <=2^(1/4)sqrt(pi)
 =2.1078147305108117... .
`                                                                  (5.4)

For this explicit family, continuity also follows separately: the law of `Z^2` has an `L^1` density, `p_T` is in `L^1 cap L^infinity`, and translation continuity in `L^1` of the square kernel implies their convolution is continuous. This regularity statement is not promoted to the general theorem.

## 6. Actual application of Claude/e5: third-volume weighting is maximally inadmissible

The full `M_eps` is `3x3`, so its physical third-volume support consists of exactly one minor, with

`det(M_eps)^2=4eps^2>0`.                                         (6.1)

Consequently **every** probability weight on nonzero `3x3` minors is the point mass on that one minor. Every left-row inclusion marginal is exactly

`alpha_1=alpha_2=alpha_3=1`.                                     (6.2)

The completed e5 Theorem D requires marginals at most `1/2`; the proved D' extension permits only a threshold `h<3/4`. Therefore neither theorem is admissible on this actual target form at any `eps>0`. There is no alternative entropy weight to optimize: the admissible third-volume polytope is empty. The unconditional e5 five-volume theorem also has `Z5=0` here.

This is a theorem-scope obstruction, not a counterexample to QFORM. It shows that positive full rank and positive `E3` do not imply access to the three-volume route. Equation (5.4) simultaneously shows that the same matrix is harmless once one uses the product-preserving projected star.

## 7. Global optimization of every admissible two-volume weight on the same matrix

The nine physical `2x2` minors of `M_eps`, indexed by row-pairs and column-pairs `(12,13,23)`, are

`[[1+eps, 1-eps, -eps],
  [1-eps, 1+eps,  eps],
  [-eps,    eps,   2eps]]`.                                      (7.1)

Thus

`Z2=e2(M_eps^T M_eps)=4+12eps^2`.                                (7.2)

The canonical squared-minor row-pair masses are

`r12=r13=(2+3eps^2)/(4+12eps^2)`,
`r23=6eps^2/(4+12eps^2)=:r`.                                     (7.3)

Let `w` be any probability weight on nonzero two-minors, and let `x12,x13,x23` be its row-pair masses. Put

`ell=1-q/2`, so `q=2(1-ell)`.                                    (7.4)

Because every pair omits one of the three physical rows, the marginal conditions `alpha_i<=q/2` are exactly

`x12>=ell`, `x13>=ell`, `x23>=ell`.                              (7.5)

Hence a weight exists iff `ell<=1/3`, i.e. `q>=4/3`.

Let `nu` be the canonical squared-minor law. Relative entropy decomposes by row-pair class:

`D(w||nu)=D(x||r_vec)+sum_S x_S D(w(.|S)||nu(.|S))`.             (7.6)

Therefore at fixed row-pair masses the global entropy optimum preserves the canonical conditional column law. Since `r12=r13=(1-r)/2`, for `r<=ell<=1/3` the unique KL projection is

`x23=ell`, `x12=x13=(1-ell)/2`,                                  (7.7)

and

`D_min(ell)=D_Ber(ell||r)`.                                      (7.8)

Consequently the **globally optimal** entropy-adjusted two-volume is

`G2,opt(ell)=Z2 exp[-D_Ber(ell||r)]`.                             (7.9)

Using the completed weighted rank-two half-Riesz compiler (2.2) with the outside physical square `Z^2` gives

`B_vol(ell)
 =2^(5/4)sqrt(e) ell^(-1)(1-ell)^(-1/4)
   Z2^(-1/8) exp[D_Ber(ell||r)/8]`.                              (7.10)

Its logarithmic derivative is

`d/dell log B_vol
 =-1/ell+1/[4(1-ell)]
   +(1/8)log[ell(1-r)/(r(1-ell))]`,                              (7.11)

and

`d^2/dell^2 log B_vol
 =1/ell^2+1/[4(1-ell)^2]
   +(1/8)(1/ell+1/(1-ell))>0`.                                  (7.12)

Thus any critical point is the unique global optimum on the active branch.

At the concrete stress value

`eps=10^(-12)`,                                                   (7.13)

high-precision evaluation gives

`r=1.4999999999999999999999955e-24`,
`ell*=0.14436644508250644035...`,
`q*=1.71126710983498711930...`,                                  (7.14)

and

`boxed:
 B_vol,opt=60.69465364306978212528... .
`                                                                  (7.15)

So even globally optimized admissible two-volume weighting is almost a factor 29 worse than the projected-star certificate (5.4). As in the predecessor family, the full-block entropy cost is only logarithmic in `1/eps`, but it is still artificial here: the weak direction can be discarded deterministically before inversion.

## 8. Ridge comparison on the identical physical matrix

Let `g=gamma^2`. Because the weak eigenvector `w` is orthogonal to the two strong eigendirections, the regularized ridge matrix has physical diagonal

`diag K_gamma=(k,(k+h)/2,(k+h)/2)`,                              (8.1)

where

`k=(6g+4)/(g^2+12g+4)`,
`h=eps^2/(eps^2+g)`,                                              (8.2)

and

`theta=tr K_gamma=2k+h`.                                         (8.3)

### Direct ridge has no certificate at any scale

Let `m=max_i(K_gamma)_ii`. The leverage gate forces `q>=2m`. But, simply because there are three physical rows,

`theta=sum_i(K_gamma)_ii<=3m<=3q/2<2q`.                          (8.4)

Therefore the direct ridge condition `theta>2q` is impossible for every `gamma` and every admissible `q`.

### One valid square-assisted ridge certificate

Take

`gamma=eps/2`, `g=eps^2/4`, `q=2`.                              (8.5)

Then `h=4/5` and

`k=(4+3eps^2/2)/(4+3eps^2+eps^4/16)`.                           (8.6)

For `0<eps<=1/4`, `k>14/15`, so

`theta=2k+4/5>8/3=4q/3`;                                        (8.7)

the leverage condition is automatic because `K_gamma<=I` and `q/2=1`.

Using the exact eigenvalues of `M_eps`,

`D=det(I+M_eps^2/gamma^2)
 =5(1+48/eps^2+64/eps^4)`.                                      (8.8)

Thus (2.3) is a valid same-matrix certificate. At `eps=10^(-12)` it gives

`boxed:
 ||p_Qeps||_infinity <=1119.47706138150817722485... .
`                                                                  (8.9)

At this fixed ridge scale the asymptotic cost is

`1119...` replaced generally by

`B_ridge(eps)~21.61371819946173... eps^(-1/7)`.                  (8.10)

No claim is made that (8.5) globally optimizes the square-assisted ridge family. The comparison needed here is mechanism-level and source-valid: direct ridge has no certificate at all; a valid square-assisted ridge certificate is polynomially bad at the stress point; globally optimized two-volume weighting is logarithmically bad; the coefficient-projected product rearrangement is uniformly `2.108`.

## 9. What changed in the proof map

The new theorem removes a genuine class of false near-star obstructions. A full physical cross block may have arbitrarily high rank or an arbitrarily weak extra singular direction, and both the Claude/e5 three-volume gate and direct ridge may be unavailable on the full block. None of that matters if a deterministic coefficient-space plane contains a target-scale row-star packet on the clean-bank side.

The hierarchy on the single target-valid family (5.1), at `eps=10^(-12)`, is:

- e5 third-volume D/D': **inadmissible** because every row marginal is one;
- globally optimized admissible entropy-weighted two-volume: `60.6946536431...`;
- direct ridge: **no certificate**;
- one valid square-assisted ridge scale: `1119.4770613815...`;
- fresh designated-partner row-star mechanism after deterministic coefficient projection: `2.10781473051...`.

The crucial operation is not a post-rotation independence claim: it is the pointwise norm inequality `||q||>=||Pq||` before the inverse-radius expectation. Extra cross directions in `P^perp` are therefore helpful or neutral and never need to be inverted.

The full unrestricted QFORM conjecture remains **OPEN**. The remaining structural problem is to force such a coefficient projection, or a completed alternative, from the bare three-large-eigenvalue hypothesis without assuming a clean bank, a large physical minor, or a favorable spectral basis.

## 10. Integrity / regularity status

- `QFORM-COEFFICIENT-PROJECTED-ROWSTAR-CLEANBANK-v1`: analytic proof above; independent review pending.
- Explicit family `Q_eps`: exact spectrum and exact physical-minor algebra checked separately in `CHECKS.md`.
- Essential boundedness / absolute continuity: proved in theorem scope.
- Continuity: proved only for the displayed `Q_eps` after the independent `Z^2` convolution; not claimed generally.
- Full QFORM: OPEN.
- Native learned-memory ingestion: not observed; execution remains `WITHOUT_VERIFIED_BRAIN`.
- No Gaussian, moment, support, log-concavity, diagonal-basis, arbitrary-joint coarea, conditional-cap moment, or post-rotation-independence premise is used.
