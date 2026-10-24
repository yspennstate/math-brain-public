SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B02, 2026-09-23T05:08:31Z.
attacking: the first unpaid high-volume collar by aggregating three physical volume packets before reciprocal-minor payment, while independently checking the new sharp-Hausdorff--Young analytic constants.

# account02/B02 — three-sample volume compiler and quantitative near-endpoint routing

Programme: `QFORM-DENSITY-3EIG-20260922`.  
Status: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`.  
Execution context: `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not native learned-memory ingestion.

The full conjecture is **not** proved here. The run proves a new integrated-Fourier branch for a live ORIGINAL-coordinate cross block, gives an exact and quantitative classification of its failure mode, and exhibits an exact-target matrix on which D', D5 and the designated partner's two-sample compiler all fail while the new three-sample compiler succeeds. No moment, support, log-concavity, post-rotation independence, or law-uniform scalar pointwise stationary-phase estimate is used.

## 1. Sources actually used

1. Required Claude package:
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`,
   `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.
   I use its original-coordinate decoupling, endpoint-safe determinant expansion, D' and D5 volume mechanisms, and the prohibition on replacing them by false scalar pointwise decay.

2. Newest fractional-volume theorem:
   `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
   `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.
   I independently review its q-dependent sharp-Hausdorff--Young analytic calculation in Section 2, then use it with an entropy-tilted volume law.

3. Designated partner `account03/B02`, latest compatible completed report read in this run:
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T043653Z-account03-B02-qform-r20/REPORT.md` on current master.
   Its theorem conditions two iid determinant-weighted row triples on being disjoint and obtains
   `||p_Q||inf <= 3e delta_2^(-1/6) E3(M)^(-1/6)`.
   I apply it in Section 7 to a concrete obstruction and show exactly where a three-sample replacement is strictly stronger.

Current source corrections were consumed before use: pointwise law-uniform quadratic phase decay is false; spectral rotations do not preserve input independence; arbitrary-joint coarea and worst conditional-density gates are unavailable; one good minor or a rank-three physical cross cut cannot be assumed from the bare spectral hypothesis.

## 2. Independent analytic review of the new q-dependent theorem

This is the analytic review assigned to account02/B02. It does **not** claim the separately assigned account03/B04 matrix/tail review.

Let `M=A[I,J]` be a physical cross block, `Z=E3(M)=e3(M^T M)>0`, and let `alpha_i,beta_j` be the row and column marginals of the squared-minor volume law. After original-coordinate decoupling,

`|phi_Q(t)|^2 <= E_D prod_i |psi_i(2t(MD)_i|`,

where the coordinates of `D=X_J-X'_J` remain genuinely independent and have density caps at most one. For `q>=1`, Jensen gives `E F <= (E F^q)^(1/q)`.

For a row with volume exponent `alpha`, sharp Hausdorff--Young at output exponent `q/alpha>=2` gives, with the Fourier normalization of the source,

`|| |psi(2t .)|^q ||_(1/alpha)
 <= (pi/|t|)^alpha
    (alpha/q)^(alpha/2)
    (1-alpha/q)^(-(q-alpha)/2)`.                         (2.1)

The Gaussian Brascamp--Lieb determinant estimate contributes `alpha^(-alpha/2)` and the endpoint-safe column factors. Thus the powers of `alpha` cancel. Since `sum alpha=sum beta=3` and

`-(1-x)log(1-x)<=x`, `0<=x<=1`,

the row and column entropy factors together contribute `e^3`. Hence

`E F_t^q <= e^3 q^(-3/2) (pi/|t|)^3 Z^(-1/2)`.          (2.2)

Therefore

`|phi_Q(t)| <= min(1,K |t|^(-b))`,
`b=3/(2q)`,
`K=[e^3 q^(-3/2) pi^3 Z^(-1/2)]^(1/(2q))`.              (2.3)

For `1<=q<3/2`, `b>1` and

`int_R min(1,K|t|^(-b))dt = 2b K^(1/b)/(b-1)`.

Fourier inversion gives exactly

`boxed{ ||p_Q||inf <= 3e / ((3-2q)sqrt(q)) * Z^(-1/6). }` (2.4)

This matches the newest source. The endpoint-column convention is valid because a column with `beta_j=1` belongs to every positive-weight minor and may be dropped using its density cap before the diagonal-plus-PSD determinant expansion. My analytic verdict for (2.1)--(2.4), including constants and endpoints, is **PASS**.

The same calculation for k-volume gives, whenever `max alpha_i^(k)<=q/2` and `k>2q`,

`boxed{ ||p_Q||inf <= e q^(-1/2) k/(k-2q) * E_k(M)^(-1/(2k)). }` (2.5)

Thus the required sharp-HY versions of the live source tools are

`D':  ||p_Q||inf <= 3e Z^(-1/6)` if `h<=1/2`, and

`D':  ||p_Q||inf <= 3e/[sqrt(2h)(3-4h)] Z^(-1/6)` if `1/2<h<3/4`,

where `h=max alpha_i`, while

`D5:  boxed{ ||p_Q||inf <= (5e/sqrt(2)) E5(M)^(-1/10) }`   (2.6)

has no marginal gate because every fifth-volume marginal is at most one. This is an `L^1_t` characteristic-function conclusion, hence it also gives a continuous density vanishing at infinity on its scope.

## 3. Entropy-tilted fractional-volume lemma

The following form of (2.4) is the input for the new construction.

Let

`w_(R,T)=det(M[R,T])^2/Z`, `|R|=|T|=3`,

be the canonical three-volume law, and let `mu_R=sum_T w_(R,T)` be its row marginal law. Let `nu` be any probability law on row triples supported where `mu_R>0`, and lift it to a full row/column minor law by retaining the canonical conditional columns,

`pi_(R,T)=nu_R w(T|R)`.

Then

`D(pi||w)=D(nu||mu)=:D`.

If every row inclusion marginal of `nu` is at most `q/2`, `1<=q<3/2`, the weighted AM--GM determinant step gains exactly the entropy penalty `exp(-D)`:

`det(D_J+M^T D_I M)
 >= Z exp(-D) prod_i d_i^(alpha_i) prod_j e_j^(1-beta_j)`.   (3.1)

Accordingly (2.2) becomes

`E F_t^q <= exp(D/2+3) q^(-3/2)(pi/|t|)^3 Z^(-1/2)`.        (3.2)

Running (2.3)--(2.4) yields

`boxed{
 ||p_Q||inf
 <= [3e/((3-2q)sqrt(q))] exp(D/6) Z^(-1/6).
}`                                                                  (3.3)

All same-bank quadratic phases, outside couplings and conditioning-generated affine terms remain present because only the original-coordinate cross block is decoupled.

## 4. Main theorem: three-sample common-intersection compiler

Draw three iid row triples `R_1,R_2,R_3~mu` and define

`delta_3 = P(R_1 cap R_2 cap R_3 = empty)`.                 (4.1)

### Theorem 4.1 (`QFORM-TRIPLE-DISJOINT-VOLUME-COMPILER-v1`)

If `delta_3>0`, then the full quadratic-plus-affine form has a continuous density and

`boxed{
 ||p_Q||inf
 <= (9 sqrt(3) e / 2) delta_3^(-1/6) E3(M)^(-1/6).
}`                                                                  (4.2)

### Proof

Condition the iid triple law `mu^3` on

`E={R_1 cap R_2 cap R_3=empty}`

and let `nu` be the first marginal. The conditioned law is exchangeable. For every physical row index `i`, at most two of the three triples can contain `i` on `E`; hence

`3 P_nu(i in R) = E[sum_(a=1)^3 1{i in R_a}|E] <= 2`.

Thus every row marginal of `nu` is at most `2/3`. Moreover, by data processing,

`D(nu||mu)
 <=D(Law(R_1,R_2,R_3|E)||mu^3)
 =log(1/delta_3)`.                                          (4.3)

Apply (3.3) with `q=4/3`. Since `q/2=2/3`, the gate is exactly satisfied, and

`3e/((3-2q)sqrt(q))=9sqrt(3)e/2`.

Combining this with (4.3) gives (4.2). Since the proof produces an integrable characteristic-function envelope, continuity and vanishing at infinity follow. QED.

This is not a scalar stationary-phase bound. The frequency decay appears only after three determinant-weighted physical volume packets have been aggregated and the full product source has been decoupled.

## 5. Exact endpoint classification when delta_3=0

When `delta_3=0`, every three positive-mass row triples have nonempty common intersection. For a finite family of 3-subsets this has an elementary exact classification.

### Lemma 5.1 (three-wise intersecting 3-sets)

Let `F` be a family of 3-subsets such that every three members have nonempty common intersection. Then either

1. all members of `F` contain one common element; or
2. there is a four-element set `H` such that every member of `F` is a 3-subset of `H`.

### Proof

If the total intersection is empty, choose a minimal subfamily `A_1,...,A_m` with empty intersection. Since every three intersect, `m>=4`. Minimality provides, for every `k`, an element `x_k` belonging to all `A_j`, `j!=k`, but not to `A_k`. The `x_k` are distinct. Each `A_j` contains the `m-1` distinct elements `x_k`, `k!=j`; because `|A_j|=3`, necessarily `m=4` and `A_j=H\{x_j}` for `H={x_1,x_2,x_3,x_4}`. Any further `A in F` must meet every pairwise intersection `A_j cap A_k`, i.e. every two-subset of `H`. A 3-set with that property is itself a 3-subset of `H`. QED.

Apply this to the support of `mu`.

* In case 1, some physical row `i` occurs in every nonzero three-minor. Therefore

  `E3(M[I\{i},J])=0`,

  so `rank M[I\{i},J]<=2`. This is an exact physical row coloop.

* In case 2, all positive row triples lie in a four-row set `H`. Because `Z>0`, three rows in `H` are linearly independent. If a row `x` outside `H` were nonzero, its determinant with at least one pair among those three basis rows would be nonzero: otherwise it lies simultaneously in the three pair-spans, whose intersection is `{0}`. Hence every row outside `H` is zero and

  `boxed{ M[I\H,J]=0, |H|<=4. }`                            (5.1)

So the exact failure endpoint is not an amorphous Fourier obstruction: it is either a rank-at-most-two residual after one physical row, or a cross interaction living on at most four physical rows.

## 6. Quantitative stability near the endpoint

The exact endpoint can be made quantitative without selecting one tiny determinant.

Let

`h=max_i P_mu(i in R)`

and fix `0<epsilon<1`. Put

`eta=delta_3/epsilon`,
`tau=eta/[2(epsilon-eta)^2]`,

and suppose `eta<epsilon` and `tau<=1/2`.

### Theorem 6.1 (`QFORM-TRIPLE-INTERSECTION-STABILITY-v1`)

Either

**(A) near coloop:** some row `i` satisfies

`E3(M[I\{i},J]) < epsilon Z`,                              (6.1)

or

**(B) near four-row support:** some four-row set `H` satisfies

`E3(M[H,J]) >= (1-rho) Z`,
`rho=eta+5 tau`.                                            (6.2)

More precisely, (A) holds whenever `h>1-epsilon`; if `h<=1-epsilon`, (B) holds.

### Proof

If `h>1-epsilon`, choose a row `i` with inclusion probability greater than `1-epsilon`. The three-volume mass of row triples avoiding `i` is `1-alpha_i<epsilon`, exactly giving (6.1).

Assume now `h<=1-epsilon`. For row triples `A,B`, define

`q(A,B)=P_C(C cap A cap B=empty)`.

If `|A cap B|=0`, `q(A,B)=1`; if `A cap B={i}`, then

`q(A,B)=1-alpha_i>=epsilon`.

Therefore

`P(|A cap B|<=1) <= delta_3/epsilon = eta`.                 (6.3)

Choose one triple `A_0={1,2,3}` such that

`r:=P_B(|A_0 cap B|<=1)<=eta`.

Write `m_0` for the mass of `B=A_0`, and let `a,b,c` be the masses of the good types

`{1,2,x}`, `{1,3,x}`, `{2,3,x}`, `x notin A_0`,

respectively. Since every coordinate marginal is at most `1-epsilon`, omission of coordinate 3, 2, or 1 gives

`a,b,c >= epsilon-r >= epsilon-eta`.                        (6.4)

Write `p_12(x),p_13(x),p_23(x)` for the three type masses. An ordered pair of types `{1,2,x}` and `{1,3,y}` with `x!=y` has intersection only `{1}`, hence is counted in (6.3). Both orientations occur, so

`ab-sum_x p_12(x)p_13(x) <= eta/2`,                        (6.5)

and similarly for the other two type pairs.

Normalize `P_x=p_12(x)/a`, `Q_x=p_13(x)/b`, `R_x=p_23(x)/c`. By (6.4)--(6.5),

`<P,Q>, <P,R>, <Q,R> >= 1-tau`.                            (6.6)

Choose `x_*` with maximal `P_x`. Since `<P,Q><=max_x P_x`, we have `P_(x_*)>=1-tau`. Then (6.6) and the fact that the contribution away from `x_*` is at most `1-P_(x_*)<=tau` give

`Q_(x_*),R_(x_*) >=1-2tau`.                                (6.7)

Let `H=A_0 union {x_*}`. The volume-law mass of triples not contained in `H` is at most

`r + a(1-P_(x_*))+b(1-Q_(x_*))+c(1-R_(x_*))
 <= eta+5tau=rho`.                                          (6.8)

But that volume-law mass is exactly

`1-E3(M[H,J])/Z`.

This proves (6.2). QED.

A concrete parameter choice makes the collar explicit. Take

`epsilon=1/4`, `delta_3<1/1024`.

Then `eta=1/256`, `tau=128/3969`, and

`rho=167809/1016064 <0.165156`.

Thus for **every** physical cross block with `Z>0`, either

* `delta_3>=1/1024`, in which case (4.2) gives
  `||p_Q||inf <67.265 Z^(-1/6)`; or
* some row deletion leaves `<Z/4` third-volume; or
* some four-row set carries more than `0.834844 Z` of the total third-volume.

This is the first paid quantitative routing step from the high-marginal D' collar toward a physical coloop/four-row core while retaining arbitrary self curvature and extra spectrum.

## 7. Actual partner application and an exact-target strict-extension example

The designated partner's r20 theorem uses two iid row triples and

`delta_2=P(R_1 cap R_2=empty)`.

When `delta_2>0`, it gives

`||p_Q||inf <=3e delta_2^(-1/6) Z^(-1/6)`.                 (7.1)

Together with (4.2), on the common scope one may use the genuine combined inequality

`boxed{
 ||p_Q||inf
 <= e Z^(-1/6)
    min{3 delta_2^(-1/6), (9sqrt(3)/2) delta_3^(-1/6)}.
}`                                                                  (7.2)

The new branch is strictly stronger as a *compiler*, because `delta_2` can vanish identically while `delta_3` is positive.

Take the 5-by-3 Vandermonde matrix `V` with physical rows

`v_t=(1,t,t^2)`, `t=0,1,2,3,4`,

and set `M=2V`. The ten squared 3-by-3 minors of `V`, in lexicographic row-triple order, are

`4,36,144,36,256,144,4,36,36,4`,

so `E3(V)=700` and

`Z=E3(M)=2^6*700=44800`.                                   (7.3)

Every two 3-subsets of a 5-set intersect, hence

`delta_2=0`: the partner's two-sample conditioning event is empty and (7.1) cannot be invoked. The original row-volume marginals are

`(31/35,13/35,17/35,13/35,31/35)`,

so `h=31/35>3/4`: D' also fails. Since `rank M=3`, `E5(M)=0`: D5 fails as well.

Nevertheless exact enumeration of the determinant-weighted triple law gives

`delta_3=9396/214375 >0`.                                   (7.4)

The singular values of `M` are approximately

`39.24307694, 3.72638552, 1.44739868`.

Embed it in the symmetric ORIGINAL-coordinate target matrix

`A = [[0,M],[M^T,0]]`.

Its nonzero eigenvalues are the positive and negative singular values of `M`; in particular it has at least three eigenvalues of absolute value at least one. Therefore this is an exact-target family, not merely a cross-block toy. For **every** independent product input with coordinate densities at most one, (4.2), (7.3), and (7.4) give

`boxed{ ||p_(X^T A X)||inf <5.988. }`                       (7.5)

The characteristic function is in `L^1`, so the density is continuous. This is an actual inequality on a source-valid target instance where the required D', D5 and completed partner two-sample certificates all fail.

## 8. What is paid and what remains

Paid in this run:

1. independent analytic review of the new q-dependent sharp-HY fractional-volume constants/endpoints: **PASS** for the analytic scope;
2. sharp-HY D' and D5 are explicitly retained on a live physical cross block;
3. the partner's two-sample theorem is applied to the real combined inequality (7.2), and its exact obstruction is exposed by the target matrix in Section 7;
4. a new three-sample entropy compiler closes that obstruction whenever `delta_3>0`;
5. its exact zero endpoint is classified as a physical coloop/rank-two residual or a four-row cross core;
6. its small-positive endpoint is quantitatively routed to a near-coloop or a near-four-row concentration.

The first unpaid implication is now narrower:

`QFORM-NEAR-COLOOP-OR-FOURROW-ROUTING-v1`:

> Starting from a physical cross block whose third exterior volume is either reduced by a fixed factor after one row deletion or is concentrated by a fixed factor on four physical rows, combine the existing exact-null coloop kernel / near-null machinery / physical-pair and mixed-hub theorems with the residual volume, without dropping arbitrary same-bank quadratic curvature or additional spectrum, to obtain a dimension-free target bound or a second cross block with a paid D'/D5/triple-volume certificate.

The bare three-large-eigenvalue hypothesis still has not been shown to furnish a physical cross block with a universally lower-bounded `Z`, and the near-coloop/four-row branch above is not yet exhaustively closed. Therefore the unrestricted QFORM conjecture remains **OPEN**.

I found no exact-target counterexample to the stronger global unweighted criterion `int |phi_Q(t)| dt<infinity`; it remains OPEN target-wide. This report proves it on the stated D5, D', and three-sample-volume branches only.
