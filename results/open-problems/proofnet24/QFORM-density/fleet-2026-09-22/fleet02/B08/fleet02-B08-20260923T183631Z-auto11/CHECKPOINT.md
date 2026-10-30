SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B08, 2026-09-23T18:36:31.799774Z.
attacking: the r43/r44 two-hub common-plane survivor; first remove the nonzero light-light edge/tail when the physical two-hub self quadratic vanishes, then isolate the genuine hub-quadratic stability debt.

# Early substantive checkpoint — zero-hub receiver with arbitrary light remainder

Full QFORM remains OPEN.

The newest partner fleet03/B08 r44 proves the exact two-arm PATH receiver when the two light banks have no direct crossing, even with an arbitrary internal hub function. I attack the complementary face: allow an arbitrary light-light quadratic remainder, but require that the two-dimensional hub enter only linearly.

## Lemma — `QFORM-TWOHUB-LINEAR-ARBITRARY-LIGHT-REMAINDER-v1`

Let `W` be an `R^2`-valued random vector independent of a random block `Z`. Assume every one-dimensional unit projection of `W` has a density bounded by `K_W`. Let `S=S(Z)` be an `R^2`-valued random vector with density bounded by `M_S`, and let `G(Z)` be an arbitrary measurable real function, with no independence required between `S` and `G`. Put

`Q = G(Z) + 2 <W,S(Z)>`.

Then `Q` has an essentially bounded density and

`||p_Q||_infinity <= K_W sqrt(pi M_S).`                         (1)

No continuity conclusion is claimed.

### Proof

Condition on `Z=z`. For `s=S(z) !=0`, the scalar `<W,s>` is `|s|` times a unit projection of `W`, so the conditional density of `2<W,s>` is bounded by

`K_W/(2|s|)`.

Because `S` is absolutely continuous, `P(S=0)=0`. Thus for every Borel interval `I`,

`P(Q in I) <= |I| (K_W/2) E |S|^{-1}`.

For an `R^2` probability density `p<=M_S`, the bathtub/rearrangement bound gives

`int p(s)|s|^{-1} ds <= 2 sqrt(pi M_S)`:

the maximizing density is `M_S 1_{|s|<=R}`, with `pi R^2 M_S=1`, and its integral is `2 pi M_S R=2 sqrt(pi M_S)`. Substitution proves (1). QED.

## Original-product two-arm corollary

Let three disjoint original-coordinate banks be `H,J_1,J_2`. Let `W=R_H^T X_H` be a two-dimensional orthonormal projection of the hub bank. For cap-one product laws, every unit projection of `W` is an orthonormal one-dimensional projection of a product law, hence `K_W<=sqrt(2)`.

Let

`U=M_1 X_{J_1}`, `V=M_2 X_{J_2}`

with `M_r` of row rank two and singular-product `S_r=s_1(M_r)s_2(M_r)`. The two-dimensional projection-density bound gives

`||p_U||_infinity<=2/S_1`, `||p_V||_infinity<=2/S_2`.

Since the banks are independent, for

`S=U+V+beta`

we have

`||p_S||_infinity <= min(2/S_1,2/S_2)=2/max(S_1,S_2)`.

Therefore every quadratic form of the shape

`Q = G(X_{J_1},X_{J_2}) + 2 <W, M_1X_{J_1}+M_2X_{J_2}+beta>`      (2)

with **arbitrary** measurable `G` satisfies

`boxed: ||p_Q||_infinity <= 2 sqrt(pi) max(S_1,S_2)^(-1/2).}`    (3)

In particular `G` may contain every same-bank quadratic term and an arbitrary nonzero physical crossing between the two light banks. Thus no small light-light coefficient is deleted.

## Application to the newest fleet03/B08 common-plane state

In r43/r44's diffuse R2 bisection, both arm products obey

`S_r > L^2/(64 sqrt(896))`.

If the translated two-physical-hub block has zero quadratic part (affine terms are absorbed into `beta`), (3) pays the **entire** common-plane edge and transverse tail, not only the exact-zero path endpoint:

`||p_Q||_infinity
 < 2 sqrt(pi) [L^2/(64 sqrt(896))]^(-1/2)
 = 16 sqrt(pi) 896^(1/4) / L
 = 155.157195638.../L.`                                         (4)

This complements partner r44: r44 allows an arbitrary hub function but requires zero light-light crossing; (4) allows an arbitrary light-light remainder but requires zero hub quadratic. The first unpaid implication is therefore sharpened to stability under the **nonzero 2x2 physical hub quadratic itself**, not stability under light-light leakage on this face.

In the no-pivot regime this remaining hub block is coefficient-small but may not be discarded for arbitrary fragmented/unbounded product laws. The final report will quantify that smallness and give a source-valid stress family.
