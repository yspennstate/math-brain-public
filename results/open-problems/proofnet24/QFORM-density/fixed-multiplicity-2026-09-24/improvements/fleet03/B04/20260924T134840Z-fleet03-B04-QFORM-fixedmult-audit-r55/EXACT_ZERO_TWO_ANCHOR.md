# QFORM exact-zero two-anchor affine receiver

Run: `20260924T134840Z-fleet03-B04-QFORM-fixedmult-audit-r55`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Status: **PROVED SUPPORTING LEMMA; does not close multiplicity eight.**

## Theorem `QFORM-EXACT-ZERO-TWO-ANCHOR-AFFINE-RECEIVER-v1`

Let `X=(X_H,Y)` have independent real coordinates with densities bounded by one, where `H={h_1,h_2}` consists of two literal original coordinates. Let

`Q=X^T A X+b^T X+c`

with arbitrary real symmetric `A`, arbitrary affine terms, and assume the physical principal block vanishes exactly:

`A[H,H]=0_(2x2)`.

Write

`C=A[H,H^c]`

and suppose `C` has row rank two. Put

`G=C C^T`.

Then `Q` has an essentially bounded density and

`||p_Q||_infinity <= e sqrt(2 pi) det(G)^(-1/4)`.

Numerically the front constant is

`e sqrt(2 pi)=6.813722089631097...`.

More locally, if `S,T subset H^c` are two-sets for which the displayed determinants are defined, then

`det(G) >= det A[H,S]^2+det A[H,T]^2 >= 2 |det A[H,S] det A[H,T]|`,

and hence

`||p_Q||_infinity <= e 2^(1/4) sqrt(pi) |det A[H,S] det A[H,T]|^(-1/4)`,

with front constant

`e 2^(1/4) sqrt(pi)=5.7296344797058385...`.

The theorem retains arbitrary curvature and affine terms on the entire complement `H^c`; no rotated random coordinates are declared independent.

## Proof

Because the `H x H` block is zero, after collecting all terms outside `H` into an arbitrary quadratic-affine polynomial `R(Y)`,

`Q = R(Y)+2 X_H . L(Y)`,

where

`L(Y)=C Y+b_H/2`.

Condition on the literal complement `Y`. For every value with `L(Y) !=0`, the baseline one-dimensional product-projection estimate applied to the two independent physical coordinates `X_H` gives the linear form `L(Y).X_H` a density bounded by

`sqrt(e)/|L(Y)|`.

The factor two in `2 L.X_H` therefore gives the conditional density domination

`||p_(Q|Y)||_infinity <= sqrt(e)/(2|L(Y)|)`.                    (1)

We now control the inverse radius without any moment hypothesis. Since `G=CC^T` is positive definite, set

`U=G^(-1/2) C`.

Then `U U^T=I_2`, so `U Y` is a two-dimensional orthogonal projection of the original product source. The baseline product-projection lemma gives its density the cap `e`. The invertible linear map `G^(1/2)` and translation by `b_H/2` therefore show that `L(Y)` has a two-dimensional density bounded by

`M=e/sqrt(det G)`.                                               (2)

In particular `P{L=0}=0`, so the exceptional conditional degeneracy has zero outer probability.

For any `r>0`, split the inverse-radius integral at radius `r`:

`E 1/|L|
 <= M int_(|z|<=r) |z|^(-1) dz + r^(-1) P{|L|>r}
 <= 2 pi M r + 1/r`.

Choose `r=(2 pi M)^(-1/2)`. Then

`E 1/|L| <= 2 sqrt(2 pi M)`.                                    (3)

Integrating the conditional measure domination (1) and using (2)--(3) yields

`||p_Q||_infinity
 <= (sqrt(e)/2) E 1/|L|
 <= sqrt(2 pi e M)
 <= e sqrt(2 pi) det(G)^(-1/4)`.

This proves the first assertion as an essential-density bound. It does not assert continuity.

Finally Cauchy--Binet gives

`det(CC^T)=sum_(|U|=2) det(C[:,U])^2`.

Therefore any two physical two-column minors contribute

`det(G)>=u^2+v^2>=2|uv|`,

where `u=det A[H,S]`, `v=det A[H,T]`. Substitution into the preceding estimate gives the local two-sided-collar form.

## Relation to the current multiplicity-eight collar

The current eight-direction reduction produces aggregate two-sided currency

`Xi_2=sum_(S,H,T) det A[S,H]^2 det A[H,T]^2`

and allows the common anchor diagonal entries to be zero or arbitrarily small. The theorem above rigorously pays a **single exact-zero 2x2 anchor block** when its outside cross map has rank two. It is useful because arbitrary complement curvature disappears after conditioning: the physical anchor remains purely affine.

It does **not** solve the current eight-direction theorem for two separate reasons:

1. the terminal anchor block is not forced to vanish as a full `2x2` matrix; small/nonzero indefinite anchor curvature reintroduces a moving logarithmic critical value that arbitrary complement curvature can correlate with;
2. the aggregate lower bound on `Xi_2` does not by itself force one local product `|det A[H,S] det A[H,T]|` bounded below independently of dimension. Selecting a tiny local collar and paying its reciprocal would lose the required universal constant.

Thus the still-open implication is an aggregate/masked collar receiver that spends the two-sided packet before local reciprocal payment, or an equivalent dependence-safe argument retaining the shifted product masks from the bilateral shear.