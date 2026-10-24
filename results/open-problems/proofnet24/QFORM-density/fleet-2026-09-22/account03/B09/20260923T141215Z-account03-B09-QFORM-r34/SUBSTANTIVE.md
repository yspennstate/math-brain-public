SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-23T14:12:15Z.
attacking: the grouped 2+1 anchored aggregate endpoint: consume a high-leverage hub jointly with the second hub direction and moved-leaf third volume, retaining arbitrary within-bank curvature.

# Early substantive checkpoint — Pluecker concentration is either one-anchor payable or a genuinely localized physical pair

Full QFORM remains OPEN. This checkpoint records an exact deterministic identity and a quantitative routing step for the high-hub-leverage survivor left after account03/B09 r32 and account02/B09 r13. It does not use post-rotation independence, moments/support bounds, or pointwise quadratic stationary phase.

## 1. Exact two-plane Pluecker identity

Let P be an m x 2 real matrix with P^T P=I_2. For i<j write the signed Pluecker coordinate

    q_ij=det P[{i,j},:],   w_ij=q_ij^2,

so Cauchy--Binet gives sum_(i<j) w_ij=1. Fix an edge {a,b} with w=w_ab>0. Put

    r_a=sum_(i notin {a,b}) w_ai,
    r_b=sum_(i notin {a,b}) w_bi,
    d=sum_(i<j, i,j notin {a,b}) w_ij.

With the usual signed convention q_ji=-q_ij, the Pluecker relation

    q_ab q_ij = q_ai q_bj-q_aj q_bi

and the Lagrange identity give the EXACT formula

    d = [r_a r_b-c_ab^2]/w <= r_a r_b/w,

where

    c_ab=sum_(i notin {a,b}) q_ai q_bi.

Consequently

    1=w+r_a+r_b+d <= w(1+r_a/w)(1+r_b/w).                  (1)

Thus if r_a,r_b <= delta w, then

    w >= (1+delta)^(-2).                                     (2)

This converts concentration on one partner row into actual localization of the ENTIRE two-dimensional physical hub plane, not merely its incident edge distribution.

## 2. Fractional one-anchor thinning

For a fixed anchor a, let w be a maximum Pluecker edge incident to a and let r_a be the remaining incident mass. There is a fractional submeasure z_ai with 0<=z_ai<=w_ai, supported on edges containing a, of total mass

    m_a=min(w+r_a, 2 r_a),                                   (3)

such that every non-anchor row has normalized marginal at most 1/2. Indeed, if w<=r_a retain every incident edge; otherwise retain every residual edge and only r_a of the dominant edge. In both cases no retained partner edge exceeds m_a/2.

The determinant lower bound used in the selected-subvolume Brascamp--Lieb argument permits such fractional thinning: replace a determinant coefficient det^2 by theta det^2 with 0<=theta<=1 before weighted AM--GM. The one-anchor three-volume proof remains valid because its derived two-volume inequality only uses the domination z_R<=||a_row||^2 Z2_R, which fractional thinning preserves.

In the r32 Bernoulli compiler, hub-pair determinant weights factor independently from the moved-leaf/column determinant weights. Therefore, in the diffuse-singleton branch, thinning the hub pair by (3) preserves every moved-leaf marginal <1/2 and produces a selected physical three-minor mass

    Z_anchor >= m_a W(S),
    W(S)>=(27/256) G_*.                                      (4)

Applying account02/B09 `QFORM-ONE-ANCHOR-THREEVOLUME-HYBRID-v1` gives the actual inequality

    ||p_Q||_infinity
      <= 5*2^(4/5)*sqrt(e)
         [ ||A[a,T]||_2 /(m_a W(S)) ]^(1/5),                 (5)

with a continuous density and the same coefficient times interval length. All same-bank curvature remains arbitrary.

## 3. Quantitative high-leverage dichotomy

Suppose the preceding q-Jensen route has failed at a hub row h with leverage eta_h>=3/4 and its dominant partner b has

    w=w_hb>eta_h/2>=3/8.

Fix 0<delta<=1. If either r_h>=delta w or r_b>=delta w, then the corresponding anchored thinning has

    m_anchor>=2 delta w >=(3/4)delta.                        (6)

Hence (4)-(5) pay that aggregate branch with a dimension-free retained determinant fraction.

If neither residual is this large, then (2) forces

    w >=(1+delta)^(-2).                                      (7)

For example delta=1/4 gives the exhaustive fork

    either m_anchor>=3/16,
    or w_hb>=16/25=0.64.                                     (8)

In the second case the physical two-row matrix P[{h,b},:] satisfies

    sigma_min(P[{h,b},:]) >= sqrt(w_hb) >=4/5,               (9)

because P[{h,b},:]^T P[{h,b},:] <=I_2 and its determinant is w_hb. Thus the unresolved high-hub endpoint is no longer merely a concentrated conditional partner distribution: it is a quantitatively almost-coordinate two-plane carried by a literal physical pair.

The next step in this run is to splice (8)-(9) to an existing two-physical-hub or cross-volume receiver without deleting arbitrary leaf curvature. The exact two-row endpoint P=I_2 is retained as a mandatory control; it shows that a scalar selected-row marginal argument cannot by itself finish the branch.
