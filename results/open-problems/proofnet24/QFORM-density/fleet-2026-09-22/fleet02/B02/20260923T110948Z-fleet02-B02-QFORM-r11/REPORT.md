SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B02, 2026-09-23T11:09:48Z.
attacking: Integrated Fourier estimate: sharpen the live D'/D5 cross-block route and attack the transport-fail mixed-hub receiver using the latest compatible partner result.

# fleet02/B02 r11 — bankwise Schur shear and grouped L1 Fourier receiver

## Status and first unpaid implication

**Status:** `ESSENTIAL_STEP_APPLIED`; the full QFORM target remains **OPEN**.  The target-wide statement `\int_R |phi_Q(t)|dt <= C` under only the three-large-eigenvalue hypothesis remains **OPEN / not refuted**.  Continuity is proved on the new branch below because the full characteristic function is genuinely in `L1`; full-target continuity is not claimed.

The first unpaid implication is now `QFORM-SCHUR-NEARRANK1-TRANSVERSE-RECEIVER-v1`: on the invertible double-anchor residue with `G=D^2||S||_F^2` and low stable rank, the exact-rank-one Schur residual is paid below.  If `rank(S)>=2` but the transverse singular product is arbitrarily small, one must spend a second physical resource (incident third volume, an H2 strip, a grouped hub/star packet, or a separately verified TRUE symmetric Schur mechanism) without deleting the small cross tail.  The singular two-anchor branch is partly paid below after choosing only a genuinely nonzero scalar physical pivot.  This is the remaining collar after the partner's stable-rank-four D5 receiver and the theorem of this run.

## 1. Sources consumed and analytic audit

Fresh owner control remained QFORM-only, revision `2026-09-22.15`.  Required source package:

- `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`;
- q-dependent sharp-HY continuation `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`;
- projection-density input `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`;
- designated partner fleet03/B02 r28, `QFORM-DOUBLEANCHOR-E5-SCHUR-BRIDGE-v1`, canonical mathematics `yspennstate/math-open-problems@3dc52765d1ebb50341bba6a4fea5ca8d68f97372`;
- compatible grouped-cross result fleet03/B09 r30, `yspennstate/math-open-problems@562304f5ab9c8b19ba586a31e55a5a4535cbe445`.

I rechecked the q-dependent sharp Hausdorff--Young calculation on its analytic scope.  For a physical cross block `M`, `Z=E3(M)=e3(M^TM)`, if all third-volume row marginals satisfy `alpha_i<=q/2`, `1<=q<3/2`, then

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] Z^(-1/6)`.

The endpoint `q=1` is admissible and gives `3e Z^(-1/6)`; `q=3/2` is exactly the non-`L1_t` endpoint.  The same calculation at degree five with `q=2` is ungated and gives

`||p_Q||_infinity <= (5e/sqrt(2)) E5(M)^(-1/10)`.

Thus the analytic audit is **PASS** for these constants/endpoints.  No claim is made here about independent matrix/tail reviews assigned to other slots.

## 2. New theorem — `QFORM-CROSS-SCHUR-SHEAR-GROUPED-L1-v1`

Let `I=H disjoint_union I0` and `J=K disjoint_union J0` be two disjoint banks of ORIGINAL coordinates.  Condition on every coordinate outside `I union J`.  Write the physical cross block, after reordering only coordinates, as

`B = [[P,R],[C,M]]`,

where `P` is an invertible physical `k x k` block.  Put

`S=M-C P^(-1)R`.

Let `r=rank(S)`, take a thin SVD

`S=U Sigma V^T`,

and write

`Delta_r(S)=prod_{j=1}^r sigma_j(S)`, with `Delta_0=1`.

For an orthonormal frame `U`, define the source-valid projection cap

`mathcal B(U)=prod_i (1-ell_i(U))^(-(1-ell_i(U))/2)`,

with factor one at leverage one.  The weighted affine-fiber BL theorem gives `mathcal B(U)<=e^(r/2)`, and similarly for `V`.

Set `d=k+r`.  If `d>2`, then the full ambient quadratic-plus-affine form, with arbitrary same-bank quadratic terms and arbitrary outside couplings, obeys

`boxed:
 |phi_Q(t)| <= min{1,
  pi^(d/2)|t|^(-d/2)
  [mathcal B(U)mathcal B(V)]^(1/2)
  (|det P| Delta_r(S))^(-1/2)}.
`

Consequently

`boxed:
 ||p_Q||_infinity
 <= [d/(d-2)] [mathcal B(U)mathcal B(V)]^(1/d)
    (|det P| Delta_r(S))^(-1/d).
}`

In particular,

`boxed:
 ||p_Q||_infinity
 <= [(k+r)/(k+r-2)] exp(r/(k+r))
    (|det P| Delta_r(S))^(-1/(k+r)).
}`

The characteristic function is in `L1`, so this branch has a bounded continuous density vanishing at infinity.

### Proof

Write the two banks as `(x,u)` and `(y,v)`, where `x,y in R^k` are the physical anchor variables.  The whole cross phase before the global factor two is

`x^T P y + x^T Rv + u^T C y + u^T Mv`.

Make **bankwise** triangular changes of variables

`xi  = x + P^(-T) C^T u`,
`eta = y + P^(-1) R v`.

They do not mix the two independent source banks.  Direct expansion gives the exact identity

`x^T P y + x^T Rv + u^T C y + u^T Mv
 = xi^T P eta + u^T S v.`

This is only an algebraic cross-Schur identity.  It does **not** identify `S` with a TRUE full symmetric Schur complement.

Crucially, no independence is declared after either shear.  For the first bank the transformed density is

`f_I0(u) f_H(xi-P^(-T)C^T u)`.

Let `z=U^T u`.  The joint density of `(xi,z)` is

`g_A(a,z)=int_{U^T u=z} f_I0(u) f_H(a-P^(-T)C^T u) dmu_z(u)`.

Since every original anchor density is at most one, `f_H<=1`, hence

`g_A(a,z) <= p_(U^T X_I0)(z) <= mathcal B(U)`.

The last inequality is the weighted affine-fiber BL projection theorem, which controls the **joint projected density** without asserting coordinatewise independence.  Similarly the joint density of `(eta,V^T v)` is at most `mathcal B(V)`.  The two grouped vectors remain independent of each other because the two transformations act separately on the two original independent banks.

All same-bank quadratic and affine phases, including those made dense by the shears, stay inside their own bank.  Disintegrating each bank over the grouped variables gives complex amplitudes `alpha_t(a,z)` and `beta_t(b,w)` with

`|alpha_t|<=g_A`, `||alpha_t||_2<=mathcal B(U)^(1/2)`,
`|beta_t|<=g_B`,  `||beta_t||_2<=mathcal B(V)^(1/2)`.

Because `u^TSv=(U^Tu)^T Sigma(V^Tv)`, the remaining cross phase is

`2t Z_A^T D Z_B`,  `D=diag(P,Sigma)`,

in dimension `d`, and `|det D|=|det P| Delta_r(S)`.  Cauchy--Schwarz and Plancherel with the convention `hat f(q)=int f(w)e^(iq.w)dw` give, uniformly in every outside conditioning value,

`|phi_z(t)|
 <= pi^(d/2)|t|^(-d/2)
    ||alpha_t||_2 ||beta_t||_2 |det D|^(-1/2)`.

Averaging the outside coordinates preserves the same bound.  Combining it with `|phi_Q|<=1` gives the displayed envelope.  For `a=d/2>1`,

`(1/(2pi)) int_R min{1,A|t|^(-a)}dt
 = [d/(d-2)] [mathcal B(U)mathcal B(V)]^(1/d)
   (|det P|Delta_r(S))^(-1/d)`,

because `A^(2/d)=pi [mathcal B(U)mathcal B(V)]^(1/d)(|detP|Delta)^(-1/d)`.  Fourier inversion proves the theorem. `QED`

## 3. Apply the designated fleet03/B02 partner to a live inequality

The partner r28 starts from the double-anchor packet

`B=[[P,R],[C,M]]`, `D=|det P|`, `S=M-CP^(-1)R`,
`G=||det(P)M-C adj(P)R||_F^2=D^2||S||_F^2`.

It proves

`E5(B)>=D^2 E3(S)`

and, if `rho=sr(S)>3`,

`E5(B)>=[(rho-3)/(6rho)] G^3/D^4`.

Applying the **reviewed sharp-HY D5 constant** to this actual inequality gives

`boxed:
 ||p_Q||_infinity
 <=(5e/sqrt(2))[6rho/(rho-3)]^(1/10)
   D^(2/5)G^(-3/10).
}`

At `rho>=4`, this is

`||p_Q||_infinity <13.205980 D^(2/5)G^(-3/10)`.

The partner's stronger regularized-determinant integration improves `13.205980` to `9.302883`.  On its live residue `G>Z3/24`, that completed partner branch gives

`||p_Q||_infinity <24.136869 D^(2/5) Z3^(-3/10)`.

Thus D5 pays the high-stable-rank double-anchor residue.  The theorem of Section 2 attacks the complementary low-rank side without pointwise decay.

### Exact rank-one Schur residue

If `rank(S)=1`, then `Delta_1(S)=||S||_F` and `d=3`.  Section 2 gives

`||p_Q||_infinity
 <=3[mathcal B(U)mathcal B(V)]^(1/3)(D||S||_F)^(-1/3)
 <=3e^(1/3)G^(-1/6)`.

On the partner's live `G>Z3/24` packet,

`boxed:
 ||p_Q||_infinity <7.110847 Z3^(-1/6).
}`

This is a genuine `L1_t` receiver for the exact-rank-one endpoint left by the partner's `sr(S)<4` complement; the two anchor directions and the one grouped Schur direction jointly supply the required `|t|^(-3/2)` decay.

### Exact rank-two and rank-three Schur residues

If `rank(S)=2`, write `rho=sr(S) in (1,2]`.  Since

`Delta_2(S)=||S||_F^2 sqrt(rho-1)/rho`,

Section 2 gives

`boxed:
 ||p_Q||_infinity
 <=2e^(1/2)D^(1/4)G^(-1/4)
   [rho/sqrt(rho-1)]^(1/4).
}`

The divergence as `rho downarrow 1` is kept explicit; a tiny second cross direction is **not** deleted.

If `rank(S)=3`, then

`boxed:
 ||p_Q||_infinity
 <=(5/3)e^(3/5)(D Delta_3(S))^(-1/5),
}`

whose universal coefficient is `3.036865`.  Since the partner identity gives `E5(B)>=D^2 Delta_3(S)^2` in exact residual rank three, sharp-HY D5 alone would give coefficient `5e/sqrt(2)=9.610578` on the same `(D Delta_3)^(-1/5)` scale.  The bankwise-shear receiver is therefore strictly sharper on this anchored exact-rank-three slice while allowing the same arbitrary self curvature.

## 4. Singular two-anchor endpoint: scalar-pivot rank-three slice

Suppose the partner's `2x2` anchor `P2` is singular but rank one, and its aggregate double-anchor third-volume is `G>0`.  Choose any genuinely nonzero physical scalar entry `p` of `P2` as a `1x1` pivot; do **not** invert `P2`.  Let `S1` be the resulting scalar cross-Schur residual.

Every physical `3x3` minor counted by the double-anchor packet becomes `p` times one physical `2x2` minor of `S1`.  Hence

`p^2 E2(S1) >= G`.

If `rank(S1)=2`, then `E2(S1)=Delta_2(S1)^2`, so

`|p|Delta_2(S1)>=sqrt(G)`.

Section 2 with `k=1,r=2,d=3` yields

`boxed:
 ||p_Q||_infinity <=3e^(2/3)G^(-1/6).
}`

On `G>Z3/24`,

`boxed:
 ||p_Q||_infinity <9.923986 Z3^(-1/6).
}`

This pays the exact cross-rank-three slice of the singular double-anchor endpoint using only a nonzero original-coordinate scalar pivot.  It does not regularize or invert the singular `2x2` anchor.

## 5. D' and D5 stress family: both named volume exits fail, the new L1 receiver succeeds

Let `m>=2`, take unit vectors `a,b in R^m`, and use disjoint original-coordinate banks of size `m+2`.  Define the physical cross block

`B_m = diag(I_2, a b^T)`

and the symmetric target matrix

`A_m=[[0,B_m],[B_m^T,0]]`.

The nonzero singular values of `B_m` are exactly `1,1,1`, so `A_m` has eigenvalues `+1,+1,+1,-1,-1,-1` (and zeros).  Thus this is an exact-target family.

Every nonzero physical `3x3` minor of `B_m` must contain both pivot rows and both pivot columns plus one residual row/column.  Therefore the third-volume marginals of each pivot row and pivot column equal **one**.  The D' gate fails maximally.  Also `rank(B_m)=3`, so `E5(B_m)=0` and D5 is unavailable.

Nevertheless Section 2 with `P=I_2`, `S=ab^T`, `D=1` gives

`||p_Q||_infinity <=3[mathcal B(a)mathcal B(b)]^(1/3)<3e^(1/3)<4.187`

for every admissible product input law.  If `|a_i|=|b_i|=1/sqrt(m)`, this is explicitly

`boxed:
 ||p_Q||_infinity
 <=3(1-1/m)^(-(m-1)/3)<4.187.
}`

So this source-valid target family defeats both named D'/D5 volume certificates while the new **integrated** Fourier mechanism remains uniformly bounded.  It is not a counterexample to the target-wide `L1_t` criterion; on the contrary it is a new positive branch.

## 6. Correction boundary and remaining work

The proof never uses law-uniform pointwise scalar quadratic decay.  It never asserts independence of rotated/grouped coordinates.  The triangular shears are kept as dependent bankwise densities and are paid by a joint projection-density cap.  No arbitrary conditional density cap is introduced.  The algebraic cross-Schur residual is not called a TRUE symmetric Schur complement.  No exact-zero hypothesis is replaced by a small pivot, and no small coefficient/cross tail is deleted on unbounded inputs.

The strongest global Fourier criterion remains unresolved: no source-valid target counterexample to universal target-wide `int |phi_Q|` was found.  The next mathematical move is therefore not a fourth unchanged volume attempt: it is to combine the exact dominant Schur direction forced by `sr(S)<4` with one transverse physical resource, so that the bankwise grouped dimension remains at least three even when the remaining Schur singular values collapse.

Execution status: `WITHOUT_VERIFIED_BRAIN`; repository transport was used, but authenticated native receiver-memory retrieval was not.
