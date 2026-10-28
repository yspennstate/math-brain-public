SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B10, 2026-09-23T11:18:53.714323Z.
attacking: the single-null-hub three-bank packet receiver on the unpaid two-sheet side; aggregate the designated partner's S/Y/Z product banks before any local minor payment.

# account02/B10 — union-graph null-hub receiver and a punctured three-bank stress family

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Rank-three coupled case / complementary constructions and source-valid counterexamples  
**Run:** `20260923T111853Z-account02-B10-QFORM-auto11`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / LOCAL_CANDIDATE_REFUTED / FULL_QFORM_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** not claimed for the new endpoint; the theorem proves essential boundedness.

The unrestricted target remains OPEN: arbitrary independent original-coordinate densities bounded by one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, and no moment, support, log-concavity, diagonal-basis, identical-law, or post-rotation-independence assumption.

## 1. Source boundary and first unpaid implication

Fresh owner control was resolved from `yspennstate/math-research-brain` main at start commit

`d8ae9f823b044ecb1756fa6bca4c2bf9f66155c9`,


Required owner-pinned source package read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`,

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

The designated partner actually used is account03/B10 r23, canonical report commit

`yspennstate/math-open-problems@be74f28001070ca45728f51da989c89335e2803c`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260923T101459Z-account03-B10-QFORM-r23/REPORT.md`.

Its first unpaid implication was

`QFORM-NULL-HUB-THREEBANK-PACKET-TO-LINFINITY-v1`.

This report closes an exact bank-graph endpoint of that implication and shows by an exact target family that the partner packet alone does not give a zero-or-fixed-positive innovation dichotomy. The first unpaid statement after this run is stated in Section 7.

The completed dependence-safe receiver used below is account01/B11's `QFORM` null-scalar/arbitrary-pair theorem, source-pinned at a repository commit containing

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/QFORM-B11-20260922T211147Z/REPORT.md`.

The two-dimensional product-projection cap is the completed `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical source

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`.

All uses below preserve original-coordinate product provenance. In particular, no conditional projection-density cap is promoted to independence.

## 2. Required newest-Claude ruled theorem applied at its exact scope

For an exact rank-three form of signature `(2,1)`, the proved ruled-level-set theorem in the required `COUNTEREXAMPLE_SEARCH.md` gives the actual target inequality

`boxed: ess sup_(s>=0) p_Q(s) <= pi sqrt(2).`                         (2.1)

For signature `(1,2)` the sign-reversed half-line is paid. Thus the genuinely hard indefinite geometry in the present run is the convex/two-sheet half-line. Equation (2.1) is not used beyond that stated side.

## 3. Designated partner state and a new union-bank invariant

Use the exact-rank-three partner state

`A=R M R^T`, `R^T R=I_3`,                                           (3.1)

with

`D:=|det M|>=1`, `sigma_min(M)>=1`.                                 (3.2)

There is one ORIGINAL physical null hub

`u_0=sqrt(h) r`, `||r||=1`, `h>55/64`, `r^T M r=0`.                (3.3)

Additional rows exactly collinear with `r`, if present, are kept as a separate original-coordinate bank. Every remaining row belongs to a complementary bank `C` and is written

`u_j=t_j r+y_j`, `y_j in r^perp`,                                   (3.4)

with the exact Parseval identities

`sum_(j in C) y_j y_j^T=I_2`,
`sum_(j in C) t_j y_j=0`,
`sum_(j in C) t_j^2=rho`.                                           (3.5)

The designated partner applies account04/B10's completed three-bank split and produces a partition of ORIGINAL coordinates

`C=S disjoint_union Y disjoint_union Z`                              (3.6)

such that, with

`rho_S=sum_(i in S)t_i^2`,
`G_Y=sum_(j in Y)y_jy_j^T`,
`G_Z=sum_(k in Z)y_ky_k^T`,                                         (3.7)

and

`M_2(G_Y,G_Z)=tr(adj(G_Y)G_Z)
             =sum_(j in Y,k in Z) det(y_j,y_k)^2`,                  (3.8)

one has

`boxed: rho_S M_2(G_Y,G_Z) >= (2/81)rho.`                           (3.9)

Since `rho_S<=rho` and `rho>0` in the mixed survivor,

`boxed: M_2(G_Y,G_Z)>=2/81.`                                        (3.10)

This is the required equation-level use of the designated partner.

Put

`T:=Y disjoint_union Z`, `G_T:=G_Y+G_Z`.                             (3.11)

For two-by-two matrices,

`det(H+K)=det H+det K+tr(adj(H)K)`.                                  (3.12)

Therefore

`boxed: det G_T >= M_2(G_Y,G_Z) >=2/81.`                            (3.13)

Let `Y_T` denote the `|T| x2` matrix whose rows are `y_j^T`, and let `t_T=(t_j)_(j in T)`. Define the **union-bank longitudinal innovation**

`tau_T^2:=dist(t_T,col(Y_T))^2`.                                     (3.14)

Because (3.13) makes `Y_T` full column rank, `tau_T=0` exactly when there is a deterministic `a in r^perp` such that

`boxed: t_j=a dot y_j for every j in T.`                             (3.15)

The key point is that (3.15) is an identity of original-coordinate coefficient rows, not a regression statement about random variables after rotation.

## 4. New theorem: the union-graph endpoint is uniformly paid

### Theorem `QFORM-NULL-HUB-UNION-GRAPH-RECEIVER-v1`

In the state (3.1)--(3.14), if

`tau_T=0`,                                                           (4.1)

then `Q=X^TAX` has an essentially bounded density and

`boxed: ||p_Q||_infinity
 <=3*2^(2/3)*(9e/sqrt(2))^(2/3)*(64/55)^(1/3)
 <33.504.`                                                            (4.2)

No continuity assertion is made by this argument.

### Proof

Condition only on the ORIGINAL coordinates in `S` and on any additional exact `r`-collinear rows. This preserves the product law on the unconditioned coordinates. All conditioned variables contribute only an affine spectral shift.

The remaining random sources are:

1. the original hub scalar `X_0`, whose density cap is one;
2. the whole original-coordinate bank `T`, summarized by its transverse two-dimensional projection

`P_T:=sum_(j in T)y_jX_j in r^perp`.                                 (4.3)

These two sources are genuinely independent because their original-coordinate supports are disjoint.

Normalize the transverse coefficient matrix by

`R_T:=Y_T G_T^(-1/2)`, so `R_T^T R_T=I_2`.                          (4.4)

The completed weighted affine-fiber Brascamp--Lieb theorem gives the orthonormal product projection `G_T^(-1/2)P_T` a joint density cap at most `e`. Undoing the deterministic linear map and using (3.13),

`||p_(P_T)||_infinity
 <=e/sqrt(det G_T)
 <=e sqrt(81/2)
 =9e/sqrt(2).`                                                       (4.5)

Under (4.1), relation (3.15) gives an exact random-variable identity on the whole bank,

`sum_(j in T)t_jX_j = a dot P_T`.                                    (4.6)

Choose an orthonormal basis of `r^perp`. In variables `(x,p) in R x R^2`, the homogeneous spectral contribution of the unconditioned sources is the invertible linear map

`B(x,p)=sqrt(h)x r+(a dot p)r+p`.                                    (4.7)

Its matrix is triangular in the decomposition `Rr direct_sum r^perp`, hence

`det B=sqrt(h)`.                                                      (4.8)

The homogeneous conditional quadratic matrix is

`H=B^T M B`.                                                         (4.9)

Since the hub is null,

`H_xx=h r^TMr=0`,                                                     (4.10)

while

`|det H|=(det B)^2 |det M|=hD>=55/64`.                              (4.11)

Now apply account01/B11's completed dependence-safe null-scalar/arbitrary-pair theorem to the genuinely independent scalar `X_0` and dependent pair `P_T`. That theorem requires no independence inside the pair and permits arbitrary affine terms. With scalar cap `L=1`, pair cap from (4.5), and determinant (4.11), it yields

`||p_(Q | conditioned original banks)||_infinity
 <=3*2^(2/3)(L M_pair)^(2/3)|det H|^(-1/3)`
` <=3*2^(2/3)*(9e/sqrt(2))^(2/3)*(64/55)^(1/3)`
` =33.5038726325... .`                                                (4.12)

The estimate is uniform in every conditioned original-coordinate value. Averaging those conditional laws proves (4.2). QED.

### Why this does not trigger the live dependence correction

The scalar and pair in Theorem 4 are not dependent spectral coordinates. `X_0` is one untouched ORIGINAL coordinate, while `P_T` uses a disjoint ORIGINAL bank. The internal components of `P_T` are left dependent and are paid only through their joint density cap. No statement of the form “bounded conditional density implies independence” is used.

## 5. Exact punctured target family: the packet does not force an innovation gap

The next construction shows that the numerical packet (3.9) cannot by itself imply either `tau_T=0` or `tau_T>=c_0` for one universal `c_0>0`, even inside exact target matrices with a true near-unit null hub and collapsing local certificates.

### Construction `QFORM-THREEBANK-PACKET-PUNCTURED-INNOVATION-FAMILY-v1`

Fix an even integer `m>=8`. Let `(r,v,w)` be an orthonormal basis of `R^3`, put

`rho=1/m`, `h=1-rho`, `epsilon=1/m`,                                (5.1)

and choose signs `sigma_1,...,sigma_m in {+1,-1}` with

`sum_j sigma_j=0`.                                                    (5.2)

Define physical frame rows as follows.

Hub:

`u_0=sqrt(h) r`.                                                       (5.3)

Bank `Y`, `m` rows:

`u_j^Y=(sigma_j epsilon/sqrt(m)) r + sqrt(3/(4m)) v`.                 (5.4)

Bank `Z`, `m` rows:

`u_j^Z=sqrt(3/(4m)) w`.                                               (5.5)

Bank `S_v`, `m` rows:

`u_j^(S_v)=sigma_j sqrt((rho-epsilon^2)/m) r + (1/(2sqrt(m)))v`.      (5.6)

Bank `S_w`, `m` rows:

`u_j^(S_w)=(1/(2sqrt(m)))w`.                                         (5.7)

Take `S=S_v disjoint_union S_w`. By (5.2), all longitudinal/transverse cross sums vanish. The three diagonal Parseval ledgers are

`r: h+epsilon^2+(rho-epsilon^2)=1`,
`v: 3/4+1/4=1`,
`w: 3/4+1/4=1`.                                                       (5.8)

Hence the full row matrix `R_m` satisfies exactly

`R_m^T R_m=I_3`.                                                      (5.9)

Use the fixed symmetric spectral matrix

`M_0=[[0,1,0],[1,0,0],[0,0,1]]`.                                    (5.10)

It has spectrum `{-1,1,1}` and operator norm one. Therefore

`A_m=R_m M_0 R_m^T`                                                   (5.11)

is an exact target matrix with nonzero spectrum exactly `{-1,1,1}`. The hub is exactly null because `r^TM_0r=0`, and

`h=1-1/m>=7/8>55/64`.                                                (5.12)

Every complementary transverse row has squared transverse norm at most `3/(4m)<1/2`, so the family lies in the residual-diffuse heavy-null geometry.

### 5.1 The designated-partner packet is uniformly strong

For the displayed partition,

`G_Y=(3/4)vv^T`, `G_Z=(3/4)ww^T`,                                   (5.13)

so

`M_2(G_Y,G_Z)=9/16`,                                                  (5.14)

while

`rho_S=rho-epsilon^2=1/m-1/m^2`.                                    (5.15)

Thus

`rho_S M_2(G_Y,G_Z)
 =(9/16)(1/m-1/m^2)
 >2/(81m)
 =(2/81)rho`                                                         (5.16)

for every `m>=8`. This is much stronger than the partner threshold.

Moreover

`G_T=G_Y+G_Z=(3/4)I_2`, `det G_T=9/16`.                              (5.17)

### 5.2 Yet the union innovation is positive and tends to zero

On `T=Y disjoint_union Z`, the longitudinal coefficient vector is supported only on `Y` and has entries

`sigma_j epsilon/sqrt(m)`.                                           (5.18)

The two columns of `Y_T` are constant on the `Y` block and on the `Z` block respectively. By (5.2), the vector (5.18) is orthogonal to both columns. Hence

`boxed: tau_T^2=epsilon^2=1/m^2`,
`boxed: tau_T=1/m>0 ->0.`                                            (5.19)

Therefore a constant three-bank transverse packet does not create a zero-or-uniformly-positive union-innovation alternative.

### 5.3 Every fixed local physical certificate collapses

For `m>=8`, every nonhub row above has

`||u_j||^2<=1/m`.                                                     (5.20)

Because `||M_0||=1`, every nonhub physical scalar pivot satisfies

`|A_jj|<=1/m`,                                                        (5.21)

while the hub pivot is exactly zero.

Since `||wedge^2 M_0||=1`, for any physical pair `(i,j)`,

`|det A_m[{i,j},{i,j}]|
 <=||u_i wedge u_j||^2
 <=||u_i||^2||u_j||^2`.                                              (5.22)

Thus a hub/nonhub pair has determinant `<1/m`, and a nonhub/nonhub pair has determinant at most `1/m^2`.

For a physical triple `I`, exact rank three gives

`|det A_m[I,I]|=|det M_0| det(R_{m,I})^2
               <=product_(i in I)||u_i||^2`.                        (5.23)

Hence a triple containing the hub is `<1/m^2`, and an all-nonhub triple is at most `1/m^3`.

So scalar pivots, pair determinants, and principal triples all vanish locally even though the aggregate partner packet stays constant. This is a route counterexample, not a counterexample to QFORM.

The required ruled theorem still pays the one-sheet side of every member of this family:

`ess sup_(s>=0) p_(X^T A_m X)(s)<=pi sqrt(2)`                       (5.24)

for every admissible product law. The possible difficulty remains only on the two-sheet side.

## 6. Relation to the current innovation bridge

The completed residual-diffuse work elsewhere shows two complementary facts for heavy-null frames: an exact zero bank innovation can be paid by a null-scalar/dependent-pair receiver, while a genuinely rank-three cross block can be paid away from its singular-volume puncture. Those estimates do not remain uniform merely by sending a positive innovation coefficient to zero, because the source laws have no moment or support bound.

Theorem 4 adds a different exact endpoint tied directly to the designated partner's `S/Y/Z` packet: if the **union** `Y sqcup Z` is one common transverse graph, it is uniformly paid at `<33.504`, regardless of the graph slope. Construction 5 shows that the packet can approach this graph endpoint through positive innovations while every local certificate collapses.

## 7. First unpaid implication after this run

The first unpaid statement is now

`QFORM-NULL-HUB-PUNCTURED-UNION-INNOVATION-v1`:

> In the designated-partner state (3.1)--(3.14), prove a universal essential density bound on the convex/two-sheet side when `tau_T>0`, uniformly as `tau_T downarrow0`, using the disjoint ORIGINAL banks `X_0`, `S`, `Y`, `Z` before any collapse to dependent spectral coordinates. The receiver must retain the same-bank longitudinal/transverse contamination and may not perturbatively delete the innovation, take a worst conditional projection-density supremum, or replace bounded conditional density by independence.

The exact endpoint `tau_T=0` is now paid by Theorem 4. The ruled half-line is already paid by (2.1). Construction 5 shows that a quantitative gap `tau_T>=c_0` cannot be inferred from the partner packet alone.

## 8. Integrity summary

- Full QFORM: **OPEN**.
- New result: `QFORM-NULL-HUB-UNION-GRAPH-RECEIVER-v1`, essential density `<33.504`.
- Designated partner account03/B10 used at equations (3.9)--(3.13), not citation-only.
- Required newest-Claude ruled theorem used at equations (2.1) and (5.24), only on its proved one-sheet side.
- Exact target-valid structural stress family: Section 5, spectrum `{-1,1,1}`.
- Product provenance: every conditioning is on disjoint original-coordinate banks; no post-rotation independence.
- No hidden moments/support/log-concavity assumptions.
- Native brain ingestion/receiver use was not authenticated: `WITHOUT_VERIFIED_BRAIN`.
- No task/schedule state, notification/email setting, public workflow, paid call, permission, or cross-account native action was changed.
