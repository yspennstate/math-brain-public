SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B10, 2026-09-23T14:18:08Z.
attacking: the nonzero near-null physical-hub collar; obtain a q-uniform original-product small-ball estimate before any reciprocal-pivot payment, and identify exactly why the r24 null mixed-Fresnel normal form cannot be perturbed through q != 0.

# Early substantive checkpoint

Let `A=R M R^T`, `R^T R=I_3`, with all three eigenvalues of the invertible symmetric `M` of modulus at least one. Let one ORIGINAL physical row be `u_0=sqrt(h) r`, `||r||=1`, and write every other spectral row as

`u_j=t_j r+p_j`, `p_j in r^perp`.

Parseval gives

`sum_j t_j^2=1-h`, `sum_j p_jp_j^T=I_2`, `sum_j t_jp_j=0`.

Put `q=r^T M r` and let `g=(A_0j)_(j!=0)` be the physical hub cross row. Then exactly

`||g||_2^2 = h r^T M(I-h rr^T)Mr = h(||Mr||^2-hq^2) >= h(1-hq^2)`.

The last inequality uses `sigma_min(M)>=1`. Thus for `|q|<=eta<h^(-1/2)`, the independent leaf linear form `L=g.X_L` has, by the one-dimensional product-projection bound,

`||p_L||_infinity <= sqrt(2)/||g||_2 <= sqrt(2)[h(1-heta^2)]^(-1/2)`.

Now write the full quadratic polynomial in the ORIGINAL hub coordinate as

`Q=(hq)X_0^2+2LX_0+R_L`,

where `(L,R_L)` is an arbitrary dependent pair measurable in the leaves and is independent of `X_0`. Applying `QFORM-RANDOM-SLOPE-SQRT-SMALLBALL-v1` from fleet01/B03 gives, uniformly in the scalar coefficient `hq`,

`sup_z P(|Q-z|<=eps) <= 4 sqrt(||p_L||_infinity eps)`
` <=4*2^(1/4)[h(1-heta^2)]^(-1/4) eps^(1/2)`.

For the live heavy collar `h>55/64` and `|q|<=1/2`, this is

`sup_z P(|Q-z|<=eps) < 5.249 sqrt(eps)`.

This is a genuine q-uniform punctured-collar estimate. It is deliberately only square-root anti-concentration, not an L-infinity density bound.

A second exact calculation explains why r24's null mixed-Fresnel normal form is not perturbatively available. For a nonzero physical scalar pivot `a=A_00!=0`, write the physical matrix as

`A=[[a,g^T],[g,B]]`.

Under any scalar shear `X_0=Z-l.X_L`, the new cross vector and leaf block are

`g'=g-a l`,
`B'=B-g l^T-l g^T+a l l^T`.

Their Schur complement is invariant:

`B'-g'g'^T/a = B-gg^T/a`.

For exact rank three and `a!=0`, this Schur complement has rank exactly two. Therefore no scalar shear can reproduce the null endpoint's rank-one residual. Moreover, if a chosen shear happens to make `rank(B')<=2`, then `g'` lies in the range of `B'`: otherwise adding/subtracting the rank-one term `g'g'^T/a` to the rank-two Schur complement would create rank three. Hence the augmented hub-plus-rank-two Gram required by the direct one-hub mixed-Fresnel receiver is singular in that low-rank realization. This is an algebraic rank jump at `a=0`, not a continuity issue in constants.

The next step is to combine the q-uniform square-root estimate with the designated fleet04/B10 disjoint three-bank curvature packet, rather than attempting the refuted near-zero half-Riesz interpolation.
