# QFORM fleet02/B10 — rank-one leaf compiler and star-parallel second-curvature obstruction

Programme: QFORM-DENSITY-3EIG-20260922  
Role: rank-three coupled case; complementary constructions/source-valid counterexamples  
Status: **PROVED SUPPORTING THEOREM / TARGET-VALID NEAR-NULL SUBCHAMBER CLOSED / VALID INTERMEDIATE-ROUTE OBSTRUCTION / FULL EXACT-RANK-THREE OPEN / FULL QFORM OPEN**

## 1. First unpaid implication

**QFORM-STAR-PARALLEL-SECOND-CURVATURE-RECEIVER-v1.**

Let one ORIGINAL coordinate be the physical hub `H`, let the remaining ORIGINAL coordinates form a leaf bank, and let `x,y` be orthonormal coefficient vectors on that bank. The endpoint work already controls the null-hub form

`2 s H L + b L^2 + 2 k L V + d V^2`,  `L=x·X`, `V=y·X`,

without assuming `L,V` are independent. The new calculation below controls every hub Rayleigh coefficient when the non-diagonal leaf quadratic block has rank one. The first unpaid case is therefore the genuinely rank-two leaf block, especially the indefinite one, with nonzero hub Rayleigh coefficient tending to zero.

The receiver must retain ORIGINAL-coordinate product provenance. In particular it may not (i) diagonalize the three aggregate variables and call them independent, (ii) replace the leaf projection by an arbitrary joint density and then take a worst conditional-density supremum, or (iii) use coefficient continuity as the hub Rayleigh coefficient tends to zero. The explicit family in Section 6 shows why the most direct source Fourier compilers do not automatically pay this second-curvature case.

## 2. Sources actually used

At the required source pin

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

I used the completed mixed-Fresnel theorem from

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`

and the completed ruled-level-set theorem from

`.../COUNTEREXAMPLE_SEARCH.md`.

The mixed-Fresnel theorem says, in the one-hub/one-Fresnel-direction case, that if the leaf star vector is `C`, the unit Fresnel vector is `z`,

`Gamma = Gram(C,z)`,

and every normalized row leverage of the two-column frame is at most `1/2`, then for arbitrary hub quadratic coefficient, arbitrary ORIGINAL-coordinate diagonal leaf twist, and arbitrary affine terms,

`|phi_Q(t)| <= (4 pi)^(3/2) / (2 |t|^(3/2) |lambda|^(1/2) det(Gamma)^(1/2)).`

The source theorem uses the ORIGINAL independent coordinates before taking moduli; it does not assert independence of the projected forms.

The ruled theorem says that for signature `(2,1)` with all three eigenvalue magnitudes at least one, the majority-sign one-sheet levels satisfy `p_Q(q)<=pi sqrt(2)` after the appropriate sign convention.

I also consume the latest completed compatible fleet03/B10 r28 geometry from brain handoff commit `17a044185c3594ba150fb2ab0df5d2a0ecd3b431`, whose canonical mathematics is `math-open-problems@b2a0240b45c8a0716d803b8413bac31af519ce42`. It supplies an ORIGINAL-leaf orthonormal pair `(r,y)` with

`max_i (r_i^2+y_i^2) < 1/54`

and a physical star `C=sqrt(h) gamma r` with

`||C||^2=h gamma^2>16065/16384`.

## 3. A quantitative one-hub/rank-one-leaf receiver

### Lemma 3.1

Let `H,X_1,...,X_m` be independent real random variables with densities at most one. Let `C,z in R^m`, with `||z||=1`, and suppose `C,z` are linearly independent. Let

`Gamma=[[||C||^2,<C,z>],[<C,z>,1]]`.

Assume the normalized two-column leverage bound

`max_i (C_i,z_i) Gamma^(-1) (C_i,z_i)^T <= 1/2`.

For arbitrary real `a`, arbitrary ORIGINAL-coordinate diagonal `D=diag(d_i)`, arbitrary affine terms, and `lambda !=0`, set

`Q = a H^2 + 2 H <C,X> + X^T D X + lambda <z,X>^2 + affine.`

Then `Q` has an essentially bounded density and

`||p_Q||_infty <= 3*2^(4/3) (|lambda| det Gamma)^(-1/3).`   (3.1)

#### Proof

Apply the pinned mixed-Fresnel theorem with heavy set consisting of the single ORIGINAL hub coordinate, one leaf Fresnel direction `z`, and leaf-hub column `C`. It gives

`|phi_Q(t)| <= B |t|^(-3/2)`,

where

`B=(4 pi)^(3/2) 2^(-1) |lambda|^(-1/2) det(Gamma)^(-1/2).`

Always `|phi_Q(t)|<=1`, hence

`int_R |phi_Q(t)| dt <= int_R min(1,B|t|^(-3/2)) dt = 6 B^(2/3).`

Fourier inversion therefore gives

`||p_Q||_infty <= (1/(2 pi)) 6 B^(2/3)`

`= (3/pi) [(4 pi)^(3/2)/2]^(2/3) (|lambda| det Gamma)^(-1/3)`

`=3*2^(4/3)(|lambda| det Gamma)^(-1/3).`

All diagonal leaf terms are twisted one-coordinate phases in the source theorem. The hub quadratic term is also allowed there. No projected-coordinate independence is used. QED.

The numerical constant is

`3*2^(4/3)=7.559526299...`.

## 4. Determinant compensation for an exact rank-three aggregate

The preceding source theorem becomes target-level in a rank-one leaf chamber because its apparent angle/star losses multiply to the determinant of the actual three-dimensional quadratic matrix.

### Theorem 4.1 — QFORM-RANK1-LEAF-HYBRID-MF-v1

Let `H,X_1,...,X_m` be independent cap-one ORIGINAL variables. Let `x,y in R^m` be orthonormal and assume

`max_i (x_i^2+y_i^2) <= 1/2`.

Put `L=x·X`, `V=y·X`. Consider

`Q = alpha H^2 + 2 s H L + b L^2 + 2 k L V + d V^2 + affine`,

with aggregate coefficient matrix

`M=[[alpha,s,0],[s,b,k],[0,k,d]].`

Assume the leaf block

`N=[[b,k],[k,d]]`

has rank one and all three eigenvalues of `M` have modulus at least one. Then

`||p_Q||_infty <= 3*2^(4/3) |det M|^(-1/3) <= 3*2^(4/3) < 7.560.`   (4.1)

This is an essential-density statement; continuity is not asserted here.

#### Proof

Write the nonzero rank-one leaf block as

`N=lambda u u^T`,  `u=(cos theta,sin theta)`,  `lambda !=0`.

The leaf quadratic is therefore

`lambda Z^2`,  `Z=(cos theta)x·X+(sin theta)y·X`,

whose unit ORIGINAL-coordinate coefficient vector is

`z=(cos theta)x+(sin theta)y`.

The physical hub star is `C=s x`. In the orthonormal leaf basis `[x,y]`, the two columns `[C,z]` are obtained through

`[C,z]=[x,y] B`,

`B=[[s,cos theta],[0,sin theta]].`

If `s sin theta=0`, then the displayed `3x3` matrix `M` is singular, contrary to the hypothesis that its three eigenvalues have modulus at least one. Hence `B` is invertible. Since `Gamma=B^T B`, the normalized leverage at leaf coordinate `i` is

`(x_i,y_i) B (B^T B)^(-1) B^T (x_i,y_i)^T = x_i^2+y_i^2 <=1/2`.

Also

`det Gamma=(det B)^2=s^2 sin^2 theta.`   (4.2)

Because `det N=0`, expansion of the aggregate determinant along the first row gives

`det M = alpha det N - s^2 d = -s^2 d.`

But `d=lambda sin^2 theta`, so

`|det M|=s^2 |lambda| sin^2 theta = |lambda| det Gamma.`   (4.3)

Insert (4.3) into Lemma 3.1. Since the product of the three eigenvalue magnitudes is `|det M|>=1`, (4.1) follows. QED.

### What the determinant identity buys

Neither a small transverse angle nor a small individual star coefficient causes a loss. If the rank-one leaf direction approaches the star direction, `det Gamma` tends to zero, but the exact-rank-three spectral hypothesis forces the rank-one coefficient `|lambda|` and/or the star scale to compensate because their product is precisely `|det M|`. This is the desired kind of endpoint-stable payment: it is algebraic, does not invoke moments or supports, and is made before forgetting source provenance.

## 5. Two actual applications

### 5.1 Partner near-coloop one-tail chamber

The fleet03/B10 r28 frame has `C=sqrt(h) gamma r`, `r perpendicular y`,

`||C||^2>16065/16384`,  `max_i(r_i^2+y_i^2)<1/54`.

Therefore any residual physical form of the exact source-compatible shape

`Q=aH^2+2H<C,X>+X^T D X+lambda (y·X)^2+affine`,

where `D` is ORIGINAL-coordinate diagonal and `|lambda|>=1`, satisfies Lemma 3.1 with

`Gamma=diag(||C||^2,1)`.

Hence the concrete partner-frame inequality is

`||p_Q||_infty <= 3*2^(4/3) (|lambda| ||C||^2)^(-1/3)`

`< 3*2^(4/3) (16065/16384)^(-1/3) < 7.610.`   (5.1)

This spends the partner geometry at a new receiver. In this subchamber the near-coloop star does not lose a power of the leakage parameter. The remaining generic partner form is not claimed to have rank-one leaf curvature; that missing second curvature is exactly the unpaid implication stated in Section 1.

### 5.2 An exact target family through the null endpoint

For any odd `m>=109`, let

`theta_j=2 pi j/m`,

`x_j=sqrt(2/m) cos(theta_j)`,  `y_j=sqrt(2/m) sin(theta_j)`.

Then `x,y` are orthonormal and every leaf row has leverage

`x_j^2+y_j^2=2/m<1/54`.

For `eta>=0`, define

`Q_eta = eta H^2 + 2 sqrt(1+eta) H L + V^2`.

Its aggregate matrix is

`M_eta=[[eta,sqrt(1+eta),0],[sqrt(1+eta),0,0],[0,0,1]]`

with exact nonzero spectrum

`{1+eta,-1,1}`.

Thus this is a valid exact-rank-three target instance for arbitrary independent cap-one ORIGINAL source laws. The two leaf aggregates share all `m` leaves and are generally dependent. Theorem 4.1 gives the endpoint-stable all-level estimate

`||p_(Q_eta)||_infty <= 3*2^(4/3)(1+eta)^(-1/3) <= 7.560.`   (5.2)

There is no singularity as `eta downarrow0`.

The required pinned ruled-level-set theorem is also applied to this same family. Its signature is `(2,1)`, so for every majority-sign level `q>=0`,

`p_(Q_eta)(q) <= pi sqrt(2) < 4.443.`   (5.3)

Equation (5.3) is consumed as a theorem from the source; it is not reproved here.

## 6. The exact obstruction left by a second leaf curvature

The rank-one theorem does not hide the generic difficulty. The following exact target family isolates it while remaining fully diffuse and source-valid.

Use the same Fourier leaf frame `x,y`, now for any odd `m>=109`, and for `eta>=0` set

`R_eta = eta H^2 + 2 sqrt(2(1+eta)) H L + L^2 - V^2.`   (6.1)

The aggregate matrix is

`M_eta^*=[[eta,sqrt(2(1+eta)),0],[sqrt(2(1+eta)),1,0],[0,0,-1]].`

The first `2x2` block has eigenvalues `eta+2` and `-1`; hence

`spec(M_eta^*)={eta+2,-1,-1}`.   (6.2)

So (6.1) is again an exact-rank-three target family with all nonzero eigenvalue magnitudes at least one. It lies in the same diffuse leaf regime `2/m<1/54`.

### 6.1 The direct mixed-Fresnel compiler becomes singular

The leaf block is now genuinely rank two, `N=diag(1,-1)`. Its natural rank-two Fresnel frame is `S=[x,y]`, while the physical star is

`C=sqrt(2(1+eta)) x`.

The augmented Gram appearing in the pinned mixed-Fresnel theorem is therefore

`Gamma = Gram(C,x,y)`

`=[[2(1+eta),sqrt(2(1+eta)),0],`

`  [sqrt(2(1+eta)),1,0],`

`  [0,0,1]],`

and

`det Gamma=0.`   (6.3)

This is not a numerical accident: the star column is exactly parallel to one of the two leaf-curvature directions. Thus the direct rank-two mixed-Fresnel application has no determinant to spend. A different diagonal extraction or a different proof mechanism would be needed; no claim is made that every possible reformulation of the source theorem is impossible.

### 6.2 Every original-coordinate cross block has rank at most two

Write the physical matrix of (6.1) as

`A_eta = eta e_0 e_0^T + s(e_0 x^T+x e_0^T)+x x^T-y y^T`,

where `s=sqrt(2(1+eta))` and `x,y` vanish in the hub coordinate.

For any two disjoint sets of ORIGINAL coordinates `I,J`, the cross block `A_{I,J}` has rank at most two. If neither side contains the hub, this follows immediately from the two leaf outer products. If the hub lies in `I`, every row of the cross block is still a linear combination of `x_J` and `y_J`: the hub row contributes `s x_J`, and every leaf row contributes a combination of `x_J,y_J`. The case with the hub in `J` is symmetric.

Consequently

`e_3(A_{I,J}^T A_{I,J})=0`   (6.4)

for every disjoint cut. The pinned three-volume decoupling theorem D and its relaxed-marginal D' extension therefore give no rank-three payment on this family; the five-volume theorem is also vacuous.

The full-rank Fresnel theorem F also does not directly apply to the exact rank-three spectral frame because the ORIGINAL hub coordinate has range-projection leverage one.

Thus (6.1) is a concrete target-valid survivor of the most direct low-rank versions of the pinned Fourier compilers: the issue is not insufficient spectral size or large transverse leverage, but the fact that the hub star lies inside the two-dimensional non-diagonal leaf-curvature span.

### 6.3 The ruled side is already paid

The signature in (6.2) is `(1,2)`. Apply the pinned ruled theorem to `-R_eta`, whose signature is `(2,1)`. For every `q<=0`,

`p_(R_eta)(q) <= pi sqrt(2).`   (6.5)

Hence the open level-set side for this test family is specifically `q>0`, the minority/two-sheet side. Reproving the one-sheet geometry would not advance the target.

### 6.4 The endpoint itself is paid, so the obstruction is genuine gluing

At `eta=0`, (6.1) becomes

`R_0=2 sqrt(2) H L+L^2-V^2`.

The previously proved dependence-safe endpoint receiver applies because `H` is an ORIGINAL coordinate independent of the leaf pair and the two-dimensional product projection has joint density cap at most `2`. With endpoint parameters `a=sqrt(2)`, `d=-1`, `K=2`, it gives

`||p_(R_0)||_infty <= 6*2^(2/3)*(sqrt(2))^(-2/3)=6*2^(1/3)`

`=3*2^(4/3)<7.560.`   (6.6)

Thus neither the exact null endpoint nor the ruled side is singular. The unpaid object is the positive-Rayleigh gluing of the same-bank second leaf curvature. Coefficient continuity cannot be invoked because the ORIGINAL laws can have arbitrary unbounded and fragmented supports.

### 6.5 Localized physical minors also collapse in the diffuse version

For the exact rank-three factorization `A=R M_eta^* R^T` with rows `e_0` and the Fourier leaf frame, a principal triple containing the hub and leaves `i,j` has determinant

`det(A_{\{0,i,j\}})=det(M_eta^*) (x_i y_j-x_j y_i)^2.`

For the Fourier frame,

`|x_i y_j-x_j y_i| <= 2/m`,

so, for `0<=eta<=1`,

`|det(A_{\{0,i,j\}})| <= 12/m^2 ->0.`   (6.7)

A leaf-only principal triple has rank at most two. Hence this family also prevents a uniform proof from simply selecting one well-conditioned physical `3x3` block as `m` grows.

Equations (6.3), (6.4), and (6.7) isolate a real structural obstruction, not a counterexample to QFORM.

## 7. Why the new theorem is source-safe

1. `H` is an actual ORIGINAL coordinate. Its independence from the leaf bank is genuine.
2. `L,V,Z` are only linear forms of the ORIGINAL leaf variables. They are never declared independent.
3. The mixed-Fresnel theorem is applied before replacing the leaf product law by an arbitrary joint law; its Brascamp-Lieb step sees the ORIGINAL coordinate factors.
4. The only basis changes are deterministic changes of coefficient vectors used to identify Gram matrices and determinants. They are not probabilistic rotations of the inputs.
5. No moment, support, centering, identical-law, log-concavity, smoothness, or continuity assumption is used.
6. The ruled theorem is used only on its proved one-sheet side. The opposite side is kept explicit.

## 8. Result and next step

New proved theorem: the diffuse exact-rank-three one-hub chamber with rank-one non-diagonal leaf curvature has

`||p_Q||_infty < 7.560`,

uniformly through arbitrary hub Rayleigh coefficient, because the mixed-Fresnel determinant loss is exactly compensated by `|det M|`.

New partner-frame corollary: the fleet03/B10 endpoint-stable star/transverse geometry pays every one-tail residual of the form in Section 5.1 by `<7.610`, with no leakage power loss.

New obstruction: the exact target family (6.1) has a full-rank indefinite leaf block, every original-coordinate cross block of rank at most two, a singular direct mixed-Fresnel augmented Gram, collapsing localized `3x3` determinants, and a uniformly paid exact-null endpoint. The pinned ruled theorem pays its majority-sign half. Therefore the next useful implication is precisely

**QFORM-STAR-PARALLEL-SECOND-CURVATURE-RECEIVER-v1:** obtain a uniform bound on the minority/two-sheet side of (6.1), and then its general rank-two-leaf analogue, by retaining the hub/star phase jointly with the second same-bank leaf curvature before absolute values. A successful estimate must remain uniform as `eta downarrow0` and must use ORIGINAL-coordinate product provenance rather than a worst conditional projection density.

Full exact rank three remains open outside the proved chambers above. Full QFORM remains open. Continuity remains separate.
