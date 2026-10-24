SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B10, 2026-09-23T03:48:36Z.
attacking: the exact-rank-three near-null physical hub after the Pluecker small-disjoint-mass reduction; preserve the original product source through the minority-sign discriminant and test the remaining ultranear-null interpolation.

# account02/B10 r11 — minority-hub transverse discriminant + positive-d logarithmic square-peel obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** rank-three coupled case; complementary constructions/source-valid counterexamples  
**Owner control read:** revision `2026-09-22.15` (base programme revision `2026-09-22.5`)  
**Run id:** `20260923T034836Z-account02-B10-r11-a1f7`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** `NEW SUPPORTING TARGET-LEVEL THEOREM + PARTNER SPLICE + TARGET-VALID INTERMEDIATE-MECHANISM FALSIFIER / FULL QFORM OPEN`.

## 1. Exact target and live correction boundary

The target remains unrestricted: for every finite `n`, arbitrary independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite essential bound on the density of `X^T A X`, or give a valid counterexample. No moment, support, connected-support, log-concavity, identical-law, diagonal-basis, or post-rotation independence assumption is introduced. Continuity is tracked separately.

Fresh protected control and the current correction inbox were reread before the final proof write. In particular, I do not use law-uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea, conditional projection-height suprema, independence after spectral rotation, or the false inference that a near-zero scalar pivot may be treated by the exact-zero half-Riesz argument with an error term. Small coefficients are never treated as small random perturbations.

The first unpaid implication at the start of this run came from the latest designated partner `account03/B10`, `20260923T023946Z-account03-B10-QFORM-r23b`. Its exact disjoint-Pluecker identity and endpoint compilers reduce the small-disjoint-mass branch `0<d<1/64`, unless already paid, to an ORIGINAL physical hub `i` with leverage `c_i>1/4`, small normalized Rayleigh quotient `|q_i|=|u_i^T M u_i|<1/16`, and fixed aggregate physical star resource `||A_(i,-i)||_2 > sqrt(1023)/64`. The indefinite one-sheet output side is already paid by the ruled theorem. The genuine B10 debt is the two-sheet/minority-side near-null interpolation while retaining product provenance.

## 2. Required source package actually applied

I read the required exact source package `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Two completed results from that package are used below at actual inequalities. First, an orthogonal two-dimensional projection of an original cap-one product source has joint density at most `2`; this is the dependence-safe receiver cap used in the new theorem. Second, the ruled one-sheet theorem says an exact rank-three indefinite form with spectral scale at least one has density at most `pi sqrt(2)` on its one-sheet side. In Section 6 it gives the concrete inequality `p_(Q_eps)(0)<=pi sqrt(2)` for the explicit target family that simultaneously makes the raw square-peel envelope diverge.

A new compatible theorem appeared on the live mathematical source tree during this run and was consumed rather than duplicated: account03/B11 r24, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260923T035259Z-account03-B11-QFORM-r24/REPORT.md`, proves the minority-scalar elliptic-discriminant estimate for one independent scalar and an arbitrary bounded-density two-dimensional pair. The new argument below identifies an exact cancellation that lets that discriminant mechanism survive the extra dependent longitudinal leaf coordinate present in an arbitrary exact-rank-three physical hub.

## 3. New theorem — longitudinal leaves cancel from the minority discriminant

### Theorem 3.1 — `QFORM-MINORITY-HUB-TRANSVERSE-DISCRIMINANT-v1`

Let `A=R M R^T`, `R^T R=I_3`, be exact rank three. Assume `M` has inertia `(2,1)` or `(1,2)`. Fix an ORIGINAL physical coordinate `i` with spectral row `r_i=sqrt(c)u`, `||u||=1`, `c>0`, and put `q=u^T M u`. Assume `q` carries the minority inertia sign, equivalently `q det M>0`. For arbitrary independent original inputs with densities at most one,

`boxed: ||p_(X^T A X)||_infinity <= 2 sqrt(2 pi) c^(-1/2) (q det M)^(-1/4).` (3.1)

The assertion is about essential boundedness. No continuity conclusion is added.

### Proof

Choose a `3 x 2` matrix `E` whose columns form an orthonormal basis of `u^perp`. In the spectral basis `(u,E)`, write `M=[[q,b^T],[b,C]]`. Let `R_-` be `R` with physical row `i` removed, and define from the remaining ORIGINAL coordinates

`T=(R_-u)^T X_-`, `Y=E^T R_-^T X_- in R^2`.                       (3.2)

The scalar `X_i` is genuinely independent of the whole leaf vector `(T,Y)` because it is an original coordinate. Parseval gives `R_-^T R_-=I_3-cuu^T`, so `(R_-E)^T(R_-E)=I_2`. Therefore `Y` is an orthogonal two-dimensional projection of the original cap-one leaf product law, and the completed projection theorem gives

`||p_Y||_infinity<=2`.                                              (3.3)

No independence between the two coordinates of `Y` is asserted.

The spectral source coordinate equals

`R^T X=u(sqrt(c)X_i+T)+EY`.                                         (3.4)

Hence, writing `x=X_i`,

`Q=q(sqrt(c)x+T)^2+2(sqrt(c)x+T)b^TY+Y^TCY`.                       (3.5)

For fixed leaves and target `t`, the scalar quadratic in `x` has coefficient `a=cq`, linear half-coefficient `L=sqrt(c)(qT+b^TY)`, and leaf remainder `R_0=qT^2+2Tb^TY+Y^TCY`. Its discriminant is

`D_t=L^2-a(R_0-t)`.

The key exact cancellation is

`boxed: D_t=c[(b^T Y)^2-qY^TCY+qt].`                               (3.6)

Every occurrence of the dependent longitudinal coordinate `T` cancels. I never condition on `T`, so no conditional projection-density bound is needed.

At a real root, the absolute scalar derivative is `2sqrt(D_t)`. There are at most two roots and `f_i<=1`, so for almost every `t`, conditional on the leaves,

`p_(Q|leaves)(t)<=1_{D_t>0}/sqrt(D_t)`.                            (3.7)

Put `K=bb^T-qC`. If `q` has the minority sign, the Schur complement `S=C-bb^T/q` has the majority definite sign, hence `K=-qS>0`. Also

`det K=q det M>0`.                                                   (3.8)

Thus `D_t=c[Y^TKY+qt]`. For `s>0`, the Lebesgue area of

`{y:0<c(y^TKy+qt)<s^(-2)}`

is at most `pi/[c s^2 sqrt(det K)]`, by the change `z=K^(1/2)y`. Averaging (3.7), using both probability mass one and (3.3), and applying layer cake gives

`p_Q(t) <= integral_0^infinity min{1,2pi/[c sqrt(det K)] s^(-2)} ds`
`       = 2sqrt(2pi)c^(-1/2)(det K)^(-1/4)`,                       (3.9)

which with (3.8) is (3.1). QED.

The account03/B11 source theorem has one scalar independent of a two-dimensional pair. An arbitrary exact-rank-three physical hub has the extra longitudinal leaf variable `T`, generally dependent on the transverse pair `Y`. Conditioning on `T` would be unsafe. Identity (3.6) is the new product-preserving bridge: the longitudinal variable cancels before any density estimate.

## 4. Designated-partner splice: a quantitative new paid band

Apply Theorem 3.1 to the latest designated-partner small-`d` survivor. There `c>1/4`, `|det M|>=1`, and `|q|<1/16`. On the minority-sign subbranch with

`|q|>=2^(-10)=1/1024`,                                             (4.1)

(3.1) gives the actual inequality

`||p_Q||_infinity <=2sqrt(2pi)(1/4)^(-1/2)(1/1024)^(-1/4)`
`                  =56.7185232289... <56.719`.                     (4.2)

Thus visible-minority physical hubs are paid all the way down to normalized Rayleigh scale `2^(-10)` by an aggregate transverse projection, without selecting one physical pair or triple. The exact point `q=0` is already paid by completed exact-null source theorems in the current proof graph. The genuinely unpaid minority interpolation may therefore be restricted to

`0<|q|<2^(-10)`                                                     (4.3)

inside the already-small `0<d<1/64` collar.

## 5. Minority-pivot Schur identity and the wrong interface

For a minority-sign nonzero physical pivot `a=A_ii=cq`, scalar completion leaves a definite rank-two Schur form. Its two nonzero spectral coefficients have product

`|det N|=c|det M|/|a|=|det M|/|q|`.                                (5.1)

The completed rank-two definite theorem therefore gives a remainder density cap of order `sqrt(|q|/|det M|)`. That fact by itself does not close the scalar square peel uniformly: the next section gives an exact target family in the genuine positive-`d` collar for which the unconditional half-Riesz square envelope diverges logarithmically while the actual output density at the same value stays bounded by the ruled theorem.

## 6. Target-valid positive-`d` family: raw square peeling has logarithmic loss

### Proposition 6.1 — `QFORM-NEARNULL-SQUARE-PEEL-LOG-LOSS-v1`

For every `0<eps<=1/64` there is an exact-rank-three target form with spectrum `{1,1,-1}`, an ORIGINAL hub in the partner's `0<d<1/64` near-null fixed-star collar, and iid `Uniform[-1/2,1/2]` source coordinates, such that the standard cap-one scalar-square half-Riesz envelope at output zero is at least

`(sqrt(2)/6) log(1/(2sqrt(eps)))`,                                  (6.1)

and therefore diverges as `eps->0`, whereas the actual output density obeys

`p_Q(0)<=pi sqrt(2)`                                                (6.2)

by the required source package's ruled theorem.

### Construction and proof

Let `delta=eps^2`, `s=sqrt(1-eps^2)`, and in an orthonormal spectral basis `(u,w,v)` set

`M_eps=[[-eps,0,s],[0,1,0],[s,0,eps]]`.                             (6.3)

The `(u,v)` block has trace zero and determinant `-1`, so `spec(M_eps)={1,1,-1}` and `M_eps^2=I_3`.

Use the six-row Parseval frame

`r1=u/sqrt(2), r2=u/sqrt(2),`
`r3=sqrt(1-delta)w, r4=sqrt(delta)w,`
`r5=sqrt(1-delta)v, r6=sqrt(delta)v`.                               (6.4)

Then `R^TR=I_3`, and `A_eps=RM_epsR^T` is an exact target matrix. Only Pluecker bases containing one row from each spectral line have positive weight. Two independent Pluecker bases are disjoint exactly when they choose opposite rows on all three lines, hence

`d_eps=(1/2)[2delta(1-delta)]^2=2eps^4(1-eps^2)^2`,                 (6.5)

so `0<d_eps<1/64`.

Take `r1` as the hub. Its leverage and normalized Rayleigh quotient are `c=1/2`, `q=-eps`, its physical pivot is `A_11=-eps/2`, and because `M_eps^2=I`,

`sum_(j!=1)A_1j^2=(A^2)_11-A_11^2=1/2-eps^2/4`.                    (6.6)

Thus the aggregate star is uniformly large.

Let all six original inputs be iid `Uniform[-1/2,1/2]`, and define the independent bank linear forms

`U=(X1+X2)/sqrt(2)`,
`W=sqrt(1-delta)X3+sqrt(delta)X4`,
`V=sqrt(1-delta)X5+sqrt(delta)X6`.                                  (6.7)

Then

`Q_eps=-eps U^2+2sUV+W^2+eps V^2`.                                 (6.8)

Complete the square in the ORIGINAL hub coordinate `X1` only:

`Q_eps=-(eps/2)[X1+X2-sqrt(2)sV/eps]^2+R_eps`,                      (6.9)

where `R_eps=W^2+V^2/eps`. The ordinary conditional cap-one square change of variables has, at target zero, the envelope

`B_eps=sqrt(2/eps) E[R_eps^(-1/2)]`.                                (6.10)

Restrict the expectation to

`|X4|,|X6|<=1/4`, `|X3|<=1/4`, `sqrt(eps)/2<=|X5|<=1/4`.            (6.11)

For `y=|X5|` there and `eps<=1/64`,

`|W|<=1/4+eps/4<=y/sqrt(eps)`,
`|V|<=y+eps/4<=(17/16)y`.                                          (6.12)

Hence `sqrt(R_eps)<=(3/2)y/sqrt(eps)` and

`R_eps^(-1/2)>=(2/3)sqrt(eps)/y`.                                  (6.13)

All source densities equal one on their supports. Integrating (6.13) over (6.11) gives

`E[R_eps^(-1/2)] >= (sqrt(eps)/6)log(1/(2sqrt(eps)))`.              (6.14)

Substituting in (6.10) proves (6.1). This is not a QFORM counterexample. The same target matrix has signature `(2,1)` and unit spectral scale, so the completed ruled theorem from the required `e5f71d...` package gives directly at the cone boundary

`boxed: p_(Q_eps)(0)<=pi sqrt(2).`                                  (6.15)

The logarithmic divergence is therefore created by discarding the location factor of the original hub density before using the transverse product geometry. A successful ultranear-null interpolation must keep that factor, or an equivalent cross-transverse/Fresnel cancellation, alive.

## 7. Current exact-rank-three proof map

The required ruled theorem pays the entire one-sheet side at `pi sqrt(2)`. The latest account03/B10 Pluecker compiler pays `d>=1/64`, the exact endpoint `d=0`, and reduces `0<d<1/64` to a high-leverage near-null physical hub/star unless another paid branch fires. Theorem 3.1 pays every minority-sign hub at a quantitative nonzero Rayleigh scale without selecting a local minor; using the partner's `c>1/4` resource, the whole minority band `2^(-10)<=|q|<1/16` is paid by `<56.719`. The exact `q=0` endpoint is already paid. Proposition 6.1 shows that the remaining interpolation `0<|q|<2^(-10)` cannot be closed by a raw scalar-square half-Riesz envelope, even inside a target-valid positive-`d` family with fixed aggregate star norm.

The first unpaid implication is therefore **`QFORM-MINORITY-HUB-ULTRANEARNULL-PRODUCT-INTERPOLATION-v1`**:

> In the exact-rank-three partner survivor with `c>1/4`, `0<d<1/64`, minority-sign normalized Rayleigh quotient `0<|q|<2^(-10)`, and fixed aggregate star norm, interpolate product-safely between the exact-null compiler and Theorem 3.1. The estimate must retain the original hub density factor jointly with at least one transverse product bank (or an equivalent cross-transverse/Fresnel object); the unconditional half-Riesz Schur envelope is ruled out by Proposition 6.1.

The hidden-minority / majority-diagonal balanced near-rank-one chamber identified by account03/B11 remains a separate exact-rank-three debt. Arbitrary additional spectral directions remain separate for the full owner target.

## 8. Verification scope and honest status

A deterministic checker accompanies this report. For `eps=1/64,1/256,1/1024` it verifies `spec(M_eps)={-1,1,1}`, `M_eps^2=I`, `R^TR=I`, the exact Pluecker disjoint-mass formula (6.5), hub leverage `1/2`, pivot `-eps/2`, and star-energy formula (6.6). Those finite computations are regression checks only; the proof is the exact algebra above.

`QFORM-MINORITY-HUB-TRANSVERSE-DISCRIMINANT-v1`: **PROVED** in exact rank three.  
Designated partner account03/B10: **APPLIED** at the actual inequality (4.2), shrinking its minority-sign near-null survivor.  
Required `math-open-problems@e5f71d...` source: **APPLIED** at the projection cap (3.3) and the concrete ruled inequality (6.15).  
`QFORM-NEARNULL-SQUARE-PEEL-LOG-LOSS-v1`: **PROVED target-valid falsifier of an intermediate proof mechanism**, not a counterexample to QFORM.  
Full exact-rank-three theorem: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full owner QFORM target with arbitrary additional spectrum: **OPEN**.  
Continuity beyond already source-proved branches: **OPEN separately**.  
Native brain ingestion/receiver use: **not verified; execution remains `WITHOUT_VERIFIED_BRAIN`**.
