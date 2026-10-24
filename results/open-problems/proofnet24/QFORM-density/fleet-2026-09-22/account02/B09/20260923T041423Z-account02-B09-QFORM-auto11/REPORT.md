# account02/B09 — determinant-balanced mixed-hub smoothing with arbitrary dense same-side curvature

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism; complementary constructions / source-valid counterexamples  
Status: **ESSENTIAL_STEP_APPLIED / STRICT-N3 STAR PAID / FULL TARGET OPEN**  
Execution label: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains open. This report proves a new branch for an original-coordinate hub/star with a completely retained dense within-leaf quadratic operator. The operator is not dropped, treated as a small random error, or diagonalized and then declared independent. Instead its exact off-diagonal part is spectrally expanded only as a coefficient identity inside the original product coordinates, and a determinant-weighted physical-basis law pays the resulting mixed Fourier integral.

No moments, compact support, log-concavity, connected support, identical laws, Gaussianity, or independence after rotation are used. All input independence is the original coordinate independence. The final interval estimate is linear in interval length; there is no probability squaring / square-root decoupling loss.

## 1. First unpaid implication

The current B09 debt is

`QFORM-HUB-PLUCKER-SMALLRHO-OR-DEGENERATE-G-ROUTING-v1`:

> In the no-small-physical-pivot hub/star survivor, write the exact leaf curvature as diagonal plus its full spectral expansion in coefficient space. Either force a universal-scale determinant-balanced mixed-hub certificate of the theorem below, or route small disjoint-basis mass / nearly singular mixed Gram matrix / weak curvature product to an already-paid physical-pair, zero-hubpair wedge, cross-volume, grouped-slope, ridge, or finite-core exit while keeping the external third source-compatible smoother unconditioned.

For the rank-two leaf-curvature case, failure by small disjoint-basis mass already yields a concrete three-physical-coordinate localization witness (Section 4). What remains is the quantitative routing of that witness with arbitrary residual curvature and without inventing post-rotation independence.

## 2. Completed inputs actually used

### 2.1 Newest-Claude mixed-hub reduction

At the owner-required source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`,

Theorem H proves the exact mixed-hub Fourier reduction. For one original-coordinate hub `h`, a leaf bank `I`, arbitrary remaining bank `J`, and

`A_II = D + sum_(k=1)^r lambda_k v_k v_k^T`,

with `D` diagonal, the proof first conditions on `J`, integrates the untouched physical hub using `f_h<=1`, and applies Fresnel linearisation only to the displayed coefficient identity. Before its final leverage-gated Brascamp--Lieb step, it gives the exact factors

`(2|t|)^(-1) prod_k (4 pi |t lambda_k|)^(-1/2)`

multiplying an `(r+1)`-dimensional Fourier integral whose row vectors are

`(v_{1i},...,v_{ri},A_{ih})`.

The blocks `A_hh,A_hJ,A_IJ,A_JJ` and all conditioning-generated affine terms are arbitrary. This precise pre-gate reduction is applied at equation (3.3) below.

The same required source package's `FOURIER_ROUTE_REPORT.md` and `COUNTEREXAMPLE_SEARCH.md` were read at the same pinned commit. They preserve the full conjecture as open and prohibit replacing the product law by an arbitrary rotated joint law.

### 2.2 Determinant-weighted entropy Brascamp--Lieb

The completed theorem `QFORM-PLUCKER-ENTROPY-BL-v1` is

`yspennstate/math-open-problems@32c257209b588141fb60af698f478f1d0ad20b8a`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260922T123512Z-b07-qform-minors-11/REPORT.md`.

For any `N x d` matrix `U` with orthonormal columns, Pluecker weights

`w_S=det(U_S)^2`, `|S|=d`,

sum to one. If `pi` is a basis law with inclusion marginals `p_i<=1/2`, then for arbitrary cap-one one-dimensional factors with arbitrary one-coordinate phases,

`int_(R^d) prod_i |hat g_i(<U_i,z>+a_i)| dz
 <= exp(D(pi||w)/2) (2 pi)^d e^(d/2)`.                 (2.1)

If `S,T` are iid from the Pluecker law and

`rho=P(S cap T=empty)>0`,

conditioning on disjointness gives such a `pi`, with

`D(pi||w)<=log(1/rho)`.                                 (2.2)

This result is valid for general frame dimension `d`, not only `d=3`.

## 3. New theorem: mixed hub plus arbitrary dense same-side curvature

Let the original coordinates be split as `{h} union I union J`. The inputs are independent and each density is bounded by one. Allow arbitrary affine terms. Assume only that the exact leaf principal block is written

`A_II=D+sum_(k=1)^r lambda_k v_k v_k^T`,              (3.1)

where `D` is diagonal, `r>=1`, and every `lambda_k!=0`. No low-rank approximation is being made: for an arbitrary symmetric `A_II`, one may take `D=diag(A_II)` and spectrally expand the exact symmetric off-diagonal remainder `A_II-D`.

Put

`c=A[I,h]`,

`W=[v_1,...,v_r,c]`,

`G=W^T W`, `d=r+1`.                                     (3.2)

Assume `G>0`. Whiten the physical frame by

`U=W G^(-1/2)`,

so `U^T U=I_d`. For every `d`-subset `S` of leaf coordinates let

`w_S=det(U_S)^2`,

and define the exact determinant-weighted disjoint-basis mass

`rho=sum_(S cap T=empty) w_S w_T`.

### Theorem `QFORM-MIXED-HUB-PLUCKER-SMOOTHING-v1`

If `rho>0`, then the full quadratic form has a continuous density and

`boxed:
 ||p_Q||_infinity
 <= C_r [rho det(G) prod_(k=1)^r |lambda_k|]^(-1/(r+2)),`

where

`C_r=((r+2)/r) exp((r+1)/(r+2)).`                       (3.3)

Consequently every interval `L` satisfies

`boxed:
 P{Q in L}
 <= C_r [rho det(G) prod_k |lambda_k|]^(-1/(r+2)) |L|.` (3.4)

The blocks `A_hh,A_hJ,A_IJ,A_JJ` are arbitrary, as are all affine terms.

### Proof

Condition on the original coordinates in `J`. Theorem H's proof, applied before its final leverage gate, integrates the physical hub variable using only `f_h<=1`. The substitution `y=2tX_h` contributes `(2|t|)^(-1)`. Fresnel linearisation of the exact rank-`r` coefficient identity in (3.1) contributes

`prod_k (4 pi |t lambda_k|)^(-1/2)`.

The remaining absolute Fourier integral has the form

`J_t=int_(R^d) prod_(i in I)
     |hat g_i(<W_i,z>+a_i)| dz`,                         (3.5)

where `|g_i|=f_i`; the diagonal terms in `D` are one-coordinate phases and `a_i` contains arbitrary conditioning-generated translations.

Set `z'=G^(1/2)z`. Then `Wz=Uz'` and

`J_t=det(G)^(-1/2)
    int_(R^d) prod_i |hat g_i(<U_i,z'>+a_i)| dz'.        (3.6)

A frequency shift of one factor is just another one-coordinate phase, so (2.1)-(2.2) apply without any restriction on the `a_i`. Hence

`J_t <= det(G)^(-1/2) (2 pi)^d e^(d/2) rho^(-1/2).`     (3.7)

Combining (3.7) with the hub and Fresnel factors gives, for `t!=0`,

`|phi_Q(t)| <= A |t|^(-alpha)`,                          (3.8)

with

`alpha=(r+2)/2`

and

`A=pi^alpha e^((r+1)/2)
  [rho det(G) prod_k |lambda_k|]^(-1/2).`                (3.9)

Indeed the powers of two cancel exactly:

`2^(-1) (4 pi)^(-r/2) (2 pi)^(r+1)=pi^((r+2)/2)`.

Together with `|phi_Q(t)|<=1`,

`int_R |phi_Q(t)|dt
 <=2 alpha/(alpha-1) A^(1/alpha).`                       (3.10)

Fourier inversion therefore gives

`||p_Q||_infinity
 <= alpha/[pi(alpha-1)] A^(1/alpha)
 =((r+2)/r)e^((r+1)/(r+2))
   [rho det(G) prod_k |lambda_k|]^(-1/(r+2)),`

which is (3.3). Since `alpha>1`, the envelope is integrable, so the density is continuous on this branch. Averaging over the conditioned original coordinates in `J` preserves the same bound. QED.

Two useful constants are

`C_1=3 e^(2/3)<5.844`,

`C_2=2 e^(3/4)<4.235`.

This improves the raw natural-leverage constant on the overlap and, crucially, permits individual mixed physical leverages larger than one half when the determinant mass still supports two disjoint coordinate bases.

## 4. Small `rho` produces a physical localization witness

The same determinant law gives an exact failure certificate. For a basis `S`, let

`R_S=sum_(i notin S) U_i U_i^T=I_d-U_S^T U_S`.

The complementary-minor identity gives

`sum_(T subset S^c, |T|=d) w_T=det(R_S)`.

Since

`rho=sum_S w_S det(R_S)`,

some Pluecker basis `S` satisfies

`det(R_S)<=rho`.                                         (4.1)

Let `s_min` be the smallest eigenvalue of `R_S`. Because every eigenvalue of `R_S` lies in `[0,1]`,

`s_min^d<=det(R_S)<=rho`.

Thus there is a unit direction `z in R^d` with

`sum_(i notin S) |<U_i,z>|^2 <= rho^(1/d)`,              (4.2)

or equivalently an active mixed direction carrying at least

`1-rho^(1/d)`

of its coordinate energy on only `d=r+1` physical leaves. For the main `r=2` star/curvature packet, small `rho` therefore produces a three-coordinate localized mixed direction. This is a structural alternative, not a density estimate by itself; the remaining routing must retain all residual curvature and the external target direction.

## 5. Strict-N3 target star where the old leverage gate fails

Take the no-pivot threshold `tau=1/128`. Split a leaf bank into three disjoint supports `I_1,I_2,I_3`.

On `I_1`, choose a unit vector `v_1` whose squared coordinate weights are

`0.6` and one hundred copies of `0.004`.

On `I_2`, let `v_2` be flat on 256 coordinates. On `I_3`, let `c` be flat on 256 coordinates. The three vectors are orthonormal because their supports are disjoint.

Define

`B_1=v_1v_1^T-diag(v_{1i}^2)`,

`mu_1=lambda_max(B_1)`, `lambda_1=1/mu_1`,

and

`B_2=v_2v_2^T-diag(v_{2i}^2)`, `lambda_2=256/255`.

The first Rayleigh quotient gives

`mu_1 >= v_1^T B_1 v_1
       =1-sum_i v_{1i}^4
       =1-(0.36+100*0.004^2)
       =0.6384`.                                          (5.1)

Also `B_1<=v_1v_1^T` in Loewner order, hence `mu_1<=1`; therefore

`1<=lambda_1<=1/0.6384<1.567`.                            (5.2)

Let the full source-coordinate matrix be

`A_hh=0`,

`A[I,h]=c`,

`A_II=lambda_1 B_1+lambda_2 B_2`,

with all other entries zero. This has exactly the theorem form with

`D=-lambda_1 diag(v_{1i}^2)-lambda_2 diag(v_{2i}^2)`

and rank-two dense terms `lambda_1v_1v_1^T+lambda_2v_2v_2^T`.

### 5.1 Target spectrum

The supports are disjoint, so the matrix is an orthogonal direct sum of three source-coordinate pieces. The hub plus `c` support is the star block

`[[0,c^T],[c,0]]`,

with nonzero eigenvalues `+1,-1`. By definition `lambda_1B_1` has largest eigenvalue `+1`; and `lambda_2B_2` has largest eigenvalue

`(256/255)(255/256)=1`.

Thus the full matrix has at least the four eigenvalues

`{1,-1,1,1}`

of modulus at least one.

### 5.2 Strict N3

Every physical diagonal is exactly zero. Therefore every physical `2 x 2` principal determinant is `-A_ij^2`.

The star coefficients satisfy `c_i^2=1/256<1/128`. On the second curvature support every off-diagonal coefficient equals `1/255`. On the first support, the largest unscaled product is the heavy/small product

`|v_{1i}v_{1j}|^2<=0.6*0.004=0.0024`.

Using (5.2),

`max_(i!=j) |lambda_1v_{1i}v_{1j}|^2
 <=0.0024/0.6384^2
 <0.005889
 <1/128`.                                                (5.3)

Hence every `|A_ii|<1/128` and every physical pair determinant has magnitude `<1/128`: this is a literal strict-N3 target matrix.

### 5.3 Old gate fails, determinant balance pays

Here `W=[v_1,v_2,c]` already has orthonormal columns, so `G=I_3`. The heavy row has leverage

`0.6>1/2`,

so the original natural-leverage version of Theorem H does not apply.

But because the three directions have disjoint supports, a Pluecker basis chooses one coordinate from each support and its weight is the product of the three squared coordinate weights. Two bases are disjoint exactly when the choices differ in every support. Hence

`rho
 =(1-(0.6^2+100*0.004^2))(255/256)^2
 =0.6384(255/256)^2
 =0.6334222412109375`.                                  (5.4)

Since `lambda_1lambda_2>=1`, Theorem (3.3) with `r=2` gives

`boxed:
 ||p_Q||_infinity
 <=2e^(3/4) rho^(-1/4)
 <4.746.`                                                (5.5)

Thus a genuine strict-no-pivot original-coordinate star with dense same-side couplings is controlled uniformly for every admissible product law, even though the completed newest-Claude Theorem H's raw leverage gate fails.

## 6. Required designated-partner theorem applied to a real inequality

The latest completed account03/B09 result available to this run is

`QFORM-GROUPED-TWOSLOPE-ONEFRESNEL-DISJOINT-v1`,

canonical source

`yspennstate/math-open-problems@0ca2df8a2cfb2702f2498ee6924f3a7cee63166a`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T034845Z-account03-B09-QFORM-r23/REPORT.md`.

It states, for disjoint original-coordinate banks with rank-two cross block `C`, one transverse same-side Fresnel direction `v`, and active disjoint-basis mass `rho`, that

`||p_Q||_infinity
 <=(5e/3)[|lambda| delta^2 pdet(CC^T) rho]^(-1/5)`.       (6.1)

Apply it to a second strict-N3 matrix built from the same heavy vector `v_1` on `I_1`, two flat unit vectors `r_1,r_2` on disjoint 256-coordinate supports `I_2,I_3`, and two physical coordinates `Z_1,Z_2` in a disjoint bank `J`:

`T=2<r_1,X_I>Z_1+2<r_2,X_I>Z_2
  +lambda_1[(<v_1,X_I>)^2-sum_i v_{1i}^2X_i^2]`.         (6.2)

Here `C=[r_1,r_2]`, so `pdet(CC^T)=1`; `v_1` is orthogonal to `range(C)`, so `delta=1`; and the active orthonormal frame `[v_1,r_1,r_2]` has exactly the same disjointness mass (5.4). Moreover `lambda_1>=1`. Therefore (6.1) gives the actual inequality

`boxed:
 ||p_T||_infinity
 <=(5e/3) rho^(-1/5)
 <4.964,`                                                (6.3)

and the same coefficient multiplies every interval length.

This matrix is also strict N3(1/128): all physical diagonals are zero, the cross coefficients have square `1/256`, and the heavy-curvature coefficients satisfy (5.3). Its spectrum contains two independent hyperbolic pairs `+1,-1,+1,-1` plus the curvature eigenvalue `+1`, so it satisfies the full target spectral hypothesis. This is an actual application of the designated partner theorem, not a bibliography-only citation.

The partner packet is complementary to the new theorem in Section 3: account03/B09 spends two grouped cross slopes plus one curvature direction; the present result spends one physical hub plus arbitrarily many exact same-side curvature directions.

## 7. Regression controls and limitations

1. If `r=1` and the star vector is exactly parallel to the curvature vector, then `det G=0`. For two independent cap-one uniforms, the source-coordinate model `2XY+Y^2=Y(2X+Y)` has a logarithmically unbounded density at zero. Its active matrix has only rank two, so it is not a QFORM counterexample; it shows why an external third direction cannot be silently conditioned away at the degenerate mixed-Gram endpoint.

2. Small `rho` is not declared a counterexample. Equation (4.2) shows it is a localization flag. A valid full proof still has to combine that localized mixed direction with the remaining target spectrum while preserving the product provenance.

3. The theorem does not assert a universal lower bound on `rho detG prod|lambda_k|` from `s_3(A)>=1`. Establishing a compatible exhaustive alternative is precisely the remaining structural debt.

4. Continuity is proved only on the integrable-Fourier branch in this report. The owner target is essential boundedness; full-target continuity remains separate and open.

## 8. Proof-map change

The earlier mixed-hub route stopped whenever one physical row of the augmented curvature/star frame had leverage above one half. That is no longer a valid stopping point. The exact replacement is:

- if determinant mass supports two disjoint physical bases at quantitative scale, pay the entire dense same-side operator and the hub simultaneously by (3.3), even with a leverage-`0.6` physical row;
- if the disjointness mass is small, extract the explicit `(r+1)`-coordinate localized active direction (4.2);
- if the mixed Gram is nearly singular, treat it as an algebraic near-collapse of the star into the curvature span and retain an external smoother rather than deleting it;
- combine those concentrated survivors with the already-paid physical-pair, zero-hubpair wedge, grouped-slope, cross-volume and ridge exits.

For `r=2`, the first genuinely unpaid branch is therefore a three-physical-leaf localized mixed direction plus arbitrary residual curvature in strict N3. No claim of full closure is made.

## 9. Source integrity

Required newest-Claude package read at `e5f71d79eff325201dd0274053d20268ce65b837`: `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md`.

Completed mathematical inputs used at equations:

- e5f71d79eff325201dd0274053d20268ce65b837, Theorem H pre-leverage mixed-hub reduction, used in (3.5)-(3.8);
- 32c257209b588141fb60af698f478f1d0ad20b8a, `QFORM-PLUCKER-ENTROPY-BL-v1`, used in (3.7) and Section 4;
- 0ca2df8a2cfb2702f2498ee6924f3a7cee63166a, latest completed account03/B09 theorem, applied at (6.3).

Independent review of the new theorem: **not yet performed**. Full QFORM: **OPEN**.
