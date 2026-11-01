SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B06, 2026-09-22T18:24:19Z.

attacking: replace the false dimension-losing scalar/fiber supremum by an actually weighted curved-fiber integral, and test it on an exact product-law adversary.

# fleet02/B06 — scalar-conditioning falsifier, weighted curved-fiber repair, and grouped-bank comparison

Run `b06-20260922T182419Z-a73c8f1e`. Programme `QFORM-DENSITY-3EIG-20260922`. Classification: **ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED**. The full conjecture remains **OPEN / NOT PROVED**. Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source state and corrections consumed


Corrections used as hard constraints: law-uniform pointwise quadratic Fresnel decay is false; rotation does not preserve independence; unrestricted fiber suprema can lose dimension; arbitrary-joint 3D coarea with only an L-infinity density cap is false; fixed positive moments of vector-conditioned projection density can diverge; local good-minor/cross-rank dichotomies and direct Pluecker-pivot averaging can fail. No such statement is used below.

Assigned partner actually consumed: fleet03/B06 run `20260922T172229Z-fleet03-B06-qform-r14`, canonical source `yspennstate/math-open-problems@f0b750686f976524454cb490179785f5d764638a:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260922T172229Z-fleet03-B06-qform-r14/REPORT.md`, blob `570dac22bf2f5bdc800fb1be8595aeac2c3dd9b2`. Its theorem `QFORM-RANK3-GLOBAL-RANK1-SCHUR-AGGREGATION-v1` is applied quantitatively in Section 5.

A second complete supporting source is the arbitrary-rank physical-pair theorem `yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`, blob `d690b4e1e9f29a458c5ee7d8f2f107b98da64360`. It is pending independent review and is used only in its stated scope.

## 2. The stronger scalar-conditioning gate is false

The revision-.11 owner message proposes, for a three-large-eigenvalue core `Q3` and scalar spectral remainder `Q'`, to bound

`M = sup_b ||p_(Q3 | Q'=b)||_infinity`.

That gate is false even for four iid unit-density uniforms and a fixed 4 x 4 target matrix.

Let

`e=(1,1,1,1)/2`, `v=(1,-1,0,0)/sqrt(2)`, `P=I-ee^T`,

and define

`A3=P-2vv^T`, `A_alpha=A3+alpha ee^T`, `alpha=1/128`.

Then `A_alpha` has eigenvalues exactly `{1,1,-1,1/128}`: `v` has eigenvalue `-1`, two directions in `e^perp cap v^perp` have eigenvalue `1`, and `e` has eigenvalue `1/128`. Thus it is an exact target matrix with three eigenvalues of modulus one.

Take independent `X_i ~ Uniform[0,1]`. Put

`S=sum_i X_i`, `Q3=X^T A3 X`, `Q'=alpha(e.X)^2=alpha S^2/4`.

For `0<s<1`, conditioning on `S=s` gives the uniform measure on the intrinsic 3-simplex

`{x_i>=0, sum x_i=s}=s Delta_3`.

Write `X=sU`, with `U` uniform on `Delta_3={u_i>=0,sum u_i=1}`, and `c=(1,1,1,1)/4`. Since `A3 e=0`,

`Q3 = s^2 T(U)`,

where on the three-dimensional hyperplane `e^perp`, after an orthogonal change of coordinates,

`T(U)=y_1^2+y_2^2-y_3^2`, `y=U-c`.

The simplex has intrinsic volume `1/3`, hence `U` has intrinsic density `3`. Also `||U-c||^2<=3/4`, so `T` is supported in an interval of length at most `3/2`. Its law is absolutely continuous by coarea: the only ambient critical point of the nondegenerate quadratic restriction is the simplex centre, a null point. Therefore

`||p_T||_infinity >= 2/3`.

Scaling gives, for every `0<s<1`,

`||p_(Q3 | S=s)||_infinity = s^(-2) ||p_T||_infinity >= 2/(3s^2)`.      (2.1)

Since `Q'=alpha s^2/4` is one-to-one in `s>0`, conditioning on `Q'=alpha s^2/4` is the same regular conditional law as conditioning on `S=s`. Hence

`ess sup_b ||p_(Q3 | Q'=b)||_infinity = infinity`.                     (2.2)

This is a genuine Boolean falsifier to the proposed uniform scalar-conditioning supremum. It does **not** refute QFORM.

## 3. Curvature is bounded once the scalar-fiber probability weight is retained

The same example gives the correct repair explicitly.

### Lemma 3.1 — hyperbolic trace in a 3-ball

For `q(y)=y_1^2+y_2^2-y_3^2` and every `R>0,t in R`,

`integral_{|y|<=R} delta(q(y)-t) dy <= 2 pi R`.                       (3.1)

Proof: in cylindrical coordinates `(r,theta,z)`, the inner integral is

`integral_0^{sqrt(R^2-z^2)} 2 pi r delta(r^2-z^2-t) dr <= pi`.

Integrating over `-R<=z<=R` gives (3.1). QED.

For `Delta_3-c`, `R=sqrt(3)/2`, so with intrinsic density `3`,

`||p_T||_infinity <= 3 pi sqrt(3)`.                                  (3.2)

Consequently, for `0<s<1`,

`M_s := ||p_(Q3 | S=s)||_infinity <= 3 pi sqrt(3)/s^2`.               (3.3)

The same bound with `(4-s)^(-2)` holds for `3<s<4` by replacing `X` by `1-X`.

For `1<=s<=3`, the Irwin-Hall density of `S` satisfies `f_S(s)>=1/6`. In orthogonal coordinates `(y,e.X)`, the conditional density of `y=PX` given `S=s` is uniform on the physical cube slice with density at most

`1/(2 f_S(s)) <= 3`.

That slice lies in the ball `|y|<=3/2`. Lemma 3.1 therefore gives

`M_s <= 9 pi`, `1<=s<=3`.                                            (3.4)

### Lemma 3.2 — weighted scalar conditional sufficiency

For any decomposition `Q=U+V` for which the regular conditional laws `U|V=b` have densities, set `M(b)=||p_(U|V=b)||_infinity`. Then

`||p_Q||_infinity <= integral M(b) d law(V)(b)`.                      (3.5)

This is just disintegration:

`p_Q(t)=integral p_(U|V=b)(t-b) d law(V)(b)`.

Thus the correct sufficient interface is a probability-weighted conditional envelope, not `sup_b M(b)`.

For the exact adversary above, because `Q'=alpha S^2/4` is one-to-one on `S in (0,4)`,

`integral M(b) d law(Q')(b) = integral_0^4 M_s f_S(s) ds`.            (3.6)

On `0<s<1`, `f_S(s)=s^3/6`, so (3.3) gives

`integral_0^1 M_s f_S(s) ds <= pi sqrt(3)/4`.

The opposite corner contributes the same amount. The middle slice has probability `11/12`, so (3.4) gives at most `9 pi * 11/12 = 33 pi/4`. Therefore

`integral M(b) d law(Q')(b)
 <= pi(33/4 + sqrt(3)/2)
 < 29`.                                                              (3.7)

In particular, the exact instance whose scalar conditional **supremum is infinite** nevertheless satisfies

`||p_(X^T A_alpha X)||_infinity < 29`                                 (3.8)

by retaining the true product/slice probability weights. The corner mechanism is transparent: normalized curved-fiber density blows up like `s^(-2)`, while the product-law slice weight is `s^3/6`; their product is only order `s` and is integrable.

I call (3.5) together with this exact compensation mechanism `QFORM-WEIGHTED-SCALAR-CURVED-FIBER-v1`. A full proof would need a uniform weighted-envelope theorem for arbitrary product laws and arbitrary remaining spectrum; (3.7) establishes the mechanism on a source-valid exact target stress family and disproves the stronger supremum gate.

## 4. The falsifier is not hiding a target counterexample

For the full matrix `A_alpha`, the physical principal pair on coordinates `{1,3}` is

`H=(1/512) [[-127,-127],[-127,385]]`.

Thus

`det H=-127/512`, `D=127/512>1/5`, and `trace H=129/256`.

For this indefinite 2 x 2 matrix, the inequality

`4D > trace(H)+1/4`

is exactly sufficient to give `sigma_min(H)>1/4`; here it reads `127/128>193/256`. Also `s_3(A_alpha)=1`. The complete arbitrary-rank pair theorem cited in Section 1 therefore gives, for **arbitrary independent cap-one inputs**, not merely uniforms,

`||p_(X^T A_alpha X)||_infinity
 <= 3*400^(1/3)*(D^2 kappa)^(-1/6)
 < 3*400^(1/3)*100^(1/6)
 < 48`.                                                              (4.1)

This independent source-valid certificate confirms that (2.2) is failure of a proof interface, not evidence against the conjecture.

## 5. Assigned-partner theorem applied, and why grouping must precede reciprocal pair payment

Apply fleet03/B06's completed exact-rank-three theorem to the core `A3`. For the same pair `{1,3}`, the core scalar entry is `r=-1/4`. If `R` is any orthonormal spectral frame for `e^perp`, then `RR^T=P`, hence

`Delta_13=P_11 P_33-P_13^2=(3/4)^2-(-1/4)^2=1/2`.

Also `|det Lambda|=1`. The partner theorem gives the real inequality

`||p_(X^T A3 X)||_infinity
 <=16 sqrt(15) 2^(1/4) (1/8)^(-1/4)
 <124`                                                              (5.1)

for every independent cap-one input law. This is a direct application of the named partner result in exactly its proved scope.

Now compare the standard exact-rank-three stress family

`A_m = [1] direct_sum (J_m/m) direct_sum (-J_m/m)`.

Its spectral form is

`Q=X_0^2 + Y_+^2 - Y_-^2`,
`Y_+=m^(-1/2) sum_{k=1}^m X_k^+`,
`Y_-=m^(-1/2) sum_{k=1}^m X_k^-`,

with the three coordinate banks independent. Selecting the singleton and one negative-bank physical coordinate gives the partner resource

`|r| |det Lambda| Delta = 1/m`,

so (5.1)'s local-pair mechanism alone costs `m^(1/4)`.

But group the independent bank **before** paying reciprocal curvature. Rogozin--Ball gives

`||p_(Y_+)||_infinity, ||p_(Y_-)||_infinity <= sqrt(2)`.

For any scalar `Z` with density cap `M`, the density of `Z^2` is at most `M y^(-1/2)` for `y>0`. Therefore the two independent same-sign terms `X_0^2` and `Y_+^2` have convolution density at most

`pi sqrt(2)`

by the beta integral. Convolution with the independent law of `-Y_-^2` cannot raise the supremum. Hence

`||p_(X^T A_m X)||_infinity <= pi sqrt(2)` for every `m`.             (5.2)

More generally, if an exact-rank-three spectral frame has three disjoint original-coordinate supports, then its three spectral projections are independent and each has density cap at most `sqrt(2)`; choosing the unavoidable same-sign eigenpair gives the uniform bound `2 pi`. I call this `QFORM-DISJOINT-SPECTRAL-BANK-GROUPING-v1`.

Equations (5.1)-(5.2) quantify the partner's own stated next step: reciprocal physical-pair curvature can be dimension-losing even when grouped product structure is uniformly strong. Aggregation must occur before or jointly with the curvature inversion.

## 6. Conditional end-to-end route and first unpaid implication

A corrected conditional route is now:

1. choose a three-large-eigenvalue spectral core `Q3` and scalar/spectral remainder `Q'` without asserting post-rotation independence;
2. disintegrate only at the scalar level and retain the actual weight `d law(Q')`;
3. prove a universal bound on the weighted envelope

`W := integral ||p_(Q3 | Q'=b)||_infinity d law(Q')(b)`;              (6.1)

4. then (3.5) gives the full target density bound.

The first essential missing implication is therefore not the refuted `sup_b` statement but:

`QFORM-WEIGHTED-SCALAR-ENVELOPE-GLOBAL-v1`: prove a dimension-free bound for (6.1), or replace it by a still more coupled product-weighted curved trace, using original-coordinate grouping / pair-log / ridge mechanisms before normalization.

The exact adversary proves that any successful statement must allow conditional normalized fiber densities to diverge like inverse square while compensating them with the vanishing probability of those fibers. The singleton-plus-two-banks calculation proves that it must also permit distributed curvature to be grouped before any reciprocal local minor is paid.

No full-QFORM proof is claimed.

## 7. Exact checker

`CHECK.py` in this immutable run folder was executed in this invocation. It verifies with exact rational arithmetic the spectrum certificate, the physical-pair determinant and `kappa>1/4` inequality, the partner-core resource, the `<29` weighted envelope constant, the divergent conditional-sup lower bounds, the `<48` full-matrix pair certificate, and the `m^(1/4)` versus `pi sqrt(2)` bank comparison.

Executed-code SHA-256: `09784e893d25347e36d8ec3c5ddbf98f3dc2664939442697e091eb2c426d6f2e`.
Output SHA-256: `27abeb3c3a81e181abd0a601a287f81d6c31362ed756d5e9e3226f03640a87d6`.
