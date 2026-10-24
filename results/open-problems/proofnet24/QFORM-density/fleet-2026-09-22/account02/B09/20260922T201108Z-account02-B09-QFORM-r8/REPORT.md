SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-22T20:11:08Z.
attacking: aggregate bilinear packet anti-concentration across a product-preserving partition and close an O(interval length) estimate without reciprocal tiny-minor or square-root decoupling loss.

# account02/B09 QFORM r8 — curved three-bank scalar compression

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260922T201108Z-account02-B09-QFORM-r8`  
Control at start: `yspennstate/math-research-brain@8d88b8a0f0c629b892444e56cf0657fc9419bc25`; OWNER CONTROL revision `2026-09-22.15`.  
Outcome: **ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED / FULL_TARGET_OPEN**.  
Execution status: **WITHOUT_VERIFIED_BRAIN**.

The full conjecture is not proved. This report closes a three-scalar curved compression branch and identifies an exact obstruction to extending the partner's rank-one triangle theorem using cross strengths alone.

## 1. Source-pinned inputs and first unpaid implication

The latest completed named-partner result actually used is account03/B09 `QFORM-THREE-BANK-RANKONE-TRIANGLE-v1`, canonical source

`yspennstate/math-open-problems@5e92c0aa0681b3d24630451076ab511f92dc718c:proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260922T194535Z-account03-B09-QFORM-r16/REPORT.md`.

For three disjoint original-coordinate banks with independent projections `U=<u,X_I>`, `V=<v,X_J>`, `W=<w,X_K>`, zero scalar self terms, rank-one cross links, arbitrary aligned affine terms and independent outside noise, it proves

`||p_F||_infinity <= 2(3+log 8)(s_IJ s_IK s_JK)^(-1/3)`.      (1.1)

The second completed dependency is `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`, source

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For independent cap-one inputs, every invertible symmetric two-dimensional quadratic form `R` with arbitrary original-coordinate affine term obeys

`sup_t E |R-t|^(-1/2) <= 128 |det Lambda|^(-1/4)`.             (1.2)

The third dependency is `QFORM-PAIR-LOG-SMALLBALL-SMOOTHING-v1`, source

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

For an exact-rank-three physical block with spectral scale `s`, an invertible indefinite physical pair `B` with `D=|det B|` and `kappa=sigma_min(B)` yields

`||p_Q||_infinity <= 8 sqrt(5) (D*kappa*s)^(-1/4)`.           (1.3)

All three inputs preserve arbitrary cap-one laws; none asserts independence after a spectral rotation. The live corrections ruling out arbitrary-joint coarea, positive conditional projection-density moments, uniform pointwise Fresnel decay, a universal fixed good minor, and one-heavy-row/same-square absorption are enforced.

**First unpaid implication after this report:**

`QFORM-GAPPED-SCALAR-COMPRESSION-OR-GENUINE-BANK-CURVATURE-v1` — from the bare hypothesis `s_3(A)>=1`, after product-preserving aggregation into disjoint original-coordinate banks, force either (i) a completed two-cross wedge/ridge certificate, (ii) the named partner's rank-one triangle certificate, (iii) a three-bank scalar compression with a universal spectral gap as paid below, or else isolate genuine within-bank curvature orthogonal to those active projections and pay it by a translation-uniform half-Riesz/ridge estimate. Section 5 shows why cross strengths alone cannot replace the scalar-compression spectral gap.

## 2. Three independent scalars: arbitrary curved 3x3 compression

### Theorem 2.1 — `QFORM-THREE-SCALAR-CURVED-COMPRESSION-v1`

Let `X=(X1,X2,X3)` have independent real densities bounded by one. Let `H` be a real symmetric invertible `3x3` matrix with

`sigma_min(H) >= s > 0`.

Allow an arbitrary affine term `ell^T X+c`. Then

`boxed: ||p_(X^T H X + ell^T X+c)||_infinity
        <= 128*2^(1/4)/s < 153/s.`                                  (2.1)

The same bound survives conditioning on arbitrary disjoint outside original coordinates whenever the selected physical `3x3` block is `H`: outside quadratic terms become additive shifts and outside cross terms become arbitrary affine terms in the selected three coordinates.

### Proof

Write `H=(h_ij)` and let `d=max_i |h_ii|`.

#### Case A: a scalar pivot has size at least `s/2`

After relabeling let `a=h_11` with `|a|>=s/2`, and write

`H = [[a, r^T],[r,C]]`.

Completing the square in the original coordinate `X1` gives

`X^T H X + ell^T X+c
 = a (X1+m(X2,X3))^2 + R(X2,X3)`,                            (2.2)

where `R` is a quadratic-affine form in the two still-independent original coordinates and its quadratic matrix is the Schur complement

`S=C-r r^T/a`.

Because `H` is invertible, `S` is invertible and

`det S = det H/a`.                                             (2.3)

For fixed `(X2,X3)`, the shifted variable `X1+m` has a density bounded by one. The elementary two-branch change of variables for a square gives, for almost every `t`,

`p_(a(X1+m)^2 | X2,X3)(t-R)
 <= |a|^(-1/2) |t-R|^(-1/2)`.                                (2.4)

Average (2.4), then apply (1.2) to `R`:

`||p_Q||_infinity
 <= |a|^(-1/2) * 128 |det S|^(-1/4)
 = 128 (|a| |det H|)^(-1/4).                                 (2.5)

Since every singular value of `H` is at least `s`, `|det H|>=s^3`; together with `|a|>=s/2`,

`||p_Q||_infinity <=128*2^(1/4)/s`.                           (2.6)

No conditional density supremum of a spectral projection is introduced: the only conditioning is on original independent coordinates.

#### Case B: every scalar pivot is smaller than `s/2`

Assume `|h_ii|<s/2` for all `i`. Since `sigma_min(H)>=s`, every physical row satisfies

`||H e_i||_2 >= s`.

Hence for each `i`,

`sum_(j!=i) h_ij^2 >= s^2-h_ii^2 > 3s^2/4`.                  (2.7)

Choose an off-diagonal entry `b=h_ij` from one row with

`|b| >= sqrt(3/8) s`.                                         (2.8)

Let the corresponding physical pair be

`B=[[a,b],[b,c]]`, with `|a|,|c|<s/2`.

It is indefinite because `b^2>3s^2/8>|ac|`. Moreover

`D=|det B|=b^2-ac >= b^2-|ac| > s^2/8`.                       (2.9)

Writing the two eigenvalues of `B` as `m+-r`, where

`m=(a+c)/2`, `r=sqrt(b^2+((a-c)/2)^2)`,

the smaller absolute eigenvalue is `kappa=r-|m|`. Therefore

`kappa >= |b|-|m|
 > (sqrt(3/8)-1/2)s
 = ((sqrt(6)-2)/4)s`.                                        (2.10)

Apply the pair-log theorem (1.3) to this physical pair inside the exact-rank-three block `H`:

`||p_Q||_infinity
 <= 8 sqrt(5) [D*kappa*s]^(-1/4)
 <= 8 sqrt(5) [32/(sqrt(6)-2)]^(1/4) / s
 < 52/s.                                                       (2.11)

This is strictly stronger than (2.1). Cases A and B prove the theorem. `QED`

### Direct interval form

For every interval `L`, Theorem 2.1 gives

`P{X^T H X+ell^T X+c in L} <= 153 |L|/s`.                    (2.12)

Thus this branch reaches the assigned `O(interval length)` endpoint directly; no square-root conversion or resampling occurs.

## 3. Product-preserving three-bank corollary with scalar self-curvature

### Corollary 3.1 — `QFORM-THREE-BANK-CURVED-SCALAR-COMPRESSION-v1`

Let `I,J,K,R` be disjoint original-coordinate banks. Choose nonzero vectors `u in R^I`, `v in R^J`, `w in R^K`, and set

`U=<u,X_I>`, `V=<v,X_J>`, `W=<w,X_K>`.

These three variables are genuinely independent. Suppose, after conditioning only on `X_R`, the entire dependence on the active banks is

`z^T H z + affine(z) + outside_shift`, `z=(U,V,W)`,             (3.1)

where `H` is an arbitrary symmetric `3x3` matrix; thus scalar self-curvatures `h_11 U^2`, `h_22 V^2`, `h_33 W^2` are allowed. Equivalently, within each active bank the quadratic/cross terms are aligned with the selected scalar projection; arbitrary curvature orthogonal to these projections is not asserted to be covered.

Put

`D0=diag(||u||_2,||v||_2,||w||_2)`, `G=D0 H D0`.               (3.2)

If

`sigma_min(G) >= tau >0`,                                     (3.3)

then

`boxed: ||p_Q||_infinity <= 256*2^(1/4)/tau <305/tau`.         (3.4)

### Proof

By the one-dimensional product-marginal theorem used in the named partner's proof, the normalized projections

`Y1=U/||u||`, `Y2=V/||v||`, `Y3=W/||w||`

have density caps at most `sqrt(2)` and remain independent. Therefore `Z=sqrt(2)Y` has three independent cap-one coordinates. In these variables the quadratic matrix is `G/2`, whose smallest singular value is at least `tau/2`. Apply Theorem 2.1 conditionally on the outside coordinates and then average:

`||p_Q||_infinity
 <= [128*2^(1/4)]/(tau/2)
 =256*2^(1/4)/tau <305/tau`.                                  (3.5)

Again this is a direct linear interval estimate. `QED`

This is a genuine extension of the three-bank scalar geometry from zero self terms to arbitrary **scalar** self-curvature, provided the aggregate `3x3` compression stays nondegenerate. It is not a theorem for arbitrary within-bank operators.

## 4. Named-partner result applied to an actual sharpened inequality

The partner theorem (1.1) is much sharper on the zero-self subcase of Corollary 3.1. If `diag G=0` and `sigma_min(G)>=tau`, then

`det G = 2 G12 G13 G23`                                       (4.1)

and the spectral gap gives `|det G|>=tau^3`. Hence

`|G12 G13 G23| >= tau^3/2`.                                   (4.2)

The partner's aggregate strengths are exactly

`s_IJ=|G12|`, `s_IK=|G13|`, `s_JK=|G23|`.

Substituting (4.2) into account03/B09 r16 gives the actual bound

`boxed: ||p_Q||_infinity
 <= 2^(4/3)(3+log 8)/tau
 =12.7993906401.../tau.`                                      (4.3)

Thus the new theorem handles scalar-curved compressions, while the named partner remains the preferred certificate on the zero-self face.

## 5. Exact falsifier: cross-cycle strength does not survive arbitrary self-curvature

A tempting strengthening of the partner theorem would retain only the three nonzero cross strengths and allow arbitrary scalar self terms, without requiring a spectral gap for the full aggregate compression. That statement is false even for three physical coordinates.

Take independent

`U,V,W ~ Uniform[-1/2,1/2]`

and set

`Q=(U+V+W)^2
  = U^2+V^2+W^2+2UV+2UW+2VW`.                                (5.1)

All three cross-cycle strengths equal one. But the coefficient matrix is the all-ones matrix, with spectrum `{3,0,0}`. Let `S=U+V+W`. The centered Irwin--Hall density satisfies exactly

`p_S(0)=3/4`.                                                   (5.2)

For `t>0`, symmetry gives

`p_Q(t)=[p_S(sqrt(t))+p_S(-sqrt(t))]/(2sqrt(t))
       =p_S(sqrt(t))/sqrt(t)`.                                (5.3)

Therefore

`p_Q(t) ~ (3/4)t^(-1/2)` as `t downarrow 0`,                    (5.4)

so the density is unbounded.

This is **not** a counterexample to the full QFORM conjecture: the matrix has only one nonzero eigenvalue, not three eigenvalues of magnitude at least one. It is a source-valid counterexample to the intermediate claim that a strong three-edge bilinear cycle by itself can absorb arbitrary scalar self-curvature. The aggregate spectral gap in Corollary 3.1, or some genuinely independent curvature payment, is essential.

Correction ID: `QFORM-CROSS-CYCLE-ARBITRARY-SELF-CURVATURE-FALSE-v1`.

## 6. Relation to the full target

This run pays a previously exposed part of `QFORM-ONE-STRONG-CROSS-CURVED-BANK-v1`: whenever three disjoint product banks reduce to a full-rank scalar quadratic compression at universal aggregate scale, arbitrary scalar self-curvature is harmless and the output has a direct `O(|L|)` bound. The result aggregates bank projections before reciprocal physical-minor payment, so diffuse examples with entries tending to zero remain eligible.

It does **not** prove that `s_3(A)>=1` forces such a compression, and it does not control arbitrary within-bank curvature orthogonal to the three chosen projections. The exact falsifier in Section 5 blocks any attempt to route the latter merely by preserving three cross edges. The next step must either extract a gapped scalar compression/wedge/ridge at universal scale or keep the residual curved-bank operator in the smoothing argument itself.

No claim of continuity is made. The unrestricted conjecture remains OPEN.

## 7. Numerical checks and provenance

The exact proof above is analytic. A deterministic checker in this run folder only evaluates the displayed universal constants and the elementary falsifier identities; it is not proof evidence. The expected values are:

`128*2^(1/4) = 152.2185107203483`,

`8*sqrt(5)*(32/(sqrt(6)-2))^(1/4) = 51.96160262281568`,

`2^(4/3)*(3+log 8) = 12.799390640145784`,

`256*2^(1/4) = 304.4370214406966`.

No Monte Carlo, histogram, moment assumption, support bound, post-rotation independence, arbitrary-joint coarea theorem, or conditional spectral-density supremum is used.
