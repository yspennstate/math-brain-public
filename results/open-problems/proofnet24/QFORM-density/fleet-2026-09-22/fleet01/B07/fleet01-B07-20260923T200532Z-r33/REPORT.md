SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B07, 2026-09-23T20:05:32Z.
attacking: turn the partner's physical rank-two Frobenius tube into an aggregate Pluecker determinant dichotomy that either pays by the existing E2 receiver or forces a finite family of physical star/projected-cross hubs, without selecting or reciprocating a tiny minor.

# fleet01/B07 r33 — rank-one-update compound shadow for the rank-two tube

Status: `NEW_EXACT_COMPOUND_SHADOW / NEW_FOUR-DISTRIBUTION_HUB_DECONVOLUTION / DESIGNATED_PARTNER_APPLIED / FULL_QFORM_OPEN / WITHOUT_VERIFIED_BRAIN`.

The unrestricted QFORM conjecture and the requested global continuity conclusion remain open. All coordinates below are ORIGINAL physical coordinates. Orthogonal projections used below are deterministic coefficient-space operations only; no random variables are rotated and no independence is asserted after rotation.

## 1. Incoming completed partner theorem

Use the completed fleet02/B07 theorem from
`yspennstate/math-open-problems@5ff9d960bffec400a9d6db422401e4c4df98ce6d`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260923T150720Z-fleet02-B07-qform/REPORT.md`.

For a physical cross block

`M=[[s^T,r^T],[C,K]]`, `S=||s||_2>0`,

it proves the exact identity

`G_* = sum_j s_j^2 E2(K_j)`,
`K_j=K-C[:,j]r^T/s_j`,

and, at `eps=1/8`, the alternative

`G_* >= S^2 Omega/8192`                                      (1.1)

or

`dist_F(K,rank<=2)<Omega^(1/4)/8`,                            (1.2)

for every `Omega<=E2(K)`. The first branch is already an aggregate third-volume branch. I study the second branch, but I retain the exact pivot-averaging provenance rather than merely using the existence of an abstract rank-two approximant.

Assume from now on that the first branch fails and take `Omega=E2(K)>0`. Since

`G_*/S^2 = sum_j (s_j^2/S^2) E2(K_j) < Omega/8192`,

there exists an ACTUAL physical star coordinate `j` with `s_j!=0` such that

`g:=E2(H)<Omega/8192`, `H:=K_j`.                              (1.3)

Write

`a=C[:,j]/s_j`, so that exactly `K=a r^T+H`.                   (1.4)

No reciprocal `1/s_j` will appear in any analytic density estimate below; it is used only to express the exact deterministic coefficient decomposition selected by determinant-weight averaging.

## 2. Exact second-compound decomposition

For a matrix `L`, let `C2(L)` denote its second compound, indexed by physical row pairs and physical column pairs. Put

`D=C2(K)`, `U=C2(H)`, `T=D-U`.                                (2.1)

Because `a r^T` has rank one, every 2x2 determinant of `K=a r^T+H` contains either two H entries or exactly one rank-one entry. Thus

`D=T+U`                                                        (2.2)

exactly.

Define coefficient-space orthogonal projections

`P_a=I-aa^T/||a||^2`, `P_r=I-rr^T/||r||^2`,
`Z=P_a H P_r`.                                                 (2.3)

On the present branch `a`, `r`, and `Z` are nonzero: if any vanished then `T=0`, hence `D=U` and `Omega=g`, contradicting (1.3).

For a vector `v`, let `L_v x=v wedge x`. Then the cross compound is

`T=L_a Z L_r^*`.                                               (2.4)

Indeed, for row pair `{i,k}` and column pair `{p,q}`,

`T_{ik,pq}`
`=(a_i Z_{kq}-a_k Z_{iq})r_p-(a_i Z_{kp}-a_k Z_{ip})r_q`,      (2.5)

which is unchanged if H is replaced by `P_a H P_r`, because wedge multiplication kills components parallel to `a` and `r`.

Since `a^T Z=0` and `Zr=0`, the standard wedge identity

`||v wedge x||^2=||v||^2||x||^2-<v,x>^2`

gives the exact norm formula

`boxed: ||T||_F^2=||a||^2 ||r||^2 ||Z||_F^2.`                 (2.6)

This is the rank-one-update compound shadow. It is an exact aggregate identity, not a selected-minor estimate.

## 3. Dimension-free stability of the complete physical E2 determinant law

Normalize the actual complete determinant law of K by

`W(R,C)=D_{R,C}^2/Omega`,                                      (3.1)

where `Omega=||D||_F^2=E2(K)`. Normalize the compound shadow by

`W_T(R,C)=T_{R,C}^2/||T||_F^2`.                               (3.2)

### Lemma 3.1 — normalized-squares TV inequality

For any two nonzero real arrays x,y, if `p_i=x_i^2/||x||_2^2` and `q_i=y_i^2/||y||_2^2`, then

`d_TV(p,q) <= ||x/||x||-y/||y||||_2 <= 2||x-y||_2/||x||_2`.    (3.3)

Proof. With normalized arrays u,v,

`1/2 sum_i |u_i^2-v_i^2|`
`<=1/2 ||u-v||_2 ||u+v||_2 <= ||u-v||_2`.

Also

`||x/||x||-y/||y||||`
`<=||x-y||/||x|| + | ||y||-||x|| |/||x||`
`<=2||x-y||/||x||`. QED.

Apply the lemma with `x=D`, `y=T` and `D-T=U`. Since `||U||_F^2=E2(H)=g`,

`boxed: d_TV(W,W_T) <= 2 sqrt(g/Omega).`                        (3.4)

By (1.3),

`boxed: d_TV(W,W_T)<1/(32 sqrt(2))=0.0220970869121... .`        (3.5)

This estimate is dimension-free and, unlike a generic Frobenius-near-rank-two statement, contains no operator-norm amplification. The reason is that the approximating compound is inherited from the exact physical star pivot.

## 4. Exact physical marginal factorization of the shadow

Define four probability vectors on ORIGINAL physical indices:

left star:      `p_i=a_i^2/||a||^2`,
left projected: `q_i=||Z[i,:]||_2^2/||Z||_F^2`,
right star:     `p'_k=r_k^2/||r||^2`,
right projected:`q'_k=||Z[:,k]||_2^2/||Z||_F^2`.              (4.1)

Let `alpha_i^T` be the inclusion probability of physical row i in the row pair under `W_T`, and `beta_k^T` the analogous column inclusion probability. Then

`boxed: alpha_i^T=p_i+q_i,   beta_k^T=p'_k+q'_k.`              (4.2)

Proof for rows. For a fixed physical pair `{i,l}`, the row of T across all column pairs is the wedge of `r` with

`v_{il}=a_i Z[l,:]-a_l Z[i,:]`.

Because `Zr=0`,

`sum_C T_{il,C}^2=||r||^2 ||v_{il}||^2`.

Summing over `l!=i`, using `a^T Z=0`, gives

`sum_{l!=i}||v_{il}||^2`
`=a_i^2||Z||_F^2+||a||^2||Z[i,:]||^2`.                        (4.3)

Divide by (2.6). The column formula is the transpose argument. QED.

Since total variation controls every event, if `alpha_i`, `beta_k` are the actual inclusion marginals under W, then

`alpha_i <= p_i+q_i+d_TV(W,W_T)`,
`beta_k <= p'_k+q'_k+d_TV(W,W_T)`.                             (4.4)

Therefore if all four one-coordinate probability vectors have maximum at most `3/16`, then by (3.5)

`boxed: max_i alpha_i, max_k beta_k`
`<3/8+1/(32sqrt(2))`
`=0.397097086912... <2/5.`                                     (4.5)

Conversely, failure of this four-vector diffuseness produces an explicit original-coordinate hub in one of `a`, the row energy of Z, `r`, or the column energy of Z. Each one of the four probability vectors has at most five coordinates with mass strictly greater than `3/16`.

This is the promised hub deconvolution: the near-rank-two determinant tube is reduced to a finite set of literal physical-coordinate star/projected-cross hubs unless its *actual* E2 determinant law is diffuse enough for the existing receiver.

## 5. Apply the completed fleet01/B07 E2 receiver

Use the completed r32 theorem `QFORM-E2-DIFFUSE-CROSSPAY-OR-FOURHUB-SCHUR-TUBE-v1` from
`yspennstate/math-open-problems@4c25b2dd7287d7fb03c84c588d34ff058e37f556`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B07/fleet01-B07-20260923T193206Z-r32/SCHUR_TUBE_ADDENDUM.md`.

By (4.5) its hypotheses hold with `a=b=2/5`. Taking the receiver parameter `epsilon=1/2`, either the full ambient quadratic form has a continuous density with

`||p_Q||_inf`
`<=C_E3 [Omega ||K||_F^2/1280]^(-1/6)`,                        (5.1)

where `C_E3=3*2^(4/3)*e^(1/3)`, or one actual physical 2x2 anchor selected after determinant aggregation yields the relative four-hub Schur tube of r32.

Since

`Omega=e2(KK^T)<=||K||_F^4/2`,

we have `||K||_F^2>=sqrt(2Omega)`, and the payment simplifies to

`boxed: ||p_Q||_inf <=32.8126952405 Omega^(-1/4).`              (5.2)

This branch is continuous because the r32 receiver is an L1-characteristic-function argument.

Combining Sections 1-5 gives the new theorem.

### Theorem 5.1 — `QFORM-STAR-R2TUBE-COMPOUND-SHADOW-v1`

In the completed fleet02/B07 star/E2 state with `Omega=E2(K)>0`, after the regenerated-E3 branch (1.1) is removed, one of the following holds:

1. one of the four original-coordinate probability vectors in (4.1) has a physical hub of mass `>3/16` (hence at most five candidate coordinates for that vector);
2. the full ambient QFORM has a continuous density satisfying (5.2);
3. the actual physical cross block enters the r32 four-hub relative rank-two Schur tube, with its true nonzero residual retained.

No individual small determinant is reciprocated in branches 1 or 2. The pivot in branch 3 appears only after determinant-weighted aggregation, exactly as in the r32 theorem.

## 6. Actual numerical application to the designated partner scale

The completed fleet02/B07 carrier report
`yspennstate/math-open-problems@12da18e77ea3c2097023c2da5193c86ef3b6478c`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260923T183825Z-fleet02-B07-qform-r11/REPORT.md`
records the actual physical lower bound

`Omega>854675.100194511 h^4`,
`h=(2sqrt(2)-1)/1572864=1.1624826588606455e-6`.                (6.1)

Therefore branch 2 of Theorem 5.1 gives the concrete continuous full-form estimate

`boxed: ||p_Q||_inf <928335.929.`                              (6.2)

Thus, on the partner's rank-two-carrier side, the only states not paid by this step are now explicit finite physical hubs in the star/projected-cross factors, or the already-identified four-hub Schur tube. This applies a completed partner inequality to an actual density bound, as required by the assignment.

## 7. Independent exact E2 marginal identity

For later hub selection, let `G=KK^T`, `E=tr G=||K||_F^2`, `Omega=e2(G)`. The complete E2 determinant-law row marginal has the exact original-coordinate formula

`boxed: alpha_i=[G_ii E-(G^2)_ii]/Omega.`                      (7.1)

Proof: sum all squared 2x2 minors using row i; by Cauchy-Binet this is

`sum_{l!=i} det G[{i,l},{i,l}]`
`=G_ii(E-G_ii)-sum_{l!=i}G_il^2`
`=G_ii E-(G^2)_ii`.

If `x_s` are squared singular values and `u_s` left singular vectors, define

`theta_s=x_s(E-x_s)/(2Omega)`, `sum_s theta_s=1`.               (7.2)

Then

`boxed: alpha_i=2 sum_s theta_s u_s(i)^2.`                     (7.3)

In exact rank two, `theta_1=theta_2=1/2`, so alpha is exactly the leverage vector of the physical two-plane. In particular any actual determinant hub satisfies the concrete coefficient lower bound

`alpha_i>c  =>  ||K[i,:]||_2^2 > c Omega/E`.                   (7.4)

The column formulas are identical for `K^T`.

## 8. Scope and remaining implication

This report uses no Gaussianity, moments, compactness, connected support, log-concavity, iid law, diagonal-basis assumption, or rotated independence. It does not infer density control from a bounded projection alone. It does not use the refuted uniform pointwise van-der-Corput claim. The fresh logarithmic tube correction is compatible: no rough nonzero coefficient tail is discarded here.

Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Global continuity remains OPEN; continuity is proved only in branch 2 above.

First remaining B07 implication:

`QFORM-FOURDIST-HUB-OR-FOURHUB-SCHUR-RECEIVER-v1` — consume the finite physical hub states in `a`, the row-energy law of Z, `r`, or the column-energy law of Z, and the r32 four-hub Schur tube, while retaining arbitrary same-bank curvature and every nonzero residual direction. A natural next split is collision of left/right hub sets (finite physical core) versus disjoint hub supports (mixed-Fresnel/cross-volume receiver).
