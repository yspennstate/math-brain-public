# fleet01/B05 improvement — fixed-anchor overlap mass can be spent before seed inversion

Run: `20260924T152256Z-fleet01-B05-fixedmult-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned source reviewed: `yspennstate/math-open-problems@eeb752c8943536541b34b42b8bf48e924f4d3d2f`, `paper.tex` blob `19fb119877426b640b2c0dae19ec2f78a399fe11`.

Status: **new supporting theorem for the multiplicity-eight overlap branch; multiplicity eight remains OPEN.** The result aggregates all overlap-one minors sharing one physical coordinate before any reciprocal individual seed determinant is introduced. It does not supply a dimension-free lower bound for the required fixed-anchor currency, so it is not an eight-eigenvalue theorem.

# Theorem `QFORM-FIXED-ANCHOR-OVERLAP-SCALAR-RECEIVER-v1`

Let `X=(X_1,...,X_n)` have independent real coordinates with densities bounded by `K`. Let

`Q=X^T A X+b^T X+c`, `A=A^T`.

Fix one literal physical coordinate `h` with

`a=A_hh !=0`.

For disjoint two-sets `S,T subset [n]\{h}`, define the same-anchor bordered minor

`Delta_(S,T;h)=det A_(S union {h}, T union {h})`,

with rows/columns listed in increasing order; signs are irrelevant below. Define the fixed-anchor overlap mass

`W_h = sum Delta_(S,T;h)^2`,

where the sum may either run over all ordered disjoint `S,T`, or only over those with `det A_(S,T)!=0` as in the manuscript's `W^cross_(2,1)`. In the latter convention the result below remains valid because only terms are removed.

If `W_h>0`, then `Q` has an essentially bounded density and

`boxed: ||p_Q||_infinity <= C2 sqrt(2) K^2 |a|^(-1/4) W_h^(-1/8)`,

where

`C2=8 sqrt(e) 2^(-1/8)<14`.

In particular,

`boxed: ||p_Q||_infinity <18 K^2 (|a|^2 W_h)^(-1/8).`

No moment, support, iid, sign, compactness, log-concavity, post-rotation independence, or exact-rank assumption is used. All affine terms are arbitrary.

## Proof for `K=1`

Complete the square in the literal original coordinate `X_h`. Put

`r=A_([n]\{h}),h`,

and let

`S^(h)=A_([n]\{h}),([n]\{h}) - a^(-1) r r^T`

be the Schur complement of the scalar pivot. Then, against nonnegative output test functions exactly as in the manuscript's scalar profile lemma,

`Q=a(X_h-m(X_-h))^2+R(X_-h)`

and

`p_Q(z) <= |a|^(-1/2) E|z-R|^(-1/2)`

for almost every `z`. The quadratic matrix of `R` is `S^(h)`; its affine term is unrestricted.

Now fix disjoint two-sets `S,T` outside `h`. The bordered determinant/Schur identity gives

`Delta_(S,T;h)= +/- a det S^(h)_(S,T)`.

Indeed, after ordering `h` last on both row and column sides, subtracting the rank-one scalar-pivot contribution gives

`det [[A_(S,T), A_(S,h)], [A_(h,T),a]]
 = a det(A_(S,T)-a^(-1)A_(S,h)A_(h,T))`.

Squaring removes the ordering sign. Therefore

`V_2(S^(h)) >= W_h/a^2`,

because `V_2` contains every ordered disjoint two-by-two minor of the Schur complement, while the manuscript's `W^cross` convention may omit some singular original seeds.

Apply the manuscript's fair-coordinate-cut identity to `S^(h)`. There is a literal partition of the remaining original coordinates whose crossing block `M` satisfies

`Z_2(M) >= V_2(S^(h))/16`.

The independently audited marginal-free order-two receiver then gives the *full* half potential

`sup_z E|R-z|^(-1/2)
 <= C2 Z_2(M)^(-1/8)
 <= C2 16^(1/8) V_2(S^(h))^(-1/8)
 = C2 sqrt(2) V_2(S^(h))^(-1/8).`

Combining with the scalar profile and the overlap lower bound,

`||p_Q||_infinity
 <= C2 sqrt(2) |a|^(-1/2) (W_h/a^2)^(-1/8)
 = C2 sqrt(2) |a|^(-1/4) W_h^(-1/8).`

Since `C2 sqrt(2)=8 sqrt(e)2^(3/8)=17.1051...<18`, the displayed numerical form follows. Every conditioning step is on a literal original coordinate or a literal coordinate partition; the orthogonal operations used inside the order-two receiver are deterministic density estimates, not probabilistic independence assertions.

## General density cap `K`

Set `Y=KX`. In the `Y` variables the coordinate densities are at most one and the quadratic matrix is `A/K^2`. Thus

`a -> a/K^2`, `Delta -> Delta/K^6`, `W_h -> W_h/K^12`.

The normalized right side becomes

`C2 sqrt(2) (|a|/K^2)^(-1/4)(W_h/K^12)^(-1/8)
 = C2 sqrt(2) K^2 |a|^(-1/4)W_h^(-1/8).`

This proves the stated scaling.

# Local three-by-three interpretation

For one seed `B=A_(S,T)` with `det B!=0`, write

`c=A_(S,h)`, `d=A_(T,h)`.

The bordered determinant is

`Delta=det B [a-d^T B^(-1)c]`.

After the scalar Schur step the two-by-two crossing block is

`B'=B-c d^T/a`,

and the matrix determinant lemma gives the exact identity

`det B' = Delta/a`.

A packet-by-packet proof would therefore pay

`C2 |a|^(-1/4)|Delta|^(-1/4)`.

The theorem above is stronger in the relevant direction: for one fixed physical anchor it sums `Delta^2` over *all* disjoint packets first, passes that aggregate through the Schur complement and random-cut identity, and only then takes the negative eighth power. Thus no reciprocal individual `det B` or individual `Delta` appears.

# Consequence for the current eight-direction overlap branch

Group the manuscript's overlap mass by the shared physical coordinate:

`W^cross_(2,1)=sum_h W_h`.

For every `h` with `A_hh !=0` and `W_h>0`, the theorem gives

`||p_Q||_infinity <18 K^2 (|A_hh|^2 W_h)^(-1/8).`

Therefore a dimension-free lower bound

`max_h |A_hh|^2 W_h >= omega>0`

would close the entire corresponding overlap chamber with density bound `18 K^2 omega^(-1/8)`.

The current spectral-overlap theorem supplies only

`sum_h W_h >= constant`

in the unpaid normalized `s_8` chamber. That does **not** imply a dimension-free lower bound on `max_h |A_hh|^2 W_h`: the overlap mass may be spread over many anchors, and the physical diagonals may be arbitrarily close to zero. The no-pivot hypothesis gives an *upper* bound on `|A_hh|`, not the needed lower bound.

Thus the new theorem closes a genuine fixed-anchor/scalar-curvature subbranch while isolating the remaining issue more sharply.

# Exact remaining gap after this run

**GAP `QFORM-S8-MULTI-ANCHOR-OVERLAP-RECEIVER`.** In the no-pivot `s_8` terminal collar one already has a dimension-free aggregate `sum_h W_h`. To turn it into a density theorem one still needs one of:

1. a product-preserving multi-anchor inequality that consumes `sum_h W_h` before selecting a physical anchor; or
2. a dichotomy showing that failure of `max_h |A_hh|^2W_h >= omega` forces enough *different-anchor* curvature into a disjoint order-three crossing volume already handled by the marginal-free receiver; or
3. a shared-linear-carrier receiver for the near-zero `A_hh` anchors, using the retained-copy frequency Jacobian `det A_(S union {h},T union {h})` without paying a reciprocal seed determinant first.

The first and third options must preserve original product provenance. Replacing the relevant projection by an arbitrary bounded joint density, conditioning on a rotated coordinate, or using pointwise quadratic-phase decay for rough bounded densities would repeat already identified invalid mechanisms.

# Threshold status

- Pinned nine-eigenvalue, constant-400 manuscript: one full independent PASS from this run; not self-certified as fully validated.
- Eight eigenvalues: **OPEN**. The present fixed-anchor theorem is supporting progress only.
- Unrestricted three-eigenvalue conjecture: **OPEN**.
