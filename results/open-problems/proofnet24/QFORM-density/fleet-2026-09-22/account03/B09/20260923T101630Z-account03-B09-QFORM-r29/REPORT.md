SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-23T10:16:30Z.
attacking: remove the literal-physical-hub bottleneck in determinant-balanced bilinear smoothing by collapsing an arbitrary original-coordinate hub bank to its cross-range projection, keeping arbitrary same-bank hub curvature as a bounded complex amplitude.

# account03/B09 r29 — grouped-hub determinant-balanced bilinear smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Bilinear block mechanism  
Status: **NEW SUPPORTING ANALYTIC THEOREM / PEER PROJECTION THEOREM APPLIED / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains **OPEN**. The new theorem below removes an artificial restriction present in the completed two-hub and multi-hub Pluecker smoothing theorems: the smoothing variables no longer need to be literal physical coordinates. An arbitrarily large original-coordinate bank may be compressed to the finite-dimensional range of its cross block, while all quadratic curvature internal to that bank is retained exactly as a unit-modulus conditional phase. The only probabilistic price is the joint density cap of that finite-dimensional projection, which is supplied dimension-free by the completed weighted affine-fiber Brascamp--Lieb theorem.

No post-rotation independence is used. The projected coordinates may be dependent. No moment, compact-support, connected-support, log-concavity, Gaussian, diagonal-basis, arbitrary-joint coarea, worst conditional fiber supremum, or law-uniform pointwise quadratic-phase decay is used. The characteristic function is bounded by an integrable envelope directly, so the final small-ball estimate is genuinely `O(|L|)` and does not come from square-root decoupling.

## 1. Fresh controls and source-pinned dependencies

Fresh control was read from `yspennstate/math-research-brain` main at commit

`c393c6af9218e1c22871c899ce8a3823556b6ee9`.


The direct predecessor is account03/B09 r27,

`yspennstate/math-open-problems@e6d2395b5b13bf75552b015668177a0270d3e89f`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T091354Z-account03-B09-QFORM-r27/REPORT.md`.

It proved chirp-stable physical-pivot smoothing and a weighted star/triangle stability lemma, leaving a localization-heavy frontier. A same-hour account03/B09 r28 run already owns the canonical `10Z` login and is pursuing that local near-star/near-triangle route, so this run deliberately changes mechanism to an aggregate bank theorem rather than racing the same local branch.

The completed determinant-balanced analytic source is account02/B09

`QFORM-TWOHUB-PLUCKER-SMOOTHING-v1`,

`yspennstate/math-open-problems@bc348aa1a3631b0a0a3a9939cbb6b023578e9abc`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T064043Z-account02-B09-QFORM-r13/REPORT.md`.

The completed projection theorem applied at an actual inequality below is account02/B06

`QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`,

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`.

For an `n x h` matrix `P` with orthonormal columns and an original-coordinate cap-one product source `X`, it gives

`||p_(P^T X)||_infinity <= exp(h/2).`                            (1.1)

The newest account01/B09 theorem

`QFORM-MULTIHUB-PLUCKER-SMOOTHING-v1`,

`yspennstate/math-open-problems@b7fca6f016b94984bfdfdb30e4c183fafff77443`,

is the literal-physical-hub analogue of the theorem proved here. The present proof identifies the extra step needed to replace those literal hubs by a dependent grouped projection.

A fresh canonical search found no completed current-QFORM `account04/B09` artifact, so no designated-partner theorem is fabricated or awaited.

## 2. Setup: an arbitrary original-coordinate hub bank

Partition the original independent coordinates into three disjoint sets

`H union I union J`.

The bank `J` will be conditioned. Let

`B=A[H,I]`

have rank `h>=1`. Choose a thin factorization

`B=P C^T`,                                                       (2.1)

where

`P in R^(|H| x h)`, `P^T P=I_h`,
`C in R^(|I| x h)`.

For example, in a thin SVD `B=P Sigma R^T`, take `C=R Sigma`. Thus the nonzero singular values of `B` are exactly the singular values of `C`.

Assume that the exact `I x I` principal block has the form

`A_II=D+sum_(k=1)^r lambda_k v_k v_k^T`,                        (2.2)

where `D` is diagonal, `r>=0`, and every displayed `lambda_k` is nonzero. No condition is imposed on `A_HH`, on any block involving `J`, or on affine terms generated after conditioning.

Form

`W=[v_1,...,v_r,c_1,...,c_h] in R^(|I| x (r+h))`,               (2.3)

where `c_a` are the columns of `C`, and put

`d=r+h`, `G=W^T W`.                                              (2.4)

Assume `G>0`. Whiten only this deterministic coefficient frame,

`U=W G^(-1/2)`, so `U^T U=I_d`.                                 (2.5)

For every `d`-subset `S` of physical leaf coordinates define

`w_S=det(U_S)^2`.                                                (2.6)

Cauchy--Binet gives `sum_S w_S=1`. Let `S,T` be iid from this Pluecker basis law and define

`rho=P(S cap T=empty)`.                                         (2.7)

The random coordinates themselves are never whitened or rotated.

Finally set

`Y=P^T X_H`.                                                     (2.8)

The coordinates of `Y` need not be independent. Suppose only that `Y` has a density `g_Y` with

`||g_Y||_infinity <= M`.                                        (2.9)

## 3. Main theorem

### Theorem `QFORM-GROUPED-HUB-PLUCKER-SMOOTHING-v1`

Assume

`r+2h>2`, `rho>0`, and the setup of Section 2.

Then the full quadratic form has a bounded **continuous** density and

`boxed:
||p_Q||_infinity
 <= C_(h,r) M^(2/(r+2h))
    [rho det(G) prod_(k=1)^r |lambda_k|]^(-1/(r+2h)),`          (3.1)

where

`C_(h,r)=((r+2h)/(r+2h-2)) exp((r+h)/(r+2h)).`                  (3.2)

Consequently every interval `L` satisfies

`boxed:
P{Q in L}
 <= C_(h,r) M^(2/(r+2h))
    [rho det(G) prod_k |lambda_k|]^(-1/(r+2h)) |L|.`            (3.3)

The block `A_HH` is completely arbitrary. In particular, it may be dense, indefinite, singular, or large. The theorem does not assume that the `h` projected hub coordinates are independent.

### Proof

Condition on the original coordinates `X_J`. This preserves independence between the original-coordinate banks `X_H` and `X_I`. It changes only affine terms and an additive constant in the active form.

Write all terms depending only on the hub bank as a measurable real phase `F_H(X_H)`. Since the only hub-to-leaf quadratic interaction is (2.1), the active form can be written

`Q=F_H(X_H)
   + sum_(i in I) D_ii X_i^2
   + sum_(k=1)^r lambda_k (v_k^T X_I)^2
   + 2 (P^T X_H)^T C^T X_I
   + ell_I^T X_I + constant.`                                  (3.4)

For fixed `t`, disintegrate the hub-bank product law under `Y=P^T X_H` and define the complex amplitude

`a_t(y)=g_Y(y) E[exp(i t F_H(X_H)) | Y=y].`                     (3.5)

This is the key grouped-hub step. It preserves all same-bank hub curvature exactly and gives merely

`|a_t(y)|<=g_Y(y)<=M.`                                         (3.6)

No independence of the coordinates of `Y` is asserted or needed.

Insert (3.5) into the characteristic function and substitute

`q=2 t y in R^h`.                                               (3.7)

The Jacobian is

`dy=(2|t|)^(-h) dq`,                                            (3.8)

and by (3.6) the hub contribution after absolute values costs at most

`M (2|t|)^(-h)`.                                                (3.9)

Now Fresnel-linearize each displayed square in (2.2). In absolute value the `r` squares contribute

`prod_(k=1)^r (4 pi |t lambda_k|)^(-1/2).`                      (3.10)

After the substitutions (3.7) and the `r` Fresnel variables, the remaining leaf integral factorizes over the **original** independent coordinates in `I`. It has the exact form

`J_t=int_(R^d) prod_(i in I)
      |hat g_(i,t)(<W_i,z>+b_i)| dz`,                           (3.11)

where each one-coordinate complex amplitude satisfies

`|g_(i,t)(x)|=f_i(x)`.                                          (3.12)

The diagonal entries of `D` and every conditioning-generated affine term are contained in these unimodular one-coordinate phases.

Use the deterministic whitening `z'=G^(1/2)z`. Then

`J_t=det(G)^(-1/2)
 int_(R^d) prod_i |hat g_(i,t)(<U_i,z'>+b_i)| dz'.`             (3.13)

Apply the completed determinant-weighted entropy Brascamp--Lieb estimate used in the account02/B09 theorem. Conditioning two iid Pluecker bases on disjointness gives the admissible basis law and yields

`J_t <= det(G)^(-1/2)(2 pi)^d e^(d/2) rho^(-1/2).`             (3.14)

Combining (3.9), (3.10), and (3.14), all powers of two cancel:

`2^(-h) 2^(-r) 2^(r+h)=1`.                                    (3.15)

The power of `pi` is

`pi^(-r/2) pi^(r+h)=pi^(h+r/2)`.                               (3.16)

Set

`alpha=h+r/2=(r+2h)/2>1`                                       (3.17)

and

`R=rho det(G) prod_k |lambda_k|`.                              (3.18)

We obtain the uniform conditional envelope

`|phi_Q(t)|
 <= M pi^alpha e^((r+h)/2) R^(-1/2) |t|^(-alpha).`             (3.19)

The same envelope holds after averaging over the conditioned bank `J`.

Together with `|phi_Q(t)|<=1`, if

`A_0=M pi^alpha e^((r+h)/2) R^(-1/2)`,                          (3.20)

then

`int_R |phi_Q(t)| dt
 <= 2 alpha/(alpha-1) A_0^(1/alpha).`                           (3.21)

Fourier inversion therefore gives

`||p_Q||_infinity
 <= alpha/[pi(alpha-1)] A_0^(1/alpha)`

`= ((r+2h)/(r+2h-2))
   exp((r+h)/(r+2h))
   M^(2/(r+2h))
   R^(-1/(r+2h)),`                                              (3.22)

which is (3.1). Since `phi_Q in L^1`, Fourier inversion also yields a continuous density. Integrating that density over an interval proves (3.3). QED.

The proof uses no probability squaring. The direct `|t|^(-alpha)` envelope has exponent strictly larger than one, and that is why the interval estimate stays linear.

## 4. Product-law corollary: the grouped projection costs only `exp(h/2)`

We now apply the completed account02/B06 theorem at an actual inequality. Since `P^T P=I_h` and `X_H` is still an original-coordinate product source with coordinate densities at most one, `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` gives

`boxed: M=||p_(P^T X_H)||_infinity <= e^(h/2).}`                (4.1)

Substitute this into (3.1). Because

`[e^(h/2)]^(2/(r+2h))
 * exp((r+h)/(r+2h))
 = exp((h+r+h)/(r+2h))=e`,                                     (4.2)

the exponentials collapse exactly.

### Corollary `QFORM-GROUPED-CROSS-PLUCKER-LINF-v1`

Under Sections 2--3 with the actual target product input law,

`boxed:
||p_Q||_infinity
 <= e (r+2h)/(r+2h-2)
    [rho det(G) prod_k |lambda_k|]^(-1/(r+2h)).`                (4.3)

The density is continuous and every interval has probability at most the displayed constant times its length.

Two useful endpoints are

`h=2,r=0:`

`boxed: ||p_Q||_infinity <=2e [rho det(C^T C)]^(-1/4),`         (4.4)

and

`h=3,r=0:`

`boxed: ||p_Q||_infinity <=(3e/2)[rho det(C^T C)]^(-1/6).`      (4.5)

Since `C` has the same nonzero singular values as the physical cross block `A[H,I]`, (4.4) is an aggregate rank-two bank estimate, not a reciprocal fixed-minor estimate.

## 5. A target-valid diffuse family where literal physical hubs lose scale

The grouped theorem has a scope not covered uniformly by selecting literal physical hubs.

Let `N` be even and let `P in R^(N x 2)` have rows

`p_j=(1,s_j)/sqrt(N)`,                                         (5.1)

where exactly half the signs `s_j` are `+1` and half are `-1`. Then `P^T P=I_2`.

Let the leaf bank consist of two disjoint groups of size `m>=2`. Define `C in R^(2m x 2)` by

`c_i=(m^(-1/2),0)` on the first group,
`c_i=(0,m^(-1/2))` on the second group.                         (5.2)

Then `C^T C=I_2`. Set

`B=P C^T`                                                       (5.3)

and take the symmetric quadratic-form matrix

`A=[[0,B],[B^T,0]]`.                                            (5.4)

Its nonzero spectrum is exactly

`{-1,-1,1,1}`,                                                  (5.5)

because the two nonzero singular values of `B` are both one. Hence this is a literal full-target family with at least four eigenvalues of modulus one.

Every physical cross coefficient has magnitude only

`1/sqrt(Nm)`.                                                    (5.6)

The whitened leaf frame is already `C`. Its Pluecker basis law chooses one coordinate from each leaf group, uniformly, so

`rho=(1-1/m)^2`.                                                 (5.7)

Apply (4.4): for **every** admissible cap-one product input law,

`boxed:
||p_(X^T A X)||_infinity
 <=2e (1-1/m)^(-1/2).`                                         (5.8)

For `m=16`,

`boxed: ||p_(X^T A X)||_infinity <5.615.}`                      (5.9)

The density is continuous and the same number multiplies interval length.

This is genuinely an aggregate-before-inversion gain. If two literal physical hub coordinates `j,k` are selected, their two cross rows have Gram determinant zero when `s_j=s_k`, and only

`4/N^2`                                                        (5.10)

when `s_j!=s_k`. A literal two-hub determinant payment therefore carries a factor of order `sqrt(N)`. The grouped theorem first projects the entire original hub bank to its two-dimensional cross range, uses the product-law projection theorem there, and retains a constant independent of `N`.

The two projected hub variables in this example are linear combinations of all `N` original hub coordinates and are generally dependent. The proof never treats them as independent.

## 6. What this removes, and what remains

This run removes the **literal-hub bottleneck** from the determinant-balanced bilinear mechanism. Whenever an original-coordinate cut has finite cross rank `h`, all curvature on the entire source bank may remain arbitrary; only the `h`-dimensional projected source density is needed, and the completed affine-fiber theorem supplies it with a dimension-free cap. Thus diffuse physical rows are no longer a reason to pay a vanishing local cross minor.

The first remaining B09 implication on this mechanism is

`QFORM-GROUPED-CROSS-TO-GENERAL-LEAF-CURVATURE-v1`:

> Starting from a quantitative grouped cross block, either extract a determinant-balanced diagonal-plus-low-rank packet from the opposite bank at universal scale, or combine the grouped-hub amplitude argument with the opposite bank's full quadratic curvature without replacing it by a worst conditional density. A successful routing must preserve the original-coordinate product law and must not discard small coefficients as random errors.

This is a structural/curvature forcing problem. The bare three-large-eigenvalue hypothesis has **not** yet been shown to force the hypotheses of Theorem 3, so the full QFORM conjecture remains OPEN. Full-target continuity likewise remains OPEN, although continuity is proved in the exact grouped-hub scope above.

## 7. Integrity and run-collision note

The canonical account03/B09 `2026-09-23T10Z` login already existed when this invocation attempted its create-only login. It belongs to the distinct same-hour run `20260923T100501Z-account03-B09-QFORM-r28`. Following the protocol, that login was preserved rather than overwritten. This run uses the unique run ID `20260923T101630Z-account03-B09-QFORM-r29` and separate immutable start/finish/receipt paths.

Changed files for this run are confined to its immutable account03/B09 mathematics bundle and corresponding short handoff, worker memory, and run records. No schedule, notification, email, public release, permission, credential, remote workflow, paid API/model/Codex call, or cross-account authentication state is changed.
