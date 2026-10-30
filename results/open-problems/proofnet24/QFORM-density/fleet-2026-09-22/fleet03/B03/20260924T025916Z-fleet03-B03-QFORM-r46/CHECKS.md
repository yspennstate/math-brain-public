# fleet03/B03 r46 deterministic checks

Run: `20260924T025916Z-fleet03-B03-QFORM-r46`.

## Constant checks

With `P=s1*s2` and cap-one product projection constants `L1=sqrt(2)`, `M2=2`:

1. Planar projected coefficient density cap is `M2/P=2/P`.
2. `E |W-a|^-1 <=2 sqrt(pi*2/P)=2 sqrt(2pi) P^-1/2`.
3. The conditional scalar density for `2<a,Y>` is at most `sqrt(2)/(2|a|)=1/(sqrt(2)|a|)`.
4. Multiplying gives `H=2 sqrt(pi) P^-1/2 = 3.5449077018110318... P^-1/2`.
5. If `p_D<=H`, the bathtub/layer-cake half-Riesz bound is `E|D|^-1/2<=2sqrt(2H)=4 pi^(1/4)P^-1/4`.
6. The Fourier Riesz multiplier is `sqrt(2pi)`, hence

`int |t|^-1/2 |phi|^2 <=4sqrt(2)pi^(3/4)P^-1/4`

with constant `13.348651463672827...`.

For the designated fleet04/B03 r3 density cap `H_partner=8 Delta^-1/4`, the same compiler gives

`int |t|^-1/2 |phi|^2 <=4sqrt(pi H_partner)=8sqrt(2pi)Delta^-1/8`,

whose unit-determinant constant is `20.053026197048002...`.

## Homogeneity checks

Scale the crossing `M -> lambda M`. Then `P=s1s2 -> lambda^2 P`; the density estimate scales as `P^-1/2 -> |lambda|^-1`, exactly the scaling of a scalar output dominated by a bilinear/linear-in-Y term. The whole-copy weighted-time quantity scales as `P^-1/4 -> |lambda|^-1/2`, matching the half-Riesz/time weight.

## Dependence/provenance checks

- `u1^T X,u2^T X` may be dependent; only their **joint two-dimensional density cap** is used.
- No singular-vector coordinate is declared independent.
- The `Y`-bank is used through the scalar product-projection theorem conditional on the genuine independent bank `(X,Z)`.
- The full coefficient vector `M^T X+q` is retained. Extra singular directions can only increase its Euclidean norm; no tail is dropped probabilistically.
- The independent-copy identity is applied only to the complete scalar outputs `S,S'`.
- No conditioning of `X-X'` on `X+X'` occurs.

## Boundary/counterexample compatibility

The fleet02/B03 rank-two triangle instability contains quadratic self-curvature on both banks after the small second crossing is restored. The present theorem explicitly requires the conditioned `Y` bank to enter linearly. Therefore it does not contradict that logarithmic-singularity example and cannot be extended to arbitrary `Y^T D Y` by a perturbative argument.

## Regularity scope

The proof gives a mixture of conditional absolutely continuous laws and an integrable uniform density envelope. The exceptional zero-coefficient event has probability zero because a two-dimensional projection of `M^T X+q` has an absolutely continuous density. Hence absolute continuity and the essential `L^infinity` bound are valid. No proof that the resulting density has a continuous representative is supplied.

`QFORM_B03_R46_CHECK_PASS`
