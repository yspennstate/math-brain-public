# fleet02/B18 r52 — near-rank-one cross collar forces transverse complement curvature

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260924T091122Z-fleet02-B18-qform-auto11-r52`  
**Status:** PROVED SUPPORTING STRUCTURAL REDUCTION / LATEST PARTNER APPLIED / PINNED e5f THEOREM APPLIED / FULL QFORM OPEN  
**Continuity:** not asserted by the generic structural/partner branch.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B18, 2026-09-24T09:11:22Z.

attacking: the latest fleet03/B18 rank-one cross collar; prove that the three-large-eigenvalue hypothesis forces nearly unit curvature transverse to its top opposite-bank singular direction, then test that survivor against the pinned mixed-hub theorem.

## 1. First unpaid implication, now sharpened

The newest completed designated-partner result is fleet03/B18 auto22, scientific commit `f41725400c9a25ea98a414477c94fd4a4333e078`. For an ORIGINAL-coordinate split with zero self-block

`A = [[0,D],[D^T,C]]`

and singular values `d1>=d2>=...` of the full cross map `D`, arbitrary opposite-bank curvature `C` is retained and

`||p_Q||_inf <= 2 sqrt(pi)/(d1 d2)^(1/2)`

whenever `d2>0`. Hence at any threshold `theta>0`, either `d1 d2>=theta` and the density is paid, or `d2<sqrt(theta)` and `D` lies in an operator-norm rank-one collar.

The first unpaid implication inside this packet was therefore: **what does `s3(A)>=1` force on the opposite-bank curvature once the full cross map is near rank one?**

This run proves an exact answer.

## 2. New deterministic theorem: `QFORM-RANK1-COLLAR-FORCES-TRANSVERSE-CURVATURE-v1`

Let

`A = [[0,D],[D^T,C]]`

be a real symmetric block matrix, with `C=C^T`. Write `s=s3(A)` for the third singular value of `A` (equivalently the third largest absolute eigenvalue). Let `d1>=d2>=...` be the singular values of `D`, taking `d2=0` if `rank(D)<=1`.

Assume `d1>0`, choose top singular vectors `u,v` with

`D v = d1 u`,  `D^T u = d1 v`,

and let `P=I-vv^T` on the opposite bank. Then

`boxed:  s3(A) <= d2 + ||P C P||_op.`

Equivalently,

`boxed:  ||P C P||_op >= (s-d2)_+.`

Thus a rank-one (or near-rank-one) full cross carrier cannot support a third large singular direction by its longitudinal curvature/coupling alone: the compression of `C` transverse to the top right singular vector must carry the missing spectral scale.

### Proof

Let

`D1=d1 u v^T`,  `E=D-D1`,  so `||E||_op=d2` by Eckart--Young.

Write

`c=v^T C v`,  `h=P C v`,

and retain only the part of `C` touching `v`:

`C0 = c vv^T + v h^T + h v^T`

`   = vv^T C + C vv^T - vv^T C vv^T.`

Define

`R = [[0,D1],[D1^T,C0]].`

In the full direct sum space put

`e=(0,v)`,  `q=(d1 u, h+(c/2)v)`.

Then exactly

`R = e q^T + q e^T`,

so `rank(R)<=2`.

Moreover

`A-R = [[0,E],[E^T,P C P]].`

The off-diagonal symmetric block `[[0,E],[E^T,0]]` has operator norm `||E||_op=d2`, while `diag(0,PCP)` has operator norm `||PCP||_op`. Therefore

`||A-R||_op <= d2 + ||PCP||_op.`

By the rank-two approximation characterization of the third singular value,

`s3(A)=inf_{rank(S)<=2} ||A-S||_op <= ||A-R||_op`,

which proves the theorem. No probabilistic assumption enters this step. QED.

## 3. Equation-level splice with newest fleet03/B18 auto22

Apply the partner theorem to the same ORIGINAL-coordinate packet. For every `theta>0`:

* if `d1 d2>=theta`, then

  `||p_Q||_inf <= 2 sqrt(pi)/sqrt(theta)`;

* if `d1 d2<theta`, then `d2<sqrt(theta)` because `d2<=d1`, and the theorem above gives

  `||P C P||_op > s-sqrt(theta)`.

Thus the combined exact dichotomy is

`boxed: either ||p_Q||_inf <= 2 sqrt(pi)/sqrt(theta),`

`       or ||P_{v^perp} C P_{v^perp}||_op > s3(A)-sqrt(theta).`

At the live threshold `theta=2^-12` and owner normalization `s3(A)>=1`,

`boxed: either ||p_Q||_inf <=128 sqrt(pi)=226.874092915906... ,`

`       or ||P_{v^perp} C P_{v^perp}||_op >63/64.`

So the newest partner's surviving rank-one collar is **not arbitrary opposite-bank curvature**. It necessarily contains an almost-unit transverse compression. Importantly this is only a rotated Rayleigh/compression statement; it does NOT make the corresponding projected coordinate independent and it does NOT imply a large physical diagonal entry.

If `D=0`, the block is `0 direct_sum C` and the statement degenerates to the exact recursive fact `s3(C)=s3(A)`; no top right singular vector is needed.

## 4. Sharpness and a source-valid obstruction to a large physical pivot

The deterministic inequality is sharp. Take a scalar `X0`, an opposite bank `Y in R^m`, orthonormal vectors `v,w in R^m`, and

`A_{m,d,s} = [[0,d v^T],[d v,s w w^T]]`,  `d>=s>0`.

On `span{X0,v,w}` the matrix is exactly

`[[0,d,0],[d,0,0],[0,0,s]]`,

so its nonzero spectrum is `{-d,d,s}`. Hence `s3(A)=s`, `d2=0`, and with `P=I-vv^T`,

`||P C P||_op=s`.

Now make the curvature maximally diffuse. For even `m>=4`, set

`v_i=1/sqrt(m)` for every `i`,

and `w_i=+1/sqrt(m)` on the first half and `-1/sqrt(m)` on the second half. Then `v,w` are orthonormal and every physical diagonal on the `Y` bank equals

`A_ii=s/m`.

At `s=1`, `d>=1`, this is a literal owner-target family with spectrum `{-d,d,1}`, yet every physical scalar pivot tends to zero as `m->infinity`. Therefore the new transverse-curvature conclusion cannot be strengthened to a uniformly large ORIGINAL-coordinate diagonal pivot. This is a proof-interface obstruction, not a counterexample to QFORM.

## 5. Required pinned e5f result applied to the same survivor

Use the pinned source

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

and its proved Theorem H (mixed hub Fresnel--Brascamp--Lieb). For the diffuse family above with `s=1`, choose the literal hub `H={X0}` and `I=Y`. Inside `I`, the quadratic block is the rank-one square `w w^T`. The hub coupling is `d v`.

The normalized two-frame rows are

`rho_i=(w_i,d v_i)`,

with Gram matrix

`G=sum_i rho_i rho_i^T = diag(1,d^2)`

because `v perp w`. Each normalized leverage equals

`rho_i^T G^{-1} rho_i = w_i^2+v_i^2 = 2/m <=1/2`.

Theorem H therefore applies literally, without rotating the product law or asserting independence of `v^T Y` and `w^T Y`. It gives

`|phi_Q(t)| <= 4 pi^(3/2) d^(-1) |t|^(-3/2)`.

Using `|phi_Q|<=1` and Fourier inversion,

`int_R min(1,K |t|^-3/2) dt = 6 K^(2/3)`,

so

`boxed: ||p_Q||_inf <= 3 * 2^(4/3) d^(-2/3)`

`       = 7.559526299369239... d^(-2/3) <=7.559526299369239... .`

This pays a genuine exact-rank-three family lying **exactly** in the latest partner's rank-one cross survivor (`d2=0`) even though every physical diagonal can vanish like `1/m`. It demonstrates the correct aggregate mechanism: one original-coordinate hub plus a diffuse transverse square, not a forced large coordinate pivot.

The pinned `COUNTEREXAMPLE_SEARCH.md` reports no valid counterexample, but that search miss is not used as novelty evidence or as evidence for the full theorem.

## 6. Primary-source audit actually needed here

The latest partner's analytic receiver uses the marginal-density theorem of Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1. Its statement assumes an actual product probability density `prod_i f_i`, with each one-dimensional density bounded, and proves for every `k`-dimensional orthogonal marginal

`||pi_E f||_inf <= min{(n/(n-k))^((n-k)/2), 2^(k/2)} prod_i ||f_i||_inf^(gamma_i)`,

for weights `gamma_i in [0,1]`, `sum gamma_i=k`. Under the owner cap `||f_i||_inf<=1`, this gives the exact `2^(k/2)` cap; for `k=1,2`, respectively `sqrt(2)` and `2`. The source requires no moments, compact support, log-concavity, iid, centering, symmetry, or smoothness. It bounds the marginal density only; it does **not** assert that projected coordinates are independent.

No external theorem is needed for the new deterministic rank-two approximation argument. The pinned mixed-hub result is used at its exact proved hypotheses.

## 7. Remaining exact debt

Inside a zero-self-bank packet, the live unpaid geometry is now:

1. the full cross map is exact/near rank one;
2. its second singular tail must be retained, not deleted;
3. the opposite-bank compression transverse to the top right singular direction has operator norm almost `s3(A)`;
4. that transverse curvature may be maximally diffuse in physical coordinates.

The next useful implication is therefore

`QFORM-RANK1-CROSS-TRANSVERSE-CURVATURE-TO-HUB-OR-AGGREGATE-EXIT-v1`:

route the forced large transverse compression into a product-preserving mixed-hub, grouped-bank, projected-crossing, physical-pair, or Fresnel aggregate receiver, while retaining the nonzero `d2` tail and all same-bank curvature. A rotated eigenvector of `P C P` is not an independent source, and small operator-norm coefficients cannot be discarded under arbitrary unbounded cap-one laws.

Outside this packet, the bare global hypothesis `s3(A)>=1` still does not force a zero-self ORIGINAL-coordinate side, so the full product-preserving compiler remains unpaid.

## 8. Status

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. The result above is a supporting deterministic-plus-analytic funnel and an exact target-family payment. Continuity is separate and is not asserted by the generic partner branch.
