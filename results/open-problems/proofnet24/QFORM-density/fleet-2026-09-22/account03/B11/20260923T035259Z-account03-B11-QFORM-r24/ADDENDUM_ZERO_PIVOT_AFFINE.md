# Addendum — affine-stable exact zero-pivot lift

This addendum applies and slightly extends the source-valid exact-null scalar/dependent-pair kernel from

`yspennstate/math-open-problems@5bf3d5e6765ecd1dd091fc7d862f6f04211c530f`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260922T232932Z-account02-B16-QFORM-auto11/REPORT.md`.

That source proves the weak-`L^(3/2)` estimate for

`2 beta X C + alpha C^2+2 delta C D+gamma D^2`

when `X` is genuinely independent of the possibly dependent pair `(C,D)`, `||p_(C,D)||_infinity<=M`, and `beta gamma!=0`:

`||p_Q||_infinity <=3(2M)^(2/3)|beta^2 gamma|^(-1/3)`.            (Z.1)

The present observation is that the same proof is completely stable under the arbitrary affine terms created by outside original-coordinate conditioning.

## Z.1 Affine null-scalar theorem

Let `X` have density at most one and be independent of a pair `(C,D)` with joint probability density bounded by `M`. Let `beta gamma!=0`. For arbitrary real coefficients define

`Q=2 beta X C + alpha C^2+2 delta C D+gamma D^2
   +2 r X+2u C+2v D+c0`.                                         (Z.2)

Then

`boxed:
 ||p_Q||_infinity <=3(2M)^(2/3)|beta^2 gamma|^(-1/3).`            (Z.3)

### Proof

First translate the pair coordinate

`C'=C+r/beta`.                                                     (Z.4)

This is a determinant-one translation, so the pair density cap remains `M`, and it eliminates the scalar affine term:

`2 beta X C+2rX=2 beta X C'`.                                    (Z.5)

It only changes the coefficients of the affine terms in `(C',D)` and the scalar constant. Thus it suffices to allow arbitrary pair-affine terms in the source proof.

Condition on `(C,D)=(c,d)`. The map in `X` is affine with slope `2 beta c`, so for almost every target `t`,

`p_Q(t)=integral g(c,d) K_t(c,d) dc dd`,                           (Z.6)

where

`K_t(c,d)
 =[2|beta c|]^(-1)
 f((t-alpha c^2-2delta cd-gamma d^2-2u c-2v d-c0)/(2 beta c)).`   (Z.7)

If `K_t(c,d)>s`, then

`f(x_t(c,d))>2|beta|s|c|`,                                       (Z.8)

hence necessarily

`|c|<1/(2|beta|s)`.                                               (Z.9)

For fixed nonzero `c`, let `m=2|beta|s|c|` and `E_m={x:f(x)>m}`. Since `f` is a probability density,

`|E_m|<=1/m`.                                                      (Z.10)

As a function of `d`, `x_t(c,d)` is a quadratic whose leading coefficient is still exactly

`-gamma/(2 beta c)`.                                              (Z.11)

The added affine terms only move its vertex and target level. The source quadratic-preimage lemma is translation-uniform: for any measurable set `E` of length `L` and any nonzero quadratic leading coefficient `A`,

`|{d:A(d-d0)^2+w in E}|<=2 sqrt(L/|A|)`.                          (Z.12)

Using (Z.10)-(Z.12), the `d`-measure of the superlevel set at fixed `c` is at most

`2/[sqrt(|gamma|) sqrt(s)]`.                                      (Z.13)

Integrating over the `c` interval (Z.9) gives the unchanged weak-`L^(3/2)` estimate

`|{(c,d):K_t(c,d)>s}|
 <=2/(|beta|sqrt(|gamma|)) s^(-3/2).`                             (Z.14)

Now combine the pair density cap and probability normalization:

`P_g(K_t>s)
 <=min{1, [2M/(|beta|sqrt(|gamma|))]s^(-3/2)}`.                   (Z.15)

Layer cake yields

`p_Q(t)
 <=3[2M/(|beta|sqrt(|gamma|))]^(2/3)`
` =3(2M)^(2/3)|beta^2 gamma|^(-1/3)`.                             (Z.16)

This proves (Z.3). QED.

## Z.2 Original-coordinate zero physical pivot

Let `H` be an invertible ORIGINAL-coordinate physical `3x3` block and suppose one physical diagonal is exactly zero. Relabel so

`H=[[0,b^T],[b,C]]`.                                              (Z.17)

Invertibility forces `b!=0`. Apply an orthogonal transformation **only to the deterministic two-dimensional pair coordinates in the analysis**, aligning

`b -> (beta,0)`, `beta=||b||`.                                    (Z.18)

The transformed pair law need not have independent coordinates, but its two-dimensional density cap is unchanged because the orthogonal map has Jacobian one. In this basis

`H'=[[0,beta,0],[beta,alpha,delta],[0,delta,gamma]]`,             (Z.19)

and

`det H=-beta^2 gamma`.                                            (Z.20)

Hence `gamma!=0`. Conditioning every outside original coordinate creates precisely the affine terms allowed by (Z.2). With the original pair density cap `M=1`, (Z.3) gives the full-ambient target-level estimate

`boxed:
 ||p_{X^T A X}||_infinity
 <=3*2^(2/3)|det H|^(-1/3).`                                     (Z.21)

This is `QFORM-ZERO-PHYSICAL-PIVOT-AFFINE-v1`.

No post-rotation independence is asserted: the pair is explicitly allowed to become dependent after the deterministic orthogonal change, and only its joint density cap is used.

## Z.3 Exact zero-diagonal rotated endpoint

For

`H0=[[0,1,1],[1,0,1],[1,1,0]]`,                                  (Z.22)

one has spectrum `{2,-1,-1}` and `det H0=2`. Thus arbitrary independent cap-one inputs satisfy

`||p_{X^T H0 X}||_infinity
 <=3*2^(1/3)
 =3.7797631496... .`                                              (Z.23)

Every physical diagonal is zero, so none of the nonzero-pivot estimates in the main report or first addendum applies. The weak-`L^(3/2)` null mechanism is therefore genuinely complementary.

The rank-two control remains logarithmically singular. The third direction removes it here because the scalar-linear coupling plus the transverse pair curvature gives a weak-`L^(3/2)` kernel in two pair variables; its layer cake is integrable, whereas the rank-two analogue is at the logarithmic endpoint.

## Z.4 Combined scalar/pair compiler

For any invertible indefinite ORIGINAL-coordinate physical triple `H`, the scalar/pair completion is now exhaustive at the level of a chosen physical pivot:

- if `a=H_ii!=0` and has minority sign, use the sharp elliptic discriminant bound `2sqrt(pi)|a det H|^(-1/4)`;
- if `a!=0` and has majority sign, use the rank-two half-Riesz receiver `16sqrt(30)|a det H|^(-1/4)`;
- if `a=0`, use the affine null-scalar weak-`L^(3/2)` bound `3*2^(2/3)|det H|^(-1/3)`.

These are **local compilers**, not a full solution: the bare three-large-eigenvalue hypothesis does not force one physical triple with uniformly quantitative determinant/pivot currency. The global remaining work is still aggregate-before-inversion in the hidden-minority balanced near-rank-one/no-pivot chamber.

Continuity is not claimed for the null-pivot theorem.
