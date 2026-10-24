SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B11, 2026-09-24T12:02:33Z.
attacking: the r14 near-coloop stability frontier; aggregate one heavy/physical direction and two diffuse rank-one source banks before paying the latest account03/B11 r56 indefinite physical-triple receiver.

# account02/B11 r15 — three-line frame-deficit aggregation and a genuine two-sheet near-coloop family

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING TARGET-LEVEL BRANCH / FULL QFORM OPEN`

The unrestricted conjecture remains OPEN / NOT PROVED / NOT DISPROVED. Continuity remains separate and is not claimed below.

## 1. First unpaid implication and new theorem

The first unpaid implication from r14 was quantitative near-coloop stability: aggregate before reciprocal physical-minor payment. The following is one clean paid chamber.

### Theorem 1 — `QFORM-NEAR-COLOOP-THREE-LINE-FRAME-DEFICIT-v1`

Let

`A=R M R^T`, `R^T R=I_3`,

have rank exactly three, with `M` real symmetric invertible and

`s=sigma_min(M)=min_j |lambda_j(M)|>0`.

Partition the ORIGINAL coordinates into four disjoint banks

`G_1 disjoint_union G_2 disjoint_union G_3 disjoint_union H`.

Assume that in each active bank the spectral frame rows are collinear:

`r_i=c_i^(a) v_a`, `i in G_a`, `||v_a||=1`,

and put

`lambda_a=sum_{i in G_a} (c_i^(a))^2>0`.

Let the residual spectral-frame operator be

`T_H=sum_{i in H} r_i r_i^T`,

and assume

`epsilon=||T_H||_op<1`.

For arbitrary independent original inputs with one-dimensional probability densities bounded by one, if `M` is indefinite then

`boxed: ||p_{X^T A X}||_(infinity,ess)
       <= 2 C_ind / [s(1-epsilon)]
       < 106.952/[s(1-epsilon)],`

where

`C_ind=4*22^(3/4)*3^(1/4)=53.4758031116...`

is the latest account03/B11 r56 localized-indefinite constant.

No moments, support bounds, log-concavity, post-rotation independence, or conditional projection-density cap is used.

### Proof

Condition only on all original coordinates in `H`. This is genuine product conditioning. It creates an arbitrary affine perturbation in the active variables but does not alter their quadratic carrier.

Define the normalized original-source linear summaries

`L_a=lambda_a^(-1/2) sum_{i in G_a} c_i^(a) X_i`.

Because the three banks are disjoint, `L_1,L_2,L_3` are genuinely independent. The sharp one-dimensional Rogozin--Ball product-projection bound gives

`||p_{L_a}||_infinity <= sqrt(2)`.

Set

`W=[sqrt(lambda_1)v_1, sqrt(lambda_2)v_2, sqrt(lambda_3)v_3]`.

Parseval for the spectral frame gives the exact identity

`W W^T = I_3-T_H`.

Hence

`W W^T >= (1-epsilon)I_3`,

so `W` is invertible and

`sigma_min(W)^2 >=1-epsilon`.

After conditioning on `H`, the quadratic part in `L=(L_1,L_2,L_3)` is

`L^T B L`, `B=W^T M W`,

plus an arbitrary affine term. Since

`B^(-1)=W^(-1) M^(-1) W^(-T)`,

`||B^(-1)||_op
 <= ||W^(-1)||_op^2 ||M^(-1)||_op
 <= 1/[s(1-epsilon)]`.

Therefore

`boxed: sigma_min(B)>=s(1-epsilon).`

Congruence also preserves inertia, so `B` is indefinite exactly when `M` is.

Now set `Y_a=sqrt(2)L_a`. The `Y_a` are independent cap-one scalars. Their quadratic carrier is `B/2`, hence

`sigma_min(B/2)>=s(1-epsilon)/2`.

Apply the completed latest partner theorem `QFORM-INDEFINITE-PHYSICAL-3X3-LOCALIZED-v1` to the three genuine independent scalar variables `Y_a`. Its affine-uniform form yields

`||p_{Q | X_H}||_(infinity,ess)
 <= C_ind/[s(1-epsilon)/2]
 =2 C_ind/[s(1-epsilon)].`

The estimate is uniform in the conditioned residual coordinates. Averaging the conditional interval bounds proves the theorem. QED.

This is an aggregate-before-inversion result: no literal physical 3x3 block needs to be well conditioned.

## 2. Zero-diagonal aggregate carrier: sign-specific improvement

If, in addition, the aggregate carrier `B` has zero physical diagonal, then after the `sqrt(2)` rescaling so does `B/2`. In either indefinite signature, r56's interlacing dichotomy is automatically in its no-majority-pivot branch. With

`sigma_min(B/2)>=s(1-epsilon)/2`,

its stronger moving-critical-value estimate gives

`boxed:
 ||p_Q||_(infinity,ess)
 < 16*6^(1/4)/[s(1-epsilon)]
 =25.0413532812.../[s(1-epsilon)].`

The point is not the constant. The third direction is being spent through the pair's moving logarithmic critical value before any physical minor of the original diffuse matrix is inverted.

## 3. Concrete near-coloop/diffuse two-sheet family

Let

`H, Y_1,...,Y_m, Z_1,...,Z_m`

be arbitrary independent cap-one variables and define

`U_m=m^(-1/2) sum_{j=1}^m Y_j`,
`V_m=m^(-1/2) sum_{j=1}^m Z_j`,

and

`boxed: Q_m=2 H U_m+2 H V_m+2 U_m V_m.`

The three aggregate variables come from disjoint original-source banks. The ambient exact-rank-three matrix is `A_m=R M_0 R^T`, where

`M_0=[[0,1,1],[1,0,1],[1,1,0]]`.

Its nonzero spectrum is

`boxed: {2,-1,-1}.`

Thus every `Q_m` is a genuine owner-target family of signature `(1,2)`.

The hub row has leverage one. Hence the pinned fully-spread theorem does not apply through its low-leverage gate. At the same time every invertible literal physical 3x3 principal block must use `H`, one `Y_i`, and one `Z_j`, and is

`C_m=[[0,m^(-1/2),m^(-1/2)],
      [m^(-1/2),0,m^(-1)],
      [m^(-1/2),m^(-1),0]].`

It has one eigenvalue `-1/m`; the other two are the roots of

`lambda^2-(1/m)lambda-2/m=0`.

Therefore

`boxed: sigma_min(C_m)=1/m.`

The latest partner r56 literal-local theorem would consequently give only `<53.476 m`, which diverges. This is a real demonstration that the global bridge must aggregate first.

Rogozin--Ball gives

`||p_{U_m}||_infinity, ||p_{V_m}||_infinity <=sqrt(2)`.

Set

`U'=sqrt(2)U_m`, `V'=sqrt(2)V_m`.

Then `H,U',V'` are independent cap-one scalars and the exact quadratic carrier becomes

`C'=[[0,1/sqrt(2),1/sqrt(2)],
     [1/sqrt(2),0,1/2],
     [1/sqrt(2),1/2,0]].`

For the physical pair `(H,U')`,

`kappa=sigma_min([[0,1/sqrt(2)],[1/sqrt(2),0]])=1/sqrt(2)`,

while

`|det C'|=1/2`.

Use the exact no-pivot r56 estimate

`||p||_infinity
 <=8*2^(1/4) (kappa |det C'|)^(-1/4)`.

This yields the dimension-free full-line inequality

`boxed:
 ||p_{Q_m}||_(infinity,ess)
 <=8*2^(5/8)
 =12.3376866033...`

for every `m` and every admissible original product law.

This is substantially stronger than paying a literal physical triple and, unlike a diagonal-only argument, it covers a genuinely cross-coupled indefinite carrier.

## 4. Rank-two logarithm retained exactly; third direction removal

Delete the third bank terms and retain only

`R_m=2 H U_m`.

Take the original variables to be centered unit uniforms. The density `g_m` of `U_m` is continuous and strictly positive at zero. Choose `delta_m,c_m>0` so that

`g_m(u)>=c_m` for `|u|<=delta_m`.

For sufficiently small `t!=0`, the product-density formula gives

`p_{R_m}(t)
 =int_{-1/2}^{1/2} g_m(t/(2h)) dh/(2|h|)
 >=c_m log(delta_m/|t|),`

so

`boxed: p_{R_m}(t) -> infinity logarithmically as t->0.`

Thus the diffuse bank does not regularize the rank-two saddle by itself.

Restore `V_m`. For fixed `V_m=v`, the pair polynomial is

`2 H U_m+2v(H+U_m)
 =2(H+v)(U_m+v)-2v^2.`

Therefore the rank-two logarithmic critical value is no longer fixed: it moves as

`boxed: tau(v)=-2v^2.`

That is exactly the latest partner r56 mechanism. The third source-disjoint bank does not make the pair density bounded first. Instead its quadratic motion gives a square-root tube law for the critical value, and averaging that law against the pair-log envelope makes the logarithm integrable. This remains valid with arbitrary cap-one original marginals because `V_m` itself has the source-valid universal density cap `sqrt(2)`.

## 5. Required pinned-source inequality on the one-sheet side

The required fixed source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` was read in full for `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Its completed ruled-level-set Theorem C states that an exact-rank-three `(2,1)` form with all three eigenvalue magnitudes at least `s` satisfies

`p_Q(t)<=pi sqrt(2)/s`

on its one-sheet sign side. Since `Q_m` has signature `(1,2)` and nonzero spectrum `{2,-1,-1}`, apply Theorem C to `-Q_m`. This gives the actual sign-specific inequality

`boxed: p_{Q_m}(t)<=pi sqrt(2),   t<=0.`

I do not transfer this X-ray/ruling estimate to `t>0`; the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction forbids that step. The aggregate r56 bound above pays the full line, in particular the opposite two-sheet side `t>0`.

This is the required completed pinned-source receiver applied at a real inequality.

## 6. Relation to r14 and r56; remaining debt

The preceding r14 theorem paid the exact no-disjoint-Pluecker-base endpoint and isolated `QFORM-NEAR-COLOOP-STABILITY-v1`. Theorem 1 above quantitatively pays one nontrivial neighborhood of that endpoint: three source-disjoint rank-one spectral banks may be arbitrarily diffuse internally, provided their frame mass misses at most an operator fraction `epsilon<1`.

The newest completed designated partner account03/B11 r56 is used essentially, not just cited: after source-preserving bank scalarization, its localized physical-triple theorem is applied to the induced independent scalar triple. The explicit family in Section 3 also uses r56's sharper exact moving-critical-value branch to replace an `O(m)` literal-local estimate by `12.338` uniformly in `m`.

The first unpaid implication is now

`QFORM-NEAR-COLOOP-INTERNAL-RANK2-ROUTING-v2`:

> In the exact-rank-three near-coloop survivor, either force three disjoint rank-one source banks whose aggregate spectral frame satisfies `I-T_H >= c I` for a universal `c>0`, or exploit a genuine internal two-dimensional bank wedge before conditioning to route to an already-paid cross-volume / grouped-square / Schur mechanism. The argument must remain product-source valid and must not condition one coordinate of a same-bank rotated pair as though its density cap survived.

Arbitrary additional nonseparable spectrum remains a separate bridge beyond exact rank three. Full-target continuity also remains open.
