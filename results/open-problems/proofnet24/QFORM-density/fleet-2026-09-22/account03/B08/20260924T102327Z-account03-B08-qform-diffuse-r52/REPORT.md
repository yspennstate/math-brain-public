SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-24T10:23:27Z.
attacking: the split-slope mismatch in the exact two-eigenvalue child endpoint by converting it into a genuinely diffuse third Schur direction before the physical square is peeled.

# account03/B08 r52 — split-mismatch Schur-Fresnel closure away from the tiny transverse collar

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T102327Z-account03-B08-qform-diffuse-r52`  
Assignment: diffuse eigenvector case  
Status: **NEW SUPPORTING DENSITY THEOREM + EXACT-TAIL COLLAR SHRINKING / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**.

The unrestricted conjecture remains OPEN. Global continuity remains OPEN. The theorem below proves essential boundedness on a new exact-child-tail branch. The inherited third-compound branch is continuous `C_0`; the new Schur-Fresnel/square-peel branch is recorded only as an essential-density bound.

No Gaussian, log-concavity, moment, compact-support, connected-support, identical-law, post-rotation independence, arbitrary-joint coarea, fiber supremum, law-uniform pointwise quadratic-phase decay, or perturbative deletion of a random quadratic term is used.

## 1. Fresh source state

Fresh owner/control files were read from `yspennstate/math-research-brain` main before the mathematics. OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only; the programme manifest remains revision `2026-09-22.5` and `FULL_CONJECTURE_OPEN`.

Immediate same-slot predecessor:

- `yspennstate/math-open-problems@b72d0f5814183fc536c65a4b9dbbbec4ae93d611`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260924T092359Z-account03-B08-qform-diffuse-r51/REPORT.md`.

Its surviving geometry has one ORIGINAL physical hub and a child:

`A = [[a,b^T],[b,C]]`,

`C=V Lambda V^T+E`,

where `V in R^(m x 2)` has orthonormal columns, the two large child singular values obey

`m_2 >= m_0 L`, `m_0=sqrt(47/48)=0.9895285072531598...`,

and

`max_i ||V_{i,*}||_2^2 <= mu`, `mu=1/16`.

The predecessor selected an ORIGINAL-coordinate physical half-cut `J disjoint_union K` with

`G=V_J^T V_J >= g I_2`,
`H=V_K^T V_K=I_2-G >= g I_2`,

`g=1/2-1/(4sqrt(2))=0.32322330470336313...`.

Define the bankwise least-squares coefficients and residuals

`c_J=G^(-1)V_J^T b_J`, `r_J=b_J-V_J c_J`,
`c_K=H^(-1)V_K^T b_K`, `r_K=b_K-V_K c_K`,

`delta=c_J-c_K`, `e^2=||r_J||^2+||r_K||^2`,

and let

`c_*=G c_J+H c_K`,
`u=b-Vc_*`, `beta=||u||=dist(b,range(V))`.

The predecessor proved exactly

`beta^2=e^2+delta^T G H delta`.                                  (1.1)

It also proved the tunable literal-crossing payment: with `eta=2^(-20)`, a star distance at least `eta L` from either top-two crossing singular plane gives a continuous density bound `<2369.566/L`.

Analytic input used here for the new branch is the completed rank-three spread Fresnel theorem as source-pinned and re-used in

- `yspennstate/math-open-problems@f9b52864d58b3a80fbc59b48e247af8e9a759a6f`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260924T094535Z-account02-B03-QFORM-auto11-r53/REPORT.md`.

At its exact scope: if `S=UMU^T`, `U^TU=I_3`, every physical row leverage of `U` is at most `1/2`, and the original inputs are independent with density caps one, then

`||p_(Y^T S Y)||_infinity <= 12 |det M|^(-1/3)`,                 (1.2)

with a continuous `C_0` density. This is a product-coordinate Fresnel estimate; it does not assert independence of the spectral coordinates.

The elementary two-sided cap-to-half-Riesz bound used below is

`p_R<=M`, `int p_R=1`  =>  `sup_t E|R-t|^(-1/2) <=2 sqrt(2M)`.    (1.3)

It is the bathtub/rearrangement bound already used in the completed same-bank square-hyperbolic receiver.

## 2. The hidden mismatch vector is an actual diffuse physical direction

The first new point is to expose the vector hidden behind (1.1), not merely its norm.

Put

`r=(r_J,r_K)`

and define the split-mismatch vector

`w=( V_J H delta, -V_K G delta )`.                               (2.1)

Because `G+H=I` and `GH=HG`,

`V^T w = G H delta-H G delta=0`.                                 (2.2)

The bankwise least-squares orthogonality gives

`V^T r=0`, `r.w=0`.                                               (2.3)

Moreover

`u=b-Vc_* = r+w`.                                                 (2.4)

A direct computation gives

`||w||^2`
` =delta^T(HGH+GHG)delta`
` =delta^TGHdelta`.                                               (2.5)

Thus (1.1) is the literal orthogonal Pythagoras decomposition

`boxed: beta^2=||r||^2+||w||^2.`                                 (2.6)

The mismatch direction is itself quantitatively diffuse. Let `v_i^T` be row `i` of `V`. For `i in J`,

`w_i=v_i^T H delta`,

and for `i in K`,

`w_i=-v_i^T G delta`.

Since every eigenvalue of `G` lies in `[g,1-g]`, simultaneous diagonalization of `G,H` gives

`||H delta||^2 <=[(1-g)/g] delta^TGHdelta`,
`||G delta||^2 <=[(1-g)/g] delta^TGHdelta`.                       (2.7)

Therefore, using `||v_i||^2<=mu`,

`boxed: max_i w_i^2/||w||^2 <= alpha`,

`alpha:=mu(1-g)/g=0.1308647700847534...`.                         (2.8)

This is a deterministic original-coordinate statement. No probabilistic independence of `w.X` from `V^T X` is asserted.

## 3. A four-to-one mismatch threshold forces a diffuse three-frame

Suppose

`beta>4e`.                                                        (3.1)

Then `e/beta<1/4`. Since `u=r+w`, for every physical coordinate

`|u_i|/beta`
` <= |w_i|/beta+|r_i|/beta`
` <= sqrt(alpha)+1/4`.                                            (3.2)

Also `u perp range(V)` by construction. Hence

`U=[V,u/beta]`

has orthonormal columns, and every physical row leverage satisfies

`||U_{i,*}||^2`
` <= mu+(sqrt(alpha)+1/4)^2`
` =0.436740950167119... <1/2.                                    (3.3)

This is the key gain over the previous run: a sufficiently genuine split-slope mismatch does not merely produce a bounded-density scalar projection; it manufactures a full **diffuse third spectral carrier direction** which is admissible for the completed rank-three Fresnel receiver.

## 4. Main theorem — split-mismatch Schur-Fresnel square peel

### `QFORM-EXACTTAIL-SPLITMISMATCH-SCHUR-FRESNEL-v1`

Assume

`C=V Lambda V^T`                                                  (4.1)

exactly, where `V^TV=I_2`, `Lambda=Lambda^T` is invertible, and the cut/least-squares objects above satisfy the live gates `mu<=1/16`, `G,H>=gI`. Let

`beta=dist(b,range(V))>0`.

If

`beta>4e`                                                         (4.2)

and the physical hub pivot is nonzero,

`a!=0`,                                                           (4.3)

then for every admissible cap-one product law the quadratic form

`Q=aX_0^2+2X_0<b,Y>+Y^T V Lambda V^T Y`

has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <=4 sqrt(6) [ |a| beta sqrt(|det Lambda|) ]^(-1/3).
}`                                                                  (4.4)

No continuity conclusion is asserted from this square-peel proof.

### Proof

Write

`b=Vc_*+u`, `u perp range(V)`, `||u||=beta`,

and set `uhat=u/beta`. Complete the ORIGINAL physical hub square:

`Q`
`=a(X_0+a^(-1)<b,Y>)^2+Y^T S Y`,                                 (4.5)

where

`S=V Lambda V^T-a^(-1)bb^T`.                                     (4.6)

Let `U=[V,uhat]`. In this orthonormal three-frame, `S=U M U^T` with

`M = diag_block(Lambda,0)-a^(-1) q q^T`,
`q=(c_*,beta)`.                                                    (4.7)

Because `beta!=0`, `M` is invertible. Taking the Schur complement of its bottom-right entry `-beta^2/a` gives the exact determinant identity

`boxed: det M = -(beta^2/a) det Lambda.`                           (4.8)

Indeed the rank-one correction in the top-left block cancels exactly against the off-diagonal Schur term, leaving `Lambda`.

By Section 3 the physical leverage of `U` is `<1/2`. Apply the completed rank-three spread Fresnel theorem (1.2) to

`R=Y^T S Y`.

It gives

`||p_R||_infinity`
` <=12 |det M|^(-1/3)`
` =12 [beta^2 |det Lambda|/|a|]^(-1/3).                            (4.9)

Now condition on `Y`. The shifted random variable

`a(X_0+a^(-1)<b,Y>)^2`

has, for each fixed `Y`, a density bounded by

`|a|^(-1/2)|s|^(-1/2)`                                           (4.10)

on the appropriate half-line. Mixing these conditional densities therefore gives, for a.e. `t`,

`p_Q(t)`
` <=|a|^(-1/2) E |t-R|^(-1/2).`                                  (4.11)

Apply (1.3) with the cap in (4.9):

`p_Q(t)`
` <=|a|^(-1/2) 2 sqrt(24) |det M|^(-1/6)`
` =4sqrt(6) |a|^(-1/2)`
`   [beta^2 |det Lambda|/|a|]^(-1/6)`
` =4sqrt(6)[|a| beta sqrt(|det Lambda|)]^(-1/3).`                  (4.12)

This proves (4.4). The shift of the hub density depends on `Y`, but only its cap-one height is used after conditioning on `Y`; no false independence after the shear is invoked. QED.

## 5. Exact-tail r51 collar: a new finite payment

Return to the live r51 state and specialize only the child tail to the exact endpoint

`E=0`, equivalently `r=s_3(C)=0`.                                 (5.1)

This is not the already-paid aligned point: `beta` may be nonzero.

Because

`D=V_J Lambda V_K^T`

has rank exactly two and both restricted frames have full column rank, its top-two left and right singular spaces are exactly

`range(V_J)` and `range(V_K)`.                                    (5.2)

Hence the predecessor's literal star distances become exactly

`d_J=e_J`, `d_K=e_K`.                                             (5.3)

Fix

`eta=2^(-20)=9.5367431640625e-7`.                                 (5.4)

The exact-tail crossing has

`s_2(D)>=g m_0 L=0.31983867421255213... L`.                       (5.5)

If either `e_J>=eta L` or `e_K>=eta L`, the completed marginal-free third-compound receiver gives

`boxed: ||p_Q||_infinity <2368.360/L,  p_Q in C_0(R).`            (5.6)

Assume instead

`e_J,e_K<eta L`.

Then

`e<sqrt(2) eta L`.                                                (5.7)

Define

`beta_0:=4sqrt(2) eta`
`      =5.3947966093944364e-6`.                                   (5.8)

If

`beta<=beta_0 L`,                                                  (5.9)

the state lies in the remaining ultra-thin transverse collar.

Otherwise `beta>beta_0 L>4e`, so Theorem (4.4) applies whenever the physical hub pivot is not near-null. In particular, if

`|a|>=L/64`,                                                       (5.10)

then `sqrt(|det Lambda|)>=m_0 L`, and

`|a| beta sqrt(|det Lambda|)`
` >(1/64) beta_0 m_0 L^3`.

Therefore

`boxed:
 ||p_Q||_infinity <2242.477/L.
}`                                                                  (5.11)

This is an essential-density bound. Combining (5.6)-(5.11), the exact two-eigenvalue child endpoint is now reduced to only two unhandled collars:

1. **ultra-transverse:** `beta<=5.395e-6 L`; or
2. **near-null physical hub:** `|a|<L/64`.

The exact aligned point `beta=0` itself was already paid by the earlier exact-aligned theorem. Thus the surviving difficulty is genuinely a punctured near-aligned/near-null interface, not the broad split-mismatch state from r51.

## 6. Designated account04/B08 partner applied on the surviving exact-tail collar

The designated completed partner remains

- `yspennstate/math-open-problems@f324267086411b9725aa0733e108ab6efc2e760a`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account04/B08/20260924T081435Z-account04-B08-QFORM-r3/REPORT.md`,
- theorem `QFORM-DISTRIBUTED-STAR-DERIVATIVE-SPLIT-v1`.

The inherited B08 state has the actual physical-star lower bound

`||b||>rho_* L`, `rho_*=0.0006247538095703261`.

For

`Gamma(Y)=2<b,Y>`,

the standard one-dimensional product-projection theorem gives

`||p_Gamma||_infinity <=1/(sqrt(2)||b||)`.

Applying the partner theorem directly to the same full polynomial, with the entire exact-rank-two child retained as its arbitrary dependent remainder, gives

`boxed:
 sup_t P(|Q-t|<epsilon)
 <=4*2^(1/4) sqrt(epsilon/||b||)
 <190.311 sqrt(epsilon/L).
}`                                                                  (6.1)

This applies in particular on both remaining collars from Section 5, including the near-null pivot. It is a square-root small-ball bound, not a bounded-density conclusion; no such upgrade is claimed without an additional valid receiver.

## 7. Regression checks

A fixed-seed deterministic checker generated 1000 diffuse two-frames with physical row leverage at most `1/16`, balanced physical cuts satisfying the live `g` gate, split mismatch vectors, bankwise residuals, and random invertible two-dimensional child cores.

Observed maxima:

- error in `beta^2=e^2+delta^TGHdelta`: `1.7763568394002505e-15`;
- violation scale for `V^T w=V^T r=V^T u=0`: maximum norm `1.2909001160129719e-15`;
- `|r.w|`: `2.47198095326695e-17`;
- relative error in `det M=-(beta^2/a)det Lambda`: `2.0758264772230857e-15`;
- maximum sampled row leverage of `[V,u/beta]`: `0.12936955458642768`, below the analytic ceiling `0.436740950167119`.

The fixed constants were recomputed independently:

`alpha=0.1308647700847534`,
`mu+(sqrt(alpha)+1/4)^2=0.436740950167119`,
`g*m_0=0.31983867421255213`,
`beta_0=5.3947966093944364e-6`,
`C_cross=2368.359653017247`,
`C_Schur=2242.476045115443`.

The computations are regression evidence only. Sections 2-6 are analytic.

## 8. Correction boundary and what remains

The live correction `QFORM-HUBSTAR-FIBERL2-MIXEDNORM-UNIVERSAL-FALSE-v1` was consumed during this run. The proof above never absoluteizes a mixed Fourier norm of the form `int |t|^(-1/2)||G_t||_2 dt`; instead it first obtains a genuine one-copy density bound for the exact Schur quadratic from the completed rank-three product-coordinate Fresnel theorem, and only then applies the elementary probability-density half-Riesz rearrangement bound.

This run does **not** prove the full conjecture and does not claim continuity for the new Schur-Fresnel/square-peel branch. The first remaining B08 implication is now

`QFORM-EXACTTAIL-ULTRATRANSVERSE-OR-NEARNULL-HUB-COMPILER-v1`:

close the exact-rank-two child state when either `0<beta<=5.395e-6 L` or `|a|<L/64`, without perturbing from the paid `beta=0` endpoint and without paying a negative power of the puncture. After that, return to the nonzero child-tail state `0<r<L/4096` using a receiver that keeps the tail jointly rather than deleting it.

Full universal boundedness: **OPEN**.  
Global continuity: **OPEN**.
