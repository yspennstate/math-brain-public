SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B10, 2026-09-22T21:18:27Z.
attacking: the exact-rank-three heavy-null nonnested branch; turn the B19 two-bank partition into a three-cross-singular-value density gate, and quantify the complementary high-leverage row geometry without conditional projection caps.

# account03/B10 r18 — geometric-mean three-cross gate + all-scale Witt row gate

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** rank-three coupled case  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREMS / FULL TARGET OPEN`

The exact owner target remains open: for every finite dimension, independent real original-coordinate inputs with probability densities at most one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal bound on the essential supremum of the density of `Q=X^TAX`, or give a target-valid counterexample. Continuity is tracked separately.

Fresh owner control at this run was QFORM-only, revision `2026-09-22.15`. The live corrections against law-uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea, positive conditional projection-density moments, post-rotation independence, fixed-good-minor extraction and naive fiber suprema remain binding. None is used here.

The exact named partner `account04/B10` still has no completed current-QFORM report or handoff visible at the fresh lookup, only its current-QFORM login. I therefore do not fabricate a partner result. The completed compatible account04 result actually applied is account04/B16,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260922T161909Z-account04-B16-QFORM-r2/REPORT.md`,

whose fixed-pair determinant-bank identity is used quantitatively in Section 5.

Other completed inputs used at their proved scopes are:

1. account03/B19, `QFORM-DIFFUSE-2D-TWO-BANK-PARTITION-v1`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260922T203112Z-account03-B19-QFORM/REPORT.md`;
2. the regularized cross-determinant theorem,
   `proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`;
3. the exact-rank-three scalar-pivot theorem `QFORM-RANK3-ALL-RESIDUAL-ORIENTATIONS-v1`, source-recorded at
   `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`;
4. this slot's preceding r17 theorem `QFORM-INDEFINITE-PAIR-SCHUR-BANK-v1`.

## 1. Exact state inherited from B10 r17 and B19

After the cap-one null-bank compression from earlier B10 work, the unpaid near-endpoint exact-rank-three state has a Parseval spectral representation with an invertible symmetric `3 x 3` matrix `M`, a distinguished synthetic original independent coordinate `X_0`, and spectral row

`u_0=sqrt(c) r`,

where

`r^T M r=0`, `c>=7/9`, `sigma:=sigma_min(M)>=1/2`, `D:=|det M|>=1/2`.

Write every complementary row in an orthonormal Witt basis `(r,w,m)` as

`u_j=alpha_j r+beta_j w+gamma_j m`,

and put

`v_j=(beta_j,gamma_j) in R^2`, `h_j=||v_j||^2`.

The r17 nested-heavy result has already closed every branch with some `h_j>1/2`. Hence the current branch satisfies

`h_j<=1/2` for all `j`, and `sum_j v_j v_j^T=I_2`.                 (1.1)

Apply account03/B19. There is a partition of the complementary **original-coordinate** indices into disjoint banks `J,K` such that

`S_G:=sum_(j in G) v_j v_j^T`, `G=J,K`,

obeys

`det S_J det S_K>=1/640`,                                      (1.2)

and, in particular,

`det S_J,det S_K>=1/640`, `lambda_min(S_J),lambda_min(S_K)>=1/640`. (1.3)

This is the residual-diffuse two-bank state. It is product-preserving because `J,K` are disjoint physical coordinate sets.

For each bank let `V_G` be the matrix with rows `v_j`, let `alpha_G=(alpha_j)_(j in G)`, and make the exact least-squares decomposition

`alpha_G=V_G p_G+eta_G`, `V_G^T eta_G=0`,

with

`tau_G=||eta_G||^2`.                                            (1.4)

The account03/B04 generated-leakage theorem already closes the branch `tau_J=0` or `tau_K=0`. The genuinely unpaid state therefore has both `tau_J,tau_K>0`.

## 2. New algebra: the two residual leakages are exactly the missing third cross singular direction

Let `C_G` be the physical-row matrix on bank `G`, with rows

`(alpha_j,beta_j,gamma_j)`.

Its Gram matrix is `K_G=C_G^T C_G`. Subtracting the generated component `V_G p_G` from the first column is a determinant-one column shear. In the sheared coordinates the first column is `eta_G`, orthogonal to the other two columns. Hence

`boxed: det K_G=tau_G det S_G.`                                  (2.1)

Because `tau_G>0` and `S_G` is positive definite, each `C_G` has column rank three.

The physical cross block between the two independent banks is

`B_JK=A[J,K]=C_J M C_K^T`.                                      (2.2)

Write `C_G=Q_G K_G^(1/2)` with `Q_G^TQ_G=I_3`. Then

`B_JK=Q_J [K_J^(1/2) M K_K^(1/2)] Q_K^T`.                       (2.3)

Therefore `B_JK` has exactly three nonzero singular values `s_1>=s_2>=s_3>0`, and their product is

`boxed:
 s_1 s_2 s_3
 =D sqrt(det K_J det K_K)
 =D sqrt(tau_J tau_K det S_J det S_K).`                         (2.4)

Using (1.2),

`boxed:
 s_1s_2s_3 >= D sqrt(tau_J tau_K/640).`                         (2.5)

Thus the two residual leakages are not merely nuisance terms. When both are present, they create the third singular direction of an actual original-coordinate cross block. This is exact; no projected-coordinate independence is asserted.

The projection onto `range(B_JK)=range(C_J)` also has an exact row-leverage formula. In the sheared coordinates its diagonal at `j in J` is

`ell_(J,j)=v_j^T S_J^(-1)v_j + eta_j^2/tau_J`.                  (2.6)

Indeed the sheared Gram is `diag(tau_J,S_J)`. Define

`L_G=max_(j in G) ell_(G,j)`.                                   (2.7)

The same formula holds on `K`.

## 3. New analytic theorem: geometric-mean three-cross gate

### Theorem 3.1 — `QFORM-THREE-CROSS-GEOMEAN-v1`

Let a quadratic form in independent cap-one original coordinates have a disjoint physical cut with cross block `B` of rank at least three. Let its first three singular values be `s_1,s_2,s_3`, and put

`g=(s_1s_2s_3)^(1/3)`.

Suppose that on one side of the cut the coordinate diagonal of the orthogonal projection onto `range(B)` is at most `q/2`, for some

`1<=q<3/2`.                                                       (3.1)

Then the full quadratic form, with arbitrary self-quadratic terms on both sides and arbitrary outside coordinates/couplings, has a **bounded continuous density** and

`boxed:
 ||p_Q||_infinity <= C(q)/g,`                                    (3.2)

where

`C(q)= [e sqrt(pi)/(2 sqrt(2q))]
       Gamma(3/(4q)-1/2)/Gamma(3/(4q)).`                        (3.3)

No lower bound on the individual `s_i` is required; only their geometric mean appears.

#### Proof

The completed regularized determinant theorem gives, under (3.1),

`|phi_Q(t)| <= prod_(i=1)^3
 (1+a_q t^2 s_i^2)^(-1/(4q)),`

where

`a_q=2q/(pi^2 e^2)`.                                            (3.4)

All other singular-value factors, if present, are at most one and may be discarded. Put `x_i=a_q t^2s_i^2`. By the elementary symmetric AM-GM inequalities,

`sum x_i>=3(x_1x_2x_3)^(1/3)`,
`sum_(i<j)x_ix_j>=3(x_1x_2x_3)^(2/3)`.

Therefore

`prod_(i=1)^3(1+x_i)
 >=[1+(x_1x_2x_3)^(1/3)]^3
 =[1+a_q t^2 g^2]^3`.                                           (3.5)

Hence

`|phi_Q(t)| <=(1+a_q g^2t^2)^(-3/(4q)).`                        (3.6)

Because `q<3/2`, the exponent `3/(4q)` is strictly greater than `1/2`, so the right side is integrable. Fourier inversion gives continuity and

`||p_Q||_infinity
 <=(2pi)^(-1) int_R(1+a_qg^2t^2)^(-3/(4q))dt`
` =C(q)/g`,                                                     (3.7)

using the standard beta/gamma integral. QED.

This is an integrated product-space Fourier estimate. It does not contradict the correction against law-uniform pointwise one-dimensional quadratic-phase decay.

For reference,

`C(1)=5.0398975039...`,
`C(5/4)=9.7332824231...`,
`C(4/3)=14.4367825896...`.                                      (3.8)

## 4. Direct application to the B10 residual-diffuse heavy-null state

Apply Theorem 3.1 to the actual original-coordinate cut `J,K` from Section 1. Combining (2.4) with (1.2),

`g
 >=D^(1/3) (tau_Jtau_K/640)^(1/6).`                            (4.1)

Thus whenever

`min(L_J,L_K)<=q/2`, `1<=q<3/2`,                                (4.2)

we obtain the target-level inequality

`boxed:
 ||p_Q||_infinity
 <= C(q) D^(-1/3) 640^(1/6)(tau_Jtau_K)^(-1/6).`               (4.3)

In the compressed B10 state `D>=1/2`, so

`||p_Q||_infinity
 <= C(q) 2^(1/3)640^(1/6)(tau_Jtau_K)^(-1/6).`                 (4.4)

Three useful numerical instances are:

- if `min L_G<=1/2`, the front constant in (4.4) is `<18.641`;
- if `min L_G<=5/8`, it is `<36.000`;
- if `min L_G<=2/3`, it is `<53.397`.

In particular:

### Corollary 4.1 — a fully universal residual-leakage branch

If

`tau_J>=1/64`, `tau_K>=1/64`, and `min(L_J,L_K)<=2/3`,            (4.5)

then

`boxed: ||p_Q||_infinity <214,`                                 (4.6)

and the density is continuous.

Indeed `(tau_Jtau_K)^(-1/6)<=4`; use `q=4/3` in (4.4).

This closes a genuine part of the previously unresolved **both-residual-leakages-nonzero** chamber. It does not select a local minor, and arbitrary longitudinal/transverse overlap inside both banks is retained.

## 5. Completed account04 mathematics applied to an actual inequality

The exact designated account04/B10 has no completed current-QFORM artifact at this run's lookup. The completed compatible account04/B16 fixed-pair identity says, for the distinguished exact-null physical row `0` and any complement row `j`,

`P_0j:=sum_k |det A_{ {0,j,k} }|
      =D c h_j`.                                                  (5.1)

Apply this identity to each B19 bank. Since

`sum_(j in G)h_j=tr S_G >=2 sqrt(det S_G)>=2/sqrt(640)`,         (5.2)

we get the concrete bankwise determinant-resource estimate

`boxed:
 sum_(j in G) P_0j
 >= 2Dc/sqrt(640)
 >= 7/(9sqrt(640))
 =0.03074436614... ,
 G=J,K.`                                                         (5.3)

Thus neither independent B19 bank can be transverse-determinant empty. Equation (5.3) is an actual inequality obtained from the completed account04 theorem, not a decorative citation. The remaining difficulty is how its determinant resource is distributed relative to the longitudinal residual-leakage vectors; Theorem 3.1 pays a large part of that overlap through the full three-singular-value cross block instead of reciprocal local minors.

## 6. New all-scale Witt energy inequality

The remaining failure mode of Corollary 4.1 includes high bank-range leverage. The following quantitative lemma narrows that geometry and does not require `h>=1/2` as r17 did.

### Lemma 6.1 — `QFORM-NULL-WITT-ENERGY-ALLSCALE-v1`

Let `M` be invertible symmetric `3 x 3`, `sigma=sigma_min(M)`, and let `r` be a unit null vector. Put `S=||Mr||`, `w=Mr/S`, and complete `(r,w)` to an orthonormal basis `(r,w,m)`. For

`u=alpha r+beta w+gamma m`,
`h=beta^2+gamma^2`,
`x=S|beta|/sigma=|r^TMu|/sigma`,
`q=u^TMu`,

one has

`boxed:
 h <= 2|q|/sigma +12x^2+2alpha^2.`                              (6.1)

#### Proof

In the Witt basis write

`M=[[0,S,0],[S,a,b],[0,b,k]]`.

Direct inversion gives

`S>=sigma`, `|k|>=sigma`,
`|b|<=S|k|/sigma`,
`|a|<=2S^2|k|/sigma^2`.                                        (6.2)

Therefore

`|q|/sigma >=|q|/|k|`
` >=gamma^2-2|alpha|x-2x^2-2x|gamma|`.

Since `beta^2<=x^2`,

`>=h-3x^2-2|alpha|x-2x|gamma|`.

Use `2x|gamma|<=(1/2)gamma^2+2x^2` and then `2|alpha|x<=alpha^2+x^2`. This yields

`|q|/sigma >= (1/2)h-6x^2-alpha^2`,

which rearranges to (6.1). QED.

### Corollary 6.2 — a nonlongitudinal diffuse row is already paid

In the compressed B10 state (`sigma,D>=1/2`, `c>=7/9`), suppose a complementary physical row has

`h>=1/1920`, `alpha^2<=h/8`.                                    (6.3)

Then the full quadratic form has an essentially bounded density with the explicit, deliberately nonoptimized universal estimate

`boxed: ||p_Q||_infinity <12054.`                               (6.4)

#### Proof

By (6.1), (6.3) implies

`(3/4)h <=2|q|/sigma+12x^2`.

Hence either

`|q|>=3sigma h/16`                                              (6.5)

or

`x^2>=h/32`.                                                    (6.6)

In (6.5), the exact-rank-three scalar-pivot theorem gives

`||p_Q||_infinity
 <=128[(alpha^2+h)|q|D]^(-1/4)
 <=128[3h^2/64]^(-1/4)
 <12054`                                                        (6.7)

at `h=1/1920`.

In (6.6), the physical cross coefficient from the heavy null row is

`b_0j=sqrt(c) r^TMu`,

so

`|b_0j|>=sqrt(7/9)(1/2)sqrt(h/32)
        =0.07795119555... sqrt(h)`.                             (6.8)

If `|q|>=|b_0j|`, the scalar-pivot theorem is even better (`<4907` at the endpoint). If `|q|<|b_0j|`, the physical pair

`[[0,b_0j],[b_0j,q]]`

is indefinite and has least singular value at least `|b_0j|/2`. The r17 aggregate Schur-bank theorem applies, while account04/B16 gives its fixed-pair bank

`P_0j=Dch>=7h/18`.                                              (6.9)

Thus

`||p_Q||_infinity
 <=8*2^(3/4)[sigma_min(pair) P_0j]^(-1/4)
 <654`                                                          (6.10)

at `h=1/1920`. Combining the cases proves (6.4). QED.

The value `12054` is not presented as a sharp constant; its purpose is to make the branch genuinely universal.

## 7. What the remaining exact-rank-three obstruction now looks like

For a bank `G`, write

`t_j=v_j^T S_G^(-1)v_j`, `s_j=eta_j^2/tau_G`,

so its cross-range leverage is `ell_j=t_j+s_j` by (2.6). If `ell_j>2/3`, then either `t_j>1/3` or `s_j>1/3`.

If `t_j>1/3`, (1.3) gives

`h_j>=lambda_min(S_G)t_j>1/1920`.                               (7.1)

Corollary 6.2 therefore pays that row unless it is quantitatively longitudinal-dominant:

`alpha_j^2>h_j/8`.                                              (7.2)

Consequently, after this run, a configuration escaping the universal `<214` cross gate and the row gate must lie in the following much narrower state:

1. at least one residual leakage norm is `<1/64`, **or** both bank range leverages exceed `2/3`;
2. in every bank whose leverage excess is caused by `t_j>1/3`, every such witness surviving the row gate satisfies the longitudinal-dominance condition (7.2);
3. if instead the excess is caused by `s_j>1/3`, more than one third of that bank's residual leakage energy is concentrated on a single physical coordinate.

Call this remaining mechanism

`QFORM-HEAVY-NULL-SMALLRESIDUAL-OR-DOUBLEHIGH-v1`.

It is strictly smaller than the r17 `QFORM-HEAVY-NULL-NONNESTED-v1` chamber: the two-bank extraction, both-residual exact cross determinant, a nontrivial universal cross-density branch, and an all-scale high-transverse-row gate are all now paid.

A next attack should aggregate the **small residual leakage** with the heavy null scalar before any conditional cap is taken, and separately exploit the two explicit physical witnesses in the double-high branch. A mere perturbative operator-norm argument is not justified under the current no-moment hypotheses.

## 8. Status and regularity

Proved in this run:

- `QFORM-THREE-CROSS-GEOMEAN-v1`, including continuity;
- exact two-bank cross determinant identity (2.4) and leverage identity (2.6);
- the universal `<214` residual-leakage branch (4.6);
- account04/B16 applied to the actual bankwise determinant lower bound (5.3);
- `QFORM-NULL-WITT-ENERGY-ALLSCALE-v1`;
- the universal nonlongitudinal diffuse-row gate (6.4).

Not proved:

- the small-positive-residual-leakage limit uniformly as `tau_G downarrow0`;
- the double-high bank-range-leverage state after the explicit witness split above;
- arbitrary additional spectrum beyond exact rank three;
- the full owner conjecture.

Essential boundedness is proved in the new branches. Continuity is proved for the three-cross geometric-mean branch through `L^1` Fourier inversion; it is **not** claimed for the Witt row branch. The full QFORM conjecture remains **OPEN / NOT PROVED**.
