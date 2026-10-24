SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B07, 2026-09-23T13:33:58Z.
attacking: the partner's residual E3 branch — spend diffuse third-volume immediately, close every bounded-support physical core, then downshift the genuinely support-diffuse double-anchor packet without selecting one minor.

# account02/B07 — residual E3 diffuse/core/downshift compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T133358Z-account02-B07-qform-r11auto`  
Role: Coordinate minor selection / complementary constructions and source-valid counterexamples  
Owner control: revision `2026-09-22.15`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
Status: **ESSENTIAL STEP APPLIED / RESIDUAL-E3 DIFFUSE BRANCH PAID / BOUNDED-SUPPORT CORE PAID / DOUBLE-ANCHOR DOWNSHIFT PROVED / FULL QFORM OPEN**.

The unrestricted theorem is not claimed. All coordinates below are ORIGINAL physical coordinates. No moment, support, log-concavity, Gaussianity, iid, diagonal-basis or post-rotation independence hypothesis is introduced. Same-bank quadratic curvature, outside couplings, affine terms, signs and additional spectrum are retained in every paid branch.

## 1. First unpaid implication and source-valid incoming state

The latest completed designated partner actually used is account03/B07 r30, available at

`yspennstate/math-open-problems@71c369d883ef5211a624f1e943e53dcfbcc3dcdd`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T130749Z-account03-B07-qform-r30/REPORT.md`.

Its rank-four compiler leaves, on one genuine unpaid branch, a far physical cross block `D` satisfying

`Z3:=E3(D) > (8/3) a^6`,                                           (1.1)

where `a=s3(M)` is the natural scale of the preceding physical cross block. In the same live N3 state the partner records

`a > a0 := 1.9279762269984055e-7`                                 (1.2)

and the physical off-diagonal entry cap

`|A_uv| <= u0 := h/8`,  `h=(2sqrt(2)-1)/1572864`.                (1.3)

All other r30 alternatives are already routed separately: a paid physical pair or a six-disjoint-bank certificate. Thus the first obligation attacked here is exactly the partner's `QFORM-R4-RESIDUAL-E3-OR-SIXBANK-CURVATURE-RECEIVER-v1`, on its residual-E3 side.

The required pinned newest-Claude source was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

The completed result used below is its D' volume theorem: if a physical third-volume packet of mass `Z` has all inclusion marginals on one chosen side at most `h<3/4`, then

`||p_Q||_infinity
 <= 6 sqrt(e) (2h)^(-1/2)(3-4h)^(-1) Z^(-1/6)`.                 (1.4)

At `h=2/3`, this is `9 sqrt(3e) Z^(-1/6)`. The proof uses original-coordinate decoupling, so arbitrary same-bank curvature and affine terms are allowed.

For bounded physical cores I use the completed projected-gradient finite-dimensional receiver

`yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`,

`proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`:
if an `m`-coordinate physical principal block has three actual eigenvalues of modulus at least `sigma`, then, uniformly in arbitrary affine terms,

`||p_Q||_infinity <= 2 sqrt(6 pi m)/sigma`.                       (1.5)

Conditioning outside the physical core is therefore legitimate.

## 2. The residual-E3 diffuse branch is paid immediately

Normalize all squared physical `3x3` minors of `D` to a probability law

`w(S,T)=det D[S,T]^2/Z3`,                                         (2.1)

and write

`alpha_i=P_w(i in S)`,  `beta_j=P_w(j in T)`,                    (2.2)

so `sum alpha_i=sum beta_j=3`.

If

`max_i alpha_i <=2/3`                                             (2.3)

then (1.4) applies directly. If instead

`max_j beta_j <=2/3`,                                             (2.4)

apply the same theorem to `D^T`. Hence either diffuse orientation gives

`||p_Q||_infinity
 <=9 sqrt(3e) Z3^(-1/6)
 <9 sqrt(3e)(3/8)^(1/6) a^(-1)
 =21.8250671726... a^(-1)`.                                      (2.5)

Using the actual partner floor (1.2), this is `<1.133e8`. This is a real application of the pinned completed theorem to the partner's inequality (1.1), not merely a citation. It yields a continuous density on this branch.

Thus every still-unpaid residual-E3 state has physical coordinates `i,j` with

`alpha_i>2/3`,  `beta_j>2/3`.                                    (2.6)

## 3. Concentration forces an entire doubly anchored packet

Under the determinant-volume law (2.1), the union bound gives

`P_w(i in S and j in T) >= alpha_i+beta_j-1 >1/3`.               (3.1)

Therefore the complete doubly anchored third-volume packet

`G := G3^(i,j)(D)
   = sum_(|R|=|T|=2)
       det D[{i} union R,{j} union T]^2`                          (3.2)

satisfies

`boxed: G > Z3/3 > (8/9)a^6.`                                    (3.3)

No individual minor has been selected. The entire determinant weight through two physical anchors is retained.

## 4. Bounded residual support gives an actual physical spectral core

Normalize the summands in (3.2) to a probability law on the residual row pairs `R` and residual column pairs `T`. Let their inclusion marginals be `rho_k,sigma_l`; each family sums to two.

Take any residual physical supports `R0,C0`, with

`p=|R0|`, `q=|C0|`,

and tail

`delta = sum_(k notin R0) rho_k + sum_(l notin C0) sigma_l <1`.   (4.1)

The union bound gives

`P(R subset R0, T subset C0) >=1-delta`.                          (4.2)

Hence for the actual physical cross block

`C=D[{i} union R0,{j} union C0]`

we have the aggregate lower bound

`E3(C) >= (1-delta)G > (8/9)(1-delta)a^6`.                       (4.3)

Let

`r0=min(p+1,q+1)`, `L=||C||_op`.                                 (4.4)

Cauchy--Binet and singular-value ordering give

`E3(C)=e3(s_1(C)^2,...)
 <= binom(r0,3) L^4 s3(C)^2`,                                   (4.5)

so

`s3(C) > [2sqrt(2)/3] sqrt(1-delta) a^3
          / [sqrt(binom(r0,3)) L^2].`                            (4.6)

Let `H={i} union R0 union {j} union C0`. Since `C` is a rectangular compression of the symmetric physical principal block `A[H,H]`, singular-value monotonicity under compression gives

`s3(A[H,H]) >= s3(C)`.                                           (4.7)

Thus (1.5), after conditioning only on ORIGINAL coordinates outside `H`, proves

`boxed:
 ||p_Q||_infinity
 < (3/sqrt(2)) sqrt(6 pi (p+q+2)) sqrt(binom(r0,3)) L^2
   / [sqrt(1-delta) a^3].
}`                                                               (4.8)

This is the bounded-dimensional spectral subproblem integrated directly into determinant-weighted coordinate extraction. It does not infer one good minor; a whole anchored packet is localized first.

In the live N3 state, every entry of this cross block is off diagonal and obeys (1.3), hence

`L^2 <= (p+1)(q+1)u0^2`.                                        (4.9)

Consequently any fixed-cardinality residual supports with `delta<=1/2` are universally paid. For example, with `p=q=8`, (1.2)-(1.3) give the explicit, deliberately unoptimized cap

`||p_Q||_infinity < 1.209e11`.                                   (4.10)

The point is finiteness independent of ambient dimension, not optimization of this large constant.

## 5. Genuine support diffusion downshifts to lower compound currencies

It remains to describe the state when neither D' nor bounded-support core extraction fires. Write the actual physical block around the anchors as

`D = [[b,r^T],[c,E]].`                                           (5.1)

For every residual row pair `R` and column pair `T`, Laplace expansion gives

`det D[{i} union R,{j} union T]
 = b det E[R,T] - Psi_(R,T)`,                                   (5.2)

where

`Psi_(R,T)=r_T^T adj(E[R,T]) c_R`.                              (5.3)

The entire cofactor array is the matrix, up to orientation signs, of the exterior-map composition

`K=(c wedge .) o E o i_r : wedge^2 -> wedge^2`.                 (5.4)

The operator norms of wedge multiplication by `c` and contraction by `r` are `||c||` and `||r||`. Therefore

`sum_(R,T) Psi_(R,T)^2
 =||K||_HS^2
 <=||c||^2 ||r||^2 ||E||_F^2`.                                 (5.5)

Taking the Euclidean norm in the entire anchored-minor array gives

`boxed:
 sqrt(G)
 <= |b| sqrt(E2(E)) + ||r|| ||c|| ||E||_F.
}`                                                               (5.6)

Using (3.3), at least one of

`boxed: |b| sqrt(E2(E)) > (sqrt(2)/3)a^3,`                       (5.7)

`boxed: ||r|| ||c|| ||E||_F > (sqrt(2)/3)a^3`                    (5.8)

must hold.

This is `QFORM-RESIDUAL-E3-DIFFUSE-CORE-OR-DOUBLEANCHOR-DOWNSHIFT-v1`. It converts the partner's residual third-volume packet into either a paid D' branch, a paid bounded physical core, or one of two explicit lower-compound physical resources. No determinant is inverted and no single minor is selected.

## 6. Exact target-class regression: the star-star-F branch is genuinely necessary

The second term in (5.6) cannot be removed in favor of the first. For even `N`, let `c,u in R^N` be the normalized constant and alternating vectors, and let `r,v in R^N` be copies on the column side. Put

`E=u v^T`,

`D_N=[[0,r^T],[c,E]]`,                                           (6.1)

and form the symmetric bipartite target matrix

`A_N=[[0,D_N],[D_N^T,0]]`.                                      (6.2)

In the orthonormal modal row basis `(anchor,c,u)` and column basis `(anchor,r,v)`, `D_N` is exactly

`[[0,1,0],[1,0,0],[0,0,1]]`.                                    (6.3)

Hence its three nonzero singular values are `1,1,1`, and `A_N` has spectrum containing three `+1` and three `-1`. This is a genuine target-class matrix.

Every nonzero third minor must contain the physical anchor row and anchor column. Consequently

`E3(D_N)=G3^(anchor,anchor)(D_N)=1`,                              (6.4)

while the anchor inclusion marginals equal one. The residual pair inclusion marginals are exactly `2/N`, so no fixed number of physical residual coordinates captures a fixed fraction of the packet as `N->infinity`.

Moreover

`b=0`, `E2(E)=0`,

but

`||r|| ||c|| ||E||_F=1`.                                        (6.5)

Thus (5.6) is sharp on this family: all anchored third-volume survives in the star-star-Frobenius term, while the edge-times-E2 term vanishes identically. Also every fixed-cardinality physical principal core `H`, `|H|<=M`, satisfies

`s3(A_N[H,H]) <= ||A_N[H,H]||_op <= M/sqrt(N) ->0`.              (6.6)

So neither a bounded-core theorem nor an edge-E2-only theorem can close the concentrated branch universally.

This is not a QFORM counterexample. It is exactly paid by the pinned source's completed mixed-hub theorem H. Taking the two physical anchors as hubs, the far quadratic block has rank two with eigenvalues `+1,-1`; the four-dimensional hub/rank feature Gram is `I_4`, and every physical feature leverage is `2/N<=1/2`. The theorem gives

`|phi_Q(t)| <=16 pi^3 |t|^-3`,                                  (6.7)

hence

`boxed: ||p_Q||_infinity <=3*2^(1/3)<3.780.`                     (6.8)

This applies another completed pinned result to the exact obstruction and confirms that the obstruction is to the structural shortcut, not to the target theorem.

## 7. What changed and the next unpaid implication

The partner's residual-E3 branch is no longer an undifferentiated third-volume debt. It is now exhausted into:

1. a D' diffuse-volume branch, paid by (2.5);
2. any bounded residual-support branch, paid by the actual physical-core estimate (4.8);
3. a genuinely support-diffuse double-anchor branch carrying either (5.7) or (5.8).

The sharp regression (6.1) shows that alternative (5.8) is essential and can coexist with complete failure of bounded-cardinality core extraction.

The first unpaid B07 implication is therefore

`QFORM-R4-ANCHORED-E3-SUPPORTDIFFUSE-LOWERCOMPOUND-RECEIVER-v1`:

in the support-diffuse double-anchor state, spend either the edge-times-E2 currency (5.7) or the star-star-Frobenius currency (5.8) while retaining arbitrary same-bank quadratic curvature and every additional eigenvalue. The exact low-rank mixed-hub regression is paid, so the remaining difficulty is the same resource with genuinely arbitrary far curvature. A valid continuation may use a curvature-safe mixed-hub/decoupled determinant receiver or force another physical pair before completion; it may not assume the E2 bank survives a Schur complement, and it may not replace aggregate determinant weight by a reciprocal single minor.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains separate and open. The D' and finite-core exits above give continuous densities at their stated scopes; the report makes no continuity claim for the still-unpaid lower-compound state.

## 8. Checks and provenance

`CHECKS.py` / `CHECKS.txt` in this immutable run directory verify on 300 deterministic random blocks that the cofactor Hilbert--Schmidt and bordered inequalities hold numerically, verify the D' constant and partner scale, and check the exact regression family at `N=8,16`. The output ends `STATUS=PASS`. These checks are regression evidence only; the proofs are Sections 2--6.

Fresh pre-publication owner control remained revision `2026-09-22.15`, QFORM-only, with no B07 pause. Repository retrieval is not native learned-memory ingestion; this run remains `WITHOUT_VERIFIED_BRAIN`.
