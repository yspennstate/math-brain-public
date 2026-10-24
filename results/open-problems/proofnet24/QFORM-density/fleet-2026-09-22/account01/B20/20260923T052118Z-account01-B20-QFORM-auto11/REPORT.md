# account01/B20 — O3 star wedge alignment and anchored-overlap collapse

Status: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN / CONTINUITY_OPEN`.

Target: independent real coordinates with densities at most one; real symmetric A with at least three eigenvalues of modulus at least one; prove a universal essential density bound for Q=X^TAX or give a valid counterexample. No Gaussian, moment, iid, compact-support, log-concavity, or post-rotation-independence assumption is used below.

## Sources actually consumed

Fresh designated partner: account02/B20 r24, canonical mathematics `yspennstate/math-open-problems@0da7f3ef78f89efa33d2014211323fcda3d3214b`, theorem `QFORM-STAR-THIRD-RESOURCE-WEDGE-ANCHOR-v1`.

In its surviving ORIGINAL-coordinate star block

    C = [[a,m^T],[m,B]],

put r=||m||_2 and gamma=s_3(C). The partner proves

    r > 1/48,    gamma > 1/6,

and, with

    W_j = sum_{k<l; k,l != j} (m_k B_{jl}-m_l B_{jk})^2,
    E_j = sum_{k != j} (m_j B_{jk}-B_{jj}m_k)^2,
    W=sum_j W_j, E=sum_j E_j,

it proves

    W+E >= r^2 gamma^2/2 > T0 := 1/165888.              (1)

The prior account01/B20 physical disjointization theorem is also used in the W-side compiler: if W>0, some deterministic original-coordinate partition J sqcup R of the leaves gives

    N=C[{hub} union J,R],
    e_2(NN^T) >= (4/27) W.                               (2)

The reviewed third-volume diffuse theorem used in the previous B20 compiler is retained only in its already source-valid scope: if e_3(NN^T) is substantial and one orientation has all third-volume marginals <=2/3, it pays the full ambient quadratic form by

    ||p_Q||_infinity <= 9 sqrt(3e) e_3(NN^T)^(-1/6).     (3)

No uniform pointwise quadratic oscillatory decay, arbitrary-joint coarea, conditional spectral cap, rotated independence, or one-good-minor extraction is used.

## 1. A weighted line-graph rigidity lemma for W

### Theorem A (`QFORM-STAR-WEDGE-ALIGNMENT-v1`)

Let m in R^d be nonzero, r=||m||_2, and B be real symmetric. Define W as above. Assume

    max_j m_j^2 <= h r^2,       0<h<1.                  (4)

Then there are a scalar mu and a diagonal matrix D such that

    ||B-mu m m^T-D||_F^2
       <= (1 + 5/(1-h)) W/r^2.                           (5)

In particular, under max_j m_j^2<=r^2/2,

    inf_{mu,D diagonal} ||B-mu m m^T-D||_F^2
       <= 11 W/r^2.                                      (6)

This is a deterministic physical-coordinate statement. Singular/eigenvector coordinates are not used probabilistically.

### Proof

Normalize e=m/r and write w_j=e_j^2, so sum_j w_j=1. Let

    S={j:w_j>0},   Z={j:w_j=0}.

Condition (4) implies |S|>=2. First treat edges with both endpoints in S. For j,k in S, j!=k, write

    B_{jk}=e_j e_k q_{jk},   q_{jk}=q_{kj}.

For each j in S set

    c_j = [sum_{k in S, k!=j} w_k q_{jk}]/(1-w_j).

Let

    F = sum_{j in S} w_j sum_{k in S,k!=j} w_k(q_{jk}-c_j)^2.   (7)

The weighted-variance identity

    sum_{k<l} w_k w_l(x_k-x_l)^2
      = (sum_k w_k) sum_k w_k(x_k-xbar)^2

applied in every row gives

    W/r^2 >= sum_{j in S} w_j(1-w_j)
                sum_{k in S,k!=j} w_k(q_{jk}-c_j)^2
            >= (1-h)F.                                   (8)

Now put lambda=sum_{j in S} w_j c_j. Symmetry q_{jk}=q_{kj} gives

    Var_w(c)=sum_{j<k;j,k in S} w_jw_k(c_j-c_k)^2 <= 2F, (9)

because for every edge

    (c_j-c_k)^2 <=2[(c_j-q_{jk})^2+(q_{jk}-c_k)^2].

Expanding around each row mean and using (9),

    sum_{j!=k;j,k in S}(B_{jk}-lambda e_j e_k)^2
      = F + sum_j w_j(1-w_j)(c_j-lambda)^2
      <= F+Var_w(c)
      <=3F
      <= 3W/[(1-h)r^2].                                  (10)

It remains to account for zero coordinates of m. If j in S and k in Z, then the terms in W_j using the pair {k,l}, l in S\{j}, contribute

    r^2(1-w_j) B_{jk}^2.

Hence

    2 sum_{j in S,k in Z} B_{jk}^2
      <= 2 W/[(1-h)r^2].                                 (11)

If j,k are distinct elements of Z, then for fixed j, summing in W_j over the pairs {k,l}, l in S, contributes exactly r^2 B_{jk}^2. Consequently

    sum_{j!=k;j,k in Z} B_{jk}^2 <= W/r^2.               (12)

Combining (10)-(12),

    sum_{j!=k}(B_{jk}-lambda e_je_k)^2
      <= [1+5/(1-h)]W/r^2.                               (13)

Set mu=lambda/r^2 and choose the diagonal entries

    D_j=B_{jj}-mu m_j^2.

Then B-mu mm^T-D has zero diagonal, and (13) is exactly (5). QED.

## 2. Exact rowwise decomposition of the anchored E currency

For any j with r^2-m_j^2>0, define the physical row projection coefficient

    c_j^row = <m_{-j},B_{j,-j}>/(r^2-m_j^2),

and residual

    u_j=B_{j,-j}-c_j^row m_{-j},

so u_j is perpendicular to m_{-j}. Put

    t_j=B_{jj}-c_j^row m_j.

Then the definitions of W_j,E_j give the exact identities

    W_j=(r^2-m_j^2)||u_j||_2^2,                           (14)

    E_j=m_j^2||u_j||_2^2+(r^2-m_j^2)t_j^2
       =[m_j^2/(r^2-m_j^2)]W_j+(r^2-m_j^2)t_j^2.         (15)

Therefore in the diffuse-star regime max_j m_j^2<=r^2/2,

    sum_j (r^2-m_j^2)t_j^2 >= E-W.                       (16)

This is useful because it records the E reserve without extracting a reciprocal individual minor.

## 3. Apply the partner inequality with an 88-way threshold

Set

    w_* := T0/88 = 1/14598144.                           (17)

We split the partner certificate (1) according to W.

### Branch I: W >= w_*

Apply (2): some ORIGINAL-coordinate cross block N satisfies

    e_2(NN^T) >= (4/27)W > 1/98537472.                  (18)

Thus the entire not-too-small-W branch is again compiled into a standard physical cross-block resource, now at the explicit scale (18).

For completeness, the previous B20 e_2-to-third-volume compiler gives an exhaustive quantitative refinement. The identity

    3 e_3(NN^T) >= e_2(NN^T)
       dist_F(N,{rank<=2})^2                              (19)

implies that with

    eps_* := 1/1210828455936
            = (1/98537472)/12288,                        (20)

one has either

    dist_F(N,{rank<=2}) < 1/64,                           (21)

or e_3(NN^T)>=eps_*. In the latter case, if either the row or column third-volume law has all marginals <=2/3, (3) yields

    ||p_Q||_infinity
      <= 9 sqrt(3e) eps_*^(-1/6)
      < 2653.368.                                         (22)

If neither orientation is diffuse, row and column anchors have marginal >2/3, their joint inclusion probability is >1/3, and a two-colouring of the remaining two rows and columns gives a nested ORIGINAL-coordinate anchored packet of third-minor mass

    > eps_*/12
    = 1/14529941471232.                                  (23)

Thus no diffuse aggregate W debt remains: Branch I is either paid, in an explicit rank-two tube, or in an explicit nested two-anchor packet.

### Branch II: W < w_*

By (1),

    E > T0-W > (87/88)T0.                                (24)

There are now two subbranches.

#### II(a). Heavy star coordinate

If max_j m_j^2>r^2/2, then some physical hub-leaf coefficient obeys

    |m_j|>r/sqrt(2)>1/(48sqrt(2)).                       (25)

This is a single fixed-strength physical arm. It is recorded as a separate residual chamber; no same-bank-curvature absorption is asserted from (25) alone.

#### II(b). Diffuse star: aggregate E collapses to one anchored physical row

Assume max_j m_j^2<=r^2/2. By Theorem A and W<w_*, there are mu and diagonal D such that

    B=mu mm^T+D+R,
    diag R=0,
    ||R||_F^2 <= 11W/r^2.                                (26)

Using r^2>1/2304, T0=1/165888=1/(72*2304), and w_*=T0/88,

    ||R||_F^2
      < 11*2304/(165888*88)
      = 11/(72*88)
      = 1/576,

hence

    boxed: ||R||_F < 1/24.                               (27)

Form the exact rank-one-plus-diagonal surrogate

    C0=[[a,m^T],[m,mu mm^T+D]].                          (28)

Because ||C-C0||_op<=||R||_F<1/24 and s_3(C)>1/6,

    s_3(C0)>1/8.                                         (29)

But

    Cbase=[[a,m^T],[m,mu mm^T]]

has rank at most two: every leaf column is a multiple of [1;mu m], together with the hub column [a;m]. Since

    C0=Cbase+diag(0,D),

Eckart--Young/Weyl gives

    s_3(C0) <= ||diag(0,D)||_op=max_j |D_j|.

Consequently there is a PHYSICAL leaf j for which

    boxed: |D_j|>1/8.                                   (30)

For this same j, the anchored-overlap vector from the partner has the exact representation

    (m_jB_{jk}-B_{jj}m_k)_{k!=j}
       = m_j R_{j,-j}-D_j m_{-j}.                        (31)

The diffuse-star assumption gives both |m_j|<=r/sqrt(2) and ||m_{-j}||>=r/sqrt(2). Combining (27), (30), and the reverse triangle inequality,

    sqrt(E_j)
      >= |D_j| ||m_{-j}||-|m_j| ||R_{j,-j}||
      > r/(8sqrt(2))-r/(24sqrt(2))
      = r/(12sqrt(2))
      > 1/(576sqrt(2)).                                  (32)

Therefore

    boxed: E_j > 1/663552.                               (33)

This is the main new closure step: in the genuinely E-heavy/small-W/diffuse-star chamber, the partner's aggregate anchored-minor reserve cannot remain diffuse over all leaves. It collapses to one fixed physical leaf carrying a dimension-free row aggregate of one-overlap 2x2 minors.

For later use, (16), (24), and W<w_*=T0/88 also give the separate row-adapted twist reserve

    sum_j (r^2-m_j^2)t_j^2
       >= E-W
       > T0-2w_*
       = (43/44)T0.                                      (34)

No individual t_j is extracted from (34); equation (33) is obtained instead from the global spectral rank argument (29)-(31).

## 4. Resulting proof graph

The account02/B20 r24 O3-star packet is now routed as follows.

1. `W>=T0/88`: a genuine disjoint physical cross block has e_2>1/98537472, hence the already valid e_3 diffuse/rank-two/nested-anchor compiler applies.
2. `W<T0/88` and one star coordinate is heavy: a fixed physical arm satisfies |m_j|>1/(48sqrt(2)).
3. `W<T0/88` and the star is diffuse: there is one fixed physical leaf j with the anchored-overlap row certificate E_j>1/663552; moreover the leaf block is within Frobenius 1/24 of a rank-one-plus-diagonal matrix and its diagonal twist has a physical entry >1/8.

Thus the former unresolved `aggregate E` state has been replaced by two sharply localized, source-valid states: one heavy physical arm or one fixed anchored-overlap row. The latter has a quantitative one-overlap determinant norm and a rank-one-plus-diagonal provenance.

The first remaining implication in this chamber is now `QFORM-O3-HEAVY-ARM-OR-ANCHORED-OVERLAP-PAYMENT-v1`: construct a dependence-safe density receiver for (25) or (33), retaining arbitrary same-bank curvature and outside couplings. The natural next target is a grouped overlap-chain theorem rather than extraction of a single large minor.

## 5. Scope discipline

- Full QFORM remains OPEN / not proved / not disproved.
- Global continuity remains OPEN; the present result is deterministic structure plus reuse of already scoped density exits.
- All partitions and anchors are original physical coordinates.
- No rotated variable is declared independent.
- No uniform pointwise quadratic Fresnel decay is used.
- No claim that aggregate minor mass yields one large individual minor is made.
- The heavy-arm alternative is not declared paid merely from one coefficient.
