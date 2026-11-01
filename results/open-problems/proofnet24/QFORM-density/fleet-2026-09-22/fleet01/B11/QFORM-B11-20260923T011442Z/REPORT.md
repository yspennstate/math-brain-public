SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B11, 2026-09-23T01:14:42Z.
attacking: the exact-rank-three zero-diagonal indefinite chamber by projective-null-conic canonicalization, a uniform hub half-potential, and the newest fractional-volume exit.

# fleet01/B11 — projective conic normal form and a uniform half-potential in the null chamber

Programme: QFORM-DENSITY-3EIG-20260922  
Owner control read at start: revision 2026-09-22.15  
Run: QFORM-B11-20260923T011442Z  
Status: **ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREMS / FULL_TARGET_OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

## 1. Exact scope and compact conditional proof map

The full target is still open. This report attacks the exact-rank-three indefinite zero-diagonal chamber, which is the singular limit left after scalar/pair-pivot exits.

Let

    A = R M R^T,      R^T R = I_3,

where M is invertible of inertia (2,1) or (1,2), and put

    s = min |lambda(M)|.

Assume in Sections 2--7 that

    A_ii = 0 for every original coordinate i.                 (1.1)

No rotation of the independent random variables is made anywhere below.

The end-to-end conditional map after this run is:

1. If a usable physical scalar/pair pivot exists, previously completed scalar/pair theorems apply.
2. In the exact zero-diagonal chamber, fleet02/B11's completed D0 theorem gives either a quantitative product-preserving rank-three cross cut or a heavy original null hub.
3. Applying the newest fractional-volume theorem D' to that exact partner cut shows that every cut for which one oriented side has rank-three volume marginal at most 2/3 is already paid by an explicit continuous-density estimate.
4. When D0 <= 1/2, the partner theorem gives a hub leverage c_h >= 1/6. The new projective conic theorem below turns the complete zero-diagonal form into a determinant of three ORIGINAL-coordinate linear aggregates and identifies the third direction exactly as a weighted projective variance.
5. Independently of how badly the residual variables overlap, the hub produces a uniform one-sided half-potential bound. This uses the scalar projection theorem and fleet03/B11's translation-stable half-potential theorem, with fleet02/B11's leverage lower bound inserted at an actual inequality.
6. What remains is a sharply localized double-coloop/overlap implication: convert the uniform half-potential plus forced projective variance and a two-sided high-leverage rank-three cross cut into an L-infinity density estimate without pretending that the residual square direction is independent.

The full arbitrary-rank theorem and continuity in this remaining chamber are not proved here.

## 2. New theorem: projective-null-conic canonicalization

### Theorem 2.1 (`QFORM-NULL-PROJECTIVE-CONIC-v1`)

Under (1.1), there are signs d_i in {+1,-1}, nonzero vectors

    q_i = (u_i,v_i) in R^2,

and epsilon in {+1,-1} depending only on the inertia orientation, such that after the ORIGINAL-coordinate reflections

    Y_i = d_i X_i,

which preserve independence and preserve every density cap <=1,

    (D A D)_ii = 0,
    epsilon (D A D)_ij = det(q_i,q_j)^2          (i != j).      (2.1)

Consequently, if

    L_20 = sum_i u_i^2 Y_i,
    L_11 = sum_i u_i v_i Y_i,
    L_02 = sum_i v_i^2 Y_i,

then the quadratic form has the exact determinant representation

    epsilon Q = 2 (L_20 L_02 - L_11^2)
              = 2 det [[L_20,L_11],[L_11,L_02]].                (2.2)

Equivalently, every exact-rank-three indefinite zero-diagonal matrix is switching-equivalent to a squared projective-distance kernel on RP^1.

### Proof

Put

    J = [[0,0,1],[0,-2,0],[1,0,0]].

The quadratic form z^T J z equals 2(z_0 z_2-z_1^2), so J has inertia (1,2). By Sylvester's law there are an invertible T and epsilon in {+1,-1} such that

    M = epsilon T^T J T.                                       (2.3)

For the i-th row r_i of R set z_i=T r_i. Since A_ii=r_i^T M r_i=0,

    z_i^T J z_i=0,

or z_{i0} z_{i2}=z_{i1}^2. Identifying z=(x,y,z) with the rank-one symmetric matrix [[x,y],[y,z]], every nonzero real solution is a signed rank-one square. Hence for some q_i=(u_i,v_i) !=0 and d_i in {+1,-1},

    z_i = d_i nu(q_i),       nu(u,v)=(u^2,uv,v^2).             (2.4)

A direct multiplication gives the key identity

    nu(q)^T J nu(q') = det(q,q')^2.                            (2.5)

Therefore

    A_ij = r_i^T M r_j
         = epsilon d_i d_j det(q_i,q_j)^2.

Conjugating A by D=diag(d_i) proves (2.1). Expanding

    2(L_20 L_02-L_11^2)

cancels every diagonal Y_i^2 term; the coefficient of Y_iY_j, i<j, is

    2[u_i^2 v_j^2+u_j^2 v_i^2-2u_i v_i u_j v_j]
      =2 det(q_i,q_j)^2,

which proves (2.2). Only sign reflections of the original variables were used. QED.

### Immediate exact identities

For every triple i,j,k,

    det[nu(q_i);nu(q_j);nu(q_k)]
      = det(q_i,q_j) det(q_i,q_k) det(q_j,q_k).                (2.6)

Thus every nonzero physical triangle has the same switched sign, and

    det A_{ijk}
      = 2 epsilon det(q_i,q_j)^2 det(q_i,q_k)^2 det(q_j,q_k)^2. (2.7)

Every nonzero physical 2x2 principal pair remains an opposite-sign saddle:

    det [[0,A_ij],[A_ij,0]] = -A_ij^2.                         (2.8)

So (2.1) does not erase the rank-two logarithmic obstruction; it identifies its exact projective geometry.

## 3. Hub chart and the exact third-direction variance

Fix an original coordinate h. An SL(2,R) change of all q_i preserves every determinant det(q_i,q_j), so choose a chart with

    q_h=(0,1).                                                  (3.1)

For every active residual coordinate j with A_hj !=0, write

    q_j = u_j(1,t_j),
    rho_j = u_j^2 = |A_hj|.                                    (3.2)

Coordinates projectively parallel to q_h have A_hj=0 and can be kept separately. For active j,k, (2.1) gives the exact original-coordinate relations

    |A_hj| = rho_j,
    |A_jk| = rho_j rho_k (t_j-t_k)^2.                          (3.3)

Let

    a=A_{-h,h},   B=A_{-h,-h},
    W=||a||_2^2=sum_j rho_j^2,
    pi_j=rho_j^2/W.                                             (3.4)

The previous B11 null-ruling theorem proved

    a^T B a = det(M)c_h,
    u^T B u has the minority inertia sign and |u^T B u|>=s/2,
    u=a/sqrt(W),                                                (3.5)

where c_h=||r_h||^2 is the spectral leverage of the ORIGINAL hub.

Substituting (3.3) into a^TBa gives a new exact interpretation:

    a^T B a
      = 2 epsilon sum_{j<k} rho_j^2 rho_k^2 (t_j-t_k)^2
      = 2 epsilon W^2 Var_pi(t).                               (3.6)

Therefore

    u^T B u = 2 epsilon W Var_pi(t),                            (3.7)

and the matched-curvature lower bound (3.5) becomes

    **W Var_pi(t) >= s/4.**                                    (3.8)

This is the cleanest structural answer obtained so far to "what does the third direction do?" In the rank-two saddle all active residual projective slopes may collapse to one value, so this variance vanishes and the logarithmic singularity survives. Exact rank three forces a quantitatively nonzero projective variance in the same original-coordinate hub chart.

A second useful exact form of (2.2), in the chart (3.1), is

    epsilon Q = 2[S Z - T^2],                                  (3.9)

where

    S=sum_j rho_j Y_j,
    T=sum_j rho_j t_j Y_j,
    Z=Y_h + sum_j rho_j t_j^2 Y_j + (parallel-ray terms).       (3.10)

The only genuinely independent scalar in (3.9) is the ORIGINAL hub Y_h. The other three aggregates may be strongly dependent; no independence among S,T and the residual part of Z is asserted.

## 4. New corollary: small residual physical pairs force large projective effective support

Assume for a fixed hub that

    |A_jk| <= delta s          for every active residual j != k. (4.1)

Using (3.3),

    rho_j^2 rho_k^2 (t_j-t_k)^2
      = rho_j rho_k |A_jk|
      <= delta s rho_j rho_k.

Since

    W Var_pi(t)
      = (1/W) sum_{j<k} rho_j^2 rho_k^2(t_j-t_k)^2,

(3.8) gives

    s/4 <= (delta s/W) sum_{j<k}rho_jrho_k
         = (delta s/(2W))[(sum_j rho_j)^2-W].

Hence

    **(sum_j rho_j)^2/W >= 1 + 1/(2 delta).**                  (4.2)

This is an exact dimension-free many-small-support consequence of the third-direction curvature. It is different from the previously known star-energy/max-edge effective-support bound.

## 5. Assigned partner fleet02/B11 applied to an actual inequality

Required partner source actually used:

    yspennstate/math-open-problems
    commit e47740cfec219112c826613bec5785af4b96cf3
    proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B11/
      20260922T233948Z-fleet02-B11-QFORM-b35bb6c3/REPORT.md

That completed theorem defines the disjoint-volume statistic D0 and proves

    max_i c_i >= (1-D0)/3,                                    (5.1)

and also gives an original-coordinate cut with

    sigma_3(A[S,S^c]) >= s sqrt(D0)/8.                         (5.2)

### 5.1 Uniform half-potential in the small-D0 chamber

Assume D0<=1/2. By (5.1) choose an ORIGINAL hub h with

    c_h >= (1-D0)/3 >= 1/6.                                   (5.3)

Its star slope in the chart above is

    S=sum_j rho_jY_j,
    ||rho||_2=sqrt(W)=||A_{h,-h}||_2.

The exact zero-diagonal star identity gives

    W=(A^2)_hh=r_h^T M^2 r_h >= s^2 c_h.                      (5.4)

The one-dimensional Rogozin--Ball/Rudelson--Vershynin projection bound gives

    ||p_S||_infinity <= sqrt(2)/sqrt(W).                       (5.5)

Now use fleet03/B11's completed translation-stable half-potential theorem from

    yspennstate/math-open-problems@633e2442f30ae1848ba02e37eecc735d2f22b12e
    proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/
      20260923T004154Z-fleet03-B11-QFORM-r20/REPORT.md.

It says that for

    R=2 a Z S+H,

with Z independent of (S,H), density caps p_Z<=L and p_S<=K, while H may depend arbitrarily on S,

    sup_t E (t-R)_+^{-1/2}, sup_t E (R-t)_+^{-1/2}
       <=4 sqrt(LK/|a|).                                      (5.6)

Apply (5.6) directly to (3.9) with Z=Y_h, |a|=1, L=1, and with **all** residual self-coupling, including -2T^2, absorbed into H. This is legitimate because Y_h is an untouched ORIGINAL variable and is independent of every residual coordinate. Equations (5.3)--(5.5) give

    H_{1/2,+}(Q), H_{1/2,-}(Q)
      <=4*2^(1/4)*W^(-1/4)
      <=4*(6/(1-D0))^(1/4) s^(-1/2).                          (5.7)

In particular, throughout D0<=1/2,

    **H_{1/2,+}(Q), H_{1/2,-}(Q)
       <=4*12^(1/4) s^(-1/2) <7.445 s^(-1/2).**               (5.8)

This is a genuine uniform estimate as D0 tends to zero. It is not yet an L-infinity density bound; the missing operation is to make the projective-variance curvature pay this half-potential without falsely declaring it independent of S.

## 6. Newest Claude/fractional-volume source applied to the partner cut

The owner-required newest analytic source is the proved D' extension in

    yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837
    proofnet24/QFORM-density/interactive/
      20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md

and the current volume-stability continuation at

    yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba
    proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/.

For a cross block C and rank-three volume-sampling row marginals alpha_i<=h<3/4, D' proves

    ||p_Q||_infinity
      <=6 sqrt(e)(2h)^(-1/2)(3-4h)^(-1) Z^(-1/6),             (6.1)

with Z=e_3(C^TC). For an exact-rank-three cross block, the row marginals are precisely the diagonal leverages of its left singular subspace; transposing C exchanges the two sides.

Insert the partner cut (5.2). Since

    Z=sigma_1(C)^2 sigma_2(C)^2 sigma_3(C)^2 >= sigma_3(C)^6,

we have

    Z^(-1/6) <= 8/(s sqrt(D0)).                               (6.2)

Take h=2/3. If **either orientation** of the partner cut has every rank-three volume marginal <=2/3, orient that side as the constrained D' side. From (6.1)--(6.2),

    **||p_Q||_infinity
       <=72 sqrt(3e)/(s sqrt(D0))
       <205.609/(s sqrt(D0)).**                               (6.3)

This D' exit has a continuous density because its proof gives an integrable characteristic function.

Therefore every still-unpaid positive-D0 partner cut must have, on both sides, a rank-three range-projection leverage strictly greater than 2/3. For exact rank three this is an exact original-frame statement: if G_S=sum_{i in S} r_i r_i^T, then there exist i in S and j in S^c with

    r_i^T G_S^{-1}r_i >2/3,
    r_j^T (I-G_S)^{-1}r_j >2/3.                               (6.4)

By the matrix determinant lemma, each is a genuine volume coloop:

    det(G_S-r_ir_i^T) < (1/3)det G_S,
    det((I-G_S)-r_jr_j^T) < (1/3)det(I-G_S).                  (6.5)

So the unresolved cross-cut branch is now two-sided near-coloop, not merely an arbitrary nondiffuse cross block.

## 7. Rank-two logarithmic control is retained exactly

Let X,Y be independent Uniform[-1/2,1/2]. Their densities equal one. For U=2XY,

    p_U(t)=log(1/(2|t|)),        0<|t|<1/2.                    (7.1)

Thus the opposite-sign rank-two saddle has a genuinely unbounded logarithmic density. The present result does not hide that singularity. The new rank-three mechanism is instead:

- the hub product supplies a uniform half-potential, (5.8);
- exact rank three forces nonzero projective curvature, (3.8);
- diffuse rank-three cross volume gives the paid continuous-density exit, (6.3);
- the remaining obstacle is precisely the dependence between the forced projective curvature and the hub slope in the two-sided coloop regime.

This is consistent with the live correction that bounded scalar densities do not yield law-uniform pointwise quadratic-phase decay.

## 8. First essential missing implication

Name:

    QFORM-NULL-DOUBLE-COLOOP-PROJECTIVE-TRACE-v1.

Hypotheses after all exits above:

1. exact-rank-three indefinite, zero physical diagonal;
2. 0<D0<=1/2;
3. partner heavy hub c_h>=1/6 and the uniform half-potential (5.8);
4. exact projective determinant form (2.2) and hub variance W Var_pi(t)>=s/4;
5. the partner rank-three cut has sigma_3>=s sqrt(D0)/8;
6. both orientations of that cut have a volume coloop >2/3, so D' cannot be applied directly.

Required implication: use the ORIGINAL-coordinate product structure to convert the half-potential and projective variance into an L-infinity density bound uniformly as D0 tends to zero, or force an already-paid physical-pair/ridge/ray-bank certificate. A variance-only argument cannot simply assert two balanced separated projective banks: an abstract probability law can carry fixed variance in an arbitrarily small far-away atom. The missing proof must exploit the conic coefficients together with product-source concentration, not variance alone.

## 9. Continuity and full-scope status

- The D' exit (6.3): continuous bounded density.
- The new projective canonicalization and half-potential theorem: structural/fractional-potential estimates only; they do not by themselves prove an essentially bounded density.
- The full arbitrary-rank target: OPEN.
- No Gaussianity, log-concavity, compact support, connected support, moments, identical laws, or post-rotation independence were used.

## 10. Deterministic check

`VERIFY.py` and `VERIFY_OUTPUT.txt` in this bundle check on an explicit nontrivial projective chart that

1. Q=2(L20 L02-L11^2),
2. a^TBa=2W^2 Var_pi(t),
3. det[nu(q_i);nu(q_j);nu(q_k)]=Delta_ij Delta_ik Delta_jk,
4. the h=2/3 D' constant equals 72 sqrt(3e).

The expected terminal marker is

    QFORM_B11_PROJECTIVE_CONIC_CHECK_PASS

Independent end-to-end full-target reviews: not applicable; no full candidate is claimed.
