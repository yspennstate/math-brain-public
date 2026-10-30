SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B06, 2026-09-23T16:53:50Z.
attacking: convert failure of the r=1,k=1 Fresnel-cross volume marginal gate into an exact at-most-two-original-coordinate fused-volume concentration certificate, then spend partner r39's near-rank-two floor before any local inverse minor.

# Early substantive checkpoint — exact fused-row identity and heavy-row transfer

Full target remains OPEN. This checkpoint records a source-valid structural calculation for the diagonal-plus-rank-one same-bank subbranch; it does not assert the unrestricted theorem.

Let `v in R^m` be unit, `M` an `m x n` physical cross block, and

`C=(I-vv^T)M`, `Z=||C||_F^2>0`.

Equivalently

`Z = sum_{p<q} sum_t (v_p M_{qt}-v_q M_{pt})^2`.

Put the canonical fused-minor probability

`w_{pq,t}=(v_p M_{qt}-v_q M_{pt})^2/Z`,

and its row marginal `alpha_i=P_w(i in {p,q})`.

## Exact row identity

For every physical row `i`,

`boxed: alpha_i = v_i^2 + ||C_{i,*}||_2^2/Z.`

Proof. Replace each column `M_t` by `c_t=(I-vv^T)M_t`; the two-by-two determinants with the first column `v` are unchanged. Since `<v,c_t>=0` and `||v||=1`,

`sum_{j != i} (v_i c_{jt}-v_j c_{it})^2
 = v_i^2 ||c_t||^2 + c_{it}^2`.

Sum in `t` and divide by `Z`. In particular `sum_i alpha_i=2`, as required for a probability on row pairs.

## Exact transfer of a heavy physical row

Consider the quadratic-form subbranch

`Q = X^T(D + lambda vv^T)X + 2 X^T M Y + R(Y) + affine`,

where `D` is diagonal in the ORIGINAL `X` coordinates, all original coordinates in `X,Y` remain independent with densities at most one, and `R` is arbitrary. Move one physical coordinate `h` from the Fresnel bank to the arbitrary bank. Put

`s^2=1-v_h^2`.

When `s>0`, the remaining rank-one term is `lambda' v'v'^T` with

`v'=v_{-h}/s`, `lambda'=lambda s^2`.

The enlarged cross block acquires one extra column `lambda v_h v_{-h}`, which is parallel to `v'` and therefore contributes zero to the transverse fused currency. If `Z'` is the new `r=1,k=1` fused currency, then Cauchy-Binet gives

`s^2 Z' = sum_{p<q, p,q != h} sum_t (v_pM_{qt}-v_qM_{pt})^2
       = Z(1-alpha_h)`.

Hence the scale entering the B06 Fresnel-volume receiver obeys the exact identity

`boxed: |lambda'| Z' = |lambda| Z (1-alpha_h).`

Moreover the new squared-minor law is precisely the old law conditioned on `h` not belonging to the sampled row pair. If `s=0`, every nonzero fused minor contains `h`, so this is already the fully concentrated endpoint.

## Two-transfer compiler

Let `C_F=3*2^(4/3)*e^(1/3)`. The preceding B06 Fresnel-volume theorem gives

`D(Q)<=C_F (|lambda|Z)^(-1/3)`

whenever all fused row marginals are at most `1/2`.

The transfer identity yields the following unconditional structural dichotomy for this subbranch:

* either, after moving at most one heavy physical row to the arbitrary bank, the remaining fused law has all row marginals at most `1/2` and retains probability mass `p>=1/4`; then

  `boxed: D(Q) <= C_F 4^(1/3) (|lambda|Z)^(-1/3)`;

* or there is a set `H` of at most two ORIGINAL coordinates such that

  `boxed: P_w({p,q} intersects H) > 3/4`,

  equivalently more than `3Z/4` of the physical fused determinant mass touches `H`.

Indeed, if the first heavy row has marginal `alpha_1>1/2`, the surviving mass is `p_1=1-alpha_1<1/2`. If `p_1<1/4`, one row already gives the concentration alternative. Otherwise transfer it. If the conditional law is diffuse, the density theorem applies with `p_1>=1/4`; if it has another heavy row, the twice-surviving mass is `p_2=p_1(1-alpha_2')<p_1/2<1/4`, so two rows meet more than `3/4` of the original fused mass.

This replaces an uncontrolled marginal failure by a bounded-cardinality ORIGINAL-coordinate certificate without selecting a single large minor and without rotating the product law.
