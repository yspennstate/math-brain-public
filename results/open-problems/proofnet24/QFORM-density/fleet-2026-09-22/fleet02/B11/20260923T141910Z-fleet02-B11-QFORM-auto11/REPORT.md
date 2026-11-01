SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B11, 2026-09-23T14:19:10Z.
attacking: the approximate-ray clustered near-zero-pivot branch, using sign-specific null rulings and aggregate-before-inversion to recover the third direction without post-rotation independence.

# fleet02/B11 — weighted four-ray compiler and quantitative null-ruling defect

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** indefinite signatures; complementary constructions/source-valid counterexamples  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREMS / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture remains OPEN / NOT PROVED / NOT DISPROVED. Continuity is separate from the essential density bounds below.

## 1. First unpaid implication and source boundary

The first unpaid B11 implication is now

`QFORM-NULL-RULING-TO-PRODUCT-CUT-v1`:

> In the exact-rank-three two-plane indefinite survivor, use quantitative original-row proximity to the two null rulings on each spectral plane to force either two disjoint original-coordinate aggregate banks with target-scale three-dimensional volume, or an already-paid physical-pivot/pair-area/ridge/diffuse exit. The conversion must preserve source-coordinate product independence. A small matrix coefficient error is not treated as a small random quadratic perturbation under unbounded inputs.

Fresh owner control kept the full QFORM target open. I consumed the live corrections forbidding pointwise scalar phase decay, arbitrary-joint rank-three coarea, post-rotation independence, X-ray-only control of the two-sheet side, local-minor-only reductions, and near-zero-as-exact-zero perturbation.

The completed source results actually used are:

1. `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `COUNTEREXAMPLE_SEARCH.md`, Theorem C: for an exact rank-three `(+, +, -)` form with eigenvalue magnitudes at least one, the one-sheet side satisfies `p_Q(s)<=pi sqrt(2)` for `s>=0`. No such conclusion is inferred for `s<0`.
2. `math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, rank-three Schur consequence: for exact rank three, a physical row with leverage `c_i`, nonzero pivot `a=A_ii`, and spectral matrix `M` gives
   `||p_Q||_infinity <=128 [c_i |a| |det M|]^(-1/4)`.
3. Designated partner fleet03/B11 r32, `20260923T131406Z-fleet03-B11-QFORM-r32`: its equal-weight four-ray theorem and, crucially, its correction that vanishing rowwise pivot certificates do not force rowwise or bank-L2 proximity to the exact split.
4. The disjoint-volume compiler used by that partner, fleet04/B11 r5 at `math-open-problems@50b07997bec888ff7cc6820cd42be8e34d0ffc48`: for exact rank three `A=RMR^T`, two disjoint physical triples with squared spectral volumes `v_K,v_L`, and `s=min |lambda(M)|`,
   `||p_Q||_infinity <= (3/s)(v_K v_L)^(-1/6)`.

All uses below stay in original independent coordinates or in normalized sums over disjoint original-coordinate groups.

## 2. Weighted four-ray Parseval geometry

Fix `0<rho<1` and define four spectral rays

`s_+=(1,+sqrt(rho),0)`, `s_-=(1,-sqrt(rho),0)`,
`t_+=(0,sqrt(1-rho),+1)`, `t_-=(0,sqrt(1-rho),-1)`.

Put arbitrary original physical rows on these rays:

`r_i=a_i s_+` for `i in S_+`,
`r_i=a_i s_-` for `i in S_-`,
`r_j=b_j t_+` for `j in T_+`,
`r_j=b_j t_-` for `j in T_-`,

where amplitudes may have arbitrary signs and multiplicities but

`sum_(S_+) a_i^2=sum_(S_-) a_i^2=sum_(T_+) b_j^2=sum_(T_-) b_j^2=1/2`.       (2.1)

The sign cancellations and (2.1) give exactly

`R^T R=I_3`.                                                               (2.2)

Thus for every invertible symmetric `3 x 3` matrix `M`, `A=RMR^T` has exactly the three nonzero eigenvalues of `M`.

The relevant base triple determinants are

`det(s_+,s_-,t_+)^2=det(s_+,s_-,t_-)^2=4 rho`,                (2.3)

`det(s_+,t_+,t_-)^2=det(s_-,t_+,t_-)^2=4(1-rho)`.             (2.4)

These identities expose why the larger of `rho` and `1-rho` determines which pair of rays should be split.

## 3. Main structural theorem: diffuse-side arbitrary-weight compiler

### Theorem 3.1 — `QFORM-WEIGHTED-FOUR-RAY-DIFFUSE-SIDE-v1`

Let the frame satisfy (2.1)-(2.2), let `M` be any invertible symmetric matrix, and set

`s=min_k |lambda_k(M)|>0`.

If either

- `rho>=1/2` and every squared amplitude on both `S_+` and `S_-` is at most `1/4`, or
- `rho<=1/2` and every squared amplitude on both `T_+` and `T_-` is at most `1/4`,

then for arbitrary independent original inputs with density caps at most one,

`boxed: ||p_(X^T R M R^T X)||_infinity <=24/s.`                       (3.1)

No condition is imposed on the amplitudes of the two unsplit rays, on physical diagonal entries, or on the signature of `M`.

### Proof when `rho>=1/2`

An elementary partition lemma is enough. If nonnegative weights have total `1/2` and each is at most `1/4`, order them arbitrarily and accumulate until the running total first reaches `1/8`. The selected mass is in `[1/8,3/8]`, so its complement is also at least `1/8`. Hence partition each of `S_+` and `S_-` into two disjoint groups,

`S_+^1 sqcup S_+^2=S_+`, `S_-^1 sqcup S_-^2=S_-`,

whose squared-amplitude masses `alpha_1,alpha_2,beta_1,beta_2` all satisfy

`1/8 <= alpha_l,beta_l <=3/8`.                                      (3.2)

Keep `T_+` and `T_-` as two further groups. For any one of these six groups `g`, with coefficient amplitudes `c_i` and squared mass `sigma_g^2=sum_(i in g)c_i^2`, define the normalized source sum

`Y_g=sigma_g^(-1) sum_(i in g)c_i X_i`.                              (3.3)

The six `Y_g` are mutually independent because their source-coordinate sets are disjoint. Their coefficient vectors have Euclidean norm one, so the scalar Rogozin-Ball projection bound gives

`||p_(Y_g)||_infinity <=sqrt(2)`.                                    (3.4)

Set `Z_g=sqrt(2)Y_g`. Then the six `Z_g` remain independent and have density cap at most one.

Let `R_0` be the six-row matrix whose row corresponding to group `g` is `sigma_g` times that group's base ray. Since the groups partition the four original rays without changing their total squared masses,

`R_0^T R_0=I_3`.                                                      (3.5)

Moreover

`R^T X=R_0^T Y=(1/sqrt(2))R_0^T Z`,                                  (3.6)

hence exactly

`Q=Z^T R_0 (M/2) R_0^T Z`.                                           (3.7)

No approximation and no rotation of the independent variables has occurred.

Choose the two disjoint aggregate triples

`K={S_+^1,S_-^1,T_+}`, `L={S_+^2,S_-^2,T_-}`.                        (3.8)

The full `T_+` and `T_-` masses are each `1/2`. By (2.3) and (3.2),

`v_K=4rho alpha_1 beta_1(1/2)=2rho alpha_1 beta_1 >=1/64`,             (3.9)

and similarly `v_L>=1/64`. The effective spectral matrix in (3.7) is `M/2`, whose minimum eigenvalue magnitude is `s/2`. Applying the completed disjoint-volume compiler therefore gives

`||p_Q||_infinity
 <= 3/(s/2) [(1/64)^2]^(-1/6)
 =6*4/s
 =24/s`.                                                             (3.10)

### Proof when `rho<=1/2`

Split `T_+` and `T_-` into two groups each satisfying (3.2), keep `S_+` and `S_-` whole, and use

`K={S_+,T_+^1,T_-^1}`, `L={S_-,T_+^2,T_-^2}`.                        (3.11)

By (2.4),

`v_K=4(1-rho)(1/2)alpha_1 beta_1 >=1/64`,                             (3.12)

and similarly for `L`; the same argument gives (3.10). QED.

### Relation to the designated partner

Fleet03/B11 r32 proved the equal-weight four-ray endpoint and obtained the sharper constant

`6*2^(5/3)=19.0488126...`                                             (3.13)

for `s=1`. That completed partner result applies directly when all four ray masses are spread equally. Theorem 3.1 extends the same product-preserving mechanism to completely arbitrary weights and multiplicities. It also shows precisely where a new difficulty can remain: only a heavy row on the pair of rays that must be split.

## 4. A complete genuinely rotated target family

Take

`M_*=[[1,0,0],[0,0,1],[0,1,0]]`.                                    (4.1)

Then

`spec(M_*)={1,1,-1}`, `det M_*=-1`,                                  (4.2)

so `A=R M_* R^T` is a genuine target-scope signature `(+, +, -)` for every weighted frame above; replacing `M_*` by `-M_*` gives `(+, -, -)`.

### Theorem 4.1 — `QFORM-WEIGHTED-FOUR-RAY-TARGET-v1`

For every weighted frame satisfying (2.1), every number of source coordinates, and arbitrary independent cap-one input laws,

`boxed: ||p_(X^T R M_* R^T X)||_infinity <232.`                       (4.3)

The same bound holds for `-M_*`.

### Proof

If the diffuse-side condition of Theorem 3.1 holds, (3.1) gives the much smaller bound `24`.

Suppose first `rho>=1/2` and the diffuse-side condition fails. Then some `S_+` or `S_-` row has squared amplitude

`w=a_i^2>1/4`.                                                        (4.4)

For such a row,

`c_i=||r_i||^2=w(1+rho)`, `A_ii=r_i^T M_* r_i=w`.                     (4.5)

Thus

`c_i |A_ii| |det M_*|=w^2(1+rho) > (1/16)(3/2)=3/32`.                 (4.6)

Apply the completed rank-three scalar-pivot half-Riesz theorem:

`||p_Q||_infinity
 <128(32/3)^(1/4)
 =231.322112924...`.                                                   (4.7)

Now suppose `rho<=1/2` and a split T ray is heavy, with `w=b_j^2>1/4`. Then

`c_j=w(2-rho)`,
`|A_jj|=2sqrt(1-rho)w`.                                               (4.8)

Hence

`c_j|A_jj|
 =2(2-rho)sqrt(1-rho)w^2
 >3/(16sqrt(2))`,                                                      (4.9)

and the same theorem gives

`||p_Q||_infinity
 <128(16sqrt(2)/3)^(1/4)
 =212.123312834...`.                                                   (4.10)

The maximum of (4.7), (4.10), and `24` is below `232`, proving (4.3). Reflection of the output variable proves the `-M_*` case. QED.

The early checkpoint contained an arithmetic slip in the T-heavy numerical constant; `CHECKPOINT_CORRECTION.md` records (4.9)-(4.10). The global `<232` theorem was unaffected.

## 5. Required Claude result applied to the one-sheet side

Theorem C in the pinned `e5f71d79...` `COUNTEREXAMPLE_SEARCH.md` applies directly to the same weighted target family because its nonzero eigenvalues are exactly `1,1,-1`. Therefore, independently of all row weights and multiplicities,

`boxed: p_Q(t) <= pi sqrt(2),  t>=0.`                                  (5.1)

This is the real source inequality required by the owner continuation. It is not extended to `t<0`: the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction rules out that inference from line/X-ray control alone. Theorem 4.1 supplies a full-line bound, so in this family the sign-specific splice is explicit:

- the ruled theorem sharply pays the one-sheet side `t>=0`;
- aggregate-before-inversion plus the physical-pivot branch pays the opposite two-sheet side.

For `-Q`, the same statement is reflected: the ruled estimate applies to `t<=0` for the original `Q`.

## 6. Quantitative null-ruling defect for the general two-plane chamber

The weighted theorem handles an exact clustered model. The next issue is to identify a correct quantitative invariant in the general near-null two-plane geometry. Partner r32 proves that the maximum of the old local pivot certificates is not such an invariant.

Use the partner r31 coordinates. Let the T-plane physical rows be

`z_j=(u_j,v_j)`,

with plane covariance

`sum_j z_j z_j^T=diag(1-rho,1)`,                                      (6.1)

and let the spectral matrix have `m_22=0`. Then

`d_j:=A_jj=v_j(2m_23u_j+m_33v_j)`.                                   (6.2)

Invertibility of `M` implies

`kappa_T:=sqrt(4m_23^2+m_33^2)>0`;                                   (6.3)

otherwise its second and third rows cannot give full rank when `m_22=m_23=m_33=0`.

Define the two null rulings in the T plane by

`L_0={v=0}`,
`L_1={2m_23u+m_33v=0}`.                                               (6.4)

### Lemma 6.1 — `QFORM-NULL-RULING-L1-TO-L2-v1`

For every T row,

`boxed: dist(z_j,L_0 union L_1)^2 <= |A_jj|/kappa_T.`                  (6.5)

Consequently, if

`D_T=sum_j |A_jj|`,                                                   (6.6)

and `z_j^*` is a nearest-point projection of `z_j` to the union of the two null lines, then

`boxed: sum_j ||z_j-z_j^*||^2 <= D_T/kappa_T.`                        (6.7)

### Proof

The distances to the two individual lines are exactly

`d_0=|v_j|`,
`d_1=|2m_23u_j+m_33v_j|/kappa_T`.                                    (6.8)

By (6.2), `d_0d_1=|A_jj|/kappa_T`. Since `min(d_0,d_1)^2<=d_0d_1`, (6.5) follows; summing gives (6.7). QED.

This is the correct aggregate repair of the false rowwise implication. It uses the L1 physical-diagonal defect `D_T`, not the maximum of a leverage-weighted local certificate.

### Covariance consequence

Set

`epsilon_T^2=D_T/kappa_T`,
`eta_T=2sqrt(2)epsilon_T+epsilon_T^2`.                                (6.9)

Let

`G_T^*=sum_j z_j^*(z_j^*)^T`.                                        (6.10)

Because `sum ||z_j||^2=2-rho<=2`, (6.7) and the elementary Gram perturbation estimate give

`||G_T^*-diag(1-rho,1)||_op <= eta_T`.                               (6.11)

Indeed, with row matrices `Z^*=Z-E`,

`||Z^T Z-(Z-E)^T(Z-E)||_op
 <=2||Z||_F||E||_F+||E||_F^2
 <=2sqrt(2)epsilon_T+epsilon_T^2`.

If

`eta_T <= (1-rho)/2`,                                                 (6.12)

then each null ruling must carry quantitative projected squared mass. Write

`G_T^*=m_0 e_0e_0^T+m_1e_1e_1^T`,                                   (6.13)

where `e_0,e_1` are unit vectors along the two lines. Weyl's inequality and (6.11) give

`det G_T^* >= (1-rho)/4`,
`tr G_T^* <=3`.                                                       (6.14)

Since

`det G_T^*=m_0m_1 sin^2(theta)`, `tr G_T^*=m_0+m_1`,                  (6.15)

we obtain

`m_0,m_1 >= (1-rho)/12`,
`sin^2(theta) >= (1-rho)/9`.                                         (6.16)

The angle is explicit:

`sin(theta)=2|m_23|/kappa_T`,                                        (6.17)

so (6.16) also forces

`|m_23| >= kappa_T sqrt(1-rho)/6`.                                   (6.18)

There is an exact reflected S-plane statement. For S rows `(x_i,y_i)`,

`A_ii=x_i(m_11x_i+2m_12y_i)`,
`kappa_S=sqrt(m_11^2+4m_12^2)`,                                      (6.19)

and the two null rulings are `x=0` and `m_11x+2m_12y=0`. If `D_S=sum_i|A_ii|`, then

`sum_i dist((x_i,y_i),L_0^S union L_1^S)^2 <= D_S/kappa_S`.          (6.20)

With `epsilon_S^2=D_S/kappa_S`, `eta_S=2sqrt(2)epsilon_S+epsilon_S^2`, the condition `eta_S<=rho/2` implies both projected S-ruling masses are at least `rho/12` and

`2|m_12|/kappa_S >= sqrt(rho)/3`.                                    (6.21)

### Why this does not contradict partner r32

At the symmetric partner stress point `rho=1/2` with `M=M_*`, its local pivot quantities vanish like `k^-2`, but the aggregate ruling defect does not vanish. Indeed

`D_S/kappa_S=1`,
`D_T/kappa_T=1/sqrt(2)`.                                              (6.22)

So Lemma 6.1 correctly refuses to infer proximity to an exact null split. This applies the partner's obstruction to identify a genuinely stronger invariant rather than renaming the same failed local criterion.

## 7. Rank-two logarithmic control and the precise third-direction smoothing

The mandatory rank-two failure remains real. For independent

`X,Y ~ Uniform[-1/2,1/2]`,

`R=2XY`

has

`p_R(t)=log(1/(2|t|))`, `0<|t|<1/2`.                                (7.1)

Thus an opposite-sign rank-two saddle is not bounded-density.

Now add an independent original cap-one scalar `Z` through a genuine square:

`Q_0=2XY+Z^2`.                                                        (7.2)

The rank-two matrix of `2XY` is `[[0,1],[1,0]]`, determinant `-1`. The completed affine half-Riesz theorem, in its sharper zero-affine form, gives

`sup_s E|2XY-s|^(-1/2) <=16sqrt(30)`.                                (7.3)

The density of `Z^2` is at most `u^(-1/2)` for `u>0`; therefore

`p_(Q_0)(s)
 <= E[(s-2XY)_+^(-1/2)]
 <= E|s-2XY|^(-1/2)
 <=16sqrt(30)`.                                                       (7.4)

Equation (7.4) says exactly what the third direction does analytically: it does not make the rank-two density bounded first; its square kernel takes a half-order Riesz potential of the logarithmic saddle, and that fractional potential is finite.

The weighted four-ray target is harder because its spectral coordinates are dependent: for `M_*`, formally

`Q=Y_1^2+2Y_2Y_3`, `Y=R^T X`,                                      (7.5)

but `Y_1,Y_2,Y_3` are not declared independent. Theorem 3.1 recovers the missing third-direction smoothing instead by grouping disjoint **source** coordinates until two independent physical rank-three volumes are macroscopic. Thus the same “rank two logarithm plus a third direction” principle survives a genuinely rotated setting without a hidden rotation-independence assumption.

## 8. What changed and what remains

This run makes two substantive advances over the previous proof map.

First, the equal-weight four-ray obstruction of partner r32 is no longer an isolated stress example: arbitrary ray weights and multiplicities are uniformly paid whenever the geometrically stronger pair of rays is diffuse, and the canonical target matrix `M_*` is uniformly paid in all weight configurations by the diffuse/heavy dichotomy. The resulting explicit target-family constant is `<232`, while the pinned ruled theorem gives the much sharper `pi sqrt(2)` on the one-sheet half-line.

Second, the near-null two-plane problem now has a correct aggregate geometry variable. Small `D_T/kappa_T` or `D_S/kappa_S` forces L2 proximity to the actual pair of null rulings, with quantitative mass on both rulings and a quantitative angle. Partner r32 shows why the old maximum local-pivot quantity cannot do this.

The remaining mathematical gap is not “prove rows approach the null set”; Lemma 6.1 now supplies that implication under the aggregate defect. The gap is the **product-preserving compiler from approximate ruling clusters**: the actual rows are close to, but not exactly on, the rulings, so replacing them by their projections would be an impermissible small-quadratic perturbation argument for arbitrary unbounded input supports. One must instead use the cluster membership on the original coordinates to build a true cross-volume/ridge/Fresnel receiver, or route the failure of the aggregate-defect condition to another paid branch.

Arbitrary additional nonseparable spectrum remains a separate full-QFORM bridge. No claim here closes the unrestricted conjecture.

## 9. Verification summary

The exact identities checked for this run are:

- `spec(M_*)={1,1,-1}` and `det M_*=-1`;
- the four base triple squared determinants are `4rho,4rho,4(1-rho),4(1-rho)`;
- `R^T R=I_3` under four arbitrary ray mass totals `1/2`;
- aggregate group volumes in Theorem 3.1 are at least `1/64`;
- the diffuse branch constant is `24/s`;
- the S-heavy constant is `128(32/3)^(1/4)=231.322112924...`;
- the corrected T-heavy constant is `128(16sqrt(2)/3)^(1/4)=212.123312834...`;
- the null-ruling pointwise distance identity (6.5) and Gram perturbation bound (6.11) are algebraic.

No Monte Carlo inference, new task, scheduler mutation, email/notification action, cross-account authentication, paid call, remote workflow, public release, permission change, installation, FEI, benchmark, or unrelated-data access was used.
