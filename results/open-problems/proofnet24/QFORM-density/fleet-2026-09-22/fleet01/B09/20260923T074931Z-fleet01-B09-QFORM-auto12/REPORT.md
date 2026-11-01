SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B09, 2026-09-23T07:49:31Z.
attacking: an original-coordinate two-hub star with arbitrary within-bank quadratic curvature, by conditioning a low-leverage curvature vertex cover and preserving the hub wedge quantitatively.

# fleet01/B09 auto12 — punctured-frame vertex-cover smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN. The result below pays a new class of two-hub/star configurations with genuinely arbitrary same-bank quadratic coefficients on a conditioned curvature core. It keeps all original-coordinate independence, gives a linear interval estimate, and proves continuity in its stated scope.

No moment, compact-support, connected-support, Gaussian, log-concave, identical-law, post-rotation-independence, arbitrary-joint coarea, worst conditional-density supremum, or law-uniform pointwise stationary-phase assertion is used. No matrix coefficient is discarded as a small random perturbation.

## 1. Exact predecessor used

The designated partner `fleet02/B09` completed

`QFORM-TWOHUB-PLUCKER-SMOOTHING-v1`

at

`yspennstate/math-open-problems@bc348aa1a3631b0a0a3a9939cbb6b023578e9abc`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260923T064043Z-fleet02-B09-QFORM-r13/REPORT.md`.

Its `r=0` endpoint is the following. Split unconditioned original coordinates into two literal physical hubs `H={h1,h2}` and a leaf bank `I`. If the exact leaf principal block is diagonal and the two hub-to-leaf columns form a matrix `C_I` with

`G_I=C_I^T C_I>0`,

let `rho_I` be the probability that two iid bases drawn from the Pluecker basis law of `U_I=C_I G_I^(-1/2)` are disjoint. Then, with an arbitrary physical `2 x 2` hub core, arbitrary affine terms, and arbitrary already-conditioned outside blocks,

`||p_Q||_infinity <= 2 sqrt(e) [rho_I det(G_I)]^(-1/4)`.       (1.1)

The density is continuous and

`P{Q in L} <= 2 sqrt(e) [rho_I det(G_I)]^(-1/4) |L|`.         (1.2)

I apply this theorem quantitatively below; the new work is to show that a whole class of arbitrary within-bank curvature can be conditioned away while retaining a dimension-free lower bound on the exact determinant-disjointness certificate.

## 2. Setup: arbitrary curvature behind a vertex cover

Split the original independent coordinates into

`H={h1,h2}`, a leaf bank `L`, and an outside bank `J`.           (2.1)

No assumption is placed on the physical hub block `A_HH`, on `A_HJ`, `A_LJ`, or `A_JJ`. Write

`C=A[L,H]`,                                                      (2.2)

viewing `C` as an `|L| x 2` matrix. For each `i in L`, let `c_i` be its row. Put

`G=C^T C`,                                                       (2.3)

and assume `G>0`.

Let `K subset L`, put `I=L\K`, and assume only that `K` is a vertex cover of the off-diagonal support of the exact leaf block:

`A_ij=0` for every distinct `i,j in I`.                          (2.4)

Thus every non-diagonal leaf-leaf coefficient is allowed, provided at least one endpoint lies in `K`. In particular, `A_KK` can be fully dense and arbitrarily large, and every coefficient between `K` and `I` is arbitrary.

Define the full two-frame row leverages

`p_i = c_i^T G^(-1) c_i`,                                      (2.5)

so

`sum_(i in L) p_i = 2`.                                        (2.6)

Set

`theta = sum_(i in K) p_i`,
`q = max_(i in I) p_i`.                                        (2.7)

The useful regime is

`theta + 2q < 1`.                                               (2.8)

## 3. New theorem — `QFORM-TWOHUB-VERTEXCOVER-PUNCTURE-v1`

Under (2.1)--(2.8), for arbitrary independent real input variables with densities at most one, the full quadratic form `Q=X^T A X` has a continuous density satisfying

`boxed:
 ||p_Q||_infinity
 <= 2 sqrt(e) [(1-theta-2q) det(G)]^(-1/4).`                   (3.1)

Consequently every interval `D` obeys

`boxed:
 P{Q in D}
 <= 2 sqrt(e) [(1-theta-2q) det(G)]^(-1/4) |D|.`               (3.2)

This result is completely insensitive to the size, sign and rank of the curvature incident to `K`. The only payment is the amount of the two-hub coefficient-frame leverage removed when `K` is conditioned.

### Proof

Condition on the original coordinates `X_K` and `X_J`. Because the input law is a product law, the two hubs and the coordinates in `I` remain mutually independent with their original one-dimensional density caps. Every quadratic term having an endpoint in `K` or `J` becomes either an affine term in the surviving variables or a constant. By (2.4), the surviving `I x I` quadratic block is diagonal. Therefore the conditional form is exactly in the `r=0` scope of the partner theorem (1.1).

It remains to lower-bound the partner certificate for the punctured two-frame.

Let

`C_K=A[K,H]`, `C_I=A[I,H]`,
`G_I=C_I^T C_I=G-C_K^T C_K`.                                  (3.3)

Whiten with the **full** deterministic frame and define

`R_K=G^(-1/2) C_K^T C_K G^(-1/2)`.                            (3.4)

Then `R_K` is positive semidefinite and

`tr R_K = theta`.                                               (3.5)

Because `theta<1`,

`0 <= R_K <= theta I_2 < I_2`.                                (3.6)

Moreover

`G_I=G^(1/2)(I_2-R_K)G^(1/2)`,                                (3.7)

so `G_I>0` and

`det G_I
 = det G det(I_2-R_K)
 = det G [1-tr R_K+det R_K]
 >= (1-theta) det G`.                                          (3.8)

For `i in I`, let

`ell_i=c_i^T G_I^(-1)c_i`                                      (3.9)

be its leverage in the punctured normalized frame. From (3.6)--(3.7),

`G_I^(-1)
 <= (1-theta)^(-1) G^(-1)`,                                   (3.10)

hence

`ell_i <= p_i/(1-theta) <= q/(1-theta)`.                       (3.11)

Now form `U_I=C_I G_I^(-1/2)`, so `U_I^T U_I=I_2`. For its Pluecker basis law on two-element subsets,

`w_{ab}=det((U_I)_{a,b})^2`,                                   (3.12)

Cauchy--Binet gives `sum w_ab=1`, and the inclusion marginal of coordinate `i` is exactly

`P{i in S}=ell_i`.                                              (3.13)

Let `S,T` be iid draws from this law. Then

`P{S cap T != empty}
 <= E |S cap T|
 = sum_(i in I) ell_i^2
 <= [max_i ell_i] sum_i ell_i
 = 2 max_i ell_i`.                                              (3.14)

The last equality uses `sum_i ell_i=tr(I_2)=2`. Therefore the partner disjointness mass satisfies

`rho_I=P{S cap T=empty}
 >= 1 - 2q/(1-theta)
 = (1-theta-2q)/(1-theta)`.                                   (3.15)

Multiplying (3.8) and (3.15) gives the key cancellation:

`boxed:
 rho_I det G_I
 >= (1-theta-2q) det G.`                                      (3.16)

Apply the completed partner inequality (1.1) conditionally on `(X_K,X_J)` and use (3.16). The bound is deterministic and uniform in the conditioning values, so averaging preserves it and gives (3.1)--(3.2).

For continuity, each conditional density supplied by the partner theorem is continuous, and all are bounded by the same deterministic right side of (3.1). If `t_n -> t`, dominated convergence applied to the conditional density representation gives `p_Q(t_n)->p_Q(t)`. Thus the unconditional density is continuous. QED.

There is no squaring of a small-ball probability. The final estimate is exactly linear in interval length.

## 4. Star corollary: arbitrary weighted within-bank star

Suppose the exact off-diagonal part of `A_LL` is an arbitrary weighted star centered at one physical leaf `s`; that is,

`A_ij=0` for distinct `i,j` outside `{s}`.                      (4.1)

Take `K={s}`. The star weights `A_sj`, the diagonal entries, the hub core, all outside blocks and all affine terms are arbitrary. Let

`p_s=c_s^T G^(-1)c_s`,
`q=max_(i != s) c_i^T G^(-1)c_i`.                              (4.2)

If

`p_s+2q<1`,                                                     (4.3)

then

`boxed:
 ||p_Q||_infinity
 <=2sqrt(e)[(1-p_s-2q)det G]^(-1/4).`                          (4.4)

This is the requested original-coordinate hub/star mechanism with arbitrary within-bank star curvature. The center is conditioned, not rotated. All of its arbitrary quadratic interactions become translations/linear terms, exactly within the partner theorem's scope.

More generally, (3.1) pays any arbitrary curvature graph admitting a vertex cover whose **total hub-frame leverage**, rather than its cardinality, is small.

## 5. Actual application of the designated partner theorem

A clean target-valid family shows the scale of (3.1). Take literal physical hubs `h1,h2`, a star center `s`, and three disjoint groups `G1,G2,G3` of size `m>=3`. Put

`u_a=m^(-1/2) 1_(G_a)`, `a=1,2,3`,                            (5.1)

and take the quadratic matrix whose only off-diagonal blocks are the three normalized stars

`h1 -- u1`, `h2 -- u2`, `s -- u3`,                            (5.2)

with coefficient one in matrix notation, so

`Q=2 X_h1 <u1,X_G1>
  +2 X_h2 <u2,X_G2>
  +2 X_s  <u3,X_G3>`.                                         (5.3)

The matrix is an orthogonal direct sum of three rank-two hyperbolic blocks and zeros; its nonzero spectrum is

`{1,-1,1,-1,1,-1}`.                                            (5.4)

Thus it satisfies the full target spectral hypothesis. For the two designated hubs, the full leaf frame has

`G=I_2`, `det G=1`, `p_s=0`, `q=1/m`.                         (5.5)

The leaf curvature relative to these two hubs is the arbitrary star centered at `s`; condition that center and apply the **completed fleet02/B09 r13 theorem** to the punctured diagonal bank. Formula (4.4) gives the actual inequality

`boxed:
 ||p_Q||_infinity
 <=2sqrt(e)(1-2/m)^(-1/4),`                                   (5.6)

and the same coefficient times `|D|` bounds every interval. For `m=8`,

`||p_Q||_infinity <3.544`.                                     (5.7)

This application is at the physical-coordinate level; no claim is made that the group averages themselves inherit density cap one.

## 6. Improvement on the already-paid strict-N3 diffuse star control

The earlier fleet01/B09 strict-N3 global-star extraction gave a two-column physical cross frame `C` with

`s_2(C)>=1-delta`,
`delta=1/128+sqrt(1/128+1/128^2)=0.0965454429...`,             (6.1)

and every row leverage at most

`ell=2(1/128+1/128^2)/(1-delta)^2
   =0.0192924392...`.                                          (6.2)

That branch already has diagonal residual leaves after elevating the star center to a physical hub, so here `K=empty`, `theta=0`, `q<=ell`. Since

`det(C^TC)>=s_2(C)^4`,                                         (6.3)

(3.1), equivalently the actual partner r13 `r=0` inequality plus (3.14), improves its previous `<4.428` bound to

`||p_Q||_infinity
 <=2sqrt(e)(1-2ell)^(-1/4)/(1-delta)
 <3.686`.                                                       (6.4)

This is an improvement of an already-paid branch, not a claim that N3 is solved.

## 7. What this changes and the first unpaid implication

The partner r13 frontier was

`QFORM-TWOHUB-HIGHRANK-OR-LOCALIZED-LEAF-ROUTING-v1`:

starting from a quantitative two-row hub wedge, deal with arbitrary same-side leaf curvature when the exact low-rank Pluecker packet is unavailable.

The present theorem closes a substantial localized-curvature part of that frontier: **all** non-diagonal leaf curvature can be arbitrary on a vertex cover `K`, and can be removed exactly whenever its total hub-frame leverage plus twice the largest surviving row leverage is below one. In particular, arbitrary weighted stars are paid under the explicit leverage criterion (4.3).

The first unpaid implication is now

`QFORM-TWOHUB-NO-LOWLEVERAGE-COVER-TO-CROSSVOLUME-v1`:

> Given a quantitative two-row hub wedge and an arbitrary leaf block for which every curvature vertex cover `K` violates `theta_K+2 q_K<1`, prove that the remaining curvature forces one of the already-paid matrix-level exits: a quantitative cross-volume/tail certificate, a ridge/diffuse certificate, a determinant-balanced low-rank packet, or a bounded physical core retaining the third spectral resource.

This is a genuinely different structural task from deleting a small matrix perturbation. It should be attacked by thresholding the actual leaf off-diagonal coefficients and converting failure of a low-leverage vertex cover into a quantitative matching/cross-volume certificate, with cancellation checked at the level of singular values/volumes rather than individual entries.

Full QFORM and full-target continuity remain OPEN. Independent end-to-end review of the new theorem is not yet claimed.
