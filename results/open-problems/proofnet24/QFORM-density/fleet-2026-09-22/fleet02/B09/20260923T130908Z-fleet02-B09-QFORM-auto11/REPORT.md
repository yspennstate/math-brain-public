SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B09, 2026-09-23T13:09:08Z.

# fleet02/B09 auto11 — selected-subvolume fractional BL extends rank-two hub/star compiler to hub leverage < 3/4

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism / complementary constructions and source-valid counterexamples  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN. This run proves a q-dependent selected-minor extension of the fractional three-volume Fourier/Brascamp--Lieb theorem and plugs it into the newest fleet03/B09 aggregate rank-two hub/star compiler. The previous compiler required physical hub-frame leverage at most `1/2`; the new result pays every leverage strictly below `3/4`, with completely arbitrary within-leaf quadratic curvature retained. The endpoint `3/4` is exactly where this Fourier envelope becomes `|t|^{-1}` and ceases to be integrable.

No moments, bounded support, log-concavity, connected support, Gaussianity, diagonal-basis input, post-rotation independence, or small-random-perturbation argument is used. All cuts and marginals are on literal original coordinates. The estimate is obtained by an integrable characteristic-function envelope, so the small-ball conclusion is directly `O(|L|)` with no probability squaring or square-root decoupling loss.

## 1. First unpaid implication

The newest completed designated partner result is fleet03/B09 r32,

`QFORM-RANK2-HUBSTAR-AGGREGATE-COMPILER-v1`,

canonical source

`yspennstate/math-open-problems@56d0211f2f04d74152032fd1914196673eb5c3e6`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T124906Z-fleet03-B09-QFORM-r32/REPORT.md`.

For a physical rank-two hub/star

`A[H,I]=P C^T,   P^T P=I_2`,

with completely arbitrary `D=A[I,I]`, it defines literal singleton third-volume quantities

`Gamma_k^2=e_3(M_k^T M_k)`,

and the aggregate

`G_*=sum_k Gamma_k^2`.

It compiles `G_*` into one genuine source-coordinate cross cut. Its diffuse-singleton branch used a selected family of physical `3x3` minors whose moved-leaf row marginals are `<1/2` and whose hub-row marginals are exactly

`ell_h=(P P^T)_{hh}`.

The old analytic gate therefore stopped at `max_h ell_h<=1/2`.

The first unpaid B09 implication attacked here is

`QFORM-RANK2-HUBSTAR-HIGH-HUBLEVERAGE-OR-SCALE-ROUTING-v1`:

> keep the partner's aggregate-before-reciprocal-minor construction, retain arbitrary within-bank curvature, and pay as much of the high-hub-leverage regime as the true fractional Fourier integrability permits; then isolate the genuine remaining endpoint/high-leverage debt rather than treating the old `1/2` gate as structural.

This run moves the gate from `1/2` to every value `<3/4`. The remaining B09 debt is now the **very-high physical hub leverage regime `>=3/4` with genuinely general leaf curvature**, together with the separate structural task of forcing a universal-scale `G_*` or another already-paid exit from the bare three-large-eigenvalue hypothesis.

## 2. Required sources actually used

### 2.1 Newest Claude package `e5f71d79...`

I read the required `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

Two facts matter here.

1. Theorem H integrates literal physical hub coordinates before Fresnel/BL smoothing and allows arbitrary `A_HH,A_HJ,A_IJ,A_JJ`; it never rotates the random input vector.
2. The fractional-volume extension raises the old row-marginal gate from `1/2` to any `h<3/4` by Jensen, with the loss exactly corresponding to a slower but still integrable Fourier power.

Section 6 below applies Theorem H to an actual target-valid source-coordinate two-hub star and derives an explicit density inequality.

The required counterexample search reports no valid counterexample to the full QFORM conjecture; it specifically leaves delocalized/high-dimensional and convex-side geometry as possible hiding places. Nothing in this run contradicts that status.

### 2.2 Sharp q-dependent volume theorem

I also used the completed sharp-Hausdorff--Young q-dependent theorem at

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

For a literal cross matrix `M`, full three-volume `Z=e_3(M^T M)`, `1<=q<3/2`, and normalized row-volume marginals `alpha_i<=q/2`, it proves

`||p_Q||_inf <= [3e/((3-2q)sqrt(q))] Z^(-1/6)`,

with continuous density, arbitrary same-side phases, and the same coefficient times interval length.

### 2.3 Designated partner fleet03/B09 r32

The r32 compiler gives `c=27/256` and a literal selected physical-minor family of mass `W>=cG_*`. It also proves a concentrated-singleton exit

`||p_Q||_inf <= 3e(512/27)^(1/6)G_*^(-1/6)`

without any hub-leverage assumption. I use both statements below.

## 3. New theorem: q-dependent fractional BL for an arbitrary selected physical minor family

Let `M` be any actual original-coordinate cross matrix. Let `Omega` be any nonempty collection of pairs `(R,C)` of physical row triples and physical column triples. Put

`Z_Omega=sum_(R,C in Omega) det(M[R,C])^2>0`,

and normalize

`pi_(R,C)=det(M[R,C])^2/Z_Omega`.

Let `alpha_i=P_pi(i in R)` and `beta_j=P_pi(j in C)`.

### Theorem `QFORM-FRACTIONAL-SUBVOLUME-BL-q-v1`

For any `1<=q<3/2`, if

`max_i alpha_i<=q/2`,

then every quadratic-plus-affine form having this literal cross matrix, with arbitrary same-side measurable phases and arbitrary conditioned outside coordinates, has a continuous density satisfying

`boxed:
 ||p_Q||_inf
 <= [3e/((3-2q)sqrt(q))] Z_Omega^(-1/6).`

Consequently every interval `L` satisfies

`boxed:
 P{Q in L}
 <= [3e/((3-2q)sqrt(q))] Z_Omega^(-1/6)|L|.`

### Proof

The partner r32 selected-family proof already identifies the only place where completeness of the minor family could matter: the Gaussian BL determinant lower bound. With positive row Gaussian parameters `d_i` and active column parameters `e_j`, the diagonal-plus-PSD determinant expansion gives

`det(D_J+M^T D_I M)`

`>= sum_(all physical 3x3 minors) det(M[R,C])^2 prod_(i in R)d_i prod_(j notin C)e_j`

`>= sum_(R,C in Omega) det(M[R,C])^2 prod_(i in R)d_i prod_(j notin C)e_j`.

Weighted AM--GM with the selected probabilities `pi_(R,C)` yields

`det(D_J+M^T D_I M)`

`>= Z_Omega prod_i d_i^(alpha_i) prod_j e_j^(1-beta_j).`       (3.1)

A column with `beta_j=1` belongs to every positive-weight selected minor, so its endpoint Gaussian parameter never occurs in an active product; this is the same endpoint handling as in the completed source theorem.

After (3.1), the sharp q-dependent proof uses only

`sum_i alpha_i=sum_j beta_j=3`,
`0<=alpha_i,beta_j<=1`,
`alpha_i<=q/2`,

plus independence of the original-coordinate difference variables. It does not use minors outside the determinant lower bound. Thus its Jensen step, sharp Hausdorff--Young row norms, column entropy factor, and Fourier inversion go through verbatim with `Z` replaced by `Z_Omega`, giving

`|phi_Q(t)|<=min(1,K|t|^(-3/(2q)))`.

Because `q<3/2`, the power `3/(2q)>1` is integrable; the exact inversion calculation gives the displayed constant `3e/((3-2q)sqrt(q))`. This proves the theorem.

There is no hidden spectral rotation: `Omega`, `alpha`, and `beta` are all attached to physical source-coordinate minors.

## 4. Main consequence: rank-two hub/star aggregate compiler for every hub leverage < 3/4

Retain the partner r32 setup

`A[H,I]=P C^T,  P^T P=I_2`,

with completely arbitrary symmetric `D=A[I,I]`, and define `Gamma_k,G_*` as in Section 1. Put

`eta=max_(h in H)(P P^T)_(hh)`.

### Theorem `QFORM-RANK2-HUBSTAR-AGGREGATE-q-v1`

Assume

`eta<3/4`,

and set

`q_eta=max(1,2eta)`.

If `G_*>0`, then

`boxed:
 ||p_Q||_inf <= C(eta) G_*^(-1/6),`

where

`C(eta)=max{
  3e(512/27)^(1/6),
  [3e/((3-2q_eta)sqrt(q_eta))](256/27)^(1/6)
}`.

The density is continuous on this branch and

`P{Q in L}<=C(eta)G_*^(-1/6)|L|`

for every interval `L`.

All within-hub curvature `A[H,H]`, the full arbitrary `D=A[I,I]`, outside quadratic blocks/couplings, and conditioning-generated affine terms remain present.

### Proof

Let `c=27/256`.

**Concentrated singleton.** If some

`Gamma_k^2 >= (c/2)G_*`,

the partner r32/r30 literal rank-three cut gives

`||p_Q||_inf<=3e(512/27)^(1/6)G_*^(-1/6)`

with no leverage assumption.

**Diffuse singleton.** Otherwise every

`Gamma_k^2<(c/2)G_*`.

The partner Bernoulli compiler gives a genuine physical cut and selected minor family `Omega_S` with

`Z_(Omega_S)=W(S)>=cG_*`.

For every moved leaf row `k`, r32 proves

`alpha_k<1/2`.

For every physical hub row `h`, factorization of the selected determinant weights gives exactly

`alpha_h=(P P^T)_(hh)<=eta`.

Hence every selected-family row marginal is at most

`max(1/2,eta)=q_eta/2`.

Because `eta<3/4`, `q_eta<3/2`. Apply `QFORM-FRACTIONAL-SUBVOLUME-BL-q-v1` and `W(S)>=cG_*`:

`||p_Q||_inf`

`<= [3e/((3-2q_eta)sqrt(q_eta))] W(S)^(-1/6)`

`<= [3e/((3-2q_eta)sqrt(q_eta))](256/27)^(1/6)G_*^(-1/6)`.

Combining the two cases proves the theorem.

For `eta<=1/2`, `q_eta=1` and this recovers the partner's diffuse branch. For `1/2<eta<3/4`, it is a strict extension. As `eta` approaches `3/4`, `q_eta` approaches `3/2` and the denominator `3-2q_eta` vanishes: this is the exact `|t|^{-1}` Fourier-integrability endpoint of this mechanism, not a counterexample to QFORM.

## 5. Actual target-valid high-rank dense-curvature inequality beyond the old 1/2 gate

This section applies the newest partner compiler and the new q-selected theorem to a literal target matrix, not just to abstract notation.

Let the physical hub bank have three coordinates and take the equal-norm Parseval frame

`p_1=(sqrt(2/3),0)`,
`p_2=(-1/sqrt(6),1/sqrt(2))`,
`p_3=(-1/sqrt(6),-1/sqrt(2))`.

Then `P^TP=I_2` and every hub leverage is exactly

`ell_h=2/3`.

Let `m>=32` be a Walsh dimension. On the leaf bank choose a complete flat Walsh orthonormal basis

`c_1,c_2,v_3,...,v_m`,

and signs `sigma_3,...,sigma_m in {+1,-1}` with equal numbers of each sign, so `sum sigma_l=0`. Put

`C=[c_1,c_2]`,

`D=sum_(l=3)^m sigma_l v_l v_l^T`,

and form the block matrix

`A=[[0, P C^T],[C P^T,D]]`.

The leaf curvature `D` has rank `m-2` and is generally dense in physical coordinates. It is retained exactly.

Algebraically, the hub `P`-subspace couples isometrically to `span{c_1,c_2}`, giving eigenvalues

`+1,-1,+1,-1`.

On the orthogonal leaf complement, `D` has eigenvalues `sigma_3,...,sigma_m`, all of modulus one. The one hub direction orthogonal to `range P` is null. Thus **every nonzero eigenvalue of A has modulus one**, in particular the owner target has far more than three large eigenvalues.

Now compute the partner singleton resource exactly. For a leaf index `k`, the two truncated Walsh rows have Gram determinant

`det(C_{-k}^T C_{-k})=1-2/m`.

Write `a_k=D[k,I\{k}]`. Since all Walsh vectors are flat and `sum sigma_l=0`,

`<a_k,c_1|_{-k}>=<a_k,c_2|_{-k}>=0`,

and

`||a_k||_2^2=1-2/m`.

Therefore

`Gamma_k^2`

`=sum_(|J|=3,J not contains k) det([C_J^T;D[k,J]])^2`

`=(1-2/m)^2`.

Hence

`boxed: G_*=m(1-2/m)^2.}`

Moreover

`Gamma_k^2/G_*=1/m<27/512`

for `m>=32`, so this is genuinely the partner's **diffuse-singleton** branch; the old concentrated-singleton escape does not apply. The old r32 diffuse theorem also does not apply because `eta=2/3>1/2`.

Our extension uses

`q_eta=4/3`.

The diffuse constant is

`[3e/((3-8/3)sqrt(4/3))](256/27)^(1/6)`

`=(9sqrt(3)e/2)(256/27)^(1/6)`

`=30.823384457...`,

larger than the concentrated-case constant `13.316806914...`. Consequently this actual target family satisfies

`boxed:
 ||p_(X^T A X)||_inf
 <=30.824 [m(1-2/m)^2]^(-1/6),`

and

`boxed:
 P{X^T A X in L}
 <=30.824 [m(1-2/m)^2]^(-1/6)|L|.`

This is dimension-free (indeed it improves with `m`) for arbitrary independent cap-one input densities, despite dense rank-`m-2` same-side curvature and hub leverage `2/3`.

No eigenbasis independence is used: the Walsh basis is only an algebraic construction of the coefficient matrix; the analytic proof uses physical-coordinate cuts.

## 6. Required application of the completed `e5f71d79...` mixed-hub theorem to an actual source-coordinate star

To consume the owner-required completed Theorem H at a real inequality, take two literal physical hub coordinates `X_1,X_2` and an `m>=8` leaf bank `Y`. Let `c_1,c_2,v` be three flat orthonormal Walsh vectors and set

`Q_m=2X_1<c_1,Y>+2X_2<c_2,Y>+<v,Y>^2`.

The active coefficient matrix on the algebraic span of the two physical hubs and `c_1,c_2,v` has spectrum

`{+1,-1,+1,-1,+1}`,

so this is target-valid. Physical hub-leaf entries are `O(m^-1/2)` and the same-side dense square has entries `O(m^-1)`.

Apply Theorem H with the **literal physical hubs** `H={1,2}`, rank-one leaf curvature `lambda=1,v`, and leaf bank `I`. Its augmented mixed rows are

`rho_i=(v_i,(c_1)_i,(c_2)_i)`.

Their Gram is exactly `I_3` and each normalized physical row leverage is `3/m<=1/2`. Theorem H therefore gives

`|phi_(Q_m)(t)|`

`<= (2|t|)^(-2)(4pi|t|)^(-1/2)(4pi)^3`

`=8 pi^(5/2)|t|^(-5/2)`.

Integrating `min(1,8pi^(5/2)|t|^(-5/2))` and applying Fourier inversion yields the explicit source-valid inequality

`boxed:
 ||p_(Q_m)||_inf
 <=(5/3) 8^(2/5)
 =(5/3)2^(6/5)
 =3.828994516... .}`

Thus

`P{Q_m in L}<=3.829|L|`.

This example has extreme two-dimensional hub-frame leverage `1` if the rank-two hub factor is written with `P=I_2`, yet is still paid because the dense same-side leaf square supplies a genuinely transverse mixed-Hub smoothing direction. Therefore **high hub leverage itself is not the obstruction**. The remaining high-leverage debt is specifically the regime with genuinely general leaf curvature for which no compatible determinant-balanced/mixed-frame packet has yet been forced.

## 7. Scope and obstruction after this run

The new selected-family theorem stops at `eta<3/4` for a precise analytic reason. At `eta=3/4`, the smallest Jensen exponent allowed by the row gate is `q=3/2`, so the characteristic-function power is

`3/(2q)=1`.

The resulting absolute-value Fourier envelope is not integrable. Taking `q>3/2` only makes the power worse. Therefore this exact fractional-volume route cannot simply be continued through `eta=3/4` by changing constants.

This is **not** a counterexample to the QFORM conjecture. Section 6 already gives a target-valid `eta=1` family paid by a different mixed-hub resource. The correct first unpaid implication is now

`QFORM-RANK2-HUBSTAR-VERY-HIGH-LEVERAGE-GENERAL-CURVATURE-v1`:

> Starting from the bare three-large-eigenvalue condition and the rank-two hub/star survivor, either (a) force `eta<3/4` with a universal-scale aggregate `G_*`, now paid here; (b) expose a determinant-balanced low-rank-plus-diagonal mixed-hub packet, an actual rank-three cut, ridge/pair/definite/multi-hyperbolic exit, now already paid; or (c) in the residual `eta>=3/4` general-curvature geometry, exploit the concentrated physical hub direction together with a genuine third spectral resource without conditioning that resource away. Also still required is the global structural lower bound/routing from `s_3(A)>=1` to one of these certificates.

A proposed proof that merely replaces the `1/2` gate by `1` in the same absolute-value Fourier argument would be invalid; its envelope crosses the nonintegrable endpoint. No claim beyond the exact `<3/4` theorem is made.

## 8. Counterexample-search status and continuity

The required pinned counterexample search found no valid counterexample to the full target. This run also found none. The q-selected and Theorem-H branches above each have an `L^1` characteristic function, hence a continuous density vanishing at infinity. Full-target continuity remains separate and open because the global theorem remains open.

Independent review status: **pending**. The selected-family q-extension is short and source-local, but it has not been independently rechecked in this run.

## 9. Telemetry scope

Model self-report: GPT-5.6 Sol. Requested reasoning effort: maximum actually supported. Configured/self-reported reasoning level: UNKNOWN. Provider reasoning-token and pure-thinking-time telemetry: UNKNOWN/null/not exposed. Any elapsed execution field recorded by the run includes reasoning, connector/network activity, output generation, and overhead and is not pure thinking.
