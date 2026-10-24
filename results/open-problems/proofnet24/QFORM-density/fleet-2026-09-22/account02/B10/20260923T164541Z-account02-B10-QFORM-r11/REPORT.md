# account02/B10 — near-null hub discriminant obstruction and aggregate crossing factorization

Status: `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_IDENTITIES / LOCAL_ROUTE_COUNTEREXAMPLE / FULL_QFORM_OPEN`.

Programme: QFORM-DENSITY-3EIG-20260922. Owner continuation acknowledged: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`. The full target remains open.

## 1. First unpaid implication

After consuming the completed one-sheet theorem and the designated-partner exact-null theorem, the first unpaid B10 implication is

`QFORM-TWOSHEET-NEARNULL-JOINT-PRODUCT-SMOOTHING-v1`:

For an exact-rank-three indefinite form with a heavy ORIGINAL physical row whose Rayleigh coefficient is nonzero but arbitrarily close to zero, control the two-sheet side uniformly while retaining the hub and transverse original-coordinate product structure jointly through the smoothing step.

The calculation below proves two exact identities and a source-valid route obstruction. The first identity shows that hub-first root integration collapses to a two-dimensional discriminant with determinant exactly `q det M`; its natural absolute negative-half-power receiver can diverge logarithmically as `q->0`. The second identity factors the newest one-hub projected-crossing currency exactly into spectral-frame Gram determinants, showing that near-nullness itself does not degrade that currency; only product-partition/near-coloop degeneracy can.

## 2. Sources actually consumed

Required source bundle: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. I read `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` at that commit.

Two completed results from that source are applied below at actual inequalities: the ruled one-sheet theorem `p_Q(s)<=pi sqrt(2)` on the one-sheet side of exact rank-three inertia `(2,1)` with the present zero linear term, and the three-variable theorem `||p_Q||_infinity<=6 sqrt(pi)/sigma` when all three eigenvalues have modulus at least `sigma`.

Designated partner actually applied: account03/B10 r24, canonical bundle `yspennstate/math-open-problems@c0d7e627b3b877fcecc3004a58335658f6541d64`, report introduced at `dc9d69f51688728122da9fd35835593beaa694c7`. Its completed theorem `QFORM-NULL-HUB-TRANSVERSE-LEVERAGE-CLOSURE-v1` gives

`||p_Q||_infinity <= 3*2^(4/3)(h |det M|)^(-1/3)`

for an exact-null ORIGINAL hub `u_0=sqrt(h)r` when every complementary transverse leverage is at most `1/2`.

Newest continuation checked: `math-open-problems@c4c23b784395630c094ba299a50712209921d1ae`, `20260922T231000Z-semidefinite-and-hub-reduction/README.md` and `hub_with_diagonal/REPORT.md`; and `math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`, `NEW_PROJECTED_CROSSING.md`. During this run account01/B03 completed the compatible row-marginal-free one-hub theorem at `math-open-problems@4b7608c198ea570378ae30b5a22d63ba7d387534`, theorem `QFORM-ONE-HUB-ROW-MARGINAL-FREE-2VOLUME-v1`; it is applied in Section 6 to an actual physical partition.

## 3. Exact discriminant identity in ORIGINAL product coordinates

Let

`A=R M R^T`, `R^T R=I_3`,

where `M` is symmetric and invertible and all three eigenvalues of `M` have modulus at least one. Choose an ORIGINAL physical row

`u_0=sqrt(h) r`, `||r||=1`, `0<h<=1`.

Relative to `span(r) direct-sum r^perp`, write

`M = [[q,b^T],[b,C]]`,

with `q=r^T M r`. For every remaining row write `u_j=t_j r+p_j`, `p_j in r^perp`. Parseval gives

`sum_j t_j^2=1-h`,
`sum_j p_j p_j^T=I_2`,
`sum_j t_j p_j=0`.

For the ORIGINAL leaf variables define

`T=sum_j t_j X_j`, `V=sum_j p_j X_j`.

Then `X_0` is genuinely independent of `(T,V)`, and with `z=sqrt(h)X_0+T`,

`Q=q z^2+2z b^T V+V^T C V`.                                             (3.1)

For `q!=0`, solving `Q=s` in the ORIGINAL independent coordinate `X_0` yields at every simple root

`(qz+b^T V)^2 = D_s(V)`,
`D_s(V)=V^T K V+q s`,
`K=bb^T-qC`.                                                             (3.2)

The derivative is `|partial Q/partial X_0|=2 sqrt(h) sqrt(D_s(V))`. Since there are at most two roots and `f_0<=1`, the one-coordinate coarea/root formula gives for a.e. `s`

`p_Q(s) <= h^(-1/2) E[1_{D_s(V)>0} D_s(V)^(-1/2)]`.                    (3.3)

The longitudinal leaf variable `T` disappears exactly. The remaining `V` is not declared to have independent coordinates: it is a two-dimensional projection of the original independent leaves with Parseval rows `p_j`.

The discriminant matrix obeys

`det K = q det M`.                                                        (3.4)

Indeed, in dimension two,

`det(qC-bb^T)=q^2 det C-q b^T adj(C)b=q det M`,

and `K=-(qC-bb^T)` has the same determinant. Also

`||b||^2=||Mr||^2-q^2 >= 1-q^2`                                      (3.5)

because `sigma_min(M)>=1`.

For inertia `(2,1)`, if `q<0`, the Schur complement `C-bb^T/q` is positive definite, so `K=-q(C-bb^T/q)` is positive definite. If `q>0`, the Schur complement and `K` are indefinite. At `q=0`, `K=bb^T` has rank one. This is the exact rank jump in the near-null collar.

## 4. Exact factorization of the one-hub aggregate crossing currency

Let the leaves be split into disjoint ORIGINAL banks `I` and `J`. Put

`S_I=sum_(i in I) p_i p_i^T`,
`G_J=sum_(j in J) u_j u_j^T`.

For account01/B03's one-hub theorem, define `m=A_{0,J}`, `a_i=A_{i,J}` and

`V_3=sum_(i<k in I)|m wedge a_i wedge a_k|^2`.

Then in exact rank three,

`boxed: V_3 = h (det M)^2 det(S_I) det(G_J).`                           (4.1)

Proof. For every pair `i,k in I`, the three-row cross matrix is

`A_{ {0,i,k},J}=R_{ {0,i,k}} M R_J^T`.

Therefore

`|m wedge a_i wedge a_k|^2`
` =det(A_{ {0,i,k},J} A_{ {0,i,k},J}^T)`
` =(det M)^2 det(G_J) det(R_{ {0,i,k}})^2`.

Since `u_0=sqrt(h)r` and `u_i=t_i r+p_i`,

`det(R_{ {0,i,k}})^2=h det(p_i,p_k)^2`.

Summing and applying two-dimensional Cauchy-Binet gives

`sum_(i<k in I) det(p_i,p_k)^2=det(S_I)`, proving (4.1).

Consequently the newest row-marginal-free theorem gives the conditional structural implication

`||p_Q||_infinity <= C_* [h(det M)^2 det(S_I)det(G_J)]^(-1/6)`,         (4.2)

whenever one can exhibit such a split with positive determinants, where `C_*=3*2^(7/6) exp(1/3)<9.400`.

Equation (4.1) is useful conceptually: the one-hub projected-crossing currency does **not** contain the near-null scalar `q` at all. Thus nonzero `q->0` is not itself an obstruction to this compiler. Degeneration occurs only if every relevant original-coordinate split loses transverse determinant or full three-dimensional leaf Gram determinant; in particular, the exact-coloop limit `h->1` can force `det(G_J)->0` for every leaf-only `J`.

## 5. Source-valid logarithmic obstruction to the hub-first absolute receiver

Fix `h=7/8` and `0<=eps<=1/288`, and put

`M_eps=[[eps,sqrt(1+eps),0],[sqrt(1+eps),0,0],[0,0,1]]`.               (5.1)

Its eigenvalues are exactly `{1+eps,1,-1}`. Use the six Parseval rows

`sqrt(h)e1`, `sqrt(1-h)e1`, `e2/sqrt(2)`, `e2/sqrt(2)`, `e3/sqrt(2)`, `e3/sqrt(2)`.   (5.2)

Thus the physical matrix has exactly those three nonzero eigenvalues. Every complementary transverse leverage relative to `r=e1` is `0` or `1/2`.

Take the two `e2`-bank inputs iid Uniform`[-1/2,1/2]` and the two `e3`-bank inputs iid Uniform`[1,2]`; the two `e1`-bank inputs may be any cap-one probability laws. Define the disjoint-bank projections

`Y=(X_2+X_3)/sqrt(2)`, `Z=(X_4+X_5)/sqrt(2)`.

Their triangular densities satisfy

`p_Y(y)>=1/sqrt(2)` for `0<=y<=1/(2sqrt(2))`,
`p_Z(z)>=1/sqrt(2)` for `5/(2sqrt(2))<=z<=7/(2sqrt(2))`.                 (5.3)

Here `q=eps`, `b=(sqrt(1+eps),0)`, `C=diag(0,1)`, so

`K=diag(1+eps,-eps)`,
`D_0(Y,Z)=(1+eps)Y^2-eps Z^2`.                                          (5.4)

On

`5/(2sqrt(2))<=z<=7/(2sqrt(2))`,
`3sqrt(eps)<=y<=1/(2sqrt(2))`,

we have `z<3`, so `D_0>0`, and also `D_0<=(1+eps)y^2`. Hence

`E[1_{D_0>0}D_0^(-1/2)]`
` >= [1/(2sqrt(2)sqrt(1+eps))] log(1/(6sqrt(2 eps)))`.                  (5.5)

This diverges as `eps downarrow 0`. Therefore the absolute receiver in (3.3) cannot furnish a uniform near-null bridge. This is a counterexample to that proof interface, not to QFORM.

## 6. The same family is uniformly safe — four actual inequalities

### 6.1 Required ruled theorem

For every `eps>=0`, the form has inertia `(2,1)` and no linear term. The completed ruled theorem at the required `e5f71d...` source gives on the one-sheet side, including `s=0`,

`p_Q(s)<=pi sqrt(2)<4.443`.                                               (6.1)

Thus the logarithm in (5.5) is loss in the hub-first absolute estimate at the same level where the actual density is uniformly bounded.

### 6.2 Required source three-variable theorem after legal bank aggregation

The six original variables split into three disjoint coordinate banks. Their spectral-axis projections

`Z_1=sqrt(h)X_0+sqrt(1-h)X_1`, `Y`, `Z`

are genuinely independent. Each has density at most `sqrt(2)` by the one-dimensional product-projection bound. Put `W_i=sqrt(2)Z_i`; then the `W_i` are independent with density at most one, and

`Q=(1/2)W^T M_eps W`.

The eigenvalues of `M_eps/2` have modulus at least `1/2`. Theorem A from the required `COUNTEREXAMPLE_SEARCH.md` therefore gives the all-level bound

`||p_Q||_infinity<=12 sqrt(pi)<21.270`,                                  (6.2)

uniformly in `eps`. Independence is used only for the disjoint ORIGINAL banks.

### 6.3 Designated partner at the compatible exact-null endpoint

At `eps=0`, (5.2) has an exact-null heavy hub with `h=7/8`, `|det M_0|=1`, and all complementary transverse leverages at most `1/2`. Account03/B10 r24 therefore applies exactly:

`||p_Q||_infinity <=3*2^(4/3)(7/8)^(-1/3)`
`=7.903605...<7.904`.                                                     (6.3)

This is the required inequality-level use of the completed designated partner theorem. No continuity in `eps` is inferred.

### 6.4 Newest row-marginal-free one-hub crossing theorem on an actual partition

For the corrected family choose leaf banks

`I={one e2/sqrt(2) row, one e3/sqrt(2) row}`,
`J={sqrt(1-h)e1, the other e2/sqrt(2) row, the other e3/sqrt(2) row}`.

Then

`S_I=diag(1/2,1/2)`, so `det S_I=1/4`,

while

`G_J=diag(1-h,1/2,1/2)`, so `det G_J=(1-h)/4=1/32`.

Since `|det M_eps|=1+eps`, (4.1) gives

`V_3 = h(1+eps)^2/128 = 7(1+eps)^2/1024 >=7/1024`.                     (6.4)

Apply account01/B03's completed `QFORM-ONE-HUB-ROW-MARGINAL-FREE-2VOLUME-v1`:

`||p_Q||_infinity <= C_* V_3^(-1/6)`
` <= 9.399132 (1024/7)^(1/6)`
` <21.576`.                                                              (6.5)

This is a direct original-coordinate physical-partition payment. It independently confirms that the punctured family is uniformly safe even though the hub-first discriminant receiver diverges.

## 7. Consequence for the proof map

The surviving collar is not a weak-star problem. Equation (3.5) keeps the hub-to-transverse star quantitatively strong as `q->0`. Equation (3.4) shows that hub-first elimination creates a discriminant direction whose determinant collapses exactly linearly in `q`; the target-valid family (5.1)-(5.5) shows that paying its absolute negative-half-power can lose a logarithm even while the actual output is uniformly bounded by three independent completed mechanisms.

Equation (4.1) separates this from the newest aggregate crossing mechanism: that currency is independent of `q` and survives the corrected family uniformly. Thus the genuinely difficult state is narrower than “small nonzero q”: it is small nonzero `q` **combined with original-coordinate partition degeneration** (notably the near-coloop/full-leaf-rank loss) where no uniformly positive `det(S_I)det(G_J)` has yet been forced.

The next B10 target is therefore

`QFORM-TWOSHEET-NEARNULL-NEARCOLOOP-JOINT-SMOOTHING-v1`:

retain the hub together with at least one transverse original-coordinate product resource in the two-sheet near-null/near-coloop state, and obtain a uniform `L^1_t` or linear small-ball estimate without first replacing the leaf geometry by the absolute expectation in (3.3), without a worst conditional-density supremum, without post-rotation independence, and without moment/support assumptions.

The newest `hub_with_diagonal` square-root-profile route and grouped/crossing Fourier route are compatible candidates, but no missing uniform partition/profile hypothesis is asserted here.

## 8. Scope and correction note

`CHECKPOINT.md` first used a four-row example whose two transverse rows had leverage one. That version correctly demonstrated the discriminant logarithm and ruled-side comparison but was not compatible with the designated partner r24 leverage gate. The immutable `CORRECTION.md` replaces it by the six-row construction (5.2). All partner and endpoint statements in this report use the corrected construction.

No full exact-rank-three theorem and no full QFORM theorem is claimed. Continuity is separate. No projected spectral coordinates were treated as independent; independence was used only after grouping disjoint ORIGINAL coordinate banks in Section 6.2.
